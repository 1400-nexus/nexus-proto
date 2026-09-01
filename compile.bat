@echo off
setlocal enabledelayedexpansion

set PROTO_DIR=proto
set OUT_DIR=generated

if not exist "%OUT_DIR%\cpp" mkdir "%OUT_DIR%\cpp"
if not exist "%OUT_DIR%\python" mkdir "%OUT_DIR%\python"
if not exist "%OUT_DIR%\typescript" mkdir "%OUT_DIR%\typescript"

echo Cleaning old generated files...
del /q /s "%OUT_DIR%\cpp\*" >nul 2>&1
del /q /s "%OUT_DIR%\python\*" >nul 2>&1
del /q /s "%OUT_DIR%\typescript\*" >nul 2>&1

set PROTO_FILES=
for /r "%PROTO_DIR%" %%f in (*.proto) do (
    set PROTO_FILES=!PROTO_FILES! "%%f"
)

if "%PROTO_FILES%"=="" (
    echo Error: No .proto files found in %PROTO_DIR%
    exit /b 1
)

echo Compiling Protobuf files for C++, Python, and TypeScript...

protoc ^
  --proto_path="%PROTO_DIR%" ^
  --cpp_out="%OUT_DIR%\cpp" ^
  --python_out="%OUT_DIR%\python" ^
  --pyi_out="%OUT_DIR%\python" ^
  --ts_out="%OUT_DIR%\typescript" ^
  !PROTO_FILES!

if %ERRORLEVEL% equ 0 (
    echo Done! Compiled outputs placed in %OUT_DIR%/
) else (
    echo Error: Protobuf compilation failed with exit code %ERRORLEVEL%.
)

endlocal