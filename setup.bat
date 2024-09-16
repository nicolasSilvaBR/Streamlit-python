@echo off
setlocal

:: Define the path for the virtual environment and installer
set ENV_PATH=streamlitEnv
set PYTHON_INSTALLER=python-installer.exe

:: Check if Python is installed
python --version >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo Python is not installed. Downloading and installing Python...

    :: Check if the installer exists
    if not exist %PYTHON_INSTALLER% (
        echo Python installer not found. Please download it from https://www.python.org and place it in the script directory.
        pause
        exit /b 1
    )
    
    :: Run the Python installer
    echo Installing Python...
    %PYTHON_INSTALLER% /quiet InstallAllUsers=1 PrependPath=1
    if %ERRORLEVEL% neq 0 (
        echo Python installation failed. Please install Python manually.
        pause
        exit /b 1
    )
) else (
    echo Python is already installed.
)

:: Check if the virtual environment already exists
if not exist %ENV_PATH%\Scripts\activate (
    echo Creating virtual environment...
    python -m venv %ENV_PATH%
) else (
    echo Virtual environment already exists.
)

:: Activate the virtual environment
call %ENV_PATH%\Scripts\activate

:: Install the dependencies
echo Installing dependencies...
pip install -r requirements.txt

:: Run streamlit in a new command window and keep it open
echo Starting Streamlit application...
start "" cmd /k "streamlit run fundamentals.py"

endlocal
