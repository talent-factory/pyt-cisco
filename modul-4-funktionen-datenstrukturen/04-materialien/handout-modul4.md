# Handout Modul 4: Functions, Tuples, Dictionaries, Exceptions

## Funktionen (CISCO 4.1-4.5)

### Warum Funktionen?

- **DRY** - Don't Repeat Yourself
- **Modularität** - Code in logische Einheiten aufteilen
- **Wiederverwendbarkeit** - Code mehrfach nutzen
- **Testbarkeit** - Einzelne Funktionen testen

### Syntax

```python
def funktionsname(parameter1, parameter2="default"):
    """
    Docstring: Beschreibt was die Funktion macht.

    Args:
        parameter1: Beschreibung
        parameter2: Beschreibung (Standard: default)

    Returns:
        Beschreibung des Rückgabewerts
    """
    # Funktionskörper
    ergebnis = parameter1 + parameter2
    return ergebnis
```

### Parameter-Typen

1. **Positional**: `funktion(wert1, wert2)` - Reihenfolge zählt
2. **Keyword**: `funktion(param=wert)` - Name explizit
3. **Default**: `def funktion(param=default)` - Standardwert
4. **Mixed**: Positional zuerst, dann Keyword

### Scope (Geltungsbereich)

```python
x = "global"

def funktion():
    x = "lokal"    # Neue lokale Variable
    print(x)       # "lokal"

funktion()
print(x)           # "global" (unverändert!)
```

### Rekursion

Eine Funktion, die sich selbst aufruft:
- Braucht **Basisfall** (Abbruchbedingung)
- Braucht **Rekursionsschritt** (Annäherung an Basisfall)

## Tuples (CISCO 4.6.1-4.6.2)

### Eigenschaften

- **Unveränderbar** (immutable)
- **Geordnet** (Index-Zugriff möglich)
- **Duplikate erlaubt**
- Kann als Dictionary-Key verwendet werden

### Verwendung

```python
# Erstellen
punkt = (10, 20)
rgb = (255, 128, 0)

# Unpacking
x, y = punkt

# Als Rückgabewert
def get_bounds(zahlen):
    return min(zahlen), max(zahlen)

minimum, maximum = get_bounds([1, 5, 3, 8, 2])
```

## Dictionaries (CISCO 4.6.3-4.6.5)

### Eigenschaften

- **Schlüssel-Wert-Paare**
- **Veränderbar** (mutable)
- **Keys müssen eindeutig und hashbar sein** (Strings, Zahlen, Tuples)
- **Seit Python 3.7 geordnet**

### Operationen

```python
person = {"name": "Anna", "alter": 25}

# Zugriff
person["name"]              # "Anna"
person.get("beruf", "N/A")  # "N/A" (sicherer Zugriff)

# Ändern/Hinzufügen
person["alter"] = 26
person["stadt"] = "Zürich"

# Löschen
del person["stadt"]

# Iteration
for key, value in person.items():
    print(f"{key}: {value}")
```

## Exceptions (CISCO 4.7)

### Konzept

Exceptions sind **Laufzeitfehler**, die während der Programmausführung auftreten können. Mit Exception Handling können wir diese Fehler **abfangen und behandeln**.

### try-except Struktur

```python
try:
    # Code der fehlschlagen könnte
    zahl = int(input("Zahl: "))
    ergebnis = 100 / zahl
except ValueError:
    # Wird ausgeführt bei ValueError
    print("Keine gültige Zahl!")
except ZeroDivisionError:
    # Wird ausgeführt bei ZeroDivisionError
    print("Division durch Null!")
else:
    # Wird ausgeführt wenn KEIN Fehler
    print(f"Ergebnis: {ergebnis}")
finally:
    # Wird IMMER ausgeführt
    print("Fertig.")
```

### Häufige Exception-Typen

| Exception | Wann |
|-----------|------|
| `ValueError` | Falscher Wert für Operation |
| `TypeError` | Falscher Datentyp |
| `KeyError` | Key nicht im Dictionary |
| `IndexError` | Index ausserhalb des Bereichs |
| `ZeroDivisionError` | Division durch 0 |
| `FileNotFoundError` | Datei existiert nicht |
| `AttributeError` | Attribut/Methode existiert nicht |

### Best Practices

1. **Spezifische Exceptions** fangen (nicht `except:` ohne Typ)
2. **Minimal** Code im try-Block
3. **Sinnvolle Fehlermeldungen** ausgeben
4. **Nicht schweigend** Fehler ignorieren

## Zusammenfassung

| Konzept | Wichtigste Punkte |
|---------|-------------------|
| Funktionen | `def`, Parameter, `return`, Scope |
| Tuples | Unveränderbar, Unpacking, als Return |
| Dictionaries | Key-Value, `.get()`, `.items()` |
| Exceptions | `try-except`, spezifische Typen |

## PCEP Prüfungstipps

- Verstehen Sie den Unterschied zwischen `return` und `print()`
- Kennen Sie alle Parameter-Typen und deren Reihenfolge
- Wissen, wann Tuples vs Listen verwendet werden
- Dictionary-Methoden und Zugriff beherrschen
- Exception-Typen und deren Ursachen kennen
