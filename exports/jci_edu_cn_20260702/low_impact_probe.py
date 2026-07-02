import json, time, hashlib, re
from pathlib import Path
from urllib.parse import urljoin
import urllib.request
import urllib.error

BASE = 'https://www.jci.edu.cn/'
OUT = Path('exports/jci_edu_cn_20260702/evidence')
OUT.mkdir(parents=True, exist_ok=True)

PATHS = [
    '/',
    '/index.vsb.css',
    '/_sitegray/_sitegray.js',
    '/_sitegray/_sitegray_d.css',
    '/system/resource/js/counter.js',
    '/system/resource/js/vsbscreen.min.js',
    '/templates/scripts/es-checker.js',
    '/templates/scripts/jq.js',
    '/templates/scripts/flux.min.js',
    '/favicon.ico',
    '/robots.txt',
    '/sitemap.xml',
    '/swagger-ui.html', '/swagger/index.html', '/swagger.json', '/openapi.json', '/v2/api-docs', '/v3/api-docs', '/api-docs', '/docs', '/redoc',
    '/graphql',
    '/.env', '/.git/HEAD', '/WEB-INF/web.xml', '/backup.zip', '/www.zip', '/wwwroot.zip', '/index.jsp.bak', '/index.jsp~',
    '/system/login.jsp', '/system/resource/code/validateCode.jsp',
    '/system/resource/code/news/click/dynclicks.jsp',
    '/system/resource/code/news/click/clicktimes.jsp',
    '/system/resource/code/news/pagelist.jsp',
]

UA = 'Mozilla/5.0 (compatible; authorized-ctf-low-impact/1.0)'
results = []
for path in PATHS:
    url = urljoin(BASE, path.lstrip('/'))
    req = urllib.request.Request(url, headers={'User-Agent': UA})
    item = {'path': path, 'url': url}
    try:
        with urllib.request.urlopen(req, timeout=12) as resp:
            body = resp.read(200000)
            headers = dict(resp.headers.items())
            item.update({
                'status': resp.status,
                'reason': resp.reason,
                'content_type': headers.get('Content-Type',''),
                'content_length_header': headers.get('Content-Length',''),
                'body_len_sampled': len(body),
                'sha256_sample': hashlib.sha256(body).hexdigest(),
                'headers': headers,
                'title': (re.search(rb'<title[^>]*>(.*?)</title>', body, re.I|re.S).group(1).decode('utf-8','ignore').strip() if re.search(rb'<title[^>]*>(.*?)</title>', body, re.I|re.S) else ''),
                'snippet': body[:500].decode('utf-8','ignore')
            })
            safe = path.strip('/').replace('/','__').replace('?','_') or 'root'
            (OUT / f'{safe}.body.txt').write_bytes(body)
            (OUT / f'{safe}.headers.json').write_text(json.dumps(headers,ensure_ascii=False,indent=2), encoding='utf-8')
    except urllib.error.HTTPError as e:
        body = e.read(50000)
        headers = dict(e.headers.items())
        item.update({
            'status': e.code,
            'reason': e.reason,
            'content_type': headers.get('Content-Type',''),
            'content_length_header': headers.get('Content-Length',''),
            'body_len_sampled': len(body),
            'sha256_sample': hashlib.sha256(body).hexdigest(),
            'headers': headers,
            'title': (re.search(rb'<title[^>]*>(.*?)</title>', body, re.I|re.S).group(1).decode('utf-8','ignore').strip() if re.search(rb'<title[^>]*>(.*?)</title>', body, re.I|re.S) else ''),
            'snippet': body[:300].decode('utf-8','ignore')
        })
    except Exception as e:
        item.update({'error': repr(e)})
    results.append(item)
    print(f"{item.get('status','ERR')} {path} {item.get('content_type','')} {item.get('title','')[:40]}")
    time.sleep(0.7)

(OUT / 'probe_results.json').write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding='utf-8')
print('saved', OUT / 'probe_results.json')
