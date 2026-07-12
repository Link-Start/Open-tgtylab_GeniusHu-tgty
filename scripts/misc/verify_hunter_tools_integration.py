#!/usr/bin/env python3
"""Validate the single hunter_tools registration and OpenTgtyLab workspace bridge."""
from __future__ import annotations
import argparse, importlib.util, json, os, sys, tomllib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
DEFAULT_HUNTER=Path.home()/'.agents'/'skills'/'hunter'/'mcp_server.py'

def load_toml(path:Path)->dict: return tomllib.loads(path.read_text(encoding='utf-8-sig'))
def check_registration()->list[str]:
 errors=[]
 mcp_json=json.loads((ROOT/'.mcp.json').read_text(encoding='utf-8-sig'))
 for source,servers in ((".mcp.json",mcp_json.get('mcpServers',{})),(".codex/config.toml",load_toml(ROOT/'.codex'/'config.toml').get('mcp_servers',{}))):
  if 'hunter' in servers: errors.append(f'{source}: legacy hunter registration is forbidden')
  if 'hunter_tools' not in servers: errors.append(f'{source}: hunter_tools registration is missing')
 return errors

def main()->int:
 parser=argparse.ArgumentParser(); parser.add_argument('--config-only',action='store_true'); args=parser.parse_args()
 errors=check_registration()
 if args.config_only:
  print(json.dumps({'status':'error' if errors else 'ok','workspace':str(ROOT),'errors':errors},ensure_ascii=False,indent=2)); return 1 if errors else 0
 entrypoint=Path(os.environ.get('HUNTER_TOOLS_ENTRYPOINT',DEFAULT_HUNTER)).expanduser().resolve()
 if not entrypoint.is_file(): errors.append(f'Hunter entrypoint missing: {entrypoint}')
 else:
  os.environ.setdefault('OPEN_TGTYLAB_ROOT',str(ROOT)); sys.path.insert(0,str(entrypoint.parent))
  spec=importlib.util.spec_from_file_location('hunter_tools_integration_check',entrypoint); module=importlib.util.module_from_spec(spec); assert spec and spec.loader; spec.loader.exec_module(module)
  health=module._workspace.health()
  checks=health.get('data',{}).get('checks',{})
  if not checks.get('root') or not checks.get('kb'): errors.append(f'Workspace adapter unavailable: {health}')
  tools={name for name,value in vars(module).items() if name.startswith('hunter_') and callable(value)}
  required={'hunter_workspace_health','hunter_case_open','hunter_project_kb_search','hunter_evidence_save','hunter_report_publish'}
  if missing:=sorted(required-tools): errors.append(f'Missing workspace MCP tools: {missing}')
 print(json.dumps({'status':'error' if errors else 'ok','workspace':str(ROOT),'hunter_entrypoint':str(entrypoint),'errors':errors},ensure_ascii=False,indent=2)); return 1 if errors else 0
if __name__=='__main__': raise SystemExit(main())
