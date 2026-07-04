<div align="center">

# 🐙 open-tgtylab

> One-click security research toolkit

150+ MCP tools · 208 knowledge base articles · 15 automated pipelines · 9 reverse engineering tools auto-download

[![License: GPL-3.0](https://img.shields.io/badge/License-GPL--3.0-red.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux%20%7C%20WSL-blue.svg)]()
[![MCP Tools](https://img.shields.io/badge/MCP_Tools-150+-9cf.svg)]()
[![Knowledge Base](https://img.shields.io/badge/KB-208%20Articles-brightgreen.svg)]()
[![Pipelines](https://img.shields.io/badge/CTF_Pipelines-15-orange.svg)]()

</div>

---

> [中文版](README.zh.md)

## Features

- 🔧 150+ MCP automation tools (PE reverse / Android / CTF / Crypto / Debug)
- 📚 208 technical articles (Web / APK / PE / Crypto / Game Security)
- 🔄 15 CTF pipelines (Full chain / 24h unattended / Attack router / Specialized)
- 🛠 9 reverse engineering tools auto-download (Ghidra / Cutter / x64dbg / DiE / PE-bear / Procmon / nmap / apktool / jadx)
- 🖥 Multi-platform (Windows / macOS / Linux / WSL)
- 💾 Auto-backup existing configuration
- ✅ One-click deploy, auto-detect all config directories

## Quick Start

### Windows

Double-click `启动.bat`.

### macOS

```bash
chmod +x tgtylab-files/install.sh
./tgtylab-files/install.sh
```

### Linux

```bash
chmod +x tgtylab-files/linux-install.sh
./tgtylab-files/linux-install.sh
```

### Usage

After deployment, **open the `Open-tgtylab` directory in your AI tool**:

- **Claude Code**: `cd Open-tgtylab` before starting the session
- **Codex App**: open the `Open-tgtylab` folder directly
- **Hermes / OpenCode**: auto-configured, restart to apply

> ⚠️ You must use the tool from inside the `Open-tgtylab` directory. MCP tools and knowledge base paths are relative to the project root.

## Routing

```
Signal → kb_router(board=) → kb_read_file → Technique → MCP tool mapping → Execution
```

| Signal Type | Board | KB Categories / Files | MCP Tool Family |
|---|---|---|---|
| HTTP/Web/API/CVE/Cloud | `ctf-website` | 26/118 | `http_probe` `run_ctf_tool` `kb_router` |
| APK/DEX/SO/Frida/Java | `apk-reverse` | 8/20 | `android_app_baseline` `android_crypto_unpack_recipe` `android_frida_*` |
| PE/x64/x86/malware/driver | `pe-reverse` | 9/22 | `triage_pe` `ghidra_headless_analyze` `make_x64dbg_breakpoint_script` `sample_full_workup` |
| Crypto/Protocol/Cheat/IoT/Radio | `general` | 5/17 | `die_scan` `ghidra_*` `rizin_*` `python_re_tool_*` |

## Knowledge Base

```
kb/
├── ctf-website/techniques/   26 categories, 118 articles — Full web attack surface
├── apk-reverse/techniques/    8 categories,  20 articles — APK/DEX reverse engineering
├── pe-reverse/techniques/     9 categories,  22 articles — PE binary analysis
├── general/techniques/        5 categories,  17 articles — Cryptography / Protocols / Kernel / Cheating
└── windows/techniques/        1 category,     2 articles — Windows security
```

## Directory Convention

```
samples/      → Original samples + _quarantine/ + unpacked/
exports/      → Tool outputs
patches/      → Patch artifacts
notes/        → Analysis notes
reports/      → Final reports
scripts/      → Automation scripts
kb/           → Knowledge base
tools/        → Toolchain
cases/        → Lightweight index
```

## System Requirements

| Dependency | Version | Notes |
|------------|---------|-------|
| **OS** | Windows 10/11 / macOS 12+ / Linux | WSL auto-detected |
| **Python** | 3.11+ | MCP tool runtime |
| **Git** | Any | Clone the project |
| **PowerShell** | 5.1+ (Windows) | Deploy scripts |
| **uv** | Any | Python package manager (auto-installed) |

| AI Tool | Status |
|---------|--------|
| Claude Code | ✅ Full support |
| Codex App | ✅ Full support |
| Hermes | ✅ Full support |
| OpenCode | ✅ Full support |

| Compatibility | Status |
|---------------|--------|
| Windows 11 / 10 / 8 / 7 | ✅ |
| WSL (Ubuntu/Debian) | ✅ Auto-detected |
| macOS 12+ | ✅ |
| Linux (Ubuntu/Debian/Arch) | ✅ |
| Non-ASCII paths | ✅ |
| Spaces in paths | ✅ |
| Non-admin | ✅ |

## Other Operations

| Action | Windows | macOS / Linux |
|--------|---------|---------------|
| Uninstall | Double-click `卸载.bat` | `./tgtylab-files/uninstall.sh` |
| Verify | Double-click `验证.bat` | Check `~/.claude/CLAUDE.md` exists |
| Restore | Double-click `恢复备份.bat` | Copy `~/.claude/backups/tgtylab-*` |

## File Structure

```
open-tgtylab/
├── 启动.bat                       Windows one-click deploy
├── 启动.command                   macOS one-click deploy
├── 卸载.bat / 验证.bat / 恢复备份.bat
├── tgtylab-files/
│   ├── deploy.ps1                 Windows deploy engine
│   ├── install_tools.ps1          Reverse engineering tool downloader
│   ├── install.sh / linux-install.sh / uninstall.sh
│   └── config-bundle/
│       ├── CLAUDE.md              Research protocol (562 examples)
│       └── system-prompt.md       System prompt
├── tools/
│   ├── ctf-website/               CTF tools + wordlists + payloads
│   ├── skills/mcp/                MCP Server (150+ tools)
│   ├── common/                    Ghidra (auto-download)
│   ├── windows/                   x64dbg/DiE/PE-bear/Procmon (auto-download)
│   └── android/                   apktool/jadx (auto-download)
├── kb/                            Knowledge base (208 articles)
├── .claude/                       Claude Code config + pipelines + skills
├── .codex/                        Codex config
├── AGENTS.md                      Agent protocol
├── AI-USAGE.md                    Task routing
├── codex-files/                   Codex config template
├── hermes-files/                  Hermes config
└── opencode-files/                OpenCode config
```

## License

GPL-3.0-only. See [LICENSE](LICENSE) for details.

## Disclaimer

This project is for educational and research purposes only. Users are solely responsible for any consequences arising from the use of this project.
