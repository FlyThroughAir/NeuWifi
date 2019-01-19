@echo off


::echo filename=%date:~0,4%-%date:~5,2%-%date:~8,2% %time:~0,2%:%time:~3,2%:%time:~6,2% >> nohup.out
::goto :eof

::得到盘符和页面
set SPARK_DIST_CLASSPATH=%~d0%~p0


::得到盘符和页面循环方式
::FOR /F %%i IN ('echo %~d0%~p0') DO @set SPARK_DIST_CLASSPATH=%%i
::echo SPARK_DIST_CLASSPATH = %SPARK_DIST_CLASSPATH%


SET Content=%SPARK_DIST_CLASSPATH%MyWifi.py
::echo Content = python %Content% --type login



::echo param = %1%
@set param=%1%
::echo param = %param%
if "%param%"=="" goto :login

if "%param%"=="login" goto %param%
if "%param%"=="logout" goto %param%
goto errorcase


:login
python %Content% --type login

goto :eof
 
:logout
python %Content% --type logout
goto :eof


:errorcase
echo "input error！require [login|logout]"




