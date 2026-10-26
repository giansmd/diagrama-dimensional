@echo off
title Generador Dimensional de Buyers
echo ============================================================
echo   Iniciando Generador de Analisis Dimensional Conformado...
echo ============================================================
cd /d "%~dp0"
start "" "index.html"
python server.py
pause
