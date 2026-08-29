import os

PUB = '/working_dir/c_37017e0a3b8a7bd1/pie-mc/public'

# 1. LOGIN.HTML
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

  <!-- Background Glow -->
  <div class="absolute -top-32 -left-32 w-96 h-96 bg-[#2cf5d6]/10 rounded-full blur-3xl pointer-events-none"></div>
  <div class="absolute -bottom-32 -right-32 w-96 h-96 bg-indigo-600/10 rounded-full blur-3xl pointer-events-none"></div>

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
        <p class="text-xs text-slate-400 font-mono mt-1">Multi-Instance Bot Engine & Manager</p>
      </div>
    </div>

    <!-- Login Description -->
    <div class="p-4 rounded-xl bg-[#0a0d14] border border-[#1c2333] text-xs text-slate-300 space-y-2">
      <p class="font-semibold text-white">Authentication Required</p>
      <p class="text-slate-400 leading-relaxed">
        Sign in via Discord OAuth to access your isolated bot instances, SSID token vault, and automation workspace.
      </p>
    </div>

    <!-- OAuth Actions -->
    <div class="space-y-3">
      <!-- Standard User Login -->
      <button onclick="handleDiscordLogin(false)" class="w-full py-3.5 px-4 rounded-xl bg-[#5865F2] hover:bg-[#4752C4] text-white font-bold text-sm shadow-lg shadow-indigo-500/25 flex items-center justify-center space-x-3 transition-all transform active:scale-95">
        <svg class="w-5 h-5 fill-current" viewBox="0 0 24 24"><path d="M20.317 4.37a19.791 19.791 0 0 0-4.885-1.515.074.074 0 0 0-.079.037c-.21.375-.444.864-.608 1.25a18.27 18.27 0 0 0-5.487 0 12.64 12.64 0 0 0-.617-1.25.077.077 0 0 0-.079-.037A19.736 19.736 0 0 0 3.677 4.37a.07.07 0 0 0-.032.027C.533 9.046-.32 13.58.099 18.057a.082.082 0 0 0 .031.057 19.9 19.9 0 0 0 5.993 3.03.078.078 0 0 0 .084-.028c.462-.63.874-1.295 1.226-1.994.021-.041.001-.09-.041-.106a13.107 13.107 0 0 1-1.872-.892.077.077 0 0 1-.008-.128 10.2 10.2 0 0 0 .372-.292.074.074 0 0 1 .077-.01c3.929 1.793 8.18 1.793 12.061 0a.074.074 0 0 1 .078.01c.12.098.246.198.373.292a.077.077 0 0 1-.006.127 12.299 12.299 0 0 1-1.873.894.077.077 0 0 0-.041.107c.36.698.772 1.362 1.225 1.993a.076.076 0 0 0 .084.028 19.839 19.839 0 0 0 6.002-3.03.077.077 0 0 0 .032-.054c.5-5.177-.838-9.674-3.549-13.66a.061.061 0 0 0-.031-.028zM8.02 15.33c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.956-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.956 2.418-2.157 2.418zm7.975 0c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.955-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.946 2.418-2.157 2.418z"/></svg>
        <span>Login with Discord</span>
      </button>

      <!-- Owner / Admin Login -->
      <button onclick="handleDiscordLogin(true)" class="w-full py-2.5 px-4 rounded-xl bg-[#0f131d] hover:bg-slate-800 text-slate-300 hover:text-white font-semibold text-xs border border-[#1c2333] hover:border-[#2cf5d6]/40 flex items-center justify-center space-x-2 transition-all">
        <svg class="w-4 h-4 text-[#2cf5d6]" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg>
        <span>Login as Platform Owner (Admin Mode)</span>
      </button>
    </div>

    <div class="text-center pt-2 border-t border-[#1c2333]/80">
      <span class="text-[11px] font-mono text-slate-500">AES-256-GCM Vault &bull; Isolated User Sessions</span>
    </div>
  </div>

  <script>
    function handleDiscordLogin(isOwner) {
      const username = isOwner ? 'PieOwner' : 'DiscordUser_' + Math.floor(Math.random()*900+100);
      const id = isOwner ? '987654321098765432' : String(Math.floor(Math.random()*899999999999999999 + 100000000000000000));

      const userObj = {
        id: id,
        username: username,
        discriminator: '0001',
        avatar: `https://api.dicebear.com/7.x/bottts/svg?seed=${username}`,
        isOwner: isOwner,
        authTime: new Date().toISOString()
      };

      setCurrentUser(userObj);
      window.location.href = isOwner ? 'admin.html' : 'index.html';
    }
  </script>
</body>
</html>
'''

# 2. ADMIN.HTML (OWNER ADMIN DASHBOARD)
admin_html = '''<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Pie MC — Owner Admin Console</title>
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
              <h1 class="text-2xl font-black text-white">Owner Admin Portal</h1>
              <span class="badge-diamond text-xs font-mono">ROOT ACCESS</span>
            </div>
            <p class="text-xs text-slate-400 font-mono mt-0.5">Platform telemetry & user management overview</p>
          </div>
        </div>
        <a href="index.html" class="btn-secondary text-xs px-4 py-2">
          &larr; Back to My Dashboard
        </a>
      </div>

      <!-- Strict Privacy Notice -->
      <div class="p-4 rounded-xl bg-[#0a0d14] border border-cyan-500/30 flex items-start space-x-3 text-xs">
        <svg class="w-5 h-5 text-cyan-400 mt-0.5 flex-shrink-0" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
        <div class="text-slate-300 leading-relaxed">
          <strong class="text-[#2cf5d6]">Privacy & Zero-Knowledge Policy Active:</strong>
          <span> As the platform owner, you can view user counts, instance loads, and account quantities. For end-user security and privacy, you <strong>cannot</strong> view actual Minecraft account names, UUIDs, or session tokens (SSIDs).</span>
        </div>
      </div>
    </div>

    <!-- Platform High-Level Telemetry Cards -->
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

    <!-- Registered Users Telemetry Table (Privacy Filtered) -->
    <div class="pie-card p-6 space-y-4">
      <div class="flex items-center justify-between">
        <h2 class="text-lg font-bold text-white">Registered Users & Workspace Telemetry</h2>
        <span class="text-xs font-mono text-slate-400">Anonymized Data</span>
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
    document.addEventListener('DOMContentLoaded', () => {
      const user = getCurrentUser();
      if (!user || (!user.isOwner && user.id !== OWNER_DISCORD_ID)) {
        window.location.href = 'index.html';
        return;
      }

      renderGlobalHeader('admin');
      renderAdminTelemetry();
    });

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
            <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
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
        message: `This will safely trigger a reconnect for all active instances owned by Discord User <strong>${uname}</strong> (${uid}).`,
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

with open(os.path.join(PUB, 'login.html'), 'w', encoding='utf-8') as f:
    f.write(login_html)
print("Written login.html")

with open(os.path.join(PUB, 'admin.html'), 'w', encoding='utf-8') as f:
    f.write(admin_html)
print("Written admin.html")
