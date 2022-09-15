@echo off
python Mixiot.py
if  errorlevel 1 goto ERROR
goto EOF
:ERROR
py Mixiot.py
:EOF 