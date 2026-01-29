# Lektion 2: Rückgabewerte, Scopes & Rekursion

**Dauer:** 50 Minuten
**Format:** 15 Min Theorie + 20 Min Live-Coding + 15 Min Übung
**CISCO NetAcad:** Kapitel 4.3, 4.4, 4.5

## Lernziele

Nach dieser Lektion können Sie:
- Rückgabewerte mit `return` erstellen
- Den Unterschied zwischen `return` und `print()` verstehen
- `None` als Rückgabewert verstehen
- Lokale und globale Variablen unterscheiden
- Das `global` Keyword verwenden
- Rekursive Funktionen verstehen

## Theorie (15 Min)

### Return-Anweisung (CISCO 4.3.1)

**Unterschied print vs return:**
```python
# Mit print - zeigt nur an
def zeige_summe(a, b):
    print(a + b)

# Mit return - gibt Wert zurück
def berechne_summe(a, b):
    return a + b

zeige_summe(3, 4)        # Zeigt: 7 (aber Wert nicht verwendbar)
ergebnis = berechne_summe(3, 4)  # ergebnis = 7
print(ergebnis * 2)      # 14
```

**Wichtig:** `return` beendet die Funktion sofort!

```python
def pruefe_positiv(zahl):
    """Prüft ob Zahl positiv ist."""
    if zahl <= 0:
        return False  # Funktion endet hier
    return True       # Nur erreicht wenn zahl > 0
```

### None (CISCO 4.3.2)

Funktionen ohne `return` geben `None` zurück:

```python
def sage_hallo():
    print("Hallo!")

ergebnis = sage_hallo()  # Zeigt: Hallo!
print(ergebnis)          # None
print(type(ergebnis))    # <class 'NoneType'>
```

**None prüfen:**
```python
def finde_element(liste, gesucht):
    """Findet Index oder gibt None zurück."""
    for i, element in enumerate(liste):
        if element == gesucht:
            return i
    return None  # Nicht gefunden

index = finde_element([1, 2, 3], 2)
if index is not None:
    print(f"Gefunden an Position {index}")
else:
    print("Nicht gefunden")
```

### Funktionen und Listen (CISCO 4.3.3)

```python
def verdopple_alle(zahlen):
    """Verdoppelt alle Zahlen in einer Liste."""
    ergebnis = []
    for zahl in zahlen:
        ergebnis.append(zahl * 2)
    return ergebnis

original = [1, 2, 3, 4, 5]
verdoppelt = verdopple_alle(original)
print(verdoppelt)  # [2, 4, 6, 8, 10]
```

### Scopes - Geltungsbereiche (CISCO 4.4.1-4.4.2)

**Lokale Variablen:**
```python
def beispiel():
    x = 10  # Lokal - nur in der Funktion sichtbar
    print(x)

beispiel()   # 10
# print(x)   # NameError: name 'x' is not defined
```

**Globale Variablen:**
```python
zaehler = 0  # Global

def erhoehe():
    global zaehler  # Zugriff auf globale Variable
    zaehler += 1

erhoehe()
erhoehe()
print(zaehler)  # 2
```

**Best Practice:** Vermeiden Sie `global` wenn möglich!

```python
# Besser: Parameter und Return verwenden
def erhoehe(wert):
    return wert + 1

zaehler = 0
zaehler = erhoehe(zaehler)  # 1
zaehler = erhoehe(zaehler)  # 2
```

### Rekursion (CISCO 4.5.5)

Eine Funktion ruft sich selbst auf:

```python
def fakultaet(n):
    """Berechnet n! rekursiv."""
    if n <= 1:        # Basisfall
        return 1
    return n * fakultaet(n - 1)  # Rekursiver Aufruf

print(fakultaet(5))  # 120 (5 * 4 * 3 * 2 * 1)
```

**Wie es funktioniert:**
```
fakultaet(5)
= 5 * fakultaet(4)
= 5 * 4 * fakultaet(3)
= 5 * 4 * 3 * fakultaet(2)
= 5 * 4 * 3 * 2 * fakultaet(1)
= 5 * 4 * 3 * 2 * 1
= 120
```

## Live-Coding (20 Min)

### Beispiel 1: Berechnung mit Return

