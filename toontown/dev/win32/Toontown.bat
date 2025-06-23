@echo off
title Toontown Online - Game Client
cd..

rem Read the contents of PPYTHON_PATH into %PPYTHON_PATH%:
set /P PPYTHON_PATH=<PPYTHON_PATH

set LOGIN_TOKEN=dev

%PYTHON_LOCATION% -m toontown.launcher.StartToontownLauncher #br 2005 a 2011
%PYTHON_LOCATION% -m toontown.launcher.QuickStartLauncher #en 2013
pause
