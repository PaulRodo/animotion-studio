@echo off
chcp 65001 >nul
title AniMotion - Проверка видеокарты
echo ==============================================
echo          AniMotion - Проверка GPU
echo ==============================================
echo.
where nvidia-smi >nul 2>nul
if errorlevel 1 (
  echo nvidia-smi не найден. Проверь, установлен ли драйвер NVIDIA.
  echo.
  echo Открой Диспетчер задач ^> Производительность ^> GPU.
) else (
  nvidia-smi --query-gpu=name,memory.total,memory.free,driver_version --format=csv
)
echo.
echo Системная память:
wmic computersystem get TotalPhysicalMemory 2>nul
if errorlevel 1 echo Сведения о RAM можно посмотреть в Диспетчере задач ^> Производительность ^> Память.
echo.
echo Для AniMotion с RTX 2050 4 ГБ начинай с маленьких картинок и batch 1.
echo Не запускай тяжёлые video-workflow без отдельной проверки.
echo.
pause
