@echo off
:: Check if the virtual environment exists
if not exist "env\Scripts\activate" (
    echo Virtual environment not found. Please set up the environment by running setup_env.bat.
    exit /b 1
)

:: Activate the virtual environment
echo Activating virtual environment...
call env\Scripts\activate
if %errorlevel% neq 0 (
    echo Failed to activate virtual environment.
    exit /b 1
)

:: Run the Python script
echo Running script.py...
python script.py
if %errorlevel% neq 0 (
    echo Failed to execute script.py.
    exit /b 1
)

:: Deactivate the virtual environment
echo Deactivating virtual environment...
deactivate

echo Script execution complete.
pause
