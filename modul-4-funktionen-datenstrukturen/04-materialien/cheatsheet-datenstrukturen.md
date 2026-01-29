# Cheatsheet: Datenstrukturen

## Tuples

### Erstellen
```python
punkt = (10, 20)
person = ("Anna", 25, "Zürich")
einzelwert = (42,)  # Komma wichtig!
leer = ()
```

### Zugriff
```python
print(punkt[0])      # 10
print(person[-1])    # "Zürich"
print(punkt[0:2])    # (10, 20)
```

### Unpacking
```python
x, y = punkt
name, alter, stadt = person

# Mehrere Rückgabewerte
def get_pos():
    return 10, 20

x, y = get_pos()
```

### Eigenschaften
- **Unveränderbar** (immutable)
- **Geordnet**
- **Duplikate erlaubt**
- Kann als Dictionary-Key verwendet werden

## Dictionaries

### Erstellen
```python
person = {
    "name": "Anna",
    "alter": 25,
    "stadt": "Zürich"
}
leer = {}
```

### Zugriff
```python
print(person["name"])              # "Anna"
print(person.get("beruf"))         # None
print(person.get("beruf", "N/A"))  # "N/A"
```

### Ändern / Hinzufügen
```python
person["alter"] = 26               # Ändern
person["beruf"] = "Entwicklerin"   # Hinzufügen
```

### Löschen
```python
del person["stadt"]
wert = person.pop("alter")         # Löschen und zurückgeben
person.clear()                     # Alles löschen
```

### Methoden
```python
person.keys()     # dict_keys(['name', 'alter', 'stadt'])
person.values()   # dict_values(['Anna', 25, 'Zürich'])
person.items()    # dict_items([('name', 'Anna'), ...])
```

### Iteration
```python
# Über Keys
for key in person:
    print(key)

# Über Values
for value in person.values():
    print(value)

# Über Key-Value-Paare
for key, value in person.items():
    print(f"{key}: {value}")
```

### Prüfungen
```python
"name" in person        # True (Key existiert)
"xyz" in person         # False
"Anna" in person.values()  # True (Wert existiert)
```

## Exception Handling

### try-except Basis
```python
try:
    ergebnis = 10 / 0
except ZeroDivisionError:
    print("Division durch Null!")
```

### Mehrere Exceptions
```python
try:
    zahl = int(input("Zahl: "))
    ergebnis = 100 / zahl
except ValueError:
    print("Keine gültige Zahl")
except ZeroDivisionError:
    print("Division durch Null")
```

### Mit else und finally
```python
try:
    datei = open("test.txt")
    inhalt = datei.read()
except FileNotFoundError:
    print("Datei nicht gefunden")
else:
    print("Erfolgreich gelesen")
finally:
    print("Wird immer ausgeführt")
```

### Häufige Exceptions
| Exception | Ursache |
|-----------|---------|
| `ValueError` | Falscher Wert (z.B. `int("abc")`) |
| `TypeError` | Falscher Typ |
| `KeyError` | Key nicht im Dictionary |
| `IndexError` | Index ausserhalb der Liste |
| `ZeroDivisionError` | Division durch 0 |
| `FileNotFoundError` | Datei nicht gefunden |

## Vergleich der Strukturen

| Typ | Syntax | Veränderbar | Geordnet | Duplikate |
|-----|--------|-------------|----------|-----------|
| Liste | `[1, 2, 3]` | Ja | Ja | Ja |
| Tuple | `(1, 2, 3)` | Nein | Ja | Ja |
| Dict | `{"a": 1}` | Ja | Ja* | Keys: Nein |
| Set | `{1, 2, 3}` | Ja | Nein | Nein |

*Seit Python 3.7

## Wann welche Struktur?

| Situation | Empfehlung |
|-----------|------------|
| Sammlung von Elementen, änderbar | Liste |
| Koordinaten, RGB-Farben | Tuple |
| Unveränderliche Daten | Tuple |
| Key-Value Zuordnung | Dictionary |
| Lookup-Tabelle | Dictionary |
| Eindeutige Elemente | Set |
| Mengenoperationen | Set |

## Schnellreferenz Dictionary

```python
# CRUD
d["key"] = value    # Create/Update
d["key"]            # Read (KeyError wenn nicht vorhanden)
d.get("key", None)  # Read (sicher)
del d["key"]        # Delete

# Methoden
d.keys()            # Alle Keys
d.values()          # Alle Values
d.items()           # Alle Key-Value Paare
d.update(other)     # Zusammenführen
d.pop("key")        # Löschen und zurückgeben
```
