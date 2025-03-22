@echo off
title Toontown Online #_BR #JP #FR #ES - AI Server
cd ../..

:main 
$WINTOOLS/bin/python.exe -m toontown.ai.AIStart $TOONTOWN/src/launcher/Configrc.prc QA=$OTP/built/Configrc.prc EN 2011=$TOONTOWN/src/launcher/client_Configrc.prc
pause
goto :main
