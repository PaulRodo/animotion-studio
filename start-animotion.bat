@echo off
chcp 65001 >nul
cd /d "%~dp0"
where python >nul 2>nul
if errorlevel 1 (
  echo Python 3 не найден. Установи Python 3.10+ и включи Add Python to PATH.
  pause
  exit /b 1
)
echo AniMotion Studio 0.3: http://127.0.0.1:8090
echo Оставь это окно открытым во время работы.
start "" http://127.0.0.1:8090
python run_server.py
pause
