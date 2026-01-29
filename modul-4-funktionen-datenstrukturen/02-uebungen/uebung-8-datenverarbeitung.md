# Übung 8: Datenverarbeitung (CISCO LAB 4.3.8)

**Schwierigkeit:** Schwer
**Thema:** Kombination aller Konzepte

## Aufgabe 8.1: Kraftstoffverbrauch (CISCO LAB 4.3.8)

Konvertieren Sie zwischen verschiedenen Einheiten für Kraftstoffverbrauch:

```python
def liter_pro_100km_zu_mpg(l_pro_100km):
    """Konvertiert l/100km zu Miles per Gallon (US).

    Formeln:
    - 1 Meile = 1.609344 km
    - 1 US Gallone = 3.785411784 Liter
    - mpg = 235.215 / l_pro_100km
    """
    # Ihr Code hier
    pass

def mpg_zu_liter_pro_100km(mpg):
    """Konvertiert Miles per Gallon zu l/100km."""
    # Ihr Code hier
    pass

# Tests
print(liter_pro_100km_zu_mpg(7.5))   # ~31.4 mpg
print(mpg_zu_liter_pro_100km(30))    # ~7.8 l/100km
```

## Aufgabe 8.2: Notenstatistik

Erstellen Sie ein vollständiges Notenverwaltungssystem:

```python
def notensystem():
    """Komplettes Notenverwaltungssystem."""

    daten = {}

    def note_hinzufuegen(student, fach, note):
        """Fügt eine Note hinzu."""
        # Ihr Code hier
        pass

    def durchschnitt_student(student):
        """Berechnet Durchschnitt eines Studenten."""
        # Ihr Code hier
        pass

    def durchschnitt_fach(fach):
        """Berechnet Durchschnitt eines Fachs."""
        # Ihr Code hier
        pass

    def beste_note(fach):
        """Findet die beste Note in einem Fach."""
        # Ihr Code hier
        pass

    def bericht_erstellen():
        """Erstellt einen vollständigen Bericht."""
        # Ihr Code hier
        pass

    # Tests
    note_hinzufuegen("Anna", "Mathe", 5.5)
    note_hinzufuegen("Anna", "Deutsch", 5.0)
    note_hinzufuegen("Max", "Mathe", 4.5)
    note_hinzufuegen("Max", "Deutsch", 5.5)
    note_hinzufuegen("Lisa", "Mathe", 6.0)
    note_hinzufuegen("Lisa", "Deutsch", 5.0)

    print(f"Anna Durchschnitt: {durchschnitt_student('Anna'):.2f}")
    print(f"Mathe Durchschnitt: {durchschnitt_fach('Mathe'):.2f}")
    print(f"Beste Note Mathe: {beste_note('Mathe')}")
    bericht_erstellen()

# notensystem()
```

## Aufgabe 8.3: Textanalyse

```python
def analysiere_text(text):
    """Führt eine umfassende Textanalyse durch.

    Returns:
        Dictionary mit:
        - anzahl_woerter
        - anzahl_saetze
        - anzahl_zeichen
        - durchschnitt_wortlaenge
        - haeufigste_woerter (Top 5)
        - laengstes_wort
    """
    # Ihr Code hier
    pass

# Test
text = """
Python ist eine grossartige Programmiersprache. Sie ist einfach zu lernen
und sehr mächtig. Viele Unternehmen nutzen Python für Datenanalyse,
Webentwicklung und künstliche Intelligenz. Python hat eine grosse
Community und viele hilfreiche Bibliotheken.
"""

ergebnis = analysiere_text(text)
for key, value in ergebnis.items():
    print(f"{key}: {value}")
```

## Aufgabe 8.4: Bankkonten-Simulation

```python
def bank_simulation():
    """Einfache Bankkonten-Simulation."""

    konten = {}

    def konto_erstellen(kontonummer, inhaber, startguthaben=0):
        """Erstellt ein neues Konto."""
        # Ihr Code hier
        pass

    def einzahlen(kontonummer, betrag):
        """Zahlt einen Betrag ein."""
        # Mit Fehlerbehandlung
        pass

    def abheben(kontonummer, betrag):
        """Hebt einen Betrag ab."""
        # Prüfen ob genug Guthaben
        pass

    def ueberweisen(von_konto, nach_konto, betrag):
        """Überweist von einem Konto auf ein anderes."""
        # Ihr Code hier
        pass

    def kontoauszug(kontonummer):
        """Zeigt den Kontostand."""
        # Ihr Code hier
        pass

    def alle_konten():
        """Zeigt alle Konten."""
        # Ihr Code hier
        pass

    # Tests
    konto_erstellen("CH001", "Anna Müller", 1000)
    konto_erstellen("CH002", "Max Weber", 500)

    einzahlen("CH001", 200)
    abheben("CH002", 100)
    ueberweisen("CH001", "CH002", 300)

    alle_konten()

# bank_simulation()
```

## Aufgabe 8.5: Quiz-System

```python
def quiz_system():
    """Interaktives Quiz-System."""

    fragen = [
        {
            "frage": "Was gibt 'print(type([]))' aus?",
            "optionen": ["<class 'list'>", "<class 'tuple'>", "<class 'dict'>"],
            "antwort": 0
        },
        {
            "frage": "Welches Keyword definiert eine Funktion?",
            "optionen": ["function", "def", "func"],
            "antwort": 1
        },
        {
            "frage": "Was ist 2 ** 3?",
            "optionen": ["6", "8", "9"],
            "antwort": 1
        }
    ]

    def quiz_starten():
        """Startet das Quiz."""
        # Ihr Code hier
        pass

    def ergebnis_anzeigen(punkte, total):
        """Zeigt das Ergebnis an."""
        # Ihr Code hier
        pass

    # quiz_starten()

# quiz_system()
```

## Bonus: Datenvalidierung

```python
def validiere_person(daten):
    """Validiert Personendaten.

    Erwartete Struktur:
    {
        "name": str (nicht leer),
        "alter": int (0-150),
        "email": str (enthält @),
        "telefon": str (optional)
    }

    Returns:
        (True, None) wenn gültig
        (False, [Fehlermeldungen]) wenn ungültig
    """
    # Ihr Code hier
    pass

# Tests
print(validiere_person({"name": "Anna", "alter": 25, "email": "anna@mail.ch"}))
# (True, None)

print(validiere_person({"name": "", "alter": 200, "email": "invalid"}))
# (False, ['Name darf nicht leer sein', 'Alter muss zwischen 0 und 150 sein', 'Email muss @ enthalten'])
```

## Musterlösung

Versuchen Sie zuerst selbst zu lösen! Die Musterlösung finden Sie in [../05-beispiele/uebung_8_loesung.py](../05-beispiele/uebung_8_loesung.py)
