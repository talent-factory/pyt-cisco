# Installation und Setup

## 📋 Übersicht

Diese Anleitung hilft Ihnen, Ihre Entwicklungsumgebung für den Python CISCO Kurs einzurichten.

## 🎯 Zwei Optionen

### Option 1: GitHub Codespaces (Empfohlen für Anfänger)

**Vorteile:**
- ✅ Keine lokale Installation nötig
- ✅ Sofort einsatzbereit
- ✅ Funktioniert auf jedem Gerät mit Browser
- ✅ Konsistente Umgebung für alle

**Schritte:**
1. GitHub-Account erstellen (falls noch nicht vorhanden)
2. Repository öffnen
3. Auf "Code" → "Codespaces" → "Create codespace" klicken
4. Warten bis die Umgebung bereit ist
5. Loslegen!

### Option 2: Lokale Installation

**Vorteile:**
- ✅ Funktioniert offline
- ✅ Volle Kontrolle über die Umgebung
- ✅ Schnellere Performance

**Voraussetzungen:**
- Python 3.11 oder höher
- Git
- VS Code
- Terminal/Kommandozeile

## 🔧 Lokale Installation - Schritt für Schritt

### 1. Python installieren

**Windows:**
1. Besuchen Sie [python.org](https://www.python.org/downloads/)
2. Laden Sie Python 3.11+ herunter
3. Führen Sie den Installer aus
4. ✅ Wichtig: "Add Python to PATH" aktivieren!

**macOS:**
```bash
# Mit Homebrew
brew install python@3.11
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3.11 python3.11-venv python3-pip
```

### 2. Git installieren

**Windows:**
- Download von [git-scm.com](https://git-scm.com/)

**macOS:**
```bash
brew install git
```

**Linux:**
```bash
sudo apt install git
```

### 3. VS Code installieren

1. Download von [code.visualstudio.com](https://code.visualstudio.com/)
2. Installieren Sie die Python Extension

### 4. uv installieren

**macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**Alternative (mit pip):**
```bash
pip install uv
```

### 5. Repository klonen

```bash
git clone https://github.com/IHR-USERNAME/pyt-cisco.git
cd pyt-cisco
```

### 6. Dependencies installieren

```bash
# uv sync erstellt automatisch eine virtuelle Umgebung (.venv)
# und installiert alle Dependencies
uv sync

# Für Development-Dependencies:
uv sync --all-extras
```

## ✅ Installation überprüfen

```bash
# Python-Version prüfen
uv run python --version

# Jupyter starten (optional)
uv run jupyter notebook

# Tests ausführen
uv run pytest
```

## 🔄 Tägliche Nutzung

```bash
# Projekt-Dependencies aktualisieren
uv sync

# Python-Skript ausführen
uv run python mein_script.py

# Jupyter Notebook starten
uv run jupyter notebook

# Tests ausführen
uv run pytest

# Code formatieren
uv run black .

# Code-Qualität prüfen
uv run flake8 .
```

## 🆘 Probleme?

Bei Problemen kontaktieren Sie Ihren Kursleiter oder erstellen Sie ein Issue im Repository.

