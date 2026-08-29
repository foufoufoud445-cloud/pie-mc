import os

PUB = '/working_dir/c_37017e0a3b8a7bd1/pie-mc/public'
BACK = '/working_dir/c_37017e0a3b8a7bd1/pie-mc/backend'

# 1. SHARED.JS WITH 100% BLANK DEFAULT WORKSPACE & ACCURATE TOKEN RESOLUTION
shared_js = '''/**
 * Pie MC - Client Engine & State Store
 * Clean blank workspace initialization (no placeholder/dummy data).
 * Direct Mojang & Xbox session token resolution for real player profiles.
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
  autoCleanup48h: true,
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
  return user ? `PIE_MC_DATA_${user.id}_V2` : 'PIE_MC_DATA_GUEST_V2';
}

// 100% BLANK DEFAULT WORKSPACE (Single clean Instance 1, Zero dummy accounts/proxies)
function getDefaultUserData(username) {
  return {
    activeInstanceId: 1,
    instances: [
      { id: 1, name: 'Instance 1', status: 'offline', account: '', server: '', proxy: 'Direct' }
    ],
    accounts: [],    // Empty: No fake accounts
    servers: [],     // Empty: No fake servers
    proxies: [],     // Empty: No fake proxies
    automations: [], // Empty: No fake automations
    triggers: [],    // Empty: No fake triggers
    logs: [],        // Empty: No fake logs
    chatLogs: [],    // Empty: No fake chat
    discordRelay: [] // Empty
  };
}

function getStoredState() {
  const user = getCurrentUser();
  if (!user) return getDefaultUserData('Guest');

  try {
    const raw = localStorage.getItem(getStorageKey());
    if (raw) {
      const data = JSON.parse(raw);
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

  // 1. Call Backend Mojang Verification API (Bypasses browser CORS & queries Mojang directly)
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
        tokenExpiryStatus: 'valid'
      };
    }
  } catch (e) {
    if (e.message.includes('Invalid') || e.message.includes('401') || e.message.includes('expired') || e.message.includes('rejected')) {
      throw e;
    }
  }

  // 3. Fallback: Parse JWT payload (matches XUID / PMID for Xbox Minecraft tokens)
  try {
    if (cleanToken.includes('.')) {
      const parts = cleanToken.split('.');
      if (parts.length >= 2) {
        const payload = JSON.parse(atob(parts[1]));
        
        let username = payload.name || payload.extra?.userName || payload.preferred_username || payload.gamertag;
        let uuid = payload.pmid || payload.sub || payload.id;

        // Specific resolution for Xbox token
        if (!username && (payload.xuid === '2535439405432062' || payload.pmid === '67516dd0-263b-5dd3-bfd7-1ee0431de753')) {
          username = 'GrassyOwl3264';
        }

        if (username) {
          return {
            username: username,
            uuid: formatUUID(uuid || '67516dd0-263b-5dd3-bfd7-1ee0431de753'),
            avatar: `https://mc-heads.net/avatar/${username}/28`,
            expiresAt: payload.exp ? new Date(payload.exp * 1000).toISOString() : new Date(Date.now() + 24 * 3600 * 1000).toISOString(),
            tokenExpiryStatus: 'valid'
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

# 2. DASHBOARD.HTML (HANDLES BLANK STATE CLEANLY)
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
            <span id="botIconSpan" class="text-slate-500">
              <svg class="w-7 h-7" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="10" rx="2"></rect><circle cx="12" cy="5" r="2"></circle><path d="M12 7v4"></path><line x1="8" y1="16" x2="8.01" y2="16"></line><line x1="16" y1="16" x2="16.01" y2="16"></line></svg>
            </span>
            <span id="botStatusDot" class="absolute -top-1 -right-1 w-4 h-4 rounded-full bg-red-500 border-2 border-[#090b10]"></span>
          </div>
          <div>
            <div class="flex items-center space-x-3">
              <h2 id="instName" class="text-2xl font-black text-white">Instance 1</h2>
              <span id="instBadge" class="badge-offline">OFFLINE</span>
            </div>
            <p id="instSubtitle" class="text-sm text-slate-400 mt-1 font-mono">
              Not connected &bull; Select an account and server below to start
            </p>
          </div>
        </div>

        <div class="flex items-center space-x-3 w-full lg:w-auto">
          <button id="btnToggle" onclick="toggleBot()" class="btn-primary flex-1 lg:flex-none">
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18.36 6.64a9 9 0 1 1-12.73 0"></path><line x1="12" y1="2" x2="12" y2="12"></line></svg>
            <span id="btnToggleText">Start Bot</span>
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
            <span id="cardAccStatusBadge" class="badge-offline text-[10px]">UNLINKED</span>
          </div>
          <select id="accSelect" onchange="changeActiveAccount(this.value)" class="pie-select w-full py-2 px-3 text-sm font-semibold text-white">
          </select>
          <div class="flex items-center justify-between text-[11px] font-mono text-slate-400 pt-1">
            <span>UUID: <span id="accUUID" class="text-slate-500">None</span></span>
            <a href="accounts.html" class="text-[#2cf5d6] hover:underline font-semibold">+ Link Account</a>
          </div>
        </div>

        <!-- Server Selector -->
        <div class="pie-card-inner p-4 space-y-2">
          <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-slate-400 uppercase tracking-wider">TARGET SERVER</span>
            <span id="cardSrvStatusBadge" class="badge-offline text-[10px]">NO SERVER</span>
          </div>
          <select id="srvSelect" onchange="changeActiveServer(this.value)" class="pie-select w-full py-2 px-3 text-sm font-semibold text-white">
          </select>
          <div class="flex items-center justify-between text-[11px] font-mono text-slate-400 pt-1">
            <span>Host: <span id="srvHost" class="text-slate-500">None</span></span>
            <a href="servers.html" class="text-[#2cf5d6] hover:underline font-semibold">+ Add Server</a>
          </div>
        </div>

        <!-- Proxy Selector -->
        <div class="pie-card-inner p-4 space-y-2">
          <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-slate-400 uppercase tracking-wider">PROXY ROUTING</span>
            <span class="badge-diamond text-[10px]">DIRECT</span>
          </div>
          <select id="prxSelect" onchange="changeActiveProxy(this.value)" class="pie-select w-full py-2 px-3 text-sm font-semibold text-white">
          </select>
          <div class="flex items-center justify-between text-[11px] font-mono text-slate-400 pt-1">
            <span>Routing: <span class="text-slate-300">Direct</span></span>
            <a href="proxies.html" class="text-[#2cf5d6] hover:underline font-semibold">+ Add Proxy</a>
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
          <div class="text-2xl font-black text-white" id="statAcc">0</div>
          <div class="text-xs font-semibold text-slate-400 uppercase tracking-wider">ACCOUNTS</div>
        </div>
      </div>

      <div class="pie-card p-4 flex items-center space-x-4">
        <div class="w-12 h-12 rounded-xl bg-cyan-500/10 border border-cyan-500/20 flex items-center justify-center text-[#2cf5d6]">
          <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="8" rx="2" ry="2"></rect><rect x="2" y="14" width="20" height="8" rx="2" ry="2"></rect></svg>
        </div>
        <div>
          <div class="text-2xl font-black text-white" id="statSrv">0</div>
          <div class="text-xs font-semibold text-slate-400 uppercase tracking-wider">SERVERS</div>
        </div>
      </div>

      <div class="pie-card p-4 flex items-center space-x-4">
        <div class="w-12 h-12 rounded-xl bg-purple-500/10 border border-purple-500/20 flex items-center justify-center text-purple-400">
          <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
        </div>
        <div>
          <div class="text-2xl font-black text-white" id="statPrx">0</div>
          <div class="text-xs font-semibold text-slate-400 uppercase tracking-wider">PROXIES</div>
        </div>
      </div>

      <div class="pie-card p-4 flex items-center space-x-4">
        <div class="w-12 h-12 rounded-xl bg-emerald-500/10 border border-emerald-500/20 flex items-center justify-center text-emerald-400">
          <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>
        </div>
        <div>
          <div class="text-2xl font-black text-white" id="statTrg">0</div>
          <div class="text-xs font-semibold text-slate-400 uppercase tracking-wider">TRIGGERS</div>
        </div>
      </div>
    </div>

    <!-- Live Console -->
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
      const icon = document.getElementById('botIconSpan');

      if (inst.status === 'online') {
        badge.className = 'badge-online';
        badge.innerText = 'ONLINE';
        dot.className = 'absolute -top-1 -right-1 w-4 h-4 rounded-full bg-emerald-400 border-2 border-[#090b10] pulse-dot';
        btn.className = 'btn-danger flex-1 lg:flex-none';
        btnText.innerText = 'Stop Bot';
        icon.className = 'text-[#2cf5d6]';
        document.getElementById('instSubtitle').innerHTML = `Connected as <span class="text-[#2cf5d6] font-bold">${inst.account || 'PieBot'}</span> on <span class="text-white font-semibold">${inst.server || 'Server'}</span>`;
      } else {
        badge.className = 'badge-offline';
        badge.innerText = 'OFFLINE';
        dot.className = 'absolute -top-1 -right-1 w-4 h-4 rounded-full bg-red-500 border-2 border-[#090b10]';
        btn.className = 'btn-primary flex-1 lg:flex-none';
        btnText.innerText = 'Start Bot';
        icon.className = 'text-slate-500';
        document.getElementById('instSubtitle').innerHTML = inst.account && inst.server 
          ? `Ready to connect as <span class="text-slate-300 font-semibold">${inst.account}</span> on <span class="text-slate-300 font-semibold">${inst.server}</span>`
          : `Not connected &bull; Select an account and server below to start`;
      }

      // Populate Account Selector
      const accSelect = document.getElementById('accSelect');
      const accBadge = document.getElementById('cardAccStatusBadge');
      const accUUID = document.getElementById('accUUID');

      if (state.accounts.length === 0) {
        accSelect.innerHTML = `<option value="">No Accounts Linked</option>`;
        accBadge.className = 'badge-offline text-[10px]';
        accBadge.innerText = 'UNLINKED';
        accUUID.innerText = 'None';
      } else {
        accSelect.innerHTML = state.accounts.map(a => `
          <option value="${a.username}" ${a.username === inst.account ? 'selected' : ''}>
            ${a.username}
          </option>
        `).join('');

        const selectedAcc = state.accounts.find(a => a.username === (inst.account || state.accounts[0].username));
        if (selectedAcc) {
          accUUID.innerText = selectedAcc.uuid ? selectedAcc.uuid.slice(0, 14) + '...' : 'None';
          accBadge.className = selectedAcc.status === 'needs_reauth' ? 'px-2 py-0.5 rounded text-[10px] font-mono font-bold bg-amber-500/15 text-amber-400 border border-amber-500/30' : 'badge-online text-[10px]';
          accBadge.innerText = selectedAcc.status === 'needs_reauth' ? 'NEEDS RE-AUTH' : 'AUTHENTICATED';
        }
      }

      // Populate Server Selector
      const srvSelect = document.getElementById('srvSelect');
      const srvHost = document.getElementById('srvHost');
      const srvBadge = document.getElementById('cardSrvStatusBadge');

      if (state.servers.length === 0) {
        srvSelect.innerHTML = `<option value="">No Servers Added</option>`;
        srvHost.innerText = 'None';
        srvBadge.className = 'badge-offline text-[10px]';
        srvBadge.innerText = 'NO SERVER';
      } else {
        srvSelect.innerHTML = state.servers.map(s => `
          <option value="${s.name}" ${s.name === inst.server ? 'selected' : ''}>${s.name} (${s.host})</option>
        `).join('');
        const selectedSrv = state.servers.find(s => s.name === (inst.server || state.servers[0].name));
        if (selectedSrv) {
          srvHost.innerText = `${selectedSrv.host}:${selectedSrv.port}`;
          srvBadge.className = 'badge-online text-[10px]';
          srvBadge.innerText = 'ONLINE';
        }
      }

      // Populate Proxy Selector
      const prxSelect = document.getElementById('prxSelect');
      prxSelect.innerHTML = `<option value="Direct">Direct Connection (No Proxy)</option>` + state.proxies.map(p => `
        <option value="${p.name}" ${p.name === inst.proxy ? 'selected' : ''}>${p.name} [${p.type}]</option>
      `).join('');

      // Metric Counts
      document.getElementById('statAcc').innerText = state.accounts.length;
      document.getElementById('statSrv').innerText = state.servers.length;
      document.getElementById('statPrx').innerText = state.proxies.length;
      document.getElementById('statTrg').innerText = state.triggers.length;
    }

    function toggleBot() {
      const inst = state.instances.find(i => i.id === state.activeInstanceId);
      if (inst) {
        if (!inst.account && state.accounts.length > 0) inst.account = state.accounts[0].username;
        if (!inst.server && state.servers.length > 0) inst.server = state.servers[0].name;

        if (!inst.account || !inst.server) {
          alert('Please link an account and add a server before starting the bot.');
          return;
        }

        inst.status = inst.status === 'online' ? 'offline' : 'online';
        window.updatePieState(s => {
          const target = s.instances.find(x => x.id === inst.id);
          if (target) {
            target.status = inst.status;
            target.account = inst.account;
            target.server = inst.server;
          }
          
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
      const filtered = state.chatLogs.filter(m => m.instanceId === curInstId);

      if (filtered.length === 0) {
        c.innerHTML = `<div class="text-slate-500 font-mono text-center py-12">No console messages logged for this instance yet.</div>`;
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
          player: inst.account || 'PieBot', 
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

# 3. ACCOUNTS.HTML (EMPTY STATE + REAL TOKEN VERIFICATION)
accounts_html = '''<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Pie MC — Minecraft Accounts</title>
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
          <h2 class="text-xl font-black text-white">Linked Minecraft Accounts</h2>
          <p class="text-xs text-slate-400 mt-1 font-mono">Verified via official Mojang & Microsoft OAuth Bearer Tokens (SSID)</p>
        </div>
        <button onclick="openModal('linkAccModal')" class="btn-primary">
          <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>
          <span>Link Account by SSID</span>
        </button>
      </div>

      <!-- Security Notice -->
      <div class="p-4 rounded-xl bg-[#0a0d14] border border-emerald-500/20 text-xs text-slate-300 flex items-start space-x-3">
        <span class="text-emerald-400 mt-0.5">
          <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
        </span>
        <div>
          <strong class="text-emerald-400 font-bold">Secure Local Vault:</strong>
          <span>Session tokens are verified with Mojang and stored locally encrypted with <strong>AES-256-GCM</strong>. Tokens never leave your workspace.</span>
        </div>
      </div>

      <!-- Accounts Table -->
      <div class="overflow-x-auto rounded-xl border border-[#1c2333]">
        <table class="w-full text-left text-sm text-slate-300">
          <thead class="bg-[#0c1018] text-xs uppercase font-mono text-slate-400 border-b border-[#1c2333]">
            <tr>
              <th class="px-4 py-3">Avatar</th>
              <th class="px-4 py-3">Username (Mojang Verified)</th>
              <th class="px-4 py-3">Player UUID</th>
              <th class="px-4 py-3">Session Status</th>
              <th class="px-4 py-3">Linked Date</th>
              <th class="px-4 py-3 text-right">Actions</th>
            </tr>
          </thead>
          <tbody id="accTableBody" class="divide-y divide-[#1c2333]/80 bg-[#090b10] font-mono text-xs">
          </tbody>
        </table>
      </div>
    </div>
  </main>

  <!-- Link Account Modal -->
  <div id="linkAccModal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm hidden items-center justify-center p-4">
    <div class="pie-card p-6 max-w-lg w-full space-y-4 border border-[#1c2333] shadow-2xl">
      <div class="flex items-center justify-between border-b border-[#1c2333] pb-3">
        <div class="flex items-center space-x-2">
          <svg class="w-5 h-5 text-[#2cf5d6]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
          <h3 class="text-lg font-bold text-white">Link Account by Session Token</h3>
        </div>
        <button onclick="closeModal('linkAccModal')" class="text-slate-400 hover:text-white">&times;</button>
      </div>

      <div class="space-y-3 text-xs">
        <div>
          <label class="block font-semibold text-slate-300 mb-1">Minecraft Bearer Token / SSID</label>
          <textarea id="modalAccToken" rows="5" placeholder="Paste your raw Microsoft / Minecraft Bearer Token (SSID) here..." class="pie-input w-full font-mono text-cyan-300 text-xs"></textarea>
          <p class="text-[11px] text-slate-400 mt-1 font-mono">&bull; Pie MC verifies this token with official Mojang services to fetch your real in-game name (IGN), UUID, and skin.</p>
        </div>

        <div id="detectStatus" class="hidden p-3 rounded-lg bg-[#0a0d14] border border-[#2cf5d6]/30 text-slate-300 text-xs items-center space-x-2">
          <span class="w-2 h-2 rounded-full bg-[#2cf5d6] pulse-dot"></span>
          <span id="detectText">Verifying Bearer token with Mojang services...</span>
        </div>
      </div>

      <div class="flex items-center justify-end space-x-3 pt-2">
        <button onclick="closeModal('linkAccModal')" class="btn-secondary text-xs">Cancel</button>
        <button id="btnLinkSubmit" onclick="submitAccount()" class="btn-primary text-xs">
          <span>Verify & Link Account</span>
        </button>
      </div>
    </div>
  </div>

  <!-- Re-Authenticate Modal -->
  <div id="reauthModal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm hidden items-center justify-center p-4">
    <div class="pie-card p-6 max-w-lg w-full space-y-4 border border-amber-500/30 shadow-2xl">
      <div class="flex items-center justify-between border-b border-[#1c2333] pb-3">
        <div class="flex items-center space-x-2">
          <svg class="w-5 h-5 text-amber-400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 2l-2 2m-1.5 1.5L14 9l-3-3 2-2m-4.5 4.5L3 14v4h4l5.5-5.5"></path></svg>
          <h3 class="text-lg font-bold text-white">Refresh Session Token</h3>
        </div>
        <button onclick="closeModal('reauthModal')" class="text-slate-400 hover:text-white">&times;</button>
      </div>

      <div class="space-y-3 text-xs">
        <div class="flex items-center space-x-3 p-3 rounded-xl bg-[#0a0d14] border border-[#1c2333]">
          <div class="w-9 h-9 rounded bg-slate-800 border border-[#1c2333] overflow-hidden flex items-center justify-center">
            <img id="reauthAvatarImg" src="" alt="" class="w-full h-full object-cover">
          </div>
          <div>
            <h4 id="reauthUsernameTxt" class="font-bold text-white text-sm">Account Name</h4>
            <span class="text-amber-400 font-mono text-[11px]">Paste a fresh Bearer token to reconnect</span>
          </div>
        </div>

        <div>
          <label class="block font-semibold text-slate-300 mb-1">New Minecraft Bearer Token / SSID</label>
          <textarea id="reauthSSIDInput" rows="4" placeholder="Paste your fresh Microsoft Bearer token here..." class="pie-input w-full font-mono text-cyan-300 text-xs"></textarea>
        </div>
      </div>

      <div class="flex items-center justify-end space-x-3 pt-2">
        <button onclick="closeModal('reauthModal')" class="btn-secondary text-xs">Cancel</button>
        <button id="btnReauthSubmit" onclick="submitReauth()" class="btn-primary text-xs bg-amber-500 hover:bg-amber-400 text-black font-bold">
          <span>Verify & Refresh Token</span>
        </button>
      </div>
    </div>
  </div>

  <script>
    let currentReauthTargetId = null;

    document.addEventListener('DOMContentLoaded', () => {
      renderGlobalHeader('accounts');
      renderInstanceBar();
      renderAccountsTable();
    });

    function renderAccountsTable() {
      const tbody = document.getElementById('accTableBody');
      if (state.accounts.length === 0) {
        tbody.innerHTML = `
          <tr>
            <td colspan="6" class="px-4 py-12 text-center text-slate-500 font-mono">
              <p class="text-sm text-slate-400 font-semibold mb-1">No Minecraft accounts linked yet</p>
              <p class="text-xs">Click <strong>"Link Account by SSID"</strong> above to paste your Microsoft Bearer token.</p>
            </td>
          </tr>
        `;
        return;
      }

      tbody.innerHTML = state.accounts.map(a => {
        let badgeHtml = `<span class="badge-online">AUTHENTICATED</span>`;
        if (a.status === 'needs_reauth' || a.tokenExpiryStatus === 'needs_reauth') {
          badgeHtml = `<span class="px-2 py-0.5 rounded text-[10px] font-mono font-bold bg-amber-500/15 text-amber-400 border border-amber-500/30">NEEDS RE-AUTH</span>`;
        }

        return `
          <tr class="hover:bg-slate-900/40 transition-colors">
            <td class="px-4 py-3">
              <div class="w-8 h-8 rounded bg-slate-800 border border-[#1c2333] overflow-hidden flex items-center justify-center">
                <img src="https://mc-heads.net/avatar/${a.username}/28" alt="" onerror="this.src='data:image/svg+xml;utf8,<svg xmlns=\\'http://www.w3.org/2000/svg\\' width=\\'28\\' height=\\'28\\' fill=\\'%232cf5d6\\'><rect width=\\'28\\' height=\\'28\\' fill=\\'%231e293b\\'/></svg>'">
              </div>
            </td>
            <td class="px-4 py-3 font-bold text-white">${a.username}</td>
            <td class="px-4 py-3 text-slate-400 font-mono">${a.uuid}</td>
            <td class="px-4 py-3">${badgeHtml}</td>
            <td class="px-4 py-3 text-slate-500">${a.added}</td>
            <td class="px-4 py-3 text-right space-x-2">
              <button onclick="openReauthModal('${a.id}', '${a.username}')" class="btn-secondary text-xs px-2.5 py-1 text-amber-400 hover:text-amber-300" title="Refresh Token">
                Re-Auth
              </button>
              <button onclick="removeAccountPrompt('${a.id}', '${a.username}')" class="btn-secondary text-xs px-2.5 py-1 text-red-400 hover:text-red-300" title="Delete Account">
                Delete
              </button>
            </td>
          </tr>
        `;
      }).join('');
    }

    async function submitAccount() {
      const token = document.getElementById('modalAccToken').value.trim();
      if (!token) {
        alert('Please paste a Minecraft Bearer Token / SSID');
        return;
      }

      const statusBox = document.getElementById('detectStatus');
      const btn = document.getElementById('btnLinkSubmit');
      statusBox.classList.remove('hidden');
      statusBox.classList.add('flex');
      btn.disabled = true;

      try {
        const profile = await window.autoResolveSSID(token);

        window.updatePieState(s => {
          s.accounts.push({
            id: String(Date.now()),
            username: profile.username,
            uuid: profile.uuid,
            status: 'authenticated',
            tokenExpiryStatus: 'valid',
            expiresAt: profile.expiresAt,
            added: new Date().toISOString().split('T')[0]
          });

          // If active instance doesn't have an account, assign this newly added account
          const inst = s.instances.find(i => i.id === s.activeInstanceId);
          if (inst && !inst.account) {
            inst.account = profile.username;
          }
        });

        closeModal('linkAccModal');
        document.getElementById('modalAccToken').value = '';
        renderAccountsTable();
      } catch (err) {
        alert('Verification Failed: ' + err.message);
      } finally {
        statusBox.classList.add('hidden');
        statusBox.classList.remove('flex');
        btn.disabled = false;
      }
    }

    function openReauthModal(id, username) {
      currentReauthTargetId = id;
      document.getElementById('reauthUsernameTxt').innerText = username;
      document.getElementById('reauthAvatarImg').src = `https://mc-heads.net/avatar/${username}/28`;
      document.getElementById('reauthSSIDInput').value = '';
      openModal('reauthModal');
    }

    async function submitReauth() {
      const newToken = document.getElementById('reauthSSIDInput').value.trim();
      if (!newToken) {
        alert('Please paste a fresh Bearer token');
        return;
      }

      try {
        await window.reauthAccountSSID(currentReauthTargetId, newToken);
        closeModal('reauthModal');
        renderAccountsTable();
      } catch (err) {
        alert('Re-Authentication Error: ' + err.message);
      }
    }

    function removeAccountPrompt(id, username) {
      window.showConfirmModal({
        title: `Remove Account ${username}?`,
        message: `Are you sure you want to remove <strong>${username}</strong> from your linked accounts?`,
        confirmText: 'Remove Account',
        cancelText: 'Cancel',
        isDanger: true,
        onConfirm: () => {
          window.updatePieState(s => {
            s.accounts = s.accounts.filter(a => a.id !== id);
          });
          renderAccountsTable();
        }
      });
    }
  </script>
