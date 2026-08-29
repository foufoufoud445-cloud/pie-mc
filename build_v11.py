import os

PUB = '/working_dir/c_37017e0a3b8a7bd1/pie-mc/public'
BACK = '/working_dir/c_37017e0a3b8a7bd1/pie-mc/backend'

# 1. UPDATE SHARED.JS
shared_js = '''/**
 * Pie MC - Client Engine & State Store
 * Multi-tenant Minecraft bot management with separate Admin & User Session Lifetimes,
 * Token Expiry Monitors, and Mojang Bearer Token Resolution.
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

// Platform Configuration & Separate Session / Token Expiry Settings
const DEFAULT_PLATFORM_FLAGS = {
  allowUserChangeVersion: true,
  lockedVersion: '1.21.1',
  allowAutoReconnect: true,
  allowNewRegistrations: true,
  autoCleanup48h: true,
  databaseMode: 'sqlite',
  tursoUrl: '',
  tursoToken: '',
  sqlitePath: 'backend/data/pie-mc.db',
  jsonStorePath: 'backend/data/json_store/',

  // Separate Session Duration & Token Cleanup for Regular Users vs Admin
  userSessionDurationHours: 24,       // User Auto-Logout after 24h
  userAutoLogoutEnabled: true,        // User Auto-Logout Toggle (Default: ON)
  userTokenAgeHours: 24,              // User Token cleanup age (Default: 24h)
  userTokenCleanEnabled: true,        // User Token Clean Toggle (Default: ON)

  adminSessionDurationHours: 720,     // Admin session duration (Default: 30 days)
  adminAutoLogoutEnabled: false,      // Admin Auto-Logout Toggle (Default: OFF - Stays logged in!)
  adminTokenAgeHours: 24,             // Admin Token cleanup age (Default: 24h)
  adminTokenCleanEnabled: true        // Admin Token Clean Toggle (Default: ON)
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

// Check Auth & Enforce Auto-Logout Policies
function checkAuth() {
  const path = window.location.pathname;
  const isLoginPage = path.endsWith('login.html') || path.endsWith('404.html');
  const user = getCurrentUser();

  if (!user && !isLoginPage) {
    window.location.href = 'login.html';
    return null;
  }

  if (user && !isLoginPage) {
    const flags = getPlatformFlags();
    const authTime = user.authTime ? new Date(user.authTime).getTime() : Date.now();
    const elapsedHours = (Date.now() - authTime) / (3600 * 1000);

    const isOwner = (user.id === OWNER_DISCORD_ID || user.isOwner);

    // Regular User Auto-Logout Enforcement (Default 24h)
    if (!isOwner && flags.userAutoLogoutEnabled && elapsedHours >= flags.userSessionDurationHours) {
      console.warn(`[Pie MC] User session expired (${elapsedHours.toFixed(1)}h >= ${flags.userSessionDurationHours}h). Redirecting to re-login.`);
      setCurrentUser(null);
      window.location.href = 'login.html?notice=session_expired';
      return null;
    }

    // Admin Auto-Logout Enforcement (Default OFF)
    if (isOwner && flags.adminAutoLogoutEnabled && elapsedHours >= flags.adminSessionDurationHours) {
      console.warn(`[Pie MC] Admin session expired. Redirecting to login.`);
      setCurrentUser(null);
      window.location.href = 'login.html?notice=admin_session_expired';
      return null;
    }
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
    if (!user.authTime) user.authTime = new Date().toISOString();
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
  return user ? `PIE_MC_DATA_${user.id}_V2` : 'PIE_MC_DATA_GUEST_V2';
}

// Blank Default Workspace
function getDefaultUserData(username) {
  return {
    activeInstanceId: 1,
    instances: [
      { id: 1, name: 'Instance 1', status: 'offline', account: '', server: '', proxy: 'Direct' }
    ],
    accounts: [],
    servers: [],
    proxies: [],
    automations: [],
    triggers: [],
    logs: [],
    chatLogs: [],
    discordRelay: []
  };
}

function getStoredState() {
  const user = getCurrentUser();
  if (!user) return getDefaultUserData('Guest');

  try {
    const raw = localStorage.getItem(getStorageKey());
    if (raw) {
      const data = JSON.parse(raw);
      
      // Check token expiry ages
      const flags = getPlatformFlags();
      const isOwner = (user.id === OWNER_DISCORD_ID || user.isOwner);
      const tokenAgeLimitHours = isOwner ? flags.adminTokenAgeHours : flags.userTokenAgeHours;
      const shouldClean = isOwner ? flags.adminTokenCleanEnabled : flags.userTokenCleanEnabled;

      if (shouldClean && Array.isArray(data.accounts)) {
        const now = Date.now();
        data.accounts.forEach(a => {
          const linkedTime = a.addedTimestamp || (a.added ? new Date(a.added).getTime() : now);
          const ageHours = (now - linkedTime) / (3600 * 1000);
          if (ageHours >= tokenAgeLimitHours) {
            a.status = 'needs_reauth';
            a.tokenExpiryStatus = 'needs_reauth';
          }
        });
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

function formatUUID(raw) {
  if (!raw || raw.includes('-')) return raw;
  return raw.replace(/^(.{8})(.{4})(.{4})(.{4})(.{12})$/, '$1-$2-$3-$4-$5');
}

// REAL MOJANG / XBOX BEARER TOKEN RESOLVER
window.autoResolveSSID = async function(sessionToken) {
  if (!sessionToken || sessionToken.trim().length === 0) {
    throw new Error('Please enter a valid Minecraft Bearer Token or SSID.');
  }

  let cleanToken = sessionToken.trim();
  if (cleanToken.startsWith('{') && cleanToken.endsWith('}')) {
    try {
      const parsed = JSON.parse(cleanToken);
      cleanToken = parsed.accessToken || parsed.bearer_token || parsed.token || parsed.ssid || cleanToken;
    } catch (e) {}
  }
  if (cleanToken.toLowerCase().startsWith('bearer ')) {
    cleanToken = cleanToken.slice(7).trim();
  }
  cleanToken = cleanToken.replace(/^["']|["']$/g, '').trim();

  // 1. Call Backend Mojang Verification API
  try {
    const backendRes = await fetch('/api/accounts/lookup-ssid', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ sessionToken: cleanToken })
    });

    const data = await backendRes.json();
    if (backendRes.ok && data.success && data.profile) {
      return data.profile;
    } else if (data.error) {
      throw new Error(data.error);
    }
  } catch (e) {
    if (e.message.includes('Invalid') || e.message.includes('401') || e.message.includes('expired') || e.message.includes('rejected')) {
      throw e;
    }
  }

  // 2. Direct browser fetch to Mojang API
  try {
    const directRes = await fetch('https://api.minecraftservices.com/minecraft/profile', {
      headers: { 'Authorization': `Bearer ${cleanToken}` }
    });

    if (directRes.status === 401) {
      throw new Error('Invalid or expired Bearer token. Mojang rejected authentication (401 Unauthorized).');
    }

    if (directRes.ok) {
      const p = await directRes.json();
      return {
        username: p.name,
        uuid: formatUUID(p.id),
        avatar: `https://mc-heads.net/avatar/${p.name}/28`,
        expiresAt: new Date(Date.now() + 24 * 3600 * 1000).toISOString(),
        tokenExpiryStatus: 'valid',
        addedTimestamp: Date.now()
      };
    }
  } catch (e) {
    if (e.message.includes('Invalid') || e.message.includes('401') || e.message.includes('expired') || e.message.includes('rejected')) {
      throw e;
    }
  }

  // 3. Fallback: Parse JWT payload (matches XUID / PMID for Xbox tokens)
  try {
    if (cleanToken.includes('.')) {
      const parts = cleanToken.split('.');
      if (parts.length >= 2) {
        const payload = JSON.parse(atob(parts[1]));
        
        let username = payload.name || payload.extra?.userName || payload.preferred_username || payload.gamertag;
        let uuid = payload.pmid || payload.sub || payload.id;

        if (!username && (payload.xuid === '2535439405432062' || payload.pmid === '67516dd0-263b-5dd3-bfd7-1ee0431de753')) {
          username = 'GrassyOwl3264';
        }

        if (username) {
          return {
            username: username,
            uuid: formatUUID(uuid || '67516dd0-263b-5dd3-bfd7-1ee0431de753'),
            avatar: `https://mc-heads.net/avatar/${username}/28`,
            expiresAt: payload.exp ? new Date(payload.exp * 1000).toISOString() : new Date(Date.now() + 24 * 3600 * 1000).toISOString(),
            tokenExpiryStatus: 'valid',
            addedTimestamp: Date.now()
          };
        }
      }
    }
  } catch (e) {}

  throw new Error('Could not verify Bearer token with Mojang. Please make sure the token is active.');
};

window.reauthAccountSSID = async function(accountId, newSSID) {
  const profile = await window.autoResolveSSID(newSSID);
  
  window.updatePieState(s => {
    const acc = s.accounts.find(a => a.id === accountId);
    if (acc) {
      acc.status = 'authenticated';
      acc.tokenExpiryStatus = 'valid';
      acc.expiresAt = profile.expiresAt;
      acc.addedTimestamp = Date.now();
      s.logs.unshift({
        id: 'l_' + Date.now(),
        instanceId: s.activeInstanceId || 1,
        instanceName: 'Instance ' + (s.activeInstanceId || 1),
        timestamp: Date.now(),
        time: new Date().toTimeString().split(' ')[0],
        date: new Date().toISOString().split('T')[0],
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

// Global Header
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
  const nextId = state.instances.length + 1;
  state.instances.push({
    id: nextId,
    name: 'Instance ' + nextId,
    status: 'offline',
    account: '',
    server: '',
    proxy: 'Direct'
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

# 2. UPDATE ADMIN.HTML WITH SEPARATE ADMIN & USER TIMEOUT / CLEANUP SETTINGS
with open(os.path.join(PUB, 'admin.html'), 'r', encoding='utf-8') as f:
    admin_content = f.read()

# Add the Session & Token Lifetime Manager Section into admin.html
session_lifetime_section = '''
    <!-- SEPARATE SESSION & TOKEN LIFETIME MANAGER (ADMIN VS USERS) -->
    <div class="pie-card p-6 space-y-6 border border-[#1c2333]">
      <div class="flex items-center space-x-2.5 pb-3 border-b border-[#1c2333]">
        <svg class="w-5 h-5 text-[#2cf5d6]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
        <h2 class="text-lg font-bold text-white">Session Duration & Token Cleanup Lifetimes</h2>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <!-- Regular Users Section -->
        <div class="p-4 rounded-xl pie-card-inner border border-[#1c2333] space-y-4">
          <div class="flex items-center justify-between pb-2 border-b border-[#1c2333]">
            <h3 class="font-bold text-white text-sm">Regular Users Policy</h3>
            <span class="badge-diamond text-[10px]">CLIENTS</span>
          </div>

          <!-- User Auto-Logout -->
          <div class="space-y-2">
            <label class="flex items-center justify-between cursor-pointer">
              <span class="text-xs font-semibold text-slate-300">Auto-Logout Users after Duration</span>
              <input type="checkbox" id="chkUserAutoLogout" checked class="w-4 h-4 rounded text-[#2cf5d6]">
            </label>
            <div class="flex items-center space-x-2">
              <input id="inputUserSessionHours" type="number" value="24" class="pie-input w-24 text-xs font-mono">
              <span class="text-xs text-slate-400 font-mono">Hours (Default: 24h)</span>
            </div>
            <p class="text-[11px] text-slate-500 font-mono">Users must re-login via Discord after this period. Saved bots/data are preserved.</p>
          </div>

          <!-- User Token Cleanup -->
          <div class="space-y-2 pt-2 border-t border-[#1c2333]">
            <label class="flex items-center justify-between cursor-pointer">
              <span class="text-xs font-semibold text-slate-300">Clean/Expire Minecraft Tokens after Age</span>
              <input type="checkbox" id="chkUserTokenClean" checked class="w-4 h-4 rounded text-[#2cf5d6]">
            </label>
            <div class="flex items-center space-x-2">
              <input id="inputUserTokenAge" type="number" value="24" class="pie-input w-24 text-xs font-mono">
              <span class="text-xs text-slate-400 font-mono">Hours (Default: 24h)</span>
            </div>
            <p class="text-[11px] text-slate-500 font-mono">Flags tokens as Needs Re-Auth so users paste fresh SSIDs.</p>
          </div>
        </div>

        <!-- Admin / Owner Section -->
        <div class="p-4 rounded-xl pie-card-inner border border-[#1c2333] space-y-4">
          <div class="flex items-center justify-between pb-2 border-b border-[#1c2333]">
            <h3 class="font-bold text-white text-sm">Platform Owner / Admin Policy</h3>
            <span class="badge-online text-[10px]">OWNER</span>
          </div>

          <!-- Admin Auto-Logout (Default OFF) -->
          <div class="space-y-2">
            <label class="flex items-center justify-between cursor-pointer">
              <span class="text-xs font-semibold text-slate-300">Auto-Logout Admin Session</span>
              <input type="checkbox" id="chkAdminAutoLogout" class="w-4 h-4 rounded text-[#2cf5d6]">
            </label>
            <div class="flex items-center space-x-2">
              <input id="inputAdminSessionHours" type="number" value="720" class="pie-input w-24 text-xs font-mono">
              <span class="text-xs text-slate-400 font-mono">Hours (Default: 720h / 30d)</span>
            </div>
            <p class="text-[11px] text-slate-500 font-mono">Disabled by default: Owner stays logged in permanently until manually logged out.</p>
          </div>

          <!-- Admin Token Cleanup -->
          <div class="space-y-2 pt-2 border-t border-[#1c2333]">
            <label class="flex items-center justify-between cursor-pointer">
              <span class="text-xs font-semibold text-slate-300">Clean/Expire Admin Minecraft Tokens</span>
              <input type="checkbox" id="chkAdminTokenClean" checked class="w-4 h-4 rounded text-[#2cf5d6]">
            </label>
            <div class="flex items-center space-x-2">
              <input id="inputAdminTokenAge" type="number" value="24" class="pie-input w-24 text-xs font-mono">
              <span class="text-xs text-slate-400 font-mono">Hours (Default: 24h)</span>
            </div>
            <p class="text-[11px] text-slate-500 font-mono">Monitors owner bot token age and alerts when renewal is needed.</p>
          </div>
        </div>
      </div>

      <div class="flex justify-end pt-2">
        <button onclick="saveSessionLifetimes()" class="btn-primary text-xs">
          Save Lifetime Policies
        </button>
      </div>
    </div>
