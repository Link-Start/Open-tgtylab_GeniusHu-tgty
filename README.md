# open-tgtylab

Open-source security research toolkit — 208-article knowledge base, 150+ MCP automation tools, covering CTF pentesting / APK reverse engineering / PE binary analysis / cryptography & protocol cracking / game cheating analysis. Agent-native, directory-as-convention.

> [中文版](README.zh.md)

## 路由

```
信号 → kb_router(board=) → kb_read_file → 技术文档 → MCP 工具映射 → 执行
```

| 信号类型 | 板块 | 知识库 | MCP 工具族 |
|---------|------|--------|-----------|
| HTTP/Web/API/CVE/Cloud | `ctf-website` | 26/118 | `http_probe` `run_ctf_tool` `kb_router` |
| APK/DEX/SO/Frida/Java | `apk-reverse` | 8/20 | `android_app_baseline` `android_crypto_unpack_recipe` `android_frida_*` |
| PE/x64/x86/malware/driver | `pe-reverse` | 9/22 | `triage_pe` `ghidra_headless_analyze` `make_x64dbg_breakpoint_script` `sample_full_workup` |
| Crypto/Protocol/Cheat/IoT/Radio | `general` | 5/17 | `die_scan` `ghidra_*` `rizin_*` `python_re_tool_*` |
| Windows 安全 | `windows` | 1/2 | `triage_pe` `ghidra_*` |

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

Agent 工作流：检测信号 → `kb_router` 查技术文档 → `kb_read_file` 读取 → 按 MCP 工具映射执行。

## 板块

| 板块 | 触发信号 |
|------|---------|
| `ctf-website` | URL, HTTP, JWT, SQLi, SSRF, CVE, API, CSP, OAuth, CAPTCHA, Cloudflare, ReDoS, DoS |
| `apk-reverse` | APK, DEX, adb, Frida, jadx, smali, SO, native |
| `pe-reverse` | PE, EXE, DLL, x64dbg, Ghidra, Procmon, packer, malware |
| `general` | AES/DES/RSA, protobuf, game cheat, EAC/BE/Vanguard, firmware, JTAG, SDR |
| `windows` | Notepad++, config injection, Windows security |

## CTF 流水线（15 条）

| 流水线 | 功能 |
|--------|------|
| `ctf-full-pipeline` | 全链路：资产 → 漏洞 → 验证 → 报告 |
| `ctf-24h-fleet` | 24h 舰队攻击（批量目标自动循环） |
| `ctf-24h-round` | 24h 单轮攻击（无人值守，支持断点恢复） |
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

Ghidra · Cutter · x64dbg · DiE · PE-bear · Procmon · nmap · apktool · jadx

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

## 安装

### 一键安装

```
git clone https://github.com/GeniusHu-tgty/Open-tgtylab.git
cd Open-tgtylab
```

**Windows：** 双击 `启动.bat`
**macOS：** `chmod +x tgtylab-files/install.sh && ./tgtylab-files/install.sh`
**Linux：** `chmod +x tgtylab-files/linux-install.sh && ./tgtylab-files/linux-install.sh`

启动.bat 自动完成：配置部署 → MCP 依赖 → Python RE 库 → 逆向工具下载。

### 验证

```
Windows: 双击 验证.bat
macOS/Linux: 检查 ~/.claude/CLAUDE.md 是否存在
```

## AI 工具兼容性

| 工具 | 支持 |
|------|------|
| Claude Code | ✅ |
| Codex App | ✅ |
| Hermes | ✅ |
| OpenCode | ✅ |
| WSL | ✅ 自动检测 |

## 上下文链

启动时 Agent 沿此链加载上下文：

```
CLAUDE.md → AGENTS.md → AI-USAGE.md → kb/<board>/AI-USAGE.md
```

## 许可

GPL-3.0 — 详见 [LICENSE](LICENSE)。

## 免责声明

本项目仅供学习交流使用，使用本项目造成的任何后果由使用者自行承担。
