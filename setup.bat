@echo off
echo.
echo ╔══════════════════════════════════════╗
echo ║         الارتقاء — Setup             ║
echo ║   Islamic Self-Improvement OS        ║
echo ╚══════════════════════════════════════╝
echo.

REM Check Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed. Download from https://python.org
    pause
    exit /b 1
)

REM Create virtual environment
echo Creating virtual environment...
python -m venv venv
call venv\Scripts\activate.bat

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt -q

REM Run migrations
echo Setting up database...
python manage.py migrate --run-syncdb

echo.
echo ════════════════════════════════════════
echo [OK] Setup complete!
echo.
echo To start the app, run:
echo   venv\Scripts\activate
echo   python manage.py runserver
echo.
echo Then open http://127.0.0.1:8000 in your browser.
echo ════════════════════════════════════════
pause
