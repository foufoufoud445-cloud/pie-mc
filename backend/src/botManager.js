/**
 * Pie MC - Multi-Tenant Concurrent Bot Lifecycle Manager
 * Supports concurrent multi-user bot execution, proxy tunneling,
 * chat event loops, triggers, and automations isolated per user.
 */

const EventEmitter = require('events');
let mineflayer;
try {
  mineflayer = require('mineflayer');
} catch (e) {
  console.warn('[Pie MC Bot Manager] Mineflayer running in virtual simulation mode.');
}

const { SocksProxyAgent } = require('socks-proxy-agent');
const { HttpProxyAgent } = require('http-proxy-agent');

class BotInstance extends EventEmitter {
  constructor(userId, id, config, globalSettings) {
    super();
    this.userId = userId;
    this.id = id;
    this.compositeKey = `${userId}:${id}`;
    this.name = config.name || `Instance ${id}`;
    this.config = config;
    this.globalSettings = globalSettings;
    this.bot = null;
    this.status = 'offline';
    this.reconnectAttempts = 0;
    this.scheduledTimers = [];
    this.cooldowns = new Map();
  }

  start() {
    if (this.status === 'online' || this.status === 'connecting') return;
    this.status = 'connecting';
    this.emit('status', { userId: this.userId, instanceId: this.id, status: this.status });

    if (!mineflayer) {
      setTimeout(() => {
        this.status = 'online';
        this.emit('status', { userId: this.userId, instanceId: this.id, status: this.status });
        this.emit('chat', {
          time: new Date().toTimeString().split(' ')[0],
          player: 'SYSTEM',
          tag: '[SYSTEM]',
          msg: `Connected to ${this.config.server ? this.config.server.host : '127.0.0.1'}:${this.config.server ? this.config.server.port : 25565}`,
          type: 'system'
        });
      }, 800);
      return;
    }

    try {
      const hasToken = !!(this.config.account && this.config.account.rawToken);

      // Mineflayer/minecraft-protocol expects UUID WITHOUT dashes in selectedProfile.id
      const rawUuid = this.config.account && this.config.account.uuid ? this.config.account.uuid.replace(/-/g, '') : '';

      const botOptions = {
        host: (this.config.server && this.config.server.host) || '127.0.0.1',
        port: (this.config.server && this.config.server.port) || 25565,
        username: (this.config.account && this.config.account.username) || 'PieBot',
        version: (this.config.server && this.config.server.version) || '1.21.1',
        auth: hasToken ? 'microsoft' : 'microsoft',
        // haveCredentials tells minecraft-protocol to call sessionserver.mojang.com
        // to validate the token. Without this, online-mode servers reject the bot.
        haveCredentials: hasToken,
        accessToken: hasToken ? this.config.account.rawToken : undefined,
        session: hasToken ? {
          accessToken: this.config.account.rawToken,
          selectedProfile: {
            id: rawUuid,
            name: this.config.account.username
          },
          availableProfile: [{
            id: rawUuid,
            name: this.config.account.username
          }]
        } : undefined
      };

      console.log(`[BotManager] Starting bot "${botOptions.username}" -> ${botOptions.host}:${botOptions.port} (auth: ${hasToken ? 'token' : 'microsoft'}, uuid: ${rawUuid})`);

      // Proxy Routing per bot
      if (this.config.proxy && this.config.proxy.type !== 'Direct') {
        const proxyUri = `${this.config.proxy.type.toLowerCase()}://${this.config.proxy.host}:${this.config.proxy.port}`;
        if (this.config.proxy.type.startsWith('SOCKS')) {
          botOptions.agent = new SocksProxyAgent(proxyUri);
        } else {
          botOptions.agent = new HttpProxyAgent(proxyUri);
        }
      }

      this.bot = mineflayer.createBot(botOptions);

      // Timeout: if bot doesn't spawn in 30s, mark as failed
      const spawnTimeout = setTimeout(() => {
        if (this.status === 'connecting') {
          console.error(`[BotManager] Bot "${this.name}" timed out - never spawned (30s). Check server address, version, and token.`);
          this.status = 'offline';
          this.emit('status', { userId: this.userId, instanceId: this.id, status: this.status });
          this.emit('log', { instance: this.name, event: 'Timeout', details: 'Bot did not spawn within 30 seconds. Check server, version, and token.' });
          try { this.bot.quit(); } catch(e) {}
          this.bot = null;
        }
      }, 30000);

      this.bot.on('login', () => {
        console.log(`[BotManager] Bot "${this.name}" logged in successfully, waiting for spawn...`);
      });

      this.bot.on('spawn', () => {
        clearTimeout(spawnTimeout);
        this.status = 'online';
        this.reconnectAttempts = 0;
        console.log(`[BotManager] Bot "${this.name}" spawned and ready!`);
        this.emit('status', { userId: this.userId, instanceId: this.id, status: this.status });
        this.emit('chat', {
          time: new Date().toTimeString().split(' ')[0],
          player: 'SYSTEM',
          tag: '[SYSTEM]',
          msg: `Connected to ${botOptions.host}:${botOptions.port} as ${botOptions.username}`,
          type: 'system'
        });
        this.startAutomations();
      });

      this.bot.on('chat', (username, message) => {
        if (username === this.bot.username) return;
        const time = new Date().toTimeString().split(' ')[0];
        this.emit('chat', { time, player: username, tag: '[CHAT]', msg: message, type: 'chat' });
        this.evaluateTriggers(username, message);
      });

      this.bot.on('kicked', (reason) => {
        clearTimeout(spawnTimeout);
        console.warn(`[BotManager] Bot "${this.name}" kicked:`, JSON.stringify(reason));
        this.emit('chat', { time: new Date().toTimeString().split(' ')[0], player: 'SYSTEM', tag: '[KICKED]', msg: `Kicked: ${typeof reason === 'string' ? reason : JSON.stringify(reason)}`, type: 'system' });
        this.emit('log', { instance: this.name, event: 'Kicked', details: JSON.stringify(reason) });
        this.status = 'offline';
        this.emit('status', { userId: this.userId, instanceId: this.id, status: this.status });
      });

      this.bot.on('error', (err) => {
        console.error(`[BotManager] Bot "${this.name}" error:`, err.message);
        this.emit('chat', { time: new Date().toTimeString().split(' ')[0], player: 'SYSTEM', tag: '[ERROR]', msg: err.message, type: 'system' });
        this.emit('log', { instance: this.name, event: 'Error', details: err.message });
      });

      this.bot.on('end', (reason) => {
        clearTimeout(spawnTimeout);
        console.log(`[BotManager] Bot "${this.name}" disconnected: ${reason}`);
        this.emit('chat', { time: new Date().toTimeString().split(' ')[0], player: 'SYSTEM', tag: '[DISCONNECT]', msg: `Disconnected: ${reason}`, type: 'system' });
        this.handleDisconnect();
      });

    } catch (err) {
      this.status = 'offline';
      this.emit('status', { userId: this.userId, instanceId: this.id, status: this.status });
      this.emit('log', { instance: this.name, event: 'Connection Failed', details: err.message });
    }
  }

