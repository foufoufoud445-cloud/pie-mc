import os

PUB = '/working_dir/c_37017e0a3b8a7bd1/pie-mc/public'

# SERVERS.HTML
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
        s.servers.push({ id: String(Date.now()), name, host, port, players: '1/50', ping: '15ms', status: 'online' });
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

# PROXIES.HTML
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

# AUTOMATION.HTML
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
            <button onclick="removeAutoPrompt('${au.id}', '${au.msg}')" class="text-red-400 hover:text-red-300 text-xs">Delete</button>
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

# TRIGGERS.HTML
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
            <button onclick="removeTrgPrompt('${tr.id}', '${tr.name}')" class="text-red-400 hover:text-red-300 text-xs">Delete</button>
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

    function removeTrgPrompt(id, name) {
      window.showConfirmModal({
        title: `Delete Trigger ${name}?`,
        message: `Are you sure you want to delete trigger rule <strong>${name}</strong>?`,
        confirmText: 'Delete Trigger',
        cancelText: 'Cancel',
        isDanger: true,
        onConfirm: () => {
          window.updatePieState(s => {
            s.triggers = s.triggers.filter(x => x.id !== id);
          });
          renderTrgTable();
        }
      });
    }
  </script>
</body>
</html>
'''

with open(os.path.join(PUB, 'servers.html'), 'w', encoding='utf-8') as f:
    f.write(servers_html)

with open(os.path.join(PUB, 'proxies.html'), 'w', encoding='utf-8') as f:
    f.write(proxies_html)

with open(os.path.join(PUB, 'automation.html'), 'w', encoding='utf-8') as f:
    f.write(automation_html)

with open(os.path.join(PUB, 'triggers.html'), 'w', encoding='utf-8') as f:
    f.write(triggers_html)

print("Updated CRUD pages with custom confirmation modal!")
