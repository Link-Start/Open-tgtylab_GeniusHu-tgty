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

Each technique file: `Scenario → Input signal → Method → Attack chain → MCP tool mapping`

## Boards

| Board | Trigger Signals |
|---|---|
| `ctf-website` | URL, HTTP, JWT, SQLi, SSRF, CVE, API, CSP, OAuth, CAPTCHA, Cloudflare, ReDoS, DoS |
| `apk-reverse` | APK, DEX, adb, Frida, jadx, smali, SO, native |
| `pe-reverse` | PE, EXE, DLL, x64dbg, Ghidra, Procmon, packer, malware |
| `general` | AES/DES/RSA, protobuf, game cheat, EAC/BE/Vanguard, firmware, JTAG, SDR |

## Directory Convention

```
samples/      → Original samples + _quarantine/ + unpacked/
exports/      → Tool outputs (triage / IOC / YARA / Sigma / Ghidra)
patches/      → Patch artifacts (original samples never modified)
notes/        → Analysis notes
reports/      → Final reports
scripts/      → Automation scripts
kb/           → Reusable knowledge base
tools/        → Toolchain
cases/        → Lightweight index
```

## Installation

Double-click `启动.bat` on Windows, or run `install.sh` on macOS/Linux.

```powershell
git clone https://github.com/GeniusHu-tgty/Open-tgtylab.git
cd Open-tgtylab
启动.bat
```

## Agent Quick Start

1. Clone to a stable local directory.
2. Double-click `启动.bat` (Windows) or run `install.sh` (macOS/Linux).
3. Open the `Open-tgtylab` folder in Claude Code / Codex / Hermes / OpenCode.
4. Verify: double-click `验证.bat`.

## Context Chain

```
CLAUDE.md → AGENTS.md → AI-USAGE.md → kb/<board>/AI-USAGE.md
```

## License

GPL-3.0-only. See [LICENSE](LICENSE) for details.

## Disclaimer

This project is for educational and research purposes only. Users are solely responsible for any consequences arising from the use of this project.
