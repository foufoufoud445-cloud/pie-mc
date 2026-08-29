/**
 * Pie MC - Backend API & WebSocket Server
 * Username/password authentication, admin panel, multi-tenant bot management.
 */

const express = require('express');
const http = require('http');
const path = require('path');
const cors = require('cors');
const WebSocket = require('ws');
require('dotenv').config();

const { initDatabase, getDB } = require('./src/database');
const {
  encryptToken, decryptToken,
  authenticateUser, createUser,
  logLoginAction, getAllUsers, getUserById,
  updateUserPassword, updateUserProfile,
  deleteUser, getLoginLogs, getAllUsersSummary
} = require('./src/auth');
const botManager = require('./src/botManager');

const app = express();
const server = http.createServer(app);
const wss = new WebSocket.Server({ server });

const PORT = process.env.PORT || 8082;

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.static(path.join(__dirname, '../public')));

// ─── Auth Middleware ───────────────────────────────────────
function requireAuth(req, res, next) {
  const userId = req.headers['x-user-id'];
  if (!userId) return res.status(401).json({ success: false, error: 'Not authenticated' });
  const user = getUserById(userId);
  if (!user) return res.status(401).json({ success: false, error: 'User not found' });
  req.user = user;
  next();
}

function requireAdmin(req, res, next) {
  if (!req.user || req.user.role !== 'admin') {
    return res.status(403).json({ success: false, error: 'Admin access required' });
  }
  next();
}

// ─── Helpers ───────────────────────────────────────────────
function formatUUID(raw) {
  if (!raw || raw.includes('-')) return raw;
  return raw.replace(/^(.{8})(.{4})(.{4})(.{4})(.{12})$/, '$1-$2-$3-$4-$5');
}

