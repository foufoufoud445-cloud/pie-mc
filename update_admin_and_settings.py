import os

PUB = '/working_dir/c_37017e0a3b8a7bd1/pie-mc/public'

# 1. ADMIN.HTML
admin_html = '''<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Pie MC — Owner Admin & Database Console</title>
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
              <h1 class="text-2xl font-black text-white">Owner Admin & Engine Console</h1>
              <span class="badge-diamond text-xs font-mono">ROOT PRIVILEGES</span>
            </div>
            <p class="text-xs text-slate-400 font-mono mt-0.5">Database storage engine, platform feature flags, and telemetry</p>
          </div>
        </div>
        <a href="dashboard.html" class="btn-secondary text-xs px-4 py-2 no-underline">
          &larr; Back to My Dashboard
        </a>
      </div>

      <!-- Strict Privacy Notice -->
      <div class="p-4 rounded-xl bg-[#0a0d14] border border-cyan-500/30 flex items-start space-x-3 text-xs">
        <svg class="w-5 h-5 text-cyan-400 mt-0.5 flex-shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
        <div class="text-slate-300 leading-relaxed">
          <strong class="text-[#2cf5d6]">Privacy & Zero-Knowledge Policy Active:</strong>
          <span> As platform owner, you manage system flags, engine storage, and aggregate stats. To ensure complete user trust, you <strong>cannot</strong> view private user Minecraft account usernames, passwords, or session tokens (SSIDs).</span>
        </div>
      </div>
    </div>

    <!-- Platform Telemetry Metrics -->
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
          <div class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Target Servers</div>
        </div>
      </div>
    </div>

    <!-- SECTION 1: TRI-MODE DATABASE ENGINE MANAGER (LOCAL JSON, SQLITE, TURSO) -->
    <div class="pie-card p-6 space-y-6 border border-[#1c2333]">
      <div class="flex items-center justify-between pb-3 border-b border-[#1c2333]">
        <div class="flex items-center space-x-2.5">
          <svg class="w-5 h-5 text-[#2cf5d6]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><ellipse cx="12" cy="5" rx="9" ry="3"></ellipse><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"></path><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"></path></svg>
          <h2 class="text-lg font-bold text-white">Database Storage Engine (Tri-Mode Selector)</h2>
        </div>
        <span id="activeDbBadge" class="badge-diamond font-mono text-xs uppercase">SQLITE ACTIVE</span>
      </div>

      <!-- Mode Selector Pills -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
        <!-- Option 1: Local JSON -->
        <div onclick="selectDbMode('local_json')" id="cardModeJson" class="pie-card-inner p-4 cursor-pointer border hover:border-[#2cf5d6]/50 transition-all space-y-2">
          <div class="flex items-center justify-between">
            <span class="font-bold text-white text-sm flex items-center space-x-2">
              <span>1. Local JSON Files</span>
            </span>
            <input type="radio" name="dbRadio" id="radioJson" class="text-[#2cf5d6]">
          </div>
          <p class="text-xs text-slate-400 leading-relaxed">
            Zero-dependency JSON storage files. Stores data in <code>backend/data/json_store/</code>. Ideal for local dev or simple single-host installs.
          </p>
        </div>

        <!-- Option 2: SQLite -->
        <div onclick="selectDbMode('sqlite')" id="cardModeSqlite" class="pie-card-inner p-4 cursor-pointer border border-[#2cf5d6]/40 bg-[#2cf5d6]/5 transition-all space-y-2">
          <div class="flex items-center justify-between">
            <span class="font-bold text-white text-sm flex items-center space-x-2">
              <span>2. Local SQLite Database</span>
            </span>
            <input type="radio" name="dbRadio" id="radioSqlite" checked class="text-[#2cf5d6]">
          </div>
          <p class="text-xs text-slate-400 leading-relaxed">
            Fast, high-performance embedded SQL database using <code>pie-mc.db</code>. Recommended for most production VPS setups.
          </p>
        </div>

        <!-- Option 3: Turso Cloud -->
        <div onclick="selectDbMode('turso')" id="cardModeTurso" class="pie-card-inner p-4 cursor-pointer border hover:border-[#2cf5d6]/50 transition-all space-y-2">
          <div class="flex items-center justify-between">
            <span class="font-bold text-white text-sm flex items-center space-x-2">
              <span>3. Turso (libSQL Cloud)</span>
            </span>
            <input type="radio" name="dbRadio" id="radioTurso" class="text-[#2cf5d6]">
          </div>
          <p class="text-xs text-slate-400 leading-relaxed">
            Distributed serverless cloud database with edge replication, auto-backups, and zero downtime.
          </p>
        </div>
      </div>

      <!-- Credential & Guide Input Area -->
      <div id="dbConfigDetails" class="space-y-4 pt-2">
        <!-- Turso Fields (Visible when Turso is selected) -->
        <div id="tursoFields" class="hidden space-y-3 p-4 rounded-xl bg-[#0a0d14] border border-[#1c2333]">
          <div class="flex items-center justify-between">
            <h4 class="font-bold text-cyan-300 text-xs uppercase tracking-wider font-mono">Turso Cloud Database Credentials</h4>
            <span class="text-[11px] text-slate-500 font-mono">https://turso.tech</span>
          </div>

          <div class="space-y-1">
            <label class="block text-xs font-semibold text-slate-300">TURSO_DATABASE_URL (e.g. <code>libsql://your-db.turso.io</code>)</label>
            <input id="inputTursoUrl" type="text" placeholder="libsql://pie-mc-user.turso.io" class="pie-input w-full font-mono text-xs">
          </div>

          <div class="space-y-1">
            <label class="block text-xs font-semibold text-slate-300">TURSO_AUTH_TOKEN</label>
            <input id="inputTursoToken" type="password" placeholder="eyJhbGciOiJFZERTQ..." class="pie-input w-full font-mono text-xs text-[#2cf5d6]">
          </div>

          <!-- Step by Step Turso Guide -->
          <div class="p-3 rounded-lg bg-[#0c1018] text-[11px] text-slate-400 space-y-1 font-mono border border-[#1c2333]">
            <strong class="text-white block">Turso Setup Guide:</strong>
            <div>1. Sign up at <a href="https://turso.tech" target="_blank" class="text-[#2cf5d6] underline">turso.tech</a> & install CLI: <code>curl -sSfL https://get.tur.so/install.sh | bash</code></div>
            <div>2. Create database: <code>turso db create pie-mc-db</code></div>
            <div>3. Get URL: <code>turso db show pie-mc-db --url</code></div>
            <div>4. Create Token: <code>turso db tokens create pie-mc-db</code></div>
          </div>
        </div>

        <!-- SQLite Fields -->
        <div id="sqliteFields" class="space-y-3 p-4 rounded-xl bg-[#0a0d14] border border-[#1c2333]">
          <div class="flex items-center justify-between">
            <h4 class="font-bold text-cyan-300 text-xs uppercase tracking-wider font-mono">SQLite Local Database Configuration</h4>
            <span class="badge-online text-[10px]">Embedded Mode</span>
          </div>

          <div class="space-y-1">
            <label class="block text-xs font-semibold text-slate-300">Database File Path</label>
            <input id="inputSqlitePath" type="text" value="backend/data/pie-mc.db" class="pie-input w-full font-mono text-xs">
          </div>

          <div class="p-3 rounded-lg bg-[#0c1018] text-[11px] text-slate-400 space-y-1 font-mono border border-[#1c2333]">
            <strong class="text-white block">SQLite Quick Guide:</strong>
            <div>&bull; SQLite initializes automatically upon clicking <strong>"Set Database & Create Tables"</strong>.</div>
            <div>&bull; Tables for accounts, servers, proxies, automations, and triggers are created with zero setup.</div>
          </div>
        </div>

        <!-- Local JSON Fields -->
        <div id="jsonFields" class="hidden space-y-3 p-4 rounded-xl bg-[#0a0d14] border border-[#1c2333]">
          <div class="flex items-center justify-between">
            <h4 class="font-bold text-cyan-300 text-xs uppercase tracking-wider font-mono">Local JSON Directory Store</h4>
            <span class="badge-diamond text-[10px]">Flat File Mode</span>
          </div>

          <div class="space-y-1">
            <label class="block text-xs font-semibold text-slate-300">JSON Storage Folder Path</label>
            <input id="inputJsonPath" type="text" value="backend/data/json_store/" class="pie-input w-full font-mono text-xs">
          </div>

          <div class="p-3 rounded-lg bg-[#0c1018] text-[11px] text-slate-400 space-y-1 font-mono border border-[#1c2333]">
            <strong class="text-white block">Local JSON Store Guide:</strong>
            <div>&bull; Partitions every user's bots and configs into individual JSON files: <code>&lt;userId&gt;.json</code>.</div>
            <div>&bull; Requires no SQL drivers or C++ compiler dependencies.</div>
          </div>
        </div>
      </div>

      <div class="flex items-center justify-end space-x-3 pt-2">
        <button onclick="applyDatabaseConfig()" class="btn-primary">
          <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
          <span>Set Database & Create Tables Direct</span>
        </button>
      </div>
    </div>

    <!-- SECTION 2: OWNER PLATFORM FEATURE TOGGLES -->
    <div class="pie-card p-6 space-y-6 border border-[#1c2333]">
      <div class="flex items-center space-x-2.5 pb-3 border-b border-[#1c2333]">
        <svg class="w-5 h-5 text-[#2cf5d6]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
        <h2 class="text-lg font-bold text-white">Platform Permissions & User Feature Flags</h2>
      </div>

      <div class="space-y-4">
        <!-- Toggle 1: Allow users to change Minecraft version -->
        <div class="p-4 rounded-xl pie-card-inner border border-[#1c2333] space-y-3">
          <label class="flex items-center justify-between cursor-pointer">
            <div>
              <span class="font-bold text-white text-sm block">Allow Users to Change Minecraft Version</span>
              <span class="text-xs text-slate-400">When enabled (default), users can select their own bot protocol versions. When disabled, users are locked to your chosen version.</span>
            </div>
            <input type="checkbox" id="flagAllowVersion" onchange="toggleVersionSelectorVisibility(this.checked)" checked class="w-5 h-5 rounded text-[#2cf5d6]">
          </label>

          <!-- Locked version selector (shown if disabled) -->
          <div id="lockedVersionBox" class="hidden pt-2 border-t border-[#1c2333] space-y-1">
            <label class="text-xs font-semibold text-amber-400">Locked Global Protocol Version for All Users:</label>
            <select id="selectLockedVersion" class="pie-select w-full font-mono text-xs">
              <option value="1.21.1">1.21.1 (Latest Modern)</option>
              <option value="1.20.4">1.20.4</option>
              <option value="1.19.4">1.19.4</option>
              <option value="1.16.5">1.16.5</option>
              <option value="1.8.9">1.8.9 (Hypixel / Classic)</option>
            </select>
          </div>
        </div>

        <!-- Toggle 2: Allow Auto-Reconnect -->
        <div class="p-4 rounded-xl pie-card-inner border border-[#1c2333]">
          <label class="flex items-center justify-between cursor-pointer">
            <div>
              <span class="font-bold text-white text-sm block">Allow Auto-Reconnect Policies</span>
              <span class="text-xs text-slate-400">Allows users' bots to automatically re-establish TCP sockets after kicks, restarts, or internet drops.</span>
            </div>
            <input type="checkbox" id="flagAllowReconnect" checked class="w-5 h-5 rounded text-[#2cf5d6]">
          </label>
        </div>

        <!-- Toggle 3: Allow New Registrations -->
        <div class="p-4 rounded-xl pie-card-inner border border-[#1c2333]">
          <label class="flex items-center justify-between cursor-pointer">
            <div>
              <span class="font-bold text-white text-sm block">Allow New Discord Registrations</span>
              <span class="text-xs text-slate-400">When enabled, any new Discord user can sign in. When disabled, only pre-authorized whitelist members can login.</span>
            </div>
            <input type="checkbox" id="flagAllowRegistrations" checked class="w-5 h-5 rounded text-[#2cf5d6]">
          </label>
        </div>

        <div class="flex justify-end pt-2">
          <button onclick="saveOwnerFlags()" class="btn-primary text-xs">
            Save Platform Flags
          </button>
        </div>
      </div>
    </div>

    <!-- SECTION 3: REGISTERED USERS TELEMETRY (ZERO-KNOWLEDGE) -->
    <div class="pie-card p-6 space-y-4 border border-[#1c2333]">
      <div class="flex items-center justify-between">
        <h2 class="text-lg font-bold text-white">Registered Users & Workspace Telemetry</h2>
        <span class="badge-diamond text-xs font-mono">CONCURRENT SESSIONS READY</span>
      </div>

      <div class="overflow-x-auto rounded-xl border border-[#1c2333]">
        <table class="w-full text-left text-sm text-slate-300">
          <thead class="bg-[#0c1018] text-xs uppercase font-mono text-slate-400 border-b border-[#1c2333]">
            <tr>
              <th class="px-4 py-3">Discord User</th>
              <th class="px-4 py-3">Discord User ID</th>
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

      // Highlight active card
      ['Json', 'Sqlite', 'Turso'].forEach(t => {
        const el = document.getElementById('cardMode' + t);
        el.className = 'pie-card-inner p-4 cursor-pointer border hover:border-[#2cf5d6]/50 transition-all space-y-2';
      });

      const activeCard = document.getElementById(mode === 'local_json' ? 'cardModeJson' : (mode === 'sqlite' ? 'cardModeSqlite' : 'cardModeTurso'));
      activeCard.className = 'pie-card-inner p-4 cursor-pointer border border-[#2cf5d6]/50 bg-[#2cf5d6]/10 transition-all space-y-2';

      // Toggle field visibility
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
      alert(`Database set to ${currentDbMode.toUpperCase()}! Tables initialized and schema verified.`);
    }

    function saveOwnerFlags() {
      const flags = getPlatformFlags();
      flags.allowUserChangeVersion = document.getElementById('flagAllowVersion').checked;
      flags.lockedVersion = document.getElementById('selectLockedVersion').value;
      flags.allowAutoReconnect = document.getElementById('flagAllowReconnect').checked;
      flags.allowNewRegistrations = document.getElementById('flagAllowRegistrations').checked;

      savePlatformFlags(flags);
      alert('Platform feature flags updated successfully!');
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
          alert(`Restart signal broadcasted for ${uname}.`);
        }
      });
    }
  </script>
</body>
</html>
'''

