import os

PUB = '/working_dir/c_37017e0a3b8a7bd1/pie-mc/public'

# 1. INDEX.HTML (DASHBOARD)
index_html = '''<!DOCTYPE html>
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
              Connected as <span id="instAccSpan" class="text-[#2cf5d6] font-bold">PieBot_Alpha</span> on <span id="instSrvSpan" class="text-white font-semibold">mc.hypixel.net:25565</span>
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
            <span class="badge-online">AUTHENTICATED</span>
          </div>
          <select id="accSelect" onchange="changeActiveAccount(this.value)" class="pie-select w-full py-2 px-3 text-sm font-semibold text-white">
          </select>
          <div class="flex items-center justify-between text-[11px] font-mono text-slate-400 pt-1">
            <span>UUID: <span id="accUUID" class="text-slate-300">d8f3-4a11-98bc</span></span>
            <span class="text-emerald-400 font-semibold">AES-256 Valid</span>
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
            <span class="text-purple-400 font-semibold">SOCKS5 Tunneled</span>
          </div>
        </div>
      </div>
    </div>

    <!-- 4 Metric Cards -->
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

    <!-- Live In-Game Chat Stream Console -->
    <div class="pie-card p-5 space-y-4">
      <div class="flex items-center justify-between">
        <div class="flex items-center space-x-3">
          <div class="w-2.5 h-2.5 rounded-full bg-[#2cf5d6] pulse-dot"></div>
          <h3 class="text-base font-bold text-white">Live In-Game Chat Stream <span class="text-xs font-mono text-slate-400 font-normal">(Instance Live Feed)</span></h3>
        </div>
        <div class="flex items-center space-x-2">
          <button onclick="clearChatConsole()" class="btn-secondary text-xs px-2.5 py-1">Clear Console</button>
          <a href="chat.html" class="btn-primary text-xs px-3 py-1 no-underline">Open Full Console &rarr;</a>
        </div>
      </div>

      <div id="dashChatStream" class="h-64 overflow-y-auto bg-black/80 rounded-xl p-4 font-mono text-xs space-y-2 border border-[#1c2333]">
      </div>

      <form onsubmit="handleSendChat(event)" class="flex items-center space-x-2 pt-2">
        <input id="dashChatInput" type="text" placeholder="Send a chat message or Minecraft /command through this bot..." class="pie-input flex-1 font-mono text-sm">
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

      // Selectors
      const accSelect = document.getElementById('accSelect');
      accSelect.innerHTML = state.accounts.map(a => `<option value="${a.username}" ${a.username === inst.account ? 'selected' : ''}>${a.username}</option>`).join('');

      const srvSelect = document.getElementById('srvSelect');
      srvSelect.innerHTML = state.servers.map(s => `<option value="${s.name}" ${s.name === inst.server ? 'selected' : ''}>${s.name} (${s.host})</option>`).join('');

      const prxSelect = document.getElementById('prxSelect');
      prxSelect.innerHTML = `<option value="Auto">Auto Pool (Best Available)</option>` + state.proxies.map(p => `<option value="${p.name}" ${p.name === inst.proxy ? 'selected' : ''}>${p.name} [${p.type}]</option>`).join('');

      // Stats
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
        });
        populateDashboard();
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
      c.innerHTML = state.chatLogs.map(m => `
        <div class="flex items-start space-x-2">
          <span class="text-slate-600">[${m.time}]</span>
          <span class="${m.type === 'bot' ? 'text-emerald-400 font-bold' : 'text-cyan-400'}">${m.tag} ${m.player}:</span>
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
        s.chatLogs.push({ time: now, player: inst.account, tag: '[BOT]', msg: val, type: 'bot' });
      });

      renderChatLogs();
      input.value = '';
    }

    function clearChatConsole() {
      window.updatePieState(s => s.chatLogs = []);
      renderChatLogs();
    }
  </script>
</body>
</html>
'''

