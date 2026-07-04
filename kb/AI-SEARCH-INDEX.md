# AI Search Index

> 全知识库 RAG 检索索引。每个条目将漏洞信号映射到对应 KB 文章。
> 覆盖 194 篇文章：12 篇深度攻略 + 111 篇 Web 技术 + 19 篇 APK 逆向 + 21 篇 PE 分析 + 15 篇通用技术 + 16 篇 Checklist/Payloads.

---

## 一、深度攻击指南（deep-articles/）

| 信号 | 路径 | 标题 |
|------|------|------|
| SQLi, injection, database, UNION, blind, sqli, mysql, postgres, mssql | `deep-articles/sql-injection.md` | SQL Injection — Complete Attack Guide |
| SSRF, internal, metadata, cloud, 169.254, gopher, file:// | `deep-articles/ssrf.md` | SSRF — Complete Attack Guide |
| SSTI, template, Jinja2, Twig, Freemarker, Velocity, Smarty, Thymeleaf | `deep-articles/ssti.md` | SSTI — Complete Attack Guide |
| XSS, script, reflected, stored, DOM, CSP bypass | `deep-articles/xss.md` | XSS — Complete Attack Guide |
| LFI, file read, path traversal, /etc/passwd, PHP wrapper, log poisoning | `deep-articles/lfi-file-inclusion.md` | LFI / File Inclusion — Complete Guide |
| JWT, token, alg, none, kid, jku, brute force, hashcat | `deep-articles/jwt-attacks.md` | JWT Attack — Complete Guide |
| deserialization, unserialize, gadget, phar, magic method, type juggling | `deep-articles/php-deserialization.md` | PHP Deserialization — Complete Guide |
| XXE, XML, entity, DOCTYPE, blind OOB, SVG XXE, XInclude | `deep-articles/xxe.md` | XXE — Complete Attack Guide |
| command injection, RCE, shell, exec, bash, powershell, commix | `deep-articles/command-injection.md` | Command Injection — Complete Guide |
| file upload, webshell, bypass, extension, MIME, magic bytes | `deep-articles/file-upload.md` | File Upload Vulnerabilities — Complete Guide |
| HTTP smuggling, CL.TE, TE.CL, TE.TE, desync, cache poisoning | `deep-articles/http-smuggling.md` | HTTP Request Smuggling — Complete Guide |
| OAuth, SSO, CAS, SAML, redirect_uri, state, scope, PKCE | `deep-articles/oauth-sso-attacks.md` | OAuth/SSO Attack — Complete Guide |

---

## 二、Web 攻击技术（ctf-website/techniques/）

### 01-Recon 侦察
| 信号 | 路径 |
|------|------|
| captcha, 验证码, 验证码绕过 | `ctf-website/techniques/01-recon/captcha-bypass.md` |
| cloudflare, CF, WAF bypass, 5秒盾 | `ctf-website/techniques/01-recon/cloudflare-bypass.md` |
| fofa, 资产发现, 空间测绘 | `ctf-website/techniques/01-recon/fofa-hunting.md` |
| 侦察, 路由, 信息收集 | `ctf-website/techniques/01-recon/recon-routing.md` |
| 版本指纹, 指纹识别, whatweb | `ctf-website/techniques/01-recon/version-fingerprinting.md` |

### 02-Auth 认证
| 信号 | 路径 |
|------|------|
| host header, Host 注入, 密码重置 | `ctf-website/techniques/02-auth/host-header.md` |
| JWT overview | `ctf-website/techniques/02-auth/jwt/00-overview.md` |
| JWT alg:none | `ctf-website/techniques/02-auth/jwt/01-alg-none.md` |
| JWT algorithm confusion, RSA→HMAC | `ctf-website/techniques/02-auth/jwt/02-algorithm-confusion.md` |
| JWT weak key, 爆破 | `ctf-website/techniques/02-auth/jwt/03-weak-key-bruteforce.md` |

