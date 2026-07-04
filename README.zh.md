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

开源安全研究工具包，208 篇知识库，150+ MCP 自动化工具，覆盖 CTF 渗透测试 / APK 逆向 / PE 二进制分析 / 密码学与协议破解 / 游戏安全分析。Agent 原生，目录即约定。

> [English version](README.md)

## 路由

```
信号 → kb_router(board=) → kb_read_file → 技术文档 → MCP 工具映射 → 执行
```

| 信号类型 | Board | KB 分类数/文件数 | MCP 工具族 |
|---------|-------|-----------------|-----------|
| HTTP/Web/API/CVE/Cloud | `ctf-website` | 26/118 | `http_probe` `run_ctf_tool` `kb_router` |
| APK/DEX/SO/Frida/Java | `apk-reverse` | 8/20 | `android_app_baseline` `android_crypto_unpack_recipe` `android_frida_*` |
| PE/x64/x86/malware/driver | `pe-reverse` | 9/22 | `triage_pe` `ghidra_headless_analyze` `make_x64dbg_breakpoint_script` `sample_full_workup` |
| Crypto/Protocol/Cheat/IoT/Radio | `general` | 5/17 | `die_scan` `ghidra_*` `rizin_*` `python_re_tool_*` |

## 知识库

```
kb/
├── ctf-website/techniques/   26 类 118 篇 — Web 安全全覆盖
├── apk-reverse/techniques/    8 类  20 篇 — APK/DEX 逆向
├── pe-reverse/techniques/     9 类  22 篇 — PE 二进制分析
├── general/techniques/        5 类  17 篇 — 密码学/协议/内核/游戏安全/方法论
└── windows/techniques/        1 类   2 篇 — Windows 安全
```

每篇技术文件结构：`场景 → 输入信号 → 方法 → 攻击链 → MCP 工具映射`

Agent 工作流：检测信号 → `kb_router` 查技术 → `kb_read_file` 读取 → 按 MCP 工具映射执行。

## 板块

| 板块 | 触发信号 |
|------|---------|
| `ctf-website` | URL, HTTP, JWT, SQLi, SSRF, CVE, API, CSP, OAuth, CAPTCHA, Cloudflare, ReDoS, DoS |
| `apk-reverse` | APK, DEX, adb, Frida, jadx, smali, SO, native |
| `pe-reverse` | PE, EXE, DLL, x64dbg, Ghidra, Procmon, packer, malware |
| `general` | AES/DES/RSA, protobuf, 游戏安全, EAC/BE/Vanguard, 固件, JTAG, SDR |
| `windows` | 注入技术, 配置安全, Windows 安全 |

## 目录约定

```
samples/      → 原始样本 + _quarantine/ + unpacked/
exports/      → 工具输出（triage/IOC/YARA/Sigma/Procmon/Ghidra summary）
patches/      → Patch 产物（不修改原始样本）
notes/        → 分析笔记
reports/      → 最终报告
scripts/      → 自动化脚本
kb/           → 可复用技术知识库
tools/        → 工具链
cases/        → 轻量索引，不复制大文件
```

## 安装

Windows 用户双击目录下 `启动.bat`，自动检测 Python / uv / Git / `reverse_lab_tools` MCP，创建 wrappers，运行实际 MCP 工具调用，写出 `reports/misc/first-run-report.json`。

```powershell
git clone https://github.com/GeniusHu-tgty/Open-tgtylab.git
cd Open-tgtylab
.\启动.bat                              # 一键部署（配置 + 工具 + MCP + RE 库）
```

## Agent 快速开始

1. Clone 到本地固定目录。
2. Windows：双击 `启动.bat` 完成首次部署。
3. Claude Code：`cd Open-tgtylab` 后启动会话。
4. Codex APP：直接打开 `Open-tgtylab` 文件夹。
5. 每次更换机器或修改 MCP 配置后，重启 AI 工具确认 MCP 工具可用。

## 上下文链

启动时 Agent 沿此链加载上下文：

```
CLAUDE.md → AGENTS.md → AI-USAGE.md → kb/<board>/AI-USAGE.md
```

## 许可

GPL-3.0-only. 详见 [LICENSE](LICENSE)。
