/**
 * Pie MC - Authentication & Token Cryptography (AES-256-GCM)
 * Securely encrypts and decrypts Microsoft session tokens (SSID) at rest.
 */

const crypto = require('crypto');
const fs = require('fs');
const path = require('path');

const KEY_PATH = path.join(__dirname, '../data/encryption.key');

// Load or generate a persistent 256-bit AES master key
function getMasterKey() {
  const dir = path.dirname(KEY_PATH);
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
  }

  if (!fs.existsSync(KEY_PATH)) {
    const key = crypto.randomBytes(32);
    fs.writeFileSync(KEY_PATH, key);
    return key;
  }

  return fs.readFileSync(KEY_PATH);
}

/**
 * Encrypt a plaintext session token / SSID using AES-256-GCM
 * @param {string} plaintext - The raw session token
 * @returns {string} - Encrypted string format: iv:authTag:ciphertext (hex encoded)
 */
function encryptToken(plaintext) {
  if (!plaintext) return '';
  const key = getMasterKey();
  const iv = crypto.randomBytes(12); // 96-bit IV recommended for GCM
  const cipher = crypto.createCipheriv('aes-256-gcm', key, iv);

  let encrypted = cipher.update(plaintext, 'utf8', 'hex');
  encrypted += cipher.final('hex');
  const tag = cipher.getAuthTag().toString('hex');

  return `${iv.toString('hex')}:${tag}:${encrypted}`;
}

/**
 * Decrypt an encrypted token back to plaintext
 * @param {string} encryptedString - Format: iv:authTag:ciphertext
 * @returns {string} - The decrypted session token
 */
function decryptToken(encryptedString) {
  if (!encryptedString) return '';
  const parts = encryptedString.split(':');
  if (parts.length !== 3) {
    throw new Error('Invalid encrypted token payload format');
  }

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

module.exports = {
  encryptToken,
  decryptToken,
  getMasterKey
};
