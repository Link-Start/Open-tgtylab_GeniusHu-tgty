<div align="center">

# 🐙 open-tgtylab

**One-click security research toolkit**

150+ MCP tools · 208 knowledge base articles · 15 automated pipelines

[![License: GPL-3.0](https://img.shields.io/badge/License-GPL--3.0-red.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux%20%7C%20WSL-blue.svg)]()
[![MCP Tools](https://img.shields.io/badge/MCP_Tools-150+-9cf.svg)]()
[![Knowledge Base](https://img.shields.io/badge/KB-208%20Articles-brightgreen.svg)]()
[![Pipelines](https://img.shields.io/badge/CTF_Pipelines-15-orange.svg)]()

</div>

---

> [中文版](README.zh.md)

## What is this

open-tgtylab is an AI Agent toolkit for security researchers. It bundles 150+ MCP tools, 208 technical articles, 15 CTF automation pipelines, and 9 reverse engineering tools into a single package, deployed with one click to your AI tool.

Supports Claude Code, Codex, Hermes, and OpenCode. Works on Windows / macOS / Linux / WSL.

## Quick Start

```
git clone https://github.com/GeniusHu-tgty/Open-tgtylab.git
cd Open-tgtylab
双击 启动.bat
```

启动.bat auto-deploys: config → MCP dependencies → Python RE libs → reverse engineering tools → WSL sync.

## Capabilities

### MCP Tools (150+)

PE/ELF analysis (17) · Ghidra deep analysis (7) · Full sample analysis pipeline (4) · Android reverse (28) · Crypto/unpack (6) · CTF automation (4) · Knowledge base query (3) · Sample management (7) · Debug scripts (3) · Procmon (3) · Python RE (3) · Toolbox (4) · Workspace (7) · Audit (3)

### Knowledge Base (208 articles)

| Board | Articles | Coverage |
|-------|----------|----------|
| Web Security | 118 | JWT/SQLi/XSS/SSRF/CVE/Cloud/DoS/OAuth/GraphQL |
| PE Reverse | 22 | Packing/AOB/Unpack/TLS/YARA |
| Android | 20 | Frida/IL2CPP/Crypto/JNI/Unpack |
| General | 17 | Crypto/Protocol/Kernel/Game Security |
| Windows | 2 | Injection/Config Security |

### CTF Pipelines (15)

Full chain · 24h fleet attack · 24h unattended · Attack router · Injection/Auth/Recon/Client/SSRF/API/CVE/DoS specialized · Asset discovery · DoS assessment · Vuln discovery · PoC verification

### Reverse Engineering Tools (Auto-download)

Ghidra · Cutter · x64dbg · DiE · PE-bear · Procmon · nmap · apktool · jadx

## Directory Convention

```
samples/      → Original samples + _quarantine/ + unpacked/
exports/      → Tool outputs
patches/      → Patch artifacts
notes/        → Analysis notes
reports/      → Final reports
kb/           → Knowledge base
tools/        → Toolchain
cases/        → Lightweight index
```

## Other Operations

| Action | Windows | macOS / Linux |
|--------|---------|---------------|
| Uninstall | Double-click `卸载.bat` | `./tgtylab-files/uninstall.sh` |
| Verify | Double-click `验证.bat` | Check `~/.claude/CLAUDE.md` exists |
| Restore | Double-click `恢复备份.bat` | Manually copy `~/.claude/backups/tgtylab-*` |

## License

GPL-3.0-only. See [LICENSE](LICENSE) for details.

## Disclaimer

This project is for educational and research purposes only. Users are solely responsible for any consequences arising from the use of this project.
