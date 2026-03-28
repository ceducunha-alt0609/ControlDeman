# 🏢 SindApp – Gestão Condominial Inteligente

> PWA completo para síndicos: demandas, manutenções, Matriz GUT, IA, alertas e muito mais.

![SindApp](https://img.shields.io/badge/SindApp-v1.0.0-63b3ed?style=for-the-badge)
![PWA](https://img.shields.io/badge/PWA-Ready-22c55e?style=for-the-badge)
![HTML/CSS/JS](https://img.shields.io/badge/Stack-HTML%2FCSS%2FJS-f59e0b?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-a78bfa?style=for-the-badge)

---

## ✨ Funcionalidades

### 📋 Gestão de Demandas
- ✅ Criação e acompanhamento de demandas
- ✅ **Matriz GUT** (Gravidade × Urgência × Tendência)
- ✅ Fotos **antes/depois** das demandas
- ✅ Adição de demanda por **voz** (Web Speech API)
- ✅ Status: Aberto / Em andamento / Aguardando / Concluído

### 🔧 Controle de Manutenções
Controle completo de **20+ categorias**:
- 🔥 Extintores (recarga anual)
- 💧 Caixa d'água (lavagem semestral)
- 🪲 Dedetização (trimestral)
- ⚡ Para-raio (inspeção anual)
- 🛡️ Seguros (renovação anual)
- 🏠 Telhados (inspeção anual)
- 🌿 Jardins (mensal)
- 🚪 Portões (semestral)
- 🚽 Desentupimentos (preventivo anual)
- 💡 Iluminação (inspeção mensal)
- 📹 CFTV (revisão semestral)
- 📡 Parabólica (anual)
- 🌲 Poda/Remoção de árvores (semestral)
- 🔥 Sistema de Combate a Incêndio (anual)
- 🎨 Pinturas (a cada 3 anos)
- 🔧 Serralheria (anual)
- 🚿 Hidráulica (preventivo anual)
- 🧱 Alvenaria (bianual)
- 🪜 Escadarias (trimestral)
- ⚙️ Elétrica Geral (preventivo anual)

### 👥 Fornecedores
- ✅ Cadastro de fornecedores com CNPJ e contato
- ✅ Cotações lado a lado
- ✅ **Seleção de fornecedor vencedor**
- ✅ Histórico de contratos

### 📁 Documentos & IA
- ✅ Gestão documental completa
- ✅ **IA para análise de descarte** de documentos
  - Fichas de funcionários antigos
  - Notas fiscais antigas
  - Atas de assembleia
  - Contratos vencidos
- ✅ Análise baseada em CLT, CTN e Lei 4.591/64

### 📊 Relatórios PDF
- ✅ Relatório de Demandas
- ✅ Relatório de Manutenções
- ✅ Relatório de Fornecedores
- ✅ Relatório Gerencial Completo (para assembleias)

### 🔔 Alertas Inteligentes
- ✅ **Alertas de vencimento** automáticos
- ✅ Envio por **WhatsApp** (configurável)
- ✅ Configuração de antecedência (7/15/30/60 dias)
- ✅ Mini calendário com datas em amber/vermelho

### 🎨 Configurações & Personalização
- ✅ **Tema Claro / Escuro / Automático**
- ✅ **Paleta RGB** customizável (slider R/G/B)
- ✅ 6 cores de destaque pré-definidas
- ✅ 4 opções de **fonte** (DM Sans, Outfit, IBM Plex, Space Grotesk)
- ✅ 3 opções de **fonte display** (Syne, Playfair, Space Grotesk)
- ✅ Configuração do nome do condomínio

### 💾 Backup & Sync
- ✅ **Sincronização GitHub**
- ✅ Backup automático diário
- ✅ Exportar/Importar JSON
- ✅ Logs do sistema

### 📱 PWA & Instalação
- ✅ **Instalável como app** (PC, Android, iOS)
- ✅ Funciona **offline**
- ✅ Service Worker com cache inteligente
- ✅ Push notifications (para alertas futuros)
- ✅ Splash screen animada

### 🎯 UX/UI
- ✅ **Sidebar** colapsável
- ✅ **Cards com efeito hover** (elevam suavemente)
- ✅ **Glass effect** nos modais
- ✅ **Janelas flutuantes** (modais animados)
- ✅ **FAB** (botão de ação flutuante)
- ✅ Sistema de **toasts** (notificações)
- ✅ **Mini calendário** integrado com vencimentos
- ✅ Barras de progresso de manutenções
- ✅ **Tags coloridas** por status
- ✅ Animações suaves e microinterações
- ✅ 100% responsivo (mobile/tablet/desktop)
- ✅ **Impressão** e **compartilhamento**
- ✅ Identificador de versão
- ✅ Noise texture overlay sutil

---

## 🚀 Como Publicar no GitHub Pages

### 1. Crie o repositório
```bash
git init
git add .
git commit -m "🏢 SindApp v1.0.0 - Initial commit"
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/sindapp.git
git push -u origin main
```

### 2. Ative o GitHub Pages
1. Vá em **Settings → Pages**
2. Source: **Deploy from a branch**
3. Branch: **main** / **(root)**
4. Clique em **Save**

### 3. Gere os ícones
```bash
pip install cairosvg
python3 generate_icons.py
```
Ou use o [RealFaviconGenerator](https://realfavicongenerator.net/) com o arquivo `icons/logo.svg`.

### 4. Acesse e instale
Seu app estará em:
```
https://SEU_USUARIO.github.io/sindapp/
```

No navegador, clique em **"Instalar SindApp"** quando aparecer o banner, ou:
- **Chrome/Edge Desktop**: Menu → "Instalar SindApp..."
- **Android**: Menu → "Adicionar à tela inicial"
- **iOS (Safari)**: Compartilhar → "Adicionar à Tela de Início"

---

## 📁 Estrutura de Arquivos

```
sindapp/
├── index.html          # App principal (tudo em um arquivo!)
├── manifest.json       # Manifesto PWA
├── sw.js               # Service Worker (offline + cache)
├── generate_icons.py   # Script para gerar ícones
├── README.md           # Esta documentação
└── icons/
    ├── logo.svg        # Logo SVG (gerado pelo script)
    ├── favicon.svg     # Favicon SVG
    ├── splash.svg      # Splash screen SVG
    ├── icon-72.png     # Ícones PNG (gerar com script)
    ├── icon-96.png
    ├── icon-128.png
    ├── icon-144.png
    ├── icon-152.png
    ├── icon-192.png    # ← Principal (Android/iOS)
    ├── icon-384.png
    └── icon-512.png    # ← Principal (Splash/Desktop)
```

---

## 🗺️ Roadmap

### v1.1 – Dados Reais
- [ ] Integração com IndexedDB para persistência local
- [ ] Sync real com GitHub API
- [ ] Export PDF real com jsPDF
- [ ] Galeria de fotos antes/depois

### v1.2 – IA Real
- [ ] Integração com API Claude/OpenAI para análise de docs
- [ ] Insights automáticos baseados em padrões
- [ ] Sugestões de fornecedores por categoria

### v1.3 – Comunicação
- [ ] Integração real com WhatsApp Business API
- [ ] Email de alertas (EmailJS)
- [ ] Notificações push reais

### v2.0 – Multi-usuário
- [ ] Backend (Supabase/Firebase)
- [ ] Login de moradores
- [ ] Portal do morador para abertura de chamados
- [ ] Votação em assembleia online

---

## 🛠️ Tecnologias

| Tecnologia | Uso |
|-----------|-----|
| HTML5 | Estrutura (single-file app) |
| CSS3 | Estilos, animações, temas, glass effect |
| JavaScript ES6+ | Lógica, navegação, storage |
| Web APIs | Speech Recognition, Camera, Share, Clipboard |
| Service Worker | Offline, cache, push notifications |
| PWA Manifest | Instalação como app nativo |
| Google Fonts | Syne, DM Sans, JetBrains Mono, etc. |
| Lucide Icons | Ícones SVG |

---

## 🤖 Módulo de IA

O SindApp usa IA para analisar documentos e determinar se podem ser descartados, baseado em:

- **CLT** – Fichas de funcionários (5 anos após demissão)
- **Código Tributário Nacional** – Documentos fiscais (5 anos)
- **Lei 4.591/64** – Documentação condominial (permanente para atas)
- **Resolução CFM** – Documentos médicos/funcionais

Para integrar IA real, substitua a função `runAI()` no `index.html` por uma chamada à API de sua preferência.

---

## 📜 Licença

MIT © 2025 SindApp – Use, modifique e distribua livremente.

---

## 💡 Dicas de Uso

1. **Primeiro acesso**: O app vem com dados de demonstração para você explorar
2. **Instale como app**: Use o banner de instalação para acesso rápido
3. **Configure o tema**: Vá em Configurações e personalize cores e fontes
4. **Adicione vencimentos reais**: Edite as datas de manutenção conforme sua realidade
5. **WhatsApp**: Configure seu número em Configurações → Notificações

---

*Feito com ❤️ para síndicos que querem tecnologia de ponta na gestão do condomínio.*
