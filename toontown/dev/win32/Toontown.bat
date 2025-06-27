@echo off
title Toontown Online #BR #FR #JP #ES - Game Client
cd..

$WINTOOLS/bin/python.exe -m toontown.launcher.StartToontownLauncher #2005 a #2011
$WINTOOLS/bin/python.exe  -m toontown.launcher.QuickStartLauncher #2013
pause