# 2. CHAT.HTML
chat_html = '''<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Pie MC — Interactive Terminal & Chat</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="styles.css">
  <script src="shared.js"></script>
</head>
<body>
  <div id="header-mount"></div>
  <div id="instance-bar-mount"></div>

  <main class="flex-1 p-6 max-w-7xl w-full mx-auto space-y-6">
    <div class="pie-card p-6 flex flex-col h-[78vh]">
      <div class="flex items-center justify-between pb-4 border-b border-[#1c2333]">
        <div class="flex items-center space-x-3">
          <div class="w-8 h-8 rounded-lg bg-[#2cf5d6]/10 border border-[#2cf5d6]/30 flex items-center justify-center text-[#2cf5d6]">
            <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
          </div>
          <div>
            <h2 class="text-lg font-bold text-white">Full Minecraft Terminal</h2>
            <p class="text-xs text-slate-400 font-mono">Live bi-directional communication stream</p>
          </div>
        </div>

        <div class="flex items-center space-x-2">
          <button onclick="insertCmd('/spawn')" class="btn-secondary text-xs px-2.5 py-1 font-mono text-cyan-300">/spawn</button>
          <button onclick="insertCmd('/help')" class="btn-secondary text-xs px-2.5 py-1 font-mono text-cyan-300">/help</button>
          <button onclick="insertCmd('/list')" class="btn-secondary text-xs px-2.5 py-1 font-mono text-cyan-300">/list</button>
          <button onclick="insertCmd('/tpa ')" class="btn-secondary text-xs px-2.5 py-1 font-mono text-cyan-300">/tpa</button>
          <button onclick="clearConsole()" class="btn-secondary text-xs px-3 py-1">Clear</button>
        </div>
      </div>

      <div id="fullConsoleStream" class="flex-1 overflow-y-auto bg-black/85 rounded-xl p-4 my-4 font-mono text-xs space-y-2 border border-[#1c2333]">
      </div>

      <form onsubmit="handleSend(event)" class="flex items-center space-x-3 pt-2">
        <input id="chatInput" type="text" placeholder="Type a chat message or Minecraft command (e.g. /msg Notch hello or !coords)..." class="pie-input flex-1 font-mono text-sm">
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
      c.innerHTML = state.chatLogs.map(m => `
        <div class="flex items-start space-x-2">
          <span class="text-slate-600">[${m.time}]</span>
          <span class="${m.type === 'bot' ? 'text-emerald-400 font-bold' : 'text-cyan-400'}">${m.tag} ${m.player}:</span>
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
        s.chatLogs.push({ time: now, player: inst.account, tag: '[BOT]', msg: val, type: 'bot' });
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
      window.updatePieState(s => s.chatLogs = []);
      renderChat();
    }
  </script>
</body>
</html>
'''

