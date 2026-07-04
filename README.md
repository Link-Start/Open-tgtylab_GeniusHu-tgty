<div align="center">

# 🐙 open-tgtylab

**AI 驱动的安全研究工具包**

150+ MCP 自动化工具 · 208 篇知识库 · 15 条 CTF 流水线 · 全平台部署

[![License: GPL-3.0](https://img.shields.io/badge/License-GPL--3.0-red.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-blue.svg)]()
[![MCP Tools](https://img.shields.io/badge/MCP%20Tools-150+-purple.svg)]()
[![Knowledge Base](https://img.shields.io/badge/KB-208%20Articles-green.svg)]()

</div>

---

为 Claude Code / Codex / Hermes / OpenCode 提供完整安全研究工作流：PE 逆向、APK 分析、Web CTF、漏洞挖掘、恶意软件分析、游戏安全、内核调试。双击即用。

## 快速开始

```
git clone https://github.com/GeniusHu-tgty/Open-tgtylab.git
cd Open-tgtylab
双击 启动.bat
```

启动.bat 自动完成：配置部署 → MCP 工具安装 → Python RE 库 → 逆向工具下载。

## 你能做什么

### PE / ELF 逆向

```
分析这个样本的行为和 IOC
```
→ 自动调用 `sample_full_workup`：triage → Ghidra → 断点 → IOC → YARA

### APK 逆向

```
分析这个 APK 的加密方案和通信接口
```
→ 自动调用 `android_app_baseline` + `android_crypto_unpack_recipe`

### Web CTF

```
对 http://target.example.com 做信息收集和漏洞扫描
```
→ 自动调用 `ctf-full-pipeline`：资产 → DoS → 漏洞 → 验证 → 报告

### 24h 无人值守 CTF

```
对 target1.com target2.com 启动 24h 自动攻击
```
→ 自动调用 `ctf-24h-fleet`：批量目标 → 轮次攻击 → manifest 恢复点

## 工具链

### MCP 工具（150+）

| 类别 | 数量 | 能力 |
|------|------|------|
| PE/ELF 分析 | 17 | triage、Ghidra 反编译、Rizin 反汇编、patch |
| Ghidra 深度分析 | 7 | 函数/导入/字符串查询、call focus |
| 样本全分析 | 4 | 一键：triage → Ghidra → 断点 → IOC → YARA |
| Android 逆向 | 28 | ADB、Frida 注入、私有目录取证、流量观察 |
| CTF 自动化 | 4 | sqlmap/dirsearch/jwt_tool/tplmap |
| 加密/脱壳 | 6 | 自动解密、buffer 提取、PE/DEX carve |
| 其他 | 86 | 知识库、样本管理、Procmon、调试脚本 |

### 知识库（208 篇）

| 板块 | 篇数 | 内容 |
|------|------|------|
| Web 攻击 | ~130 | JWT/SQLi/XSS/SSRF/OAuth/GraphQL/CVE/云/DoS |
| PE 逆向 | ~24 | 壳分析/AOB/断点/脱壳/YARA/TLS |
| Android | ~22 | Frida/IL2CPP/加密/协议/脱壳/JNI |
| 通用 | ~19 | 密码学/协议/游戏安全/内核/方法论 |
| Windows | 2 | 注入/配置安全 |

### CTF 流水线（15 条）

| 流水线 | 功能 |
|--------|------|
| `ctf-full-pipeline` | 全链路：资产 → DoS → 漏洞 → 验证 → 报告 |
| `ctf-24h-fleet` | 24h 舰队攻击（批量目标自动循环） |
| `ctf-24h-round` | 24h 单轮攻击（无人值守循环） |
| `ctf-attack-router` | 攻击路由器（自动选择攻击路径） |
| `ctf-attack-injection` | 注入攻击专项 |
| `ctf-attack-auth` | 认证攻击专项 |
| `ctf-attack-recon` | 侦察专项 |
| `ctf-attack-client` | 客户端攻击专项 |
| `ctf-attack-file_ssrf` | 文件/SSRF 攻击专项 |
| `ctf-attack-api_business` | API 业务逻辑攻击专项 |
| `ctf-attack-cve_cloud_dos` | CVE/云/DoS 攻击专项 |
| `ctf-asset-discovery` | 资产发现（6 并行 agent） |
| `ctf-dos-assessment` | DoS 攻击面评估 |
| `ctf-vuln-discovery` | 漏洞挖掘（5 并行 agent） |
| `ctf-vuln-verify` | 漏洞 PoC 验证 |

### 逆向工具（自动下载）

| 工具 | 用途 |
|------|------|
| Ghidra | 反编译 |
| Cutter + Rizin | 反汇编 |
| x64dbg | 调试器 |
| DiE | 查壳 |
| PE-bear | PE 分析 |
| Procmon | 动态分析 |
| nmap | 端口扫描 |
| apktool | APK 反编译 |
| jadx | APK → Java |

## 使用方式

### Claude Code

打开 `open-tgtylab` 目录，输入 `/mcp` 确认 `reverse_lab_tools` 出现。

### Codex App

打开 `open-tgtylab` 目录，确认 `/mcp` 中有 `reverse_lab_tools`。

### Hermes / OpenCode

自动配置，重启生效。

### WSL

自动检测 WSL 环境，同步部署。

## 项目结构

```
open-tgtylab/
├── 启动.bat                    一键部署
├── 卸载.bat / 验证.bat / 恢复备份.bat
├── tgtylab-files/
│   ├── deploy.ps1              部署引擎（PS 2.0-7.x 兼容）
│   ├── install_tools.ps1       逆向工具下载器（9 个工具）
│   └── config-bundle/          配置文件
├── tools/
│   ├── ctf-website/            CTF 工具 + 字典 + payload
│   ├── skills/mcp/             MCP Server（150+ 工具）
│   ├── common/                 Ghidra（自动下载）
│   ├── windows/                x64dbg/DiE/PE-bear/Procmon（自动下载）
│   └── android/                apktool/jadx（自动下载）
├── kb/                         知识库（208 篇）
├── .claude/                    Claude Code 配置 + 流水线 + skills
├── .codex/                     Codex 配置 + MCP 注册
├── AGENTS.md                   Agent 操作协议（385 行）
├── AI-USAGE.md                 任务路由 + 工作流
├── codex-files/                Codex 配置模板
├── hermes-files/               Hermes 配置
└── opencode-files/             OpenCode 配置
```

## 验证

| 方式 | 操作 |
|------|------|
| Windows | 双击 `验证.bat` |
| macOS/Linux | 检查 `~/.claude/CLAUDE.md` 是否存在 |
| Codex | 输入 `检查 MCP server 健康状态` |

## 卸载

| 平台 | 操作 |
|------|------|
| Windows | 双击 `卸载.bat` |
| macOS | 双击 `卸载.command` |
| Linux | `./tgtylab-files/uninstall.sh` |

## 兼容性

| 系统 | 状态 |
|------|------|
| Windows 11 / 10 / 8 / 7 | ✅ (PowerShell 2.0+) |
| WSL | ✅ 自动检测 |
| macOS 12+ | ✅ |
| Linux | ✅ |
| 中文路径 / 空格路径 | ✅ |
| 非管理员 | ✅ |

## 常见问题

**Q: 双击启动.bat 没反应？**
A: 右键 → 以管理员身份运行。

**Q: MCP 工具不显示？**
A: 确认打开的是 `open-tgtylab` 目录。重启 AI 工具。

**Q: Windows Defender 报毒？**
A: 误报。把项目文件夹加到排除项。

**Q: uv 未找到？**
A: `pip install uv`，然后重启终端。

**Q: 想恢复原配置？**
A: 双击 `恢复备份.bat`。

## 许可

GPL-3.0 — 详见 [LICENSE](LICENSE)。

## 免责声明

本项目仅供学习交流使用，使用本项目造成的任何后果由使用者自行承担。
