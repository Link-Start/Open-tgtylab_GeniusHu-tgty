<div align="center">

# 🐙 open-tgtylab

**一键部署的安全研究工具包**

150+ MCP 工具 · 208 篇知识库 · 15 条自动化流水线

[![License: GPL-3.0](https://img.shields.io/badge/License-GPL--3.0-red.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux%20%7C%20WSL-blue.svg)]()
[![MCP Tools](https://img.shields.io/badge/MCP_Tools-150+-9cf.svg)]()
[![Knowledge Base](https://img.shields.io/badge/KB-208%20Articles-brightgreen.svg)]()
[![Pipelines](https://img.shields.io/badge/CTF_Pipelines-15-orange.svg)]()

</div>

---

Open-source security research toolkit with multi-agent support. One-click deployment to Claude Code, Codex App, Hermes, and OpenCode. 208-article knowledge base, 150+ MCP automation tools, covering CTF / APK reverse engineering / PE binary analysis / cryptography / game security. Agent-native, directory-as-convention.

> [中文版](README.zh.md)

## Multi-Agent Support

| Agent | Config File | Jailbreak Method |
|-------|------------|-----------------|
| **Claude Code** | `CLAUDE.md` (562 examples) | Persona + few-shot examples |
| **Codex App** | `.codex/gpt5.5-unrestricted.md` | Security researcher persona + sandbox context |
| **Hermes** | `hermes-files/SOUL.md` | Persona + few-shot examples |
| **OpenCode** | `opencode-files/prompts/security-operator.txt` | Persona + few-shot examples |

Each agent gets its own optimized configuration. One `启动.bat` deploys all.

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

## CTF Pipelines (15)

| Pipeline | Purpose |
|----------|---------|
| `ctf-full-pipeline` | Full chain: asset discovery → vulnerability scan → PoC verify → report |
| `ctf-24h-fleet` | 24h fleet attack (batch targets, auto loop) |
| `ctf-24h-round` | 24h single-round (unattended loop with checkpoint) |
| `ctf-attack-router` | Attack router (auto-select attack path by target) |
| `ctf-attack-injection` / `auth` / `recon` / `client` / `file_ssrf` / `api_business` / `cve_cloud_dos` | Specialized attack pipelines |
| `ctf-asset-discovery` | Asset discovery (6 parallel agents) |
| `ctf-dos-assessment` | DoS attack surface assessment |
| `ctf-vuln-discovery` | Vulnerability discovery (5 parallel agents) |
| `ctf-vuln-verify` | PoC verification |

## Reverse Engineering Tools (Auto-download)

Ghidra · Cutter · x64dbg · DiE · PE-bear · Procmon · nmap · apktool · jadx

All downloaded automatically by `启动.bat`.

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
cases/        → Lightweight index — no large file copies
```

## Installation

```powershell
git clone https://github.com/GeniusHu-tgty/Open-tgtylab.git
cd Open-tgtylab
双击 启动.bat
```

启动.bat auto-deploys to all agents: config → MCP dependencies → Python RE libs → reverse engineering tools → WSL sync.

## Agent Quick Start

1. Clone to a stable local directory.
2. Double-click `启动.bat` (Windows) or run `install.sh` (macOS/Linux).
3. Claude Code: `cd Open-tgtylab` before starting the session.
4. Codex App: open the `Open-tgtylab` folder directly.
5. Hermes / OpenCode: auto-configured, restart to apply.
6. Verify: double-click `验证.bat` (Windows) or check `~/.claude/CLAUDE.md` exists.

## Context Chain

```
CLAUDE.md → AGENTS.md → AI-USAGE.md → kb/<board>/AI-USAGE.md
```

## License

GPL-3.0-only. See [LICENSE](LICENSE) for details.

## Disclaimer

This project is for educational and research purposes only. Users are solely responsible for any consequences arising from the use of this project.
