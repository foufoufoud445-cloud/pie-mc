/**
 * Pie MC - Authentication & Token Cryptography
 * Username/password auth with bcrypt hashing.
 * AES-256-GCM for Minecraft session token encryption.
 */

const crypto = require('crypto');
const bcrypt = require('bcryptjs');
const fs = require('fs');
const path = require('path');
const { getDB } = require('./database');

const KEY_PATH = path.join(__dirname, '../data/encryption.key');

// Load or generate a persistent 256-bit AES master key
function getMasterKey() {
  const dir = path.dirname(KEY_PATH);
  if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });

  if (!fs.existsSync(KEY_PATH)) {
    const key = crypto.randomBytes(32);
    fs.writeFileSync(KEY_PATH, key);
    return key;
  }
  return fs.readFileSync(KEY_PATH);
}

function encryptToken(plaintext) {
  if (!plaintext) return '';
  const key = getMasterKey();
  const iv = crypto.randomBytes(12);
  const cipher = crypto.createCipheriv('aes-256-gcm', key, iv);
  let encrypted = cipher.update(plaintext, 'utf8', 'hex');
  encrypted += cipher.final('hex');
  const tag = cipher.getAuthTag().toString('hex');
  return `${iv.toString('hex')}:${tag}:${encrypted}`;
}

function decryptToken(encryptedString) {
  if (!encryptedString) return '';
  const parts = encryptedString.split(':');
  if (parts.length !== 3) throw new Error('Invalid encrypted token payload');
  const [ivHex, tagHex, ciphertextHex] = parts;
  const key = getMasterKey();
  const iv = Buffer.from(ivHex, 'hex');
  const tag = Buffer.from(tagHex, 'hex');
  const decipher = crypto.createDecipheriv('aes-256-gcm', key, iv);
  decipher.setAuthTag(tag);
  let decrypted = decipher.update(ciphertextHex, 'hex', 'utf8');
  decrypted += decipher.final('utf8');
  return decrypted;
}

// ─── User Auth Functions ───────────────────────────────────

function hashPassword(password) {
  return bcrypt.hashSync(password, 10);
}

function verifyPassword(password, hash) {
  return bcrypt.compareSync(password, hash);
}

function createUser(username, email, password, role = 'user') {
  const db = getDB();
  const existing = db.prepare('SELECT id FROM users WHERE email = ? OR username = ?').get(email, username);
  if (existing) {
    return { success: false, error: 'Username or email already exists' };
  }
  const id = 'user_' + Date.now();
  const hash = hashPassword(password);
  db.prepare('INSERT INTO users (id, username, email, password_hash, role) VALUES (?, ?, ?, ?, ?)').run(id, username, email, hash, role);
  return { success: true, user: { id, username, email, role } };
}

function authenticateUser(email, password) {
  const db = getDB();
  const user = db.prepare('SELECT * FROM users WHERE email = ?').get(email);
  if (!user) return { success: false, error: 'Invalid email or password' };
  if (!verifyPassword(password, user.password_hash)) {
    return { success: false, error: 'Invalid email or password' };
  }
  db.prepare('UPDATE users SET last_login = CURRENT_TIMESTAMP WHERE id = ?').run(user.id);
  return {
    success: true,
    user: { id: user.id, username: user.username, email: user.email, role: user.role }
  };
}

function logLoginAction(userId, username, action, details = '', ip = '') {
  const db = getDB();
  db.prepare('INSERT INTO login_logs (user_id, username, action, details, ip_address) VALUES (?, ?, ?, ?, ?)').run(userId, username, action, details, ip);
}

function getAllUsers() {
  const db = getDB();
  return db.prepare('SELECT id, username, email, role, created_at, last_login FROM users ORDER BY created_at DESC').all();
}

function getUserById(id) {
  const db = getDB();
  return db.prepare('SELECT id, username, email, role, created_at, last_login FROM users WHERE id = ?').get(id);
}

function updateUserPassword(userId, newPassword) {
  const db = getDB();
  const hash = hashPassword(newPassword);
  db.prepare('UPDATE users SET password_hash = ? WHERE id = ?').run(hash, userId);
  return { success: true };
}

function updateUserProfile(userId, username) {
  const db = getDB();
  try {
    db.prepare('UPDATE users SET username = ? WHERE id = ?').run(username, userId);
    return { success: true };
  } catch (e) {
    return { success: false, error: 'Username already taken' };
  }
}

function deleteUser(userId) {
  const db = getDB();
  const user = db.prepare('SELECT role FROM users WHERE id = ?').get(userId);
  if (user && user.role === 'admin') return { success: false, error: 'Cannot delete admin accounts' };
  db.prepare('DELETE FROM users WHERE id = ?').run(userId);
  db.prepare('DELETE FROM accounts WHERE user_id = ?').run(userId);
  db.prepare('DELETE FROM servers WHERE user_id = ?').run(userId);
  db.prepare('DELETE FROM proxies WHERE user_id = ?').run(userId);
  db.prepare('DELETE FROM automations WHERE user_id = ?').run(userId);
  db.prepare('DELETE FROM triggers WHERE user_id = ?').run(userId);
  return { success: true };
}

function getLoginLogs(limit = 100) {
  const db = getDB();
  return db.prepare('SELECT * FROM login_logs ORDER BY created_at DESC LIMIT ?').all(limit);
}

function getUserDataSummary(userId) {
  const db = getDB();
  const accounts = db.prepare('SELECT id, username, uuid, status, created_at FROM accounts WHERE user_id = ?').all(userId);
  const servers = db.prepare('SELECT id, name, host, port, version, created_at FROM servers WHERE user_id = ?').all(userId);
  const proxies = db.prepare('SELECT id, name, type, host, port, auth, created_at FROM proxies WHERE user_id = ?').all(userId);
  const triggers = db.prepare('SELECT id, name, keyword, match_mode, reply, cooldown, scope, enabled, created_at FROM triggers WHERE user_id = ?').all(userId);
  const automations = db.prepare('SELECT id, message, interval_seconds, enabled, created_at FROM automations WHERE user_id = ?').all(userId);
  return { accounts, servers, proxies, triggers, automations };
}

function getAllUsersSummary() {
  const db = getDB();
  const users = db.prepare('SELECT id, username, email, role, created_at, last_login FROM users ORDER BY created_at DESC').all();
  return users.map(u => {
    const data = getUserDataSummary(u.id);
    return { ...u, ...data };
  });
}

module.exports = {
  encryptToken,
  decryptToken,
  getMasterKey,
  hashPassword,
  verifyPassword,
  createUser,
  authenticateUser,
  logLoginAction,
  getAllUsers,
  getUserById,
  updateUserPassword,
  updateUserProfile,
  deleteUser,
  getLoginLogs,
  getUserDataSummary,
  getAllUsersSummary
};
