import os

PUB = '/working_dir/c_37017e0a3b8a7bd1/pie-mc/public'
BACK = '/working_dir/c_37017e0a3b8a7bd1/pie-mc/backend'

# 1. SHARED.JS
shared_js = '''/**
 * Pie MC - Client Engine & State Store
 * Hand-crafted multi-tenant Minecraft bot management dashboard.
 * Supports per-instance console isolation, multi-instance automation assignment,
 * and 48-hour log retention & cleanup.
 */

const ICONS = {
  dashboard: `<svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="9"></rect><rect x="14" y="3" width="7" height="5"></rect><rect x="14" y="12" width="7" height="9"></rect><rect x="3" y="16" width="7" height="5"></rect></svg>`,
  chat: `<svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>`,
  accounts: `<svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle><path d="M23 21v-2a4 4 0 0 0-3-3.87"></path><path d="M16 3.13a4 4 0 0 1 0 7.75"></path></svg>`,
  servers: `<svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="8" rx="2" ry="2"></rect><rect x="2" y="14" width="20" height="8" rx="2" ry="2"></rect><line x1="6" y1="6" x2="6.01" y2="6"></line><line x1="6" y1="18" x2="6.01" y2="18"></line></svg>`,
  proxies: `<svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>`,
  automation: `<svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>`,
  triggers: `<svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>`,
  discord: `<svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M8 12a2 2 0 1 0 4 0 2 2 0 1 0-4 0"></path><path d="M14 12a2 2 0 1 0 4 0 2 2 0 1 0-4 0"></path></svg>`,
  logs: `<svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line></svg>`,
  settings: `<svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"></circle><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path></svg>`,
  admin: `<svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg>`,
  logout: `<svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path><polyline points="16 17 21 12 16 7"></polyline><line x1="21" y1="12" x2="9" y2="12"></line></svg>`,
  plus: `<svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>`,
  trash: `<svg class="w-3.5 h-3.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg>`
};

const OWNER_DISCORD_ID = '987654321098765432';

const DEFAULT_PLATFORM_FLAGS = {
  allowUserChangeVersion: true,
  lockedVersion: '1.21.1',
  allowAutoReconnect: true,
  allowNewRegistrations: true,
  autoCleanup48h: true, // 48-Hour Log Cleanup Toggle
  databaseMode: 'sqlite',
  tursoUrl: '',
  tursoToken: '',
  sqlitePath: 'backend/data/pie-mc.db',
  jsonStorePath: 'backend/data/json_store/'
};

window.getPlatformFlags = function() {
  try {
    const raw = localStorage.getItem('PIE_MC_PLATFORM_FLAGS');
    if (raw) return JSON.parse(raw);
  } catch (e) {}
  return DEFAULT_PLATFORM_FLAGS;
};

window.savePlatformFlags = function(flags) {
  try {
    localStorage.setItem('PIE_MC_PLATFORM_FLAGS', JSON.stringify(flags));
  } catch (e) {}
};

function checkAuth() {
  const path = window.location.pathname;
  const isLoginPage = path.endsWith('login.html') || path.endsWith('404.html');
  const user = getCurrentUser();

  if (!user && !isLoginPage) {
    window.location.href = 'login.html';
    return null;
  }
  return user;
}

function getCurrentUser() {
  try {
    const raw = localStorage.getItem('PIE_MC_USER');
    if (raw) return JSON.parse(raw);
  } catch (e) {}
  return null;
}

function setCurrentUser(user) {
  if (user) {
    localStorage.setItem('PIE_MC_USER', JSON.stringify(user));
  } else {
    localStorage.removeItem('PIE_MC_USER');
  }
}

function logout() {
  setCurrentUser(null);
  window.location.href = 'login.html';
}

function getStorageKey() {
  const user = getCurrentUser();
  return user ? `PIE_MC_DATA_${user.id}` : 'PIE_MC_DATA_GUEST';
}

function getDefaultUserData(username) {
  const now = Date.now();
  const H = 3600 * 1000;

  return {
    activeInstanceId: 1,
    instances: [
      { id: 1, name: 'Instance 1', status: 'online', account: `${username}_Bot1`, server: 'Hypixel Network', proxy: 'US Residential 01' },
      { id: 2, name: 'Instance 2', status: 'offline', account: `${username}_Bot2`, server: '2b2t Anarchy', proxy: 'EU SOCKS5 Node' },
      { id: 3, name: 'Instance 3', status: 'online', account: `${username}_Bot3`, server: 'Localhost Test', proxy: 'Auto' }
    ],
    accounts: [
      { 
        id: '1', 
        username: `${username}_Bot1`, 
        uuid: 'd8f3-4a11-98bc-e63f912', 
        status: 'authenticated', 
        added: '2026-08-28', 
        expiresAt: new Date(now + 24 * H).toISOString(),
        tokenExpiryStatus: 'valid'
      },
      { 
        id: '2', 
        username: `${username}_Bot2`, 
        uuid: 'e712-3b99-11aa-a82f331', 
        status: 'needs_reauth', 
        added: '2026-08-20', 
        expiresAt: new Date(now - 2 * H).toISOString(),
        tokenExpiryStatus: 'needs_reauth'
      }
    ],
    servers: [
      { id: '1', name: 'Hypixel Network', host: 'mc.hypixel.net', port: 25565, players: '48,219/100,000', ping: '24ms', status: 'online' },
      { id: '2', name: '2b2t Anarchy', host: '2b2t.org', port: 25565, players: '250/250 (Queue: 412)', ping: '68ms', status: 'online' },
      { id: '3', name: 'Localhost Test', host: '127.0.0.1', port: 25565, players: '1/20', ping: '1ms', status: 'online' }
    ],
    proxies: [
      { id: '1', name: 'US Residential 01', type: 'SOCKS5', host: '142.93.18.22', port: 1080, auth: 'user:pass', latency: '42ms' },
      { id: '2', name: 'EU SOCKS5 Node', type: 'SOCKS5', host: '178.62.204.11', port: 1080, auth: 'None', latency: '65ms' }
    ],
    automations: [
      { 
        id: '1', 
        msg: '/clan recruit Join Pie Squad for top rewards!', 
        interval: '60 seconds', 
        status: true, 
        targetInstances: [1, 2] // Multi-instance scope
      },
      { 
        id: '2', 
        msg: 'Pie MC Bot Online - Type !help for commands', 
        interval: '5 minutes', 
        status: true, 
        targetInstances: ['all'] // All instances
      }
    ],
    triggers: [
      { id: '1', name: 'Welcome Greeter', keyword: 'hello', mode: 'Keyword anywhere', reply: 'Welcome! /msg me for help', cooldown: 10, status: true },
      { id: '2', name: 'Discord Link', keyword: '!discord', mode: 'Exact match', reply: 'Join discord.gg/piemc', cooldown: 5, status: true }
    ],
    // 48-Hour Historical Activity Logs (Strictly keyed by instanceId)
    logs: [
      { id: 'l1', instanceId: 1, instanceName: 'Instance 1', timestamp: now - 5 * 60 * 1000, time: formatTime(now - 5 * 60 * 1000), date: formatDate(now - 5 * 60 * 1000), event: 'Bot Connected', player: `${username}_Bot1`, details: 'Connected to mc.hypixel.net:25565 via SOCKS5' },
      { id: 'l2', instanceId: 1, instanceName: 'Instance 1', timestamp: now - 45 * 60 * 1000, time: formatTime(now - 45 * 60 * 1000), date: formatDate(now - 45 * 60 * 1000), event: 'Trigger Fired', player: 'Alex_Pro', details: 'Auto-replied to !discord' },
      { id: 'l3', instanceId: 1, instanceName: 'Instance 1', timestamp: now - 6 * H, time: formatTime(now - 6 * H), date: formatDate(now - 6 * H), event: 'Scheduled Task', player: 'SYSTEM', details: 'Broadcasted clan recruitment message' },
      { id: 'l4', instanceId: 1, instanceName: 'Instance 1', timestamp: now - 23 * H, time: formatTime(now - 23 * H), date: formatDate(now - 23 * H), event: 'Server Join', player: `${username}_Bot1`, details: 'Spawned at lobby_42 (X: 0, Y: 64, Z: 0)' },
      { id: 'l5', instanceId: 1, instanceName: 'Instance 1', timestamp: now - 44 * H, time: formatTime(now - 44 * H), date: formatDate(now - 44 * H), event: 'Bot Started', player: 'SYSTEM', details: 'Initialized Mineflayer instance container' },
      
      { id: 'l6', instanceId: 2, instanceName: 'Instance 2', timestamp: now - 12 * H, time: formatTime(now - 12 * H), date: formatDate(now - 12 * H), event: 'Kicked by Server', player: `${username}_Bot2`, details: 'Server closed connection on 2b2t.org' },
      { id: 'l7', instanceId: 2, instanceName: 'Instance 2', timestamp: now - 36 * H, time: formatTime(now - 36 * H), date: formatDate(now - 36 * H), event: 'Queue Position', player: `${username}_Bot2`, details: 'Position in 2b2t queue: #142' },

      { id: 'l8', instanceId: 3, instanceName: 'Instance 3', timestamp: now - 2 * H, time: formatTime(now - 2 * H), date: formatDate(now - 2 * H), event: 'Bot Connected', player: `${username}_Bot3`, details: 'Joined Localhost Test (Ping: 1ms)' }
    ],
    // Console chat stream (Separated per instance)
    chatLogs: [
      { id: 'c1', instanceId: 1, time: formatTime(now - 30 * 1000), player: `${username}_Bot1`, tag: '[JOIN]', msg: 'Joined mc.hypixel.net successfully', type: 'system' },
      { id: 'c2', instanceId: 1, time: formatTime(now - 20 * 1000), player: 'Alex_Pro', tag: '[VIP+]', msg: '!discord', type: 'chat' },
      { id: 'c3', instanceId: 1, time: formatTime(now - 19 * 1000), player: `${username}_Bot1`, tag: '[BOT]', msg: 'Join our Discord: discord.gg/piemc', type: 'bot' },
      
      { id: 'c4', instanceId: 2, time: formatTime(now - 12 * H), player: 'SYSTEM', tag: '[DISCONNECT]', msg: 'Disconnected from 2b2t.org: Server restarting', type: 'system' },
      
      { id: 'c5', instanceId: 3, time: formatTime(now - 2 * H), player: `${username}_Bot3`, tag: '[JOIN]', msg: 'Connected to 127.0.0.1:25565', type: 'system' }
    ],
    discordRelay: [
      { time: formatTime(now - 20 * 1000), author: 'PieMC-Relay', content: '💬 **[Instance 1]** `<Alex_Pro>` !discord' }
    ]
  };
}

function formatTime(ts) {
  return new Date(ts).toTimeString().split(' ')[0];
}

function formatDate(ts) {
  return new Date(ts).toISOString().split('T')[0];
}

// 48-Hour Log Pruning Function
window.pruneLogsOlderThan48Hours = function() {
  const flags = getPlatformFlags();
  const maxAge = 48 * 3600 * 1000;
  const cutoff = Date.now() - maxAge;

  window.updatePieState(s => {
    const beforeCount = s.logs.length;
    s.logs = s.logs.filter(l => l.timestamp && l.timestamp >= cutoff);
    const purged = beforeCount - s.logs.length;
    return purged;
  });
};

function getStoredState() {
  const user = getCurrentUser();
  if (!user) return getDefaultUserData('Guest');

  try {
    const raw = localStorage.getItem(getStorageKey());
    if (raw) {
      const data = JSON.parse(raw);
      // Auto-prune if setting is on
      const flags = getPlatformFlags();
      if (flags.autoCleanup48h) {
        const cutoff = Date.now() - (48 * 3600 * 1000);
        data.logs = (data.logs || []).filter(l => l.timestamp && l.timestamp >= cutoff);
      }
      return data;
    }
  } catch (e) {}

  const defaultData = getDefaultUserData(user.username);
  localStorage.setItem(getStorageKey(), JSON.stringify(defaultData));
  return defaultData;
}

function saveState(newState) {
  try {
    localStorage.setItem(getStorageKey(), JSON.stringify(newState));
  } catch (e) {}
}

const state = getStoredState();

window.updatePieState = function(mutator) {
  mutator(state);
  saveState(state);
};

// Auto SSID Mojang Resolver
window.autoResolveSSID = async function(sessionToken) {
  if (!sessionToken || sessionToken.trim().length === 0) {
    throw new Error('Please enter a valid session token (SSID)');
  }

  const cleanToken = sessionToken.trim();
  let username = '';
  let uuid = '';

  try {
    if (cleanToken.includes('.')) {
      const parts = cleanToken.split('.');
      if (parts.length >= 2) {
        const payload = JSON.parse(atob(parts[1]));
        if (payload.extra && payload.extra.userName) username = payload.extra.userName;
        if (payload.sub) uuid = payload.sub;
        if (payload.name) username = payload.name;
      }
    }
  } catch (e) {}

  if (!username) {
    const hash = Array.from(cleanToken).reduce((s, c) => Math.imul(31, s) + c.charCodeAt(0) | 0, 0);
    const names = ['EnderSlayer', 'ViperCraft', 'PixelKnight', 'ShadowBot', 'PiePro', 'NovaStrike', 'AuraPlayer', 'FrostWalker'];
    const idx = Math.abs(hash) % names.length;
    username = `${names[idx]}_${Math.abs(hash % 900 + 100)}`;
    uuid = 'c' + Math.abs(hash).toString(16).padEnd(8, '0').slice(0, 8) + '-49f1-a1b2';
  }

  if (!uuid) {
    uuid = 'd' + Math.random().toString(16).substring(2, 10) + '-4a11-98bc';
  }

  const expiresAt = new Date(Date.now() + 24 * 60 * 60 * 1000).toISOString();

  return {
    username,
    uuid,
    avatar: `https://mc-heads.net/avatar/${username}/28`,
    expiresAt,
    tokenExpiryStatus: 'valid'
  };
};

window.reauthAccountSSID = async function(accountId, newSSID) {
  const profile = await window.autoResolveSSID(newSSID);
  
  window.updatePieState(s => {
    const acc = s.accounts.find(a => a.id === accountId);
    if (acc) {
      acc.status = 'authenticated';
      acc.tokenExpiryStatus = 'valid';
      acc.expiresAt = profile.expiresAt;
      s.logs.unshift({
        id: 'l_' + Date.now(),
        instanceId: s.activeInstanceId || 1,
        instanceName: 'Instance ' + (s.activeInstanceId || 1),
        timestamp: Date.now(),
        time: formatTime(Date.now()),
        date: formatDate(Date.now()),
        event: 'Account Re-Authed',
        player: acc.username,
        details: 'Fresh Microsoft OAuth SSID token installed'
      });
    }
  });

  return profile;
};

// Custom Glassmorphic Confirmation Modal
window.showConfirmModal = function({ title, message, confirmText = 'Confirm', cancelText = 'Cancel', onConfirm, isDanger = true }) {
  let modalEl = document.getElementById('globalConfirmModal');
  if (!modalEl) {
    modalEl = document.createElement('div');
    modalEl.id = 'globalConfirmModal';
    modalEl.className = 'fixed inset-0 z-50 bg-black/80 backdrop-blur-sm hidden items-center justify-center p-4';
    document.body.appendChild(modalEl);
  }

  modalEl.innerHTML = `
    <div class="pie-card p-6 max-w-md w-full space-y-4 border border-[#1c2333] shadow-2xl">
      <div class="flex items-center space-x-3">
        <div class="w-10 h-10 rounded-xl ${isDanger ? 'bg-red-500/10 text-red-400 border border-red-500/30' : 'bg-[#2cf5d6]/10 text-[#2cf5d6] border border-[#2cf5d6]/30'} flex items-center justify-center">
          ${isDanger ? ICONS.trash : ICONS.dashboard}
        </div>
        <div>
          <h3 class="text-base font-bold text-white">${title}</h3>
          <p class="text-xs text-slate-400 font-mono mt-0.5">Please confirm your action</p>
        </div>
      </div>

      <p class="text-xs text-slate-300 leading-relaxed bg-[#0a0d14] p-3 rounded-lg border border-[#1c2333]">
        ${message}
      </p>

      <div class="flex items-center justify-end space-x-3 pt-2">
        <button id="btnConfirmCancel" class="btn-secondary text-xs px-4 py-2">${cancelText}</button>
        <button id="btnConfirmOk" class="${isDanger ? 'btn-danger' : 'btn-primary'} text-xs px-4 py-2">${confirmText}</button>
      </div>
    </div>
  `;

  modalEl.classList.remove('hidden');
  modalEl.classList.add('flex');

  document.getElementById('btnConfirmCancel').onclick = () => {
    modalEl.classList.add('hidden');
    modalEl.classList.remove('flex');
  };

  document.getElementById('btnConfirmOk').onclick = () => {
    modalEl.classList.add('hidden');
    modalEl.classList.remove('flex');
    if (onConfirm) onConfirm();
  };
};

window.deleteInstancePrompt = function(id, name, e) {
  if (e) e.stopPropagation();

  if (state.instances.length <= 1) {
    window.showConfirmModal({
      title: 'Cannot Delete Instance',
      message: 'You must have at least one active bot instance in your workspace.',
      confirmText: 'Understood',
      cancelText: 'Close',
      isDanger: false
    });
    return;
  }

  window.showConfirmModal({
    title: `Delete ${name}?`,
    message: `Are you sure you want to delete <strong>${name}</strong>? This will stop the bot and remove its configuration.`,
    confirmText: 'Delete Instance',
    cancelText: 'Keep Instance',
    isDanger: true,
    onConfirm: () => {
      window.updatePieState(s => {
        s.instances = s.instances.filter(i => i.id !== id);
        if (s.activeInstanceId === id) {
          s.activeInstanceId = s.instances[0] ? s.instances[0].id : 1;
        }
      });
      window.location.reload();
    }
  });
};

// Global Clean Header
window.renderGlobalHeader = function(activePage) {
  const user = checkAuth();
  if (!user && !window.location.pathname.endsWith('login.html') && !window.location.pathname.endsWith('404.html')) return;

  const isOwner = user && (user.id === OWNER_DISCORD_ID || user.isOwner);

  const pages = [
    { id: 'dashboard', label: 'Dashboard', href: 'dashboard.html', icon: ICONS.dashboard },
    { id: 'chat', label: 'Chat', href: 'chat.html', icon: ICONS.chat },
    { id: 'accounts', label: 'Accounts', href: 'accounts.html', icon: ICONS.accounts },
    { id: 'servers', label: 'Servers', href: 'servers.html', icon: ICONS.servers },
    { id: 'proxies', label: 'Proxies', href: 'proxies.html', icon: ICONS.proxies },
    { id: 'automation', label: 'Automation', href: 'automation.html', icon: ICONS.automation },
    { id: 'triggers', label: 'Triggers', href: 'triggers.html', icon: ICONS.triggers },
    { id: 'discord', label: 'Discord', href: 'discord.html', icon: ICONS.discord },
    { id: 'logs', label: 'Logs', href: 'logs.html', icon: ICONS.logs }
  ];

  if (isOwner) {
    pages.push({ id: 'admin', label: 'Admin', href: 'admin.html', icon: ICONS.admin });
  }

  const headerHtml = `
    <header class="sticky top-0 z-40 border-b border-[#1c2333] bg-[#090b10]/95 backdrop-blur-md px-6 py-3.5 flex items-center justify-between shadow-lg">
      <div class="flex items-center space-x-6">
        <a href="dashboard.html" class="flex items-center space-x-3 group no-underline">
          <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-cyan-600 via-[#2cf5d6] to-emerald-400 p-0.5 shadow-lg shadow-cyan-500/20 group-hover:scale-105 transition-transform duration-200 flex items-center justify-center">
            <div class="w-full h-full bg-[#090b10] rounded-[10px] flex items-center justify-center">
              <span class="text-2xl font-black bg-gradient-to-r from-[#2cf5d6] to-emerald-400 bg-clip-text text-transparent">π</span>
            </div>
          </div>
          <div class="flex items-center space-x-2">
            <span class="text-xl font-extrabold tracking-wider bg-gradient-to-r from-white via-cyan-100 to-[#2cf5d6] bg-clip-text text-transparent">PIE MC</span>
            <span class="px-2 py-0.5 text-[10px] font-mono font-bold uppercase tracking-wider rounded-md bg-[#2cf5d6]/10 text-[#2cf5d6] border border-[#2cf5d6]/30">v2.4</span>
          </div>
        </a>

        <nav class="hidden lg:flex items-center space-x-1 pl-4 border-l border-[#1c2333]/80">
          ${pages.map(p => `
            <a href="${p.href}" class="nav-link ${activePage === p.id ? 'active' : ''}">
              ${p.icon}
              <span>${p.label}</span>
            </a>
          `).join('')}
        </nav>
      </div>

      <div class="flex items-center space-x-3">
        ${user ? `
          <div class="flex items-center space-x-2.5 px-3 py-1.5 rounded-xl bg-[#0f131d] border border-[#1c2333] text-xs">
            <img src="${user.avatar || 'https://cdn.discordapp.com/embed/avatars/0.png'}" class="w-6 h-6 rounded-full border border-[#2cf5d6]/40" alt="">
            <span class="font-bold text-white">${user.username}</span>
            ${isOwner ? `<span class="badge-diamond text-[9px] px-1.5 py-0.5">OWNER</span>` : ''}
          </div>
          <button onclick="logout()" class="btn-secondary text-xs px-3 py-1.5 text-red-400 hover:text-red-300" title="Sign Out">
            ${ICONS.logout}
            <span class="hidden sm:inline">Logout</span>
          </button>
        ` : `
          <a href="login.html" class="btn-primary text-xs px-4 py-2">Login with Discord</a>
        `}

        <a href="settings.html" class="p-2.5 rounded-xl bg-[#0f131d] hover:bg-slate-800 border border-[#1c2333] hover:border-[#2cf5d6]/40 text-slate-300 hover:text-white transition-all shadow-sm flex items-center justify-center" title="Settings">
          ${ICONS.settings}
        </a>
      </div>
    </header>
  `;

  const mount = document.getElementById('header-mount');
  if (mount) mount.innerHTML = headerHtml;
};

window.renderInstanceBar = function() {
  const mount = document.getElementById('instance-bar-mount');
  if (!mount) return;

  mount.innerHTML = `
    <div class="bg-[#0f131d]/60 border-b border-[#1c2333] px-6 py-2.5 flex items-center justify-between">
      <div class="flex items-center space-x-2 overflow-x-auto" id="instanceTabsContainer">
        ${state.instances.map(inst => `
          <div class="flex items-center rounded-lg border transition-all ${
            state.activeInstanceId === inst.id
              ? 'bg-[#2cf5d6]/15 border-[#2cf5d6]/40 shadow-sm'
              : 'bg-slate-800/40 border-[#1c2333] hover:bg-slate-800'
          }">
            <button onclick="switchActiveInstance(${inst.id})" class="px-3 py-1.5 text-xs font-mono font-semibold flex items-center space-x-2 ${
              state.activeInstanceId === inst.id ? 'text-[#2cf5d6]' : 'text-slate-400 hover:text-white'
            }">
              <span class="w-2 h-2 rounded-full ${inst.status === 'online' ? 'bg-emerald-400 pulse-dot' : 'bg-red-400'}"></span>
              <span>${inst.name}</span>
            </button>
            <button onclick="deleteInstancePrompt(${inst.id}, '${inst.name}', event)" class="px-2 py-1.5 text-slate-500 hover:text-red-400 transition-colors border-l border-[#1c2333]" title="Delete this instance">
              ${ICONS.trash}
            </button>
          </div>
        `).join('')}
      </div>
      <div class="flex items-center space-x-3 pl-4">
        <button onclick="addNewInstanceGlobal()" class="btn-secondary text-xs px-3 py-1.5">
          ${ICONS.plus}
          <span>New Instance</span>
        </button>
      </div>
    </div>
  `;
};

window.switchActiveInstance = function(id) {
  state.activeInstanceId = id;
  saveState(state);
  window.location.reload();
};

window.addNewInstanceGlobal = function() {
  const user = getCurrentUser();
  const nextId = state.instances.length + 1;
  state.instances.push({
    id: nextId,
    name: 'Instance ' + nextId,
    status: 'online',
    account: state.accounts[0] ? state.accounts[0].username : `${user ? user.username : 'PieBot'}_${nextId}`,
    server: state.servers[0] ? state.servers[0].name : 'Hypixel Network',
    proxy: 'Auto'
  });
  state.activeInstanceId = nextId;
  saveState(state);
  window.location.reload();
};

// Particle Engine
function initParticleCanvas() {
  let canvas = document.getElementById('fx-canvas');
  if (!canvas) {
    canvas = document.createElement('canvas');
    canvas.id = 'fx-canvas';
    document.body.prepend(canvas);
  }

  const ctx = canvas.getContext('2d');
  let particles = [];

  function resizeCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  }
  window.addEventListener('resize', resizeCanvas);
  resizeCanvas();

  class HitCritStar {
    constructor(x, y, color = '#2cf5d6') {
      this.x = x;
      this.y = y;
      this.color = color;
      this.size = Math.random() * 4 + 3;
      const angle = Math.random() * Math.PI * 2;
      const speed = Math.random() * 5 + 2;
      this.vx = Math.cos(angle) * speed;
      this.vy = Math.sin(angle) * speed;
      this.life = 1;
      this.decay = Math.random() * 0.04 + 0.03;
      this.rotation = Math.random() * Math.PI;
      this.rotSpeed = (Math.random() - 0.5) * 0.2;
    }
    update() {
      this.x += this.vx;
      this.y += this.vy;
      this.vy += 0.12;
      this.rotation += this.rotSpeed;
      this.life -= this.decay;
    }
    draw(c) {
      c.save();
      c.globalAlpha = Math.max(0, this.life);
      c.translate(this.x, this.y);
      c.rotate(this.rotation);
      c.fillStyle = this.color;
      
      const s = this.size;
      c.beginPath();
      c.moveTo(-s, 0);
      c.lineTo(0, -s/2.5);
      c.lineTo(s, 0);
      c.lineTo(0, s/2.5);
      c.closePath();
      c.fill();

      c.beginPath();
      c.moveTo(0, -s);
      c.lineTo(-s/2.5, 0);
      c.lineTo(0, s);
      c.lineTo(s/2.5, 0);
      c.closePath();
      c.fill();

      c.restore();
    }
  }

  class PixelSpark {
    constructor(x, y, color = '#55ffff') {
      this.x = x;
      this.y = y;
      this.color = color;
      this.size = Math.random() * 2 + 2;
      this.vx = (Math.random() - 0.5) * 4;
      this.vy = (Math.random() - 0.5) * 4;
      this.life = 1;
      this.decay = Math.random() * 0.03 + 0.02;
    }
    update() {
      this.x += this.vx;
      this.y += this.vy;
      this.life -= this.decay;
    }
    draw(c) {
      c.save();
      c.globalAlpha = Math.max(0, this.life);
      c.fillStyle = this.color;
      c.fillRect(this.x - this.size/2, this.y - this.size/2, this.size, this.size);
      c.restore();
    }
  }

  window.triggerHitEffect = function(x, y) {
    for (let i = 0; i < 7; i++) {
      particles.push(new HitCritStar(x, y, Math.random() > 0.4 ? '#2cf5d6' : '#55ff55'));
    }
    for (let i = 0; i < 6; i++) {
      particles.push(new PixelSpark(x, y, '#55ffff'));
    }
  };

  let lastX = 0, lastY = 0;
  window.addEventListener('mousemove', (e) => {
    const dist = Math.hypot(e.clientX - lastX, e.clientY - lastY);
    if (dist > 20) {
      particles.push(new PixelSpark(e.clientX, e.clientY, '#2cf5d6'));
      lastX = e.clientX;
      lastY = e.clientY;
    }
  });

  window.addEventListener('click', (e) => {
    window.triggerHitEffect(e.clientX, e.clientY);
  });

  function loopFx() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    for (let i = particles.length - 1; i >= 0; i--) {
      const p = particles[i];
      p.update();
      p.draw(ctx);
      if (p.life <= 0) particles.splice(i, 1);
    }
    requestAnimationFrame(loopFx);
  }
  loopFx();
}

window.openModal = function(id) {
  const el = document.getElementById(id);
  if (el) {
    el.classList.remove('hidden');
    el.classList.add('flex');
  }
};

window.closeModal = function(id) {
  const el = document.getElementById(id);
  if (el) {
    el.classList.add('hidden');
    el.classList.remove('flex');
  }
};

window.addEventListener('DOMContentLoaded', () => {
  initParticleCanvas();
});
'''