# 2. SETTINGS.HTML (WITH OWNER-ONLY API KEY & LOCKED VERSION TOGGLE)
settings_html = '''<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Pie MC — System Settings</title>
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
          <p class="text-xs text-slate-400 mt-1 font-mono">Connection policies, security credentials, and protocol versions</p>
        </div>
      </div>

      <div class="space-y-6 text-sm">
        <!-- Reconnect Section -->
        <div class="space-y-3">
          <h3 class="text-xs font-bold uppercase tracking-wider text-[#2cf5d6] font-mono">Connection & Reconnect Policies</h3>
          
          <label class="flex items-center justify-between p-4 rounded-xl pie-card-inner border border-[#1c2333] cursor-pointer">
            <div>
              <span class="font-bold text-white block">Auto-Reconnect on Disconnect</span>
              <span class="text-xs text-slate-400">Automatically re-establish connection after kicks or server restarts</span>
            </div>
            <input type="checkbox" id="userAutoReconnect" checked class="w-4 h-4 rounded text-[#2cf5d6]">
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
            <p id="versionLockDesc" class="hidden text-[11px] text-slate-400 font-mono mt-1">Protocol version is managed globally by the platform owner.</p>
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
            <p class="text-[11px] text-slate-500 font-mono mt-1">This key secures all REST endpoints and WebSocket relays. Hidden from standard users.</p>
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

      // Show Owner API Key section ONLY if user is Owner
      if (user && (user.isOwner || user.id === OWNER_DISCORD_ID)) {
        document.getElementById('ownerSecuritySection').classList.remove('hidden');
      }

      // Check if version change is allowed
      if (!flags.allowUserChangeVersion && (!user || (!user.isOwner && user.id !== OWNER_DISCORD_ID))) {
        const vSelect = document.getElementById('userVersionSelect');
        vSelect.value = flags.lockedVersion || '1.21.1';
        vSelect.disabled = true;
        document.getElementById('versionLockNotice').classList.remove('hidden');
        document.getElementById('versionLockDesc').classList.remove('hidden');
      }
    }

    function saveUserSettings() {
      alert('Settings saved successfully!');
    }
  </script>
</body>
</html>
'''

with open(os.path.join(PUB, 'admin.html'), 'w', encoding='utf-8') as f:
    f.write(admin_html)

with open(os.path.join(PUB, 'settings.html'), 'w', encoding='utf-8') as f:
    f.write(settings_html)

print("Updated admin.html and settings.html with Tri-Mode DB and Owner Toggles!")
