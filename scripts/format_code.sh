#!/bin/bash
# Code automatisch formatieren

echo "🎨 Formatiere Python-Code..."

# Black für Formatierung
uv run black modul-* tests/

# Ruff für Auto-Fixes (optional)
echo "Running ruff auto-fix..."
uv run ruff check --fix modul-* tests/

echo "✅ Code-Formatierung abgeschlossen!"

