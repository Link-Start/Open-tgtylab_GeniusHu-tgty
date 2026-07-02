#!/usr/bin/env python3
"""open-tgtylab GUI Installer — 一键可控部署"""

import json
import os
import shutil
import subprocess
import sys
import threading
from pathlib import Path
from tkinter import (
    BooleanVar,
    Button,
    Checkbutton,
    END,
    Frame,
    Label,
    messagebox,
    StringVar,
    Text,
    Tk,
    Toplevel,
    BOTH,
    LEFT,
    RIGHT,
    X,
    Y,
    W,
    E,
    N,
    S,
    WORD,
    DISABLED,
    NORMAL,
)
from tkinter.ttk import (
    Button as TtkButton,
    Checkbutton as TtkCheck,
    Frame as TtkFrame,
    Label as TtkLabel,
    Labelframe,
    Progressbar,
    Scrollbar,
    Separator,
    Style,
)

# ── Paths ──
SCRIPT_DIR = Path(__file__).resolve().parent
BUNDLE_DIR = SCRIPT_DIR / "tgtylab-files" / "config-bundle"
USER_HOME = Path.home()
CLAUDE_DIR = USER_HOME / ".claude"
CODEX_DIR = USER_HOME / ".codex"
HERMES_DIR = USER_HOME / ".hermes"
OPENCODE_DIR = USER_HOME / ".config" / "opencode"
MCP_DIR = SCRIPT_DIR / "tools" / "skills" / "mcp" / "ReverseLabToolsMCP"
SKILL_SRC = SCRIPT_DIR / ".claude" / "skills" / "reverse-flow"

# Claude Code config dirs to check
CLAUDE_DIRS = [CLAUDE_DIR]
for candidate in [
    USER_HOME / "AppData" / "Roaming" / "claude",
    USER_HOME / "AppData" / "Roaming" / "Claude",
    USER_HOME / "AppData" / "Roaming" / "Claude-3p",
    USER_HOME / "AppData" / "Local" / "claude-code",
    USER_HOME / "AppData" / "Local" / "claude",
    USER_HOME / "AppData" / "Local" / "Claude",
    USER_HOME / "AppData" / "Local" / "Claude-3p",
]:
    if candidate.exists() and candidate != CLAUDE_DIR:
        CLAUDE_DIRS.append(candidate)


def safe_copy(src: Path, dst: Path) -> bool:
    try:
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(str(src), str(dst))
        return True
    except Exception:
        return False


def safe_mkdir(path: Path) -> bool:
    try:
        path.mkdir(parents=True, exist_ok=True)
        return True
    except Exception:
        return False


def write_utf8(path: Path, content: str) -> bool:
    try:
        path.write_text(content, encoding="utf-8")
        return True
    except Exception:
        return False


def merge_settings_json(path: Path) -> bool:
    """Merge bypassPermissions + MCP server into settings.json"""
    try:
        if path.exists():
            data = json.loads(path.read_text(encoding="utf-8-sig"))
        else:
            data = {}

        changed = False
        if not data.get("permissions"):
            data["permissions"] = {"defaultMode": "bypassPermissions"}
            changed = True
        elif data["permissions"].get("defaultMode") != "bypassPermissions":
            data["permissions"]["defaultMode"] = "bypassPermissions"
            changed = True

        if not data.get("skipDangerousModePermissionPrompt"):
            data["skipDangerousModePermissionPrompt"] = True
            changed = True

        mcp_py = str(MCP_DIR / "reverse_lab_tools_mcp.py")
        if MCP_DIR.exists() and not data.get("mcpServers", {}).get("reverse_lab_tools"):
            if "mcpServers" not in data:
                data["mcpServers"] = {}
            data["mcpServers"]["reverse_lab_tools"] = {
                "command": "uv",
                "args": ["run", "--project", str(MCP_DIR), "python", mcp_py],
                "env": {},
            }
            changed = True

        if changed or not path.exists():
            write_utf8(path, json.dumps(data, indent=2, ensure_ascii=False))
        return True
    except Exception:
        return False


