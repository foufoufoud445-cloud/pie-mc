import os

PUB = '/working_dir/c_37017e0a3b8a7bd1/pie-mc/public'

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
        <!-- Account Selector with Token Expiry Alert Tag -->
        <div class="pie-card-inner p-4 space-y-2">
          <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-slate-400 uppercase tracking-wider">ACTIVE ACCOUNT</span>
            <span id="cardAccStatusBadge" class="badge-online">AUTHENTICATED</span>
          </div>
          <select id="accSelect" onchange="changeActiveAccount(this.value)" class="pie-select w-full py-2 px-3 text-sm font-semibold text-white">
          </select>
          <div class="flex items-center justify-between text-[11px] font-mono text-slate-400 pt-1">
            <span>UUID: <span id="accUUID" class="text-slate-300">d8f3-4a11-98bc</span></span>
            <a href="accounts.html" id="accReauthLink" class="text-[#2cf5d6] hover:underline font-semibold">Manage Vault &rarr;</a>
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

      // Check current account status
      const currentAcc = state.accounts.find(a => a.username === inst.account);
      const accBadge = document.getElementById('cardAccStatusBadge');
      if (currentAcc && (currentAcc.status === 'needs_reauth' || currentAcc.tokenExpiryStatus === 'needs_reauth')) {
        accBadge.className = 'px-2 py-0.5 rounded text-[10px] font-mono font-bold bg-amber-500/15 text-amber-400 border border-amber-500/30';
        accBadge.innerText = 'NEEDS RE-AUTH';
      } else {
        accBadge.className = 'badge-online';
        accBadge.innerText = 'AUTHENTICATED';
      }

      // Selectors
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

with open(os.path.join(PUB, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(index_html)
with open(os.path.join(PUB, 'dashboard.html'), 'w', encoding='utf-8') as f:
    f.write(index_html)

print("Updated index.html and dashboard.html with Token Expiry Alert status badge!")