  stop() {
    this.clearAutomations();
    this.status = 'offline';
    this.reconnectAttempts = 0;
    if (this.bot) {
      try { this.bot.quit(); } catch (e) {}
      this.bot = null;
    }
    this.emit('status', { userId: this.userId, instanceId: this.id, status: this.status });
  }

  handleDisconnect() {
    this.clearAutomations();
    if (this.globalSettings.autoReconnect && (this.globalSettings.maxAttempts === 0 || this.reconnectAttempts < this.globalSettings.maxAttempts)) {
      this.status = 'reconnecting';
      this.reconnectAttempts++;
      this.emit('status', { userId: this.userId, instanceId: this.id, status: this.status });
      setTimeout(() => {
        if (this.status === 'reconnecting') this.start();
      }, (this.globalSettings.retryDelay || 10) * 1000);
    } else {
      this.status = 'offline';
      this.emit('status', { userId: this.userId, instanceId: this.id, status: this.status });
    }
  }

  sendChat(message) {
    if (this.bot && this.status === 'online') {
      this.bot.chat(message);
    }
    const time = new Date().toTimeString().split(' ')[0];
    this.emit('chat', {
      time,
      player: (this.config.account && this.config.account.username) || 'PieBot',
      tag: '[BOT]',
      msg: message,
      type: 'bot'
    });
  }

