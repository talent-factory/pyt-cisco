# Übung 1: Funktionen Basis

**Schwierigkeit:** Einfach
**Thema:** Funktionen definieren, Parameter, Default-Werte

## Aufgabe 1.1: Trennlinie

Erstellen Sie eine Funktion `trennlinie(zeichen, laenge)`:

```python
def trennlinie(zeichen="-", laenge=40):
    """Gibt eine Trennlinie aus.

    Args:
        zeichen: Das Zeichen für die Linie (Standard: "-")
        laenge: Die Länge der Linie (Standard: 40)
    """
    # Ihr Code hier
    pass

# Tests
trennlinie()           # ----------------------------------------
trennlinie("*")        # ****************************************
trennlinie("=", 20)    # ====================
trennlinie("#", 10)    # ##########
```

## Aufgabe 1.2: Box zeichnen

Erstellen Sie eine Funktion `zeichne_box(breite, hoehe, zeichen)`:

```python
def zeichne_box(breite=10, hoehe=5, zeichen="*"):
    """Zeichnet eine Box aus Zeichen.

    Args:
        breite: Breite der Box
        hoehe: Höhe der Box
        zeichen: Zeichen für die Box
    """
    # Ihr Code hier
    pass

# Test
zeichne_box()
# **********
# *        *
# *        *
# *        *
# **********

zeichne_box(5, 3, "#")
# #####
# #   #
# #####
```

## Aufgabe 1.3: Begrüssungstext

Erstellen Sie eine Funktion `begruessung(name, sprache)`:

```python
def begruessung(name, sprache="de"):
    """Begrüsst eine Person in verschiedenen Sprachen.

    Args:
        name: Name der Person
        sprache: Sprachcode (de, en, fr, it)
    """
    # Ihr Code hier
    pass

# Tests
begruessung("Anna")             # Hallo Anna!
begruessung("Max", "en")        # Hello Max!
begruessung("Pierre", "fr")     # Bonjour Pierre!
begruessung("Marco", "it")      # Ciao Marco!
begruessung("Lisa", sprache="de")  # Hallo Lisa!
```

## Musterlösung

Versuchen Sie zuerst selbst zu lösen! Die Musterlösung finden Sie in [../05-beispiele/uebung_1_loesung.py](../05-beispiele/uebung_1_loesung.py)