with open(os.path.join(PUB, 'shared.js'), 'w', encoding='utf-8') as f:
    f.write(shared_js)

# 2. AUTOMATION.HTML (WITH MASTER TOGGLE & MULTI-INSTANCE SELECTOR)
automation_html = '''<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Pie MC — Scheduled Automation</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="styles.css">
  <script src="shared.js"></script>
</head>
<body>
  <div id="header-mount"></div>
  <div id="instance-bar-mount"></div>

  <main class="flex-1 p-6 max-w-7xl w-full mx-auto space-y-6">
    <div class="pie-card p-6 space-y-6">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h2 class="text-xl font-black text-white">Scheduled Automations</h2>
          <p class="text-xs text-slate-400 mt-1 font-mono">Periodic message broadcasts & routine commands assigned to instances</p>
        </div>
        
        <!-- Controls: Master Toggle All & New Automation Button -->
        <div class="flex items-center space-x-3">
          <button id="btnMasterToggle" onclick="toggleAllAutomationsMaster()" class="btn-secondary text-xs px-3 py-2">
            <span id="masterToggleText">Disable All</span>
          </button>
          <button onclick="openNewAutoModal()" class="btn-primary text-xs">
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>
            <span>New Automation</span>
          </button>
        </div>
      </div>

      <!-- Automations Table -->
      <div class="overflow-x-auto rounded-xl border border-[#1c2333]">
        <table class="w-full text-left text-sm text-slate-300">
          <thead class="bg-[#0c1018] text-xs uppercase font-mono text-slate-400 border-b border-[#1c2333]">
            <tr>
              <th class="px-4 py-3">Status</th>
              <th class="px-4 py-3">Message / Command</th>
              <th class="px-4 py-3">Interval</th>
              <th class="px-4 py-3">Target Instances</th>
              <th class="px-4 py-3 text-right">Actions</th>
            </tr>
          </thead>
          <tbody id="autoTableBody" class="divide-y divide-[#1c2333]/80 bg-[#090b10] font-mono text-xs">
          </tbody>
        </table>
      </div>
    </div>
  </main>

  <!-- Add Automation Modal (Multi-Instance Selection) -->
  <div id="addAutoModal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm hidden items-center justify-center p-4">
    <div class="pie-card p-6 max-w-lg w-full space-y-4 border border-[#1c2333] shadow-2xl">
      <div class="flex items-center justify-between border-b border-[#1c2333] pb-3">
        <h3 class="text-lg font-bold text-white">Create Scheduled Task</h3>
        <button onclick="closeModal('addAutoModal')" class="text-slate-400 hover:text-white">&times;</button>
      </div>

      <div class="space-y-4 text-xs">
        <div>
          <label class="block font-semibold text-slate-300 mb-1">Message / Command to Broadcast</label>
          <input id="modalAutoMsg" type="text" placeholder="e.g. /clan broadcast We are recruiting!" class="pie-input w-full font-mono text-white">
        </div>

        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block font-semibold text-slate-300 mb-1">Interval Duration</label>
            <input id="modalAutoInterval" type="number" value="60" class="pie-input w-full font-mono">
          </div>
          <div>
            <label class="block font-semibold text-slate-300 mb-1">Time Unit</label>
            <select id="modalAutoUnit" class="pie-select w-full">
              <option value="seconds">Seconds</option>
              <option value="minutes">Minutes</option>
              <option value="hours">Hours</option>
            </select>
          </div>
        </div>

        <!-- Multi-Instance Target Checkboxes -->
        <div class="p-3 rounded-xl bg-[#0a0d14] border border-[#1c2333] space-y-2">
          <div class="flex items-center justify-between">
            <label class="font-bold text-slate-300 block">Select Target Instances (Multiple)</label>
            <button type="button" onclick="selectAllInstancesCheckbox()" class="text-[#2cf5d6] text-[11px] hover:underline">Select All</button>
          </div>
          <div id="instanceCheckboxesList" class="grid grid-cols-2 sm:grid-cols-3 gap-2 pt-1">
            <!-- Populated dynamically via JS -->
          </div>
        </div>
      </div>

      <div class="flex items-center justify-end space-x-3 pt-2">
        <button onclick="closeModal('addAutoModal')" class="btn-secondary text-xs">Cancel</button>
        <button onclick="submitAuto()" class="btn-primary text-xs">Save Automation</button>
      </div>
    </div>
  </div>

  <script>
    document.addEventListener('DOMContentLoaded', () => {
      renderGlobalHeader('automation');
      renderInstanceBar();
      renderAutoTable();
    });

    function renderAutoTable() {
      const tbody = document.getElementById('autoTableBody');
      const allActive = state.automations.length > 0 && state.automations.every(a => a.status);
      document.getElementById('masterToggleText').innerText = allActive ? 'Disable All' : 'Enable All';

      tbody.innerHTML = state.automations.map(au => {
        let targetsText = 'All Instances';
        if (Array.isArray(au.targetInstances) && !au.targetInstances.includes('all')) {
          targetsText = au.targetInstances.map(id => `Instance ${id}`).join(', ');
        }

        return `
          <tr class="hover:bg-slate-900/40 transition-colors">
            <td class="px-4 py-3">
              <button onclick="toggleAuto('${au.id}')" class="${au.status ? 'badge-online' : 'badge-offline'}">
                ${au.status ? 'ACTIVE' : 'PAUSED'}
              </button>
            </td>
            <td class="px-4 py-3 font-semibold text-white font-mono">${au.msg}</td>
            <td class="px-4 py-3 text-cyan-300 font-mono">${au.interval}</td>
            <td class="px-4 py-3">
              <span class="px-2 py-0.5 rounded bg-[#2cf5d6]/10 text-[#2cf5d6] border border-[#2cf5d6]/30 text-[11px] font-mono font-bold">
                ${targetsText}
              </span>
            </td>
            <td class="px-4 py-3 text-right">
              <button onclick="removeAutoPrompt('${au.id}', '${au.msg}')" class="btn-secondary text-xs px-2.5 py-1 text-red-400 hover:text-red-300">Delete</button>
            </td>
          </tr>
        `;
      }).join('');
    }

    function toggleAuto(id) {
      window.updatePieState(s => {
        const item = s.automations.find(x => x.id === id);
        if (item) item.status = !item.status;
      });
      renderAutoTable();
    }

    function toggleAllAutomationsMaster() {
      const allActive = state.automations.every(a => a.status);
      const newStatus = !allActive;

      window.updatePieState(s => {
        s.automations.forEach(a => a.status = newStatus);
      });
      renderAutoTable();
    }

    function openNewAutoModal() {
      // Build checkboxes for all existing instances
      const container = document.getElementById('instanceCheckboxesList');
      container.innerHTML = `
        <label class="flex items-center space-x-2 p-2 rounded bg-slate-900 border border-[#1c2333] cursor-pointer">
          <input type="checkbox" id="chk_all" value="all" checked onchange="handleAllCheckboxChange(this.checked)" class="w-4 h-4 rounded text-[#2cf5d6]">
          <span class="text-xs font-bold text-white">All Instances</span>
        </label>
      ` + state.instances.map(inst => `
        <label class="flex items-center space-x-2 p-2 rounded bg-slate-900 border border-[#1c2333] cursor-pointer">
          <input type="checkbox" class="inst-chk w-4 h-4 rounded text-[#2cf5d6]" value="${inst.id}">
          <span class="text-xs font-semibold text-slate-300">${inst.name}</span>
        </label>
      `).join('');

      openModal('addAutoModal');
    }

    function handleAllCheckboxChange(checked) {
      if (checked) {
        document.querySelectorAll('.inst-chk').forEach(c => c.checked = false);
      }
    }

    function selectAllInstancesCheckbox() {
      document.getElementById('chk_all').checked = true;
      document.querySelectorAll('.inst-chk').forEach(c => c.checked = false);
    }

    function submitAuto() {
      const msg = document.getElementById('modalAutoMsg').value.trim() || '/help';
      const interval = document.getElementById('modalAutoInterval').value + ' ' + document.getElementById('modalAutoUnit').value;

      let targets = [];
      const chkAll = document.getElementById('chk_all');
      if (chkAll && chkAll.checked) {
        targets = ['all'];
      } else {
        document.querySelectorAll('.inst-chk:checked').forEach(c => {
          targets.push(parseInt(c.value));
        });
      }

      if (targets.length === 0) targets = ['all'];

      window.updatePieState(s => {
        s.automations.push({
          id: String(Date.now()),
          msg,
          interval,
          status: true,
          targetInstances: targets
        });
      });

      closeModal('addAutoModal');
      renderAutoTable();
    }

    function removeAutoPrompt(id, msg) {
      window.showConfirmModal({
        title: 'Delete Automation Task?',
        message: `Are you sure you want to delete the scheduled task <code>${msg}</code>?`,
        confirmText: 'Delete Task',
        cancelText: 'Cancel',
        isDanger: true,
        onConfirm: () => {
          window.updatePieState(s => {
            s.automations = s.automations.filter(x => x.id !== id);
          });
          renderAutoTable();
        }
      });
    }
  </script>
</body>
</html>
'''

