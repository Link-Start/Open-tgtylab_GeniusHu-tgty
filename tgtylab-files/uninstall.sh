#!/bin/bash
# open-tgtylab Uninstall - macOS/Linux
CLAUDE_DIR="$HOME/.claude"
RED='\033[0;31m'; GREEN='\033[0;32m'; CYAN='\033[0;36m'; GRAY='\033[0;37m'; NC='\033[0m'

echo ""
echo -e "${CYAN}============================================${NC}"
echo -e "${RED}  open-tgtylab Uninstall${NC}"
echo -e "${CYAN}============================================${NC}"
echo ""

ALL_DIRS=("$CLAUDE_DIR")
for candidate in \
    "$HOME/Library/Application Support/claude" \
    "$HOME/Library/Application Support/claude-code" \
    "$HOME/Library/Application Support/Claude" \
    "$HOME/Library/Application Support/Claude Code"; do
    if [ -d "$candidate" ] && [ "$candidate" != "$CLAUDE_DIR" ]; then
        ALL_DIRS+=("$candidate")
    fi
done

echo -e "${GRAY}Will remove config from:${NC}"
for d in "${ALL_DIRS[@]}"; do echo -e "${GRAY}  - $d${NC}"; done
echo ""

read -p "Confirm uninstall? (y/N): " confirm
if [[ ! "$confirm" =~ ^[Yy]$ ]]; then
    echo "Cancelled."
    read -p "Press Enter to exit..."
    exit 0
fi

total=0
for dir in "${ALL_DIRS[@]}"; do
    if [ -d "$dir" ]; then
        echo -e "${CYAN}[*] Cleaning: $dir${NC}"
        # Remove top-level config files
        for f in CLAUDE.md system-prompt.md config.toml settings.json; do
            if [ -f "$dir/$f" ]; then
                rm -f "$dir/$f" 2>/dev/null
                echo -e "${GREEN}    Removed $f${NC}"
                total=$((total + 1))
            fi
        done
        # Remove .claude/hooks/
        if [ -d "$dir/.claude/hooks" ]; then
            rm -rf "$dir/.claude/hooks" 2>/dev/null
            echo -e "${GREEN}    Removed .claude/hooks/${NC}"
            total=$((total + 1))
        fi
        # Remove .claude/workflows/
        if [ -d "$dir/.claude/workflows" ]; then
            rm -rf "$dir/.claude/workflows" 2>/dev/null
            echo -e "${GREEN}    Removed .claude/workflows/${NC}"
            total=$((total + 1))
        fi
        # Remove .claude/settings.local.json
        if [ -f "$dir/.claude/settings.local.json" ]; then
            rm -f "$dir/.claude/settings.local.json" 2>/dev/null
            echo -e "${GREEN}    Removed .claude/settings.local.json${NC}"
            total=$((total + 1))
        fi
        # Remove backups
        if [ -d "$dir/backups" ]; then
            rm -rf "$dir/backups" 2>/dev/null
            echo -e "${GREEN}    Removed backups/${NC}"
            total=$((total + 1))
        fi
        # Remove empty .claude dir
        if [ -d "$dir/.claude" ] && [ -z "$(ls -A "$dir/.claude" 2>/dev/null)" ]; then
            rmdir "$dir/.claude" 2>/dev/null
        fi
    fi
done

echo ""
echo -e "${CYAN}============================================${NC}"
echo -e "${GREEN}  Uninstall complete. Removed $total items.${NC}"
echo -e "${CYAN}============================================${NC}"
echo ""
read -p "Press Enter to exit..."
