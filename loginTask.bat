@echo off


::得到盘符和页面
set SPARK_DIST_CLASSPATH=%~d0%~p0
SET Content=%SPARK_DIST_CLASSPATH%run.bat
::echo Content = %Content%


@set param=%1%
::echo param = %param%

if "%param%"=="create" goto %param%
if "%param%"=="delete" goto %param%
::goto errorcase


:create
:: 创建 取消冲突 名称 类型 间隔 持续时间 程序或命令
SCHTASKS /Create /F /TN mytask /SC hourly /mo 2 /ST 00:00 /du 0004:00 /TR  call %Content% login >> nohup.out
if %ERRORLEVEL%==0 echo schedule have been created successful！
if not %ERRORLEVEL%==0 echo can't create！require authority!you can login as Admin!
echo schedule create successful！
goto :eof

 
:delete
SCHTASKS /delete /TN mytask /F
echo %ERRORLEVEL%
if %ERRORLEVEL%==0 echo schedule have been cancelled！
if not %ERRORLEVEL%==0 echo can't cancel！require authority! you can login as Admin!
goto :eof


:errorcase
echo "input error！require [create|delete]"
goto :eof



