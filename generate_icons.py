#!/usr/bin/env python3
"""
SindApp – Gerador de Ícones e Splash
Gera todos os ícones PWA necessários em SVG/PNG
Execute: python3 generate_icons.py
"""

import os

# SVG base do logo SindApp
LOGO_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#0a0d12"/>
      <stop offset="100%" style="stop-color:#1a2035"/>
    </linearGradient>
    <linearGradient id="icon" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#63b3ed"/>
      <stop offset="100%" style="stop-color:#3182ce"/>
    </linearGradient>
    <linearGradient id="shine" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#ffffff;stop-opacity:0.3"/>
      <stop offset="100%" style="stop-color:#ffffff;stop-opacity:0"/>
    </linearGradient>
  </defs>

  <!-- Background rounded rect -->
  <rect width="512" height="512" rx="112" ry="112" fill="url(#bg)"/>

  <!-- Subtle grid pattern -->
  <rect width="512" height="512" rx="112" ry="112" fill="none" stroke="#63b3ed" stroke-width="1" stroke-opacity="0.08"/>

  <!-- House / Building icon -->
  <!-- Main building body -->
  <rect x="156" y="220" width="200" height="200" rx="8" fill="url(#icon)" opacity="0.9"/>

  <!-- Roof / triangle -->
  <polygon points="256,80 120,230 392,230" fill="url(#icon)"/>

  <!-- Door -->
  <rect x="218" y="320" width="76" height="100" rx="6" fill="#0a0d12" opacity="0.7"/>

  <!-- Windows -->
  <rect x="170" y="250" width="50" height="45" rx="5" fill="#0a0d12" opacity="0.5"/>
  <rect x="292" y="250" width="50" height="45" rx="5" fill="#0a0d12" opacity="0.5"/>

  <!-- Window shine -->
  <rect x="174" y="254" width="20" height="18" rx="2" fill="#63b3ed" opacity="0.3"/>
  <rect x="296" y="254" width="20" height="18" rx="2" fill="#63b3ed" opacity="0.3"/>

  <!-- Small top accent (síndico star) -->
  <circle cx="256" cy="165" r="16" fill="#f59e0b" opacity="0.9"/>
  <text x="256" y="171" text-anchor="middle" fill="white" font-size="18" font-weight="bold">★</text>

  <!-- Shine overlay -->
  <rect width="512" height="256" rx="112" ry="112" fill="url(#shine)"/>
</svg>"""

# Splash screen SVG
SPLASH_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1242 2688">
  <rect width="1242" height="2688" fill="#0a0d12"/>

  <!-- Subtle background circles -->
  <circle cx="621" cy="1344" r="600" fill="#63b3ed" opacity="0.03"/>
  <circle cx="621" cy="1344" r="400" fill="#63b3ed" opacity="0.04"/>

  <!-- Logo icon centered -->
  <g transform="translate(471, 1144)">
    <rect width="300" height="300" rx="66" fill="#1a2035"/>
    <rect width="300" height="300" rx="66" fill="none" stroke="#63b3ed" stroke-width="1.5" opacity="0.3"/>

    <!-- House -->
    <rect x="75" y="160" width="150" height="110" rx="4" fill="#63b3ed" opacity="0.9"/>
    <polygon points="150,60 50,165 250,165" fill="#63b3ed"/>
    <rect x="112" y="215" width="76" height="55" rx="4" fill="#0a0d12" opacity="0.6"/>
    <rect x="68" y="175" width="45" height="38" rx="3" fill="#0a0d12" opacity="0.4"/>
    <rect x="187" y="175" width="45" height="38" rx="3" fill="#0a0d12" opacity="0.4"/>

    <!-- Star badge -->
    <circle cx="150" cy="120" r="14" fill="#f59e0b"/>
    <text x="150" y="126" text-anchor="middle" fill="white" font-size="16" font-weight="bold">★</text>
  </g>

  <!-- App name -->
  <text x="621" y="1530" text-anchor="middle" fill="#eef1f8" font-family="Arial, sans-serif" font-size="72" font-weight="900" letter-spacing="-2">SindApp</text>
  <text x="621" y="1590" text-anchor="middle" fill="#8892a4" font-family="Arial, sans-serif" font-size="32" letter-spacing="4">GESTÃO CONDOMINIAL</text>

  <!-- Loading bar -->
  <rect x="511" y="1650" width="220" height="3" rx="2" fill="#1a2035"/>
  <rect x="511" y="1650" width="110" height="3" rx="2" fill="#63b3ed"/>
</svg>"""

# Gerar pasta icons
os.makedirs('icons', exist_ok=True)
os.makedirs('screenshots', exist_ok=True)

# Salvar SVGs
with open('icons/logo.svg', 'w') as f:
    f.write(LOGO_SVG)
print("✅ icons/logo.svg gerado")

with open('icons/splash.svg', 'w') as f:
    f.write(SPLASH_SVG)
print("✅ icons/splash.svg gerado")

# Instruções para gerar PNGs
print("""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎨 PARA GERAR OS PNGs (escolha uma opção):

OPÇÃO 1 – Inkscape (recomendado):
  inkscape icons/logo.svg --export-png=icons/icon-512.png --export-width=512
  inkscape icons/logo.svg --export-png=icons/icon-192.png --export-width=192
  inkscape icons/logo.svg --export-png=icons/icon-144.png --export-width=144
  inkscape icons/logo.svg --export-png=icons/icon-96.png --export-width=96
  inkscape icons/logo.svg --export-png=icons/icon-72.png --export-width=72

OPÇÃO 2 – CairoSVG (pip install cairosvg):
  python3 -c "
  import cairosvg
  sizes = [72, 96, 128, 144, 152, 192, 384, 512]
  for s in sizes:
    cairosvg.svg2png(url='icons/logo.svg', write_to=f'icons/icon-{s}.png', output_width=s, output_height=s)
    print(f'✅ icon-{s}.png')
  "

OPÇÃO 3 – Online:
  Acesse https://realfavicongenerator.net/
  Faça upload de icons/logo.svg
  Baixe o pacote completo

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")

# Criar favicon SVG inline (funciona sem PNG!)
FAVICON_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">
  <rect width="32" height="32" rx="7" fill="#1a2035"/>
  <polygon points="16,4 5,14 27,14" fill="#63b3ed"/>
  <rect x="8" y="14" width="16" height="14" rx="2" fill="#63b3ed" opacity="0.8"/>
  <rect x="12" y="19" width="8" height="9" rx="1" fill="#0a0d12" opacity="0.6"/>
  <circle cx="16" cy="10" r="2.5" fill="#f59e0b"/>
</svg>"""

with open('icons/favicon.svg', 'w') as f:
    f.write(FAVICON_SVG)
print("✅ icons/favicon.svg gerado (use diretamente como favicon!)")

print("\n📦 Todos os assets gerados com sucesso!")
print("🚀 Próximos passos:")
print("  1. Gere os PNGs com uma das opções acima")
print("  2. Faça commit no GitHub")
print("  3. Ative o GitHub Pages no repositório")
print("  4. Acesse a URL e instale o PWA!")
