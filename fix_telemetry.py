import os

PUB = '/working_dir/c_37017e0a3b8a7bd1/pie-mc/public'

# 1. Update shared.js with getDynamicTelemetry and automatic registration
with open(os.path.join(PUB, 'shared.js'), 'r', encoding='utf-8') as f:
    code = f.read()

dynamic_telemetry_code = '''
// Dynamic Directory & Telemetry Engine (Scans all local tenant partitions)
window.registerUserDirectory = function(user) {
  if (!user || !user.id) return;
  const list = JSON.parse(localStorage.getItem('PIE_MC_REGISTERED_USERS') || '[]');
  const idx = list.findIndex(u => u.id === user.id);
  if (idx === -1) {
    list.push({
      id: user.id,
      username: user.username,
      joined: new Date().toISOString().split('T')[0],
      isOwner: user.isOwner || (user.id === OWNER_DISCORD_ID)
    });
  } else {
    list[idx].username = user.username;
    list[idx].isOwner = user.isOwner || (user.id === OWNER_DISCORD_ID);
  }
  localStorage.setItem('PIE_MC_REGISTERED_USERS', JSON.stringify(list));
};

window.getDynamicTelemetry = function() {
  let list = JSON.parse(localStorage.getItem('PIE_MC_REGISTERED_USERS') || '[]');
  
  // If empty, ensure Owner and current user are registered
  const curUser = getCurrentUser();
  if (list.length === 0) {
    list = [
      { id: OWNER_DISCORD_ID, username: 'PieOwner', joined: '2026-08-01', isOwner: true }
    ];
    if (curUser && curUser.id !== OWNER_DISCORD_ID) {
      list.push({ id: curUser.id, username: curUser.username, joined: new Date().toISOString().split('T')[0], isOwner: false });
    }
    localStorage.setItem('PIE_MC_REGISTERED_USERS', JSON.stringify(list));
  } else if (curUser && !list.some(u => u.id === curUser.id)) {
    list.push({ id: curUser.id, username: curUser.username, joined: new Date().toISOString().split('T')[0], isOwner: curUser.isOwner || false });
    localStorage.setItem('PIE_MC_REGISTERED_USERS', JSON.stringify(list));
  }

  let totalAccounts = 0;
  let activeBots = 0;
  let totalServers = 0;

  const usersWithStats = list.map(u => {
    let accCount = 0;
    let instCount = 1;
    let srvCount = 0;

    try {
      const raw = localStorage.getItem(`PIE_MC_DATA_${u.id}_V2`) || localStorage.getItem(`PIE_MC_DATA_${u.id}`);
      if (raw) {
        const d = JSON.parse(raw);
        accCount = Array.isArray(d.accounts) ? d.accounts.length : 0;
        instCount = Array.isArray(d.instances) ? d.instances.length : 1;
        srvCount = Array.isArray(d.servers) ? d.servers.length : 0;
        if (Array.isArray(d.instances)) {
          activeBots += d.instances.filter(i => i.status === 'online').length;
        }
      }
    } catch (e) {}

    totalAccounts += accCount;
    totalServers += srvCount;

    return {
      id: u.id,
      username: u.username,
      joined: u.joined || '2026-08-29',
      accountsCount: accCount,
      instancesCount: instCount,
      isOwner: u.isOwner || (u.id === OWNER_DISCORD_ID)
    };
  });

  return {
    totalUsersCount: usersWithStats.length,
    totalAccountsCount: totalAccounts,
    activeBotsCount: activeBots,
    totalServersCount: totalServers,
    usersList: usersWithStats
  };
};
'''

# Replace setCurrentUser logic in shared.js to call registerUserDirectory
pos_set = code.find('function setCurrentUser(user)')
if pos_set != -1:
    pos_set_end = code.find('function logout()', pos_set)
    new_set_user = '''function setCurrentUser(user) {
  if (user) {
    if (!user.authTime) user.authTime = new Date().toISOString();
    localStorage.setItem('PIE_MC_USER', JSON.stringify(user));
    if (window.registerUserDirectory) window.registerUserDirectory(user);
  } else {
    localStorage.removeItem('PIE_MC_USER');
  }
}
'''
    code = code[:pos_set] + new_set_user + '\n' + dynamic_telemetry_code + '\n' + code[pos_set_end:]

with open(os.path.join(PUB, 'shared.js'), 'w', encoding='utf-8') as f:
    f.write(code)

# 2. Update admin.html to use getDynamicTelemetry()
with open(os.path.join(PUB, 'admin.html'), 'r', encoding='utf-8') as f:
    admin_html = f.read()

pos_admin_render = admin_html.find('function renderAdminTelemetry()')
if pos_admin_render != -1:
    pos_admin_render_end = admin_html.find('function terminateUserInstances', pos_admin_render)
    new_admin_render = '''function renderAdminTelemetry() {
      const tele = (window.getDynamicTelemetry) ? window.getDynamicTelemetry() : { totalUsersCount: 1, totalAccountsCount: 0, activeBotsCount: 0, totalServersCount: 0, usersList: [] };
      document.getElementById('teleTotalUsers').innerText = tele.totalUsersCount;
      document.getElementById('teleTotalAccounts').innerText = tele.totalAccountsCount;
      document.getElementById('teleActiveBots').innerText = tele.activeBotsCount;
      document.getElementById('teleTotalServers').innerText = tele.totalServersCount;

      const tbody = document.getElementById('telemetryTableBody');
      if (!tele.usersList || tele.usersList.length === 0) {
        tbody.innerHTML = `<tr><td colspan="6" class="px-4 py-8 text-center text-slate-500 font-mono">No registered users in directory.</td></tr>`;
        return;
      }

      tbody.innerHTML = tele.usersList.map(u => `
        <tr class="hover:bg-slate-900/40 transition-colors">
          <td class="px-4 py-3 font-bold text-white flex items-center space-x-2">
            <span class="w-2 h-2 rounded-full ${u.isOwner ? 'bg-[#2cf5d6]' : 'bg-emerald-400'} pulse-dot"></span>
            <span>${u.username}</span>
            ${u.isOwner ? '<span class="badge-diamond text-[9px] px-1.5 py-0.5 ml-1">OWNER</span>' : ''}
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
'''
    admin_html = admin_html[:pos_admin_render] + new_admin_render + '\n' + admin_html[pos_admin_render_end:]

with open(os.path.join(PUB, 'admin.html'), 'w', encoding='utf-8') as f:
    f.write(admin_html)

print("Dynamic Admin Telemetry & User Registration directory updated successfully!")
