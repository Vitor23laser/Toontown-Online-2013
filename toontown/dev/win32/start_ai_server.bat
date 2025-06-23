@echo off
title Toontown Online #_BR #JP #FR #ES - AI Server
cd ../..

:main 
$WINTOOLS/bin/python.exe -m toontown.ai.AIStart #-m toontown.ai.ServiceStart #-m toontown.ai.UlityStart --base-channel 401000000 ^
               --max-channels 999999 --stateserver 4002 ^
               --messagedirector-ip localhost ^
               --eventlogger-ip localhost ^ #colocar seu servidor aqui
               --district-name "Toon Valley" #--disctrict-name "Altos dos Irados" #BR
goto main