### 03-Injection 注入
| 信号 | 路径 |
|------|------|
| SQL injection, SQLi, 数据库注入 | `ctf-website/techniques/03-injection/` (多篇) |
| NoSQL injection, MongoDB | `ctf-website/techniques/03-injection/` |
| XSS, 跨站脚本 | `ctf-website/techniques/03-injection/` |
| SSTI, 模板注入 | `ctf-website/techniques/03-injection/` |
| CRLF injection | `ctf-website/techniques/03-injection/` |

### 04-SSRF
| 信号 | 路径 |
|------|------|
| SSRF, 服务端请求伪造 | `ctf-website/techniques/04-ssrf/` |
| cloud metadata, 云元数据 | `ctf-website/techniques/04-ssrf/` |
| Redis SSRF, 内网穿透 | `ctf-website/techniques/04-ssrf/` |

### 05-Deserialization 反序列化
| 信号 | 路径 |
|------|------|
| Java deserialization, ysoserial | `ctf-website/techniques/05-deserialization/` |
| PHP deserialization | `ctf-website/techniques/05-deserialization/` |
| Python pickle | `ctf-website/techniques/05-deserialization/` |

### 06-File Attacks 文件攻击
| 信号 | 路径 |
|------|------|
| file upload, 文件上传 | `ctf-website/techniques/06-file-attacks/` |
| LFI, 文件包含, path traversal | `ctf-website/techniques/06-file-attacks/` |
| .git source disclosure | `ctf-website/techniques/06-file-attacks/` |
| .svn, .DS_Store | `ctf-website/techniques/06-file-attacks/` |

### 07-Client 客户端
| 信号 | 路径 |
|------|------|
| DOM XSS, 前端漏洞 | `ctf-website/techniques/07-client/` |
| CORS misconfiguration | `ctf-website/techniques/07-client/` |
| postMessage | `ctf-website/techniques/07-client/` |

### 08-Infra 基础设施
| 信号 | 路径 |
|------|------|
| Redis 未授权, 6379 | `ctf-website/techniques/08-infra/` |
| Memcached, 11211 | `ctf-website/techniques/08-infra/` |
| Elasticsearch, 9200 | `ctf-website/techniques/08-infra/` |
| MongoDB, 27017 | `ctf-website/techniques/08-infra/` |
| Docker API, 2375 | `ctf-website/techniques/08-infra/` |

### 09-CVE
| 信号 | 路径 |
|------|------|
| Log4Shell, CVE-2021-44228 | `ctf-website/techniques/09-cve/` |
| Spring4Shell, CVE-2022-22965 | `ctf-website/techniques/09-cve/` |
| Fastjson RCE | `ctf-website/techniques/09-cve/` |
| Shiro deserialization | `ctf-website/techniques/09-cve/` |

### 10-Cloud 云
| 信号 | 路径 |
|------|------|
| AWS S3 bucket | `ctf-website/techniques/10-cloud/` |
| Azure blob | `ctf-website/techniques/10-cloud/` |
| GCP storage | `ctf-website/techniques/10-cloud/` |

### 11-Supply Chain 供应链
| 信号 | 路径 |
|------|------|
| dependency confusion | `ctf-website/techniques/11-supply-chain/` |
| typosquatting | `ctf-website/techniques/11-supply-chain/` |

### 12-Payment 支付
| 信号 | 路径 |
|------|------|
| price manipulation, 价格篡改 | `ctf-website/techniques/12-payment/` |
| coupon bypass, 优惠券绕过 | `ctf-website/techniques/12-payment/` |
| race condition payment | `ctf-website/techniques/12-payment/` |

### 13-Signature 签名
| 信号 | 路径 |
|------|------|
| HMAC bypass | `ctf-website/techniques/13-signature/` |
| RSA signature | `ctf-website/techniques/13-signature/` |

### 14-IDOR
| 信号 | 路径 |
|------|------|
| IDOR, 越权, horizontal privilege escalation | `ctf-website/techniques/14-idor/` |

### 15-Mass Assignment
| 信号 | 路径 |
|------|------|
| mass assignment, 参数注入, role escalation | `ctf-website/techniques/15-mass-assignment/` |

