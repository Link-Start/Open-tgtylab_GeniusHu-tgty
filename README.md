<div align="center">

# 🐙 open-tgtylab

**一键部署的安全研究工具包**

150+ MCP 工具 · 208 篇知识库 · 15 条自动化流水线

[![License: GPL-3.0](https://img.shields.io/badge/License-GPL--3.0-red.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-blue.svg)]()
[![MCP Tools](https://img.shields.io/badge/MCP%20Tools-150+-purple.svg)]()
[![Knowledge Base](https://img.shields.io/badge/KB-208%20Articles-green.svg)]()

</div>

---

## 一句话

双击 `启动.bat`，你的 AI 工具就变成一个有 150+ 工具、208 篇知识库、15 条流水线的安全研究平台。

## 支持的 AI 工具

| 工具 | 支持 |
|------|------|
| Claude Code | ✅ |
| Codex App | ✅ |
| Hermes | ✅ |
| OpenCode | ✅ |

## 快速开始

```
git clone https://github.com/GeniusHu-tgty/Open-tgtylab.git
cd Open-tgtylab
双击 启动.bat
```

启动.bat 会自动：
- 部署配置到所有 AI 工具
- 下载 9 个逆向工具（Ghidra/x64dbg/DiE/...）
- 安装 MCP 依赖
- 安装 Python RE 库

## 你得到了什么

### 工具（150+）

逆向工程、二进制分析、APK 逆向、Web 安全、加密分析、游戏安全、内核调试、恶意软件分析、自动化 CTF —— 全部通过 MCP 工具一键调用。

### 知识库（208 篇）

| 板块 | 篇数 | 覆盖 |
|------|------|------|
| Web 安全 | 118 | JWT/SQLi/XSS/SSRF/CVE/云/DoS/OAuth |
| PE 逆向 | 22 | 壳分析/AOB/脱壳/TLS/YARA |
| Android | 20 | Frida/IL2CPP/加密/JNI/脱壳 |
| 通用 | 17 | 密码学/协议/内核/游戏安全 |
| Windows | 2 | 注入/配置安全 |

### 流水线（15 条）

| 流水线 | 做什么 |
|--------|--------|
| 全链路 | 资产发现 → 漏洞扫描 → PoC 验证 → 报告 |
| 24h 舰队 | 批量目标自动循环攻击 |
| 24h 单轮 | 无人值守循环 |
| 攻击路由 | 自动选择攻击路径 |
| 专项攻击 | 注入/认证/侦察/客户端/SSRF/API/CVE/DoS |

### 逆向工具（自动下载）

Ghidra · Cutter · x64dbg · DiE · PE-bear · Procmon · nmap · apktool · jadx

## 项目结构

```
open-tgtylab/
├── 启动.bat              ← 双击这个
├── 卸载.bat              ← 不想要了双击这个
├── 验证.bat              ← 确认安装成功
├── 恢复备份.bat          ← 恢复原配置
├── tgtylab-files/        ← 部署脚本 + 配置文件
├── tools/                ← MCP Server + CTF 工具 + 逆向工具
├── kb/                   ← 知识库（208 篇）
├── .claude/              ← Claude Code 配置 + 流水线
├── .codex/               ← Codex 配置
├── AGENTS.md             ← Agent 操作协议
├── AI-USAGE.md           ← 任务路由
├── codex-files/          ← Codex 配置模板
├── hermes-files/         ← Hermes 配置
└── opencode-files/       ← OpenCode 配置
```

## 兼容性

| 系统 | ✅ |
|------|---|
| Windows 11/10/8/7 | ✅ |
| WSL | ✅ 自动检测 |
| macOS | ✅ |
| Linux | ✅ |
| 中文路径 | ✅ |
| 空格路径 | ✅ |
| 非管理员 | ✅ |

## 常见问题

**Q: 启动.bat 没反应？**
A: 右键 → 以管理员身份运行。

**Q: 工具不显示？**
A: 重启 AI 工具，确认打开的是 open-tgtylab 目录。

**Q: Defender 报毒？**
A: 误报。把文件夹加到排除项。

**Q: 想恢复原配置？**
A: 双击 `恢复备份.bat`。

## 许可

GPL-3.0 — 详见 [LICENSE](LICENSE)。

## 免责声明

本项目仅供学习交流使用，使用本项目造成的任何后果由使用者自行承担。
