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

> [English version](README.md)

## 这是什么

open-tgtylab 是一个面向安全研究员的 AI Agent 工具包。它把 150+ MCP 工具、208 篇技术知识库、15 条 CTF 自动化流水线、9 个逆向工具打包在一起，通过一个 `启动.bat` 一键部署到你的 AI 工具里。

支持 Claude Code、Codex、Hermes、OpenCode 四个平台，Windows / macOS / Linux / WSL 全覆盖。

## 快速开始

```
git clone https://github.com/GeniusHu-tgty/Open-tgtylab.git
cd Open-tgtylab
双击 启动.bat
```

启动.bat 自动完成：配置部署 → MCP 依赖 → Python RE 库 → 逆向工具下载 → WSL 同步。

## 能力清单

### MCP 工具（150+）

PE/ELF 分析（17）· Ghidra 深度分析（7）· 样本全分析流水线（4）· Android 逆向（28）· 加密/脱壳（6）· CTF 自动化（4）· 知识库查询（3）· 样本管理（7）· 调试脚本（3）· Procmon 动态分析（3）· Python RE 管理（3）· 工具箱管理（4）· 工作区管理（7）· 审计/维护（3）

### 知识库（208 篇）

| 板块 | 篇数 | 覆盖 |
|------|------|------|
| Web 安全 | 118 | JWT/SQLi/XSS/SSRF/CVE/云/DoS/OAuth/GraphQL |
| PE 逆向 | 22 | 壳分析/AOB/脱壳/TLS/YARA |
| Android | 20 | Frida/IL2CPP/加密/JNI/脱壳 |
| 通用安全 | 17 | 密码学/协议/内核/游戏安全 |
| Windows | 2 | 注入/配置安全 |

### CTF 流水线（15 条）

全链路 · 24h 舰队攻击 · 24h 无人值守 · 攻击路由 · 注入/认证/侦察/客户端/SSRF/API/CVE/DoS 专项 · 资产发现 · DoS 评估 · 漏洞挖掘 · PoC 验证

### 逆向工具（自动下载）

Ghidra · Cutter · x64dbg · DiE · PE-bear · Procmon · nmap · apktool · jadx

## 目录约定

```
samples/      → 原始样本 + _quarantine/ + unpacked/
exports/      → 工具输出
patches/      → Patch 产物
notes/        → 分析笔记
reports/      → 最终报告
kb/           → 知识库
tools/        → 工具链
cases/        → 轻量索引
```

## 其他操作

| 操作 | Windows | macOS / Linux |
|------|---------|---------------|
| 卸载 | 双击 `卸载.bat` | `./tgtylab-files/uninstall.sh` |
| 验证 | 双击 `验证.bat` | 检查 `~/.claude/CLAUDE.md` 是否存在 |
| 恢复 | 双击 `恢复备份.bat` | 手动复制 `~/.claude/backups/tgtylab-*` |

## 许可

GPL-3.0-only. 详见 [LICENSE](LICENSE)。

## 免责声明

本项目仅供学习交流使用，使用本项目造成的任何后果由使用者自行承担。
