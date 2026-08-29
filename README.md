# 🥧 Pie MC — Next-Gen Minecraft Bot & Automation Suite

**Pie MC** is a multi-instance Minecraft bot engine, real-time interactive terminal, and automation suite with an ultra-responsive dark-themed web dashboard and custom animated Minecraft sword cursor.

---

## 🌟 Key Features

1. **Custom Minecraft Diamond Sword Cursor & FX**
   - High-fidelity pixel-art diamond sword pointer.
   - Dynamic particle trails and critical hit click animations.

2. **Multi-Instance Dashboard**
   - Manage multiple concurrent bots (`Instance 1`, `Instance 2`, etc.).
   - Instant **Start / Stop / Restart** lifecycle controls.
   - Live status monitors with ping indicators and auto-reconnection policies.

3. **Session Token / SSID Account Linker**
   - Direct integration with Microsoft OAuth session tokens / SSIDs.
   - **Vault Cryptography**: Tokens are stored encrypted locally with **AES-256-GCM**.

4. **Live In-Game Terminal & Chat Relay**
   - Real-time bidirectional chat console with auto-scroll and color-coded player ranks.
   - Transmit commands (`/spawn`, `/tpa`, `/msg`, etc.) directly from the browser.

5. **Proxy Pool Tunneling**
   - Supports **SOCKS5**, **SOCKS4**, and **HTTP** proxies.
   - Batch import proxies via TXT file to bypass IP bans or rate limits.

6. **Reactive Triggers & Scheduled Automations**
   - Keyword, prefix, and regex match rules to automatically whisper players (`/msg <player>`) or execute server commands.
   - Cooldown management (per-player or global).
   - Interval-based scheduled broadcasts (every X seconds, minutes, or hours).

7. **Discord Bridge & Security Logs**
   - Webhook relay for whispers, mentions, and server drop alerts.
   - Comprehensive audit logs tracking trigger executions and player interactions.

---

## 🚀 Quick Start & Installation

### Prerequisites
- Node.js (v18 or higher recommended)
- npm or yarn

### 1. Install Dependencies
```bash
cd backend
npm install
```

### 2. Configure Environment (Optional)
Create a `.env` file in the `backend/` directory:
```env
PORT=8082
PIE_MC_API_KEY=pie_mc_live_89437b02c89f4172
```

### 3. Launch Pie MC
```bash
node server.js
```
Open your browser and navigate to:
```
http://localhost:8082/
```

---

## 📂 Project Structure

```
pie-mc/
├── backend/
│   ├── data/                 # SQLite database & AES encryption key
│   ├── src/
│   │   ├── auth.js           # AES-256-GCM token cipher
│   │   ├── botManager.js     # Multi-instance Mineflayer controller
│   │   └── database.js       # SQLite schema & repository
│   ├── package.json
│   └── server.js             # Express API & WebSocket Server
├── public/
│   └── index.html            # Complete Single-Page Dashboard & Particle FX
└── README.md
```

---

## 🔒 Security Notice
- Always ensure session tokens (SSIDs) are kept confidential.
- Pie MC stores tokens locally on your machine encrypted with AES-256-GCM.
