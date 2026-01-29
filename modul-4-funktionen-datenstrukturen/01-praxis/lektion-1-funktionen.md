# Lektion 1: Funktionen Grundlagen

**Dauer:** 50 Minuten
**Format:** 15 Min Theorie + 20 Min Live-Coding + 15 Min Übung
**CISCO NetAcad:** Kapitel 4.1, 4.2

## Lernziele

Nach dieser Lektion können Sie:
- Erklären, warum Funktionen wichtig sind (Decomposition, DRY)
- Funktionen mit `def` definieren
- Funktionen mit Parametern aufrufen
- Positional und Keyword Arguments unterscheiden
- Default-Werte für Parameter setzen

## Theorie (15 Min)

### Warum Funktionen? (CISCO 4.1.1-4.1.2)

**Problem ohne Funktionen:**
```python
# Code wiederholt sich!
print("=" * 40)
print("ABSCHNITT 1")
print("=" * 40)

# ... mehr Code ...

print("=" * 40)
print("ABSCHNITT 2")
print("=" * 40)
```

**Lösung mit Funktion:**
```python
def zeige_titel(text):
    """Zeigt einen formatierten Titel."""
    print("=" * 40)
    print(text)
    print("=" * 40)

zeige_titel("ABSCHNITT 1")
zeige_titel("ABSCHNITT 2")
```

**Vorteile (Decomposition):**
- **DRY:** Don't Repeat Yourself
- **Lesbarkeit:** Code ist verständlicher
- **Wartbarkeit:** Änderungen an einer Stelle
- **Wiederverwendbarkeit:** Code mehrfach nutzen
- **Testing:** Einzelne Funktionen testen

### Woher kommen Funktionen? (CISCO 4.1.3)

1. **Built-in:** `print()`, `input()`, `len()`, `range()` - von Python
2. **Module:** `math.sqrt()`, `random.randint()` - aus Bibliotheken
3. **Eigene:** Mit `def` selbst definiert

### Ihre erste Funktion (CISCO 4.1.4-4.1.5)

```python
def gruesse():
    """Gibt eine Begrüssung aus."""
    print("Hallo Welt!")

# Aufruf der Funktion
gruesse()  # Ausgabe: Hallo Welt!
```

**Wichtig:**
- `def` leitet die Definition ein
- Funktionsname in `snake_case`
- Doppelpunkt `:` am Ende der Zeile
- Code-Block eingerückt (4 Leerzeichen)
- Docstring beschreibt die Funktion

### Parameter (CISCO 4.2.1-4.2.5)

**Positional Arguments (4.2.2):**
```python
def gruesse(name, gruss):
    """Begrüsst eine Person."""
    print(f"{gruss}, {name}!")

gruesse("Anna", "Hallo")     # Hallo, Anna!
gruesse("Max", "Guten Tag")  # Guten Tag, Max!
```

**Keyword Arguments (4.2.3):**
```python
gruesse(name="Anna", gruss="Hallo")  # Explizit benannt
gruesse(gruss="Hi", name="Max")      # Reihenfolge egal
```

**Mixing (4.2.4):**
```python
gruesse("Anna", gruss="Hallo")  # Positional, dann Keyword
# gruesse(name="Anna", "Hallo")  # FEHLER! Keyword vor Positional
```

**Default-Werte (4.2.5):**
```python
def gruesse(name, gruss="Hallo"):
    """Begrüsst eine Person (Standard: Hallo)."""
    print(f"{gruss}, {name}!")

gruesse("Anna")           # Hallo, Anna!
gruesse("Max", "Hi")      # Hi, Max!
gruesse("Lisa", gruss="Servus")  # Servus, Lisa!
```

## Live-Coding (20 Min)

### Beispiel 1: Einfache Begrüssung

```python
def begruessung():
    """Gibt eine freundliche Begrüssung aus."""
    print("=" * 40)
    print("Willkommen zum Python-Kurs!")
    print("Schön, dass Sie da sind!")
    print("=" * 40)

# Aufruf
begruessung()
```

### Beispiel 2: Funktion mit Parameter

```python
def berechne_quadrat(zahl):
    """Berechnet und zeigt das Quadrat einer Zahl."""
    quadrat = zahl * zahl
    print(f"Das Quadrat von {zahl} ist {quadrat}")

# Verschiedene Aufrufe
berechne_quadrat(5)   # Das Quadrat von 5 ist 25
berechne_quadrat(12)  # Das Quadrat von 12 ist 144
```

### Beispiel 3: Mehrere Parameter

```python
def zeige_info(name, alter, stadt="Unbekannt"):
    """Zeigt Informationen über eine Person."""
    print(f"Name: {name}")
    print(f"Alter: {alter} Jahre")
    print(f"Stadt: {stadt}")
    print("-" * 30)

# Aufrufe
zeige_info("Anna", 25, "Zürich")
zeige_info("Max", 30)  # Stadt = "Unbekannt"
zeige_info(alter=22, name="Lisa", stadt="Bern")
```

### Beispiel 4: Mehrere Funktionen kombinieren

```python
def zeige_header():
    """Zeigt einen Header."""
    print("=" * 40)
    print("MEIN PROGRAMM")
    print("=" * 40)

def zeige_menu():
    """Zeigt ein Menü."""
    print("1. Berechnung starten")
    print("2. Hilfe anzeigen")
    print("3. Beenden")

def zeige_footer():
    """Zeigt einen Footer."""
    print("-" * 40)
    print("© 2025 Python Kurs")

# Hauptprogramm
zeige_header()
zeige_menu()
zeige_footer()
```

## Übungen (15 Min)

### Übung 1: Trennlinie (5 Min)

Erstellen Sie eine Funktion `trennlinie(zeichen, laenge)` mit Default-Werten:

```python
def trennlinie(zeichen="-", laenge=40):
    # Ihr Code hier
    pass

trennlinie()           # ----------------------------------------
trennlinie("*")        # ****************************************
trennlinie("=", 20)    # ====================
```

Siehe [Übung 1](../02-uebungen/uebung-1-funktionen-basis.md)

### Übung 2: Personenbegrüssung (10 Min)

Erstellen Sie eine Funktion `begruesse_person(vorname, nachname, anrede="Herr/Frau")`:

```python
def begruesse_person(vorname, nachname, anrede="Herr/Frau"):
    # Ihr Code hier
    pass

begruesse_person("Max", "Müller")
# Guten Tag, Herr/Frau Max Müller!

begruesse_person("Anna", "Schmidt", anrede="Frau")
# Guten Tag, Frau Anna Schmidt!
```

Siehe [Übung 2](../02-uebungen/uebung-2-parameter.md)

## Zusammenfassung

| Konzept | Syntax | Beispiel |
|---------|--------|----------|
| Definition | `def name():` | `def gruesse():` |
| Parameter | `def name(param):` | `def gruesse(name):` |
| Default | `def name(param=wert):` | `def gruesse(name="Gast"):` |
| Positional | `funktion(wert)` | `gruesse("Anna")` |
| Keyword | `funktion(param=wert)` | `gruesse(name="Anna")` |

**Merksätze:**
- Funktionen = Wiederverwendbare Code-Blöcke
- `def` + Name + Klammern + Doppelpunkt
- Einrückung definiert den Funktionskörper
- Parameter machen Funktionen flexibel
- Default-Werte machen Parameter optional

## Weiter

- [Lektion 2: Rückgabewerte, Scopes & Rekursion](./lektion-2-return-scopes.md)
- [Beispiele](../05-beispiele/)
