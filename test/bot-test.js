/**
 * Bot Connection Test - reads token from test/key.txt and tries to connect
 */
const fs = require('fs');
const path = require('path');

// Read token from file
const tokenPath = path.join(__dirname, 'key.txt');
if (!fs.existsSync(tokenPath)) {
  console.error('❌ Token file not found at test/key.txt');
  process.exit(1);
}

const rawToken = fs.readFileSync(tokenPath, 'utf8').trim();
console.log(`✅ Token loaded (${rawToken.length} chars, starts with: ${rawToken.substring(0, 30)}...)`);

// Try to decode JWT payload to get username
try {
  const parts = rawToken.split('.');
  if (parts.length >= 2) {
    const payload = JSON.parse(Buffer.from(parts[1], 'base64').toString());
    console.log(`📋 Token payload:`);
    console.log(`   - iat: ${payload.iat} (${new Date(payload.iat * 1000).toISOString()})`);
    console.log(`   - id: ${payload.id || 'N/A'}`);
    console.log(`   - role: ${payload.a || 'N/A'}`);
    
    // Check expiry
    if (payload.exp) {
      const now = Math.floor(Date.now() / 1000);
      const remaining = payload.exp - now;
      const hours = Math.floor(Math.abs(remaining) / 3600);
  const mins = Math.floor((Math.abs(remaining) % 3600) / 60);
  if (remaining > 0) {
    console.log(`   - expires: ${new Date(payload.exp * 1000).toISOString()} (${hours}h ${mins}m remaining)`);
  } else {
    console.log(`   - expires: ${new Date(payload.exp * 1000).toISOString()} (EXPIRED ${hours}h ${mins}m ago)`);
  }
    }
  }
} catch (e) {
  console.log(`⚠️  Could not decode JWT payload: ${e.message}`);
}

// Now verify with Mojang API
async function verifyToken() {
  console.log('\n🔍 Verifying token with Mojang API...');
  try {
    const res = await fetch('https://api.minecraftservices.com/minecraft/profile', {
      headers: {
        'Authorization': `Bearer ${rawToken}`,
        'User-Agent': 'PieMC-Test/1.0'
      }
    });
    
    if (res.status === 200) {
      const profile = await res.json();
      console.log(`✅ Mojang verified!`);
      console.log(`   - Username: ${profile.name}`);
      console.log(`   - UUID: ${profile.id}`);
      console.log(`   - Skins: ${profile.skins ? profile.skins.length : 0}`);
      return { username: profile.name, uuid: profile.id, token: rawToken };
    } else {
      const err = await res.text();
      console.error(`❌ Mojang rejected (${res.status}): ${err}`);
      return null;
    }
  } catch (e) {
    console.error(`❌ Mojang API error: ${e.message}`);
    return null;
  }
}

// Try connecting with mineflayer
async function testMineflayer(profile) {
  if (!profile) {
    console.log('\n⏭️  Skipping mineflayer test (no valid profile)');
    return;
  }

  console.log(`\n🎮 Testing mineflayer connection...`);
  console.log(`   Username: ${profile.username}`);
  console.log(`   UUID (raw): ${profile.uuid}`);
  console.log(`   UUID (no dashes): ${profile.uuid.replace(/-/g, '')}`);

  let mineflayer;
  try {
    mineflayer = require('../backend/node_modules/mineflayer');
  } catch (e) {
    console.error('❌ mineflayer not found:', e.message);
    return;
  }

  const serverHost = process.argv[2] || 'as.catpvp.net';
  const serverPort = parseInt(process.argv[3]) || 25565;
  const serverVersion = process.argv[4] || '1.21.1';

  console.log(`   Server: ${serverHost}:${serverPort} (v${serverVersion})`);

  const botOptions = {
    host: serverHost,
    port: serverPort,
    username: profile.username,
    version: serverVersion,
    // Custom auth function: bypasses OAuth, sets session, starts connection
    auth: (client, opts) => {
      client.session = opts.session;
      client.username = opts.username;
      client.uuid = opts.session.selectedProfile.id;
      opts.connect(client);
    },
    haveCredentials: true,
    accessToken: profile.token,
    session: {
      accessToken: profile.token,
      selectedProfile: {
        id: profile.uuid.replace(/-/g, ''),
        name: profile.username
      },
      availableProfile: [{
        id: profile.uuid.replace(/-/g, ''),
        name: profile.username
      }]
    }
  };

  const bot = mineflayer.createBot(botOptions);

  const timeout = setTimeout(() => {
    console.error('❌ Bot timed out (30s) - never spawned');
    console.log('   Possible causes:');
    console.log('   1. Server is not running or unreachable');
    console.log('   2. Server version mismatch');
    console.log('   3. Token expired or rejected by server');
    console.log('   4. Server has whitelist or IP restrictions');
    bot.quit();
    process.exit(1);
  }, 30000);

  bot.on('login', () => {
    console.log('✅ Bot logged in! Waiting for spawn...');
  });

  bot.on('spawn', () => {
    clearTimeout(timeout);
    console.log(`\n🎉 SUCCESS! Bot spawned on server!`);
    console.log(`   - Bot username: ${bot.username}`);
    console.log(`   - Game mode: ${bot.game.gameMode}`);
    console.log(`   - Players online: ${Object.keys(bot.players).length}`);
    
    // Send a test chat message
    setTimeout(() => {
      bot.chat('PieMC bot connected!');
      console.log('   - Sent test chat message');
      
      // Wait a bit then quit
      setTimeout(() => {
        console.log('\n✅ All tests passed! Bot is working.');
        bot.quit();
        process.exit(0);
      }, 3000);
    }, 2000);
  });

  bot.on('kicked', (reason) => {
    clearTimeout(timeout);
    const reasonStr = typeof reason === 'string' ? reason : JSON.stringify(reason);
    console.error(`\n❌ Bot kicked: ${reasonStr}`);
    process.exit(1);
  });

  bot.on('error', (err) => {
    console.error(`❌ Bot error: ${err.message}`);
    console.error(`   Stack: ${err.stack}`);
  });

  // Log all events for debugging
  const origEmit = bot.emit.bind(bot);
  bot.emit = function(event, ...args) {
    if (!['tick', 'physicTick'].includes(event)) {
      console.log(`   [event] ${event}`, typeof args[0] === 'string' ? args[0] : '');
    }
    return origEmit(event, ...args);
  };

  bot.on('end', (reason) => {
    clearTimeout(timeout);
    console.log(`🔌 Disconnected: ${reason}`);
  });
}

// Run tests
(async () => {
  const profile = await verifyToken();
  await testMineflayer(profile);
})();
