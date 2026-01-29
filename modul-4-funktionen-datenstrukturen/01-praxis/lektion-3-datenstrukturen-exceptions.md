# Lektion 3: Tuples, Dictionaries & Exceptions

**Dauer:** 50 Minuten
**Format:** 15 Min Theorie + 20 Min Live-Coding + 15 Min Übung
**CISCO NetAcad:** Kapitel 4.6, 4.7

## Lernziele

Nach dieser Lektion können Sie:
- Tuples erstellen und verwenden
- Dictionaries erstellen und manipulieren
- Die richtige Datenstruktur wählen
- Fehler mit `try-except` behandeln
- Häufige Exception-Typen kennen

## Theorie (15 Min)

### Tuples (CISCO 4.6.1-4.6.2)

**Unveränderbare Sequenzen:**
```python
# Tuple erstellen
koordinaten = (10, 20)
person = ("Anna", 25, "Zürich")
einzelwert = (42,)  # Komma wichtig!

# Zugriff wie bei Listen
print(koordinaten[0])  # 10
print(person[1])       # 25

# NICHT möglich (unveränderbar!):
# koordinaten[0] = 15  # TypeError!
```

**Tuple Unpacking:**
```python
punkt = (3, 4, 5)
x, y, z = punkt
print(x, y, z)  # 3 4 5

# Bei Funktionen mit mehreren Rückgabewerten
def get_position():
    return 10, 20  # Gibt Tuple zurück

x, y = get_position()
```

**Wann Tuples verwenden?**
- Unveränderliche Daten (Koordinaten, RGB-Farben)
- Dictionary-Keys (Listen können das nicht!)
- Mehrere Rückgabewerte aus Funktionen

### Dictionaries (CISCO 4.6.3-4.6.5)

**Schlüssel-Wert-Paare:**
```python
person = {
    "name": "Anna",
    "alter": 25,
    "stadt": "Zürich"
}

# Zugriff
print(person["name"])               # Anna
print(person.get("beruf", "N/A"))   # N/A (mit Default)

# Ändern/Hinzufügen
person["alter"] = 26
person["beruf"] = "Entwicklerin"

# Löschen
del person["stadt"]
```

**Dictionary-Methoden:**
```python
person = {"name": "Anna", "alter": 25}

# Alle Schlüssel
print(person.keys())    # dict_keys(['name', 'alter'])

# Alle Werte
print(person.values())  # dict_values(['Anna', 25])

# Alle Paare
print(person.items())   # dict_items([('name', 'Anna'), ('alter', 25)])

# Prüfen ob Key existiert
if "name" in person:
    print("Name vorhanden")
```

**Iteration:**
```python
for key in person:
    print(f"{key}: {person[key]}")

# Oder eleganter
for key, value in person.items():
    print(f"{key}: {value}")
```

### Vergleich der Datenstrukturen

| Typ | Veränderbar | Geordnet | Duplikate | Syntax |
|-----|-------------|----------|-----------|--------|
| Liste | Ja | Ja | Ja | `[1, 2, 3]` |
| Tuple | Nein | Ja | Ja | `(1, 2, 3)` |
| Dict | Ja | Ja* | Keys: Nein | `{"a": 1}` |

*Seit Python 3.7 sind Dicts geordnet

### Exceptions (CISCO 4.7.1-4.7.6)

**Häufige Fehlertypen:**
```python
# ZeroDivisionError
# print(10 / 0)

# ValueError
# int("abc")

# KeyError
# person["xyz"]

# IndexError
# liste = [1, 2, 3]
# print(liste[10])

# FileNotFoundError
# open("gibts_nicht.txt")
```

**try-except Block:**
```python
try:
    zahl = int(input("Zahl: "))
    ergebnis = 100 / zahl
    print(f"Ergebnis: {ergebnis}")
except ValueError:
    print("Bitte eine gültige Zahl eingeben!")
except ZeroDivisionError:
    print("Division durch Null nicht erlaubt!")
```

**Mehrere Exceptions:**
```python
try:
    # Code der fehlschlagen könnte
    pass
except (ValueError, TypeError):
    print("Wert- oder Typfehler")
except Exception as e:
    print(f"Unerwarteter Fehler: {e}")
```

**finally:**
```python
try:
    datei = open("test.txt", "r")
    inhalt = datei.read()
except FileNotFoundError:
    print("Datei nicht gefunden")
finally:
    print("Wird immer ausgeführt!")
```

## Live-Coding (20 Min)

### Beispiel 1: Kontakte mit Dictionary

```python
kontakte = {}

def kontakt_hinzufuegen(name, telefon, email=""):
    """Fügt einen neuen Kontakt hinzu."""
    kontakte[name] = {
        "telefon": telefon,
        "email": email
    }
    print(f"Kontakt '{name}' hinzugefügt.")

def kontakt_suchen(name):
    """Sucht einen Kontakt."""
    if name in kontakte:
        info = kontakte[name]
        print(f"Name: {name}")
        print(f"  Telefon: {info['telefon']}")
        print(f"  Email: {info['email'] or 'N/A'}")
    else:
        print(f"Kontakt '{name}' nicht gefunden.")

def alle_kontakte():
    """Zeigt alle Kontakte."""
    if not kontakte:
        print("Keine Kontakte vorhanden.")
        return

    print("\n=== KONTAKTE ===")
    for name, info in kontakte.items():
        print(f"{name}: {info['telefon']}")

# Verwendung
kontakt_hinzufuegen("Anna", "079 123 45 67", "anna@mail.ch")
kontakt_hinzufuegen("Max", "078 987 65 43")
alle_kontakte()
kontakt_suchen("Anna")
```

