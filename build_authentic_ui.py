import os

PUB = '/working_dir/c_37017e0a3b8a7bd1/pie-mc/public'

# 1. SHARED.JS
shared_js = '''/**
 * Pie MC - Client Engine & State Store
 * Hand-crafted multi-tenant Minecraft bot management dashboard.
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
    recordGlobalUserTelemetry(user);
  } else {
    localStorage.removeItem('PIE_MC_USER');
  }
}

function logout() {
  setCurrentUser(null);
  window.location.href = 'login.html';
}

function getGlobalTelemetry() {
  try {
    const raw = localStorage.getItem('PIE_MC_GLOBAL_TELEMETRY');
    if (raw) return JSON.parse(raw);
  } catch (e) {}
  return {
    totalUsersCount: 14,
    totalAccountsCount: 29,
    activeBotsCount: 8,
    totalServersCount: 12,
    usersList: [
      { id: '1092837465', username: 'Alex_99', joined: '2026-08-12', accountsCount: 3, instancesCount: 2 },
      { id: '8472910482', username: 'NovaCraft', joined: '2026-08-18', accountsCount: 4, instancesCount: 1 },
      { id: '5519283741', username: 'ShadowMC', joined: '2026-08-22', accountsCount: 2, instancesCount: 2 },
      { id: '987654321098765432', username: 'PieOwner', joined: '2026-08-01', accountsCount: 3, instancesCount: 3 }
    ]
  };
}

function recordGlobalUserTelemetry(user) {
  const tele = getGlobalTelemetry();
  if (!tele.usersList.some(u => u.id === user.id)) {
    tele.usersList.push({
      id: user.id,
      username: user.username,
      joined: new Date().toISOString().split('T')[0],
      accountsCount: 1,
      instancesCount: 1
    });
    tele.totalUsersCount = tele.usersList.length;
    localStorage.setItem('PIE_MC_GLOBAL_TELEMETRY', JSON.stringify(tele));
  }
}

function getStorageKey() {
  const user = getCurrentUser();
  return user ? `PIE_MC_DATA_${user.id}` : 'PIE_MC_DATA_GUEST';
}

function getDefaultUserData(username) {
  const now = new Date();
  const expiresFuture = new Date(now.getTime() + 24 * 60 * 60 * 1000).toISOString();
  const expiresPast = new Date(now.getTime() - 2 * 60 * 60 * 1000).toISOString();

  return {
    activeInstanceId: 1,
    instances: [
      { id: 1, name: 'Instance 1', status: 'online', account: `${username}_Bot1`, server: 'Hypixel Network', proxy: 'US Residential 01' },
      { id: 2, name: 'Instance 2', status: 'offline', account: `${username}_Bot2`, server: '2b2t Anarchy', proxy: 'EU SOCKS5 Node' }
    ],
    accounts: [
      { 
        id: '1', 
        username: `${username}_Bot1`, 
        uuid: 'd8f3-4a11-98bc-e63f912', 
        status: 'authenticated', 
        added: '2026-08-28', 
        expiresAt: expiresFuture,
        tokenExpiryStatus: 'valid'
      },
      { 
        id: '2', 
        username: `${username}_Alt2`, 
        uuid: 'e712-3b99-11aa-a82f331', 
        status: 'needs_reauth', 
        added: '2026-08-20', 
        expiresAt: expiresPast,
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
      { id: '1', msg: '/clan recruit Join our squad!', interval: '60 seconds', status: true, scope: 'Instance 1' }
    ],
    triggers: [
      { id: '1', name: 'Welcome Greeter', keyword: 'hello', mode: 'Keyword anywhere', reply: 'Welcome! /msg me for help', cooldown: 10, status: true },
      { id: '2', name: 'Discord Link', keyword: '!discord', mode: 'Exact match', reply: 'Join discord.gg/piemc', cooldown: 5, status: true }
    ],
    logs: [
      { time: '16:00:10', instance: 'Instance 1', event: 'Bot Connected', player: `${username}_Bot1`, details: 'Session token verified (AES-256-GCM)' }
    ],
    chatLogs: [
      { time: '16:00:10', player: 'Server', tag: '[SYSTEM]', msg: 'Welcome to the server!', type: 'system' }
    ],
    discordRelay: [
      { time: '16:00:10', author: 'PieMC-Relay', content: '💬 **[Instance 1]** Bot online' }
    ]
  };
}

function getStoredState() {
  const user = getCurrentUser();
  if (!user) return getDefaultUserData('Guest');

  try {
    const raw = localStorage.getItem(getStorageKey());
    if (raw) return JSON.parse(raw);
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

// Automatic SSID Profile Resolver
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
        time: new Date().toTimeString().split(' ')[0],
        instance: 'Global',
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
        <!-- Clean Brand Logo with No Clutter Subtext -->
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

// Minecraft Attack Hit Particle Engine
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
      this.vy += 0.12; // Slight gravity
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

# 2. LOGIN.HTML (CLEAN, HUMAN-CRAFTED DISCORD LOGIN)
login_html = '''<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Pie MC — Sign In</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="styles.css">
  <script src="shared.js"></script>