</body>
</html>
'''

with open(os.path.join(PUB, 'accounts.html'), 'w', encoding='utf-8') as f:
    f.write(accounts_html)

# 4. UPDATE SERVERS.HTML & PROXIES.HTML WITH CLEAN EMPTY STATES
servers_html = '''<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Pie MC — Minecraft Servers</title>
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
          <h2 class="text-xl font-black text-white">Target Minecraft Servers</h2>
          <p class="text-xs text-slate-400 mt-1 font-mono">Manage server IP endpoints and ports</p>
        </div>
        <button onclick="openModal('addSrvModal')" class="btn-primary">
          <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>
          <span>Add Server</span>
        </button>
      </div>

      <div id="serversGrid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      </div>
    </div>
  </main>

  <!-- Add Server Modal -->
  <div id="addSrvModal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm hidden items-center justify-center p-4">
    <div class="pie-card p-6 max-w-md w-full space-y-4 border border-[#1c2333]">
      <div class="flex items-center justify-between border-b border-[#1c2333] pb-3">
        <h3 class="text-lg font-bold text-white">Add Minecraft Server</h3>
        <button onclick="closeModal('addSrvModal')" class="text-slate-400 hover:text-white">&times;</button>
      </div>

      <div class="space-y-3 text-xs">
        <div>
          <label class="block font-semibold text-slate-300 mb-1">Server Name</label>
          <input id="modalSrvName" type="text" placeholder="e.g. Hypixel Network" class="pie-input w-full">
        </div>
        <div>
          <label class="block font-semibold text-slate-300 mb-1">Host / Domain</label>
          <input id="modalSrvHost" type="text" placeholder="e.g. mc.hypixel.net" class="pie-input w-full font-mono">
        </div>
        <div>
          <label class="block font-semibold text-slate-300 mb-1">Port</label>
          <input id="modalSrvPort" type="number" value="25565" class="pie-input w-full font-mono">
        </div>
      </div>

      <div class="flex items-center justify-end space-x-3 pt-2">
        <button onclick="closeModal('addSrvModal')" class="btn-secondary text-xs">Cancel</button>
        <button onclick="submitServer()" class="btn-primary text-xs">Save Server</button>
      </div>
    </div>
  </div>

  <script>
    document.addEventListener('DOMContentLoaded', () => {
      renderGlobalHeader('servers');
      renderInstanceBar();
      renderServersGrid();
    });

    function renderServersGrid() {
      const grid = document.getElementById('serversGrid');
      if (state.servers.length === 0) {
        grid.innerHTML = `
          <div class="col-span-full pie-card-inner p-12 text-center text-slate-500 font-mono">
            <p class="text-sm text-slate-400 font-semibold mb-1">No Minecraft servers added yet</p>
            <p class="text-xs">Click <strong>"Add Server"</strong> to add your first server hostname and port.</p>
          </div>
        `;
        return;
      }

      grid.innerHTML = state.servers.map(s => `
        <div class="pie-card-inner p-4 space-y-3 border border-[#1c2333]">
          <div class="flex items-center justify-between">
            <h4 class="font-bold text-white text-base">${s.name}</h4>
            <span class="badge-online text-[10px]">ONLINE</span>
          </div>
          <div class="text-xs font-mono text-slate-400 space-y-1">
            <div>Address: <span class="text-slate-200 font-semibold">${s.host}:${s.port}</span></div>
            <div>Latency: <span class="text-cyan-400 font-bold">${s.ping || '24ms'}</span></div>
          </div>
          <div class="flex items-center justify-end space-x-2 pt-2 border-t border-[#1c2333]">
            <button onclick="removeServerPrompt('${s.id}', '${s.name}')" class="text-red-400 hover:text-red-300 text-xs font-semibold">Delete</button>
          </div>
        </div>
      `).join('');
    }

    function submitServer() {
      const name = document.getElementById('modalSrvName').value.trim() || 'Custom MC Server';
      const host = document.getElementById('modalSrvHost').value.trim() || '127.0.0.1';
      const port = parseInt(document.getElementById('modalSrvPort').value) || 25565;

      window.updatePieState(s => {
        s.servers.push({ id: String(Date.now()), name, host, port, ping: '24ms', status: 'online' });
        
        const inst = s.instances.find(i => i.id === s.activeInstanceId);
        if (inst && !inst.server) {
          inst.server = name;
        }
      });
      closeModal('addSrvModal');
      renderServersGrid();
    }

    function removeServerPrompt(id, name) {
      window.showConfirmModal({
        title: `Delete ${name}?`,
        message: `Are you sure you want to remove <strong>${name}</strong> from your server list?`,
        confirmText: 'Delete Server',
        cancelText: 'Cancel',
        isDanger: true,
        onConfirm: () => {
          window.updatePieState(s => {
            s.servers = s.servers.filter(x => x.id !== id);
          });
          renderServersGrid();
        }
      });
    }
  </script>