# 3. ACCOUNTS.HTML
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
          <p class="text-xs text-slate-400 mt-1 font-mono">Manage Microsoft OAuth session tokens (SSID) & credentials</p>
        </div>
        <button onclick="openModal('linkAccModal')" class="btn-primary">
          <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>
          <span>Link Account by SSID</span>
        </button>
      </div>

      <!-- Security Notice Banner -->
      <div class="p-4 rounded-xl bg-[#0a0d14] border border-emerald-500/20 text-xs text-slate-300 flex items-start space-x-3">
        <span class="text-emerald-400 mt-0.5">
          <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
        </span>
        <div>
          <strong class="text-emerald-400 font-bold">Hardware-Level Vault Encryption:</strong>
          <span>All Minecraft tokens & SSIDs are stored locally encrypted with <strong>AES-256-GCM</strong>. Tokens never leave your local machine or server.</span>
        </div>
      </div>

      <!-- Accounts Table -->
      <div class="overflow-x-auto rounded-xl border border-[#1c2333]">
        <table class="w-full text-left text-sm text-slate-300">
          <thead class="bg-[#0c1018] text-xs uppercase font-mono text-slate-400 border-b border-[#1c2333]">
            <tr>
              <th class="px-4 py-3">Avatar</th>
              <th class="px-4 py-3">Username</th>
              <th class="px-4 py-3">UUID</th>
              <th class="px-4 py-3">Auth Status</th>
              <th class="px-4 py-3">Added Date</th>
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
    <div class="pie-card p-6 max-w-lg w-full space-y-4 border border-[#1c2333]">
      <div class="flex items-center justify-between border-b border-[#1c2333] pb-3">
        <h3 class="text-lg font-bold text-white">Link Minecraft Account (SSID / Session)</h3>
        <button onclick="closeModal('linkAccModal')" class="text-slate-400 hover:text-white">&times;</button>
      </div>

      <div class="space-y-3 text-xs">
        <div>
          <label class="block font-semibold text-slate-300 mb-1">Account Display Username</label>
          <input id="modalAccName" type="text" placeholder="e.g. PieBot_Prime" class="pie-input w-full font-mono">
        </div>
        <div>
          <label class="block font-semibold text-slate-300 mb-1">Session Token / SSID (Microsoft OAuth JWT)</label>
          <textarea id="modalAccToken" rows="4" placeholder="Paste your Microsoft launcher session token (SSID) here..." class="pie-input w-full font-mono text-cyan-300"></textarea>
        </div>
      </div>

      <div class="flex items-center justify-end space-x-3 pt-2">
        <button onclick="closeModal('linkAccModal')" class="btn-secondary text-xs">Cancel</button>
        <button onclick="submitAccount()" class="btn-primary text-xs">Verify & Link Account</button>
      </div>
    </div>
  </div>

  <script>
    document.addEventListener('DOMContentLoaded', () => {
      renderGlobalHeader('accounts');
      renderInstanceBar();
      renderAccountsTable();
    });

    function renderAccountsTable() {
      const tbody = document.getElementById('accTableBody');
      tbody.innerHTML = state.accounts.map(a => `
        <tr class="hover:bg-slate-900/40 transition-colors">
          <td class="px-4 py-3">
            <div class="w-8 h-8 rounded bg-slate-800 border border-[#1c2333] overflow-hidden flex items-center justify-center">
              <img src="https://mc-heads.net/avatar/${a.username}/28" alt="" onerror="this.src='data:image/svg+xml;utf8,<svg xmlns=\\'http://www.w3.org/2000/svg\\' width=\\'28\\' height=\\'28\\' fill=\\'%232cf5d6\\'><rect width=\\'28\\' height=\\'28\\' fill=\\'%231e293b\\'/></svg>'">
            </div>
          </td>
          <td class="px-4 py-3 font-bold text-white">${a.username}</td>
          <td class="px-4 py-3 text-slate-400">${a.uuid}</td>
          <td class="px-4 py-3"><span class="badge-online">AUTHENTICATED</span></td>
          <td class="px-4 py-3 text-slate-500">${a.added}</td>
          <td class="px-4 py-3 text-right">
            <button onclick="removeAccount('${a.id}')" class="text-red-400 hover:text-red-300">
              <svg class="w-4 h-4 inline" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="3 6 5 6 21 6"></polyline><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"></path></svg>
            </button>
          </td>
        </tr>
      `).join('');
    }

    function submitAccount() {
      const name = document.getElementById('modalAccName').value.trim() || 'PiePlayer_' + Math.floor(Math.random()*900+100);
      window.updatePieState(s => {
        s.accounts.push({
          id: String(Date.now()),
          username: name,
          uuid: 'd' + Math.random().toString(16).substring(2, 10) + '-4a11-98bc',
          status: 'authenticated',
          added: new Date().toISOString().split('T')[0]
        });
      });
      closeModal('linkAccModal');
      renderAccountsTable();
    }

    function removeAccount(id) {
      window.updatePieState(s => {
        s.accounts = s.accounts.filter(a => a.id !== id);
      });
      renderAccountsTable();
    }
  </script>
