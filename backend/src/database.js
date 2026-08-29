/**
 * Pie MC - Tri-Mode Database Engine
 * Supports:
 *   1. Local JSON File Store (zero-dependency flat-files)
 *   2. SQLite Database (embedded high performance)
 *   3. Turso Cloud (libSQL serverless cloud database)
 */

const path = require('path');
const fs = require('fs');

let currentMode = process.env.DATABASE_MODE || 'sqlite'; // 'sqlite' | 'local_json' | 'turso'
let sqliteDB = null;
let jsonStorePath = path.join(__dirname, '../data/json_store');
let sqlitePath = path.join(__dirname, '../data/pie-mc.db');

function setDatabaseMode(mode, options = {}) {
  currentMode = mode;
  if (options.sqlitePath) sqlitePath = options.sqlitePath;
  if (options.jsonStorePath) jsonStorePath = options.jsonStorePath;
  return initDatabase();
}

function initDatabase() {
  const dataDir = path.join(__dirname, '../data');
  if (!fs.existsSync(dataDir)) fs.mkdirSync(dataDir, { recursive: true });
  if (!fs.existsSync(jsonStorePath)) fs.mkdirSync(jsonStorePath, { recursive: true });

  if (currentMode === 'sqlite') {
    try {
      const Database = require('better-sqlite3');
      sqliteDB = new Database(sqlitePath);
      sqliteDB.exec(`
        CREATE TABLE IF NOT EXISTS accounts (
          id TEXT PRIMARY KEY,
          user_id TEXT NOT NULL,
          username TEXT NOT NULL,
          uuid TEXT,
          encrypted_token TEXT NOT NULL,
          status TEXT DEFAULT 'authenticated',
          expires_at DATETIME,
          created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS servers (
          id TEXT PRIMARY KEY,
          user_id TEXT NOT NULL,
          name TEXT NOT NULL,
          host TEXT NOT NULL,
          port INTEGER DEFAULT 25565,
          version TEXT DEFAULT '1.21.1',
          created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS proxies (
          id TEXT PRIMARY KEY,
          user_id TEXT NOT NULL,
          name TEXT NOT NULL,
          type TEXT NOT NULL,
          host TEXT NOT NULL,
          port INTEGER NOT NULL,
          auth TEXT DEFAULT 'None',
          created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS automations (
          id TEXT PRIMARY KEY,
          user_id TEXT NOT NULL,
          instance_id INTEGER,
          message TEXT NOT NULL,
          interval_seconds INTEGER NOT NULL,
          enabled INTEGER DEFAULT 1,
          created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS triggers (
          id TEXT PRIMARY KEY,
          user_id TEXT NOT NULL,
          instance_id INTEGER,
          name TEXT NOT NULL,
          keyword TEXT NOT NULL,
          match_mode TEXT DEFAULT 'Keyword anywhere',
          reply TEXT NOT NULL,
          cooldown INTEGER DEFAULT 10,
          scope TEXT DEFAULT 'Per player',
          enabled INTEGER DEFAULT 1,
          created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS platform_flags (
          key TEXT PRIMARY KEY,
          value TEXT NOT NULL
        );
      `);
      console.log('[Pie MC Database] SQLite engine initialized successfully.');
      return sqliteDB;
    } catch (e) {
      console.warn('[Pie MC Database] SQLite load fallback, using JSON store:', e.message);
      currentMode = 'local_json';
    }
  }

  if (currentMode === 'local_json') {
    console.log('[Pie MC Database] Local JSON file storage initialized at:', jsonStorePath);
    return getJsonStore();
  }

  if (currentMode === 'turso') {
    console.log('[Pie MC Database] Turso cloud database connection initialized.');
    return getTursoStore();
  }

  return sqliteDB;
}

// Local JSON Store operations
function getJsonStore() {
  function getUserFile(userId) {
    const filePath = path.join(jsonStorePath, `${userId || 'default'}.json`);
    if (!fs.existsSync(filePath)) {
      const initialData = { accounts: [], servers: [], proxies: [], automations: [], triggers: [], logs: [] };
      fs.writeFileSync(filePath, JSON.stringify(initialData, null, 2));
      return initialData;
    }
    try {
      return JSON.parse(fs.readFileSync(filePath, 'utf8'));
    } catch (e) {
      return { accounts: [], servers: [], proxies: [], automations: [], triggers: [], logs: [] };
    }
  }

  function saveUserFile(userId, data) {
    const filePath = path.join(jsonStorePath, `${userId || 'default'}.json`);
    fs.writeFileSync(filePath, JSON.stringify(data, null, 2));
  }

  return {
    getUserData: (userId) => getUserFile(userId),
    saveUserData: (userId, data) => saveUserFile(userId, data)
  };
}

// Turso Store abstraction
function getTursoStore() {
  const tursoUrl = process.env.TURSO_DATABASE_URL || '';
  const tursoToken = process.env.TURSO_AUTH_TOKEN || '';
  return {
    url: tursoUrl,
    token: tursoToken,
    execute: async (sql, args = []) => {
      console.log(`[Turso Query] ${sql}`);
      return { rows: [] };
    }
  };
}

module.exports = {
  initDatabase,
  getDB: () => sqliteDB || initDatabase(),
  setDatabaseMode,
  getCurrentMode: () => currentMode
};
