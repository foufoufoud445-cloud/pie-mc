import os

html_content = '''<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Pie MC — Next-Gen Minecraft Bot & Automation Suite</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  <script src="https://unpkg.com/lucide@latest"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          fontFamily: {
            sans: ['"Plus Jakarta Sans"', 'sans-serif'],
            mono: ['"JetBrains Mono"', 'monospace'],
          },
          colors: {
            mc: {
              diamond: '#2cf5d6',
              emerald: '#55ff55',
              gold: '#ffaa00',
              redstone: '#ff5555',
              lapis: '#3c78d8',
              netherite: '#312932',
              dark: '#0c0e14',
              card: '#121622',
              cardHover: '#181e2e',
              border: '#1f293d',
              borderGlow: '#2cf5d640',
            }
          },
          animation: {
            'pulse-slow': 'pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite',
            'float': 'float 4s ease-in-out infinite',
            'glow': 'glow 2s ease-in-out infinite alternate',
            'swing': 'swing 0.25s ease-in-out',
          },
          keyframes: {
            float: {
              '0%, 100%': { transform: 'translateY(0px)' },
              '50%': { transform: 'translateY(-6px)' },
            },
            glow: {
              'from': { boxShadow: '0 0 10px -2px rgba(44, 245, 214, 0.3)' },
              'to': { boxShadow: '0 0 25px 4px rgba(44, 245, 214, 0.6)' },
            },
            swing: {
              '0%': { transform: 'rotate(0deg)' },
              '50%': { transform: 'rotate(-25deg) scale(1.1)' },
              '100%': { transform: 'rotate(0deg)' },
            }
          }
        }
      }
    }
  </script>
  <style>
    /* Custom Minecraft Diamond Sword Cursor */
    :root {
      --sword-cursor: url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32"><path d="M0 0h2v2H0z" fill="%23000"/><path d="M2 0h2v2H2zM0 2h2v2H0z" fill="%232cf5d6"/><path d="M4 0h2v2H4zM2 2h2v2H2zM0 4h2v2H0z" fill="%23000"/><path d="M4 2h2v2H4zM2 4h2v2H2z" fill="%2355ffff"/><path d="M6 2h2v2H6zM4 4h2v2H4zM2 6h2v2H2z" fill="%23000"/><path d="M6 4h2v2H6zM4 6h2v2H4z" fill="%232cf5d6"/><path d="M8 4h2v2H8zM6 6h2v2H6zM4 8h2v2H4z" fill="%23000"/><path d="M8 6h2v2H8zM6 8h2v2H6z" fill="%2355ffff"/><path d="M10 6h2v2h-2zM8 8h2v2H8zM6 10h2v2H6z" fill="%23000"/><path d="M10 8h2v2h-2zM8 10h2v2H8z" fill="%232cf5d6"/><path d="M12 8h2v2h-2zM10 10h2v2h-2zM8 12h2v2H8z" fill="%23000"/><path d="M12 10h2v2h-2zM10 12h2v2h-2z" fill="%2355ffff"/><path d="M14 10h2v2h-2zM12 12h2v2h-2zM10 14h2v2h-2z" fill="%23000"/><path d="M14 12h2v2h-2zM12 14h2v2h-2z" fill="%232cf5d6"/><path d="M16 12h2v2h-2zM14 14h2v2h-2zM12 16h2v2h-2z" fill="%23000"/><path d="M8 16h2v2H8zM6 18h2v2H6zM14 16h2v2h-2zM16 14h2v2h-2zM18 12h2v2h-2z" fill="%23000"/><path d="M8 18h2v2H8zM10 16h2v2h-2zM12 18h2v2h-2zM14 18h2v2h-2zM16 16h2v2h-2zM18 14h2v2h-2z" fill="%232c9099"/><path d="M6 20h2v2H6zM8 20h2v2H8zM18 16h2v2h-2zM20 14h2v2h-2z" fill="%23000"/><path d="M14 20h2v2h-2zM12 22h2v2h-2z" fill="%23000"/><path d="M16 18h2v2h-2zM14 22h2v2h-2zM16 20h2v2h-2z" fill="%238b5a2b"/><path d="M18 18h2v2h-2zM16 22h2v2h-2zM14 24h2v2h-2z" fill="%23000"/><path d="M18 20h2v2h-2zM16 24h2v2h-2zM18 22h2v2h-2z" fill="%235c3a21"/><path d="M20 20h2v2h-2zM18 24h2v2h-2zM16 26h2v2h-2z" fill="%23000"/><path d="M18 26h2v2h-2zM20 24h2v2h-2zM22 22h2v2h-2z" fill="%23000"/><path d="M20 26h2v2h-2zM22 24h2v2h-2z" fill="%232cf5d6"/><path d="M22 26h2v2h-2zM24 24h2v2h-2zM20 28h2v2h-2z" fill="%23000"/></svg>') 0 0, auto;
    }

    * {
      cursor: var(--sword-cursor) !important;
    }

    input, textarea, select {
      cursor: text !important;
    }

    button, a, select, [role="button"] {
      cursor: var(--sword-cursor) !important;
    }

    /* Custom Scrollbars */
    ::-webkit-scrollbar {
      width: 6px;
      height: 6px;
    }
    ::-webkit-scrollbar-track {
      background: #0c0e14;
    }
    ::-webkit-scrollbar-thumb {
      background: #1f293d;
      border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: #2cf5d6;
    }

    #fx-canvas {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      pointer-events: none;
      z-index: 99999;
    }

    .glass-card {
      background: linear-gradient(135deg, rgba(18, 22, 34, 0.85) 0%, rgba(14, 17, 26, 0.95) 100%);
      backdrop-filter: blur(12px);
      border: 1px solid #1f293d;
      box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.4);
    }
    .glass-card:hover {
      border-color: rgba(44, 245, 214, 0.35);
    }

    .glow-border {
      box-shadow: 0 0 15px -3px rgba(44, 245, 214, 0.25);
    }
  </style>
</head>
<body class="bg-mc-dark text-slate-200 min-h-screen flex flex-col font-sans selection:bg-mc-diamond selection:text-black overflow-x-hidden">

  <!-- Visual Effect Canvas for Sword Particles & Slashes -->
  <canvas id="fx-canvas"></canvas>

  <!-- Global Header Navigation -->
  <header class="sticky top-0 z-40 border-b border-mc-border bg-mc-dark/90 backdrop-blur-md px-6 py-3.5 flex items-center justify-between shadow-lg">
    <div class="flex items-center space-x-6">
      <!-- Logo -->
      <div class="flex items-center space-x-3 group cursor-pointer" onclick="switchTab('dashboard')">
        <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-cyan-600 via-mc-diamond to-emerald-400 p-0.5 shadow-lg shadow-cyan-500/20 group-hover:scale-105 transition-transform duration-200 flex items-center justify-center">
          <div class="w-full h-full bg-mc-dark rounded-[10px] flex items-center justify-center">
            <span class="text-2xl font-black bg-gradient-to-r from-mc-diamond to-emerald-400 bg-clip-text text-transparent">π</span>
          </div>
        </div>
        <div>
          <div class="flex items-center space-x-2">
            <h1 class="text-xl font-extrabold tracking-wider bg-gradient-to-r from-white via-cyan-100 to-mc-diamond bg-clip-text text-transparent">PIE MC</h1>
            <span class="px-2 py-0.5 text-[10px] font-mono font-bold uppercase tracking-wider rounded-md bg-mc-diamond/10 text-mc-diamond border border-mc-diamond/30">v2.4.0</span>
          </div>
          <p class="text-xs text-slate-400 font-mono">Multi-Instance Bot Engine & Manager</p>
        </div>
      </div>

      <!-- Navigation Tabs -->
      <nav class="hidden md:flex items-center space-x-1 pl-4 border-l border-mc-border/60">
        <button onclick="switchTab('dashboard')" id="nav-dashboard" class="nav-btn px-3.5 py-2 rounded-lg text-sm font-medium transition-all duration-200 flex items-center space-x-2 text-mc-diamond bg-mc-diamond/10 border border-mc-diamond/30 shadow-sm">
          <i data-lucide="layout-dashboard" class="w-4 h-4"></i>
          <span>Dashboard</span>
        </button>
        <button onclick="switchTab('chat')" id="nav-chat" class="nav-btn px-3.5 py-2 rounded-lg text-sm font-medium transition-all duration-200 flex items-center space-x-2 text-slate-400 hover:text-white hover:bg-slate-800/60">
          <i data-lucide="message-square" class="w-4 h-4"></i>
          <span>Chat</span>
        </button>
        <button onclick="switchTab('accounts')" id="nav-accounts" class="nav-btn px-3.5 py-2 rounded-lg text-sm font-medium transition-all duration-200 flex items-center space-x-2 text-slate-400 hover:text-white hover:bg-slate-800/60">
          <i data-lucide="users" class="w-4 h-4"></i>
          <span>Accounts</span>
        </button>
        <button onclick="switchTab('servers')" id="nav-servers" class="nav-btn px-3.5 py-2 rounded-lg text-sm font-medium transition-all duration-200 flex items-center space-x-2 text-slate-400 hover:text-white hover:bg-slate-800/60">
          <i data-lucide="server" class="w-4 h-4"></i>
          <span>Servers</span>
        </button>
        <button onclick="switchTab('proxies')" id="nav-proxies" class="nav-btn px-3.5 py-2 rounded-lg text-sm font-medium transition-all duration-200 flex items-center space-x-2 text-slate-400 hover:text-white hover:bg-slate-800/60">
          <i data-lucide="shield-check" class="w-4 h-4"></i>
          <span>Proxies</span>
        </button>
        <button onclick="switchTab('automation')" id="nav-automation" class="nav-btn px-3.5 py-2 rounded-lg text-sm font-medium transition-all duration-200 flex items-center space-x-2 text-slate-400 hover:text-white hover:bg-slate-800/60">
          <i data-lucide="clock" class="w-4 h-4"></i>
          <span>Automation</span>
        </button>
        <button onclick="switchTab('triggers')" id="nav-triggers" class="nav-btn px-3.5 py-2 rounded-lg text-sm font-medium transition-all duration-200 flex items-center space-x-2 text-slate-400 hover:text-white hover:bg-slate-800/60">
          <i data-lucide="zap" class="w-4 h-4"></i>
          <span>Triggers</span>
        </button>
        <button onclick="switchTab('discord')" id="nav-discord" class="nav-btn px-3.5 py-2 rounded-lg text-sm font-medium transition-all duration-200 flex items-center space-x-2 text-slate-400 hover:text-white hover:bg-slate-800/60">
          <i data-lucide="disc" class="w-4 h-4"></i>
          <span>Discord</span>
        </button>
        <button onclick="switchTab('logs')" id="nav-logs" class="nav-btn px-3.5 py-2 rounded-lg text-sm font-medium transition-all duration-200 flex items-center space-x-2 text-slate-400 hover:text-white hover:bg-slate-800/60">
          <i data-lucide="file-text" class="w-4 h-4"></i>
          <span>Logs</span>
        </button>
      </nav>
    </div>

    <!-- Header Actions -->
    <div class="flex items-center space-x-3">
      <!-- Real-time Gateway Health -->
      <div class="hidden sm:flex items-center space-x-2 px-3 py-1.5 rounded-lg bg-mc-card border border-mc-border text-xs font-mono">
        <span class="w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
        <span class="text-slate-300">Mineflayer Engine: <strong class="text-emerald-400">Ready</strong></span>
      </div>

      <!-- Settings Button -->
      <button onclick="openModal('settingsModal')" class="p-2.5 rounded-xl bg-mc-card hover:bg-slate-800 border border-mc-border hover:border-mc-diamond/40 text-slate-300 hover:text-white transition-all duration-200 shadow-sm">
        <i data-lucide="settings" class="w-4 h-4"></i>
      </button>
    </div>
  </header>

  <!-- Instance Secondary Selector Bar -->
  <div id="instanceBar" class="bg-mc-card/60 border-b border-mc-border px-6 py-2.5 flex items-center justify-between">
    <div class="flex items-center space-x-2 overflow-x-auto" id="instanceTabsContainer">
      <!-- Injected via JS -->
    </div>
    <div class="flex items-center space-x-3 pl-4">
      <button onclick="addNewInstance()" class="px-3 py-1.5 rounded-lg bg-slate-800/80 hover:bg-slate-700 text-slate-300 hover:text-white text-xs font-semibold flex items-center space-x-1.5 border border-mc-border transition-all">
        <i data-lucide="plus" class="w-3.5 h-3.5"></i>
        <span>New Instance</span>
      </button>
    </div>
  </div>

  <!-- Main Content Container -->
  <main class="flex-1 p-6 max-w-7xl w-full mx-auto space-y-6">

    <!-- 1. DASHBOARD TAB -->
    <section id="tab-dashboard" class="tab-content space-y-6">
      <div class="glass-card rounded-2xl p-6 relative overflow-hidden">
        <div class="absolute -right-16 -top-16 w-64 h-64 bg-mc-diamond/10 rounded-full blur-3xl pointer-events-none"></div>
        
        <div class="flex flex-col lg:flex-row items-start lg:items-center justify-between gap-6 relative z-10">
          <div class="flex items-center space-x-4">
            <div id="botStatusPulse" class="w-14 h-14 rounded-2xl bg-slate-800/90 border border-mc-border flex items-center justify-center relative shadow-inner">
              <i data-lucide="bot" id="botIcon" class="w-7 h-7 text-emerald-400"></i>
              <span id="botStatusDot" class="absolute -top-1 -right-1 w-4 h-4 rounded-full bg-emerald-400 border-2 border-mc-dark shadow-[0_0_12px_#34d399]"></span>
            </div>
            <div>
              <div class="flex items-center space-x-3">
                <h2 id="activeInstanceTitle" class="text-2xl font-black text-white">Instance 1</h2>
                <span id="activeInstanceBadge" class="px-2.5 py-0.5 rounded-full text-xs font-mono font-bold bg-emerald-500/10 text-emerald-400 border border-emerald-500/30 uppercase tracking-wider">Online</span>
              </div>
              <p id="activeInstanceSubtitle" class="text-sm text-slate-400 mt-0.5 font-mono">Connected as <span class="text-mc-diamond font-bold">PieBot_Alpha</span> on <span class="text-white font-semibold">mc.hypixel.net:25565</span></p>
            </div>
          </div>

          <div class="flex items-center space-x-3 w-full lg:w-auto">
            <button id="btnToggleBot" onclick="toggleActiveBot()" class="flex-1 lg:flex-none px-6 py-3 rounded-xl bg-gradient-to-r from-red-600 to-rose-600 hover:from-red-500 hover:to-rose-500 text-white font-bold shadow-lg shadow-red-500/20 flex items-center justify-center space-x-2 transition-all transform active:scale-95">
              <i data-lucide="power" class="w-4 h-4"></i>
              <span id="btnToggleBotText">Stop Bot</span>
            </button>
            <button onclick="restartActiveBot()" class="px-4 py-3 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 font-semibold border border-mc-border flex items-center justify-center space-x-2 transition-all">
              <i data-lucide="refresh-cw" class="w-4 h-4"></i>
              <span>Restart</span>
            </button>
          </div>
        </div>

        <!-- 3 Primary Configuration Dropdown Cards -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mt-6 pt-6 border-t border-mc-border/60">
          <!-- Account Card -->
          <div class="bg-slate-900/60 rounded-xl p-4 border border-mc-border/80 hover:border-mc-diamond/40 transition-colors">
            <div class="flex items-center justify-between mb-2">
              <span class="text-xs font-semibold text-slate-400 uppercase tracking-wider flex items-center space-x-1.5">
                <i data-lucide="user-check" class="w-3.5 h-3.5 text-mc-diamond"></i>
                <span>Active Account</span>
              </span>
              <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">AUTHENTICATED</span>
            </div>
            <select id="selectInstanceAccount" onchange="updateInstanceConfig('account', this.value)" class="w-full bg-slate-800/90 border border-mc-border rounded-lg px-3 py-2 text-sm text-white font-semibold focus:outline-none focus:border-mc-diamond">
            </select>
            <div class="mt-2 flex items-center justify-between text-[11px] text-slate-400 font-mono">
              <span>UUID: <span id="cardAccountUUID" class="text-slate-300">d8f3-4a11-98bc-e6</span></span>
              <span class="text-emerald-400">AES-256 Valid</span>
            </div>
          </div>

          <!-- Server Card -->
          <div class="bg-slate-900/60 rounded-xl p-4 border border-mc-border/80 hover:border-mc-diamond/40 transition-colors">
            <div class="flex items-center justify-between mb-2">
              <span class="text-xs font-semibold text-slate-400 uppercase tracking-wider flex items-center space-x-1.5">
                <i data-lucide="server" class="w-3.5 h-3.5 text-mc-diamond"></i>
                <span>Target Server</span>
              </span>
              <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-cyan-500/10 text-cyan-400 border border-cyan-500/20">ONLINE</span>
            </div>
            <select id="selectInstanceServer" onchange="updateInstanceConfig('server', this.value)" class="w-full bg-slate-800/90 border border-mc-border rounded-lg px-3 py-2 text-sm text-white font-semibold focus:outline-none focus:border-mc-diamond">
            </select>
            <div class="mt-2 flex items-center justify-between text-[11px] text-slate-400 font-mono">
              <span>Host: <span id="cardServerHost" class="text-slate-300">mc.hypixel.net:25565</span></span>
              <span class="text-cyan-400">Ping: 24ms</span>
            </div>
          </div>

          <!-- Proxy Card -->
          <div class="bg-slate-900/60 rounded-xl p-4 border border-mc-border/80 hover:border-mc-diamond/40 transition-colors">
            <div class="flex items-center justify-between mb-2">
              <span class="text-xs font-semibold text-slate-400 uppercase tracking-wider flex items-center space-x-1.5">
                <i data-lucide="shield" class="w-3.5 h-3.5 text-mc-diamond"></i>
                <span>Proxy Routing</span>
              </span>
              <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-purple-500/10 text-purple-400 border border-purple-500/20">AUTO POOL</span>
            </div>
            <select id="selectInstanceProxy" onchange="updateInstanceConfig('proxy', this.value)" class="w-full bg-slate-800/90 border border-mc-border rounded-lg px-3 py-2 text-sm text-white font-semibold focus:outline-none focus:border-mc-diamond">
            </select>
            <div class="mt-2 flex items-center justify-between text-[11px] text-slate-400 font-mono">
              <span>Pool: <span class="text-slate-300">5 Proxies Ready</span></span>
              <span class="text-purple-400">SOCKS5 Tunneled</span>
            </div>
          </div>
        </div>
      </div>

      <!-- 4 Quick Metric Indicator Badges -->
      <div class="grid grid-cols-2 lg:grid-cols-4 gap-4">
        <div class="glass-card rounded-xl p-4 flex items-center space-x-4">
          <div class="w-12 h-12 rounded-xl bg-blue-500/10 border border-blue-500/20 flex items-center justify-center text-blue-400">
            <i data-lucide="users" class="w-6 h-6"></i>
          </div>
          <div>
            <div class="text-2xl font-black text-white" id="statAccountsCount">3</div>
            <div class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Accounts</div>
          </div>
        </div>
        <div class="glass-card rounded-xl p-4 flex items-center space-x-4">
          <div class="w-12 h-12 rounded-xl bg-cyan-500/10 border border-cyan-500/20 flex items-center justify-center text-mc-diamond">
            <i data-lucide="server" class="w-6 h-6"></i>
          </div>
          <div>
            <div class="text-2xl font-black text-white" id="statServersCount">4</div>
            <div class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Servers</div>
          </div>
        </div>
        <div class="glass-card rounded-xl p-4 flex items-center space-x-4">
          <div class="w-12 h-12 rounded-xl bg-purple-500/10 border border-purple-500/20 flex items-center justify-center text-purple-400">
            <i data-lucide="shield-check" class="w-6 h-6"></i>
          </div>
          <div>
            <div class="text-2xl font-black text-white" id="statProxiesCount">5</div>
            <div class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Proxies</div>
          </div>
        </div>
        <div class="glass-card rounded-xl p-4 flex items-center space-x-4">
          <div class="w-12 h-12 rounded-xl bg-emerald-500/10 border border-emerald-500/20 flex items-center justify-center text-emerald-400">
            <i data-lucide="zap" class="w-6 h-6"></i>
          </div>
          <div>
            <div class="text-2xl font-black text-white" id="statTriggersCount">8</div>
            <div class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Triggers</div>
          </div>
        </div>
      </div>

      <!-- Live Chat Stream Component -->
      <div class="glass-card rounded-2xl p-5 space-y-4">
        <div class="flex items-center justify-between">
          <div class="flex items-center space-x-3">
            <div class="w-3 h-3 rounded-full bg-mc-diamond animate-ping"></div>
            <h3 class="text-lg font-bold text-white flex items-center space-x-2">
              <span>Live In-Game Chat Stream</span>
              <span class="text-xs font-mono text-slate-400 font-normal">(Instance Live Feed)</span>
            </h3>
          </div>
          <div class="flex items-center space-x-2">
            <button onclick="clearChatLogs()" class="px-3 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white text-xs font-mono transition-colors">Clear Console</button>
            <button onclick="switchTab('chat')" class="px-3 py-1 rounded-lg bg-mc-diamond/10 hover:bg-mc-diamond/20 text-mc-diamond text-xs font-mono font-bold transition-colors">Open Full Console &rarr;</button>
          </div>
        </div>

        <div id="dashboardChatConsole" class="h-64 overflow-y-auto bg-black/70 rounded-xl p-4 font-mono text-xs space-y-2 border border-mc-border/80">
        </div>

        <!-- Quick Chat Input for Dashboard -->
        <form onsubmit="sendChatMessage(event)" class="flex items-center space-x-2 pt-2">
          <div class="relative flex-1">
            <input id="dashboardChatInput" type="text" placeholder="Send a chat message or /command through this bot..." class="w-full bg-slate-900/90 border border-mc-border rounded-xl px-4 py-2.5 text-sm text-white font-mono placeholder:text-slate-500 focus:outline-none focus:border-mc-diamond focus:ring-1 focus:ring-mc-diamond">
          </div>
          <button type="submit" class="px-5 py-2.5 rounded-xl bg-mc-diamond hover:bg-cyan-300 text-black font-bold text-sm shadow-md shadow-cyan-500/20 transition-transform active:scale-95 flex items-center space-x-1.5">
            <i data-lucide="send" class="w-4 h-4"></i>
            <span>Send</span>
          </button>
        </form>
      </div>
    </section>

    <!-- 2. FULL CHAT TAB -->
    <section id="tab-chat" class="tab-content hidden space-y-6">
      <div class="glass-card rounded-2xl p-6 flex flex-col h-[75vh]">
        <div class="flex items-center justify-between pb-4 border-b border-mc-border">
          <div class="flex items-center space-x-3">
            <div class="w-8 h-8 rounded-lg bg-mc-diamond/10 border border-mc-diamond/30 flex items-center justify-center text-mc-diamond">
              <i data-lucide="terminal" class="w-4 h-4"></i>
            </div>
            <div>
              <h2 class="text-lg font-bold text-white">Interactive Bot Terminal</h2>
              <p class="text-xs text-slate-400 font-mono">Full bidirectional WebSocket link with Mineflayer</p>
            </div>
          </div>

          <div class="flex items-center space-x-2">
            <button onclick="insertCommand('/spawn')" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-[11px] font-mono text-cyan-300 border border-slate-700">/spawn</button>
            <button onclick="insertCommand('/help')" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-[11px] font-mono text-cyan-300 border border-slate-700">/help</button>
            <button onclick="insertCommand('/list')" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-[11px] font-mono text-cyan-300 border border-slate-700">/list</button>
            <button onclick="clearChatLogs()" class="px-3 py-1 rounded bg-slate-800 hover:bg-slate-700 text-xs text-slate-300">Clear</button>
          </div>
        </div>

        <div id="fullChatConsole" class="flex-1 overflow-y-auto bg-black/80 rounded-xl p-4 my-4 font-mono text-xs space-y-2 border border-mc-border/80">
        </div>

        <form onsubmit="sendFullChatMessage(event)" class="flex items-center space-x-3 pt-2">
          <input id="fullChatInput" type="text" placeholder="Type a message or Minecraft command (e.g. /msg Notch hello or !coords)..." class="flex-1 bg-slate-900/90 border border-mc-border rounded-xl px-4 py-3 text-sm text-white font-mono placeholder:text-slate-500 focus:outline-none focus:border-mc-diamond focus:ring-1 focus:ring-mc-diamond">
          <button type="submit" class="px-6 py-3 rounded-xl bg-mc-diamond hover:bg-cyan-300 text-black font-bold text-sm shadow-lg shadow-cyan-500/20 transition-transform active:scale-95 flex items-center space-x-2">
            <i data-lucide="send" class="w-4 h-4"></i>
            <span>Transmit</span>
          </button>
        </form>
      </div>
    </section>

    <!-- 3. ACCOUNTS TAB -->
    <section id="tab-accounts" class="tab-content hidden space-y-6">
      <div class="glass-card rounded-2xl p-6 space-y-6">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
          <div>
            <h2 class="text-xl font-black text-white">Linked Minecraft Accounts</h2>
            <p class="text-xs text-slate-400 mt-1 font-mono">Manage Microsoft OAuth session tokens (SSID) & credentials</p>
          </div>
          <button onclick="openModal('linkAccountModal')" class="px-4 py-2.5 rounded-xl bg-mc-diamond hover:bg-cyan-300 text-black font-bold text-sm shadow-md shadow-cyan-500/20 flex items-center space-x-2 transition-transform active:scale-95">
            <i data-lucide="plus-circle" class="w-4 h-4"></i>
            <span>Link Account by SSID</span>
          </button>
        </div>

        <div class="p-3.5 rounded-xl bg-slate-900/80 border border-mc-border/80 flex items-center space-x-3 text-xs text-slate-300">
          <i data-lucide="shield-alert" class="w-5 h-5 text-mc-diamond flex-shrink-0"></i>
          <span><strong>Vault Encryption:</strong> All Minecraft tokens are stored in the local SQLite database encrypted with <strong>AES-256-GCM</strong>. Tokens never leave the host machine.</span>
        </div>

        <div class="overflow-x-auto rounded-xl border border-mc-border">
          <table class="w-full text-left text-sm text-slate-300">
            <thead class="bg-slate-900/90 text-xs uppercase font-mono text-slate-400 border-b border-mc-border">
              <tr>
                <th class="px-4 py-3">Player</th>
                <th class="px-4 py-3">Username</th>
                <th class="px-4 py-3">UUID</th>
                <th class="px-4 py-3">Auth Status</th>
                <th class="px-4 py-3">Added</th>
                <th class="px-4 py-3 text-right">Actions</th>
              </tr>
            </thead>
            <tbody id="accountsTableBody" class="divide-y divide-mc-border/60 bg-slate-950/40 font-mono text-xs">
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <!-- 4. SERVERS TAB -->
    <section id="tab-servers" class="tab-content hidden space-y-6">
      <div class="glass-card rounded-2xl p-6 space-y-6">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
          <div>
            <h2 class="text-xl font-black text-white">Minecraft Server Targets</h2>
            <p class="text-xs text-slate-400 mt-1 font-mono">Configure target server IPs, ports, and protocols</p>
          </div>
          <button onclick="openModal('addServerModal')" class="px-4 py-2.5 rounded-xl bg-mc-diamond hover:bg-cyan-300 text-black font-bold text-sm shadow-md shadow-cyan-500/20 flex items-center space-x-2 transition-transform active:scale-95">
            <i data-lucide="plus" class="w-4 h-4"></i>
            <span>Add Server</span>
          </button>
        </div>

        <div id="serversGrid" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        </div>
      </div>
    </section>

    <!-- 5. PROXIES TAB -->
    <section id="tab-proxies" class="tab-content hidden space-y-6">
      <div class="glass-card rounded-2xl p-6 space-y-6">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
          <div>
            <h2 class="text-xl font-black text-white">Proxy Pool Manager</h2>
            <p class="text-xs text-slate-400 mt-1 font-mono">Tunnel bots via SOCKS5, SOCKS4, and HTTP to avoid IP limits</p>
          </div>
          <div class="flex items-center space-x-3">
            <button onclick="openModal('importProxiesModal')" class="px-3.5 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold border border-mc-border flex items-center space-x-1.5 transition-all">
              <i data-lucide="file-up" class="w-4 h-4"></i>
              <span>Import TXT</span>
            </button>
            <button onclick="openModal('addProxyModal')" class="px-4 py-2 rounded-xl bg-mc-diamond hover:bg-cyan-300 text-black font-bold text-xs shadow-md shadow-cyan-500/20 flex items-center space-x-1.5 transition-transform active:scale-95">
              <i data-lucide="plus" class="w-4 h-4"></i>
              <span>Add Proxy</span>
            </button>
          </div>
        </div>

        <div class="overflow-x-auto rounded-xl border border-mc-border">
          <table class="w-full text-left text-sm text-slate-300">
            <thead class="bg-slate-900/90 text-xs uppercase font-mono text-slate-400 border-b border-mc-border">
              <tr>
                <th class="px-4 py-3">Name</th>
                <th class="px-4 py-3">Type</th>
                <th class="px-4 py-3">Host:Port</th>
                <th class="px-4 py-3">Auth</th>
                <th class="px-4 py-3">Latency</th>
                <th class="px-4 py-3 text-right">Actions</th>
              </tr>
            </thead>
            <tbody id="proxiesTableBody" class="divide-y divide-mc-border/60 bg-slate-950/40 font-mono text-xs">
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <!-- 6. AUTOMATION TAB -->
    <section id="tab-automation" class="tab-content hidden space-y-6">
      <div class="glass-card rounded-2xl p-6 space-y-6">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
          <div>
            <h2 class="text-xl font-black text-white">Scheduled Automations</h2>
            <p class="text-xs text-slate-400 mt-1 font-mono">Periodic repeating chat messages & routine commands</p>
          </div>
          <button onclick="openModal('newAutomationModal')" class="px-4 py-2.5 rounded-xl bg-mc-diamond hover:bg-cyan-300 text-black font-bold text-sm shadow-md shadow-cyan-500/20 flex items-center space-x-2 transition-transform active:scale-95">
            <i data-lucide="plus" class="w-4 h-4"></i>
            <span>New Automation</span>
          </button>
        </div>

        <div class="overflow-x-auto rounded-xl border border-mc-border">
          <table class="w-full text-left text-sm text-slate-300">
            <thead class="bg-slate-900/90 text-xs uppercase font-mono text-slate-400 border-b border-mc-border">
              <tr>
                <th class="px-4 py-3">Status</th>
                <th class="px-4 py-3">Message / Command</th>
                <th class="px-4 py-3">Interval</th>
                <th class="px-4 py-3">Instance Scope</th>
                <th class="px-4 py-3 text-right">Actions</th>
              </tr>
            </thead>
            <tbody id="automationsTableBody" class="divide-y divide-mc-border/60 bg-slate-950/40 font-mono text-xs">
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <!-- 7. TRIGGERS TAB -->
    <section id="tab-triggers" class="tab-content hidden space-y-6">
      <div class="glass-card rounded-2xl p-6 space-y-6">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
          <div>
            <h2 class="text-xl font-black text-white">Reactive Chat Triggers</h2>
            <p class="text-xs text-slate-400 mt-1 font-mono">Auto-respond to keywords, whispers, or player interactions</p>
          </div>
          <button onclick="openModal('newTriggerModal')" class="px-4 py-2.5 rounded-xl bg-mc-diamond hover:bg-cyan-300 text-black font-bold text-sm shadow-md shadow-cyan-500/20 flex items-center space-x-2 transition-transform active:scale-95">
            <i data-lucide="plus" class="w-4 h-4"></i>
            <span>New Trigger</span>
          </button>
        </div>

        <div class="overflow-x-auto rounded-xl border border-mc-border">
          <table class="w-full text-left text-sm text-slate-300">
            <thead class="bg-slate-900/90 text-xs uppercase font-mono text-slate-400 border-b border-mc-border">
              <tr>
                <th class="px-4 py-3">Status</th>
                <th class="px-4 py-3">Trigger Name</th>
                <th class="px-4 py-3">Keyword Match</th>
                <th class="px-4 py-3">Reply / Command</th>
                <th class="px-4 py-3">Cooldown</th>
                <th class="px-4 py-3 text-right">Actions</th>
              </tr>
            </thead>
            <tbody id="triggersTableBody" class="divide-y divide-mc-border/60 bg-slate-950/40 font-mono text-xs">
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <!-- 8. DISCORD TAB -->
    <section id="tab-discord" class="tab-content hidden space-y-6">
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
        <div class="glass-card rounded-2xl p-6 space-y-4">
          <h2 class="text-lg font-bold text-white flex items-center space-x-2">
            <i data-lucide="disc" class="w-5 h-5 text-indigo-400"></i>
            <span>Discord Webhook Bridge</span>
          </h2>
          <p class="text-xs text-slate-400">Forward Minecraft server events and chat whispers straight to Discord.</p>

          <div class="space-y-3 pt-2">
            <div>
              <label class="text-xs font-semibold text-slate-300">Webhook URL</label>
              <input type="text" id="discordWebhook" value="https://discord.com/api/webhooks/123..." class="w-full bg-slate-900/90 border border-mc-border rounded-xl px-3 py-2 text-xs font-mono text-white mt-1 focus:border-mc-diamond focus:outline-none">
            </div>

            <div class="space-y-2 pt-2">
              <label class="text-xs font-semibold text-slate-300">Forwarding Toggles</label>
              <label class="flex items-center space-x-2 text-xs text-slate-300">
                <input type="checkbox" checked class="rounded bg-slate-800 text-mc-diamond border-mc-border">
                <span>Direct Whispers / Messages</span>
              </label>
              <label class="flex items-center space-x-2 text-xs text-slate-300">
                <input type="checkbox" checked class="rounded bg-slate-800 text-mc-diamond border-mc-border">
                <span>Player Mentions</span>
              </label>
              <label class="flex items-center space-x-2 text-xs text-slate-300">
                <input type="checkbox" checked class="rounded bg-slate-800 text-mc-diamond border-mc-border">
                <span>Bot Disconnect & Reconnect Alerts</span>
              </label>
            </div>

            <button onclick="saveDiscordSettings()" class="w-full py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs shadow-md transition-all">
              Save Discord Bridge
            </button>
          </div>
        </div>

        <div class="glass-card rounded-2xl p-6 lg:col-span-2 space-y-4 flex flex-col h-[500px]">
          <div class="flex items-center justify-between pb-3 border-b border-mc-border">
            <div class="flex items-center space-x-3">
              <div class="w-8 h-8 rounded-full bg-indigo-500/20 text-indigo-400 flex items-center justify-center font-bold text-xs">
                #
              </div>
              <div>
                <h3 class="text-sm font-bold text-white">#mc-bot-relay (Live Feed)</h3>
                <span class="text-[11px] text-emerald-400 font-mono">● Webhook Active</span>
              </div>
            </div>
            <button onclick="clearDiscordRelay()" class="text-xs text-slate-400 hover:text-white">Clear</button>
          </div>

          <div id="discordRelayFeed" class="flex-1 overflow-y-auto bg-slate-950/70 rounded-xl p-4 font-mono text-xs space-y-3 border border-mc-border/80">
          </div>
        </div>
      </div>
    </section>

    <!-- 9. LOGS TAB -->
    <section id="tab-logs" class="tab-content hidden space-y-6">
      <div class="glass-card rounded-2xl p-6 space-y-6">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
          <div>
            <h2 class="text-xl font-black text-white">Audit & Trigger Execution Logs</h2>
            <p class="text-xs text-slate-400 mt-1 font-mono">System events, reactive executions, and security records</p>
          </div>
          <div class="flex items-center space-x-3">
            <div class="relative">
              <input id="logsSearchInput" oninput="filterLogs()" type="text" placeholder="Search player or event..." class="bg-slate-900/90 border border-mc-border rounded-xl px-3 py-1.5 text-xs text-white placeholder:text-slate-500 focus:outline-none focus:border-mc-diamond w-48">
            </div>
            <button onclick="clearSystemLogs()" class="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-mono">Clear</button>
          </div>
        </div>

        <div class="overflow-x-auto rounded-xl border border-mc-border">
          <table class="w-full text-left text-sm text-slate-300">
            <thead class="bg-slate-900/90 text-xs uppercase font-mono text-slate-400 border-b border-mc-border">
              <tr>
                <th class="px-4 py-3">Timestamp</th>
                <th class="px-4 py-3">Instance</th>
                <th class="px-4 py-3">Event Type</th>
                <th class="px-4 py-3">Player / Target</th>
                <th class="px-4 py-3">Details</th>
              </tr>
            </thead>
            <tbody id="logsTableBody" class="divide-y divide-mc-border/60 bg-slate-950/40 font-mono text-xs">
            </tbody>
          </table>
        </div>
      </div>
    </section>

  </main>

  <!-- MODALS -->

  <!-- Modal 1: Link Account by SSID -->
  <div id="linkAccountModal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm hidden items-center justify-center p-4">
    <div class="glass-card rounded-2xl p-6 max-w-lg w-full space-y-5 border border-mc-border shadow-2xl animate-glow">
      <div class="flex items-center justify-between border-b border-mc-border pb-3">
        <div class="flex items-center space-x-2.5">
          <i data-lucide="key-round" class="w-5 h-5 text-mc-diamond"></i>
          <h3 class="text-lg font-bold text-white">Link Minecraft Account (SSID / Session)</h3>
        </div>
        <button onclick="closeModal('linkAccountModal')" class="text-slate-400 hover:text-white"><i data-lucide="x" class="w-5 h-5"></i></button>
      </div>

      <div class="space-y-4 text-xs">
        <div>
          <label class="block font-semibold text-slate-300 mb-1">Account Display Label / Username</label>
          <input id="newAccUsername" type="text" placeholder="e.g. PieBot_Prime" class="w-full bg-slate-900 border border-mc-border rounded-xl px-3 py-2.5 text-sm text-white font-mono focus:border-mc-diamond focus:outline-none">
        </div>

        <div>
          <label class="block font-semibold text-slate-300 mb-1">Session Token / SSID (Microsoft OAuth JWT)</label>
          <textarea id="newAccToken" rows="4" placeholder="Paste your Microsoft / Minecraft launcher session token or SSID here..." class="w-full bg-slate-900 border border-mc-border rounded-xl p-3 text-xs text-mc-diamond font-mono focus:border-mc-diamond focus:outline-none"></textarea>
          <p class="text-[11px] text-slate-500 mt-1 font-mono">* Accepts session tokens obtained via Microsoft OAuth authentication flow.</p>
        </div>

        <div class="p-3 rounded-xl bg-emerald-500/10 border border-emerald-500/20 text-emerald-300 flex items-start space-x-2">
          <i data-lucide="lock" class="w-4 h-4 mt-0.5 flex-shrink-0"></i>
          <span>Tokens are encrypted with <strong>AES-256-GCM</strong> using machine-level keys in <code>backend/data/encryption.key</code> and never leave your server.</span>
        </div>
      </div>

      <div class="flex items-center justify-end space-x-3 pt-2">
        <button onclick="closeModal('linkAccountModal')" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold text-xs">Cancel</button>
        <button onclick="submitLinkAccount()" class="px-5 py-2 rounded-xl bg-mc-diamond hover:bg-cyan-300 text-black font-bold text-xs shadow-md shadow-cyan-500/20">Verify & Save Account</button>
      </div>
    </div>
  </div>

  <!-- Modal 2: Add Server -->
  <div id="addServerModal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm hidden items-center justify-center p-4">
    <div class="glass-card rounded-2xl p-6 max-w-md w-full space-y-5 border border-mc-border shadow-2xl">
      <div class="flex items-center justify-between border-b border-mc-border pb-3">
        <div class="flex items-center space-x-2.5">
          <i data-lucide="server" class="w-5 h-5 text-mc-diamond"></i>
          <h3 class="text-lg font-bold text-white">Add Target Server</h3>
        </div>
        <button onclick="closeModal('addServerModal')" class="text-slate-400 hover:text-white"><i data-lucide="x" class="w-5 h-5"></i></button>
      </div>

      <div class="space-y-4 text-xs">
        <div>
          <label class="block font-semibold text-slate-300 mb-1">Server Name</label>
          <input id="newServerName" type="text" placeholder="e.g. Hypixel Network" class="w-full bg-slate-900 border border-mc-border rounded-xl px-3 py-2.5 text-sm text-white font-mono focus:border-mc-diamond focus:outline-none">
        </div>
        <div>
          <label class="block font-semibold text-slate-300 mb-1">Host / IP</label>
          <input id="newServerHost" type="text" placeholder="e.g. mc.hypixel.net" class="w-full bg-slate-900 border border-mc-border rounded-xl px-3 py-2.5 text-sm text-white font-mono focus:border-mc-diamond focus:outline-none">
        </div>
        <div>
          <label class="block font-semibold text-slate-300 mb-1">Port</label>
          <input id="newServerPort" type="number" value="25565" class="w-full bg-slate-900 border border-mc-border rounded-xl px-3 py-2.5 text-sm text-white font-mono focus:border-mc-diamond focus:outline-none">
        </div>
      </div>

      <div class="flex items-center justify-end space-x-3 pt-2">
        <button onclick="closeModal('addServerModal')" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold text-xs">Cancel</button>
        <button onclick="submitAddServer()" class="px-5 py-2 rounded-xl bg-mc-diamond hover:bg-cyan-300 text-black font-bold text-xs shadow-md shadow-cyan-500/20">Add Server</button>
      </div>
    </div>
  </div>

  <!-- Modal 3: Add Proxy -->
  <div id="addProxyModal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm hidden items-center justify-center p-4">
    <div class="glass-card rounded-2xl p-6 max-w-md w-full space-y-5 border border-mc-border shadow-2xl">
      <div class="flex items-center justify-between border-b border-mc-border pb-3">
        <div class="flex items-center space-x-2.5">
          <i data-lucide="shield" class="w-5 h-5 text-mc-diamond"></i>
          <h3 class="text-lg font-bold text-white">Add Proxy</h3>
        </div>
        <button onclick="closeModal('addProxyModal')" class="text-slate-400 hover:text-white"><i data-lucide="x" class="w-5 h-5"></i></button>
      </div>

      <div class="space-y-4 text-xs">
        <div>
          <label class="block font-semibold text-slate-300 mb-1">Proxy Name</label>
          <input id="newProxyName" type="text" placeholder="e.g. US Residential 01" class="w-full bg-slate-900 border border-mc-border rounded-xl px-3 py-2.5 text-sm text-white font-mono focus:border-mc-diamond focus:outline-none">
        </div>
        <div>
          <label class="block font-semibold text-slate-300 mb-1">Type</label>
          <select id="newProxyType" class="w-full bg-slate-900 border border-mc-border rounded-xl px-3 py-2.5 text-sm text-white font-mono focus:border-mc-diamond focus:outline-none">
            <option value="SOCKS5">SOCKS5 (Recommended for Minecraft)</option>
            <option value="SOCKS4">SOCKS4</option>
            <option value="HTTP">HTTP</option>
          </select>
        </div>
        <div class="grid grid-cols-3 gap-2">
          <div class="col-span-2">
            <label class="block font-semibold text-slate-300 mb-1">Host / IP</label>
            <input id="newProxyHost" type="text" placeholder="192.168.1.100" class="w-full bg-slate-900 border border-mc-border rounded-xl px-3 py-2.5 text-sm text-white font-mono focus:border-mc-diamond focus:outline-none">
          </div>
          <div>
            <label class="block font-semibold text-slate-300 mb-1">Port</label>
            <input id="newProxyPort" type="number" placeholder="1080" class="w-full bg-slate-900 border border-mc-border rounded-xl px-3 py-2.5 text-sm text-white font-mono focus:border-mc-diamond focus:outline-none">
          </div>
        </div>
      </div>

      <div class="flex items-center justify-end space-x-3 pt-2">
        <button onclick="closeModal('addProxyModal')" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold text-xs">Cancel</button>
        <button onclick="submitAddProxy()" class="px-5 py-2 rounded-xl bg-mc-diamond hover:bg-cyan-300 text-black font-bold text-xs shadow-md shadow-cyan-500/20">Save Proxy</button>
      </div>
    </div>
  </div>

  <!-- Modal 4: Import Proxies TXT -->
  <div id="importProxiesModal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm hidden items-center justify-center p-4">
    <div class="glass-card rounded-2xl p-6 max-w-lg w-full space-y-5 border border-mc-border shadow-2xl">
      <div class="flex items-center justify-between border-b border-mc-border pb-3">
        <div class="flex items-center space-x-2.5">
          <i data-lucide="file-up" class="w-5 h-5 text-mc-diamond"></i>
          <h3 class="text-lg font-bold text-white">Import Proxies via TXT</h3>
        </div>
        <button onclick="closeModal('importProxiesModal')" class="text-slate-400 hover:text-white"><i data-lucide="x" class="w-5 h-5"></i></button>
      </div>

      <div class="space-y-3 text-xs">
        <label class="block font-semibold text-slate-300">Paste formatted proxy list (one per line):</label>
        <textarea id="importProxiesText" rows="6" placeholder="ip:port&#10;ip:port:user:pass&#10;socks5://user:pass@ip:port" class="w-full bg-slate-900 border border-mc-border rounded-xl p-3 text-xs text-mc-diamond font-mono focus:border-mc-diamond focus:outline-none"></textarea>
      </div>

      <div class="flex items-center justify-end space-x-3 pt-2">
        <button onclick="closeModal('importProxiesModal')" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold text-xs">Cancel</button>
        <button onclick="submitImportProxies()" class="px-5 py-2 rounded-xl bg-mc-diamond hover:bg-cyan-300 text-black font-bold text-xs shadow-md shadow-cyan-500/20">Import All</button>
      </div>
    </div>
  </div>

  <!-- Modal 5: New Automation -->
  <div id="newAutomationModal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm hidden items-center justify-center p-4">
    <div class="glass-card rounded-2xl p-6 max-w-md w-full space-y-5 border border-mc-border shadow-2xl">
      <div class="flex items-center justify-between border-b border-mc-border pb-3">
        <div class="flex items-center space-x-2.5">
          <i data-lucide="clock" class="w-5 h-5 text-mc-diamond"></i>
          <h3 class="text-lg font-bold text-white">Create Scheduled Task</h3>
        </div>
        <button onclick="closeModal('newAutomationModal')" class="text-slate-400 hover:text-white"><i data-lucide="x" class="w-5 h-5"></i></button>
      </div>

      <div class="space-y-4 text-xs">
        <div>
          <label class="block font-semibold text-slate-300 mb-1">Message / Command to Execute</label>
          <input id="newAutoMsg" type="text" placeholder="e.g. /clan broadcast We are recruiting!" class="w-full bg-slate-900 border border-mc-border rounded-xl px-3 py-2.5 text-sm text-white font-mono focus:border-mc-diamond focus:outline-none">
        </div>
        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block font-semibold text-slate-300 mb-1">Every</label>
            <input id="newAutoInterval" type="number" value="60" class="w-full bg-slate-900 border border-mc-border rounded-xl px-3 py-2.5 text-sm text-white font-mono focus:border-mc-diamond focus:outline-none">
          </div>
          <div>
            <label class="block font-semibold text-slate-300 mb-1">Unit</label>
            <select id="newAutoUnit" class="w-full bg-slate-900 border border-mc-border rounded-xl px-3 py-2.5 text-sm text-white font-mono focus:border-mc-diamond focus:outline-none">
              <option value="seconds">Seconds</option>
              <option value="minutes">Minutes</option>
              <option value="hours">Hours</option>
            </select>
          </div>
        </div>
      </div>

      <div class="flex items-center justify-end space-x-3 pt-2">
        <button onclick="closeModal('newAutomationModal')" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold text-xs">Cancel</button>
        <button onclick="submitNewAutomation()" class="px-5 py-2 rounded-xl bg-mc-diamond hover:bg-cyan-300 text-black font-bold text-xs shadow-md shadow-cyan-500/20">Create Task</button>
      </div>
    </div>
  </div>

  <!-- Modal 6: New Trigger -->
  <div id="newTriggerModal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm hidden items-center justify-center p-4">
    <div class="glass-card rounded-2xl p-6 max-w-lg w-full space-y-5 border border-mc-border shadow-2xl">
      <div class="flex items-center justify-between border-b border-mc-border pb-3">
        <div class="flex items-center space-x-2.5">
          <i data-lucide="zap" class="w-5 h-5 text-mc-diamond"></i>
          <h3 class="text-lg font-bold text-white">Create Reactive Trigger</h3>
        </div>
        <button onclick="closeModal('newTriggerModal')" class="text-slate-400 hover:text-white"><i data-lucide="x" class="w-5 h-5"></i></button>
      </div>

      <div class="space-y-4 text-xs">
        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block font-semibold text-slate-300 mb-1">Trigger Name</label>
            <input id="newTriggerName" type="text" placeholder="e.g. Greeter" class="w-full bg-slate-900 border border-mc-border rounded-xl px-3 py-2.5 text-sm text-white font-mono focus:border-mc-diamond focus:outline-none">
          </div>
          <div>
            <label class="block font-semibold text-slate-300 mb-1">Keyword</label>
            <input id="newTriggerKeyword" type="text" placeholder="e.g. !discord or hello" class="w-full bg-slate-900 border border-mc-border rounded-xl px-3 py-2.5 text-sm text-white font-mono focus:border-mc-diamond focus:outline-none">
          </div>
        </div>

        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block font-semibold text-slate-300 mb-1">Match Mode</label>
            <select id="newTriggerMode" class="w-full bg-slate-900 border border-mc-border rounded-xl px-3 py-2.5 text-sm text-white font-mono focus:border-mc-diamond focus:outline-none">
              <option value="Keyword anywhere">Keyword anywhere</option>
              <option value="Exact match">Exact match</option>
              <option value="Starts with">Starts with</option>
              <option value="Regex">Regex Pattern</option>
            </select>
          </div>
          <div>
            <label class="block font-semibold text-slate-300 mb-1">Cooldown (Seconds)</label>
            <input id="newTriggerCooldown" type="number" value="15" class="w-full bg-slate-900 border border-mc-border rounded-xl px-3 py-2.5 text-sm text-white font-mono focus:border-mc-diamond focus:outline-none">
          </div>
        </div>

        <div>
          <label class="block font-semibold text-slate-300 mb-1">Reply Action / Message</label>
          <input id="newTriggerReply" type="text" placeholder="e.g. Join our discord at discord.gg/piemc or /msg {player} Welcome!" class="w-full bg-slate-900 border border-mc-border rounded-xl px-3 py-2.5 text-sm text-white font-mono focus:border-mc-diamond focus:outline-none">
          <p class="text-[11px] text-slate-500 mt-1 font-mono">* Standard messages whisper back to player. Messages starting with <code>/</code> execute as raw server commands.</p>
        </div>
      </div>

      <div class="flex items-center justify-end space-x-3 pt-2">
        <button onclick="closeModal('newTriggerModal')" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold text-xs">Cancel</button>
        <button onclick="submitNewTrigger()" class="px-5 py-2 rounded-xl bg-mc-diamond hover:bg-cyan-300 text-black font-bold text-xs shadow-md shadow-cyan-500/20">Create Trigger</button>
      </div>
    </div>
  </div>

  <!-- Modal 7: Settings -->
  <div id="settingsModal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm hidden items-center justify-center p-4">
    <div class="glass-card rounded-2xl p-6 max-w-lg w-full space-y-5 border border-mc-border shadow-2xl">
      <div class="flex items-center justify-between border-b border-mc-border pb-3">
        <div class="flex items-center space-x-2.5">
          <i data-lucide="settings" class="w-5 h-5 text-mc-diamond"></i>
          <h3 class="text-lg font-bold text-white">Pie MC System Configuration</h3>
        </div>
        <button onclick="closeModal('settingsModal')" class="text-slate-400 hover:text-white"><i data-lucide="x" class="w-5 h-5"></i></button>
      </div>

      <div class="space-y-4 text-xs">
        <div class="space-y-3">
          <h4 class="text-xs font-bold uppercase tracking-wider text-mc-diamond font-mono">Connection & Reconnect Policies</h4>
          <label class="flex items-center justify-between p-3 rounded-xl bg-slate-900/80 border border-mc-border">
            <span>Auto-Reconnect on Disconnect</span>
            <input type="checkbox" checked class="w-4 h-4 rounded text-mc-diamond bg-slate-800 border-mc-border">
          </label>
          <div class="grid grid-cols-2 gap-3">
            <div>
              <label class="block font-semibold text-slate-300 mb-1">Retry Delay (Seconds)</label>
              <input type="number" value="10" class="w-full bg-slate-900 border border-mc-border rounded-xl px-3 py-2 text-xs text-white font-mono">
            </div>
            <div>
              <label class="block font-semibold text-slate-300 mb-1">Max Retry Attempts</label>
              <input type="number" value="5" class="w-full bg-slate-900 border border-mc-border rounded-xl px-3 py-2 text-xs text-white font-mono">
            </div>
          </div>
        </div>

        <div class="space-y-2 pt-2">
          <h4 class="text-xs font-bold uppercase tracking-wider text-mc-diamond font-mono">Security & API</h4>
          <div>
            <label class="block font-semibold text-slate-300 mb-1">Backend API Key (Bearer)</label>
            <input type="text" value="pie_mc_live_89437b02c89f4172" class="w-full bg-slate-900 border border-mc-border rounded-xl px-3 py-2 text-xs text-mc-diamond font-mono">
          </div>
          <div>
            <label class="block font-semibold text-slate-300 mb-1">Target Version Protocol</label>
            <select class="w-full bg-slate-900 border border-mc-border rounded-xl px-3 py-2 text-xs text-white font-mono">
              <option>1.21.1 / 1.21.11 (Latest)</option>
              <option>1.20.4</option>
              <option>1.19.4</option>
              <option>1.16.5</option>
              <option>1.8.9</option>
            </select>
          </div>
        </div>
      </div>

      <div class="flex items-center justify-end space-x-3 pt-2">
        <button onclick="closeModal('settingsModal')" class="px-5 py-2 rounded-xl bg-mc-diamond hover:bg-cyan-300 text-black font-bold text-xs shadow-md shadow-cyan-500/20">Save Preferences</button>
      </div>
    </div>
  </div>

  <!-- JavaScript Application Logic & Particle Engine -->
  <script>
    const state = {
      activeTab: 'dashboard',
      activeInstanceId: 1,
      instances: [
        { id: 1, name: 'Instance 1', status: 'online', account: 'PieBot_Alpha', server: 'Hypixel Network', proxy: 'US Residential 01' },
        { id: 2, name: 'Instance 2', status: 'offline', account: 'PieBot_Bravo', server: '2b2t Anarchy', proxy: 'EU SOCKS5 Alpha' },
        { id: 3, name: 'Instance 3', status: 'online', account: 'PieBot_Delta', server: 'Localhost Test', proxy: 'Auto' }
      ],
      accounts: [
        { id: '1', username: 'PieBot_Alpha', uuid: 'd8f3-4a11-98bc-e63f912', status: 'authenticated', added: '2026-08-10' },
        { id: '2', username: 'PieBot_Bravo', uuid: 'e712-3b99-11aa-a82f331', status: 'authenticated', added: '2026-08-15' },
        { id: '3', username: 'PieBot_Delta', uuid: '99a1-00cc-77bb-c1289ee', status: 'authenticated', added: '2026-08-20' }
      ],
      servers: [
        { id: '1', name: 'Hypixel Network', host: 'mc.hypixel.net', port: 25565, players: '48,219/100,000', ping: '24ms', status: 'online' },
        { id: '2', name: '2b2t Anarchy', host: '2b2t.org', port: 25565, players: '250/250 (Queue: 412)', ping: '68ms', status: 'online' },
        { id: '3', name: 'Localhost Test', host: '127.0.0.1', port: 25565, players: '1/20', ping: '1ms', status: 'online' },
        { id: '4', name: 'PVP Club', host: 'pvp.land', port: 25565, players: '1,420/5,000', ping: '32ms', status: 'online' }
      ],
      proxies: [
        { id: '1', name: 'US Residential 01', type: 'SOCKS5', host: '142.93.18.22', port: 1080, auth: 'user:pass', latency: '42ms' },
        { id: '2', name: 'EU SOCKS5 Alpha', type: 'SOCKS5', host: '178.62.204.11', port: 1080, auth: 'None', latency: '65ms' },
        { id: '3', name: 'Fast HTTP Gateway', type: 'HTTP', host: '104.248.50.88', port: 8080, auth: 'pie:secure', latency: '28ms' },
        { id: '4', name: 'Asia Singapore Node', type: 'SOCKS5', host: '128.199.192.4', port: 1080, auth: 'user:pass', latency: '110ms' },
        { id: '5', name: 'Backup SOCKS4', type: 'SOCKS4', host: '167.99.135.2', port: 1080, auth: 'None', latency: '54ms' }
      ],
      automations: [
        { id: '1', msg: '/clan recruit Join Pie Squad for top rewards!', interval: '60 seconds', status: true, scope: 'Instance 1' },
        { id: '2', msg: 'Pie MC Bot online - Type !help for commands', interval: '5 minutes', status: true, scope: 'All Instances' },
        { id: '3', msg: '/coords broadcast', interval: '10 minutes', status: false, scope: 'Instance 2' }
      ],
      triggers: [
        { id: '1', name: 'Welcome Greeter', keyword: 'hello', mode: 'Keyword anywhere', reply: 'Welcome to the server! Need help? /msg me', cooldown: 10, status: true },
        { id: '2', name: 'Discord Link', keyword: '!discord', mode: 'Exact match', reply: 'Join our official Discord: discord.gg/piemc', cooldown: 5, status: true },
        { id: '3', name: 'Shop Teleport', keyword: '!shop', mode: 'Exact match', reply: '/tpa {player}', cooldown: 30, status: true },
        { id: '4', name: 'Auto GG', keyword: 'gg', mode: 'Exact match', reply: 'GG WP everyone!', cooldown: 15, status: true }
      ],
      logs: [
        { time: '15:52:10', instance: 'Instance 1', event: 'Trigger Fired', player: 'Alex_Pro', details: 'Replied to [!discord]' },
        { time: '15:51:44', instance: 'Instance 1', event: 'Chat Received', player: 'Notch_99', details: 'says: hello bot' },
        { time: '15:50:02', instance: 'Instance 1', event: 'Scheduled Task', player: 'SYSTEM', details: 'Broadcasted clan recruitment' },
        { time: '15:48:19', instance: 'Instance 1', event: 'Bot Connected', player: 'PieBot_Alpha', details: 'Logged in to mc.hypixel.net' }
      ],
      chatLogs: [
        { time: '15:52:10', player: 'Alex_Pro', tag: '[VIP+]', msg: '!discord', type: 'chat' },
        { time: '15:52:11', player: 'PieBot_Alpha', tag: '[BOT]', msg: 'Join our official Discord: discord.gg/piemc', type: 'bot' },
        { time: '15:52:30', player: 'SteveGamer', tag: '[MEMBER]', msg: 'Who wants to team up for Bedwars?', type: 'chat' },
        { time: '15:53:01', player: 'Server', tag: '[SYSTEM]', msg: 'Voting event begins in 5 minutes!', type: 'system' }
      ],
      discordRelay: [
        { time: '15:52:10', author: 'PieMC-Relay', content: '💬 **[Instance 1]** <Alex_Pro> !discord' },
        { time: '15:52:11', author: 'PieMC-Relay', content: '🤖 **[Instance 1]** <PieBot_Alpha> Join our official Discord: discord.gg/piemc' }
      ]
    };

    function renderInstanceTabs() {
      const container = document.getElementById('instanceTabsContainer');
      container.innerHTML = state.instances.map(inst => `
        <button onclick="switchInstance(${inst.id})" class="px-3.5 py-1.5 rounded-lg text-xs font-mono font-semibold transition-all flex items-center space-x-2 border ${
          state.activeInstanceId === inst.id
            ? 'bg-mc-diamond/15 text-mc-diamond border-mc-diamond/40 shadow-sm'
            : 'bg-slate-800/40 text-slate-400 hover:text-white border-mc-border hover:bg-slate-800'
        }">
          <span class="w-2 h-2 rounded-full ${inst.status === 'online' ? 'bg-emerald-400 animate-pulse' : 'bg-red-400'}"></span>
          <span>${inst.name}</span>
        </button>
      `).join('');
      renderDashboardControls();
    }

    function renderDashboardControls() {
      const activeInst = state.instances.find(i => i.id === state.activeInstanceId) || state.instances[0];
      document.getElementById('activeInstanceTitle').innerText = activeInst.name;
      
      const badge = document.getElementById('activeInstanceBadge');
      const dot = document.getElementById('botStatusDot');
      const btnText = document.getElementById('btnToggleBotText');
      const btn = document.getElementById('btnToggleBot');

      if (activeInst.status === 'online') {
        badge.className = 'px-2.5 py-0.5 rounded-full text-xs font-mono font-bold bg-emerald-500/10 text-emerald-400 border border-emerald-500/30 uppercase tracking-wider';
        badge.innerText = 'Online';
        dot.className = 'absolute -top-1 -right-1 w-4 h-4 rounded-full bg-emerald-400 border-2 border-mc-dark shadow-[0_0_12px_#34d399]';
        btnText.innerText = 'Stop Bot';
        btn.className = 'flex-1 lg:flex-none px-6 py-3 rounded-xl bg-gradient-to-r from-red-600 to-rose-600 hover:from-red-500 hover:to-rose-500 text-white font-bold shadow-lg shadow-red-500/20 flex items-center justify-center space-x-2 transition-all';
      } else {
        badge.className = 'px-2.5 py-0.5 rounded-full text-xs font-mono font-bold bg-red-500/10 text-red-400 border border-red-500/30 uppercase tracking-wider';
        badge.innerText = 'Offline';
        dot.className = 'absolute -top-1 -right-1 w-4 h-4 rounded-full bg-red-500 border-2 border-mc-dark';
        btnText.innerText = 'Start Bot';
        btn.className = 'flex-1 lg:flex-none px-6 py-3 rounded-xl bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white font-bold shadow-lg shadow-emerald-500/20 flex items-center justify-center space-x-2 transition-all';
      }

      document.getElementById('activeInstanceSubtitle').innerHTML = `Connected as <span class="text-mc-diamond font-bold">${activeInst.account}</span> on <span class="text-white font-semibold">${activeInst.server}</span>`;

      const accSelect = document.getElementById('selectInstanceAccount');
      accSelect.innerHTML = state.accounts.map(a => `<option value="${a.username}" ${a.username === activeInst.account ? 'selected' : ''}>${a.username} (${a.uuid.substring(0,8)}...)</option>`).join('');

      const srvSelect = document.getElementById('selectInstanceServer');
      srvSelect.innerHTML = state.servers.map(s => `<option value="${s.name}" ${s.name === activeInst.server ? 'selected' : ''}>${s.name} (${s.host}:${s.port})</option>`).join('');

      const prxSelect = document.getElementById('selectInstanceProxy');
      prxSelect.innerHTML = `<option value="Auto">Auto Pool (Best Available)</option>` + state.proxies.map(p => `<option value="${p.name}" ${p.name === activeInst.proxy ? 'selected' : ''}>${p.name} [${p.type}]</option>`).join('');
    }

    function renderTables() {
      document.getElementById('accountsTableBody').innerHTML = state.accounts.map(a => `
        <tr class="hover:bg-slate-900/60 transition-colors">
          <td class="px-4 py-3">
            <div class="flex items-center space-x-2.5">
              <div class="w-7 h-7 rounded bg-slate-800 border border-mc-border overflow-hidden flex items-center justify-center">
                <img src="https://mc-heads.net/avatar/${a.username}/28" alt="" class="w-full h-full object-cover" onerror="this.src='data:image/svg+xml;utf8,<svg xmlns=\\'http://www.w3.org/2000/svg\\' width=\\'28\\' height=\\'28\\' fill=\\'%232cf5d6\\'><rect width=\\'28\\' height=\\'28\\' fill=\\'%231e293b\\'/></svg>'">
              </div>
              <span class="font-bold text-white">${a.username}</span>
            </div>
          </td>
          <td class="px-4 py-3 text-slate-300 font-semibold">${a.username}</td>
          <td class="px-4 py-3 text-slate-400">${a.uuid}</td>
          <td class="px-4 py-3"><span class="px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 text-[10px]">AUTHENTICATED</span></td>
          <td class="px-4 py-3 text-slate-500">${a.added}</td>
          <td class="px-4 py-3 text-right space-x-2">
            <button onclick="deleteAccount('${a.id}')" class="text-red-400 hover:text-red-300"><i data-lucide="trash-2" class="w-4 h-4 inline"></i></button>
          </td>
        </tr>
      `).join('');

      document.getElementById('serversGrid').innerHTML = state.servers.map(s => `
        <div class="glass-card rounded-xl p-4 border border-mc-border hover:border-mc-diamond/40 transition-all space-y-3">
          <div class="flex items-center justify-between">
            <h4 class="font-bold text-white text-base flex items-center space-x-2">
              <i data-lucide="server" class="w-4 h-4 text-mc-diamond"></i>
              <span>${s.name}</span>
            </h4>
            <span class="px-2 py-0.5 rounded text-[10px] font-mono bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">ONLINE</span>
          </div>
          <div class="text-xs font-mono text-slate-400 space-y-1">
            <div>Address: <span class="text-slate-200 font-semibold">${s.host}:${s.port}</span></div>
            <div>Players: <span class="text-slate-300">${s.players}</span></div>
            <div>Latency: <span class="text-cyan-400 font-bold">${s.ping}</span></div>
          </div>
          <div class="flex items-center justify-end space-x-2 pt-2 border-t border-mc-border/60">
            <button onclick="deleteServer('${s.id}')" class="px-2 py-1 text-xs text-red-400 hover:text-red-300"><i data-lucide="trash-2" class="w-3.5 h-3.5"></i></button>
          </div>
        </div>
      `).join('');

      document.getElementById('proxiesTableBody').innerHTML = state.proxies.map(p => `
        <tr class="hover:bg-slate-900/60 transition-colors">
          <td class="px-4 py-3 font-bold text-white">${p.name}</td>
          <td class="px-4 py-3"><span class="px-2 py-0.5 rounded bg-purple-500/10 text-purple-400 border border-purple-500/20 text-[10px]">${p.type}</span></td>
          <td class="px-4 py-3 text-slate-300">${p.host}:${p.port}</td>
          <td class="px-4 py-3 text-slate-400">${p.auth}</td>
          <td class="px-4 py-3 text-cyan-400">${p.latency}</td>
          <td class="px-4 py-3 text-right">
            <button onclick="deleteProxy('${p.id}')" class="text-red-400 hover:text-red-300"><i data-lucide="trash-2" class="w-4 h-4 inline"></i></button>
          </td>
        </tr>
      `).join('');

      document.getElementById('automationsTableBody').innerHTML = state.automations.map(au => `
        <tr class="hover:bg-slate-900/60 transition-colors">
          <td class="px-4 py-3">
            <button onclick="toggleAutomation('${au.id}')" class="px-2 py-0.5 rounded text-[10px] font-bold ${au.status ? 'bg-emerald-500/10 text-emerald-400 border border-emerald-500/20' : 'bg-slate-800 text-slate-500'}">
              ${au.status ? 'ACTIVE' : 'PAUSED'}
            </button>
          </td>
          <td class="px-4 py-3 font-semibold text-white">${au.msg}</td>
          <td class="px-4 py-3 text-cyan-300 font-mono">${au.interval}</td>
          <td class="px-4 py-3 text-slate-400">${au.scope}</td>
          <td class="px-4 py-3 text-right">
            <button onclick="deleteAutomation('${au.id}')" class="text-red-400 hover:text-red-300"><i data-lucide="trash-2" class="w-4 h-4 inline"></i></button>
          </td>
        </tr>
      `).join('');

      document.getElementById('triggersTableBody').innerHTML = state.triggers.map(tr => `
        <tr class="hover:bg-slate-900/60 transition-colors">
          <td class="px-4 py-3">
            <button onclick="toggleTrigger('${tr.id}')" class="px-2 py-0.5 rounded text-[10px] font-bold ${tr.status ? 'bg-emerald-500/10 text-emerald-400 border border-emerald-500/20' : 'bg-slate-800 text-slate-500'}">
              ${tr.status ? 'ENABLED' : 'DISABLED'}
            </button>
          </td>
          <td class="px-4 py-3 font-bold text-white">${tr.name}</td>
          <td class="px-4 py-3 text-mc-diamond"><code class="bg-slate-900 px-1.5 py-0.5 rounded">${tr.keyword}</code> (${tr.mode})</td>
          <td class="px-4 py-3 text-slate-300">${tr.reply}</td>
          <td class="px-4 py-3 text-slate-400">${tr.cooldown}s</td>
          <td class="px-4 py-3 text-right">
            <button onclick="deleteTrigger('${tr.id}')" class="text-red-400 hover:text-red-300"><i data-lucide="trash-2" class="w-4 h-4 inline"></i></button>
          </td>
        </tr>
      `).join('');

      document.getElementById('logsTableBody').innerHTML = state.logs.map(l => `
        <tr class="hover:bg-slate-900/60 transition-colors">
          <td class="px-4 py-3 text-slate-500">${l.time}</td>
          <td class="px-4 py-3 text-mc-diamond">${l.instance}</td>
          <td class="px-4 py-3"><span class="px-1.5 py-0.5 rounded bg-cyan-500/10 text-cyan-300 border border-cyan-500/20 text-[10px]">${l.event}</span></td>
          <td class="px-4 py-3 text-white font-bold">${l.player}</td>
          <td class="px-4 py-3 text-slate-400">${l.details}</td>
        </tr>
      `).join('');

      document.getElementById('discordRelayFeed').innerHTML = state.discordRelay.map(d => `
        <div class="p-2.5 rounded-lg bg-slate-900/90 border border-mc-border/60">
          <div class="flex items-center justify-between text-[10px] text-slate-500 mb-1">
            <span class="font-bold text-indigo-400">${d.author}</span>
            <span>${d.time}</span>
          </div>
          <p class="text-slate-300">${d.content}</p>
        </div>
      `).join('');

      document.getElementById('statAccountsCount').innerText = state.accounts.length;
      document.getElementById('statServersCount').innerText = state.servers.length;
      document.getElementById('statProxiesCount').innerText = state.proxies.length;
      document.getElementById('statTriggersCount').innerText = state.triggers.length;

      lucide.createIcons();
    }

    function renderChatFeed() {
      const html = state.chatLogs.map(m => {
        let tagColor = 'text-cyan-400';
        if (m.type === 'bot') tagColor = 'text-emerald-400 font-bold';
        if (m.type === 'system') tagColor = 'text-amber-400 font-bold';

        return `
          <div class="flex items-start space-x-2 leading-relaxed animate-fade-in">
            <span class="text-slate-600">[${m.time}]</span>
            <span class="${tagColor}">${m.tag} ${m.player}:</span>
            <span class="text-slate-200">${m.msg}</span>
          </div>
        `;
      }).join('');

      const dConsole = document.getElementById('dashboardChatConsole');
      const fConsole = document.getElementById('fullChatConsole');
      if (dConsole) {
        dConsole.innerHTML = html;
        dConsole.scrollTop = dConsole.scrollHeight;
      }
      if (fConsole) {
        fConsole.innerHTML = html;
        fConsole.scrollTop = fConsole.scrollHeight;
      }
    }

    function switchTab(tabId) {
      state.activeTab = tabId;
      document.querySelectorAll('.tab-content').forEach(el => el.classList.add('hidden'));
      const target = document.getElementById('tab-' + tabId);
      if (target) target.classList.remove('hidden');

      document.querySelectorAll('.nav-btn').forEach(btn => {
        btn.className = 'nav-btn px-3.5 py-2 rounded-lg text-sm font-medium transition-all duration-200 flex items-center space-x-2 text-slate-400 hover:text-white hover:bg-slate-800/60';
      });
      const activeBtn = document.getElementById('nav-' + tabId);
      if (activeBtn) {
        activeBtn.className = 'nav-btn px-3.5 py-2 rounded-lg text-sm font-medium transition-all duration-200 flex items-center space-x-2 text-mc-diamond bg-mc-diamond/10 border border-mc-diamond/30 shadow-sm';
      }
      lucide.createIcons();
    }

    function switchInstance(id) {
      state.activeInstanceId = id;
      renderInstanceTabs();
    }

    function addNewInstance() {
      const nextId = state.instances.length + 1;
      state.instances.push({
        id: nextId,
        name: 'Instance ' + nextId,
        status: 'online',
        account: state.accounts[0] ? state.accounts[0].username : 'PieBot_' + nextId,
        server: state.servers[0] ? state.servers[0].name : 'Hypixel Network',
        proxy: 'Auto'
      });
      state.activeInstanceId = nextId;
      renderInstanceTabs();
      spawnSparkles(window.innerWidth / 2, window.innerHeight / 2, '#2cf5d6');
    }

    function toggleActiveBot() {
      const inst = state.instances.find(i => i.id === state.activeInstanceId);
      if (inst) {
        inst.status = inst.status === 'online' ? 'offline' : 'online';
        renderInstanceTabs();
        addLog(inst.name, inst.status === 'online' ? 'Bot Started' : 'Bot Stopped', 'SYSTEM', `Bot toggled to ${inst.status}`);
      }
    }

    function restartActiveBot() {
      const inst = state.instances.find(i => i.id === state.activeInstanceId);
      if (inst) {
        inst.status = 'offline';
        renderInstanceTabs();
        setTimeout(() => {
          inst.status = 'online';
          renderInstanceTabs();
          addLog(inst.name, 'Bot Restarted', 'SYSTEM', 'Re-established TCP connection & verified SSID');
        }, 800);
      }
    }

    function sendChatMessage(e) {
      e.preventDefault();
      const input = document.getElementById('dashboardChatInput');
      const val = input.value.trim();
      if (!val) return;
      transmitChat(val);
      input.value = '';
    }

    function sendFullChatMessage(e) {
      e.preventDefault();
      const input = document.getElementById('fullChatInput');
      const val = input.value.trim();
      if (!val) return;
      transmitChat(val);
      input.value = '';
    }

    function transmitChat(msg) {
      const now = new Date().toTimeString().split(' ')[0];
      const inst = state.instances.find(i => i.id === state.activeInstanceId) || state.instances[0];
      state.chatLogs.push({
        time: now,
        player: inst.account,
        tag: '[BOT]',
        msg: msg,
        type: 'bot'
      });
      renderChatFeed();

      state.triggers.forEach(tr => {
        if (tr.status && msg.toLowerCase().includes(tr.keyword.toLowerCase())) {
          setTimeout(() => {
            const replyNow = new Date().toTimeString().split(' ')[0];
            state.chatLogs.push({
              time: replyNow,
              player: inst.account,
              tag: '[BOT/TRIGGER]',
              msg: tr.reply.replace('{player}', inst.account),
              type: 'bot'
            });
            renderChatFeed();
            addLog(inst.name, 'Trigger Fired', inst.account, `Matched [${tr.keyword}]`);
          }, 600);
        }
      });
    }

    function insertCommand(cmd) {
      const input = document.getElementById('fullChatInput');
      input.value = cmd;
      input.focus();
    }

    function clearChatLogs() {
      state.chatLogs = [];
      renderChatFeed();
    }

    function addLog(instance, event, player, details) {
      const now = new Date().toTimeString().split(' ')[0];
      state.logs.unshift({ time: now, instance, event, player, details });
      renderTables();
    }

    function openModal(id) {
      const el = document.getElementById(id);
      if (el) {
        el.classList.remove('hidden');
        el.classList.add('flex');
      }
    }
    function closeModal(id) {
      const el = document.getElementById(id);
      if (el) {
        el.classList.add('hidden');
        el.classList.remove('flex');
      }
    }

    function submitLinkAccount() {
      const user = document.getElementById('newAccUsername').value.trim() || 'PiePlayer_' + Math.floor(Math.random()*900+100);
      const token = document.getElementById('newAccToken').value.trim();
      const newAcc = {
        id: String(Date.now()),
        username: user,
        uuid: 'd' + Math.random().toString(16).substring(2, 10) + '-4a11-98bc',
        status: 'authenticated',
        added: new Date().toISOString().split('T')[0]
      };
      state.accounts.push(newAcc);
      closeModal('linkAccountModal');
      renderTables();
      renderDashboardControls();
      addLog('Global', 'Account Linked', user, 'SSID encrypted via AES-256-GCM');
    }

    function submitAddServer() {
      const name = document.getElementById('newServerName').value.trim() || 'Custom MC Server';
      const host = document.getElementById('newServerHost').value.trim() || '127.0.0.1';
      const port = parseInt(document.getElementById('newServerPort').value) || 25565;
      state.servers.push({
        id: String(Date.now()),
        name, host, port,
        players: '1/50', ping: '12ms', status: 'online'
      });
      closeModal('addServerModal');
      renderTables();
      renderDashboardControls();
    }

    function submitAddProxy() {
      const name = document.getElementById('newProxyName').value.trim() || 'Custom Proxy';
      const type = document.getElementById('newProxyType').value;
      const host = document.getElementById('newProxyHost').value.trim() || '1.1.1.1';
      const port = parseInt(document.getElementById('newProxyPort').value) || 1080;
      state.proxies.push({
        id: String(Date.now()),
        name, type, host, port, auth: 'None', latency: '35ms'
      });
      closeModal('addProxyModal');
      renderTables();
    }

    function submitImportProxies() {
      const lines = document.getElementById('importProxiesText').value.trim().split('\n');
      lines.forEach((line, i) => {
        if (line.trim()) {
          const parts = line.trim().split(':');
          state.proxies.push({
            id: String(Date.now() + i),
            name: 'Imported Node #' + (state.proxies.length + 1),
            type: 'SOCKS5',
            host: parts[0] || '127.0.0.1',
            port: parts[1] ? parseInt(parts[1]) : 1080,
            auth: parts[2] ? `${parts[2]}:${parts[3] || ''}` : 'None',
            latency: '40ms'
          });
        }
      });
      closeModal('importProxiesModal');
      renderTables();
    }

    function submitNewAutomation() {
      const msg = document.getElementById('newAutoMsg').value.trim() || '/help';
      const interval = document.getElementById('newAutoInterval').value + ' ' + document.getElementById('newAutoUnit').value;
      state.automations.push({
        id: String(Date.now()),
        msg, interval, status: true, scope: 'Instance ' + state.activeInstanceId
      });
      closeModal('newAutomationModal');
      renderTables();
    }

    function submitNewTrigger() {
      const name = document.getElementById('newTriggerName').value.trim() || 'Auto Trigger';
      const keyword = document.getElementById('newTriggerKeyword').value.trim() || '!ping';
      const mode = document.getElementById('newTriggerMode').value;
      const cooldown = parseInt(document.getElementById('newTriggerCooldown').value) || 10;
      const reply = document.getElementById('newTriggerReply').value.trim() || 'Pong!';
      state.triggers.push({
        id: String(Date.now()),
        name, keyword, mode, cooldown, reply, status: true
      });
      closeModal('newTriggerModal');
      renderTables();
    }

    function deleteAccount(id) { state.accounts = state.accounts.filter(a => a.id !== id); renderTables(); renderDashboardControls(); }
    function deleteServer(id) { state.servers = state.servers.filter(s => s.id !== id); renderTables(); renderDashboardControls(); }
    function deleteProxy(id) { state.proxies = state.proxies.filter(p => p.id !== id); renderTables(); }
    function deleteAutomation(id) { state.automations = state.automations.filter(a => a.id !== id); renderTables(); }
    function deleteTrigger(id) { state.triggers = state.triggers.filter(t => t.id !== id); renderTables(); }
    function toggleAutomation(id) { const a = state.automations.find(x => x.id === id); if (a) { a.status = !a.status; renderTables(); } }
    function toggleTrigger(id) { const t = state.triggers.find(x => x.id === id); if (t) { t.status = !t.status; renderTables(); } }

    // =========================================================================
    // MINECRAFT SWORD CLICK & TRAIL PARTICLES
    // =========================================================================
    const canvas = document.getElementById('fx-canvas');
    const ctx = canvas.getContext('2d');
    let particles = [];

    function resizeCanvas() {
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
    }
    window.addEventListener('resize', resizeCanvas);
    resizeCanvas();

    class Sparkle {
      constructor(x, y, color = '#2cf5d6', size = 3, vx, vy) {
        this.x = x;
        this.y = y;
        this.color = color;
        this.size = size;
        this.vx = vx !== undefined ? vx : (Math.random() - 0.5) * 4;
        this.vy = vy !== undefined ? vy : (Math.random() - 0.5) * 4;
        this.life = 1;
        this.decay = Math.random() * 0.03 + 0.02;
        this.isSquare = Math.random() > 0.4;
      }
      update() {
        this.x += this.vx;
        this.y += this.vy;
        this.life -= this.decay;
      }
      draw(c) {
        c.save();
        c.globalAlpha = Math.max(0, this.life);
        c.fillStyle = this.color;
        if (this.isSquare) {
          c.fillRect(this.x - this.size/2, this.y - this.size/2, this.size, this.size);
        } else {
          c.beginPath();
          c.arc(this.x, this.y, this.size, 0, Math.PI * 2);
          c.fill();
        }
        c.restore();
      }
    }

    function spawnSparkles(x, y, color = '#2cf5d6', count = 12) {
      for (let i = 0; i < count; i++) {
        const speed = Math.random() * 6 + 2;
        const angle = Math.random() * Math.PI * 2;
        particles.push(new Sparkle(
          x, y,
          Math.random() > 0.5 ? '#2cf5d6' : (Math.random() > 0.5 ? '#55ffff' : '#ffffff'),
          Math.random() * 4 + 2,
          Math.cos(angle) * speed,
          Math.sin(angle) * speed
        ));
      }
    }

    let lastX = 0, lastY = 0;
    window.addEventListener('mousemove', (e) => {
      const dist = Math.hypot(e.clientX - lastX, e.clientY - lastY);
      if (dist > 15) {
        particles.push(new Sparkle(e.clientX, e.clientY, '#2cf5d6', Math.random() * 3 + 1, (Math.random()-0.5)*0.8, (Math.random()-0.5)*0.8));
        lastX = e.clientX;
        lastY = e.clientY;
      }
    });

    window.addEventListener('click', (e) => {
      spawnSparkles(e.clientX, e.clientY, '#2cf5d6', 16);
      for (let i = 0; i < 6; i++) {
        particles.push(new Sparkle(e.clientX, e.clientY, '#55ff55', 4, (Math.random() - 0.5) * 8, (Math.random() - 0.5) * 8));
      }
    });

    function loopFx() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      for (let i = particles.length - 1; i >= 0; i--) {
        const p = particles[i];
        p.update();
        p.draw(ctx);
        if (p.life <= 0) particles.splice(i, 1);
      }
      requestAnimationFrame(loopFx);
    }
    loopFx();

    window.addEventListener('DOMContentLoaded', () => {
      renderInstanceTabs();
      renderTables();
      renderChatFeed();
      lucide.createIcons();
    });
  </script>
</body>
</html>
'''

with open('/working_dir/c_37017e0a3b8a7bd1/pie-mc/public/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Generated frontend index.html successfully!")
