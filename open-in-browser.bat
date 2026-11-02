@echo off
chcp 65001 >nul
setlocal
set "APP=%~dp0index.html"

if not exist "%APP%" (
  echo Не найден index.html. Распакуй весь архив проекта в одну папку.
  pause
  exit /b 1
)

if exist "%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe" (
  start "" "%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe" "%APP%"
  exit /b 0
)
if exist "%ProgramFiles%\Microsoft\Edge\Application\msedge.exe" (
  start "" "%ProgramFiles%\Microsoft\Edge\Application\msedge.exe" "%APP%"
  exit /b 0
)
if exist "%LOCALAPPDATA%\Microsoft\Edge\Application\msedge.exe" (
  start "" "%LOCALAPPDATA%\Microsoft\Edge\Application\msedge.exe" "%APP%"
  exit /b 0
)
if exist "%ProgramFiles%\Google\Chrome\Application\chrome.exe" (
  start "" "%ProgramFiles%\Google\Chrome\Application\chrome.exe" "%APP%"
  exit /b 0
)
if exist "%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe" (
  start "" "%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe" "%APP%"
  exit /b 0
)
if exist "%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe" (
  start "" "%LOCALAPPDATA%\Google\Chrome\Application\chrome.exe" "%APP%"
  exit /b 0
)

where msedge.exe >nul 2>nul
if not errorlevel 1 (
  start "" msedge.exe "%APP%"
  exit /b 0
)
where chrome.exe >nul 2>nul
if not errorlevel 1 (
  start "" chrome.exe "%APP%"
  exit /b 0
)

echo Не удалось автоматически найти Chrome или Edge.
echo Нажми правой кнопкой на index.html и выбери Открыть с помощью - Microsoft Edge или Google Chrome.
pause
