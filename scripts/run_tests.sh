#!/bin/bash
# Tests ausführen

echo "🧪 Führe Tests aus..."

# Pytest mit Coverage
uv run pytest tests/ -v --tb=short

echo "✅ Tests abgeschlossen!"

