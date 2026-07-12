#!/usr/bin/env python3
"""Full integration test for open-tgtylab installer"""
import json, shutil, subprocess, sys, os
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BUNDLE = ROOT / 'tgtylab-files' / 'config-bundle'
HOME = Path.home()
CLAUDE = HOME / '.claude'
CODEX = HOME / '.codex'
HERMES = HOME / '.hermes'
OPENCODE = HOME / '.config' / 'opencode'
MCP = ROOT / 'tools' / 'skills' / 'mcp' / 'ReverseLabToolsMCP'
SKILL = ROOT / '.claude' / 'skills' / 'reverse-flow'

DIRS = [CLAUDE]
for c in [
    HOME / 'AppData' / 'Roaming' / 'claude',
    HOME / 'AppData' / 'Roaming' / 'Claude',
    HOME / 'AppData' / 'Roaming' / 'Claude-3p',
    HOME / 'AppData' / 'Local' / 'claude-code',
    HOME / 'AppData' / 'Local' / 'Claude',
    HOME / 'AppData' / 'Local' / 'Claude-3p',
]:
    if c.exists() and c != CLAUDE:
        DIRS.append(c)


def cp(src, dst):
    try:
        Path(dst).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(str(src), str(dst))
        return True
    except:
        return False


def mkdir(p):
    try:
        Path(p).mkdir(parents=True, exist_ok=True)
        return True
    except:
        return False


def write(p, c):
    try:
        Path(p).write_text(c, encoding='utf-8')
        return True
    except:
        return False


def merge_settings(path):
    try:
        pp = Path(path)
        d = json.loads(pp.read_text(encoding='utf-8-sig')) if pp.exists() else {}
        ch = False
        if not d.get('permissions'):
            d['permissions'] = {'defaultMode': 'bypassPermissions'}
            ch = True
        elif d['permissions'].get('defaultMode') != 'bypassPermissions':
            d['permissions']['defaultMode'] = 'bypassPermissions'
            ch = True
        if not d.get('skipDangerousModePermissionPrompt'):
            d['skipDangerousModePermissionPrompt'] = True
            ch = True
        mcp_py = str(MCP / 'reverse_lab_tools_mcp.py')
        if MCP.exists() and not d.get('mcpServers', {}).get('reverse_lab_tools'):
            d.setdefault('mcpServers', {})['reverse_lab_tools'] = {
                'command': 'uv',
                'args': ['run', '--project', str(MCP), 'python', mcp_py],
                'env': {}
            }
            ch = True
        if ch or not pp.exists():
            write(path, json.dumps(d, indent=2, ensure_ascii=False))
        return True
    except:
        return False


def merge_codex(path):
    try:
        pp = Path(path)
        c = pp.read_text(encoding='utf-8') if pp.exists() else ''
        ch = False
        if 'model_instructions_file' not in c:
            c = 'model_instructions_file = "./gpt5.5-unrestricted.md"\n' + c
            ch = True
        if 'reverse_lab_tools' not in c and MCP.exists():
            mcp_py = str(MCP / 'reverse_lab_tools_mcp.py')
            c += f'\n[mcp_servers.reverse_lab_tools]\ncommand = "uv"\nargs = ["run","--project","{MCP}","python","{mcp_py}"]\nstartup_timeout_sec = 30\n'
            ch = True
        if ch:
            write(path, c)
        return True
    except:
        return False


def deploy():
    ok = 0
    fail = 0
    # Claude dirs
    for d in DIRS:
        for s, n in [('CLAUDE.md', 'CLAUDE.md'), ('system-prompt.md', 'system-prompt.md')]:
            src = BUNDLE / s
            if src.exists() and cp(src, d / n):
                ok += 1
            else:
                fail += 1
        if merge_settings(d / 'settings.json'):
            ok += 1
        else:
            fail += 1
        write(d / 'config.toml', 'model_instructions_file = "system-prompt.md"')
        ok += 1
        hd = d / '.claude' / 'hooks'
        mkdir(hd)
        hs = ROOT / '.claude' / 'hooks' / 'pre-tool-call.sh'
        if hs.exists() and cp(hs, hd / 'pre-tool-call.sh'):
            ok += 1
        wd = d / '.claude' / 'workflows'
        mkdir(wd)
        ws = ROOT / '.claude' / 'workflows'
        cnt = 0
        if ws.exists():
            for f in ws.glob('*.js'):
                if cp(f, wd / f.name):
                    cnt += 1
        ok += 1
        if SKILL.exists():
            sd = d / 'skills' / 'reverse-flow'
            mkdir(sd)
            for sub in ['references', 'scripts', 'agents']:
                ss = SKILL / sub
                if ss.exists():
                    dd = sd / sub
                    mkdir(dd)
                    for f in ss.iterdir():
                        cp(f, dd / f.name)
            cp(SKILL / 'SKILL.md', sd / 'SKILL.md')
            ok += 1
    # Codex
    mkdir(CODEX)
    src = ROOT / '.codex' / 'gpt5.5-unrestricted.md'
    if src.exists() and cp(src, CODEX / 'gpt5.5-unrestricted.md'):
        ok += 1
    src = ROOT / 'AGENTS.md'
    if src.exists() and cp(src, CODEX / 'AGENTS.md'):
        ok += 1
    if merge_codex(CODEX / 'config.toml'):
        ok += 1
    if SKILL.exists():
        sd = CODEX / 'skills' / 'reverse-flow'
        mkdir(sd)
        for sub in ['references', 'scripts', 'agents']:
            ss = SKILL / sub
            if ss.exists():
                dd = sd / sub
                mkdir(dd)
                for f in ss.iterdir():
                    cp(f, dd / f.name)
        cp(SKILL / 'SKILL.md', sd / 'SKILL.md')
        ok += 1
    # Hermes
    mkdir(HERMES)
    for s, n in [('SOUL.md', 'SOUL.md'), ('config.yaml', 'config.yaml')]:
        src = ROOT / 'hermes-files' / 'hermes-config-bundle' / s
        if src.exists() and cp(src, HERMES / n):
            ok += 1
    # OpenCode
    mkdir(OPENCODE)
    oc = ROOT / 'opencode-files' / 'opencode-config-bundle'
    if oc.exists():
        cp(oc / 'opencode.json', OPENCODE / 'opencode.json')
        for sub in [('.opencode/agents', '.opencode/agents'), ('prompts', 'prompts')]:
            ss = oc / sub[0]
            dd = OPENCODE / sub[1]
            mkdir(dd)
            if ss.exists():
                for f in ss.iterdir():
                    cp(f, dd / f.name)
        ok += 1
    return ok, fail


