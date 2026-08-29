/**
 * Pie MC - Database Engine
 * Turso (cloud primary) + SQLite (local cache for sync reads) + JSON fallback.
 * All API code uses sync reads from SQLite cache. Writes go to both.
 */

const path = require('path');
const fs = require('fs');

let currentMode = process.env.DATABASE_MODE || 'turso';
let sqliteDB = null;
let tursoClient = null;
let jsonStorePath = path.join(__dirname, '../data/json_store');
let sqlitePath = process.env.SQLITE_PATH || path.join(__dirname, '../data/pie-mc.db');

const TURSO_URL = process.env.TURSO_DATABASE_URL || 'libsql://dorcake-rtfgyeuijdsoe.aws-ap-south-1.turso.io';
const TURSO_TOKEN = process.env.TURSO_AUTH_TOKEN || 'eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJhIjoicnciLCJpYXQiOjE3ODgwMjE3MTcsImlkIjoiMDFhMDRlNjYtMjEwMS03MWE5LWE0NGUtOGNjMjZkZjA1ZWJkIiwia2lkIjoiVFA5YktYaGF4VXBVVHFQeUVfQUwyeUJzT2NaZ3YyWmVNUko4MzNEOFk2dyIsInJpZCI6IjU3OTVlOTQwLWY3MGYtNDQ2Ni1hMmNhLWZiMDBlM2IwNDEzNCJ9.3FpDBSIb9TvumQ-YSg1WvfLJl6o_kmAnoCovjTrZ1IgCxURWtPkxtJX-o7mlE1qm_diwsf3ZlvzLZleQGMQNBQ';

const SCHEMA = [
  `CREATE TABLE IF NOT EXISTS users (id TEXT PRIMARY KEY, username TEXT UNIQUE NOT NULL, email TEXT UNIQUE NOT NULL, password_hash TEXT NOT NULL, role TEXT DEFAULT 'user', created_at DATETIME DEFAULT CURRENT_TIMESTAMP, last_login DATETIME)`,
  `CREATE TABLE IF NOT EXISTS login_logs (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id TEXT NOT NULL, username TEXT NOT NULL, action TEXT NOT NULL, details TEXT DEFAULT '', ip_address TEXT DEFAULT '', created_at DATETIME DEFAULT CURRENT_TIMESTAMP)`,
  `CREATE TABLE IF NOT EXISTS accounts (id TEXT PRIMARY KEY, user_id TEXT NOT NULL, username TEXT NOT NULL, uuid TEXT, encrypted_token TEXT NOT NULL, status TEXT DEFAULT 'authenticated', expires_at DATETIME, created_at DATETIME DEFAULT CURRENT_TIMESTAMP)`,
  `CREATE TABLE IF NOT EXISTS servers (id TEXT PRIMARY KEY, user_id TEXT NOT NULL, name TEXT NOT NULL, host TEXT NOT NULL, port INTEGER DEFAULT 25565, version TEXT DEFAULT '1.21.1', created_at DATETIME DEFAULT CURRENT_TIMESTAMP)`,
  `CREATE TABLE IF NOT EXISTS proxies (id TEXT PRIMARY KEY, user_id TEXT NOT NULL, name TEXT NOT NULL, type TEXT NOT NULL, host TEXT NOT NULL, port INTEGER NOT NULL, auth TEXT DEFAULT 'None', created_at DATETIME DEFAULT CURRENT_TIMESTAMP)`,
  `CREATE TABLE IF NOT EXISTS automations (id TEXT PRIMARY KEY, user_id TEXT NOT NULL, instance_id INTEGER, message TEXT NOT NULL, interval_seconds INTEGER NOT NULL, enabled INTEGER DEFAULT 1, created_at DATETIME DEFAULT CURRENT_TIMESTAMP)`,
  `CREATE TABLE IF NOT EXISTS triggers (id TEXT PRIMARY KEY, user_id TEXT NOT NULL, instance_id INTEGER, name TEXT NOT NULL, keyword TEXT NOT NULL, match_mode TEXT DEFAULT 'Keyword anywhere', reply TEXT NOT NULL, cooldown INTEGER DEFAULT 10, scope TEXT DEFAULT 'Per player', enabled INTEGER DEFAULT 1, created_at DATETIME DEFAULT CURRENT_TIMESTAMP)`,
  `CREATE TABLE IF NOT EXISTS platform_flags (key TEXT PRIMARY KEY, value TEXT NOT NULL)`
];

function setDatabaseMode(mode, options = {}) {
  currentMode = mode;
  if (options.sqlitePath) sqlitePath = options.sqlitePath;
  if (options.jsonStorePath) jsonStorePath = options.jsonStorePath;
  return initDatabase();
}

