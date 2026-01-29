# Cheatsheet: Funktionen

## Funktion definieren

```python
def funktionsname(parameter1, parameter2):
    """Docstring: Was macht die Funktion?"""
    # Code hier
    return ergebnis
```

## Parameter-Arten

### Positional Arguments
```python
def greet(name, message):
    print(f"{message}, {name}!")

greet("Anna", "Hallo")  # Reihenfolge wichtig!
```

### Keyword Arguments
```python
greet(name="Anna", message="Hallo")  # Reihenfolge egal
greet(message="Hi", name="Max")
```

### Default Values
```python
def greet(name, message="Hallo"):
    print(f"{message}, {name}!")

greet("Anna")           # Hallo, Anna!
greet("Max", "Hi")      # Hi, Max!
```

### Mixing (Reihenfolge!)
```python
greet("Anna", message="Hi")  # OK: Positional, dann Keyword
# greet(name="Anna", "Hi")   # FEHLER: Keyword vor Positional
```

## Return

### Einzelner Wert
```python
def quadrat(x):
    return x * x

ergebnis = quadrat(5)  # 25
```

### Mehrere Werte (Tuple)
```python
def statistik(zahlen):
    return min(zahlen), max(zahlen), sum(zahlen)/len(zahlen)

minimum, maximum, durchschnitt = statistik([1, 2, 3, 4, 5])
```

### Ohne Return → None
```python
def sage_hallo():
    print("Hallo!")

x = sage_hallo()  # x ist None
```

## Scope (Geltungsbereich)

### Lokal vs Global
```python
x = "global"  # Globale Variable

def funktion():
    x = "lokal"  # Lokale Variable (überdeckt global)
    print(x)     # "lokal"

funktion()
print(x)  # "global" (unverändert)
```

### Global Keyword
```python
zaehler = 0

def erhoehe():
    global zaehler  # Zugriff auf globale Variable
    zaehler += 1

erhoehe()
print(zaehler)  # 1
```

## Rekursion

```python
def fakultaet(n):
    if n <= 1:           # Basisfall
        return 1
    return n * fakultaet(n - 1)  # Rekursiver Aufruf

print(fakultaet(5))  # 120
```

## Best Practices

| Do | Don't |
|----|-------|
| `def berechne_summe(a, b):` | `def f(x, y):` |
| Docstrings schreiben | Keine Dokumentation |
| Kleine, fokussierte Funktionen | Eine Funktion macht alles |
| Return statt Print für Ergebnisse | Print in Berechnungsfunktionen |
| Parameter statt globale Variablen | Exzessive Nutzung von `global` |

## Schnellreferenz

| Syntax | Beschreibung |
|--------|--------------|
| `def name():` | Funktion ohne Parameter |
| `def name(x):` | Ein Parameter |
| `def name(x, y):` | Mehrere Parameter |
| `def name(x=10):` | Parameter mit Default |
| `def name(*args):` | Beliebig viele Positional |
| `def name(**kwargs):` | Beliebig viele Keyword |
| `return wert` | Wert zurückgeben |
| `return a, b` | Mehrere Werte (Tuple) |
| `global x` | Globale Variable nutzen |
