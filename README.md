<div align="center">

# 🐙 open-tgtylab

**AI 驱动的安全研究工具包**

150+ MCP 自动化工具 · 208 篇知识库 · 15 条自动化流水线 · 全平台部署

[![License: GPL-3.0](https://img.shields.io/badge/License-GPL--3.0-red.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-blue.svg)]()
[![MCP Tools](https://img.shields.io/badge/MCP%20Tools-150+-purple.svg)]()
[![Knowledge Base](https://img.shields.io/badge/KB-208%20Articles-green.svg)]()

</div>

---

为 Claude Code / Codex / Hermes / OpenCode 提供完整安全研究工作流：PE 逆向、APK 分析、Web 安全、漏洞研究、恶意软件分析。双击即用。

## 路由

```
信号 → kb_router(board=) → kb_read_file → 技术文档 → MCP 工具映射 → 执行
```

| 信号类型 | 板块 | 知识库 | MCP 工具族 |
|---------|------|--------|-----------|
| HTTP/Web/API/CVE/Cloud | `ctf-website` | 26 类 / 118 篇 | `http_probe` `run_ctf_tool` `kb_router` |
| APK/DEX/SO/Frida/Java | `apk-reverse` | 8 类 / 20 篇 | `android_app_baseline` `android_crypto_unpack_recipe` `android_frida_*` |
| PE/x64/x86/malware/driver | `pe-reverse` | 9 类 / 22 篇 | `triage_pe` `ghidra_headless_analyze` `make_x64dbg_breakpoint_script` `sample_full_workup` |
| Crypto/Protocol/Cheat/IoT | `general` | 5 类 / 17 篇 | `die_scan` `ghidra_*` `rizin_*` `python_re_tool_*` |
| Windows 安全 | `windows` | 1 类 / 2 篇 | `triage_pe` `ghidra_*` |

## 知识库

```
kb/
├── ctf-website/techniques/   26 类 118 篇 — Web 安全全覆盖
├── apk-reverse/techniques/    8 类  20 篇 — APK/DEX 逆向
├── pe-reverse/techniques/     9 类  22 篇 — PE 二进制分析
├── general/techniques/        5 类  17 篇 — 密码学/协议/内核/方法论
└── windows/techniques/        1 类   2 篇 — Windows 安全
```

每篇技术文件结构：`场景 → 输入信号 → 方法 → 攻击链 → MCP 工具映射`

## 板块

| 板块 | 触发信号 |
|------|---------|
| `ctf-website` | URL, HTTP, JWT, SQLi, SSRF, CVE, API, CSP, OAuth, CAPTCHA, Cloudflare, DoS |
| `apk-reverse` | APK, DEX, adb, Frida, jadx, smali, SO, native |
| `pe-reverse` | PE, EXE, DLL, x64dbg, Ghidra, Procmon, packer, malware |
| `general` | AES/DES/RSA, protobuf, game cheat, EAC/BE/Vanguard, firmware, JTAG, SDR |
| `windows` | Notepad++, config injection, Windows security |

## 目录约定

```
samples/      → 原始样本 + _quarantine/ + unpacked/
exports/      → 工具输出（triage/IOC/YARA/Sigma/Procmon/Ghidra）
patches/      → Patch 产物（不修改原始样本）
notes/        → 分析笔记
reports/      → 最终报告
scripts/      → 自动化脚本
kb/           → 可复用知识库
tools/        → 工具链
cases/        → 轻量索引，不复制大文件
```

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

启动.bat 自动完成：配置部署 → MCP 工具安装 → Python RE 库 → 逆向工具下载。

### 验证

| 方式 | 操作 |
|------|------|
| Windows | 双击 `验证.bat` |
| macOS/Linux | 检查 `~/.claude/CLAUDE.md` 是否存在 |

## AI 工具兼容性

| 工具 | 支持 | 说明 |
|------|------|------|
| Claude Code | ✅ | 完整 MCP 工具 + 知识库 |
| Codex App | ✅ | MCP 工具 + 知识库 |
| Hermes | ✅ | 自动配置 |
| OpenCode | ✅ | 自动配置 |
| WSL | ✅ | 自动检测 |

## MCP 工具链（150+）

| 类别 | 数量 | 核心能力 |
|------|------|---------|
| PE/ELF 分析 | 17 | triage、Ghidra 反编译、Rizin 反汇编、patch |
| Ghidra 深度分析 | 7 | 函数/导入/字符串查询、call focus |
| 样本全分析 | 4 | 一键：triage → Ghidra → 断点 → IOC → YARA |
| Android 逆向 | 28 | ADB、Frida 注入、私有目录取证、流量观察 |
| CTF 自动化 | 4 | sqlmap/dirsearch/jwt_tool/tplmap |
| 加密/脱壳 | 6 | 自动解密、buffer 提取、PE/DEX carve |
| 知识库 | 3 | 208 篇技术文件，按信号搜索 |
| 样本管理 | 7 | 导入/复制/移动/隔离/删除 |
| 其他 | 66 | Procmon、调试脚本、Python RE、审计 |

## CTF 流水线（15 条）

| 流水线 | 功能 |
|--------|------|
| `ctf-full-pipeline` | 全链路：资产 → 漏洞 → 验证 → 报告 |
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

## 逆向工具（自动下载）

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
