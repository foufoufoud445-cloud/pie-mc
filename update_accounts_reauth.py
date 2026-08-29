import os

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
          <p class="text-xs text-slate-400 mt-1 font-mono">Auto-detected via Microsoft OAuth Session Token (SSID)</p>
        </div>
        <button onclick="openModal('linkAccModal')" class="btn-primary">
          <svg class="w-4 h-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19"></line><line x1="5" y1="12" x2="19" y2="12"></line></svg>
          <span>Link Account by SSID</span>
        </button>
      </div>

      <!-- Security & Token Expiry Notice Banner -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div class="p-4 rounded-xl bg-[#0a0d14] border border-emerald-500/20 text-xs text-slate-300 flex items-start space-x-3">
          <span class="text-emerald-400 mt-0.5">
            <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
          </span>
          <div>
            <strong class="text-emerald-400 font-bold">Hardware-Level Vault Encryption:</strong>
            <span>All tokens are stored locally encrypted with <strong>AES-256-GCM</strong>. Tokens never leave your workspace.</span>
          </div>
        </div>

        <div class="p-4 rounded-xl bg-[#0a0d14] border border-amber-500/25 text-xs text-slate-300 flex items-start space-x-3">
          <span class="text-amber-400 mt-0.5">
            <svg class="w-5 h-5" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="8" x2="12" y2="12"></line><line x1="12" y1="16" x2="12.01" y2="16"></line></svg>
          </span>
          <div>
            <strong class="text-amber-400 font-bold">Session Expiry Monitor:</strong>
            <span>Microsoft SSIDs naturally expire. Accounts showing <span class="text-amber-400 font-semibold font-mono">NEEDS RE-AUTH</span> can be instantly updated via the <strong>Re-Auth</strong> button.</span>
          </div>
        </div>
      </div>

      <!-- Accounts Table -->
      <div class="overflow-x-auto rounded-xl border border-[#1c2333]">
        <table class="w-full text-left text-sm text-slate-300">
          <thead class="bg-[#0c1018] text-xs uppercase font-mono text-slate-400 border-b border-[#1c2333]">
            <tr>
              <th class="px-4 py-3">Avatar</th>
              <th class="px-4 py-3">Username (Auto-Detected)</th>
              <th class="px-4 py-3">Entity UUID</th>
              <th class="px-4 py-3">Session Status</th>
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

  <!-- Modal 1: Link Account Modal (SSID-Only Auto-Detection) -->
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
          <label class="block font-semibold text-slate-300 mb-1">Session Token / SSID</label>
          <textarea id="modalAccToken" rows="5" placeholder="Paste your raw Microsoft / Minecraft OAuth session token (SSID) here..." class="pie-input w-full font-mono text-cyan-300 text-xs"></textarea>
          <p class="text-[11px] text-slate-500 mt-1 font-mono">&bull; Pie MC will automatically query and detect your Player Name, Entity UUID, and Avatar Skin.</p>
        </div>

        <div id="detectStatus" class="hidden p-3 rounded-lg bg-[#0a0d14] border border-[#2cf5d6]/30 text-slate-300 text-xs items-center space-x-2">
          <span class="w-2 h-2 rounded-full bg-[#2cf5d6] pulse-dot"></span>
          <span id="detectText">Resolving Mojang entity profile...</span>
        </div>
      </div>

      <div class="flex items-center justify-end space-x-3 pt-2">
        <button onclick="closeModal('linkAccModal')" class="btn-secondary text-xs">Cancel</button>
        <button id="btnLinkSubmit" onclick="submitAccount()" class="btn-primary text-xs">
          <span>Auto-Detect & Link Account</span>
        </button>
      </div>
    </div>
  </div>

  <!-- Modal 2: Re-Authenticate Account Modal -->
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
            <span class="text-amber-400 font-mono text-[11px]">Session Expired &bull; Replace SSID to reconnect</span>
          </div>
        </div>

        <div>
          <label class="block font-semibold text-slate-300 mb-1">New Microsoft Session Token / SSID</label>
          <textarea id="reauthSSIDInput" rows="4" placeholder="Paste your fresh Microsoft OAuth session token here..." class="pie-input w-full font-mono text-cyan-300 text-xs"></textarea>
        </div>
      </div>

      <div class="flex items-center justify-end space-x-3 pt-2">
        <button onclick="closeModal('reauthModal')" class="btn-secondary text-xs">Cancel</button>
        <button id="btnReauthSubmit" onclick="submitReauth()" class="btn-primary text-xs bg-amber-500 hover:bg-amber-400 text-black font-bold">
          <span>Update Token & Re-Authenticate</span>
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
      tbody.innerHTML = state.accounts.map(a => {
        let badgeHtml = `<span class="badge-online">AUTHENTICATED</span>`;
        if (a.status === 'needs_reauth' || a.tokenExpiryStatus === 'needs_reauth') {
          badgeHtml = `<span class="px-2 py-0.5 rounded text-[10px] font-mono font-bold bg-amber-500/15 text-amber-400 border border-amber-500/30 flex items-center space-x-1 inline-flex"><span class="w-1.5 h-1.5 rounded-full bg-amber-400 pulse-dot"></span><span>NEEDS RE-AUTH</span></span>`;
        } else if (a.status === 'expired') {
          badgeHtml = `<span class="badge-offline">TOKEN EXPIRED</span>`;
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
              <button onclick="openReauthModal('${a.id}', '${a.username}')" class="btn-secondary text-xs px-2.5 py-1 text-amber-400 hover:text-amber-300 border-amber-500/30 hover:border-amber-500/60" title="Update Session Token">
                <svg class="w-3.5 h-3.5 inline" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 2l-2 2m-1.5 1.5L14 9l-3-3 2-2m-4.5 4.5L3 14v4h4l5.5-5.5"></path></svg>
                <span>Re-Auth</span>
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
        alert('Please paste a session token (SSID)');
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
        });

        closeModal('linkAccModal');
        document.getElementById('modalAccToken').value = '';
        renderAccountsTable();
      } catch (err) {
        alert(err.message);
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
        alert('Please paste a fresh session token');
        return;
      }

      try {
        await window.reauthAccountSSID(currentReauthTargetId, newToken);
        closeModal('reauthModal');
        renderAccountsTable();
        alert('Account token successfully refreshed!');
      } catch (err) {
        alert(err.message);
      }
    }

    function removeAccountPrompt(id, username) {
      window.showConfirmModal({
        title: `Remove Account ${username}?`,
        message: `Are you sure you want to remove <strong>${username}</strong> from your linked account vault?`,
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

with open('/working_dir/c_37017e0a3b8a7bd1/pie-mc/public/accounts.html', 'w', encoding='utf-8') as f:
    f.write(accounts_html)
print("Updated accounts.html with Session Expiry Alerts and Quick Re-Auth Modal!")