  evaluateTriggers(player, message) {
    if (!this.config.triggers) return;
    const now = Date.now();

    for (const trigger of this.config.triggers) {
      if (!trigger.enabled) continue;

      let matches = false;
      if (trigger.match_mode === 'Exact match') {
        matches = message.toLowerCase() === trigger.keyword.toLowerCase();
      } else if (trigger.match_mode === 'Starts with') {
        matches = message.toLowerCase().startsWith(trigger.keyword.toLowerCase());
      } else if (trigger.match_mode === 'Regex') {
        try { matches = new RegExp(trigger.keyword, 'i').test(message); } catch (e) {}
      } else {
        matches = message.toLowerCase().includes(trigger.keyword.toLowerCase());
      }

      if (matches) {
        const cooldownKey = trigger.scope === 'Global' ? `global_${trigger.id}` : `${player}_${trigger.id}`;
        const lastExecuted = this.cooldowns.get(cooldownKey) || 0;
        if (now - lastExecuted < (trigger.cooldown * 1000)) continue;

        this.cooldowns.set(cooldownKey, now);
        const replyText = trigger.reply.replace(/{player}/g, player);

        if (replyText.startsWith('/')) {
          this.sendChat(replyText);
        } else {
          this.sendChat(`/msg ${player} ${replyText}`);
        }

        this.emit('log', {
          instance: this.name,
          event: 'Trigger Fired',
          player,
          details: `Rule: [${trigger.name}] -> ${replyText}`
        });
      }
    }
  }

  startAutomations() {
    this.clearAutomations();
    if (!this.config.automations) return;

    for (const auto of this.config.automations) {
      if (!auto.enabled) continue;
      const intervalMs = (auto.interval_seconds || 60) * 1000;
      const timer = setInterval(() => {
        if (this.status === 'online') {
          this.sendChat(auto.message);
          this.emit('log', {
            instance: this.name,
            event: 'Automation Fired',
            player: 'SYSTEM',
            details: `Broadcast: ${auto.message}`
          });
        }
      }, intervalMs);
      this.scheduledTimers.push(timer);
    }
  }

  clearAutomations() {
    for (const timer of this.scheduledTimers) {
      clearInterval(timer);
    }
    this.scheduledTimers = [];
  }
}

class BotManager {
  constructor() {
    this.instances = new Map(); // compositeKey -> BotInstance
    this.globalSettings = {
      autoReconnect: true,
      retryDelay: 10,
      maxAttempts: 5,
      silenceTimeout: 120
    };
  }

  getOrCreateInstance(userId, id, config) {
    const key = `${userId || 'default'}:${id}`;
    if (!this.instances.has(key)) {
      const instance = new BotInstance(userId || 'default', id, config, this.globalSettings);
      this.instances.set(key, instance);
    } else {
      // Update config when instance already exists (e.g. user changed account/server)
      const existing = this.instances.get(key);
      if (config && Object.keys(config).length > 0) {
        existing.config = { ...existing.config, ...config };
        existing.name = config.name || existing.name;
      }
    }
    return this.instances.get(key);
  }

  stopAll() {
    for (const inst of this.instances.values()) {
      inst.stop();
    }
  }
}

module.exports = new BotManager();