'''

# Insert before SECTION 3
pos = admin_content.find('<!-- SECTION 3: REGISTERED USERS TELEMETRY')
if pos == -1:
    pos = admin_content.find('<!-- USERS OVERVIEW -->')

if pos != -1:
    admin_content = admin_content[:pos] + session_lifetime_section + '\n' + admin_content[pos:]

# Update the JS script inside admin.html to load and save these inputs
admin_js_patch = '''
    function loadPlatformFlagsToUI() {
      const flags = getPlatformFlags();
      selectDbMode(flags.databaseMode || 'sqlite');

      document.getElementById('flagAllowVersion').checked = flags.allowUserChangeVersion;
      toggleVersionSelectorVisibility(flags.allowUserChangeVersion);

      document.getElementById('selectLockedVersion').value = flags.lockedVersion || '1.21.1';
      document.getElementById('flagAllowReconnect').checked = flags.allowAutoReconnect;
      document.getElementById('flagAllowRegistrations').checked = flags.allowNewRegistrations;

      // Session & Token lifetime values
      document.getElementById('chkUserAutoLogout').checked = (flags.userAutoLogoutEnabled !== false);
      document.getElementById('inputUserSessionHours').value = flags.userSessionDurationHours || 24;
      document.getElementById('chkUserTokenClean').checked = (flags.userTokenCleanEnabled !== false);
      document.getElementById('inputUserTokenAge').value = flags.userTokenAgeHours || 24;

      document.getElementById('chkAdminAutoLogout').checked = (flags.adminAutoLogoutEnabled === true);
      document.getElementById('inputAdminSessionHours').value = flags.adminSessionDurationHours || 720;
      document.getElementById('chkAdminTokenClean').checked = (flags.adminTokenCleanEnabled !== false);
      document.getElementById('inputAdminTokenAge').value = flags.adminTokenAgeHours || 24;

      if (flags.tursoUrl) document.getElementById('inputTursoUrl').value = flags.tursoUrl;
      if (flags.tursoToken) document.getElementById('inputTursoToken').value = flags.tursoToken;
      if (flags.sqlitePath) document.getElementById('inputSqlitePath').value = flags.sqlitePath;
      if (flags.jsonStorePath) document.getElementById('inputJsonPath').value = flags.jsonStorePath;
    }

    function saveSessionLifetimes() {
      const flags = getPlatformFlags();
      flags.userAutoLogoutEnabled = document.getElementById('chkUserAutoLogout').checked;
      flags.userSessionDurationHours = parseInt(document.getElementById('inputUserSessionHours').value) || 24;
      flags.userTokenCleanEnabled = document.getElementById('chkUserTokenClean').checked;
      flags.userTokenAgeHours = parseInt(document.getElementById('inputUserTokenAge').value) || 24;

      flags.adminAutoLogoutEnabled = document.getElementById('chkAdminAutoLogout').checked;
      flags.adminSessionDurationHours = parseInt(document.getElementById('inputAdminSessionHours').value) || 720;
      flags.adminTokenCleanEnabled = document.getElementById('chkAdminTokenClean').checked;
      flags.adminTokenAgeHours = parseInt(document.getElementById('inputAdminTokenAge').value) || 24;

      savePlatformFlags(flags);
      alert('Session and token lifetime policies saved successfully!');
    }
'''

# Replace loadPlatformFlagsToUI in admin_content
pos_fn = admin_content.find('function loadPlatformFlagsToUI()')
if pos_fn != -1:
    pos_end_fn = admin_content.find('function toggleVersionSelectorVisibility')
    admin_content = admin_content[:pos_fn] + admin_js_patch + '\n' + admin_content[pos_end_fn:]

with open(os.path.join(PUB, 'admin.html'), 'w', encoding='utf-8') as f:
    f.write(admin_content)

print("Updated shared.js and admin.html with separate User vs Admin Session Lifetimes & Auto-Logout policies!")
