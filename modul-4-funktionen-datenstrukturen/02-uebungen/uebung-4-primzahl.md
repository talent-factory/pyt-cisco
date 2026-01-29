# Übung 4: Primzahlen (CISCO LAB 4.3.7)

**Schwierigkeit:** Mittel
**Thema:** Return-Werte, Schleifen, Algorithmen

## Hintergrund

Eine Primzahl ist eine natürliche Zahl grösser als 1, die nur durch 1 und sich selbst teilbar ist.

Beispiele: 2, 3, 5, 7, 11, 13, 17, 19, 23, ...

## Aufgabe 4.1: Primzahl prüfen

```python
def ist_primzahl(n):
    """Prüft ob n eine Primzahl ist.

    Args:
        n: Die zu prüfende Zahl

    Returns:
        True wenn Primzahl, sonst False
    """
    # Sonderfälle: n <= 1 ist keine Primzahl
    # Tipp: Prüfen Sie Teilbarkeit nur bis sqrt(n)
    # Ihr Code hier
    pass

# Tests
print(ist_primzahl(2))   # True
print(ist_primzahl(7))   # True
print(ist_primzahl(10))  # False (2 * 5)
print(ist_primzahl(23))  # True
print(ist_primzahl(1))   # False
print(ist_primzahl(0))   # False
print(ist_primzahl(-5))  # False
```

## Aufgabe 4.2: Primzahlen bis n

```python
def primzahlen_bis(n):
    """Findet alle Primzahlen bis n.

    Args:
        n: Obergrenze

    Returns:
        Liste aller Primzahlen bis n
    """
    # Tipp: Nutzen Sie ist_primzahl()
    # Ihr Code hier
    pass

# Tests
print(primzahlen_bis(10))   # [2, 3, 5, 7]
print(primzahlen_bis(20))   # [2, 3, 5, 7, 11, 13, 17, 19]
print(primzahlen_bis(2))    # [2]
print(primzahlen_bis(1))    # []
```

## Aufgabe 4.3: Erste n Primzahlen

```python
def erste_primzahlen(anzahl):
    """Findet die ersten n Primzahlen.

    Args:
        anzahl: Anzahl gewünschter Primzahlen

    Returns:
        Liste der ersten n Primzahlen
    """
    # Ihr Code hier
    pass

# Tests
print(erste_primzahlen(5))   # [2, 3, 5, 7, 11]
print(erste_primzahlen(10))  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
print(erste_primzahlen(1))   # [2]
```

## Aufgabe 4.4: Primfaktorzerlegung

```python
def primfaktoren(n):
    """Zerlegt n in Primfaktoren.

    Args:
        n: Die zu zerlegende Zahl

    Returns:
        Liste der Primfaktoren (mit Wiederholungen)
    """
    # Beispiel: 12 = 2 * 2 * 3 → [2, 2, 3]
    # Ihr Code hier
    pass

# Tests
print(primfaktoren(12))   # [2, 2, 3]
print(primfaktoren(100))  # [2, 2, 5, 5]
print(primfaktoren(17))   # [17]
print(primfaktoren(1))    # []
```

## Bonus: Zwillingsprimzahlen

Zwillingsprimzahlen sind Primzahlpaare mit Abstand 2 (z.B. 3 und 5, 11 und 13).

```python
def zwillingsprimzahlen_bis(n):
    """Findet alle Zwillingsprimzahlen bis n.

    Args:
        n: Obergrenze

    Returns:
        Liste von Tupeln (p, p+2)
    """
    # Ihr Code hier
    pass

# Test
print(zwillingsprimzahlen_bis(50))
# [(3, 5), (5, 7), (11, 13), (17, 19), (29, 31), (41, 43)]
```

## Musterlösung

Versuchen Sie zuerst selbst zu lösen! Die Musterlösung finden Sie in [../05-beispiele/uebung_4_loesung.py](../05-beispiele/uebung_4_loesung.py)