function sanitizeToken(token) {
  if (!token) return '';
  let clean = token.trim();
  if (clean.startsWith('{') && clean.endsWith('}')) {
    try {
      const parsed = JSON.parse(clean);
      clean = parsed.accessToken || parsed.bearer_token || parsed.token || parsed.ssid || clean;
    } catch (e) {}
  }
  if (clean.toLowerCase().startsWith('bearer ')) {
    clean = clean.slice(7).trim();
  }
  return clean.replace(/^["']|["']$/g, '').trim();
}

// ─── AUTH ROUTES ───────────────────────────────────────────

// Login
app.post('/api/auth/login', (req, res) => {
  const { email, password } = req.body;
  if (!email || !password) {
    return res.status(400).json({ success: false, error: 'Email and password are required' });
  }
  const result = authenticateUser(email, password);
  if (result.success) {
    logLoginAction(result.user.id, result.user.username, 'login', `Logged in via email`, req.ip);
    console.log(`[Auth] ${result.user.username} (${result.user.role}) logged in`);
  }
  res.json(result);
});

// Register - Admin only
app.post('/api/auth/register', requireAuth, requireAdmin, (req, res) => {
  const { username, email, password, role } = req.body;
  if (!username || !email || !password) {
    return res.status(400).json({ success: false, error: 'Username, email, and password are required' });
  }
  const finalRole = (role === 'admin' && req.user.role === 'admin') ? 'admin' : 'user';

  const result = createUser(username, email, password, finalRole);
  if (result.success) {
    logLoginAction(result.user.id, result.user.username, 'account_created', `Created by admin ${req.user.username}`, req.ip);
  }
  res.json(result);
});

// Get current user profile
app.get('/api/auth/me', requireAuth, (req, res) => {
  res.json({ success: true, user: req.user });
});

// Change password (any user)
app.post('/api/auth/change-password', requireAuth, (req, res) => {
  const { currentPassword, newPassword } = req.body;
  if (!currentPassword || !newPassword) {
    return res.status(400).json({ success: false, error: 'Current and new password are required' });
  }
  const { verifyPassword } = require('./src/auth');
  const db = getDB();
  const fullUser = db.prepare('SELECT password_hash FROM users WHERE id = ?').get(req.user.id);
  if (!verifyPassword(currentPassword, fullUser.password_hash)) {
    return res.status(401).json({ success: false, error: 'Current password is incorrect' });
  }
  updateUserPassword(req.user.id, newPassword);
  logLoginAction(req.user.id, req.user.username, 'password_changed', 'Changed own password', req.ip);
  res.json({ success: true, message: 'Password updated' });
});

// ─── ADMIN ROUTES ──────────────────────────────────────────

// Admin: list all users
app.get('/api/admin/users', requireAuth, requireAdmin, (req, res) => {
  const users = getAllUsers();
  res.json({ success: true, users });
});

// Admin: get full user data (accounts, servers, proxies, etc.)
app.get('/api/admin/users/:id/data', requireAuth, requireAdmin, (req, res) => {
  const summary = getAllUsersSummary().find(u => u.id === req.params.id);
  if (!summary) return res.status(404).json({ success: false, error: 'User not found' });
  res.json({ success: true, data: summary });
});

// Admin: get all users with full data
app.get('/api/admin/users-all', requireAuth, requireAdmin, (req, res) => {
  const all = getAllUsersSummary();
  res.json({ success: true, users: all });
});

// Admin: create user
app.post('/api/admin/users', requireAuth, requireAdmin, (req, res) => {
  const { username, email, password, role } = req.body;
  if (!username || !email || !password) {
    return res.status(400).json({ success: false, error: 'Username, email, and password required' });
  }
  const result = createUser(username, email, password, role === 'admin' ? 'admin' : 'user');
  if (result.success) {
    logLoginAction(result.user.id, result.user.username, 'account_created', `Created by admin ${req.user.username}`, req.ip);
  }
  res.json(result);
});

// Admin: update user profile (username)
app.put('/api/admin/users/:id', requireAuth, requireAdmin, (req, res) => {
  const { username } = req.body;
  if (username) {
    const result = updateUserProfile(req.params.id, username);
    return res.json(result);
  }
  res.status(400).json({ success: false, error: 'Username required' });
});

// Admin: reset user password
app.post('/api/admin/users/:id/reset-password', requireAuth, requireAdmin, (req, res) => {
  const { newPassword } = req.body;
  if (!newPassword) return res.status(400).json({ success: false, error: 'New password required' });
  updateUserPassword(req.params.id, newPassword);
  const user = getUserById(req.params.id);
  logLoginAction(req.user.id, req.user.username, 'admin_reset_password', `Reset password for ${user ? user.username : req.params.id}`, req.ip);
  res.json({ success: true, message: 'Password reset' });
});

// Admin: delete user
app.delete('/api/admin/users/:id', requireAuth, requireAdmin, (req, res) => {
  const result = deleteUser(req.params.id);
  if (result.success) {
    logLoginAction(req.user.id, req.user.username, 'admin_delete_user', `Deleted user ${req.params.id}`, req.ip);
  }
  res.json(result);
});

// Admin: activity logs
app.get('/api/admin/logs', requireAuth, requireAdmin, (req, res) => {
  const limit = parseInt(req.query.limit) || 100;
  const logs = getLoginLogs(limit);
  res.json({ success: true, logs });
});

// Admin: metrics
app.get('/api/admin/metrics', requireAuth, requireAdmin, (req, res) => {
  const db = getDB();
  const totalUsers = db.prepare('SELECT COUNT(*) as count FROM users').get().count;
  const totalAccounts = db.prepare('SELECT COUNT(*) as count FROM accounts').get().count;
  const totalServers = db.prepare('SELECT COUNT(*) as count FROM servers').get().count;
  const totalProxies = db.prepare('SELECT COUNT(*) as count FROM proxies').get().count;
  res.json({
    success: true,
    metrics: { totalUsers, totalAccounts, totalServers, totalProxies }
  });
});

// ─── USER ROUTES (self-service) ────────────────────────────

// User: change own password
app.post('/api/user/change-password', requireAuth, (req, res) => {
  const { currentPassword, newPassword } = req.body;
  if (!currentPassword || !newPassword) {
    return res.status(400).json({ success: false, error: 'Current and new password required' });
  }
  const { verifyPassword } = require('./src/auth');
  const db = getDB();
  const fullUser = db.prepare('SELECT password_hash FROM users WHERE id = ?').get(req.user.id);
  if (!verifyPassword(currentPassword, fullUser.password_hash)) {
    return res.status(401).json({ success: false, error: 'Current password is incorrect' });
  }
  updateUserPassword(req.user.id, newPassword);
  logLoginAction(req.user.id, req.user.username, 'password_changed', 'Changed own password', req.ip);
  res.json({ success: true, message: 'Password updated' });
});

// ─── MOJANG TOKEN VERIFICATION ─────────────────────────────

app.post('/api/accounts/lookup-ssid', async (req, res) => {
  let { sessionToken } = req.body;
  if (!sessionToken) {
    return res.status(400).json({ success: false, error: 'Bearer / SSID Token is required' });
  }

  const cleanToken = sanitizeToken(sessionToken);

  try {
    const mojangRes = await fetch('https://api.minecraftservices.com/minecraft/profile', {
      headers: {
        'Authorization': `Bearer ${cleanToken}`,
        'User-Agent': 'PieMC/2.4'
      }
    });

    if (mojangRes.status === 401) {
      return res.status(401).json({
        success: false,
        error: 'Invalid or expired Bearer token. Mojang rejected authentication (401 Unauthorized).'
      });
    }

    if (!mojangRes.ok) {
      const errBody = await mojangRes.text();
      return res.status(mojangRes.status).json({
        success: false,
        error: `Mojang API error (${mojangRes.status}): ${errBody}`
      });
    }

    const profileData = await mojangRes.json();
    const formattedUUID = formatUUID(profileData.id);
    const activeSkin = profileData.skins && profileData.skins.length > 0
      ? (profileData.skins.find(s => s.state === 'ACTIVE') || profileData.skins[0]).url
      : null;

    console.log(`[Mojang Verified] Player: ${profileData.name} (UUID: ${formattedUUID})`);

    return res.json({
      success: true,
      profile: {
        username: profileData.name,
        uuid: formattedUUID,
        rawId: profileData.id,
        skinUrl: activeSkin,
        avatar: `https://mc-heads.net/avatar/${profileData.name}/28`,
        expiresAt: new Date(Date.now() + 24 * 3600 * 1000).toISOString(),
        tokenExpiryStatus: 'valid'
      }
    });
  } catch (err) {
    console.error('[Mojang API Fetch Error]', err.message);
    return res.status(500).json({
      success: false,
      error: `Failed to contact Mojang verification service: ${err.message}`
    });
  }
});

// ─── ACCOUNTS CRUD (user-scoped) ───────────────────────────

app.get('/api/accounts', requireAuth, (req, res) => {
  const userId = req.user.id;
  const db = getDB();
  const accounts = db.prepare('SELECT id, username, uuid, status, created_at FROM accounts WHERE user_id = ?').all(userId);
  res.json({ success: true, data: accounts });
});

app.post('/api/accounts/link', requireAuth, (req, res) => {
  const userId = req.user.id;
  const { sessionToken, username, uuid } = req.body;

  if (!sessionToken) {
    return res.status(400).json({ success: false, error: 'Session Token (SSID / Bearer) is required' });
  }

  const id = String(Date.now());
  const finalUsername = username || 'PieBot_' + id.slice(-4);
  const finalUUID = uuid || 'd' + Math.random().toString(16).substring(2, 10) + '-4a11-98bc';
  const encrypted = encryptToken(sessionToken);

  const db = getDB();
  db.prepare(`
    INSERT INTO accounts (id, user_id, username, uuid, encrypted_token, status)
    VALUES (?, ?, ?, ?, ?, 'authenticated')
  `).run(id, userId, finalUsername, finalUUID, encrypted);

  logLoginAction(userId, req.user.username, 'account_linked', `Linked MC account: ${finalUsername}`, req.ip);
  res.json({ success: true, account: { id, username: finalUsername, uuid: finalUUID, status: 'authenticated' } });
});

app.post('/api/accounts/:id/reauth', requireAuth, (req, res) => {
  const userId = req.user.id;
  const { sessionToken } = req.body;

  if (!sessionToken) {
    return res.status(400).json({ success: false, error: 'Fresh Bearer / SSID is required' });
  }

  const encrypted = encryptToken(sessionToken);
  const db = getDB();
  db.prepare(`
    UPDATE accounts SET encrypted_token = ?, status = 'authenticated' WHERE id = ? AND user_id = ?
  `).run(encrypted, req.params.id, userId);

  res.json({ success: true, message: 'Account session token refreshed' });
});

app.delete('/api/accounts/:id', requireAuth, (req, res) => {
  const userId = req.user.id;
  const db = getDB();
  db.prepare('DELETE FROM accounts WHERE id = ? AND user_id = ?').run(req.params.id, userId);
  res.json({ success: true });
});

// ─── SERVERS CRUD ──────────────────────────────────────────

app.get('/api/servers', requireAuth, (req, res) => {
  const db = getDB();
  const servers = db.prepare('SELECT * FROM servers WHERE user_id = ?').all(req.user.id);
  res.json({ success: true, data: servers });
});

app.post('/api/servers', requireAuth, (req, res) => {
  const { name, host, port, version } = req.body;
  if (!name || !host) return res.status(400).json({ success: false, error: 'Name and host required' });
  const id = String(Date.now());
  const db = getDB();
  db.prepare('INSERT INTO servers (id, user_id, name, host, port, version) VALUES (?, ?, ?, ?, ?, ?)').run(id, req.user.id, name, host, port || 25565, version || '1.21.1');
  res.json({ success: true, server: { id, name, host, port: port || 25565, version: version || '1.21.1' } });
});

app.put('/api/servers/:id', requireAuth, (req, res) => {
  const { name, host, port, version } = req.body;
  const db = getDB();
  db.prepare('UPDATE servers SET name = ?, host = ?, port = ?, version = ? WHERE id = ? AND user_id = ?').run(name, host, port, version, req.params.id, req.user.id);
  res.json({ success: true });
});

app.delete('/api/servers/:id', requireAuth, (req, res) => {
  const db = getDB();
  db.prepare('DELETE FROM servers WHERE id = ? AND user_id = ?').run(req.params.id, req.user.id);
  res.json({ success: true });
});

// ─── PROXIES CRUD ──────────────────────────────────────────

app.get('/api/proxies', requireAuth, (req, res) => {
  const db = getDB();
  const proxies = db.prepare('SELECT * FROM proxies WHERE user_id = ?').all(req.user.id);
  res.json({ success: true, data: proxies });
});

app.post('/api/proxies', requireAuth, (req, res) => {
  const { name, type, host, port, auth } = req.body;
  if (!name || !type || !host || !port) return res.status(400).json({ success: false, error: 'All fields required' });
  const id = String(Date.now());
  const db = getDB();
  db.prepare('INSERT INTO proxies (id, user_id, name, type, host, port, auth) VALUES (?, ?, ?, ?, ?, ?, ?)').run(id, req.user.id, name, type, host, port, auth || 'None');
  res.json({ success: true, proxy: { id, name, type, host, port, auth: auth || 'None' } });
});

app.put('/api/proxies/:id', requireAuth, (req, res) => {
  const { name, type, host, port, auth } = req.body;
  const db = getDB();
  db.prepare('UPDATE proxies SET name = ?, type = ?, host = ?, port = ?, auth = ? WHERE id = ? AND user_id = ?').run(name, type, host, port, auth, req.params.id, req.user.id);
  res.json({ success: true });
});

app.delete('/api/proxies/:id', requireAuth, (req, res) => {
  const db = getDB();
  db.prepare('DELETE FROM proxies WHERE id = ? AND user_id = ?').run(req.params.id, req.user.id);
  res.json({ success: true });
});

// ─── WEBSOCKET REAL-TIME GATEWAY ───────────────────────────

wss.on('connection', (ws) => {
  ws.send(JSON.stringify({ type: 'welcome', message: 'Connected to Pie MC Realtime Gateway' }));

  ws.on('message', (data) => {
    try {
      const payload = JSON.parse(data);

      if (payload.type === 'start_bot') {
        const inst = botManager.getOrCreateInstance(
          payload.userId || 'default',
          payload.instanceId,
          payload.config || {}
        );
        inst.start();
      } else if (payload.type === 'stop_bot') {
        const inst = botManager.getOrCreateInstance(
          payload.userId || 'default',
          payload.instanceId,
          {}
        );
        inst.stop();
      } else if (payload.type === 'chat') {
        const inst = botManager.getOrCreateInstance(
          payload.userId || 'default',
          payload.instanceId,
          {}
        );
        inst.sendChat(payload.message);
      }
    } catch (e) {}
  });
});

// ─── START SERVER ──────────────────────────────────────────

initDatabase();

server.listen(PORT, '0.0.0.0', () => {
  console.log(`\n======================================================`);
  console.log(`Pie MC Server listening on http://localhost:${PORT}`);
  console.log(`   - Auth: Username/Password (bcrypt)`);
  console.log(`   - Admin: admin@autopie.site`);
  console.log(`   - Token Cryptography: AES-256-GCM`);
  console.log(`======================================================\n`);
});