// ─── Turso Sync Wrapper ────────────────────────────────────
// Uses Turso's HTTP API via @libsql/client but wraps in sync-compatible interface
// by caching all reads in memory and writing through to Turso async
function createTursoWrapper(client) {
  const cache = new Map(); // sql+args -> result

  async function execAsync(sql, args = []) {
    try {
      const result = await client.execute({ sql, args });
      const key = sql + JSON.stringify(args);
      cache.set(key, { rows: result.rows, rowsAffected: result.rowsAffected || 0 });
      return { ok: true, rows: result.rows, rowsAffected: result.rowsAffected || 0 };
    } catch (e) {
      console.error('[Turso]', e.message);
      return { ok: false, error: e.message, rows: [], rowsAffected: 0 };
    }
  }

  // Pre-warm cache with all tables on startup
  async function warmCache() {
    for (const table of ['users', 'login_logs', 'accounts', 'servers', 'proxies', 'automations', 'triggers', 'platform_flags']) {
      await execAsync(`SELECT * FROM ${table}`);
    }
    console.log('[Pie MC Database] Turso cache warmed.');
  }

  return {
    _client: client,
    _warmCache: warmCache,

    prepare(sql) {
      return {
        get(...args) {
          const key = sql + JSON.stringify(args);
          // Try cache first
          if (cache.has(key)) {
            const c = cache.get(key);
            return c.rows[0] || null;
          }
          // Fire async fetch, return null for now (will be available next call)
          execAsync(sql, args);
          return null;
        },
        all(...args) {
          const key = sql + JSON.stringify(args);
          if (cache.has(key)) {
            return cache.get(key).rows || [];
          }
          execAsync(sql, args);
          return [];
        },
        run(...args) {
          // Write-through: execute on Turso async, invalidate cache
          const key = sql + JSON.stringify(args);
          execAsync(sql, args).then(() => {
            // Invalidate related cache entries
            for (const [k] of cache) {
              if (k.includes(sql.split(' ')[2] || '')) cache.delete(k); // invalidate table cache
            }
          });
          return { changes: 1 }; // optimistic
        }
      };
    },
    exec(sql) {
      const statements = sql.split(';').filter(s => s.trim());
      for (const stmt of statements) {
        if (stmt.trim()) execAsync(stmt.trim());
      }
    },
    pragma() {}
  };
}

// ─── Init ──────────────────────────────────────────────────
async function initDatabase() {
  const dataDir = path.join(__dirname, '../data');
  if (!fs.existsSync(dataDir)) fs.mkdirSync(dataDir, { recursive: true });
  if (!fs.existsSync(jsonStorePath)) fs.mkdirSync(jsonStorePath, { recursive: true });

  // Turso (default for production)
  if (currentMode === 'turso' && TURSO_URL && TURSO_TOKEN) {
    try {
      const { createClient } = require('@libsql/client');
      const client = createClient({ url: TURSO_URL, authToken: TURSO_TOKEN });
      await client.execute('SELECT 1 as test');
      tursoClient = client;
      console.log('[Pie MC Database] Turso cloud connected.');

      // Create tables
      for (const stmt of SCHEMA) {
        await client.execute(stmt);
      }

      // Seed admin
      const bcrypt = require('bcryptjs');
      const adminCheck = await client.execute({ sql: 'SELECT id FROM users WHERE email = ?', args: ['admin@autopie.site'] });
      if (adminCheck.rows.length === 0) {
        const adminHash = bcrypt.hashSync('autopie@#@%2143', 10);
        await client.execute({
          sql: 'INSERT INTO users (id, username, email, password_hash, role) VALUES (?, ?, ?, ?, ?)',
          args: ['admin_001', 'admin', 'admin@autopie.site', adminHash, 'admin']
        });
        console.log('[Pie MC Database] Admin seeded: admin@autopie.site');
      }

      sqliteDB = createTursoWrapper(client);
      // Warm cache in background
      sqliteDB._warmCache().catch(e => console.warn('[Cache warm error]', e.message));
      return sqliteDB;
    } catch (e) {
      console.warn('[Pie MC Database] Turso failed, falling back to SQLite:', e.message);
      currentMode = 'sqlite';
    }
  }

  // SQLite (local fallback)
  if (currentMode === 'sqlite') {
    try {
      const Database = require('better-sqlite3');
      sqliteDB = new Database(sqlitePath);
      sqliteDB.pragma('journal_mode = WAL');
      sqliteDB.exec(SCHEMA.join(';\n'));

      const bcrypt = require('bcryptjs');
      const existingAdmin = sqliteDB.prepare('SELECT id FROM users WHERE email = ?').get('admin@autopie.site');
      if (!existingAdmin) {
        const adminHash = bcrypt.hashSync('autopie@#@%2143', 10);
        sqliteDB.prepare('INSERT INTO users (id, username, email, password_hash, role) VALUES (?, ?, ?, ?, ?)').run('admin_001', 'admin', 'admin@autopie.site', adminHash, 'admin');
        console.log('[Pie MC Database] Admin seeded: admin@autopie.site');
      }
      console.log('[Pie MC Database] SQLite initialized.');
      return sqliteDB;
    } catch (e) {
      console.warn('[Pie MC Database] SQLite failed, using JSON:', e.message);
      currentMode = 'local_json';
    }
  }

  // JSON fallback
  console.log('[Pie MC Database] JSON storage at:', jsonStorePath);
  return getJsonStore();
}

function getJsonStore() {
  function getUserFile(userId) {
    const fp = path.join(jsonStorePath, `${userId || 'default'}.json`);
    if (!fs.existsSync(fp)) {
      const d = { accounts: [], servers: [], proxies: [], automations: [], triggers: [], logs: [] };
      fs.writeFileSync(fp, JSON.stringify(d, null, 2));
      return d;
    }
    try { return JSON.parse(fs.readFileSync(fp, 'utf8')); }
    catch (e) { return { accounts: [], servers: [], proxies: [], automations: [], triggers: [], logs: [] }; }
  }
  function saveUserFile(userId, data) {
    fs.writeFileSync(path.join(jsonStorePath, `${userId || 'default'}.json`), JSON.stringify(data, null, 2));
  }
  return { getUserData: (userId) => getUserFile(userId), saveUserData: (userId, data) => saveUserFile(userId, data) };
}

module.exports = { initDatabase, getDB: () => sqliteDB, getTurso: () => tursoClient, setDatabaseMode, getCurrentMode: () => currentMode };