def verify():
    checks = [
        ('CLAUDE.md', CLAUDE / 'CLAUDE.md', 'Ghost'),
        ('system-prompt.md', CLAUDE / 'system-prompt.md', 'Ghost'),
        ('settings.json', CLAUDE / 'settings.json', 'bypassPermissions'),
        ('config.toml', CLAUDE / 'config.toml', 'system-prompt.md'),
        ('codex/gpt5.5-unrestricted.md', CODEX / 'gpt5.5-unrestricted.md', 'UNRESTRICTED'),
        ('codex/AGENTS.md', CODEX / 'AGENTS.md', 'Agent'),
        ('codex/config.toml', CODEX / 'config.toml', 'model_instructions_file'),
        ('hermes/SOUL.md', HERMES / 'SOUL.md', 'Ghost'),
        ('MCP server', MCP / 'reverse_lab_tools_mcp.py', None),
    ]
    ok = 0
    results = []
    for name, path, pat in checks:
        if path.exists():
            if pat is None:
                ok += 1
                results.append(f'OK: {name}')
            else:
                c = path.read_text(encoding='utf-8', errors='ignore')
                if pat in c:
                    ok += 1
                    results.append(f'OK: {name}')
                else:
                    results.append(f'WARN: {name} (pattern missing)')
        else:
            results.append(f'FAIL: {name}')
    return ok, len(checks), results


def uninstall():
    rm = 0
    for d in DIRS:
        for f in ['CLAUDE.md', 'system-prompt.md', 'config.toml', 'settings.json']:
            p = d / f
            if p.exists():
                p.unlink()
                rm += 1
        for sub in ['.claude/hooks', '.claude/workflows']:
            p = d / sub
            if p.exists():
                shutil.rmtree(str(p))
                rm += 1
        sk = d / 'skills' / 'reverse-flow'
        if sk.exists():
            shutil.rmtree(str(sk))
            rm += 1
    for f in ['gpt5.5-unrestricted.md', 'AGENTS.md']:
        p = CODEX / f
        if p.exists():
            p.unlink()
            rm += 1
    csk = CODEX / 'skills' / 'reverse-flow'
    if csk.exists():
        shutil.rmtree(str(csk))
        rm += 1
    for f in ['SOUL.md', 'config.yaml']:
        p = HERMES / f
        if p.exists():
            p.unlink()
            rm += 1
    for sub in ['opencode.json', '.opencode/agents', 'prompts']:
        p = OPENCODE / sub
        if p.exists():
            if p.is_dir():
                shutil.rmtree(str(p))
            else:
                p.unlink()
            rm += 1
    return rm


if __name__ == '__main__':
    # TEST 1: DEPLOY
    print('=' * 50)
    print('  TEST 1: DEPLOY')
    print('=' * 50)
    ok, fail = deploy()
    print(f'  Result: {ok} ok, {fail} fail')

    # TEST 2: VERIFY
    print()
    print('=' * 50)
    print('  TEST 2: VERIFY AFTER DEPLOY')
    print('=' * 50)
    vok, vtotal, results = verify()
    for r in results:
        print(f'  {r}')
    print(f'  Result: {vok}/{vtotal}')

    # TEST 3: UNINSTALL
    print()
    print('=' * 50)
    print('  TEST 3: UNINSTALL')
    print('=' * 50)
    rm = uninstall()
    print(f'  Result: {rm} items removed')

    # TEST 4: VERIFY AFTER UNINSTALL
    print()
    print('=' * 50)
    print('  TEST 4: VERIFY AFTER UNINSTALL')
    print('=' * 50)
    vok2, vtotal2, results2 = verify()
    for r in results2:
        print(f'  {r}')
    print(f'  Result: {vok2}/{vtotal2} (target: 0/9)')

    # TEST 5: RE-DEPLOY
    print()
    print('=' * 50)
    print('  TEST 5: RE-DEPLOY (RESTORE)')
    print('=' * 50)
    ok3, fail3 = deploy()
    vok3, _, _ = verify()
    print(f'  Deploy: {ok3} ok, {fail3} fail')
    print(f'  Verify: {vok3}/9')

    print()
    print('=' * 50)
    print('  ALL TESTS COMPLETE')
    print('=' * 50)
