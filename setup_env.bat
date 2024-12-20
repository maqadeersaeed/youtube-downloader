@echo off
:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python and try again.
    exit /b 1
)

:: Create virtual environment
echo Creating virtual environment...
python -m venv env
if %errorlevel% neq 0 (
    echo Failed to create virtual environment.
    exit /b 1
)

:: Activate the virtual environment
echo Activating virtual environment...
call env\Scripts\activate
if %errorlevel% neq 0 (
    echo Failed to activate virtual environment.
    exit /b 1
)

:: Install dependencies from requirements.txt
echo Installing dependencies...
pip install --upgrade pip
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Failed to install dependencies.
    exit /b 1
)

echo Virtual environment setup complete and dependencies installed.
pause