### 16-Rate Limit
| 信号 | 路径 |
|------|------|
| rate limit bypass, 限速绕过, brute force | `ctf-website/techniques/16-rate-limit/` |

### 17-API Attacks
| 信号 | 路径 |
|------|------|
| GraphQL, introspection, batch attack | `ctf-website/techniques/17-api-attacks/` |
| REST API, BOLA, broken authorization | `ctf-website/techniques/17-api-attacks/` |

### 18-CORS/CSP Advanced
| 信号 | 路径 |
|------|------|
| CORS bypass, CSP bypass | `ctf-website/techniques/18-cors-csp-advanced/` |

### 19-DNS/Email
| 信号 | 路径 |
|------|------|
| DNS rebinding, SPF/DKIM/DMARC | `ctf-website/techniques/19-dns-email/` |
| email spoofing | `ctf-website/techniques/19-dns-email/` |

### 20-OAuth Deep
| 信号 | 路径 |
|------|------|
| OAuth deep, redirect_uri abuse | `ctf-website/techniques/20-oauth-deep/` |

### 21-Mobile Bridge
| 信号 | 路径 |
|------|------|
| mobile-to-web, deep link | `ctf-website/techniques/21-mobile-bridge/` |

### 22-DoS
| 信号 | 路径 |
|------|------|
| DoS, denial of service, ReDoS, Slowloris | `ctf-website/techniques/22-dos/` |

### 23-Paywall Bypass
| 信号 | 路径 |
|------|------|
| paywall, 付费墙, subscription bypass | `ctf-website/techniques/23-paywall-bypass/` |

### 24-Database
| 信号 | 路径 |
|------|------|
| database specific, MySQL/MSSQL/PostgreSQL/SQLite/Oracle | `ctf-website/techniques/24-database/` |

### Checklists & Payloads
| 信号 | 路径 |
|------|------|
| attack matrix, 攻击矩阵 | `ctf-website/checklists/attack-matrix.md` |
| evidence, 证据收集 | `ctf-website/checklists/evidence.md` |
| first 30 min, 前30分钟 | `ctf-website/checklists/web-ctf-first-30-min.md` |
| payload seeds, 种子 payload | `ctf-website/payloads/web-payload-seeds.md` |
| cheatsheet, 速查 | `payloads/cheatsheet.md` |

---

## 三、APK 逆向（apk-reverse/techniques/）

| 信号 | 路径 |
|------|------|
| smali, DEX, Java injection | `apk-reverse/techniques/01-dex-java/01-smali-injection.md` |
| IL2CPP, offset, Unity | `apk-reverse/techniques/02-native/01-il2cpp-offset-discovery.md` |
| pointer chain, 指针链 | `apk-reverse/techniques/02-native/02-pointer-chain-patterns.md` |
| UE4, Unreal, offset hunting | `apk-reverse/techniques/02-native/03-ue4-offset-hunting.md` |
| kernel, procfs, driver | `apk-reverse/techniques/02-native/04-kernel-procfs-driver.md` |
| virtual memory, physical memory | `apk-reverse/techniques/02-native/05-virt-phys-memory.md` |
| AndroidManifest, entry point | `apk-reverse/techniques/03-manifest/01-entry-point-tracing.md` |
| game encryption, 游戏加密 | `apk-reverse/techniques/04-crypto/01-game-encryption-patterns.md` |
| RC4, custom crypto | `apk-reverse/techniques/04-crypto/02-rc4-custom-crypto.md` |
| game protocol, hook, 游戏协议 | `apk-reverse/techniques/05-network/01-game-protocol-hook.md` |
| license bypass, 许可证绕过 | `apk-reverse/techniques/05-network/02-license-verification-bypass.md` |
| memory read/write, hook | `apk-reverse/techniques/06-dynamic/01-memory-rw-hook.md` |
| overlay, ESP, rendering hook | `apk-reverse/techniques/06-dynamic/02-overlay-rendering-hook.md` |
| touch input, input hook | `apk-reverse/techniques/06-dynamic/03-touch-input-hook.md` |
| obfuscation, 混淆检测 | `apk-reverse/techniques/07-packer/01-obfuscation-detection.md` |
| self-extracting, 自解压 | `apk-reverse/techniques/07-packer/02-self-extracting-payload.md` |
| SO injection, repack, 重打包 | `apk-reverse/techniques/08-patch-repack/01-so-injection-repack.md` |
| network attack, 网络攻击 | `apk-reverse/techniques/attack-network.md` |

