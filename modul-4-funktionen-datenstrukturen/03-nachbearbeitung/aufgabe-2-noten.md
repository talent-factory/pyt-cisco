# Aufgabe 2: Notenverwaltung

**Zeitaufwand:** ca. 1-2 Stunden
**Thema:** Funktionen, verschachtelte Datenstrukturen, Berechnungen

## Beschreibung

Erstellen Sie ein Notenverwaltungssystem für eine Schulklasse.

## Anforderungen

### Datenstruktur

```python
klasse = {
    "info": {
        "name": "Python Kurs 2025",
        "semester": "FS25",
        "faecher": ["Programmieren", "Datenbanken", "Netzwerke"]
    },
    "studenten": {
        "S001": {
            "name": "Anna Müller",
            "noten": {
                "Programmieren": [5.5, 6.0, 5.0],
                "Datenbanken": [5.0, 5.5],
                "Netzwerke": [4.5, 5.0, 5.0]
            }
        },
        # weitere Studenten...
    }
}
```

### Zu implementierende Funktionen

```python
def student_hinzufuegen(student_id, name):
    """Fügt einen neuen Studenten hinzu."""
    pass

def note_hinzufuegen(student_id, fach, note):
    """Fügt eine Note hinzu.

    - Note muss zwischen 1.0 und 6.0 liegen
    - Fach muss in der Fächerliste existieren
    """
    pass

def durchschnitt_student(student_id):
    """Berechnet den Gesamtdurchschnitt eines Studenten."""
    pass

def durchschnitt_fach(fach):
    """Berechnet den Klassendurchschnitt für ein Fach."""
    pass

def beste_note_fach(fach):
    """Findet die beste Note und den Studenten."""
    pass

def klassenspiegel(fach):
    """Erstellt einen Notenspiegel für ein Fach.

    Returns:
        Dictionary mit Notenverteilung (6.0, 5.5, 5.0, etc.)
    """
    pass

def zeugnis_erstellen(student_id):
    """Erstellt ein Zeugnis für einen Studenten."""
    pass

def rangliste():
    """Erstellt eine Rangliste nach Durchschnitt."""
    pass

def warnung_schlechte_noten(grenzwert=4.0):
    """Findet Studenten mit Durchschnitt unter Grenzwert."""
    pass
```

## Beispielausgabe

### Zeugnis

```
╔══════════════════════════════════════════════════╗
║                    ZEUGNIS                        ║
╠══════════════════════════════════════════════════╣
║ Name: Anna Müller                                ║
║ ID: S001                                         ║
║ Semester: FS25                                   ║
╠══════════════════════════════════════════════════╣
║ Fach              │ Noten          │ Durchschnitt ║
╠═══════════════════╪════════════════╪══════════════╣
║ Programmieren     │ 5.5, 6.0, 5.0  │     5.50     ║
║ Datenbanken       │ 5.0, 5.5       │     5.25     ║
║ Netzwerke         │ 4.5, 5.0, 5.0  │     4.83     ║
╠══════════════════════════════════════════════════╣
║ Gesamtdurchschnitt:                       5.19   ║
╚══════════════════════════════════════════════════╝
```

### Klassenspiegel

```
=== Klassenspiegel Programmieren ===
6.0: ███████ 7 (35%)
5.5: █████ 5 (25%)
5.0: ████ 4 (20%)
4.5: ██ 2 (10%)
4.0: ██ 2 (10%)
---
Durchschnitt: 5.20
Beste Note: 6.0 (Anna Müller)
```

### Rangliste

```
=== Rangliste ===
 1. Anna Müller     5.50
 2. Max Weber       5.25
 3. Lisa Schmidt    5.00
 4. Tom Fischer     4.75
```

## Bewertungskriterien

- [ ] Alle Funktionen implementiert
- [ ] Korrekte Durchschnittsberechnungen
- [ ] Schöne formatierte Ausgaben
- [ ] Fehlerbehandlung (ungültige IDs, Noten, Fächer)
- [ ] Code ist modular und wiederverwendbar

## Bonus

- Exportfunktion für CSV-Format
- Importfunktion aus Testdaten
- Grafische Darstellung mit ASCII-Art (wie im Klassenspiegel)

## Abgabe

Speichern Sie Ihre Lösung als `notenverwaltung.py` im Ordner `05-beispiele/`.
