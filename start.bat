@echo off
python Mixiot.py
if not %errorlevel%==0 py Mixiot.py
