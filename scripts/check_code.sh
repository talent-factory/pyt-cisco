#!/bin/bash
# Code-Qualitätsprüfung

echo "🔍 Prüfe Python-Code..."

# Flake8 für Linting
echo "Running flake8..."
uv run flake8 modul-* --max-line-length=88 --exclude=__pycache__,*.pyc

# Black für Formatierung (nur Check)
echo "Running black (check only)..."
uv run black --check modul-* tests/

# Ruff für schnelles Linting (optional)
echo "Running ruff..."
uv run ruff check modul-* tests/

echo "✅ Code-Prüfung abgeschlossen!"

