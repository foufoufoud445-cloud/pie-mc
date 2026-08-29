import os, re

PUB = '/working_dir/c_37017e0a3b8a7bd1/pie-mc/public'

# 1. UPDATE STYLES.CSS WITH THE CRISP BASE64 CURSOR
styles_css = '''/* ==========================================================================
   PIE MC - AI MINECRAFT SUITE & PREMIUM SAAS DARK THEME
   ========================================================================== */

@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap');

:root {
  --bg-dark: #090b10;
  --bg-card: #0f131d;
  --bg-card-hover: #161b28;
  --bg-input: #0a0d14;
  --border-color: #1c2333;
  --border-glow: rgba(44, 245, 214, 0.4);
  --mc-diamond: #2cf5d6;
  --mc-diamond-glow: rgba(44, 245, 214, 0.25);
  --mc-emerald: #10b981;
  --mc-redstone: #ef4444;
  --mc-gold: #f59e0b;
  --mc-lapis: #3b82f6;
  --text-main: #f1f5f9;
  --text-muted: #94a3b8;
  --text-subtle: #64748b;

  /* Pixel-Perfect Base64 Minecraft Diamond Sword Cursor (Hotspot at exact tip: 0 0) */
  --sword-cursor: url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIzMiIgaGVpZ2h0PSIzMiIgdmlld0JveD0iMCAwIDMyIDMyIiBmaWxsPSJub25lIj4KICA8cmVjdCB4PSIwIiB5PSIwIiB3aWR0aD0iMiIgaGVpZ2h0PSIyIiBmaWxsPSIjMDAwMDAwIi8+CiAgPHJlY3QgeD0iMiIgeT0iMCIgd2lkdGg9IjIiIGhlaWdodD0iMiIgZmlsbD0iIzJjZjVkNiIvPgogIDxyZWN0IHg9IjAiIHk9IjIiIHdpZHRoPSIyIiBoZWlnaHQ9IjIiIGZpbGw9IiMyY2Y1ZDYiLz4KICA8cmVjdCB4PSI0IiB5PSIwIiB3aWR0aD0iMiIgaGVpZ2h0PSIyIiBmaWxsPSIjMDAwMDAwIi8+CiAgPHJlY3QgeD0iMiIgeT0iMiIgd2lkdGg9IjIiIGhlaWdodD0iMiIgZmlsbD0iIzU1ZmZmZiIvPgogIDxyZWN0IHg9IjAiIHk9IjQiIHdpZHRoPSIyIiBoZWlnaHQ9IjIiIGZpbGw9IiMwMDAwMDAiLz4KICAKICA8cmVjdCB4PSI0IiB5PSIyIiB3aWR0aD0iMiIgaGVpZ2h0PSIyIiBmaWxsPSIjMmNmNWQ2Ii8+CiAgPHJlY3QgeD0iMiIgeT0iNCIgd2lkdGg9IjIiIGhlaWdodD0iMiIgZmlsbD0iIzJjZjVkNiIvPgogIDxyZWN0IHg9IjYiIHk9IjIiIHdpZHRoPSIyIiBoZWlnaHQ9IjIiIGZpbGw9IiMwMDAwMDAiLz4KICA8cmVjdCB4PSI0IiB5PSI0IiB3aWR0aD0iMiIgaGVpZ2h0PSIyIiBmaWxsPSIjNTVmZmZmIi8+CiAgPHJlY3QgeD0iMiIgeT0iNiIgd2lkdGg9IjIiIGhlaWdodD0iIzAwMDAwMCIvPgogIAogIDxyZWN0IHg9IjYiIHk9IjQiIHdpZHRoPSIyIiBoZWlnaHQ9IjIiIGZpbGw9IiMyY2Y1ZDYiLz4KICA8cmVjdCB4PSI0IiB5PSI2IiB3aWR0aD0iMiIgaGVpZ2h0PSIyIiBmaWxsPSIjMmNmNWQ2Ii8+CiAgPHJlY3QgeD0iOCIgeT0iNCIgd2lkdGg9IjIiIGhlaWdodD0iMiIgZmlsbD0iIzAwMDAwMCIvPgogIDxyZWN0IHg9IjYiIHk9IjYiIHdpZHRoPSIyIiBoZWlnaHQ9IjIiIGZpbGw9IiM1NWZmZmYiLz4KICA8cmVjdCB4PSI0IiB5PSI4IiB3aWR0aD0iMiIgaGVpZ2h0PSIyIiBmaWxsPSIjMDAwMDAwIi8+CiAgCiAgPHJlY3QgeD0iOCIgeT0iNiIgd2lkdGg9IjIiIGhlaWdodD0iMiIgZmlsbD0iIzJjZjVkNiIvPgogIDxyZWN0IHg9IjYiIHk9IjgiIHdpZHRoPSIyIiBoZWlnaHQ9IjIiIGZpbGw9IiMyY2Y1ZDYiLz4KICA8cmVjdCB4PSIxMCIgeT0iNiIgd2lkdGg9IjIiIGhlaWdodD0iMiIgZmlsbD0iIzAwMDAwMCIvPgogIDxyZWN0IHg9IjgiIHk9IjgiIHdpZHRoPSIyIiBoZWlnaHQ9IjIiIGZpbGw9IiM1NWZmZmYiLz4KICA8cmVjdCB4PSI2IiB5PSIxMCIgd2lkdGg9IjIiIGhlaWdodD0iMiIgZmlsbD0iIzAwMDAwMCIvPgogIAogIDxyZWN0IHg9IjEwIiB5PSI4IiB3aWR0aD0iMiIgaGVpZ2h0PSIyIiBmaWxsPSIjMmNmNWQ2Ii8+CiAgPHJlY3QgeD0iOCIgeT0iMTAiIHdpZHRoPSIyIiBoZWlnaHQ9IjIiIGZpbGw9IiMyY2Y1ZDYiLz4KICA8cmVjdCB4PSIxMiIgeT0iOCIgd2lkdGg9IjIiIGhlaWdodD0iMiIgZmlsbD0iIzAwMDAwMCIvPgogIDxyZWN0IHg9IjEwIiB5PSIxMCIgd2lkdGg9IjIiIGhlaWdodD0iMiIgZmlsbD0iIzU1ZmZmZiIvPgogIDxyZWN0IHg9IjgiIHk9IjEyIiB3aWR0aD0iMiIgaGVpZ2h0PSIyIiBmaWxsPSIjMDAwMDAwIi8+CiAgCiAgPHJlY3QgeD0iMTIiIHk9IjEwIiB3aWR0aD0iMiIgaGVpZ2h0PSIyIiBmaWxsPSIjMmNmNWQ2Ii8+CiAgPHJlY3QgeD0iMTAiIHk9IjEyIiB3aWR0aD0iMiIgaGVpZ2h0PSIyIiBmaWxsPSIjMmNmNWQ2Ii8+CiAgPHJlY3QgeD0iMTQiIHk9IjEwIiB3aWR0aD0iMiIgaGVpZ2h0PSIyIiBmaWxsPSIjMDAwMDAwIi8+CiAgPHJlY3QgeD0iMTIiIHk9IjEyIiB3aWR0aD0iMiIgaGVpZ2h0PSIyIiBmaWxsPSIjNTVmZmZmIi8+CiAgPHJlY3QgeD0iMTAiIHk9IjE0IiB3aWR0aD0iMiIgaGVpZ2h0PSIyIiBmaWxsPSIjMDAwMDAwIi8+CiAgCiAgPHJlY3QgeD0iMTQiIHk9IjEyIiB3aWR0aD0iMiIgaGVpZ2h0PSIyIiBmaWxsPSIjMmNmNWQ2Ii8+CiAgPHJlY3QgeD0iMTIiIHk9IjE0IiB3aWR0aD0iMiIgaGVpZ2h0PSIyIiBmaWxsPSIjMmNmNWQ2Ii8+CiAgPHJlY3QgeD0iMTYiIHk9IjEyIiB3aWR0aD0iMiIgaGVpZ2h0PSIyIiBmaWxsPSIjMDAwMDAwIi8+CiAgPHJlY3QgeD0iMTQiIHk9IjE0IiB3aWR0aD0iMiIgaGVpZ2h0PSIyIiBmaWxsPSIjNTVmZmZmIi8+CiAgPHJlY3QgeD0iMTIiIHk9IjE2IiB3aWR0aD0iMiIgaGVpZ2h0PSIyIiBmaWxsPSIjMDAwMDAwIi8+CgogIDxyZWN0IHg9IjYiIHk9IjE2IiB3aWR0aD0iMiIgaGVpZ2h0PSIyIiBmaWxsPSIjMDAwMDAwIi8+CiAgPHJlY3QgeD0iOCIgeT0iMTQiIHdpZHRoPSIyIiBoZWlnaHQ9IjIiIGZpbGw9IiMwMDAwMDAiLz4KICA8cmVjdCB4PSI4IiB5PSIxNiIgd2lkdGg9IjIiIGhlaWdodD0iMiIgZmlsbD0iIzFjN2I4NSIvPgogIDxyZWN0IHg9IjEwIiB5PSIxNiIgd2lkdGg9IjIiIGhlaWdodD0iMiIgZmlsbD0iIzJjZjVkNiIvPgogIDxyZWN0IHg9IjEyIiB5PSIxOCIgd2lkdGg9IjIiIGhlaWdodD0iMiIgZmlsbD0iIzFjN2I4NSIvPgogIDxyZWN0IHg9IjE0IiB5PSIxNiIgd2lkdGg9IjIiIGhlaWdodD0iMiIgZmlsbD0iIzJjZjVkNiIvPgogIDxyZWN0IHg9IjE2IiB5PSIxNCIgd2lkdGg9IjIiIGhlaWdodD0iMiIgZmlsbD0iIzFjN2I4NSIvPgogIDxyZWN0IHg9IjE2IiB5PSIxNiIgd2lkdGg9IjIiIGhlaWdodD0iMiIgZmlsbD0iIzAwMDAwMCIvPgogIDxyZWN0IHg9IjE4IiB5PSIxMiIgd2lkdGg9IjIiIGhlaWdodD0iMiIgZmlsbD0iIzAwMDAwMCIvPgogIDxyZWN0IHg9IjYiIHk9IjE4IiB3aWR0aD0iMiIgaGVpZ2h0PSIyIiBmaWxsPSIjMDAwMDAwIi8+CiAgPHJlY3QgeD0iMTgiIHk9IjE0IiB3aWR0aD0iMiIgaGVpZ2h0PSIyIiBmaWxsPSIjMDAwMDAwIi8+CgogIDxyZWN0IHg9IjE0IiB5PSIxOCIgd2lkdGg9IjIiIGhlaWdodD0iMiIgZmlsbD0iIzAwMDAwMCIvPgogIDxyZWN0IHg9IjE2IiB5PSIxOCIgd2lkdGg9IjIiIGhlaWdodD0iMiIgZmlsbD0iIzhiNWEyYiIvPgogIDxyZWN0IHg9IjE4IiB5PSIxNiIgd2lkdGg9IjIiIGhlaWdodD0iMiIgZmlsbD0iIzAwMDAwMCIvPgogIAogIDxyZWN0IHg9IjE2IiB5PSIyMCIgd2lkdGg9IjIiIGhlaWdodD0iMiIgZmlsbD0iIzAwMDAwMCIvPgogIDxyZWN0IHg9IjE4IiB5PSIyMCIgd2lkdGg9IjIiIGhlaWdodD0iMiIgZmlsbD0iIzVjM2EyMSIvPgogIDxyZWN0IHg9IjIwIiB5PSIxOCIgd2lkdGg9IjIiIGhlaWdodD0iMiIgZmlsbD0iIzAwMDAwMCIvPgoKICA8cmVjdCB4PSIxOCIgeT0iMjIiIHdpZHRoPSIyIiBoZWlnaHQ9IjIiIGZpbGw9IiMwMDAwMDAiLz4KICA8cmVjdCB4PSIyMCIgeT0iMjIiIHdpZHRoPSIyIiBoZWlnaHQ9IjIiIGZpbGw9IiMyY2Y1ZDYiLz4KICA8cmVjdCB4PSIyMiIgeT0iMjAiIHdpZHRoPSIyIiBoZWlnaHQ9IjIiIGZpbGw9IiMwMDAwMDAiLz4KICA8cmVjdCB4PSIyMCIgeT0iMjQiIHdpZHRoPSIyIiBoZWlnaHQ9IjIiIGZpbGw9IiMwMDAwMDAiLz4KICA8cmVjdCB4PSIyMiIgeT0iMjIiIHdpZHRoPSIyIiBoZWlnaHQ9IjIiIGZpbGw9IiMwMDAwMDAiLz4KPC9zdmc+') 0 0, auto;
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  cursor: var(--sword-cursor) !important;
}

body {
  font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  background-color: var(--bg-dark);
  color: var(--text-main);
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  overflow-x: hidden;
  line-height: 1.5;
}

input, textarea, select {
  font-family: inherit;
  cursor: text !important;
}

button, a, select, [role="button"], label {
  cursor: var(--sword-cursor) !important;
}

/* Custom Scrollbars */
::-webkit-scrollbar {
  width: 6px;
  height: 6px;
}
::-webkit-scrollbar-track {
  background: #090b10;
}
::-webkit-scrollbar-thumb {
  background: #1c2333;
  border-radius: 4px;
}
::-webkit-scrollbar-thumb:hover {
  background: var(--mc-diamond);
}

/* Canvas FX */
#fx-canvas {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  pointer-events: none;
  z-index: 99999;
}

/* Glassmorphic Cards & Panels */
.pie-card {
  background: linear-gradient(135deg, rgba(15, 19, 29, 0.9) 0%, rgba(11, 14, 22, 0.95) 100%);
  backdrop-filter: blur(16px);
  border: 1px solid var(--border-color);
  border-radius: 1rem;
  box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.5);
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
}

.pie-card:hover {
  border-color: rgba(44, 245, 214, 0.35);
  box-shadow: 0 12px 35px -8px rgba(0, 0, 0, 0.6), 0 0 15px -3px rgba(44, 245, 214, 0.15);
}

.pie-card-inner {
  background: rgba(10, 13, 20, 0.85);
  border: 1px solid rgba(28, 35, 51, 0.8);
  border-radius: 0.75rem;
}

/* Sleek Select Dropdown */
.pie-select {
  appearance: none;
  background-color: #0c1018;
  background-image: url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%232cf5d6' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e");
  background-repeat: no-repeat;
  background-position: right 0.75rem center;
  background-size: 1rem;
  padding-right: 2.25rem;
  border: 1px solid var(--border-color);
  color: #fff;
  border-radius: 0.5rem;
  transition: border-color 0.15s ease, box-shadow 0.15s ease;
}

.pie-select:focus {
  outline: none;
  border-color: var(--mc-diamond);
  box-shadow: 0 0 0 1px var(--mc-diamond);
}

/* Sleek Inputs */
.pie-input {
  background-color: #0c1018;
  border: 1px solid var(--border-color);
  color: #fff;
  border-radius: 0.5rem;
  padding: 0.625rem 0.875rem;
  font-size: 0.875rem;
  transition: all 0.15s ease;
}

.pie-input:focus {
  outline: none;
  border-color: var(--mc-diamond);
  box-shadow: 0 0 0 1px var(--mc-diamond);
}

/* Buttons */
.btn-primary {
  background: linear-gradient(135deg, #2cf5d6 0%, #00e0b8 100%);
  color: #000;
  font-weight: 700;
  border-radius: 0.75rem;
  padding: 0.625rem 1.25rem;
  box-shadow: 0 4px 14px 0 rgba(44, 245, 214, 0.35);
  transition: all 0.15s ease;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
}

.btn-primary:hover {
  background: linear-gradient(135deg, #55ffff 0%, #2cf5d6 100%);
  box-shadow: 0 6px 20px 0 rgba(44, 245, 214, 0.5);
  transform: translateY(-1px);
}

.btn-primary:active {
  transform: scale(0.98);
}

.btn-secondary {
  background-color: #161b28;
  color: var(--text-main);
  border: 1px solid var(--border-color);
  font-weight: 600;
  border-radius: 0.75rem;
  padding: 0.625rem 1.25rem;
  transition: all 0.15s ease;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
}

.btn-secondary:hover {
  background-color: #1e2538;
  border-color: rgba(44, 245, 214, 0.4);
  color: #fff;
}

.btn-danger {
  background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
  color: #fff;
  font-weight: 700;
  border-radius: 0.75rem;
  padding: 0.625rem 1.25rem;
  box-shadow: 0 4px 14px 0 rgba(239, 68, 68, 0.3);
  transition: all 0.15s ease;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
}

.btn-danger:hover {
  background: linear-gradient(135deg, #f87171 0%, #ef4444 100%);
  box-shadow: 0 6px 20px 0 rgba(239, 68, 68, 0.45);
}

.btn-danger:active {
  transform: scale(0.98);
}

/* Status Badges */
.badge-online {
  background: rgba(16, 185, 129, 0.15);
  color: #34d399;
  border: 1px solid rgba(16, 185, 129, 0.3);
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.6875rem;
  font-weight: 700;
  padding: 0.2rem 0.5rem;
  border-radius: 0.375rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.badge-offline {
  background: rgba(239, 68, 68, 0.15);
  color: #f87171;
  border: 1px solid rgba(239, 68, 68, 0.3);
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.6875rem;
  font-weight: 700;
  padding: 0.2rem 0.5rem;
  border-radius: 0.375rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.badge-diamond {
  background: rgba(44, 245, 214, 0.12);
  color: #2cf5d6;
  border: 1px solid rgba(44, 245, 214, 0.3);
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.6875rem;
  font-weight: 700;
  padding: 0.2rem 0.5rem;
  border-radius: 0.375rem;
}

/* Nav Link */
.nav-link {
  padding: 0.5rem 0.875rem;
  border-radius: 0.5rem;
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--text-muted);
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.15s ease;
  text-decoration: none;
}

.nav-link:hover {
  color: #fff;
  background-color: rgba(255, 255, 255, 0.05);
}

.nav-link.active {
  color: var(--mc-diamond);
  background-color: rgba(44, 245, 214, 0.12);
  border: 1px solid rgba(44, 245, 214, 0.35);
  box-shadow: 0 0 12px -2px rgba(44, 245, 214, 0.2);
}

@keyframes pulse-glow {
  0%, 100% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7); }
  50% { box-shadow: 0 0 0 6px rgba(16, 185, 129, 0); }
}

.pulse-dot {
  animation: pulse-glow 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}
'''