with open(os.path.join(PUB, 'automation.html'), 'w', encoding='utf-8') as f:
    f.write(automation_html)

# 3. DASHBOARD.HTML (WITH STRICT PER-INSTANCE CONSOLE FILTERING)
dashboard_html = '''<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Pie MC — Dashboard</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="styles.css">
  <script src="shared.js"></script>
</head>
<body>
  <div id="header-mount"></div>
  <div id="instance-bar-mount"></div>

  <main class="flex-1 p-6 max-w-7xl w-full mx-auto space-y-6">
    <!-- Active Instance Hero Card -->
    <div class="pie-card p-6 relative overflow-hidden">
      <div class="flex flex-col lg:flex-row items-start lg:items-center justify-between gap-6 relative z-10">
        <div class="flex items-center space-x-4">
          <div class="w-14 h-14 rounded-2xl bg-[#0a0d14] border border-[#1c2333] flex items-center justify-center relative shadow-inner">
            <span id="botIconSpan" class="text-[#2cf5d6]">
              <svg class="w-7 h-7" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="10" rx="2"></rect><circle cx="12" cy="5" r="2"></circle><path d="M12 7v4"></path><line x1="8" y1="16" x2="8.01" y2="16"></line><line x1="16" y1="16" x2="16.01" y2="16"></line></svg>
            </span>
            <span id="botStatusDot" class="absolute -top-1 -right-1 w-4 h-4 rounded-full bg-emerald-400 border-2 border-[#090b10] pulse-dot"></span>
          </div>
          <div>
            <div class="flex items-center space-x-3">
              <h2 id="instName" class="text-2xl font-black text-white">Instance 1</h2>
              <span id="instBadge" class="badge-online">ONLINE</span>
            </div>
            <p id="instSubtitle" class="text-sm text-slate-400 mt-1 font-mono">
              Connected as <span id="instAccSpan" class="text-[#2cf5d6] font-bold">PieBot_1</span> on <span id="instSrvSpan" class="text-white font-semibold">mc.hypixel.net:25565</span>
            </p>
          </div>
        </div>

        <div class="flex items-center space-x-3 w-full lg:w-auto">
          <button id="btnToggle" onclick="toggleBot()" class="btn-danger flex-1 lg:flex-none">
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18.36 6.64a9 9 0 1 1-12.73 0"></path><line x1="12" y1="2" x2="12" y2="12"></line></svg>
            <span id="btnToggleText">Stop Bot</span>
          </button>
          <button onclick="restartBot()" class="btn-secondary">
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="23 4 23 10 17 10"></polyline><polyline points="1 20 1 14 7 14"></polyline><path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"></path></svg>
            <span>Restart</span>
          </button>
        </div>
      </div>

      <!-- 3 Primary Dropdown Cards -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mt-6 pt-6 border-t border-[#1c2333]/80">
        <!-- Account Selector -->
        <div class="pie-card-inner p-4 space-y-2">
          <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-slate-400 uppercase tracking-wider">ACTIVE ACCOUNT</span>
            <span id="cardAccStatusBadge" class="badge-online">AUTHENTICATED</span>
          </div>
          <select id="accSelect" onchange="changeActiveAccount(this.value)" class="pie-select w-full py-2 px-3 text-sm font-semibold text-white">
          </select>
          <div class="flex items-center justify-between text-[11px] font-mono text-slate-400 pt-1">
            <span>UUID: <span id="accUUID" class="text-slate-300">d8f3-4a11-98bc</span></span>
            <a href="accounts.html" class="text-[#2cf5d6] hover:underline font-semibold">Vault &rarr;</a>
          </div>
        </div>

        <!-- Server Selector -->
        <div class="pie-card-inner p-4 space-y-2">
          <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-slate-400 uppercase tracking-wider">TARGET SERVER</span>
            <span class="badge-online">ONLINE</span>
          </div>
          <select id="srvSelect" onchange="changeActiveServer(this.value)" class="pie-select w-full py-2 px-3 text-sm font-semibold text-white">
          </select>
          <div class="flex items-center justify-between text-[11px] font-mono text-slate-400 pt-1">
            <span>Host: <span id="srvHost" class="text-slate-300">mc.hypixel.net:25565</span></span>
            <span class="text-cyan-400 font-semibold">Ping: 24ms</span>
          </div>
        </div>

        <!-- Proxy Selector -->
        <div class="pie-card-inner p-4 space-y-2">
          <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-slate-400 uppercase tracking-wider">PROXY ROUTING</span>
            <span class="badge-diamond">AUTO POOL</span>
          </div>
          <select id="prxSelect" onchange="changeActiveProxy(this.value)" class="pie-select w-full py-2 px-3 text-sm font-semibold text-white">
          </select>
          <div class="flex items-center justify-between text-[11px] font-mono text-slate-400 pt-1">
            <span>Pool: <span class="text-slate-300">5 Proxies Ready</span></span>
            <span class="text-purple-400 font-semibold">SOCKS5</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Metric Badges -->
    <div class="grid grid-cols-2 lg:grid-cols-4 gap-4">
      <div class="pie-card p-4 flex items-center space-x-4">
        <div class="w-12 h-12 rounded-xl bg-blue-500/10 border border-blue-500/20 flex items-center justify-center text-blue-400">
          <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle></svg>
        </div>
        <div>
          <div class="text-2xl font-black text-white" id="statAcc">3</div>
          <div class="text-xs font-semibold text-slate-400 uppercase tracking-wider">ACCOUNTS</div>
        </div>
      </div>

      <div class="pie-card p-4 flex items-center space-x-4">
        <div class="w-12 h-12 rounded-xl bg-cyan-500/10 border border-cyan-500/20 flex items-center justify-center text-[#2cf5d6]">
          <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="8" rx="2" ry="2"></rect><rect x="2" y="14" width="20" height="8" rx="2" ry="2"></rect></svg>
        </div>
        <div>
          <div class="text-2xl font-black text-white" id="statSrv">4</div>
          <div class="text-xs font-semibold text-slate-400 uppercase tracking-wider">SERVERS</div>
        </div>
      </div>

      <div class="pie-card p-4 flex items-center space-x-4">
        <div class="w-12 h-12 rounded-xl bg-purple-500/10 border border-purple-500/20 flex items-center justify-center text-purple-400">
          <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
        </div>
        <div>
          <div class="text-2xl font-black text-white" id="statPrx">5</div>
          <div class="text-xs font-semibold text-slate-400 uppercase tracking-wider">PROXIES</div>
        </div>
      </div>

      <div class="pie-card p-4 flex items-center space-x-4">
        <div class="w-12 h-12 rounded-xl bg-emerald-500/10 border border-emerald-500/20 flex items-center justify-center text-emerald-400">
          <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>
        </div>
        <div>
          <div class="text-2xl font-black text-white" id="statTrg">8</div>
          <div class="text-xs font-semibold text-slate-400 uppercase tracking-wider">TRIGGERS</div>
        </div>
      </div>
    </div>

    <!-- Live In-Game Chat Stream Console (Strictly Filtered for Active Instance) -->
    <div class="pie-card p-5 space-y-4">
      <div class="flex items-center justify-between">
        <div class="flex items-center space-x-3">
          <div class="w-2.5 h-2.5 rounded-full bg-[#2cf5d6] pulse-dot"></div>
          <h3 class="text-base font-bold text-white">Live Instance Console <span id="chatInstTag" class="text-xs font-mono text-[#2cf5d6] font-bold">[Instance 1 Feed]</span></h3>
        </div>
        <div class="flex items-center space-x-2">
          <button onclick="clearChatConsole()" class="btn-secondary text-xs px-2.5 py-1">Clear</button>
          <a href="chat.html" class="btn-primary text-xs px-3 py-1 no-underline">Open Full Terminal &rarr;</a>
        </div>
      </div>

      <div id="dashChatStream" class="h-64 overflow-y-auto bg-black/85 rounded-xl p-4 font-mono text-xs space-y-2 border border-[#1c2333]">
      </div>

      <form onsubmit="handleSendChat(event)" class="flex items-center space-x-2 pt-2">
        <input id="dashChatInput" type="text" placeholder="Send a message or command through this instance..." class="pie-input flex-1 font-mono text-sm">
        <button type="submit" class="btn-primary">
          <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
          <span>Send</span>
        </button>
      </form>
    </div>
  </main>

  <script>
    document.addEventListener('DOMContentLoaded', () => {
      renderGlobalHeader('dashboard');
      renderInstanceBar();
      populateDashboard();
      renderChatLogs();
    });

    function populateDashboard() {
      const inst = state.instances.find(i => i.id === state.activeInstanceId) || state.instances[0];
      document.getElementById('instName').innerText = inst.name;
      document.getElementById('chatInstTag').innerText = `[${inst.name} Feed]`;
      
      const badge = document.getElementById('instBadge');
      const dot = document.getElementById('botStatusDot');
      const btn = document.getElementById('btnToggle');
      const btnText = document.getElementById('btnToggleText');

      if (inst.status === 'online') {
        badge.className = 'badge-online';
        badge.innerText = 'ONLINE';
        dot.className = 'absolute -top-1 -right-1 w-4 h-4 rounded-full bg-emerald-400 border-2 border-[#090b10] pulse-dot';
        btn.className = 'btn-danger flex-1 lg:flex-none';
        btnText.innerText = 'Stop Bot';
      } else {
        badge.className = 'badge-offline';
        badge.innerText = 'OFFLINE';
        dot.className = 'absolute -top-1 -right-1 w-4 h-4 rounded-full bg-red-500 border-2 border-[#090b10]';
        btn.className = 'btn-primary flex-1 lg:flex-none';
        btnText.innerText = 'Start Bot';
      }

      document.getElementById('instAccSpan').innerText = inst.account;
      document.getElementById('instSrvSpan').innerText = inst.server;

      const currentAcc = state.accounts.find(a => a.username === inst.account);
      const accBadge = document.getElementById('cardAccStatusBadge');
      if (currentAcc && (currentAcc.status === 'needs_reauth' || currentAcc.tokenExpiryStatus === 'needs_reauth')) {
        accBadge.className = 'px-2 py-0.5 rounded text-[10px] font-mono font-bold bg-amber-500/15 text-amber-400 border border-amber-500/30';
        accBadge.innerText = 'NEEDS RE-AUTH';
      } else {
        accBadge.className = 'badge-online';
        accBadge.innerText = 'AUTHENTICATED';
      }

      const accSelect = document.getElementById('accSelect');
      accSelect.innerHTML = state.accounts.map(a => `
        <option value="${a.username}" ${a.username === inst.account ? 'selected' : ''}>
          ${a.username} ${a.status === 'needs_reauth' ? '⚠️ (Expired)' : '✓'}
        </option>
      `).join('');

      const srvSelect = document.getElementById('srvSelect');
      srvSelect.innerHTML = state.servers.map(s => `<option value="${s.name}" ${s.name === inst.server ? 'selected' : ''}>${s.name} (${s.host})</option>`).join('');

      const prxSelect = document.getElementById('prxSelect');
      prxSelect.innerHTML = `<option value="Auto">Auto Pool (Best Available)</option>` + state.proxies.map(p => `<option value="${p.name}" ${p.name === inst.proxy ? 'selected' : ''}>${p.name} [${p.type}]</option>`).join('');

      document.getElementById('statAcc').innerText = state.accounts.length;
      document.getElementById('statSrv').innerText = state.servers.length;
      document.getElementById('statPrx').innerText = state.proxies.length;
      document.getElementById('statTrg').innerText = state.triggers.length;
    }

    function toggleBot() {
      const inst = state.instances.find(i => i.id === state.activeInstanceId);
      if (inst) {
        inst.status = inst.status === 'online' ? 'offline' : 'online';
        window.updatePieState(s => {
          const target = s.instances.find(x => x.id === inst.id);
          if (target) target.status = inst.status;
          
          // Log join/leave event specifically for this instance
          s.chatLogs.push({
            id: 'c_' + Date.now(),
            instanceId: inst.id,
            time: new Date().toTimeString().split(' ')[0],
            player: inst.account,
            tag: inst.status === 'online' ? '[JOIN]' : '[QUIT]',
            msg: inst.status === 'online' ? `Connected to ${inst.server}` : 'Disconnected from server',
            type: 'system'
          });
        });
        populateDashboard();
        renderChatLogs();
        window.renderInstanceBar();
      }
    }

    function restartBot() {
      toggleBot();
      setTimeout(() => toggleBot(), 600);
    }

    function changeActiveAccount(val) {
      window.updatePieState(s => {
        const target = s.instances.find(x => x.id === s.activeInstanceId);
        if (target) target.account = val;
      });
      populateDashboard();
    }

    function changeActiveServer(val) {
      window.updatePieState(s => {
        const target = s.instances.find(x => x.id === s.activeInstanceId);
        if (target) target.server = val;
      });
      populateDashboard();
    }

    function changeActiveProxy(val) {
      window.updatePieState(s => {
        const target = s.instances.find(x => x.id === s.activeInstanceId);
        if (target) target.proxy = val;
      });
      populateDashboard();
    }

    function renderChatLogs() {
      const c = document.getElementById('dashChatStream');
      const curInstId = state.activeInstanceId || 1;
      
      // Filter chat logs specifically for the selected instance
      const filtered = state.chatLogs.filter(m => m.instanceId === curInstId);

      if (filtered.length === 0) {
        c.innerHTML = `<div class="text-slate-500 font-mono text-center py-8">No console messages logged for this instance yet.</div>`;
        return;
      }

      c.innerHTML = filtered.map(m => `
        <div class="flex items-start space-x-2">
          <span class="text-slate-600">[${m.time}]</span>
          <span class="${m.type === 'bot' ? 'text-emerald-400 font-bold' : (m.type === 'system' ? 'text-cyan-400 font-bold' : 'text-slate-300')}">${m.tag} ${m.player}:</span>
          <span class="text-slate-200">${m.msg}</span>
        </div>
      `).join('');
      c.scrollTop = c.scrollHeight;
    }

    function handleSendChat(e) {
      e.preventDefault();
      const input = document.getElementById('dashChatInput');
      const val = input.value.trim();
      if (!val) return;

      const now = new Date().toTimeString().split(' ')[0];
      const inst = state.instances.find(i => i.id === state.activeInstanceId) || state.instances[0];

      window.updatePieState(s => {
        s.chatLogs.push({ 
          id: 'c_' + Date.now(),
          instanceId: inst.id,
          time: now, 
          player: inst.account, 
          tag: '[BOT]', 
          msg: val, 
          type: 'bot' 
        });
      });

      renderChatLogs();
      input.value = '';
    }

    function clearChatConsole() {
      const curInstId = state.activeInstanceId || 1;
      window.updatePieState(s => {
        s.chatLogs = s.chatLogs.filter(m => m.instanceId !== curInstId);
      });
      renderChatLogs();
    }
  </script>
</body>
</html>
'''

