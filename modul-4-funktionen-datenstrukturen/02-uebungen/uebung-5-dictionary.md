# Übung 5: Dictionary-Operationen

**Schwierigkeit:** Einfach
**Thema:** Dictionaries erstellen, zugreifen, manipulieren

## Aufgabe 5.1: Wörterbuch

```python
woerterbuch = {
    "hello": "hallo",
    "world": "welt",
    "python": "schlange",
    "computer": "computer",
    "programming": "programmierung"
}

def uebersetze(wort):
    """Übersetzt ein englisches Wort ins Deutsche.

    Args:
        wort: Englisches Wort

    Returns:
        Deutsche Übersetzung oder "Wort nicht gefunden"
    """
    # Tipp: dict.get() mit Default-Wert
    # Ihr Code hier
    pass

# Tests
print(uebersetze("hello"))   # hallo
print(uebersetze("HELLO"))   # hallo (Gross/Klein egal)
print(uebersetze("xyz"))     # Wort nicht gefunden
```

## Aufgabe 5.2: Wortzähler

```python
def zaehle_woerter(text):
    """Zählt die Häufigkeit jedes Wortes.

    Args:
        text: Der zu analysierende Text

    Returns:
        Dictionary mit Wort: Anzahl
    """
    # Ihr Code hier
    pass

# Test
text = "Python ist toll Python macht Spass Python ist einfach"
ergebnis = zaehle_woerter(text)
print(ergebnis)
# {'python': 3, 'ist': 2, 'toll': 1, 'macht': 1, 'spass': 1, 'einfach': 1}
```

## Aufgabe 5.3: Telefonbuch

```python
def telefonbuch():
    """Einfaches Telefonbuch mit Dictionary."""
    kontakte = {}

    def hinzufuegen(name, nummer):
        """Fügt einen Kontakt hinzu."""
        # Ihr Code hier
        pass

    def suchen(name):
        """Sucht eine Nummer."""
        # Ihr Code hier
        pass

    def loeschen(name):
        """Löscht einen Kontakt."""
        # Ihr Code hier
        pass

    def alle_anzeigen():
        """Zeigt alle Kontakte."""
        # Ihr Code hier
        pass

    # Tests
    hinzufuegen("Anna", "079 123 45 67")
    hinzufuegen("Max", "078 987 65 43")
    alle_anzeigen()
    print(suchen("Anna"))  # 079 123 45 67
    print(suchen("Xyz"))   # Nicht gefunden
    loeschen("Max")
    alle_anzeigen()
```

## Aufgabe 5.4: Noten-Dictionary

```python
def berechne_statistik(noten_dict):
    """Berechnet Statistiken für Noten.

    Args:
        noten_dict: Dictionary {Name: [Noten]}

    Returns:
        Dictionary {Name: {"durchschnitt": x, "beste": y, "schlechteste": z}}
    """
    # Ihr Code hier
    pass

# Test
noten = {
    "Anna": [5.5, 6.0, 5.0, 5.5],
    "Max": [4.5, 5.0, 4.0, 4.5],
    "Lisa": [6.0, 5.5, 6.0, 5.0]
}

statistik = berechne_statistik(noten)
for name, stats in statistik.items():
    print(f"{name}: Ø {stats['durchschnitt']:.2f}")
```

## Aufgabe 5.5: Inventar

```python
def inventar_verwaltung():
    """Einfache Inventarverwaltung."""
    inventar = {
        "Apfel": {"anzahl": 50, "preis": 0.50},
        "Brot": {"anzahl": 20, "preis": 3.50},
        "Milch": {"anzahl": 30, "preis": 1.80}
    }

    def zeige_inventar():
        """Zeigt das gesamte Inventar."""
        # Ihr Code hier
        pass

    def verkaufe(produkt, menge):
        """Verkauft eine bestimmte Menge."""
        # Prüfen ob genug vorhanden
        # Ihr Code hier
        pass

    def nachfuellen(produkt, menge):
        """Füllt Bestand auf."""
        # Ihr Code hier
        pass

    def gesamtwert():
        """Berechnet den Gesamtwert des Inventars."""
        # Ihr Code hier
        pass

    # Tests
    zeige_inventar()
    verkaufe("Apfel", 5)
    print(f"Gesamtwert: {gesamtwert():.2f} CHF")
```

## Musterlösung

Versuchen Sie zuerst selbst zu lösen! Die Musterlösung finden Sie in [../05-beispiele/uebung_5_loesung.py](../05-beispiele/uebung_5_loesung.py)
