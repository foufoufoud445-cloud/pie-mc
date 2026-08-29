import os

login_html = '''<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Pie MC — Login with Discord</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="styles.css">
  <script src="shared.js"></script>
</head>
<body class="flex items-center justify-center min-h-screen p-4 bg-[#090b10] relative overflow-hidden">

  <!-- Background Glow FX -->
  <div class="absolute -top-32 -left-32 w-96 h-96 bg-[#2cf5d6]/10 rounded-full blur-3xl pointer-events-none"></div>
  <div class="absolute -bottom-32 -right-32 w-96 h-96 bg-indigo-600/15 rounded-full blur-3xl pointer-events-none"></div>

  <div class="pie-card max-w-md w-full p-8 space-y-6 relative z-10 border border-[#1c2333] shadow-2xl">
    <!-- Brand Header -->
    <div class="text-center space-y-3">
      <div class="w-16 h-16 rounded-2xl bg-gradient-to-tr from-cyan-600 via-[#2cf5d6] to-emerald-400 p-0.5 shadow-xl shadow-cyan-500/25 mx-auto flex items-center justify-center">
        <div class="w-full h-full bg-[#090b10] rounded-[14px] flex items-center justify-center">
          <span class="text-3xl font-black bg-gradient-to-r from-[#2cf5d6] to-emerald-400 bg-clip-text text-transparent">π</span>
        </div>
      </div>
      <div>
        <h1 class="text-2xl font-black text-white tracking-wider">PIE MC GATEWAY</h1>
        <p class="text-xs text-slate-400 font-mono mt-1">Multi-Instance Minecraft Bot Engine</p>
      </div>
    </div>

    <!-- Status Banner / Loading -->
    <div id="authStatusBanner" class="p-4 rounded-xl bg-[#0a0d14] border border-[#1c2333] text-xs text-slate-300 space-y-1.5">
      <p class="font-semibold text-white flex items-center space-x-2">
        <span id="statusDot" class="w-2 h-2 rounded-full bg-indigo-400 pulse-dot"></span>
        <span id="statusTitle">Discord Authentication</span>
      </p>
      <p id="statusSubtitle" class="text-slate-400 leading-relaxed">
        Authenticate using your Discord account to access your personal workspace, bot instances, and SSID token vault.
      </p>
    </div>

    <!-- OAuth Action: ONLY the single 'Login with Discord' button -->
    <div class="space-y-3">
      <button id="btnLoginDiscord" onclick="startDiscordOAuth()" class="w-full py-3.5 px-4 rounded-xl bg-[#5865F2] hover:bg-[#4752C4] text-white font-bold text-sm shadow-lg shadow-indigo-500/25 flex items-center justify-center space-x-3 transition-all transform active:scale-95">
        <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24"><path d="M20.317 4.37a19.791 19.791 0 0 0-4.885-1.515.074.074 0 0 0-.079.037c-.21.375-.444.864-.608 1.25a18.27 18.27 0 0 0-5.487 0 12.64 12.64 0 0 0-.617-1.25.077.077 0 0 0-.079-.037A19.736 19.736 0 0 0 3.677 4.37a.07.07 0 0 0-.032.027C.533 9.046-.32 13.58.099 18.057a.082.082 0 0 0 .031.057 19.9 19.9 0 0 0 5.993 3.03.078.078 0 0 0 .084-.028c.462-.63.874-1.295 1.226-1.994.021-.041.001-.09-.041-.106a13.107 13.107 0 0 1-1.872-.892.077.077 0 0 1-.008-.128 10.2 10.2 0 0 0 .372-.292.074.074 0 0 1 .077-.01c3.929 1.793 8.18 1.793 12.061 0a.074.074 0 0 1 .078.01c.12.098.246.198.373.292a.077.077 0 0 1-.006.127 12.299 12.299 0 0 1-1.873.894.077.077 0 0 0-.041.107c.36.698.772 1.362 1.225 1.993a.076.076 0 0 0 .084.028 19.839 19.839 0 0 0 6.002-3.03.077.077 0 0 0 .032-.054c.5-5.177-.838-9.674-3.549-13.66a.061.061 0 0 0-.031-.028zM8.02 15.33c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.956-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.956 2.418-2.157 2.418zm7.975 0c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.955-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.946 2.418-2.157 2.418z"/></svg>
        <span id="btnText">Login with Discord</span>
      </button>

      <!-- Client Configuration Trigger if running standalone -->
      <div class="flex items-center justify-between text-[11px] font-mono text-slate-500 pt-1">
        <button onclick="openDiscordConfigModal()" class="hover:text-slate-300 underline">Configure Discord Client ID</button>
        <span>AES-256-GCM Vault</span>
      </div>
    </div>
  </div>

  <!-- Discord Client ID Settings Modal -->
  <div id="discordConfigModal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm hidden items-center justify-center p-4">
    <div class="pie-card p-6 max-w-md w-full space-y-4 border border-[#1c2333] shadow-2xl">
      <div class="flex items-center justify-between border-b border-[#1c2333] pb-3">
        <h3 class="text-base font-bold text-white">Discord OAuth2 Settings</h3>
        <button onclick="closeModal('discordConfigModal')" class="text-slate-400 hover:text-white">&times;</button>
      </div>

      <div class="space-y-3 text-xs">
        <div>
          <label class="block font-semibold text-slate-300 mb-1">Discord Application Client ID</label>
          <input id="cfgClientId" type="text" placeholder="e.g. 123456789012345678" class="pie-input w-full font-mono">
          <p class="text-[11px] text-slate-500 mt-1">Get this from <a href="https://discord.com/developers/applications" target="_blank" class="text-[#2cf5d6] underline">Discord Developer Portal</a>.</p>
        </div>
        <div>
          <label class="block font-semibold text-slate-300 mb-1">Platform Owner Discord User ID</label>
          <input id="cfgOwnerId" type="text" placeholder="e.g. 987654321098765432" class="pie-input w-full font-mono">
          <p class="text-[11px] text-slate-500 mt-1">When this Discord ID logs in, it automatically unlocks the Admin Panel.</p>
        </div>
      </div>

      <div class="flex items-center justify-end space-x-3 pt-2">
        <button onclick="closeModal('discordConfigModal')" class="btn-secondary text-xs">Cancel</button>
        <button onclick="saveDiscordConfig()" class="btn-primary text-xs">Save & Connect</button>
      </div>
    </div>
  </div>

  <script>
    // Config defaults
    const DEFAULT_DISCORD_CLIENT_ID = '123456789012345678';
    const DEFAULT_OWNER_ID = '987654321098765432';

    function getDiscordClientId() {
      return localStorage.getItem('PIE_MC_DISCORD_CLIENT_ID') || DEFAULT_DISCORD_CLIENT_ID;
    }

    function getOwnerDiscordId() {
      return localStorage.getItem('PIE_MC_OWNER_ID') || DEFAULT_OWNER_ID;
    }

    // Check for Discord OAuth Redirect on Page Load (Hash Fragment or Search Params)
    window.addEventListener('DOMContentLoaded', async () => {
      const hash = window.location.hash;
      const params = new URLSearchParams(window.location.search);

      // Handle Direct Discord Token in URL Hash: #access_token=...&token_type=Bearer
      if (hash && hash.includes('access_token=')) {
        const hashParams = new URLSearchParams(hash.substring(1));
        const accessToken = hashParams.get('access_token');
        if (accessToken) {
          await handleDiscordToken(accessToken);
          return;
        }
      }

      // Handle Backend Callback with user param: ?user=...
      if (params.get('user')) {
        try {
          const userObj = JSON.parse(decodeURIComponent(params.get('user')));
          finalizeLogin(userObj);
          return;
        } catch (e) {}
      }
    });

    // Exchange token with Discord API directly
    async function handleDiscordToken(token) {
      const statusTitle = document.getElementById('statusTitle');
      const statusSubtitle = document.getElementById('statusSubtitle');
      const btn = document.getElementById('btnLoginDiscord');

      statusTitle.innerText = 'Authenticating with Discord...';
      statusSubtitle.innerText = 'Verifying Discord identity and loading workspace partition...';
      btn.disabled = true;

      try {
        const res = await fetch('https://discord.com/api/users/@me', {
          headers: { 'Authorization': `Bearer ${token}` }
        });

        if (!res.ok) throw new Error('Failed to fetch Discord user profile');
        const discordUser = await res.json();

        const ownerId = getOwnerDiscordId();
        const isOwner = (discordUser.id === ownerId);

        const userObj = {
          id: discordUser.id,
          username: discordUser.global_name || discordUser.username,
          discriminator: discordUser.discriminator || '0000',
          avatar: discordUser.avatar 
            ? `https://cdn.discordapp.com/avatars/${discordUser.id}/${discordUser.avatar}.png` 
            : `https://cdn.discordapp.com/embed/avatars/${(parseInt(discordUser.id) || 0) % 5}.png`,
          isOwner: isOwner,
          authTime: new Date().toISOString()
        };

        finalizeLogin(userObj);
      } catch (err) {
        statusTitle.innerText = 'Discord Connection Error';
        statusSubtitle.innerText = err.message + '. Please try logging in again.';
        btn.disabled = false;
      }
    }

    function finalizeLogin(userObj) {
      setCurrentUser(userObj);
      // Clean URL hash/search
      window.history.replaceState({}, document.title, window.location.pathname);
      window.location.href = userObj.isOwner ? 'admin.html' : 'index.html';
    }

    // Main "Login with Discord" trigger
    function startDiscordOAuth() {
      const clientId = getDiscordClientId();
      const redirectUri = encodeURIComponent(window.location.origin + window.location.pathname);

      // If backend endpoint is available, route through backend
      if (window.location.protocol.startsWith('http') && window.location.port === '8082') {
        window.location.href = `/api/auth/discord`;
        return;
      }

      // Direct Discord OAuth2 Authorization URL (Implicit Grant for full client fidelity)
      const discordAuthUrl = `https://discord.com/api/oauth2/authorize?client_id=${clientId}&redirect_uri=${redirectUri}&response_type=token&scope=identify%20guilds`;

      // Open Discord OAuth Login Screen
      window.location.href = discordAuthUrl;
    }

    function openDiscordConfigModal() {
      document.getElementById('cfgClientId').value = getDiscordClientId();
      document.getElementById('cfgOwnerId').value = getOwnerDiscordId();
      openModal('discordConfigModal');
    }

    function saveDiscordConfig() {
      const cid = document.getElementById('cfgClientId').value.trim();
      const oid = document.getElementById('cfgOwnerId').value.trim();

      if (cid) localStorage.setItem('PIE_MC_DISCORD_CLIENT_ID', cid);
      if (oid) localStorage.setItem('PIE_MC_OWNER_ID', oid);

      closeModal('discordConfigModal');
      startDiscordOAuth();
    }
  </script>
</body>
</html>
'''

with open('/working_dir/c_37017e0a3b8a7bd1/pie-mc/public/login.html', 'w', encoding='utf-8') as f:
    f.write(login_html)

print("Updated login.html with single Discord OAuth button and real Discord redirect flow!")
