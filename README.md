<div align="center">

# 🐙 open-tgtylab

### **AI 安全研究平台**

**Claude Code / Codex / OpenCode / Hermes 的安全研究工具包**

[![License: GPL-3.0](https://img.shields.io/badge/License-GPL--3.0-red.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-blue.svg)]()
[![MCP Tools](https://img.shields.io/badge/MCP%20Tools-150+-purple.svg)]()
[![Knowledge Base](https://img.shields.io/badge/Knowledge%20Base-165%20Articles-green.svg)]()

</div>

---

open-tgtylab 是一套面向安全研究员的 AI Agent 工具包，包含 150+ MCP 工具、165 篇技术知识库、5 条 CTF 自动化流水线、以及完整的安全研究工作流配置。

## 快速开始

### Windows

双击 `启动.bat` 一键部署。

### macOS

```bash
chmod +x tgtylab-files/install.sh && ./tgtylab-files/install.sh
```

### Linux

```bash
chmod +x tgtylab-files/linux-install.sh && ./tgtylab-files/linux-install.sh
```

### 使用方式

部署后用 AI 工具打开 `open-tgtylab` 目录：

- **Claude Code** — 自动读取 `CLAUDE.md` + `.mcp.json`
- **Codex App** — 自动读取 `.codex/config.toml` + `AGENTS.md`
- **Claude Desktop** — 自动写入 `settings.json` 的 `mcpServers`
- **Hermes / OpenCode** — 自动配置

## 能力

### MCP 工具（150+）

| 类别 | 工具数 | 能力 |
|------|--------|------|
| PE/ELF 分析 | 17 | triage、Ghidra 反编译、Rizin 反汇编、patch |
| Ghidra 深度分析 | 7 | 函数/导入/字符串查询、call focus |
| 样本全分析 | 4 | 一键：triage → Ghidra → 断点 → IOC → YARA |
| IOC/检测规则 | 4 | YARA/Sigma 草案生成、IOC 提取 |
| 调试/断点 | 3 | x64dbg 脚本、Procmon 过滤、解密计划 |
| 加密/脱壳 | 6 | 自动解密、buffer 提取、PE/DEX carve |
| Android 逆向 | 28 | ADB、Frida 注入、私有目录取证、流量观察 |
| 知识库 | 3 | 165 篇技术文件，按信号搜索 |
| CTF 自动化 | 4 | sqlmap/dirsearch/jwt_tool/tplmap |
| 样本管理 | 7 | 导入/复制/移动/隔离/删除 |
| Procmon | 3 | 启停抓取、PML 导出 CSV |
| Python RE | 3 | lief/frida/angr/capstone/keystone/unicorn |

### 知识库（165 篇）

| 板块 | 篇数 | 内容 |
|------|------|------|
| ctf-website | 111 | JWT/SQLi/XSS/SSRF/SSTI/OAuth/GraphQL/支付 |
| pe-reverse | 21 | 壳分析/AOB/断点/脱壳/YARA |
| apk-reverse | 19 | Frida/IL2CPP/加密/协议/脱壳 |
| general | 14 | 密码学/协议逆向/游戏安全/方法论 |

### CTF 流水线（5 条）

| 流水线 | 功能 |
|--------|------|
| `ctf-full-pipeline` | 全链路：资产 → DoS → 漏洞 → 验证 → 报告 |
| `ctf-asset-discovery` | 6 并行侦察 agent |
| `ctf-dos-assessment` | DoS 攻击面评估 |
| `ctf-vuln-discovery` | 5 并行漏洞扫描 |
| `ctf-vuln-verify` | PoC 验证 |

### 逆向工具（自动下载）

| 工具 | 用途 | 下载方式 |
|------|------|---------|
| Ghidra | 反编译 | 启动.bat 自动下载 |
| Cutter + Rizin | 反汇编 | 启动.bat 自动下载 |
| x64dbg | 调试器 | 启动.bat 自动下载 |
| DiE | 查壳 | 启动.bat 自动下载 |
| PE-bear | PE 分析 | 启动.bat 自动下载 |
| Procmon | 动态分析 | 启动.bat 自动下载 |
| nmap | 端口扫描 | 启动.bat 自动下载 |
| apktool | APK 反编译 | 启动.bat 自动下载 |
| jadx | APK → Java | 启动.bat 自动下载 |

### CTF 工具（已内置）

| 工具 | 用途 |
|------|------|
| sqlmap | SQL 注入自动化 |
| dirsearch | 目录扫描 |
| jwt_tool | JWT 攻击 |
| tplmap | 模板注入 |
| wordlists | 常用字典 |
| payloads | 常用 payload |

## 部署流程

```
双击 启动.bat
  ├─ 1. 部署配置到 Claude/Codex/Hermes/OpenCode
  ├─ 2. 部署 Skills（逆向工作流）
  ├─ 3. 下载逆向工具（Ghidra/x64dbg/DiE/...）
  ├─ 4. 安装 MCP 依赖（uv sync）
  └─ 5. 安装 Python RE 库（lief/frida/angr/...）
```

## 目录结构

```
open-tgtylab/
├── 启动.bat                      一键部署
├── 卸载.bat                      卸载
├── 验证.bat                      验证部署
├── 恢复备份.bat                  恢复原配置
├── tgtylab-files/
│   ├── deploy.ps1                Windows 部署引擎
│   ├── install_tools.ps1         工具下载器
│   ├── install.sh                macOS 部署
│   └── config-bundle/
│       ├── CLAUDE.md             研究协议（562 示例）
│       └── system-prompt.md      系统提示词
├── tools/
│   ├── ctf-website/              CTF 工具 + 字典 + payload
│   ├── skills/mcp/               MCP Server（150+ 工具）
│   ├── common/                   Ghidra（自动下载）
│   ├── windows/                  x64dbg/DiE/PE-bear/Procmon（自动下载）
│   └── android/                  apktool/jadx（自动下载）
├── kb/                           知识库（165 篇）
├── .claude/
│   ├── hooks/                    MCP 拦截 hook
│   ├── workflows/                CTF 流水线（5 条）
│   └── skills/                   逆向工作流 skill
├── .codex/                       Codex 配置
├── codex-files/                  Codex 配置模板
├── hermes-files/                 Hermes 配置
└── opencode-files/               OpenCode 配置
```

## 兼容性

| 系统 | 状态 |
|------|------|
| Windows 11 | ✅ |
| Windows 10 | ✅ |
| Windows 7/8 | ✅ (PowerShell 2.0+) |
| macOS 12+ | ✅ |
| Linux | ✅ |
| WSL | ✅ 自动检测 |

## 常见问题

**Q: Windows Defender 报毒？**
A: 误报。知识库里的 markdown 文件包含安全技术教学内容。把项目文件夹加到排除项。

**Q: MCP 工具不显示？**
A: 重启 AI 工具。Codex 用户确认打开的是 `open-tgtylab` 目录。

**Q: 想恢复原配置？**
A: 双击 `恢复备份.bat`。

## 许可

GPL-3.0 — 详见 [LICENSE](LICENSE)。
