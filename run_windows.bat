@echo off

echo ========================================
echo ComicCraft - Starting Application
echo ========================================

if not exist ".venv" (
    echo Creating virtual environment...
    py -3.11 -m venv .venv
)

call .venv\Scripts\activate

echo Installing dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt

echo.
echo Starting ComicCraft...
echo Open http://127.0.0.1:8000
echo.

uvicorn app.main:app --reload

pause