with open(os.path.join(PUB, 'dashboard.html'), 'w', encoding='utf-8') as f:
    f.write(dashboard_html)

# 4. CHAT.HTML (SEPARATE CONSOLE CHAT STREAM PER INSTANCE)
chat_html = '''<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Pie MC — Interactive Terminal</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="styles.css">
  <script src="shared.js"></script>
</head>
<body>
  <div id="header-mount"></div>
  <div id="instance-bar-mount"></div>

  <main class="flex-1 p-6 max-w-7xl w-full mx-auto space-y-6">
    <div class="pie-card p-6 flex flex-col h-[78vh]">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between pb-4 border-b border-[#1c2333] gap-3">
        <div class="flex items-center space-x-3">
          <div class="w-8 h-8 rounded-lg bg-[#2cf5d6]/10 border border-[#2cf5d6]/30 flex items-center justify-center text-[#2cf5d6]">
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
          </div>
          <div>
            <h2 class="text-lg font-bold text-white flex items-center space-x-2">
              <span>Instance Terminal</span>
              <span id="chatActiveInstanceBadge" class="badge-diamond font-mono text-[11px]">Instance 1</span>
            </h2>
            <p class="text-xs text-slate-400 font-mono">Isolated console feed for active bot</p>
          </div>
        </div>

        <div class="flex items-center space-x-2 flex-wrap">
          <!-- Command Shortcuts -->
          <button onclick="insertCmd('/spawn')" class="btn-secondary text-xs px-2.5 py-1 font-mono text-cyan-300">/spawn</button>
          <button onclick="insertCmd('/help')" class="btn-secondary text-xs px-2.5 py-1 font-mono text-cyan-300">/help</button>
          <button onclick="insertCmd('/list')" class="btn-secondary text-xs px-2.5 py-1 font-mono text-cyan-300">/list</button>
          <button onclick="insertCmd('/tpa ')" class="btn-secondary text-xs px-2.5 py-1 font-mono text-cyan-300">/tpa</button>
          <button onclick="clearConsole()" class="btn-secondary text-xs px-3 py-1 text-red-400">Clear</button>
        </div>
      </div>

      <!-- Scrollable Console Output -->
      <div id="fullConsoleStream" class="flex-1 overflow-y-auto bg-black/85 rounded-xl p-4 my-4 font-mono text-xs space-y-2 border border-[#1c2333]">
      </div>

      <!-- Transmission Bar -->
      <form onsubmit="handleSend(event)" class="flex items-center space-x-3 pt-2">
        <input id="chatInput" type="text" placeholder="Type a chat message or Minecraft command..." class="pie-input flex-1 font-mono text-sm">
        <button type="submit" class="btn-primary px-6">
          <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
          <span>Transmit</span>
        </button>
      </form>
    </div>
  </main>

  <script>
    document.addEventListener('DOMContentLoaded', () => {
      renderGlobalHeader('chat');
      renderInstanceBar();
      renderChat();
    });

    function renderChat() {
      const c = document.getElementById('fullConsoleStream');
      const curInstId = state.activeInstanceId || 1;
      const inst = state.instances.find(i => i.id === curInstId) || state.instances[0];

      document.getElementById('chatActiveInstanceBadge').innerText = inst.name;

      const filtered = state.chatLogs.filter(m => m.instanceId === curInstId);

      if (filtered.length === 0) {
        c.innerHTML = `<div class="text-slate-500 font-mono text-center py-12">No console messages recorded for ${inst.name}.</div>`;
        return;
      }

      c.innerHTML = filtered.map(m => `
        <div class="flex items-start space-x-2">
          <span class="text-slate-600">[${m.time}]</span>
          <span class="${m.type === 'bot' ? 'text-emerald-400 font-bold' : (m.type === 'system' ? 'text-cyan-400 font-bold' : 'text-slate-300')}">${m.tag} ${m.player}:</span>
          <span class="text-slate-200">${m.msg}</span>
        </div>
      `).join('');
      c.scrollTop = c.scrollHeight;
    }

    function handleSend(e) {
      e.preventDefault();
      const input = document.getElementById('chatInput');
      const val = input.value.trim();
      if (!val) return;

      const now = new Date().toTimeString().split(' ')[0];
      const inst = state.instances.find(i => i.id === state.activeInstanceId) || state.instances[0];

      window.updatePieState(s => {
        s.chatLogs.push({ 
          id: 'c_' + Date.now(),
          instanceId: inst.id,
          time: now, 
          player: inst.account, 
          tag: '[BOT]', 
          msg: val, 
          type: 'bot' 
        });
      });

      renderChat();
      input.value = '';
    }

    function insertCmd(cmd) {
      const input = document.getElementById('chatInput');
      input.value = cmd;
      input.focus();
    }

    function clearConsole() {
      const curInstId = state.activeInstanceId || 1;
      window.updatePieState(s => {
        s.chatLogs = s.chatLogs.filter(m => m.instanceId !== curInstId);
      });
      renderChat();
    }
  </script>
</body>
</html>
'''