</body>
</html>
'''

# 4. SERVERS.HTML
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
          <p class="text-xs text-slate-400 mt-1 font-mono">Manage network endpoints, protocols, and latency trackers</p>
        </div>
        <button onclick="openModal('addSrvModal')" class="btn-primary">
          <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>
          <span>Add Server</span>
        </button>
      </div>

      <!-- Server Cards Grid -->
      <div id="serversGrid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      </div>
    </div>
  </main>

  <!-- Add Server Modal -->
  <div id="addSrvModal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm hidden items-center justify-center p-4">
    <div class="pie-card p-6 max-w-md w-full space-y-4 border border-[#1c2333]">
      <div class="flex items-center justify-between border-b border-[#1c2333] pb-3">
        <h3 class="text-lg font-bold text-white">Add Target Minecraft Server</h3>
        <button onclick="closeModal('addSrvModal')" class="text-slate-400 hover:text-white">&times;</button>
      </div>

      <div class="space-y-3 text-xs">
        <div>
          <label class="block font-semibold text-slate-300 mb-1">Server Name</label>
          <input id="modalSrvName" type="text" placeholder="e.g. Hypixel Network" class="pie-input w-full">
        </div>
        <div>
          <label class="block font-semibold text-slate-300 mb-1">Host / IP</label>
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
      grid.innerHTML = state.servers.map(s => `
        <div class="pie-card-inner p-4 space-y-3 border border-[#1c2333]">
          <div class="flex items-center justify-between">
            <h4 class="font-bold text-white text-base">${s.name}</h4>
            <span class="badge-online">ONLINE</span>
          </div>
          <div class="text-xs font-mono text-slate-400 space-y-1">
            <div>Address: <span class="text-slate-200 font-semibold">${s.host}:${s.port}</span></div>
            <div>Players: <span class="text-slate-300">${s.players}</span></div>
            <div>Latency: <span class="text-cyan-400 font-bold">${s.ping}</span></div>
          </div>
          <div class="flex items-center justify-end space-x-2 pt-2 border-t border-[#1c2333]">
            <button onclick="removeServer('${s.id}')" class="text-red-400 hover:text-red-300 text-xs">Delete</button>
          </div>
        </div>
      `).join('');
    }

    function submitServer() {
      const name = document.getElementById('modalSrvName').value.trim() || 'Custom MC Server';
      const host = document.getElementById('modalSrvHost').value.trim() || '127.0.0.1';
      const port = parseInt(document.getElementById('modalSrvPort').value) || 25565;

      window.updatePieState(s => {
        s.servers.push({ id: String(Date.now()), name, host, port, players: '1/50', ping: '15ms', status: 'online' });
      });
      closeModal('addSrvModal');
      renderServersGrid();
    }

    function removeServer(id) {
      window.updatePieState(s => {
        s.servers = s.servers.filter(x => x.id !== id);
      });
      renderServersGrid();
    }
  </script>
</body>
</html>
'''

