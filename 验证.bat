@echo off
chcp 65001 >nul 2>&1
title open-tgtylab Verify
set "PS_SCRIPT=%~dp0tgtylab-files\deploy.ps1"
if not exist "%PS_SCRIPT%" (
    echo [!] deploy.ps1 not found
    pause
    exit /b 1
)
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%PS_SCRIPT%" -Verify
pause
