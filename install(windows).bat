@echo off

REM Check if Python is installed
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python is not installed. Installing Python...
    REM Download Python installer
    bitsadmin /transfer pythonInstaller https://www.python.org/ftp/python/3.10.2/python-3.10.2-amd64.exe %TEMP%\python_installer.exe
    REM Install Python
    %TEMP%\python_installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
)

REM Install requests Python module if not installed
python -c "import requests" 2>nul
if %errorlevel% neq 0 (
    echo Installing requests module...
    python -m pip install requests
)

REM Run main.py
echo Running main.py...

cls
python main.py
