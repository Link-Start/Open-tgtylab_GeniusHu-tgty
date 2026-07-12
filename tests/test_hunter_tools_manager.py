import json
from pathlib import Path

from scripts.misc.hunter_tools_manager import HunterToolsManager, remove_toml_server_block


def test_remove_legacy_hunter_without_removing_hunter_tools():
    text = '[mcp_servers.hunter_tools]\ncommand="python"\n\n[mcp_servers.hunter]\ncommand="python"\n\n[features]\nx=true\n'
    out = remove_toml_server_block(text, 'hunter')
    assert '[mcp_servers.hunter_tools]' in out
    assert '[mcp_servers.hunter]' not in out
    assert '[features]' in out


def test_configure_project_is_dynamic_and_idempotent(tmp_path):
    root = tmp_path / 'Open-tgtylab'; root.mkdir()
    (root / '.codex').mkdir()
    (root / '.mcp.json').write_text(json.dumps({'mcpServers': {'hunter': {'command':'old'}}}), encoding='utf-8')
    (root / '.codex' / 'config.toml').write_text('[mcp_servers.hunter]\ncommand="old"\n', encoding='utf-8')
    hunter = tmp_path / 'hunter'; hunter.mkdir(); (hunter / 'mcp_server.py').write_text('', encoding='utf-8')
    manager = HunterToolsManager(root=root, hunter_dir=hunter, python='python')
    first = manager.configure_project(); second = manager.configure_project()
    data = json.loads((root / '.mcp.json').read_text(encoding='utf-8'))
    assert 'hunter' not in data['mcpServers'] and 'hunter_tools' in data['mcpServers']
    assert data['mcpServers']['hunter_tools']['env']['OPEN_TGTYLAB_ROOT'] == str(root.resolve())
    toml = (root / '.codex' / 'config.toml').read_text(encoding='utf-8')
    assert '[mcp_servers.hunter]' not in toml and toml.count('[mcp_servers.hunter_tools]') == 1
    assert first['changed'] is True and second['changed'] is False


def test_status_reports_contract_and_entrypoint(tmp_path):
    root=tmp_path/'lab'; root.mkdir(); (root/'cases').mkdir(); (root/'kb').mkdir()
    hunter=tmp_path/'hunter'; hunter.mkdir(); (hunter/'mcp_server.py').write_text('',encoding='utf-8')
    (hunter/'integration-contract.json').write_text(json.dumps({'contract_version':'1.0','server_name':'hunter_tools'}),encoding='utf-8')
    status=HunterToolsManager(root=root,hunter_dir=hunter,python='python').status()
    assert status['entrypoint_exists'] is True
    assert status['contract']['server_name']=='hunter_tools'
