@echo off

set /p x=Would you like to install Chocolatey? (Y/N) 
if /i "%x%"=="y" (
  call @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" ^
    -NoProfile ^ 
    -InputFormat None ^
    -ExecutionPolicy Bypass ^
    -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" ^ 
    && set "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
)

set /p x=Would you like to install Python3? (Y/N) 
if /i "%x%"=="y" ( call choco install python3 -y )

set /p x=Would you like to install Google Cloud SDK? (Y/N) 
if /i "%x%"=="y" ( call choco install gcloudsdk -y )

set /p x=Would you like to install the Python requirements? (Y/N) 
if /i "%x%"=="y" ( call pip install --upgrade -r requirements.txt )

echo Installation finished!
pause