# 5. PROXIES.HTML
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

  <!-- Add Proxy Modal -->
  <div id="addPrxModal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm hidden items-center justify-center p-4">
    <div class="pie-card p-6 max-w-md w-full space-y-4 border border-[#1c2333]">
      <div class="flex items-center justify-between border-b border-[#1c2333] pb-3">
        <h3 class="text-lg font-bold text-white">Add Proxy Node</h3>
        <button onclick="closeModal('addPrxModal')" class="text-slate-400 hover:text-white">&times;</button>
      </div>

      <div class="space-y-3 text-xs">
        <div>
          <label class="block font-semibold text-slate-300 mb-1">Name</label>
          <input id="modalPrxName" type="text" placeholder="e.g. US Residential Node" class="pie-input w-full">
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

  <!-- Import Modal -->
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
      tbody.innerHTML = state.proxies.map(p => `
        <tr class="hover:bg-slate-900/40 transition-colors">
          <td class="px-4 py-3 font-bold text-white">${p.name}</td>
          <td class="px-4 py-3"><span class="badge-diamond">${p.type}</span></td>
          <td class="px-4 py-3 text-slate-300">${p.host}:${p.port}</td>
          <td class="px-4 py-3 text-slate-400">${p.auth}</td>
          <td class="px-4 py-3 text-cyan-400 font-semibold">${p.latency}</td>
          <td class="px-4 py-3 text-right">
            <button onclick="removeProxy('${p.id}')" class="text-red-400 hover:text-red-300">Delete</button>
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

    function removeProxy(id) {
      window.updatePieState(s => {
        s.proxies = s.proxies.filter(x => x.id !== id);
      });
      renderProxiesTable();
    }
  </script>
</body>
</html>
'''

# 6. AUTOMATION.HTML
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
          <p class="text-xs text-slate-400 mt-1 font-mono">Interval-based repeating broadcasts & routine commands</p>
        </div>
        <button onclick="openModal('addAutoModal')" class="btn-primary text-xs">
          <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>
          <span>New Automation</span>
        </button>
      </div>

      <div class="overflow-x-auto rounded-xl border border-[#1c2333]">
        <table class="w-full text-left text-sm text-slate-300">
          <thead class="bg-[#0c1018] text-xs uppercase font-mono text-slate-400 border-b border-[#1c2333]">
            <tr>
              <th class="px-4 py-3">Status</th>
              <th class="px-4 py-3">Message / Command</th>
              <th class="px-4 py-3">Interval</th>
              <th class="px-4 py-3">Scope</th>
              <th class="px-4 py-3 text-right">Actions</th>
            </tr>
          </thead>
          <tbody id="autoTableBody" class="divide-y divide-[#1c2333]/80 bg-[#090b10] font-mono text-xs">
          </tbody>
        </table>
      </div>
    </div>
  </main>

  <!-- Add Automation Modal -->
  <div id="addAutoModal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm hidden items-center justify-center p-4">
    <div class="pie-card p-6 max-w-md w-full space-y-4 border border-[#1c2333]">
      <div class="flex items-center justify-between border-b border-[#1c2333] pb-3">
        <h3 class="text-lg font-bold text-white">New Scheduled Task</h3>
        <button onclick="closeModal('addAutoModal')" class="text-slate-400 hover:text-white">&times;</button>
      </div>

      <div class="space-y-3 text-xs">
        <div>
          <label class="block font-semibold text-slate-300 mb-1">Message / Command</label>
          <input id="modalAutoMsg" type="text" placeholder="e.g. /clan broadcast We are recruiting!" class="pie-input w-full">
        </div>
        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block font-semibold text-slate-300 mb-1">Interval</label>
            <input id="modalAutoInterval" type="number" value="60" class="pie-input w-full">
          </div>
          <div>
            <label class="block font-semibold text-slate-300 mb-1">Unit</label>
            <select id="modalAutoUnit" class="pie-select w-full">
              <option value="seconds">Seconds</option>
              <option value="minutes">Minutes</option>
              <option value="hours">Hours</option>
            </select>
          </div>
        </div>
      </div>

      <div class="flex items-center justify-end space-x-3 pt-2">
        <button onclick="closeModal('addAutoModal')" class="btn-secondary text-xs">Cancel</button>
        <button onclick="submitAuto()" class="btn-primary text-xs">Create Task</button>
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
      tbody.innerHTML = state.automations.map(au => `
        <tr class="hover:bg-slate-900/40 transition-colors">
          <td class="px-4 py-3">
            <button onclick="toggleAuto('${au.id}')" class="${au.status ? 'badge-online' : 'badge-offline'}">
              ${au.status ? 'ACTIVE' : 'PAUSED'}
            </button>
          </td>
          <td class="px-4 py-3 font-semibold text-white">${au.msg}</td>
          <td class="px-4 py-3 text-cyan-300">${au.interval}</td>
          <td class="px-4 py-3 text-slate-400">${au.scope}</td>
          <td class="px-4 py-3 text-right">
            <button onclick="removeAuto('${au.id}')" class="text-red-400 hover:text-red-300">Delete</button>
          </td>
        </tr>
      `).join('');
    }

    function toggleAuto(id) {
      window.updatePieState(s => {
        const item = s.automations.find(x => x.id === id);
        if (item) item.status = !item.status;
      });
      renderAutoTable();
    }

    function submitAuto() {
      const msg = document.getElementById('modalAutoMsg').value.trim() || '/help';
      const interval = document.getElementById('modalAutoInterval').value + ' ' + document.getElementById('modalAutoUnit').value;

      window.updatePieState(s => {
        s.automations.push({
          id: String(Date.now()),
          msg, interval, status: true,
          scope: 'Instance ' + s.activeInstanceId
        });
      });
      closeModal('addAutoModal');
      renderAutoTable();
    }

    function removeAuto(id) {
      window.updatePieState(s => {
        s.automations = s.automations.filter(x => x.id !== id);
      });
      renderAutoTable();
    }
  </script>
</body>
</html>
'''

# 7. TRIGGERS.HTML
triggers_html = '''<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Pie MC — Reactive Triggers</title>
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
          <h2 class="text-xl font-black text-white">Reactive Chat Triggers</h2>
          <p class="text-xs text-slate-400 mt-1 font-mono">Auto-respond to keywords, player mentions, and server triggers</p>
        </div>
        <button onclick="openModal('addTrgModal')" class="btn-primary text-xs">
          <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>
          <span>New Trigger</span>
        </button>
      </div>

      <div class="overflow-x-auto rounded-xl border border-[#1c2333]">
        <table class="w-full text-left text-sm text-slate-300">
          <thead class="bg-[#0c1018] text-xs uppercase font-mono text-slate-400 border-b border-[#1c2333]">
            <tr>
              <th class="px-4 py-3">Status</th>
              <th class="px-4 py-3">Trigger Name</th>
              <th class="px-4 py-3">Keyword Match</th>
              <th class="px-4 py-3">Reply Action</th>
              <th class="px-4 py-3">Cooldown</th>
              <th class="px-4 py-3 text-right">Actions</th>
            </tr>
          </thead>
          <tbody id="trgTableBody" class="divide-y divide-[#1c2333]/80 bg-[#090b10] font-mono text-xs">
          </tbody>
        </table>
      </div>
    </div>
  </main>

  <!-- Add Trigger Modal -->
  <div id="addTrgModal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm hidden items-center justify-center p-4">
    <div class="pie-card p-6 max-w-lg w-full space-y-4 border border-[#1c2333]">
      <div class="flex items-center justify-between border-b border-[#1c2333] pb-3">
        <h3 class="text-lg font-bold text-white">Create Reactive Trigger</h3>
        <button onclick="closeModal('addTrgModal')" class="text-slate-400 hover:text-white">&times;</button>
      </div>

      <div class="space-y-3 text-xs">
        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block font-semibold text-slate-300 mb-1">Trigger Name</label>
            <input id="modalTrgName" type="text" placeholder="e.g. Greeter" class="pie-input w-full">
          </div>
          <div>
            <label class="block font-semibold text-slate-300 mb-1">Keyword</label>
            <input id="modalTrgKeyword" type="text" placeholder="e.g. hello or !help" class="pie-input w-full font-mono">
          </div>
        </div>

        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block font-semibold text-slate-300 mb-1">Match Mode</label>
            <select id="modalTrgMode" class="pie-select w-full">
              <option value="Keyword anywhere">Keyword anywhere</option>
              <option value="Exact match">Exact match</option>
              <option value="Starts with">Starts with</option>
              <option value="Regex">Regex Pattern</option>
            </select>
          </div>
          <div>
            <label class="block font-semibold text-slate-300 mb-1">Cooldown (Seconds)</label>
            <input id="modalTrgCooldown" type="number" value="10" class="pie-input w-full">
          </div>
        </div>

        <div>
          <label class="block font-semibold text-slate-300 mb-1">Reply Message / Command</label>
          <input id="modalTrgReply" type="text" placeholder="e.g. Welcome {player}! Type !discord for info" class="pie-input w-full font-mono text-cyan-300">
        </div>
      </div>

      <div class="flex items-center justify-end space-x-3 pt-2">
        <button onclick="closeModal('addTrgModal')" class="btn-secondary text-xs">Cancel</button>
        <button onclick="submitTrigger()" class="btn-primary text-xs">Create Trigger</button>
      </div>
    </div>
  </div>

  <script>
    document.addEventListener('DOMContentLoaded', () => {
      renderGlobalHeader('triggers');
      renderInstanceBar();
      renderTrgTable();
    });

    function renderTrgTable() {
      const tbody = document.getElementById('trgTableBody');
      tbody.innerHTML = state.triggers.map(tr => `
        <tr class="hover:bg-slate-900/40 transition-colors">
          <td class="px-4 py-3">
            <button onclick="toggleTrg('${tr.id}')" class="${tr.status ? 'badge-online' : 'badge-offline'}">
              ${tr.status ? 'ENABLED' : 'DISABLED'}
            </button>
          </td>
          <td class="px-4 py-3 font-bold text-white">${tr.name}</td>
          <td class="px-4 py-3 text-[#2cf5d6]"><code>${tr.keyword}</code> (${tr.mode})</td>
          <td class="px-4 py-3 text-slate-300">${tr.reply}</td>
          <td class="px-4 py-3 text-slate-400">${tr.cooldown}s</td>
          <td class="px-4 py-3 text-right">
            <button onclick="removeTrg('${tr.id}')" class="text-red-400 hover:text-red-300">Delete</button>
          </td>
        </tr>
      `).join('');
    }

    function toggleTrg(id) {
      window.updatePieState(s => {
        const item = s.triggers.find(x => x.id === id);
        if (item) item.status = !item.status;
      });
      renderTrgTable();
    }

    function submitTrigger() {
      const name = document.getElementById('modalTrgName').value.trim() || 'Trigger';
      const keyword = document.getElementById('modalTrgKeyword').value.trim() || '!test';
      const mode = document.getElementById('modalTrgMode').value;
      const cooldown = parseInt(document.getElementById('modalTrgCooldown').value) || 10;
      const reply = document.getElementById('modalTrgReply').value.trim() || 'Auto response';

      window.updatePieState(s => {
        s.triggers.push({ id: String(Date.now()), name, keyword, mode, cooldown, reply, status: true });
      });
      closeModal('addTrgModal');
      renderTrgTable();
    }

    function removeTrg(id) {
      window.updatePieState(s => {
        s.triggers = s.triggers.filter(x => x.id !== id);
      });
      renderTrgTable();
    }
  </script>
</body>
</html>
'''

# 8. DISCORD.HTML
discord_html = '''<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Pie MC — Discord Bridge</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="styles.css">
  <script src="shared.js"></script>
</head>
<body>
  <div id="header-mount"></div>
  <div id="instance-bar-mount"></div>

  <main class="flex-1 p-6 max-w-7xl w-full mx-auto space-y-6">
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
      <div class="pie-card p-6 space-y-4">
        <h2 class="text-lg font-bold text-white flex items-center space-x-2">
          <span>Discord Webhook Relay</span>
        </h2>
        <p class="text-xs text-slate-400">Forward Minecraft whispers and alerts straight to your Discord channel.</p>

        <div class="space-y-3 pt-2">
          <div>
            <label class="text-xs font-semibold text-slate-300">Webhook URL</label>
            <input type="text" id="discordWebhookInput" value="https://discord.com/api/webhooks/123/abc..." class="pie-input w-full font-mono text-xs mt-1">
          </div>

          <div class="space-y-2 pt-2">
            <label class="flex items-center space-x-2 text-xs text-slate-300">
              <input type="checkbox" checked class="rounded bg-slate-800 text-[#2cf5d6]">
              <span>Direct Whispers & PMs</span>
            </label>
            <label class="flex items-center space-x-2 text-xs text-slate-300">
              <input type="checkbox" checked class="rounded bg-slate-800 text-[#2cf5d6]">
              <span>Player Mentions & Alerts</span>
            </label>
            <label class="flex items-center space-x-2 text-xs text-slate-300">
              <input type="checkbox" checked class="rounded bg-slate-800 text-[#2cf5d6]">
              <span>Bot Disconnect & Reconnect Notices</span>
            </label>
          </div>

          <button onclick="saveDiscord()" class="btn-primary w-full text-xs py-2.5">Save Discord Bridge</button>
        </div>
      </div>

      <div class="pie-card p-6 lg:col-span-2 space-y-4 flex flex-col h-[520px]">
        <div class="flex items-center justify-between pb-3 border-b border-[#1c2333]">
          <div class="flex items-center space-x-3">
            <div class="w-8 h-8 rounded-full bg-indigo-500/20 text-indigo-400 flex items-center justify-center font-bold text-xs">
              #
            </div>
            <div>
              <h3 class="text-sm font-bold text-white">#mc-bot-relay (Live Feed)</h3>
              <span class="badge-online">WEBHOOK ACTIVE</span>
            </div>
          </div>
          <button onclick="clearRelay()" class="btn-secondary text-xs px-2 py-1">Clear Feed</button>
        </div>

        <div id="discordRelayList" class="flex-1 overflow-y-auto bg-[#090b10] rounded-xl p-4 font-mono text-xs space-y-3 border border-[#1c2333]">
        </div>
      </div>
    </div>
  </main>

  <script>
    document.addEventListener('DOMContentLoaded', () => {
      renderGlobalHeader('discord');
      renderInstanceBar();
      renderDiscord();
    });

    function renderDiscord() {
      const feed = document.getElementById('discordRelayList');
      feed.innerHTML = state.discordRelay.map(d => `
        <div class="p-3 rounded-lg bg-[#0c1018] border border-[#1c2333]">
          <div class="flex items-center justify-between text-[10px] text-slate-500 mb-1">
            <span class="font-bold text-indigo-400">${d.author}</span>
            <span>${d.time}</span>
          </div>
          <p class="text-slate-200">${d.content}</p>
        </div>
      `).join('');
    }

    function saveDiscord() {
      alert('Discord webhook configuration saved successfully!');
    }

    function clearRelay() {
      window.updatePieState(s => s.discordRelay = []);
      renderDiscord();
    }
  </script>
</body>
</html>
'''

# 9. LOGS.HTML
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
          <h2 class="text-xl font-black text-white">System & Trigger Audit Logs</h2>
          <p class="text-xs text-slate-400 mt-1 font-mono">Real-time telemetry, connection drops, and executed actions</p>
        </div>
        <div class="flex items-center space-x-3">
          <input id="logSearch" oninput="filterLogs()" type="text" placeholder="Search player or event..." class="pie-input text-xs w-48">
          <button onclick="clearLogs()" class="btn-secondary text-xs">Clear</button>
        </div>
      </div>

      <div class="overflow-x-auto rounded-xl border border-[#1c2333]">
        <table class="w-full text-left text-sm text-slate-300">
          <thead class="bg-[#0c1018] text-xs uppercase font-mono text-slate-400 border-b border-[#1c2333]">
            <tr>
              <th class="px-4 py-3">Timestamp</th>
              <th class="px-4 py-3">Instance</th>
              <th class="px-4 py-3">Event Type</th>
              <th class="px-4 py-3">Player / Target</th>
              <th class="px-4 py-3">Details</th>
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
      renderLogsTable(state.logs);
    });

    function renderLogsTable(logList) {
      const tbody = document.getElementById('logsTableBody');
      tbody.innerHTML = logList.map(l => `
        <tr class="hover:bg-slate-900/40 transition-colors">
          <td class="px-4 py-3 text-slate-500">${l.time}</td>
          <td class="px-4 py-3 text-[#2cf5d6]">${l.instance}</td>
          <td class="px-4 py-3"><span class="badge-diamond">${l.event}</span></td>
          <td class="px-4 py-3 text-white font-bold">${l.player}</td>
          <td class="px-4 py-3 text-slate-400">${l.details}</td>
        </tr>
      `).join('');
    }

    function filterLogs() {
      const q = document.getElementById('logSearch').value.toLowerCase();
      const filtered = state.logs.filter(l => 
        l.player.toLowerCase().includes(q) || 
        l.event.toLowerCase().includes(q) || 
        l.details.toLowerCase().includes(q)
      );
      renderLogsTable(filtered);
    }

    function clearLogs() {
      window.updatePieState(s => s.logs = []);
      renderLogsTable([]);
    }
  </script>
</body>
</html>
'''

# 10. SETTINGS.HTML
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
          <h2 class="text-xl font-black text-white">Pie MC System Configuration</h2>
          <p class="text-xs text-slate-400 mt-1 font-mono">Connection policies, security credentials, and protocol versions</p>
        </div>
      </div>

      <div class="space-y-6 text-sm">
        <!-- Reconnect Section -->
        <div class="space-y-3">
          <h3 class="text-xs font-bold uppercase tracking-wider text-[#2cf5d6] font-mono">Connection & Reconnect Policies</h3>
          
          <label class="flex items-center justify-between p-4 rounded-xl pie-card-inner border border-[#1c2333]">
            <div>
              <span class="font-bold text-white block">Auto-Reconnect on Disconnect</span>
              <span class="text-xs text-slate-400">Automatically re-establish connection after kicks or server restarts</span>
            </div>
            <input type="checkbox" checked class="w-4 h-4 rounded text-[#2cf5d6]">
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

        <!-- Security & Version -->
        <div class="space-y-3 pt-4 border-t border-[#1c2333]">
          <h3 class="text-xs font-bold uppercase tracking-wider text-[#2cf5d6] font-mono">Security & API Access</h3>
          
          <div class="space-y-1">
            <label class="text-xs font-semibold text-slate-300">Backend API Key (Bearer)</label>
            <input type="text" value="pie_mc_live_89437b02c89f4172" class="pie-input w-full font-mono text-[#2cf5d6]">
          </div>

          <div class="space-y-1">
            <label class="text-xs font-semibold text-slate-300">Minecraft Target Version Protocol</label>
            <select class="pie-select w-full font-mono">
              <option>1.21.1 / 1.21.11 (Latest)</option>
              <option>1.20.4</option>
              <option>1.19.4</option>
              <option>1.16.5</option>
              <option>1.8.9</option>
            </select>
          </div>
        </div>

        <div class="pt-4 flex justify-end">
          <button onclick="alert('Settings saved successfully!')" class="btn-primary">Save Preferences</button>
        </div>
      </div>
    </div>
  </main>

  <script>
    document.addEventListener('DOMContentLoaded', () => {
      renderGlobalHeader('');
      renderInstanceBar();
    });
  </script>
</body>
</html>
'''

pages = {
    'index.html': index_html,
    'dashboard.html': index_html,
    'chat.html': chat_html,
    'accounts.html': accounts_html,
    'servers.html': servers_html,
    'proxies.html': proxies_html,
    'automation.html': automation_html,
    'triggers.html': triggers_html,
    'discord.html': discord_html,
    'logs.html': logs_html,
    'settings.html': settings_html
}

for filename, content in pages.items():
    filepath = os.path.join(PUB, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Written {filename}')

print("All 10 multi-page HTML files successfully generated!")
