@echo off
REM ===== VideoAI Auto-Render (Windows Task Scheduler, daily 05:00) =====
REM cd repo -> docker compose up -> render_queue.sh (render HD + auto-publish) -> log with timestamp.
REM Requires: Docker Desktop running when this task fires.
cd /d "C:\Users\TienNB\Desktop\video-ai"
for /f "usebackq delims=" %%i in (`powershell -NoProfile -Command "Get-Date -Format yyyyMMdd"`) do set "DS=%%i"
for /f "usebackq delims=" %%i in (`powershell -NoProfile -Command "Get-Date -Format 'yyyy-MM-dd HH:mm:ss'"`) do set "TS=%%i"
set "LOG=output\auto_render_%DS%.log"
echo. >> "%LOG%"
echo ======== AutoRender START %TS% ======== >> "%LOG%"
docker compose up -d >> "%LOG%" 2>&1
docker compose exec -T videoai bash render_queue.sh >> "%LOG%" 2>&1
for /f "usebackq delims=" %%i in (`powershell -NoProfile -Command "Get-Date -Format 'yyyy-MM-dd HH:mm:ss'"`) do set "TE=%%i"
echo ======== AutoRender END %TE% ======== >> "%LOG%"
