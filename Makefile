.PHONY: help install sync update clean test format check lint jupyter notebook run-jupyter dev-install

# Default target
help:
	@echo "📚 Python CISCO Kurs - Makefile Kommandos"
	@echo ""
	@echo "🔧 Setup & Installation:"
	@echo "  make install        - uv installieren und Projekt-Dependencies installieren"
	@echo "  make sync           - Dependencies synchronisieren (erstellt .venv)"
	@echo "  make update         - Dependencies aktualisieren"
	@echo "  make dev-install    - Development-Dependencies installieren"
	@echo ""
	@echo "🧪 Testing & Quality:"
	@echo "  make test           - Tests ausführen"
	@echo "  make test-verbose   - Tests mit ausführlicher Ausgabe"
	@echo "  make coverage       - Tests mit Coverage-Report"
	@echo ""
	@echo "🎨 Code-Formatierung & Linting:"
	@echo "  make format         - Code automatisch formatieren (black + ruff)"
	@echo "  make check          - Code-Qualität prüfen (ohne Änderungen)"
	@echo "  make lint           - Linting mit flake8 und ruff"
	@echo "  make fix            - Auto-Fix mit ruff"
	@echo ""
	@echo "📓 Jupyter:"
	@echo "  make jupyter        - Jupyter Notebook starten"
	@echo "  make notebook       - Jupyter Notebook starten (Alias)"
	@echo "  make lab            - JupyterLab starten"
	@echo ""
	@echo "🧹 Cleanup:"
	@echo "  make clean          - Temporäre Dateien löschen"
	@echo "  make clean-all      - Alles löschen (inkl. .venv)"
	@echo ""
	@echo "ℹ️  Info:"
	@echo "  make info           - Projekt-Informationen anzeigen"

# Setup & Installation
install:
	@echo "🔧 Installiere uv und Projekt-Dependencies..."
	@command -v uv >/dev/null 2>&1 || (echo "Installing uv..." && curl -LsSf https://astral.sh/uv/install.sh | sh)
	uv sync

sync:
	@echo "🔄 Synchronisiere Dependencies..."
	uv sync

update:
	@echo "⬆️  Aktualisiere Dependencies..."
	uv sync --upgrade

dev-install:
	@echo "🛠️  Installiere Development-Dependencies..."
	uv sync --all-extras

# Testing
test:
	@echo "🧪 Führe Tests aus..."
	uv run pytest tests/ -v

test-verbose:
	@echo "🧪 Führe Tests mit ausführlicher Ausgabe aus..."
	uv run pytest tests/ -vv --tb=long

coverage:
	@echo "📊 Führe Tests mit Coverage aus..."
	uv run pytest tests/ --cov=. --cov-report=html --cov-report=term

# Code Quality
format:
	@echo "🎨 Formatiere Code..."
	uv run black modul-* tests/ || true
	uv run ruff check --fix modul-* tests/ || true
	@echo "✅ Code-Formatierung abgeschlossen!"

check:
	@echo "🔍 Prüfe Code-Qualität (ohne Änderungen)..."
	uv run black --check modul-* tests/ || true
	uv run ruff check modul-* tests/ || true

lint:
	@echo "🔍 Führe Linting aus..."
	uv run flake8 modul-* tests/ --max-line-length=88 --exclude=__pycache__,*.pyc || true
	uv run ruff check modul-* tests/ || true

fix:
	@echo "🔧 Auto-Fix mit ruff..."
	uv run ruff check --fix modul-* tests/

# Jupyter
jupyter:
	@echo "📓 Starte Jupyter Notebook..."
	uv run jupyter notebook

notebook: jupyter

lab:
	@echo "🔬 Starte JupyterLab..."
	uv run jupyter lab

# Cleanup
clean:
	@echo "🧹 Lösche temporäre Dateien..."
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	find . -type f -name "*.pyo" -delete 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".ruff_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "htmlcov" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name ".coverage" -delete 2>/dev/null || true
	rm -rf build/ dist/ 2>/dev/null || true
	@echo "✅ Cleanup abgeschlossen!"

clean-all: clean
	@echo "🧹 Lösche .venv und uv.lock..."
	rm -rf .venv
	rm -f uv.lock
	@echo "✅ Vollständiges Cleanup abgeschlossen!"

# Info
info:
	@echo "📋 Projekt-Informationen:"
	@echo ""
	@echo "Python Version:"
	@uv run python --version
	@echo ""
	@echo "uv Version:"
	@uv --version
	@echo ""
	@echo "Installierte Pakete:"
	@uv pip list 2>/dev/null || echo "Keine Pakete installiert. Führe 'make install' aus."