---

## 四、PE 逆向（pe-reverse/techniques/）

| 信号 | 路径 |
|------|------|
| PE triage, 初筛 | `pe-reverse/techniques/01-triage/` |
| PE structure, PE 结构 | `pe-reverse/techniques/02-pe-structure/` |
| static analysis, 静态分析 | `pe-reverse/techniques/03-static-analysis/` |
| dynamic analysis, 动态分析 | `pe-reverse/techniques/04-dynamic-analysis/` |
| crypto unpack, 加密脱壳 | `pe-reverse/techniques/05-crypto-unpack/` |
| IOC extraction, IOC 提取 | `pe-reverse/techniques/06-ioc-extraction/` |
| YARA, Sigma, 检测规则 | `pe-reverse/techniques/07-yara-sigma/` |
| patch, 补丁分析 | `pe-reverse/techniques/08-patch/` |
| AV evasion, 免杀 | `pe-reverse/techniques/09-av-evasion/` |

---

## 五、通用技术（general/）

| 信号 | 路径 |
|------|------|
| AES, DES, RSA, crypto | `general/techniques/crypto/` |
| protobuf, protocol | `general/techniques/protocol/` |
| game cheat, 游戏外挂 | `general/techniques/cheating/` |
| methodology, 方法论 | `general/techniques/methodology/` |

---

## 六、快速查找（按场景）

### 发现漏洞时
- **SQL 注入** → `deep-articles/sql-injection.md` + `ctf-website/techniques/03-injection/`
- **XSS** → `deep-articles/xss.md` + `ctf-website/techniques/03-injection/`
- **SSRF** → `deep-articles/ssrf.md` + `ctf-website/techniques/04-ssrf/`
- **SSTI** → `deep-articles/ssti.md` + `ctf-website/techniques/03-injection/`
- **XXE** → `deep-articles/xxe.md`
- **命令注入** → `deep-articles/command-injection.md`
- **文件上传** → `deep-articles/file-upload.md` + `ctf-website/techniques/06-file-attacks/`
- **文件包含** → `deep-articles/lfi-file-inclusion.md` + `ctf-website/techniques/06-file-attacks/`
- **反序列化** → `deep-articles/php-deserialization.md` + `ctf-website/techniques/05-deserialization/`
- **JWT** → `deep-articles/jwt-attacks.md` + `ctf-website/techniques/02-auth/jwt/`
- **OAuth/SSO** → `deep-articles/oauth-sso-attacks.md` + `ctf-website/techniques/20-oauth-deep/`
- **HTTP 走私** → `deep-articles/http-smuggling.md`
- **IDOR** → `ctf-website/techniques/14-idor/`
- **竞态条件** → `ctf-website/techniques/12-payment/`
- **GraphQL** → `ctf-website/techniques/17-api-attacks/`

### 逆向分析时
- **Android APK** → `apk-reverse/techniques/` (19 篇)
- **PE/EXE** → `pe-reverse/techniques/` (21 篇)
- **游戏外挂** → `general/techniques/cheating/`
- **加密算法** → `general/techniques/crypto/`

### 需要 Payload 时
- **通用速查** → `payloads/cheatsheet.md`
- **Web 种子** → `ctf-website/payloads/web-payload-seeds.md`

### 需要 Checklist 时
- **攻击矩阵** → `ctf-website/checklists/attack-matrix.md`
- **前30分钟** → `ctf-website/checklists/web-ctf-first-30-min.md`
- **证据收集** → `ctf-website/checklists/evidence.md`
