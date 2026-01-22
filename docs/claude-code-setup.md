# Claude Code Setup - Sicherheit & Best Practices

Eine Anleitung zur sicheren Verwendung von Claude Code in GitHub Codespaces.

## 🔒 Wichtig: Codespace-Isolation verstehen

### Was ist ein Codespace?

Ein **GitHub Codespace** ist eine vollständige, cloudbasierte Entwicklungsumgebung:

- 🖥️ Eigene virtuelle Maschine (VM)
- 🔐 Komplett isoliert von anderen Codespaces
- 👤 Nur für dich zugänglich
- 🗑️ Kann jederzeit gelöscht und neu erstellt werden

### ✅ Was das für dich bedeutet

**JEDER Studierende hat seinen EIGENEN Codespace:**

```
Dozierende:
├─ Codespace von Dozent ─→ [Isolierte VM] ─→ Dozenten-API-Keys

Studierende:
├─ Codespace von Student A ─→ [Isolierte VM] ─→ API-Keys von Student A
├─ Codespace von Student B ─→ [Isolierte VM] ─→ API-Keys von Student B
└─ Codespace von Student C ─→ [Isolierte VM] ─→ API-Keys von Student C
```

**Wichtig:** Die API-Keys der Dozierenden sind **NICHT** in den Codespaces der Studierenden verfügbar!

## 🚀 Claude Code einrichten

### Voraussetzungen

