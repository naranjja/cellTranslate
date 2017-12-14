@echo off

for /f "delims== tokens=1,2" %%G in (settings.conf) do set %%G=%%H

call python translate.py

echo DONE! Check output/ folder for your spreadsheet and look at column %COLUMN%!
pause
