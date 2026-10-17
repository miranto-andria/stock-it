@echo off
REM ============================================================
REM  Peuplement de la base stock_it (sans Faker)
REM ============================================================
setlocal
cd /d "%~dp0.."

echo ==========================================
echo   Peuplement MySQL XAMPP - Base : stock_it
echo   (stdlib uniquement)
echo ==========================================

REM --- Detection Python ---
where python >nul 2>&1
if %ERRORLEVEL%==0 (
    set "PY=python"
) else (
    where py >nul 2>&1
    if %ERRORLEVEL%==0 (
        set "PY=py"
    ) else (
        echo [ERREUR] Python introuvable.
        pause
        exit /b 1
    )
)

REM --- Verification de mysql-connector-python ---
%PY% -c "import mysql.connector" >nul 2>&1
if not %ERRORLEVEL%==0 (
    echo [INFO] Installation de mysql-connector-python...
    %PY% -m pip install --quiet mysql-connector-python
)

REM --- Execution ---
%PY% "database\seed.py"
set "RC=%ERRORLEVEL%"

echo.
if "%RC%"=="0" (
    echo [OK] Peuplement termine avec succes.
) else (
    echo [ECHEC] Le script a retourne le code %RC%.
)
pause
endlocal
exit /b %RC%