```python
def berechne_rechteck(laenge, breite):
    """Berechnet Fläche und Umfang eines Rechtecks."""
    flaeche = laenge * breite
    umfang = 2 * (laenge + breite)
    return flaeche, umfang  # Mehrere Rückgabewerte!

# Verwendung
f, u = berechne_rechteck(5, 3)
print(f"Fläche: {f} m², Umfang: {u} m")

# Oder als Tuple
ergebnis = berechne_rechteck(10, 4)
print(f"Fläche: {ergebnis[0]}, Umfang: {ergebnis[1]}")
```

### Beispiel 2: BMI-Rechner (CISCO 4.5.1)

```python
def berechne_bmi(gewicht, groesse):
    """Berechnet den Body-Mass-Index.

    Args:
        gewicht: Gewicht in kg
        groesse: Grösse in m

    Returns:
        BMI-Wert als float
    """
    return gewicht / (groesse ** 2)

def bewerte_bmi(bmi):
    """Bewertet den BMI."""
    if bmi < 18.5:
        return "Untergewicht"
    elif bmi < 25:
        return "Normalgewicht"
    elif bmi < 30:
        return "Übergewicht"
    else:
        return "Adipositas"

# Verwendung
bmi = berechne_bmi(75, 1.80)
bewertung = bewerte_bmi(bmi)
print(f"BMI: {bmi:.1f} - {bewertung}")
```

### Beispiel 3: Fibonacci (CISCO 4.5.4)

```python
def fibonacci(n):
    """Gibt die n-te Fibonacci-Zahl zurück (iterativ)."""
    if n <= 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Die ersten 10 Fibonacci-Zahlen
for i in range(10):
    print(f"F({i}) = {fibonacci(i)}")
```

### Beispiel 4: Rekursive Summe

```python
def summe_bis(n):
    """Berechnet 1 + 2 + ... + n rekursiv."""
    if n <= 0:
        return 0
    return n + summe_bis(n - 1)

print(summe_bis(5))   # 15 (1+2+3+4+5)
print(summe_bis(100)) # 5050
```

### Beispiel 5: Scope demonstrieren

```python
x = "global"

def aeussere():
    x = "aeussere"

    def innere():
        x = "innere"
        print(f"Innere Funktion: {x}")

    innere()
    print(f"Äussere Funktion: {x}")

aeussere()
print(f"Global: {x}")

# Ausgabe:
# Innere Funktion: innere
# Äussere Funktion: aeussere
# Global: global
```

## Übungen (15 Min)

### Übung 3: Schaltjahr (CISCO LAB 4.3.4)

```python
def ist_schaltjahr(jahr):
    """Prüft ob ein Jahr ein Schaltjahr ist.

    Regeln:
    - Durch 4 teilbar: Schaltjahr
    - ABER durch 100 teilbar: Kein Schaltjahr
    - ABER durch 400 teilbar: Doch Schaltjahr
    """
    # Ihr Code hier
    pass

# Tests
print(ist_schaltjahr(2024))  # True
print(ist_schaltjahr(2023))  # False
print(ist_schaltjahr(2000))  # True
print(ist_schaltjahr(1900))  # False
```

Siehe [Übung 3](../02-uebungen/uebung-3-schaltjahr.md)

### Übung 4: Primzahl (CISCO LAB 4.3.7)

```python
def ist_primzahl(n):
    """Prüft ob n eine Primzahl ist."""
    # Ihr Code hier
    pass

# Tests
print(ist_primzahl(7))   # True
print(ist_primzahl(10))  # False
print(ist_primzahl(23))  # True
```

Siehe [Übung 4](../02-uebungen/uebung-4-primzahl.md)

## Zusammenfassung

| Konzept | Beschreibung |
|---------|--------------|
| `return wert` | Gibt einen Wert zurück |
| `return a, b` | Gibt mehrere Werte zurück (Tuple) |
| `None` | Standard-Rückgabewert ohne return |
| Lokale Variable | Nur innerhalb der Funktion sichtbar |
| Globale Variable | Im gesamten Modul sichtbar |
| `global x` | Zugriff auf globale Variable |
| Rekursion | Funktion ruft sich selbst auf |

**Merksätze:**
- `return` gibt Werte zurück UND beendet die Funktion
- Ohne `return` gibt die Funktion `None` zurück
- Lokale Variablen haben Vorrang vor globalen
- Rekursion braucht immer einen Basisfall!

## Weiter

- [Lektion 3: Tuples, Dictionaries & Exceptions](./lektion-3-datenstrukturen-exceptions.md)
- [Beispiele](../05-beispiele/)