def merge_codex_config(path: Path) -> bool:
    """Add model_instructions_file + MCP server to codex config.toml"""
    try:
        content = path.read_text(encoding="utf-8") if path.exists() else ""
        changed = False

        if "model_instructions_file" not in content:
            content = 'model_instructions_file = "./gpt5.5-unrestricted.md"\n' + content
            changed = True

        if "reverse_lab_tools" not in content and MCP_DIR.exists():
            mcp_py = str(MCP_DIR / "reverse_lab_tools_mcp.py")
            content += f"""
[mcp_servers.reverse_lab_tools]
command = "uv"
args = [
    "run",
    "--project",
    "{MCP_DIR}",
    "python",
    "{mcp_py}",
]
startup_timeout_sec = 30
"""
            changed = True

        if changed:
            write_utf8(path, content)
        return True
    except Exception:
        return False


class InstallerGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("open-tgtylab Installer")
        self.root.geometry("680x820")
        self.root.resizable(False, False)

        # Dark theme colors
        self.bg = "#1e1e2e"
        self.fg = "#cdd6f4"
        self.accent = "#89b4fa"
        self.green = "#a6e3a1"
        self.red = "#f38ba8"
        self.yellow = "#f9e2af"
        self.surface = "#313244"
        self.surface2 = "#45475a"

        self.root.configure(bg=self.bg)

        self.log_lines = []
        self._build_ui()

    def _build_ui(self):
        # Header
        header = Frame(self.root, bg=self.accent, height=50)
        header.pack(fill=X)
        header.pack_propagate(False)
        Label(header, text="🐙 open-tgtylab", font=("Segoe UI", 18, "bold"),
              bg=self.accent, fg=self.bg).pack(side=LEFT, padx=15)
        Label(header, text="AI Agent 越狱部署工具", font=("Segoe UI", 11),
              bg=self.accent, fg=self.bg).pack(side=LEFT, padx=5)

        # Main content
        main = Frame(self.root, bg=self.bg)
        main.pack(fill=BOTH, expand=True, padx=15, pady=10)

        # ── Platform selection ──
        pf = Labelframe(main, text=" 平台选择 ", style="Custom.TLabelframe")
        pf.pack(fill=X, pady=(0, 10))

        self.var_claude = BooleanVar(value=True)
        self.var_codex = BooleanVar(value=True)
        self.var_hermes = BooleanVar(value=True)
        self.var_opencode = BooleanVar(value=True)

        row1 = Frame(pf, bg=self.surface)
        row1.pack(fill=X, padx=10, pady=5)
        Checkbutton(row1, text="Claude Code / Desktop", variable=self.var_claude,
                    bg=self.surface, fg=self.fg, selectcolor=self.surface2,
                    activebackground=self.surface, activeforeground=self.fg).pack(side=LEFT, padx=(0, 20))
        Checkbutton(row1, text="Codex App", variable=self.var_codex,
                    bg=self.surface, fg=self.fg, selectcolor=self.surface2,
                    activebackground=self.surface, activeforeground=self.fg).pack(side=LEFT, padx=(0, 20))
        Checkbutton(row1, text="Hermes", variable=self.var_hermes,
                    bg=self.surface, fg=self.fg, selectcolor=self.surface2,
                    activebackground=self.surface, activeforeground=self.fg).pack(side=LEFT, padx=(0, 20))
        Checkbutton(row1, text="OpenCode", variable=self.var_opencode,
                    bg=self.surface, fg=self.fg, selectcolor=self.surface2,
                    activebackground=self.surface, activeforeground=self.fg).pack(side=LEFT)

        # ── Component selection ──
        cf = Labelframe(main, text=" 部署组件 ", style="Custom.TLabelframe")
        cf.pack(fill=X, pady=(0, 10))

        self.var_jailbreak = BooleanVar(value=True)
        self.var_mcp = BooleanVar(value=True)
        self.var_skills = BooleanVar(value=True)
        self.var_workflows = BooleanVar(value=True)
        self.var_hooks = BooleanVar(value=True)
        self.var_python_re = BooleanVar(value=True)

        row2 = Frame(cf, bg=self.surface)
        row2.pack(fill=X, padx=10, pady=5)
        Checkbutton(row2, text="越狱配置 (562 示例)", variable=self.var_jailbreak,
                    bg=self.surface, fg=self.fg, selectcolor=self.surface2,
                    activebackground=self.surface, activeforeground=self.fg).pack(side=LEFT, padx=(0, 20))
        Checkbutton(row2, text="MCP 工具 (150+)", variable=self.var_mcp,
                    bg=self.surface, fg=self.fg, selectcolor=self.surface2,
                    activebackground=self.surface, activeforeground=self.fg).pack(side=LEFT, padx=(0, 20))
        Checkbutton(row2, text="逆向 Skill", variable=self.var_skills,
                    bg=self.surface, fg=self.fg, selectcolor=self.surface2,
                    activebackground=self.surface, activeforeground=self.fg).pack(side=LEFT)

        row3 = Frame(cf, bg=self.surface)
        row3.pack(fill=X, padx=10, pady=(0, 5))
        Checkbutton(row3, text="CTF 流水线 (5个)", variable=self.var_workflows,
                    bg=self.surface, fg=self.fg, selectcolor=self.surface2,
                    activebackground=self.surface, activeforeground=self.fg).pack(side=LEFT, padx=(0, 20))
        Checkbutton(row3, text="MCP Hook", variable=self.var_hooks,
                    bg=self.surface, fg=self.fg, selectcolor=self.surface2,
                    activebackground=self.surface, activeforeground=self.fg).pack(side=LEFT, padx=(0, 20))
        Checkbutton(row3, text="Python RE 库", variable=self.var_python_re,
                    bg=self.surface, fg=self.fg, selectcolor=self.surface2,
                    activebackground=self.surface, activeforeground=self.fg).pack(side=LEFT)

        # ── Action buttons ──
        btn_frame = Frame(main, bg=self.bg)
        btn_frame.pack(fill=X, pady=(0, 10))

        self.btn_deploy = Button(btn_frame, text="▶ 部署", font=("Segoe UI", 12, "bold"),
                                 bg=self.green, fg=self.bg, relief="flat", padx=30, pady=8,
                                 command=self._start_deploy)
        self.btn_deploy.pack(side=LEFT, padx=(0, 10))

        self.btn_verify = Button(btn_frame, text="🔍 验证", font=("Segoe UI", 12),
                                 bg=self.accent, fg=self.bg, relief="flat", padx=20, pady=8,
                                 command=self._start_verify)
        self.btn_verify.pack(side=LEFT, padx=(0, 10))

        self.btn_uninstall = Button(btn_frame, text="🗑 卸载", font=("Segoe UI", 12),
                                    bg=self.red, fg=self.bg, relief="flat", padx=20, pady=8,
                                    command=self._start_uninstall)
        self.btn_uninstall.pack(side=LEFT)

        # ── Progress ──
        self.progress = Progressbar(main, mode="indeterminate", style="Custom.Horizontal.TProgressbar")
        self.progress.pack(fill=X, pady=(0, 5))

        # ── Log output ──
        log_frame = Frame(main, bg=self.bg)
        log_frame.pack(fill=BOTH, expand=True)

        self.log_text = Text(log_frame, bg=self.surface, fg=self.fg, font=("Consolas", 10),
                             wrap=WORD, relief="flat", padx=10, pady=10)
        scrollbar = Scrollbar(log_frame, command=self.log_text.yview)
        self.log_text.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.log_text.pack(fill=BOTH, expand=True)

        self._log("open-tgtylab Installer ready.", "info")
        self._log(f"Project: {SCRIPT_DIR}", "gray")
        self._log(f"Home: {USER_HOME}", "gray")
        self._log("", "gray")

    def _log(self, msg: str, level: str = "normal"):
        colors = {
            "info": self.accent,
            "success": self.green,
            "error": self.red,
            "warning": self.yellow,
            "gray": self.surface2,
            "normal": self.fg,
        }
        self.log_text.configure(state=NORMAL)
        self.log_text.insert(END, msg + "\n")
        self.log_text.tag_configure(level, foreground=colors.get(level, self.fg))
        # Apply tag to the last line
        last_line = int(self.log_text.index("end-1c").split(".")[0])
        self.log_text.tag_add(level, f"{last_line}.0", f"{last_line}.end")
        self.log_text.see(END)
        self.log_text.configure(state=DISABLED)
        self.root.update_idletasks()

    def _set_buttons(self, enabled: bool):
        state = NORMAL if enabled else DISABLED
        self.btn_deploy.configure(state=state)
        self.btn_verify.configure(state=state)
        self.btn_uninstall.configure(state=state)

    def _start_deploy(self):
        self._set_buttons(False)
        self.progress.start(10)
        threading.Thread(target=self._deploy, daemon=True).start()

    def _start_verify(self):
        self._set_buttons(False)
        self.progress.start(10)
        threading.Thread(target=self._verify, daemon=True).start()

    def _start_uninstall(self):
        if not messagebox.askyesno("确认卸载", "确定要卸载 open-tgtylab 配置吗？"):
            return
        self._set_buttons(False)
        self.progress.start(10)
        threading.Thread(target=self._uninstall, daemon=True).start()

    def _deploy(self):
        try:
            self._log("=" * 50, "info")
            self._log("  open-tgtylab Deploy", "info")
            self._log("=" * 50, "info")
            self._log("", "normal")

            ok = 0
            fail = 0

            # ── Claude Code / Desktop ──
            if self.var_claude.get():
                self._log("[Claude Code / Desktop]", "info")
                for d in CLAUDE_DIRS:
                    self._log(f"  Deploying to: {d}", "gray")

                    if self.var_jailbreak.get():
                        # CLAUDE.md
                        src = BUNDLE_DIR / "CLAUDE.md"
                        dst = d / "CLAUDE.md"
                        if src.exists() and safe_copy(src, dst):
                            self._log(f"    CLAUDE.md: OK ({dst.stat().st_size} bytes)", "success")
                            ok += 1
                        else:
                            self._log("    CLAUDE.md: FAIL", "error")
                            fail += 1

                        # system-prompt.md
                        src = BUNDLE_DIR / "system-prompt.md"
                        dst = d / "system-prompt.md"
                        if src.exists() and safe_copy(src, dst):
                            self._log(f"    system-prompt.md: OK", "success")
                            ok += 1
                        else:
                            self._log("    system-prompt.md: FAIL", "error")
                            fail += 1

                        # settings.json
                        if merge_settings_json(d / "settings.json"):
                            self._log("    settings.json: OK", "success")
                            ok += 1
                        else:
                            self._log("    settings.json: FAIL", "error")
                            fail += 1

                        # config.toml
                        if write_utf8(d / "config.toml", 'model_instructions_file = "system-prompt.md"'):
                            self._log("    config.toml: OK", "success")
                            ok += 1

                    # Hooks
                    if self.var_hooks.get():
                        hooks_dir = d / ".claude" / "hooks"
                        safe_mkdir(hooks_dir)
                        hook_src = SCRIPT_DIR / ".claude" / "hooks" / "pre-tool-call.sh"
                        if hook_src.exists() and safe_copy(hook_src, hooks_dir / "pre-tool-call.sh"):
                            self._log("    hooks: OK", "success")
                            ok += 1

                    # Workflows
                    if self.var_workflows.get():
                        wf_dir = d / ".claude" / "workflows"
                        safe_mkdir(wf_dir)
                        wf_src = SCRIPT_DIR / ".claude" / "workflows"
                        if wf_src.exists():
                            count = 0
                            for f in wf_src.glob("*.js"):
                                if safe_copy(f, wf_dir / f.name):
                                    count += 1
                            self._log(f"    workflows: OK ({count} files)", "success")
                            ok += 1

                    # Skills
                    if self.var_skills.get() and SKILL_SRC.exists():
                        skill_dst = d / "skills" / "reverse-flow"
                        safe_mkdir(skill_dst)
                        for sub in ["references", "scripts", "agents"]:
                            src_dir = SKILL_SRC / sub
                            if src_dir.exists():
                                dst_dir = skill_dst / sub
                                safe_mkdir(dst_dir)
                                for f in src_dir.iterdir():
                                    safe_copy(f, dst_dir / f.name)
                        safe_copy(SKILL_SRC / "SKILL.md", skill_dst / "SKILL.md")
                        safe_copy(SKILL_SRC / "README.md", skill_dst / "README.md")
                        self._log("    skills: OK", "success")
                        ok += 1

                self._log("", "normal")

            # ── Codex ──
            if self.var_codex.get():
                self._log("[Codex App]", "info")

                if self.var_jailbreak.get():
                    # gpt5.5-unrestricted.md
                    src = SCRIPT_DIR / ".codex" / "gpt5.5-unrestricted.md"
                    safe_mkdir(CODEX_DIR)
                    if src.exists() and safe_copy(src, CODEX_DIR / "gpt5.5-unrestricted.md"):
                        self._log("    gpt5.5-unrestricted.md: OK", "success")
                        ok += 1

                    # AGENTS.md
                    src = SCRIPT_DIR / "AGENTS.md"
                    if src.exists() and safe_copy(src, CODEX_DIR / "AGENTS.md"):
                        self._log("    AGENTS.md: OK", "success")
                        ok += 1

                    # config.toml
                    if merge_codex_config(CODEX_DIR / "config.toml"):
                        self._log("    config.toml: OK (model_instructions_file + MCP)", "success")
                        ok += 1

                # Skills
                if self.var_skills.get() and SKILL_SRC.exists():
                    skill_dst = CODEX_DIR / "skills" / "reverse-flow"
                    safe_mkdir(skill_dst)
                    for sub in ["references", "scripts", "agents"]:
                        src_dir = SKILL_SRC / sub
                        if src_dir.exists():
                            dst_dir = skill_dst / sub
                            safe_mkdir(dst_dir)
                            for f in src_dir.iterdir():
                                safe_copy(f, dst_dir / f.name)
                    safe_copy(SKILL_SRC / "SKILL.md", skill_dst / "SKILL.md")
                    self._log("    skills: OK", "success")
                    ok += 1

                self._log("", "normal")

            # ── Hermes ──
            if self.var_hermes.get():
                self._log("[Hermes]", "info")
                safe_mkdir(HERMES_DIR)
                if self.var_jailbreak.get():
                    src = SCRIPT_DIR / "hermes-files" / "hermes-config-bundle" / "SOUL.md"
                    if src.exists() and safe_copy(src, HERMES_DIR / "SOUL.md"):
                        self._log("    SOUL.md: OK", "success")
                        ok += 1
                    src = SCRIPT_DIR / "hermes-files" / "hermes-config-bundle" / "config.yaml"
                    if src.exists() and safe_copy(src, HERMES_DIR / "config.yaml"):
                        self._log("    config.yaml: OK", "success")
                        ok += 1
                self._log("", "normal")

            # ── OpenCode ──
            if self.var_opencode.get():
                self._log("[OpenCode]", "info")
                safe_mkdir(OPENCODE_DIR)
                oc_src = SCRIPT_DIR / "opencode-files" / "opencode-config-bundle"
                if self.var_jailbreak.get() and oc_src.exists():
                    safe_copy(oc_src / "opencode.json", OPENCODE_DIR / "opencode.json")
                    agent_dst = OPENCODE_DIR / ".opencode" / "agents"
                    safe_mkdir(agent_dst)
                    agent_src = oc_src / ".opencode" / "agents"
                    if agent_src.exists():
                        for f in agent_src.iterdir():
                            safe_copy(f, agent_dst / f.name)
                    prompt_dst = OPENCODE_DIR / "prompts"
                    safe_mkdir(prompt_dst)
                    prompt_src = oc_src / "prompts"
                    if prompt_src.exists():
                        for f in prompt_src.iterdir():
                            safe_copy(f, prompt_dst / f.name)
                    self._log("    OpenCode config: OK", "success")
                    ok += 1
                self._log("", "normal")

            # ── MCP Tools ──
            if self.var_mcp.get():
                self._log("[MCP Tools]", "info")
                if MCP_DIR.exists():
                    uv = shutil.which("uv")
                    if uv:
                        self._log("    Running uv sync...", "gray")
                        result = subprocess.run(
                            ["uv", "sync"], cwd=str(MCP_DIR),
                            capture_output=True, text=True, timeout=120
                        )
                        if result.returncode == 0:
                            self._log("    MCP dependencies: OK", "success")
                            ok += 1
                        else:
                            self._log(f"    MCP dependencies: FAIL ({result.stderr[:100]})", "error")
                            fail += 1
                    else:
                        self._log("    uv not found (pip install uv)", "warning")
                self._log("", "normal")

            # ── Python RE Libs ──
            if self.var_python_re.get():
                self._log("[Python RE Libraries]", "info")
                python = shutil.which("python")
                if python:
                    self._log("    Installing: lief frida angr capstone keystone-engine unicorn", "gray")
                    result = subprocess.run(
                        [python, "-m", "pip", "install", "--quiet",
                         "lief", "frida", "angr", "capstone", "keystone-engine", "unicorn"],
                        capture_output=True, text=True, timeout=300
                    )
                    if result.returncode == 0:
                        self._log("    Python RE libs: OK", "success")
                        ok += 1
                    else:
                        self._log(f"    Python RE libs: FAIL", "error")
                        fail += 1
                else:
                    self._log("    Python not found", "warning")
                self._log("", "normal")

            # ── Summary ──
            self._log("=" * 50, "info")
            if fail == 0:
                self._log(f"  Deploy complete! ({ok} items)", "success")
            else:
                self._log(f"  Deploy done ({ok} ok, {fail} fail)", "warning")
            self._log("  Restart your AI tool to apply changes.", "info")
            self._log("=" * 50, "info")

        except Exception as e:
            self._log(f"ERROR: {e}", "error")
        finally:
            self.progress.stop()
            self._set_buttons(True)

    def _verify(self):
        try:
            self._log("=" * 50, "info")
            self._log("  Verification", "info")
            self._log("=" * 50, "info")

            checks = [
                ("CLAUDE.md", CLAUDE_DIR / "CLAUDE.md", "Ghost"),
                ("system-prompt.md", CLAUDE_DIR / "system-prompt.md", "Ghost"),
                ("settings.json", CLAUDE_DIR / "settings.json", "bypassPermissions"),
                ("config.toml", CLAUDE_DIR / "config.toml", "system-prompt.md"),
                (".codex/gpt5.5-unrestricted.md", CODEX_DIR / "gpt5.5-unrestricted.md", "UNRESTRICTED"),
                (".codex/AGENTS.md", CODEX_DIR / "AGENTS.md", "Agent"),
                (".hermes/SOUL.md", HERMES_DIR / "SOUL.md", "Ghost"),
            ]

            ok = 0
            for name, path, pattern in checks:
                if path.exists():
                    content = path.read_text(encoding="utf-8", errors="ignore")
                    if pattern in content:
                        self._log(f"  {name}: OK", "success")
                        ok += 1
                    else:
                        self._log(f"  {name}: WARNING (pattern not found)", "warning")
                else:
                    self._log(f"  {name}: MISSING", "error")

            # MCP server
            mcp_py = MCP_DIR / "reverse_lab_tools_mcp.py"
            if mcp_py.exists():
                self._log(f"  MCP server: OK", "success")
                ok += 1
            else:
                self._log(f"  MCP server: MISSING", "error")

            self._log("", "normal")
            self._log(f"Result: {ok}/{len(checks)+1} checks passed", "success" if ok == len(checks)+1 else "warning")

        except Exception as e:
            self._log(f"ERROR: {e}", "error")
        finally:
            self.progress.stop()
            self._set_buttons(True)

    def _uninstall(self):
        try:
            self._log("=" * 50, "info")
            self._log("  Uninstall", "info")
            self._log("=" * 50, "info")

            removed = 0
            for d in CLAUDE_DIRS:
                for f in ["CLAUDE.md", "system-prompt.md", "config.toml", "settings.json"]:
                    p = d / f
                    if p.exists():
                        p.unlink()
                        self._log(f"  Removed: {p}", "success")
                        removed += 1
                hooks = d / ".claude" / "hooks"
                if hooks.exists():
                    shutil.rmtree(str(hooks))
                    self._log(f"  Removed: {hooks}", "success")
                    removed += 1
                wfs = d / ".claude" / "workflows"
                if wfs.exists():
                    shutil.rmtree(str(wfs))
                    self._log(f"  Removed: {wfs}", "success")
                    removed += 1

            self._log("", "normal")
            self._log(f"Removed {removed} items", "success")

        except Exception as e:
            self._log(f"ERROR: {e}", "error")
        finally:
            self.progress.stop()
            self._set_buttons(True)

    def run(self):
        # Style
        style = Style()
        style.configure("Custom.TLabelframe", background="#313244", foreground="#cdd6f4")
        style.configure("Custom.TLabelframe.Label", background="#313244", foreground="#89b4fa", font=("Segoe UI", 10, "bold"))
        style.configure("Custom.Horizontal.TProgressbar", troughcolor="#313244", background="#89b4fa")

        self.root.mainloop()


if __name__ == "__main__":
    app = InstallerGUI()
    app.run()