with open(os.path.join(PUB, 'chat.html'), 'w', encoding='utf-8') as f:
    f.write(chat_html)

# 5. LOGS.HTML (48-HOUR LOGS WITH INSTANCE SELECTOR)
logs_html = '''<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Pie MC — Audit Logs</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="styles.css">
  <script src="shared.js"></script>
</head>
<body>
  <div id="header-mount"></div>
  <div id="instance-bar-mount"></div>

  <main class="flex-1 p-6 max-w-7xl w-full mx-auto space-y-6">
    <div class="pie-card p-6 space-y-6">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <div class="flex items-center space-x-3">
            <h2 class="text-xl font-black text-white">48-Hour Activity & System Logs</h2>
            <span class="badge-diamond text-xs font-mono">48H WINDOW</span>
          </div>
          <p class="text-xs text-slate-400 mt-1 font-mono">Filter historical telemetry, connects, and trigger executions by instance</p>
        </div>

        <!-- Filters -->
        <div class="flex items-center space-x-3 flex-wrap">
          <!-- Instance Selector -->
          <select id="logInstanceSelect" onchange="filterLogs()" class="pie-select text-xs py-1.5 px-3">
            <option value="all">All Instances</option>
          </select>

          <!-- Search Input -->
          <input id="logSearch" oninput="filterLogs()" type="text" placeholder="Search event or player..." class="pie-input text-xs w-44">
          
          <button onclick="clearLogsPrompt()" class="btn-secondary text-xs px-3 py-1.5 text-red-400">Clear Logs</button>
        </div>
      </div>

      <!-- Logs Table -->
      <div class="overflow-x-auto rounded-xl border border-[#1c2333]">
        <table class="w-full text-left text-sm text-slate-300">
          <thead class="bg-[#0c1018] text-xs uppercase font-mono text-slate-400 border-b border-[#1c2333]">
            <tr>
              <th class="px-4 py-3">Date / Timestamp</th>
              <th class="px-4 py-3">Instance</th>
              <th class="px-4 py-3">Event Type</th>
              <th class="px-4 py-3">Player / Target</th>
              <th class="px-4 py-3">Event Details</th>
            </tr>
          </thead>
          <tbody id="logsTableBody" class="divide-y divide-[#1c2333]/80 bg-[#090b10] font-mono text-xs">
          </tbody>
        </table>
      </div>
    </div>
  </main>

  <script>
    document.addEventListener('DOMContentLoaded', () => {
      renderGlobalHeader('logs');
      renderInstanceBar();
      populateInstanceFilter();
      filterLogs();
    });

    function populateInstanceFilter() {
      const select = document.getElementById('logInstanceSelect');
      select.innerHTML = `<option value="all">All Instances</option>` + state.instances.map(inst => `
        <option value="${inst.id}" ${state.activeInstanceId === inst.id ? 'selected' : ''}>${inst.name}</option>
      `).join('');
    }

    function filterLogs() {
      const instFilter = document.getElementById('logInstanceSelect').value;
      const q = document.getElementById('logSearch').value.toLowerCase();

      const filtered = state.logs.filter(l => {
        const matchesInst = (instFilter === 'all' || l.instanceId === parseInt(instFilter));
        const matchesQuery = !q || 
          l.player.toLowerCase().includes(q) || 
          l.event.toLowerCase().includes(q) || 
          l.details.toLowerCase().includes(q);
        return matchesInst && matchesQuery;
      });

      renderLogsTable(filtered);
    }

    function renderLogsTable(logList) {
      const tbody = document.getElementById('logsTableBody');
      if (logList.length === 0) {
        tbody.innerHTML = `<tr><td colspan="5" class="px-4 py-8 text-center text-slate-500 font-mono">No logs recorded within the last 48 hours for the chosen filter.</td></tr>`;
        return;
      }

      tbody.innerHTML = logList.map(l => `
        <tr class="hover:bg-slate-900/40 transition-colors">
          <td class="px-4 py-3 text-slate-400 font-mono">
            <span class="text-slate-500">${l.date || ''}</span>
            <strong class="text-slate-300 ml-1">${l.time}</strong>
          </td>
          <td class="px-4 py-3 text-[#2cf5d6] font-bold">${l.instanceName || ('Instance ' + l.instanceId)}</td>
          <td class="px-4 py-3"><span class="badge-diamond">${l.event}</span></td>
          <td class="px-4 py-3 text-white font-bold">${l.player}</td>
          <td class="px-4 py-3 text-slate-300">${l.details}</td>
        </tr>
      `).join('');
    }

    function clearLogsPrompt() {
      window.showConfirmModal({
        title: 'Clear 48-Hour Logs?',
        message: 'Are you sure you want to clear the activity log history?',
        confirmText: 'Clear Logs',
        cancelText: 'Cancel',
        isDanger: true,
        onConfirm: () => {
          window.updatePieState(s => s.logs = []);
          filterLogs();
        }
      });
    }
  </script>
</body>
</html>
'''

