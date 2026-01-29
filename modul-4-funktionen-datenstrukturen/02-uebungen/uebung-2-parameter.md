# Übung 2: Parameter

**Schwierigkeit:** Einfach
**Thema:** Positional, Keyword, Default-Parameter

## Aufgabe 2.1: Personenbegrüssung

Erstellen Sie eine Funktion für formelle Begrüssungen:

```python
def begruesse_person(vorname, nachname, anrede="Herr/Frau"):
    """Begrüsst eine Person formell.

    Args:
        vorname: Vorname der Person
        nachname: Nachname der Person
        anrede: Anrede (Standard: "Herr/Frau")

    Returns:
        Begrüssungstext als String
    """
    # Ihr Code hier
    pass

# Tests
print(begruesse_person("Max", "Müller"))
# Guten Tag, Herr/Frau Max Müller!

print(begruesse_person("Anna", "Schmidt", anrede="Frau"))
# Guten Tag, Frau Anna Schmidt!

print(begruesse_person(nachname="Weber", vorname="Lisa", anrede="Dr."))
# Guten Tag, Dr. Lisa Weber!
```

## Aufgabe 2.2: Formatierte Ausgabe

Erstellen Sie eine Funktion für formatierte Textausgabe:

```python
def formatiere_text(text, breite=50, ausrichtung="links"):
    """Formatiert Text mit bestimmter Breite und Ausrichtung.

    Args:
        text: Der zu formatierende Text
        breite: Zielbreite (Standard: 50)
        ausrichtung: "links", "rechts" oder "mitte" (Standard: "links")

    Returns:
        Formatierter Text als String
    """
    # Tipp: str.ljust(), str.rjust(), str.center()
    # Ihr Code hier
    pass

# Tests
print(f"|{formatiere_text('Hallo')}|")
# |Hallo                                             |

print(f"|{formatiere_text('Hallo', ausrichtung='rechts')}|")
# |                                             Hallo|

print(f"|{formatiere_text('Hallo', breite=20, ausrichtung='mitte')}|")
# |       Hallo        |
```

## Aufgabe 2.3: Rechner-Funktion

Erstellen Sie eine flexible Rechner-Funktion:

```python
def rechne(a, b, operation="add"):
    """Führt eine Berechnung durch.

    Args:
        a: Erste Zahl
        b: Zweite Zahl
        operation: "add", "sub", "mul", "div" (Standard: "add")

    Returns:
        Ergebnis der Berechnung
    """
    # Ihr Code hier
    pass

# Tests
print(rechne(10, 5))                    # 15 (Addition)
print(rechne(10, 5, "sub"))             # 5  (Subtraktion)
print(rechne(10, 5, operation="mul"))   # 50 (Multiplikation)
print(rechne(b=2, a=10, operation="div"))  # 5.0 (Division)
```

## Bonus: Preisberechnung

```python
def berechne_preis(grundpreis, rabatt_prozent=0, mwst_prozent=7.7):
    """Berechnet den Endpreis mit Rabatt und MwSt.

    Args:
        grundpreis: Preis ohne Rabatt und MwSt
        rabatt_prozent: Rabatt in Prozent (Standard: 0)
        mwst_prozent: MwSt in Prozent (Standard: 7.7)

    Returns:
        Endpreis als float
    """
    # Ihr Code hier
    pass

# Tests
print(berechne_preis(100))                      # 107.70
print(berechne_preis(100, rabatt_prozent=10))   # 96.93
print(berechne_preis(100, 20, 8.1))             # 86.48
```

## Musterlösung

Versuchen Sie zuerst selbst zu lösen! Die Musterlösung finden Sie in [../05-beispiele/uebung_2_loesung.py](../05-beispiele/uebung_2_loesung.py)
