# Übung 6: Exception Handling

**Schwierigkeit:** Mittel
**Thema:** try-except, Fehlerbehandlung

## Aufgabe 6.1: Sichere Division

```python
def sichere_division(a, b):
    """Teilt a durch b mit Fehlerbehandlung.

    Args:
        a: Dividend
        b: Divisor

    Returns:
        Ergebnis oder None bei Fehler
    """
    # Fangen Sie ZeroDivisionError und TypeError
    # Ihr Code hier
    pass

# Tests
print(sichere_division(10, 2))   # 5.0
print(sichere_division(10, 0))   # None (mit Fehlermeldung)
print(sichere_division("a", 2))  # None (mit Fehlermeldung)
```

## Aufgabe 6.2: Sichere Eingabe

```python
def lese_ganzzahl(prompt, min_wert=None, max_wert=None):
    """Liest eine Ganzzahl mit Validierung.

    Args:
        prompt: Eingabeaufforderung
        min_wert: Minimaler Wert (optional)
        max_wert: Maximaler Wert (optional)

    Returns:
        Gültige Ganzzahl
    """
    # Wiederholt die Eingabe bis gültig
    # Ihr Code hier
    pass

# Test (interaktiv)
# alter = lese_ganzzahl("Ihr Alter: ", 0, 150)
# monat = lese_ganzzahl("Monat (1-12): ", 1, 12)
```

## Aufgabe 6.3: Dictionary-Zugriff

```python
def sicherer_zugriff(dictionary, *keys):
    """Greift sicher auf verschachtelte Dictionary-Werte zu.

    Args:
        dictionary: Das Dictionary
        *keys: Schlüssel-Pfad

    Returns:
        Wert oder None wenn nicht gefunden
    """
    # Beispiel: sicherer_zugriff(d, "a", "b", "c") → d["a"]["b"]["c"]
    # Ihr Code hier
    pass

# Test
daten = {
    "person": {
        "name": "Anna",
        "adresse": {
            "stadt": "Zürich",
            "plz": 8000
        }
    }
}

print(sicherer_zugriff(daten, "person", "name"))           # Anna
print(sicherer_zugriff(daten, "person", "adresse", "stadt"))  # Zürich
print(sicherer_zugriff(daten, "person", "alter"))          # None
print(sicherer_zugriff(daten, "firma"))                    # None
```

## Aufgabe 6.4: Datei lesen (Vorschau auf Modul 5)

```python
def lese_datei_sicher(dateiname):
    """Liest eine Datei mit Fehlerbehandlung.

    Args:
        dateiname: Name der Datei

    Returns:
        Inhalt als String oder None bei Fehler
    """
    # Fangen Sie FileNotFoundError und andere IOErrors
    # Ihr Code hier
    pass

# Tests
inhalt = lese_datei_sicher("test.txt")        # Datei existiert
inhalt = lese_datei_sicher("gibts_nicht.txt") # Datei existiert nicht
```

## Aufgabe 6.5: Taschenrechner

```python
def taschenrechner():
    """Einfacher Taschenrechner mit Fehlerbehandlung."""

    def berechne(ausdruck):
        """Berechnet einen Ausdruck wie '10 + 5'.

        Unterstützt: +, -, *, /
        """
        # Ihr Code hier
        # Tipp: ausdruck.split() → ['10', '+', '5']
        pass

    # Hauptschleife
    print("Taschenrechner (exit zum Beenden)")
    while True:
        eingabe = input("> ")
        if eingabe.lower() == "exit":
            break

        ergebnis = berechne(eingabe)
        if ergebnis is not None:
            print(f"= {ergebnis}")

# Tests
# taschenrechner()
# > 10 + 5
# = 15.0
# > 10 / 0
# Fehler: Division durch Null
# > abc + 5
# Fehler: Ungültige Eingabe
```

## Aufgabe 6.6: Robuste Konvertierung

```python
def konvertiere_zu_zahl(wert, typ="float"):
    """Konvertiert einen Wert zu int oder float.

    Args:
        wert: Der zu konvertierende Wert
        typ: "int" oder "float"

    Returns:
        Konvertierte Zahl oder None bei Fehler
    """
    # Ihr Code hier
    pass

# Tests
print(konvertiere_zu_zahl("42"))           # 42.0
print(konvertiere_zu_zahl("42", "int"))    # 42
print(konvertiere_zu_zahl("3.14"))         # 3.14
print(konvertiere_zu_zahl("3.14", "int"))  # 3 (gerundet)
print(konvertiere_zu_zahl("abc"))          # None
print(konvertiere_zu_zahl(None))           # None
```

## Musterlösung

Versuchen Sie zuerst selbst zu lösen! Die Musterlösung finden Sie in [../05-beispiele/uebung_6_loesung.py](../05-beispiele/uebung_6_loesung.py)
