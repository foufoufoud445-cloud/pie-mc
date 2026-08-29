# Pie MC

A Minecraft bot engine with a web dashboard. Run multiple bots at once, automate chat stuff, and manage everything from your browser.

---

## What it does

- **Multi-instance bots** — Run a bunch of bots at the same time. Start, stop, restart them from the dashboard. Live status and auto-reconnect included.
- **Session token login** — Paste your Microsoft session token (SSID) and it links your account. Tokens are encrypted on disk with AES-256-GCM so they're not sitting in plaintext.
- **Live chat terminal** — See what your bots are saying in real time. Send commands like `/spawn` or `/msg` straight from the browser.
- **Triggers & automations** — Set up keyword or regex rules so bots auto-reply, whisper players, or run server commands on a timer.
- **Proxy support** — SOCKS5, SOCKS4, HTTP proxies. Import a bunch from a txt file if you need to spread across IPs.
- **Discord webhook alerts** — Get whispers, mentions, and server events forwarded to a Discord channel.
- **Custom sword cursor** — Pixel-art diamond sword pointer with particle effects on click. Totally unnecessary but fun.

---

## Running it locally

**Prerequisites:** Node.js v18+

```bash
cd backend
npm install
node server.js
```

Then open `http://localhost:8082` in your browser.

---

## Environment variables

You can set these in a `.env` file inside `backend/` or just let it use the defaults:

```env
PORT=8082
PIE_MC_API_KEY=your_key_here
DISCORD_CLIENT_ID=your_discord_client_id
DISCORD_CLIENT_SECRET=your_discord_client_secret
DISCORD_REDIRECT_URI=https://your-domain.com/api/auth/callback
```

If you're running on Render, set `PORT` and `DISCORD_REDIRECT_URI` there — or just leave `DISCORD_REDIRECT_URI` out and it'll figure it out from the request.

---

## Deploying to Render

1. Push this repo to GitHub (private is fine)
2. Create a new **Web Service** on [render.com](https://render.com)
3. Point it at your repo, set the root directory to `backend`
4. Build command: `npm install`
5. Start command: `node server.js`
6. Add your env vars in the Render dashboard

---

## Project structure

```
pie-mc/
├── backend/
│   ├── data/              # SQLite DB + encryption key (gitignored)
│   ├── src/
│   │   ├── auth.js        # AES-256-GCM token encryption
│   │   ├── botManager.js  # Mineflayer multi-instance controller
│   │   └── database.js    # SQLite schema
│   ├── server.js          # Express API + WebSocket server
│   └── package.json
├── public/
│   ├── login.html         # Discord OAuth login page
│   ├── dashboard.html     # Main bot control panel
│   ├── accounts.html      # Account management
│   ├── servers.html       # Server list
│   ├── chat.html          # Live terminal
│   ├── triggers.html      # Automation rules
│   └── shared.js          # Shared frontend utilities
└── .gitignore
```

---

## A note on security

Your session tokens are encrypted locally with AES-256-GCM. They never leave your machine unless you're using the Discord bridge or API. Don't share your `.env` or the `data/` folder.

---

## License

MIT
