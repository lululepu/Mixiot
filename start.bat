@echo off
:someRoutine
setlocal
%@Try%
  python Mixiot.py
%@EndTry%
:@Catch
  py Mixiot.py
:@EndCatch
