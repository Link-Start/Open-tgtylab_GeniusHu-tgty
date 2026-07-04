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

开源安全研究工具包，支持多 Agent 平台。一键部署到 Claude Code、Codex App、Hermes、OpenCode。208 篇知识库，150+ MCP 自动化工具，覆盖 CTF / APK 逆向 / PE 二进制分析 / 密码学 / 游戏安全。Agent 原生，目录即约定。

> [English version](README.md)

## 多 Agent 支持

| Agent | 配置文件 | 越狱方式 |
|-------|---------|---------|
| **Claude Code** | `CLAUDE.md`（562 示例） | 人格 + few-shot 示例 |
| **Codex App** | `.codex/gpt5.5-unrestricted.md` | 安全研究者人格 + 沙箱上下文 |
| **Hermes** | `hermes-files/SOUL.md` | 人格 + few-shot 示例 |
| **OpenCode** | `opencode-files/prompts/security-operator.txt` | 人格 + few-shot 示例 |

每个 Agent 有独立优化的配置。一个 `启动.bat` 全部部署。

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
├── general/techniques/        5 类  17 篇 — 密码学/协议/内核/游戏安全
└── windows/techniques/        1 类   2 篇 — Windows 安全
```

每篇结构：`场景 → 信号 → 方法 → 攻击链 → MCP 工具映射`

## CTF 流水线（15 条）

| 流水线 | 功能 |
|--------|------|
| `ctf-full-pipeline` | 全链路：资产 → 漏洞 → 验证 → 报告 |
| `ctf-24h-fleet` | 24h 舰队攻击（批量目标自动循环） |
| `ctf-24h-round` | 24h 单轮（无人值守，支持断点恢复） |
| `ctf-attack-router` | 攻击路由器（自动选择攻击路径） |
| `ctf-attack-*` | 专项攻击（注入/认证/侦察/客户端/SSRF/API/CVE/DoS） |
| `ctf-asset-discovery` | 资产发现（6 并行 agent） |
| `ctf-vuln-discovery` | 漏洞挖掘（5 并行 agent） |
| `ctf-vuln-verify` | PoC 验证 |

## 逆向工具（自动下载）

Ghidra · Cutter · x64dbg · DiE · PE-bear · Procmon · nmap · apktool · jadx

## 目录约定

```
samples/      → 原始样本 + _quarantine/ + unpacked/
exports/      → 工具输出（triage/IOC/YARA/Sigma/Ghidra summary）
patches/      → Patch 产物（不修改原始样本）
notes/        → 分析笔记
reports/      → 最终报告
scripts/      → 自动化脚本
kb/           → 可复用技术知识库
tools/        → 工具链
cases/        → 轻量索引，不复制大文件
```

## 安装

```
git clone https://github.com/GeniusHu-tgty/Open-tgtylab.git
cd Open-tgtylab
双击 启动.bat
```

启动.bat 自动完成：配置部署 → MCP 依赖 → Python RE 库 → 逆向工具下载 → WSL 同步。

## Agent 快速开始

1. Clone 到本地固定目录。
2. 双击 `启动.bat`（Windows）或运行 `install.sh`（macOS/Linux）。
3. Claude Code：`cd Open-tgtylab` 后启动会话。
4. Codex App：直接打开 `Open-tgtylab` 文件夹。
5. Hermes / OpenCode：自动配置，重启生效。
6. 验证：双击 `验证.bat` 或检查 `~/.claude/CLAUDE.md` 是否存在。

## 上下文链

```
CLAUDE.md → AGENTS.md → AI-USAGE.md → kb/<board>/AI-USAGE.md
```

## 许可

GPL-3.0-only. 详见 [LICENSE](LICENSE)。

## 免责声明

本项目仅供学习交流使用，使用本项目造成的任何后果由使用者自行承担。
