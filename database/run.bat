@echo off
REM ============================================================
REM  Initialisation base gestion_stock via mysql-connector-python
REM ============================================================
setlocal
cd /d "%~dp0"

echo ==========================================
echo   Initialisation MySQL - XAMPP (localhost)
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
        echo [ERREUR] Python introuvable. Installez Python et ajoutez-le au PATH.
        pause
        exit /b 1
    )
)

REM --- Verification de mysql-connector-python ---
%PY% -c "import mysql.connector" >nul 2>&1
if not %ERRORLEVEL%==0 (
    echo [INFO] Installation de mysql-connector-python...
    %PY% -m pip install --quiet mysql-connector-python
    if not %ERRORLEVEL%==0 (
        echo [ERREUR] Echec installation de mysql-connector-python.
        pause
        exit /b 1
    )
)

REM --- Execution ---
%PY% init.py
set "RC=%ERRORLEVEL%"

echo.
if "%RC%"=="0" (
    echo [OK] Script termine avec succes.
) else (
    echo [ECHEC] Le script a retourne le code %RC%.
)
pause
endlocal
exit /b %RC%