1. **Anthropic API-Key** (kostenpflichtig)
   - Registrierung: [https://console.anthropic.com](https://console.anthropic.com)
   - Account erstellen und Zahlungsmethode hinterlegen
   - API-Key erstellen unter "API Keys"

2. **GitHub Codespace**
   - Repository auf GitHub öffnen
   - "Code" → "Codespaces" → "Create codespace on develop"

### Schritt 1: Codespace starten

```bash
# Warte bis der Codespace vollständig geladen ist
# Claude Code wird automatisch installiert (siehe devcontainer.json)

# Prüfe die Installation
claude --version
```

### Schritt 2: API-Key sicher konfigurieren

**⚠️ WICHTIG: Es gibt 3 Methoden - wähle die für dich passende:**

#### Methode 1: GitHub Codespace Secrets (Empfohlen für wiederkehrende Nutzung)

**Vorteil:** API-Key wird automatisch in allen neuen Codespaces verfügbar

1. Öffne GitHub Settings:
   - `https://github.com/settings/codespaces`

2. Klicke auf "New secret"

3. Erstelle Secret:
   - **Name:** `ANTHROPIC_API_KEY`
   - **Value:** `sk-ant-...` (dein API-Key)
   - **Repository access:** Wähle `talent-factory/pyt-cisco`

4. Im Codespace Terminal:
   ```bash
   # Prüfe ob der Key verfügbar ist
   echo $ANTHROPIC_API_KEY

   # Claude Code nutzt automatisch die Umgebungsvariable
   claude doctor
   ```

#### Methode 2: .env Datei (Einfach, aber nur lokal)

**Vorteil:** Schnell und einfach für einzelne Codespace-Instanz

1. Erstelle `.env` Datei im Projekt-Root:
   ```bash
   # Im Codespace Terminal
   cat > .env << 'EOF'
   ANTHROPIC_API_KEY=sk-ant-dein-api-key-hier
   EOF
   ```

2. Lade die Umgebungsvariablen:
   ```bash
   # In jeder neuen Terminal-Session ausführen
   export $(cat .env | xargs)

   # Oder füge zu ~/.bashrc hinzu (dauerhaft im Codespace)
   echo 'export $(cat .env 2>/dev/null | xargs)' >> ~/.bashrc
   ```

3. Prüfe:
   ```bash
   claude doctor
   ```

**⚠️ WICHTIG:** Die `.env` Datei ist bereits in `.gitignore` und wird **NIE** zu Git hinzugefügt!

#### Methode 3: Manuelles Login (Temporär)

**Vorteil:** Kein API-Key nötig, aber weniger bequem

```bash
# Claude Code startet interaktiven Login-Flow
claude login

# Folge den Anweisungen im Browser
```

### Schritt 3: Claude Code verwenden

```bash
# Claude Code starten
claude

# Oder direkter Befehl
claude "Erstelle ein Python-Programm das Hello World ausgibt"

# Setup prüfen
claude doctor
```

## 🔐 Sicherheits-Best Practices

### ✅ DO - Mach das:

1. **Verwende GitHub Codespace Secrets**
   - Sicher und automatisch verfügbar
   - Nie im Code sichtbar

2. **Prüfe .gitignore**
   - `.env` sollte drin stehen
   - Keine API-Keys committen

3. **Lösche alte Codespaces**
   - Unter `https://github.com/codespaces`
   - Spart Speicherplatz und Geld

4. **Rotiere API-Keys regelmäßig**
   - Besonders nach öffentlichen Commits
   - In Anthropic Console neue Keys erstellen

5. **Verwende API-Key-Limits**
   - Setze monatliche Ausgabelimits in Anthropic Console
   - Verhindert hohe Kosten bei Missbrauch

### ❌ DON'T - Mach das NICHT:

1. **NIEMALS API-Keys committen**
   ```bash
   # ❌ FALSCH
   git add .env
   git commit -m "Add API key"

   # ✅ RICHTIG
   # .env ist in .gitignore und wird automatisch ignoriert
   ```

2. **NIEMALS API-Keys in Code hardcoden**
   ```python
   # ❌ FALSCH
   api_key = "sk-ant-123456789"

   # ✅ RICHTIG
   import os
   api_key = os.environ.get("ANTHROPIC_API_KEY")
   ```

3. **NIEMALS API-Keys teilen**
   - Nicht in Discord/Slack/WhatsApp
   - Nicht in Screenshots
   - Nicht in Pull Requests

4. **NIEMALS fremde API-Keys verwenden**
   - Jeder braucht seinen eigenen Account
   - Kostenüberwachung ist wichtig

## 🆘 Troubleshooting

### Problem: "API key not found"

```bash
# Prüfe Umgebungsvariable
echo $ANTHROPIC_API_KEY

# Falls leer, siehe "Schritt 2: API-Key konfigurieren"
```

### Problem: "Rate limit exceeded"

- Zu viele Requests in kurzer Zeit
- Warte 1-2 Minuten
- Prüfe API-Limits in Anthropic Console

### Problem: "Invalid API key"

- Key ist falsch oder abgelaufen
- Erstelle neuen Key in Anthropic Console
- Aktualisiere GitHub Secret oder .env

### Problem: Claude Code nicht gefunden

```bash
# Installation prüfen
which claude

# Falls nicht installiert, Container neu bauen:
# VS Code Command Palette (Cmd/Ctrl+Shift+P)
# → "Codespaces: Rebuild Container"
```

## 💰 Kosten & Credits

### Anthropic Pricing (Stand 2025)

- **Claude Sonnet 3.5:** ~$3 pro 1M Input-Tokens
- **Claude Opus 3.5:** ~$15 pro 1M Input-Tokens
- **Claude Haiku:** ~$0.25 pro 1M Input-Tokens

**Realistische Kosten für Studierende:**
- ~$5-20 pro Monat bei moderater Nutzung
- Verwende Haiku für einfache Aufgaben (günstiger)
- Opus nur für komplexe Probleme

### GitHub Codespaces

- **Free Tier:** 120 Core-Stunden/Monat (für Studierende)
- **Ausreichend für:** ~60h mit 2-Core Codespace
- Lösche Codespaces wenn nicht benötigt!

## 📚 Weiterführende Links

- [Anthropic Console](https://console.anthropic.com)
- [Claude Code Dokumentation](https://code.claude.com/docs)
- [GitHub Codespaces Docs](https://docs.github.com/en/codespaces)
- [API Key Best Practices](https://docs.anthropic.com/en/api/security)

## ❓ FAQ

**Q: Kann mein Dozent meine API-Keys sehen?**
A: Nein. Dein Codespace ist privat und isoliert.

**Q: Muss ich einen kostenpflichtigen Account haben?**
A: Ja, Claude Code benötigt einen Anthropic API-Key mit Guthaben.

**Q: Was passiert wenn mein API-Key leaked?**
A: Sofort in Anthropic Console widerrufen und neuen erstellen!

**Q: Kann ich Claude Code auch lokal nutzen?**
A: Ja! Installation: `curl -fsSL https://claude.ai/install.sh | bash`

**Q: Gibt es Studentenrabatte?**
A: Momentan keine offiziellen Rabatte, aber die Kosten sind bei moderater Nutzung überschaubar.

---

**Bei Fragen oder Problemen:** Erstelle ein GitHub Issue oder kontaktiere deinen Dozenten.