### Beispiel 2: Tuple für Koordinaten

```python
def berechne_distanz(punkt1, punkt2):
    """Berechnet die Distanz zwischen zwei Punkten.

    Args:
        punkt1: Tuple (x, y)
        punkt2: Tuple (x, y)

    Returns:
        Distanz als float
    """
    x1, y1 = punkt1  # Tuple Unpacking
    x2, y2 = punkt2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# Verwendung
start = (0, 0)
ziel = (3, 4)
distanz = berechne_distanz(start, ziel)
print(f"Distanz: {distanz}")  # 5.0
```

### Beispiel 3: Sichere Benutzereingabe

```python
def sichere_zahl_eingabe(prompt, min_wert=None, max_wert=None):
    """Liest eine Zahl sicher ein mit Validierung."""
    while True:
        try:
            eingabe = input(prompt)
            zahl = float(eingabe)

            if min_wert is not None and zahl < min_wert:
                print(f"Zahl muss mindestens {min_wert} sein.")
                continue

            if max_wert is not None and zahl > max_wert:
                print(f"Zahl darf höchstens {max_wert} sein.")
                continue

            return zahl

        except ValueError:
            print("Bitte eine gültige Zahl eingeben.")

# Verwendung
alter = sichere_zahl_eingabe("Ihr Alter: ", min_wert=0, max_wert=150)
print(f"Sie sind {alter} Jahre alt.")
```

### Beispiel 4: Notenverwaltung

```python
def notenverwaltung():
    """Einfache Notenverwaltung mit Dictionary."""
    studenten = {}

    while True:
        print("\n1. Note hinzufügen")
        print("2. Durchschnitt anzeigen")
        print("3. Alle anzeigen")
        print("4. Beenden")

        try:
            wahl = int(input("Wahl: "))
        except ValueError:
            print("Bitte eine Zahl eingeben.")
            continue

        if wahl == 1:
            name = input("Name: ")
            try:
                note = float(input("Note: "))
                if name not in studenten:
                    studenten[name] = []
                studenten[name].append(note)
                print("Note hinzugefügt.")
            except ValueError:
                print("Ungültige Note.")

        elif wahl == 2:
            name = input("Name: ")
            if name in studenten and studenten[name]:
                noten = studenten[name]
                durchschnitt = sum(noten) / len(noten)
                print(f"Durchschnitt von {name}: {durchschnitt:.2f}")
            else:
                print("Keine Noten gefunden.")

        elif wahl == 3:
            for name, noten in studenten.items():
                avg = sum(noten) / len(noten) if noten else 0
                print(f"{name}: {noten} (Ø {avg:.2f})")

        elif wahl == 4:
            print("Auf Wiedersehen!")
            break

# notenverwaltung()  # Zum Testen auskommentieren
```

## Übungen (15 Min)

### Übung 5: Wörterbuch

```python
woerterbuch = {
    "hello": "hallo",
    "world": "welt",
    "python": "schlange"
}

def uebersetze(wort):
    """Übersetzt ein englisches Wort ins Deutsche."""
    # Ihr Code hier
    pass

print(uebersetze("hello"))   # hallo
print(uebersetze("xyz"))     # Wort nicht gefunden
```

Siehe [Übung 5](../02-uebungen/uebung-5-dictionary.md)

### Übung 6: Sichere Division

```python
def sichere_division(a, b):
    """Teilt a durch b mit Fehlerbehandlung.

    Returns:
        Ergebnis oder None bei Fehler
    """
    # Ihr Code hier (try-except verwenden)
    pass

print(sichere_division(10, 2))   # 5.0
print(sichere_division(10, 0))   # None (mit Fehlermeldung)
print(sichere_division("a", 2))  # None (mit Fehlermeldung)
```

Siehe [Übung 6](../02-uebungen/uebung-6-exceptions.md)

## Zusammenfassung

| Konzept | Syntax | Beschreibung |
|---------|--------|--------------|
| Tuple | `(1, 2, 3)` | Unveränderbar, geordnet |
| Unpacking | `x, y = punkt` | Werte extrahieren |
| Dictionary | `{"key": value}` | Schlüssel-Wert-Paare |
| Zugriff | `dict["key"]` | Direkter Zugriff |
| Sicher | `dict.get("key", default)` | Mit Standardwert |
| `try-except` | `try: ... except:` | Fehlerbehandlung |
| `finally` | `finally: ...` | Immer ausgeführt |

**Merksätze:**
- Tuples für unveränderliche Daten
- Dictionaries für Schlüssel-Wert-Zuordnungen
- `try-except` für robuste Programme
- Immer spezifische Exceptions fangen wenn möglich

## Modul 4 abgeschlossen!

Sie haben gelernt:
- Funktionen definieren und aufrufen
- Parameter, Return, Scopes
- Tuples und Dictionaries
- Exception Handling

**Weiter:** [Nachbearbeitung & Hausaufgaben](../03-nachbearbeitung/)