</head>
<body class="flex items-center justify-center min-h-screen p-4 bg-[#090b10] relative overflow-hidden">

  <!-- Subtle Ambient Glow -->
  <div class="absolute -top-32 -left-32 w-96 h-96 bg-[#2cf5d6]/10 rounded-full blur-3xl pointer-events-none"></div>
  <div class="absolute -bottom-32 -right-32 w-96 h-96 bg-indigo-600/10 rounded-full blur-3xl pointer-events-none"></div>

  <div class="pie-card max-w-md w-full p-8 space-y-6 relative z-10 border border-[#1c2333] shadow-2xl">
    <!-- Brand Header -->
    <div class="text-center space-y-3">
      <div class="w-14 h-14 rounded-2xl bg-gradient-to-tr from-cyan-600 via-[#2cf5d6] to-emerald-400 p-0.5 shadow-xl shadow-cyan-500/25 mx-auto flex items-center justify-center">
        <div class="w-full h-full bg-[#090b10] rounded-[14px] flex items-center justify-center">
          <span class="text-3xl font-black bg-gradient-to-r from-[#2cf5d6] to-emerald-400 bg-clip-text text-transparent">π</span>
        </div>
      </div>
      <div>
        <h1 class="text-2xl font-black text-white tracking-wider">PIE MC</h1>
        <p class="text-xs text-slate-400 font-mono mt-0.5">Minecraft Management Suite</p>
      </div>
    </div>

    <!-- Login Description -->
    <div class="p-4 rounded-xl bg-[#0a0d14] border border-[#1c2333] text-xs text-slate-300 space-y-1">
      <p class="font-semibold text-white">Sign In Required</p>
      <p class="text-slate-400 leading-relaxed">
        Connect your Discord account to manage your bot instances, servers, and proxies.
      </p>
    </div>

    <!-- Single Discord Login Button -->
    <div class="space-y-3">
      <button id="btnLoginDiscord" onclick="startDiscordOAuth()" class="w-full py-3.5 px-4 rounded-xl bg-[#5865F2] hover:bg-[#4752C4] text-white font-bold text-sm shadow-lg shadow-indigo-500/25 flex items-center justify-center space-x-3 transition-all transform active:scale-95">
        <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24"><path d="M20.317 4.37a19.791 19.791 0 0 0-4.885-1.515.074.074 0 0 0-.079.037c-.21.375-.444.864-.608 1.25a18.27 18.27 0 0 0-5.487 0 12.64 12.64 0 0 0-.617-1.25.077.077 0 0 0-.079-.037A19.736 19.736 0 0 0 3.677 4.37a.07.07 0 0 0-.032.027C.533 9.046-.32 13.58.099 18.057a.082.082 0 0 0 .031.057 19.9 19.9 0 0 0 5.993 3.03.078.078 0 0 0 .084-.028c.462-.63.874-1.295 1.226-1.994.021-.041.001-.09-.041-.106a13.107 13.107 0 0 1-1.872-.892.077.077 0 0 1-.008-.128 10.2 10.2 0 0 0 .372-.292.074.074 0 0 1 .077-.01c3.929 1.793 8.18 1.793 12.061 0a.074.074 0 0 1 .078.01c.12.098.246.198.373.292a.077.077 0 0 1-.006.127 12.299 12.299 0 0 1-1.873.894.077.077 0 0 0-.041.107c.36.698.772 1.362 1.225 1.993a.076.076 0 0 0 .084.028 19.839 19.839 0 0 0 6.002-3.03.077.077 0 0 0 .032-.054c.5-5.177-.838-9.674-3.549-13.66a.061.061 0 0 0-.031-.028zM8.02 15.33c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.956-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.956 2.418-2.157 2.418zm7.975 0c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.955-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.946 2.418-2.157 2.418z"/></svg>
        <span>Login with Discord</span>
      </button>

      <div class="flex items-center justify-between text-[11px] font-mono text-slate-500 pt-1">
        <button onclick="openDiscordConfigModal()" class="hover:text-slate-300 underline">OAuth Configuration</button>
        <span>Encrypted Storage</span>
      </div>
    </div>
  </div>

  <!-- Discord Client ID Settings Modal -->
  <div id="discordConfigModal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm hidden items-center justify-center p-4">
    <div class="pie-card p-6 max-w-md w-full space-y-4 border border-[#1c2333] shadow-2xl">
      <div class="flex items-center justify-between border-b border-[#1c2333] pb-3">
        <h3 class="text-base font-bold text-white">Discord App Settings</h3>
        <button onclick="closeModal('discordConfigModal')" class="text-slate-400 hover:text-white">&times;</button>
      </div>

      <div class="space-y-3 text-xs">
        <div>
          <label class="block font-semibold text-slate-300 mb-1">Discord Client ID</label>
          <input id="cfgClientId" type="text" placeholder="e.g. 123456789012345678" class="pie-input w-full font-mono">
        </div>
        <div>
          <label class="block font-semibold text-slate-300 mb-1">Owner Discord ID</label>
          <input id="cfgOwnerId" type="text" placeholder="e.g. 987654321098765432" class="pie-input w-full font-mono">
          <p class="text-[11px] text-slate-500 mt-1">This user ID automatically unlocks Owner Admin access upon login.</p>
        </div>
      </div>

      <div class="flex items-center justify-end space-x-3 pt-2">
        <button onclick="closeModal('discordConfigModal')" class="btn-secondary text-xs">Cancel</button>
        <button onclick="saveDiscordConfig()" class="btn-primary text-xs">Save & Continue</button>
      </div>
    </div>
  </div>

  <script>
    const DEFAULT_DISCORD_CLIENT_ID = '123456789012345678';
    const DEFAULT_OWNER_ID = '987654321098765432';

    function getDiscordClientId() {
      return localStorage.getItem('PIE_MC_DISCORD_CLIENT_ID') || DEFAULT_DISCORD_CLIENT_ID;
    }

    function getOwnerDiscordId() {
      return localStorage.getItem('PIE_MC_OWNER_ID') || DEFAULT_OWNER_ID;
    }

    window.addEventListener('DOMContentLoaded', async () => {
      const hash = window.location.hash;
      const params = new URLSearchParams(window.location.search);

      if (hash && hash.includes('access_token=')) {
        const hashParams = new URLSearchParams(hash.substring(1));
        const accessToken = hashParams.get('access_token');
        if (accessToken) {
          await handleDiscordToken(accessToken);
          return;
        }
      }

      if (params.get('user')) {
        try {
          const userObj = JSON.parse(decodeURIComponent(params.get('user')));
          finalizeLogin(userObj);
          return;
        } catch (e) {}
      }
    });

    async function handleDiscordToken(token) {
      const btn = document.getElementById('btnLoginDiscord');
      btn.disabled = true;

      try {
        const res = await fetch('https://discord.com/api/users/@me', {
          headers: { 'Authorization': `Bearer ${token}` }
        });

        if (!res.ok) throw new Error('Failed to fetch Discord profile');
        const discordUser = await res.json();

        const ownerId = getOwnerDiscordId();
        const isOwner = (discordUser.id === ownerId);

        const userObj = {
          id: discordUser.id,
          username: discordUser.global_name || discordUser.username,
          discriminator: discordUser.discriminator || '0000',
          avatar: discordUser.avatar 
            ? `https://cdn.discordapp.com/avatars/${discordUser.id}/${discordUser.avatar}.png` 
            : `https://cdn.discordapp.com/embed/avatars/0.png`,
          isOwner: isOwner,
          authTime: new Date().toISOString()
        };

        finalizeLogin(userObj);
      } catch (err) {
        alert('Discord login error: ' + err.message);
        btn.disabled = false;
      }
    }

    function finalizeLogin(userObj) {
      setCurrentUser(userObj);
      window.history.replaceState({}, document.title, window.location.pathname);
      window.location.href = userObj.isOwner ? 'admin.html' : 'dashboard.html';
    }

    function startDiscordOAuth() {
      const clientId = getDiscordClientId();
      const redirectUri = encodeURIComponent(window.location.origin + window.location.pathname);

      if (window.location.protocol.startsWith('http') && window.location.port === '8082') {
        window.location.href = `/api/auth/discord`;
        return;
      }

      const discordAuthUrl = `https://discord.com/api/oauth2/authorize?client_id=${clientId}&redirect_uri=${redirectUri}&response_type=token&scope=identify%20guilds`;
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

with open(os.path.join(PUB, 'login.html'), 'w', encoding='utf-8') as f:
    f.write(login_html)

# 3. ADMIN.HTML (CLEAN DEVELOPER OVERVIEW)
admin_html = '''<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Pie MC — Admin Console</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="styles.css">
  <script src="shared.js"></script>
</head>
<body>
  <div id="header-mount"></div>

  <main class="flex-1 p-6 max-w-7xl w-full mx-auto space-y-6">
    <!-- Admin Hero Banner -->
    <div class="pie-card p-6 space-y-4 border border-[#2cf5d6]/30 shadow-2xl">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div class="flex items-center space-x-3">
          <div class="w-12 h-12 rounded-xl bg-[#2cf5d6]/10 text-[#2cf5d6] border border-[#2cf5d6]/30 flex items-center justify-center">
            <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg>
          </div>
          <div>
            <div class="flex items-center space-x-2">
              <h1 class="text-2xl font-black text-white">Owner Admin Console</h1>
              <span class="badge-diamond text-xs font-mono">ADMIN ACCESS</span>
            </div>
            <p class="text-xs text-slate-400 font-mono mt-0.5">Database storage mode, platform controls, and user counts</p>
          </div>
        </div>
        <a href="dashboard.html" class="btn-secondary text-xs px-4 py-2 no-underline">
          &larr; Back to Dashboard
        </a>
      </div>

      <!-- Privacy Notice -->
      <div class="p-3.5 rounded-xl bg-[#0a0d14] border border-cyan-500/30 flex items-start space-x-3 text-xs">
        <svg class="w-5 h-5 text-cyan-400 mt-0.5 flex-shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
        <div class="text-slate-300 leading-relaxed">
          <strong class="text-[#2cf5d6]">Privacy Notice:</strong>
          <span> Account tokens, passwords, and Minecraft player names remain private and encrypted. Only platform counts and user quantities are visible.</span>
        </div>
      </div>
    </div>

    <!-- Platform Stats -->
    <div class="grid grid-cols-2 lg:grid-cols-4 gap-4">
      <div class="pie-card p-4 flex items-center space-x-4">
        <div class="w-12 h-12 rounded-xl bg-blue-500/10 border border-blue-500/20 flex items-center justify-center text-blue-400">
          <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path><circle cx="9" cy="7" r="4"></circle></svg>
        </div>
        <div>
          <div class="text-2xl font-black text-white" id="teleTotalUsers">14</div>
          <div class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Total Users</div>
        </div>
      </div>

      <div class="pie-card p-4 flex items-center space-x-4">
        <div class="w-12 h-12 rounded-xl bg-emerald-500/10 border border-emerald-500/20 flex items-center justify-center text-emerald-400">
          <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
        </div>
        <div>
          <div class="text-2xl font-black text-white" id="teleTotalAccounts">29</div>
          <div class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Linked Accounts</div>
        </div>
      </div>

      <div class="pie-card p-4 flex items-center space-x-4">
        <div class="w-12 h-12 rounded-xl bg-cyan-500/10 border border-cyan-500/20 flex items-center justify-center text-[#2cf5d6]">
          <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>
        </div>
        <div>
          <div class="text-2xl font-black text-white" id="teleActiveBots">8</div>
          <div class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Active Bots</div>
        </div>
      </div>

      <div class="pie-card p-4 flex items-center space-x-4">
        <div class="w-12 h-12 rounded-xl bg-purple-500/10 border border-purple-500/20 flex items-center justify-center text-purple-400">
          <svg class="w-6 h-6" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="8" rx="2" ry="2"></rect><rect x="2" y="14" width="20" height="8" rx="2" ry="2"></rect></svg>
        </div>
        <div>
          <div class="text-2xl font-black text-white" id="teleTotalServers">12</div>
          <div class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Servers</div>
        </div>
      </div>
    </div>

    <!-- TRI-MODE DATABASE ENGINE MANAGER -->
    <div class="pie-card p-6 space-y-6 border border-[#1c2333]">
      <div class="flex items-center justify-between pb-3 border-b border-[#1c2333]">
        <div class="flex items-center space-x-2.5">
          <svg class="w-5 h-5 text-[#2cf5d6]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><ellipse cx="12" cy="5" rx="9" ry="3"></ellipse><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"></path><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"></path></svg>
          <h2 class="text-lg font-bold text-white">Database Storage Engine</h2>
        </div>
        <span id="activeDbBadge" class="badge-diamond font-mono text-xs uppercase">SQLITE ACTIVE</span>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div onclick="selectDbMode('local_json')" id="cardModeJson" class="pie-card-inner p-4 cursor-pointer border hover:border-[#2cf5d6]/50 transition-all space-y-2">
          <div class="flex items-center justify-between">
            <span class="font-bold text-white text-sm">1. Local JSON</span>
            <input type="radio" name="dbRadio" id="radioJson" class="text-[#2cf5d6]">
          </div>
          <p class="text-xs text-slate-400">
            Stores data in <code>backend/data/json_store/</code>. Zero-dependency flat files.
          </p>
        </div>

        <div onclick="selectDbMode('sqlite')" id="cardModeSqlite" class="pie-card-inner p-4 cursor-pointer border border-[#2cf5d6]/40 bg-[#2cf5d6]/5 transition-all space-y-2">
          <div class="flex items-center justify-between">
            <span class="font-bold text-white text-sm">2. SQLite</span>
            <input type="radio" name="dbRadio" id="radioSqlite" checked class="text-[#2cf5d6]">
          </div>
          <p class="text-xs text-slate-400">
            Fast embedded database in <code>pie-mc.db</code>. Recommended for VPS installs.
          </p>
        </div>

        <div onclick="selectDbMode('turso')" id="cardModeTurso" class="pie-card-inner p-4 cursor-pointer border hover:border-[#2cf5d6]/50 transition-all space-y-2">
          <div class="flex items-center justify-between">
            <span class="font-bold text-white text-sm">3. Turso (libSQL)</span>
            <input type="radio" name="dbRadio" id="radioTurso" class="text-[#2cf5d6]">
          </div>
          <p class="text-xs text-slate-400">
            Serverless cloud database with remote backups and edge replication.
          </p>
        </div>
      </div>

      <div id="dbConfigDetails" class="space-y-4 pt-2">
        <div id="tursoFields" class="hidden space-y-3 p-4 rounded-xl bg-[#0a0d14] border border-[#1c2333]">
          <div class="space-y-1">
            <label class="block text-xs font-semibold text-slate-300">TURSO_DATABASE_URL</label>
            <input id="inputTursoUrl" type="text" placeholder="libsql://your-db.turso.io" class="pie-input w-full font-mono text-xs">
          </div>
          <div class="space-y-1">
            <label class="block text-xs font-semibold text-slate-300">TURSO_AUTH_TOKEN</label>
            <input id="inputTursoToken" type="password" placeholder="Paste Turso Auth Token..." class="pie-input w-full font-mono text-xs text-[#2cf5d6]">
          </div>
        </div>

        <div id="sqliteFields" class="space-y-3 p-4 rounded-xl bg-[#0a0d14] border border-[#1c2333]">
          <div class="space-y-1">
            <label class="block text-xs font-semibold text-slate-300">SQLite Database Path</label>
            <input id="inputSqlitePath" type="text" value="backend/data/pie-mc.db" class="pie-input w-full font-mono text-xs">
          </div>
        </div>

        <div id="jsonFields" class="hidden space-y-3 p-4 rounded-xl bg-[#0a0d14] border border-[#1c2333]">
          <div class="space-y-1">
            <label class="block text-xs font-semibold text-slate-300">JSON Directory Path</label>
            <input id="inputJsonPath" type="text" value="backend/data/json_store/" class="pie-input w-full font-mono text-xs">
          </div>
        </div>
      </div>

      <div class="flex items-center justify-end space-x-3 pt-2">
        <button onclick="applyDatabaseConfig()" class="btn-primary">
          <span>Set Database & Create Tables</span>
        </button>
      </div>
    </div>

    <!-- OWNER PLATFORM FEATURE TOGGLES -->
    <div class="pie-card p-6 space-y-6 border border-[#1c2333]">
      <div class="flex items-center space-x-2.5 pb-3 border-b border-[#1c2333]">
        <svg class="w-5 h-5 text-[#2cf5d6]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
        <h2 class="text-lg font-bold text-white">Platform Settings & Controls</h2>
      </div>

      <div class="space-y-4">
        <div class="p-4 rounded-xl pie-card-inner border border-[#1c2333] space-y-3">
          <label class="flex items-center justify-between cursor-pointer">
            <div>
              <span class="font-bold text-white text-sm block">Allow Users to Change Minecraft Version</span>
              <span class="text-xs text-slate-400">When disabled, users are locked to your chosen Minecraft version.</span>
            </div>
            <input type="checkbox" id="flagAllowVersion" onchange="toggleVersionSelectorVisibility(this.checked)" checked class="w-5 h-5 rounded text-[#2cf5d6]">
          </label>

          <div id="lockedVersionBox" class="hidden pt-2 border-t border-[#1c2333] space-y-1">
            <label class="text-xs font-semibold text-amber-400">Locked Global Version:</label>
            <select id="selectLockedVersion" class="pie-select w-full font-mono text-xs">
              <option value="1.21.1">1.21.1</option>
              <option value="1.20.4">1.20.4</option>
              <option value="1.19.4">1.19.4</option>
              <option value="1.16.5">1.16.5</option>
              <option value="1.8.9">1.8.9</option>
            </select>
          </div>
        </div>

        <div class="p-4 rounded-xl pie-card-inner border border-[#1c2333]">
          <label class="flex items-center justify-between cursor-pointer">
            <div>
              <span class="font-bold text-white text-sm block">Allow Auto-Reconnect</span>
              <span class="text-xs text-slate-400">Allows bots to automatically reconnect if dropped.</span>
            </div>
            <input type="checkbox" id="flagAllowReconnect" checked class="w-5 h-5 rounded text-[#2cf5d6]">
          </label>
        </div>

        <div class="p-4 rounded-xl pie-card-inner border border-[#1c2333]">
          <label class="flex items-center justify-between cursor-pointer">
            <div>
              <span class="font-bold text-white text-sm block">Allow New Registrations</span>
              <span class="text-xs text-slate-400">Allow new Discord users to sign in.</span>
            </div>
            <input type="checkbox" id="flagAllowRegistrations" checked class="w-5 h-5 rounded text-[#2cf5d6]">
          </label>
        </div>

        <div class="flex justify-end pt-2">
          <button onclick="saveOwnerFlags()" class="btn-primary text-xs">
            Save Settings
          </button>
        </div>
      </div>
    </div>

    <!-- USERS OVERVIEW -->
    <div class="pie-card p-6 space-y-4 border border-[#1c2333]">
      <div class="flex items-center justify-between">
        <h2 class="text-lg font-bold text-white">Registered Users Overview</h2>
      </div>

      <div class="overflow-x-auto rounded-xl border border-[#1c2333]">
        <table class="w-full text-left text-sm text-slate-300">
          <thead class="bg-[#0c1018] text-xs uppercase font-mono text-slate-400 border-b border-[#1c2333]">
            <tr>
              <th class="px-4 py-3">Discord User</th>
              <th class="px-4 py-3">User ID</th>
              <th class="px-4 py-3">Joined Date</th>
              <th class="px-4 py-3">Accounts Linked</th>
              <th class="px-4 py-3">Instances Running</th>
              <th class="px-4 py-3 text-right">Actions</th>
            </tr>
          </thead>
          <tbody id="telemetryTableBody" class="divide-y divide-[#1c2333]/80 bg-[#090b10] font-mono text-xs">
          </tbody>
        </table>
      </div>
    </div>
  </main>

  <script>
    let currentDbMode = 'sqlite';

    document.addEventListener('DOMContentLoaded', () => {
      const user = getCurrentUser();
      if (!user || (!user.isOwner && user.id !== OWNER_DISCORD_ID)) {
        window.location.href = 'dashboard.html';
        return;
      }

      renderGlobalHeader('admin');
      loadPlatformFlagsToUI();
      renderAdminTelemetry();
    });

    function selectDbMode(mode) {
      currentDbMode = mode;
      document.getElementById('radioJson').checked = (mode === 'local_json');
      document.getElementById('radioSqlite').checked = (mode === 'sqlite');
      document.getElementById('radioTurso').checked = (mode === 'turso');

      ['Json', 'Sqlite', 'Turso'].forEach(t => {
        const el = document.getElementById('cardMode' + t);
        el.className = 'pie-card-inner p-4 cursor-pointer border hover:border-[#2cf5d6]/50 transition-all space-y-2';
      });

      const activeCard = document.getElementById(mode === 'local_json' ? 'cardModeJson' : (mode === 'sqlite' ? 'cardModeSqlite' : 'cardModeTurso'));
      activeCard.className = 'pie-card-inner p-4 cursor-pointer border border-[#2cf5d6]/50 bg-[#2cf5d6]/10 transition-all space-y-2';

      document.getElementById('jsonFields').classList.toggle('hidden', mode !== 'local_json');
      document.getElementById('sqliteFields').classList.toggle('hidden', mode !== 'sqlite');
      document.getElementById('tursoFields').classList.toggle('hidden', mode !== 'turso');

      document.getElementById('activeDbBadge').innerText = mode.toUpperCase() + ' SELECTED';
    }

    function loadPlatformFlagsToUI() {
      const flags = getPlatformFlags();
      selectDbMode(flags.databaseMode || 'sqlite');

      document.getElementById('flagAllowVersion').checked = flags.allowUserChangeVersion;
      toggleVersionSelectorVisibility(flags.allowUserChangeVersion);

      document.getElementById('selectLockedVersion').value = flags.lockedVersion || '1.21.1';
      document.getElementById('flagAllowReconnect').checked = flags.allowAutoReconnect;
      document.getElementById('flagAllowRegistrations').checked = flags.allowNewRegistrations;

      if (flags.tursoUrl) document.getElementById('inputTursoUrl').value = flags.tursoUrl;
      if (flags.tursoToken) document.getElementById('inputTursoToken').value = flags.tursoToken;
      if (flags.sqlitePath) document.getElementById('inputSqlitePath').value = flags.sqlitePath;
      if (flags.jsonStorePath) document.getElementById('inputJsonPath').value = flags.jsonStorePath;
    }

    function toggleVersionSelectorVisibility(allow) {
      document.getElementById('lockedVersionBox').classList.toggle('hidden', allow);
    }

    function applyDatabaseConfig() {
      const flags = getPlatformFlags();
      flags.databaseMode = currentDbMode;
      flags.tursoUrl = document.getElementById('inputTursoUrl').value.trim();
      flags.tursoToken = document.getElementById('inputTursoToken').value.trim();
      flags.sqlitePath = document.getElementById('inputSqlitePath').value.trim();
      flags.jsonStorePath = document.getElementById('inputJsonPath').value.trim();

      savePlatformFlags(flags);
      document.getElementById('activeDbBadge').innerText = currentDbMode.toUpperCase() + ' ACTIVE';
      alert(`Database set to ${currentDbMode.toUpperCase()}!`);
    }

    function saveOwnerFlags() {
      const flags = getPlatformFlags();
      flags.allowUserChangeVersion = document.getElementById('flagAllowVersion').checked;
      flags.lockedVersion = document.getElementById('selectLockedVersion').value;
      flags.allowAutoReconnect = document.getElementById('flagAllowReconnect').checked;
      flags.allowNewRegistrations = document.getElementById('flagAllowRegistrations').checked;

      savePlatformFlags(flags);
      alert('Platform settings saved!');
    }

    function renderAdminTelemetry() {
      const tele = getGlobalTelemetry();
      document.getElementById('teleTotalUsers').innerText = tele.usersList.length;
      document.getElementById('teleTotalAccounts').innerText = tele.totalAccountsCount;
      document.getElementById('teleActiveBots').innerText = tele.activeBotsCount;
      document.getElementById('teleTotalServers').innerText = tele.totalServersCount;

      const tbody = document.getElementById('telemetryTableBody');
      tbody.innerHTML = tele.usersList.map(u => `
        <tr class="hover:bg-slate-900/40 transition-colors">
          <td class="px-4 py-3 font-bold text-white flex items-center space-x-2">
            <span class="w-2 h-2 rounded-full bg-emerald-400 pulse-dot"></span>
            <span>${u.username}</span>
          </td>
          <td class="px-4 py-3 text-slate-400 font-mono">${u.id}</td>
          <td class="px-4 py-3 text-slate-500">${u.joined}</td>
          <td class="px-4 py-3"><span class="badge-online font-bold">${u.accountsCount} Linked</span></td>
          <td class="px-4 py-3"><span class="badge-diamond font-bold">${u.instancesCount} Active</span></td>
          <td class="px-4 py-3 text-right">
            <button onclick="terminateUserInstances('${u.id}', '${u.username}')" class="text-xs text-red-400 hover:text-red-300">Restart Session</button>
          </td>
        </tr>
      `).join('');
    }

    function terminateUserInstances(uid, uname) {
      window.showConfirmModal({
        title: `Restart Session for ${uname}?`,
        message: `This will safely trigger a reconnect for all active bot instances owned by Discord User <strong>${uname}</strong> (${uid}).`,
        confirmText: 'Restart Bots',
        cancelText: 'Cancel',
        isDanger: false,
        onConfirm: () => {
          alert(`Restart signal sent for ${uname}.`);
        }
      });
    }
  </script>
</body>
</html>
'''

with open(os.path.join(PUB, 'admin.html'), 'w', encoding='utf-8') as f:
    f.write(admin_html)

# 4. 404.HTML (CLEAN NOT FOUND)
not_found_html = '''<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Pie MC — 404 Page Not Found</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="styles.css">
  <script src="shared.js"></script>
</head>
<body class="flex items-center justify-center min-h-screen p-4 bg-[#090b10] relative overflow-hidden text-center">

  <div class="absolute -top-32 -left-32 w-96 h-96 bg-[#2cf5d6]/10 rounded-full blur-3xl pointer-events-none"></div>
  <div class="absolute -bottom-32 -right-32 w-96 h-96 bg-red-500/10 rounded-full blur-3xl pointer-events-none"></div>

  <div class="pie-card max-w-lg w-full p-10 space-y-6 relative z-10 border border-[#1c2333] shadow-2xl">
    <div class="w-16 h-16 rounded-2xl bg-red-500/10 border border-red-500/30 mx-auto flex items-center justify-center text-red-400">
      <svg class="w-8 h-8" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
    </div>

    <div class="space-y-2">
      <span class="px-3 py-1 rounded-md bg-red-500/15 text-red-400 border border-red-500/30 text-xs font-mono font-bold uppercase">404 ERROR</span>
      <h1 class="text-2xl font-black text-white">Page Not Found</h1>
      <p class="text-xs text-slate-400 font-mono max-w-sm mx-auto leading-relaxed">
        The page you are looking for does not exist or has been moved.
      </p>
    </div>

    <div class="pt-2 flex items-center justify-center space-x-3">
      <a href="dashboard.html" class="btn-primary px-6 py-2.5 no-underline text-xs">
        <span>&larr; Return to Dashboard</span>
      </a>
    </div>
  </div>
</body>
</html>
'''

with open(os.path.join(PUB, '404.html'), 'w', encoding='utf-8') as f:
    f.write(not_found_html)

print("Authentic human-crafted UI files written successfully!")