with open(os.path.join(PUB, 'styles.css'), 'w', encoding='utf-8') as f:
    f.write(styles_css)

# 2. UPDATE SHARED.JS WITH ENHANCED SWORD SLASH ARC AND CRITICAL HIT FX
with open(os.path.join(PUB, 'shared.js'), 'r', encoding='utf-8') as f:
    shared_js = f.read()

# Replace the logo subtitle in header
shared_js = shared_js.replace('Multi-Instance Bot Engine', 'Autonomous AI Platform')
shared_js = shared_js.replace('Multi-Instance Bot Engine & Manager', 'Autonomous AI Platform')

# Replace the Particle Engine with Enhanced Diamond Sword Slash Arc
new_particle_engine = '''// ==========================================
// ENHANCED MINECRAFT SWORD SLASH & PARTICLE FX
// ==========================================
function initParticleCanvas() {
  let canvas = document.getElementById('fx-canvas');
  if (!canvas) {
    canvas = document.createElement('canvas');
    canvas.id = 'fx-canvas';
    document.body.prepend(canvas);
  }

  const ctx = canvas.getContext('2d');
  let particles = [];
  let slashes = [];

  function resizeCanvas() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  }
  window.addEventListener('resize', resizeCanvas);
  resizeCanvas();

  class SwordSlash {
    constructor(x, y) {
      this.x = x;
      this.y = y;
      this.radius = Math.random() * 20 + 35;
      this.startAngle = -Math.PI / 3 - (Math.random() * 0.4);
      this.endAngle = Math.PI / 2 + (Math.random() * 0.4);
      this.life = 1;
      this.decay = 0.08;
      this.color = Math.random() > 0.3 ? '#2cf5d6' : '#55ffff';
    }
    update() {
      this.life -= this.decay;
    }
    draw(c) {
      c.save();
      c.globalAlpha = Math.max(0, this.life);
      c.strokeStyle = this.color;
      c.lineWidth = 3.5 * this.life;
      c.shadowBlur = 12;
      c.shadowColor = '#2cf5d6';
      c.beginPath();
      c.arc(this.x, this.y, this.radius, this.startAngle, this.endAngle);
      c.stroke();
      c.restore();
    }
  }

  class CriticalHitParticle {
    constructor(x, y, color = '#55ff55') {
      this.x = x;
      this.y = y;
      this.color = color;
      this.size = Math.random() * 5 + 3;
      const angle = Math.random() * Math.PI * 2;
      const speed = Math.random() * 6 + 2;
      this.vx = Math.cos(angle) * speed;
      this.vy = Math.sin(angle) * speed;
      this.life = 1;
      this.decay = Math.random() * 0.04 + 0.03;
      this.rotation = Math.random() * Math.PI;
      this.rotSpeed = (Math.random() - 0.5) * 0.2;
    }
    update() {
      this.x += this.vx;
      this.y += this.vy;
      this.vy += 0.15; // Gravity
      this.rotation += this.rotSpeed;
      this.life -= this.decay;
    }
    draw(c) {
      c.save();
      c.globalAlpha = Math.max(0, this.life);
      c.translate(this.x, this.y);
      c.rotate(this.rotation);
      c.fillStyle = this.color;
      c.shadowBlur = 8;
      c.shadowColor = this.color;
      
      // Draw 4-point Minecraft Critical Star
      c.beginPath();
      const s = this.size;
      c.moveTo(-s, 0);
      c.lineTo(0, -s/3);
      c.lineTo(s, 0);
      c.lineTo(0, s/3);
      c.closePath();
      c.fill();
      
      c.beginPath();
      c.moveTo(0, -s);
      c.lineTo(-s/3, 0);
      c.lineTo(0, s);
      c.lineTo(s/3, 0);
      c.closePath();
      c.fill();
      c.restore();
    }
  }

  class Sparkle {
    constructor(x, y, color = '#2cf5d6', size = 3, vx, vy) {
      this.x = x;
      this.y = y;
      this.color = color;
      this.size = size;
      this.vx = vx !== undefined ? vx : (Math.random() - 0.5) * 3;
      this.vy = vy !== undefined ? vy : (Math.random() - 0.5) * 3;
      this.life = 1;
      this.decay = Math.random() * 0.03 + 0.02;
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
      c.fillRect(this.x - this.size/2, this.y - this.size/2, this.size, this.size);
      c.restore();
    }
  }

  window.triggerSwordSlash = function(x, y) {
    slashes.push(new SwordSlash(x, y));
    
    // Critical Hit Stars
    for (let i = 0; i < 8; i++) {
      particles.push(new CriticalHitParticle(x, y, Math.random() > 0.3 ? '#2cf5d6' : '#55ff55'));
    }
    // Diamond Dust Sparkles
    for (let i = 0; i < 10; i++) {
      particles.push(new Sparkle(x, y, '#2cf5d6', Math.random() * 3 + 2));
    }
  };

  let lastX = 0, lastY = 0;
  window.addEventListener('mousemove', (e) => {
    const dist = Math.hypot(e.clientX - lastX, e.clientY - lastY);
    if (dist > 18) {
      particles.push(new Sparkle(e.clientX, e.clientY, '#2cf5d6', Math.random() * 2.5 + 1, (Math.random()-0.5)*0.5, (Math.random()-0.5)*0.5));
      lastX = e.clientX;
      lastY = e.clientY;
    }
  });

  window.addEventListener('click', (e) => {
    window.triggerSwordSlash(e.clientX, e.clientY);
  });

  function loopFx() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    for (let i = slashes.length - 1; i >= 0; i--) {
      const s = slashes[i];
      s.update();
      s.draw(ctx);
      if (s.life <= 0) slashes.splice(i, 1);
    }

    for (let i = particles.length - 1; i >= 0; i--) {
      const p = particles[i];
      p.update();
      p.draw(ctx);
      if (p.life <= 0) particles.splice(i, 1);
    }

    requestAnimationFrame(loopFx);
  }
  loopFx();
}'''

# Replace particle canvas section in shared_js
idx_start = shared_js.find('// Particle Engine')
if idx_start == -1:
    idx_start = shared_js.find('function initParticleCanvas()')
if idx_start != -1:
    idx_end = shared_js.find('window.openModal = function')
    shared_js = shared_js[:idx_start] + new_particle_engine + '\n\n' + shared_js[idx_end:]

with open(os.path.join(PUB, 'shared.js'), 'w', encoding='utf-8') as f:
    f.write(shared_js)

# 3. CLEAN SUBTITLE IN ALL HTML FILES
for fname in os.listdir(PUB):
    if fname.endswith('.html'):
        fpath = os.path.join(PUB, fname)
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace clutter subtitles
        content = content.replace('Multi-Instance Bot Engine & Manager', 'Autonomous AI Platform')
        content = content.replace('Multi-Instance Bot Engine', 'Autonomous AI Platform')
        content = content.replace('Multi-Instance Minecraft Bot Engine', 'Autonomous AI Platform')
        
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)

print("AI-Native Polish & Sword Cursor / Click Slash FX Updated Successfully!")
