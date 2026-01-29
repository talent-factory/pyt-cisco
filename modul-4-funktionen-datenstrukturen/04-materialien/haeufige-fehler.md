# Häufige Fehler Modul 4

## Funktionen

### Fehler 1: Funktion nicht aufrufen

```python
# FALSCH
def sage_hallo():
    print("Hallo!")

sage_hallo  # Macht nichts! Kein Aufruf

# RICHTIG
sage_hallo()  # Mit Klammern aufrufen
```

### Fehler 2: Return vergessen

```python
# FALSCH
def addiere(a, b):
    ergebnis = a + b
    # return fehlt!

x = addiere(3, 4)
print(x)  # None!

# RICHTIG
def addiere(a, b):
    return a + b
```

### Fehler 3: Print statt Return

```python
# PROBLEMATISCH
def quadrat(x):
    print(x * x)  # Gibt nur aus, Wert nicht verwendbar

ergebnis = quadrat(5)  # ergebnis ist None!
y = ergebnis * 2       # Fehler!

# RICHTIG
def quadrat(x):
    return x * x

ergebnis = quadrat(5)
y = ergebnis * 2  # Funktioniert
```

### Fehler 4: Keyword vor Positional

```python
# FALSCH
def greet(name, message):
    print(f"{message}, {name}!")

greet(name="Anna", "Hallo")  # SyntaxError!

# RICHTIG
greet("Anna", message="Hallo")  # Positional zuerst
greet(name="Anna", message="Hallo")  # Oder nur Keyword
```

### Fehler 5: Default-Wert mit mutablem Objekt

```python
# FALSCH - gefährlich!
def add_item(item, liste=[]):
    liste.append(item)
    return liste

print(add_item(1))  # [1]
print(add_item(2))  # [1, 2] - Liste wird geteilt!

# RICHTIG
def add_item(item, liste=None):
    if liste is None:
        liste = []
    liste.append(item)
    return liste
```

## Tuples

### Fehler 6: Tuple ändern wollen

```python
# FALSCH
punkt = (10, 20)
punkt[0] = 15  # TypeError: tuple does not support item assignment

# RICHTIG: Neues Tuple erstellen
punkt = (15, punkt[1])
# oder
punkt = (15, 20)
```

### Fehler 7: Einzel-Tuple ohne Komma

```python
# FALSCH
x = (42)     # Das ist KEINE Tuple, sondern int!
print(type(x))  # <class 'int'>

# RICHTIG
x = (42,)    # Komma macht es zum Tuple
print(type(x))  # <class 'tuple'>
```

## Dictionaries

### Fehler 8: Nicht existierender Key

```python
# FALSCH
person = {"name": "Anna"}
print(person["alter"])  # KeyError!

# RICHTIG: Mit get()
print(person.get("alter"))        # None
print(person.get("alter", "N/A")) # "N/A"

# ODER: Prüfen
if "alter" in person:
    print(person["alter"])
```

### Fehler 9: Iteration und Änderung

```python
# FALSCH
scores = {"anna": 85, "max": 70, "lisa": 90}
for name, score in scores.items():
    if score < 80:
        del scores[name]  # RuntimeError!

# RICHTIG: Kopie erstellen
for name, score in list(scores.items()):
    if score < 80:
        del scores[name]

# ODER: Dict Comprehension
scores = {name: score for name, score in scores.items() if score >= 80}
```

### Fehler 10: Liste als Dictionary-Key

```python
# FALSCH
d = {}
d[[1, 2]] = "test"  # TypeError: unhashable type: 'list'

# RICHTIG: Tuple verwenden
d = {}
d[(1, 2)] = "test"  # OK, Tuples sind hashbar
```

## Exception Handling

### Fehler 11: Zu breites except

```python
# FALSCH - fängt ALLE Fehler, auch Programmierfehler
try:
    ergebnis = berechne_etwas()
except:
    print("Fehler")

# RICHTIG - spezifische Exceptions
try:
    ergebnis = berechne_etwas()
except ValueError as e:
    print(f"Ungültiger Wert: {e}")
except ZeroDivisionError:
    print("Division durch Null")
```

### Fehler 12: Exception verschlucken

```python
# FALSCH - Fehler werden ignoriert
try:
    datei = open("test.txt")
except:
    pass  # Tut nichts, Problem wird versteckt

# RICHTIG - Mindestens loggen
try:
    datei = open("test.txt")
except FileNotFoundError:
    print("Datei nicht gefunden, verwende Standard")
    # Sinnvolle Alternative
```

### Fehler 13: Falsche Einrückung bei try-except

```python
# FALSCH
try:
    zahl = int(input("Zahl: "))
ergebnis = 100 / zahl  # Ausserhalb von try!
except ValueError:
    print("Fehler")

# RICHTIG
try:
    zahl = int(input("Zahl: "))
    ergebnis = 100 / zahl  # Innerhalb von try
except ValueError:
    print("Fehler")
```

## Scope

### Fehler 14: Globale Variable ändern ohne global

```python
# FALSCH
counter = 0

def erhoehe():
    counter += 1  # UnboundLocalError!

# RICHTIG
counter = 0

def erhoehe():
    global counter
    counter += 1

# BESSER: Parameter und Return verwenden
def erhoehe(counter):
    return counter + 1

counter = 0
counter = erhoehe(counter)
```

## Checkliste zur Fehlervermeidung

- [ ] Funktionen mit `()` aufrufen
- [ ] `return` nicht vergessen wenn Wert benötigt
- [ ] Positional Arguments vor Keyword Arguments
- [ ] Keine mutablen Default-Werte (Listen, Dicts)
- [ ] `.get()` für sichere Dictionary-Zugriffe
- [ ] Spezifische Exception-Typen fangen
- [ ] `global` nur wenn wirklich nötig
