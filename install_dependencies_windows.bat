@echo off
setlocal

REM Define the dependencies
set DEPENDENCIES="dependency1 dependency2 dependency3"

REM Define the path to the installation directory
set INSTALL_DIR="C:\path\to\installation\directory"

REM Install the dependencies
for %%d in (%DEPENDENCIES%) do (
    echo Installing %%d...
    cd %INSTALL_DIR%
    npm install %%d
)

REM Export environment variables
setx API_KEY "your-api-key"
setx CONFIG_PATH "C:\path\to\config\file"

REM End of the script
endlocal
echo Dependencies installed successfully.
pause