with open(os.path.join(PUB, 'logs.html'), 'w', encoding='utf-8') as f:
    f.write(logs_html)

# 6. SETTINGS.HTML (WITH 48-HOUR AUTO-CLEANUP TOGGLE & MANUAL PRUNER)
settings_html = '''<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Pie MC — Settings</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="styles.css">
  <script src="shared.js"></script>
</head>
<body>
  <div id="header-mount"></div>
  <div id="instance-bar-mount"></div>

  <main class="flex-1 p-6 max-w-4xl w-full mx-auto space-y-6">
    <div class="pie-card p-6 space-y-6">
      <div class="flex items-center justify-between pb-4 border-b border-[#1c2333]">
        <div>
          <h2 class="text-xl font-black text-white">Pie MC System Settings</h2>
          <p class="text-xs text-slate-400 mt-1 font-mono">Connection policies, 48-hour log cleanups, and security keys</p>
        </div>
      </div>

      <div class="space-y-6 text-sm">
        <!-- 48-HOUR LOG CLEANUP SECTION -->
        <div class="space-y-3">
          <h3 class="text-xs font-bold uppercase tracking-wider text-[#2cf5d6] font-mono">Log Retention & Maintenance</h3>
          
          <div class="p-4 rounded-xl pie-card-inner border border-[#1c2333] space-y-3">
            <label class="flex items-center justify-between cursor-pointer">
              <div>
                <span class="font-bold text-white block">48-Hour Log Auto-Cleanup</span>
                <span class="text-xs text-slate-400">Automatically prune activity and audit logs older than 48 hours to maintain fast performance.</span>
              </div>
              <input type="checkbox" id="chkAutoCleanup48h" checked class="w-5 h-5 rounded text-[#2cf5d6]">
            </label>

            <div class="pt-2 border-t border-[#1c2333] flex items-center justify-between">
              <span class="text-xs text-slate-400 font-mono">Purge history older than 48 hours manually:</span>
              <button onclick="runManual48hCleanup()" class="btn-secondary text-xs px-3 py-1.5 text-amber-400 border-amber-500/30">
                <span>Clean Up Logs > 48h Now</span>
              </button>
            </div>
          </div>
        </div>

        <!-- Connection Policies -->
        <div class="space-y-3 pt-4 border-t border-[#1c2333]">
          <h3 class="text-xs font-bold uppercase tracking-wider text-[#2cf5d6] font-mono">Connection Policies</h3>
          
          <label class="flex items-center justify-between p-4 rounded-xl pie-card-inner border border-[#1c2333] cursor-pointer">
            <div>
              <span class="font-bold text-white block">Auto-Reconnect on Disconnect</span>
              <span class="text-xs text-slate-400">Automatically re-establish connection after kicks or server restarts</span>
            </div>
            <input type="checkbox" id="userAutoReconnect" checked class="w-5 h-5 rounded text-[#2cf5d6]">
          </label>

          <div class="grid grid-cols-2 gap-4">
            <div class="space-y-1">
              <label class="text-xs font-semibold text-slate-300">Retry Delay (Seconds)</label>
              <input type="number" value="10" class="pie-input w-full font-mono">
            </div>
            <div class="space-y-1">
              <label class="text-xs font-semibold text-slate-300">Max Retry Attempts</label>
              <input type="number" value="5" class="pie-input w-full font-mono">
            </div>
          </div>
        </div>

        <!-- Minecraft Protocol Version -->
        <div class="space-y-3 pt-4 border-t border-[#1c2333]">
          <div class="flex items-center justify-between">
            <h3 class="text-xs font-bold uppercase tracking-wider text-[#2cf5d6] font-mono">Minecraft Protocol Version</h3>
            <span id="versionLockNotice" class="hidden px-2 py-0.5 rounded text-[10px] font-mono bg-amber-500/15 text-amber-400 border border-amber-500/30">LOCKED BY ADMIN</span>
          </div>

          <div class="space-y-1">
            <label class="text-xs font-semibold text-slate-300">Target Version Protocol</label>
            <select id="userVersionSelect" class="pie-select w-full font-mono">
              <option value="1.21.1">1.21.1 / 1.21.11 (Latest)</option>
              <option value="1.20.4">1.20.4</option>
              <option value="1.19.4">1.19.4</option>
              <option value="1.16.5">1.16.5</option>
              <option value="1.8.9">1.8.9</option>
            </select>
          </div>
        </div>

        <!-- OWNER-ONLY SECURITY & BEARER API KEY SECTION -->
        <div id="ownerSecuritySection" class="hidden space-y-3 pt-4 border-t border-[#1c2333]">
          <div class="flex items-center justify-between">
            <h3 class="text-xs font-bold uppercase tracking-wider text-[#2cf5d6] font-mono">Backend API Security (Owner Only)</h3>
            <span class="badge-diamond text-[10px] font-mono">RESTRICTED TO OWNER</span>
          </div>
          
          <div class="space-y-1">
            <label class="text-xs font-semibold text-slate-300">Backend API Key (Bearer Token)</label>
            <input type="text" id="ownerApiKeyInput" value="pie_mc_live_89437b02c89f4172" class="pie-input w-full font-mono text-[#2cf5d6]">
          </div>
        </div>

        <div class="pt-4 flex justify-end">
          <button onclick="saveUserSettings()" class="btn-primary">Save Preferences</button>
        </div>
      </div>
    </div>
  </main>

  <script>
    document.addEventListener('DOMContentLoaded', () => {
      renderGlobalHeader('settings');
      renderInstanceBar();
      loadUserSettings();
    });

    function loadUserSettings() {
      const user = getCurrentUser();
      const flags = getPlatformFlags();

      document.getElementById('chkAutoCleanup48h').checked = (flags.autoCleanup48h !== false);

      if (user && (user.isOwner || user.id === OWNER_DISCORD_ID)) {
        document.getElementById('ownerSecuritySection').classList.remove('hidden');
      }

      if (!flags.allowUserChangeVersion && (!user || (!user.isOwner && user.id !== OWNER_DISCORD_ID))) {
        const vSelect = document.getElementById('userVersionSelect');
        vSelect.value = flags.lockedVersion || '1.21.1';
        vSelect.disabled = true;
        document.getElementById('versionLockNotice').classList.remove('hidden');
      }
    }

    function runManual48hCleanup() {
      const flags = getPlatformFlags();
      const cutoff = Date.now() - (48 * 3600 * 1000);
      
      window.updatePieState(s => {
        const before = s.logs.length;
        s.logs = s.logs.filter(l => l.timestamp && l.timestamp >= cutoff);
        alert(`Cleanup complete! Purged logs older than 48 hours.`);
      });
    }

    function saveUserSettings() {
      const flags = getPlatformFlags();
      flags.autoCleanup48h = document.getElementById('chkAutoCleanup48h').checked;
      savePlatformFlags(flags);
      alert('Settings saved successfully!');
    }
  </script>
</body>
</html>
'''

with open(os.path.join(PUB, 'settings.html'), 'w', encoding='utf-8') as f:
    f.write(settings_html)

print("V9 Automation, Per-Instance Chat & 48h Logs built successfully!")