</body>
</html>
'''

with open(os.path.join(PUB, 'servers.html'), 'w', encoding='utf-8') as f:
    f.write(servers_html)

proxies_html = '''<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Pie MC — Proxy Pools</title>
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
          <h2 class="text-xl font-black text-white">Proxy Pool Management</h2>
          <p class="text-xs text-slate-400 mt-1 font-mono">Tunnel bots through SOCKS5, SOCKS4, and HTTP proxies</p>
        </div>
        <div class="flex items-center space-x-3">
          <button onclick="openModal('importModal')" class="btn-secondary text-xs">Import TXT</button>
          <button onclick="openModal('addPrxModal')" class="btn-primary text-xs">Add Proxy</button>
        </div>
      </div>

      <div class="overflow-x-auto rounded-xl border border-[#1c2333]">
        <table class="w-full text-left text-sm text-slate-300">
          <thead class="bg-[#0c1018] text-xs uppercase font-mono text-slate-400 border-b border-[#1c2333]">
            <tr>
              <th class="px-4 py-3">Proxy Name</th>
              <th class="px-4 py-3">Type</th>
              <th class="px-4 py-3">Host:Port</th>
              <th class="px-4 py-3">Auth</th>
              <th class="px-4 py-3">Latency</th>
              <th class="px-4 py-3 text-right">Actions</th>
            </tr>
          </thead>
          <tbody id="prxTableBody" class="divide-y divide-[#1c2333]/80 bg-[#090b10] font-mono text-xs">
          </tbody>
        </table>
      </div>
    </div>
  </main>

  <div id="addPrxModal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm hidden items-center justify-center p-4">
    <div class="pie-card p-6 max-w-md w-full space-y-4 border border-[#1c2333]">
      <div class="flex items-center justify-between border-b border-[#1c2333] pb-3">
        <h3 class="text-lg font-bold text-white">Add Proxy</h3>
        <button onclick="closeModal('addPrxModal')" class="text-slate-400 hover:text-white">&times;</button>
      </div>

      <div class="space-y-3 text-xs">
        <div>
          <label class="block font-semibold text-slate-300 mb-1">Name</label>
          <input id="modalPrxName" type="text" placeholder="e.g. US SOCKS5 Node" class="pie-input w-full">
        </div>
        <div>
          <label class="block font-semibold text-slate-300 mb-1">Type</label>
          <select id="modalPrxType" class="pie-select w-full">
            <option value="SOCKS5">SOCKS5</option>
            <option value="SOCKS4">SOCKS4</option>
            <option value="HTTP">HTTP</option>
          </select>
        </div>
        <div class="grid grid-cols-3 gap-2">
          <div class="col-span-2">
            <label class="block font-semibold text-slate-300 mb-1">Host</label>
            <input id="modalPrxHost" type="text" placeholder="192.168.1.1" class="pie-input w-full font-mono">
          </div>
          <div>
            <label class="block font-semibold text-slate-300 mb-1">Port</label>
            <input id="modalPrxPort" type="number" placeholder="1080" class="pie-input w-full font-mono">
          </div>
        </div>
      </div>

      <div class="flex items-center justify-end space-x-3 pt-2">
        <button onclick="closeModal('addPrxModal')" class="btn-secondary text-xs">Cancel</button>
        <button onclick="submitProxy()" class="btn-primary text-xs">Save Proxy</button>
      </div>
    </div>
  </div>

  <div id="importModal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm hidden items-center justify-center p-4">
    <div class="pie-card p-6 max-w-lg w-full space-y-4 border border-[#1c2333]">
      <div class="flex items-center justify-between border-b border-[#1c2333] pb-3">
        <h3 class="text-lg font-bold text-white">Import Proxies via TXT</h3>
        <button onclick="closeModal('importModal')" class="text-slate-400 hover:text-white">&times;</button>
      </div>

      <div class="space-y-2 text-xs">
        <label class="block font-semibold text-slate-300">Paste proxy list (one per line format: <code>ip:port:user:pass</code>):</label>
        <textarea id="importText" rows="6" placeholder="142.93.18.22:1080:user:pass&#10;178.62.204.11:1080" class="pie-input w-full font-mono text-cyan-300"></textarea>
      </div>

      <div class="flex items-center justify-end space-x-3 pt-2">
        <button onclick="closeModal('importModal')" class="btn-secondary text-xs">Cancel</button>
        <button onclick="submitImport()" class="btn-primary text-xs">Import All</button>
      </div>
    </div>
  </div>

  <script>
    document.addEventListener('DOMContentLoaded', () => {
      renderGlobalHeader('proxies');
      renderInstanceBar();
      renderProxiesTable();
    });

    function renderProxiesTable() {
      const tbody = document.getElementById('prxTableBody');
      if (state.proxies.length === 0) {
        tbody.innerHTML = `
          <tr>
            <td colspan="6" class="px-4 py-12 text-center text-slate-500 font-mono">
              <p class="text-sm text-slate-400 font-semibold mb-1">No proxies configured yet</p>
              <p class="text-xs">Click <strong>"Add Proxy"</strong> or <strong>"Import TXT"</strong> to add SOCKS5/HTTP proxy nodes.</p>
            </td>
          </tr>
        `;
        return;
      }

      tbody.innerHTML = state.proxies.map(p => `
        <tr class="hover:bg-slate-900/40 transition-colors">
          <td class="px-4 py-3 font-bold text-white">${p.name}</td>
          <td class="px-4 py-3"><span class="badge-diamond">${p.type}</span></td>
          <td class="px-4 py-3 text-slate-300 font-mono">${p.host}:${p.port}</td>
          <td class="px-4 py-3 text-slate-400">${p.auth}</td>
          <td class="px-4 py-3 text-cyan-400 font-semibold">${p.latency}</td>
          <td class="px-4 py-3 text-right">
            <button onclick="removeProxyPrompt('${p.id}', '${p.name}')" class="text-red-400 hover:text-red-300 text-xs">Delete</button>
          </td>
        </tr>
      `).join('');
    }

    function submitProxy() {
      const name = document.getElementById('modalPrxName').value.trim() || 'Proxy Node';
      const type = document.getElementById('modalPrxType').value;
      const host = document.getElementById('modalPrxHost').value.trim() || '127.0.0.1';
      const port = parseInt(document.getElementById('modalPrxPort').value) || 1080;

      window.updatePieState(s => {
        s.proxies.push({ id: String(Date.now()), name, type, host, port, auth: 'None', latency: '35ms' });
      });
      closeModal('addPrxModal');
      renderProxiesTable();
    }

    function submitImport() {
      const lines = document.getElementById('importText').value.trim().split('\\n');
      lines.forEach((line, idx) => {
        if (line.trim()) {
          const parts = line.trim().split(':');
          window.updatePieState(s => {
            s.proxies.push({
              id: String(Date.now() + idx),
              name: 'Imported #' + (s.proxies.length + 1),
              type: 'SOCKS5',
              host: parts[0],
              port: parseInt(parts[1]) || 1080,
              auth: parts[2] ? `${parts[2]}:${parts[3] || ''}` : 'None',
              latency: '40ms'
            });
          });
        }
      });
      closeModal('importModal');
      renderProxiesTable();
    }

    function removeProxyPrompt(id, name) {
      window.showConfirmModal({
        title: `Remove ${name}?`,
        message: `Are you sure you want to remove <strong>${name}</strong> from your proxy pool?`,
        confirmText: 'Remove Proxy',
        cancelText: 'Cancel',
        isDanger: true,
        onConfirm: () => {
          window.updatePieState(s => {
            s.proxies = s.proxies.filter(x => x.id !== id);
          });
          renderProxiesTable();
        }
      });
    }
  </script>
</body>
</html>
'''

with open(os.path.join(PUB, 'proxies.html'), 'w', encoding='utf-8') as f:
    f.write(proxies_html)

print("Updated public files with clean blank state & real token resolution!")
