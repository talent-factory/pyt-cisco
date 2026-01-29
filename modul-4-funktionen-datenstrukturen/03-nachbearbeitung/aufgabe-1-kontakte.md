# Aufgabe 1: Kontaktverwaltung

**Zeitaufwand:** ca. 1-2 Stunden
**Thema:** Funktionen, Dictionaries, Exception Handling

## Beschreibung

Erstellen Sie eine Kontaktverwaltung mit folgenden Funktionen:

1. Kontakte hinzufügen
2. Kontakte suchen
3. Kontakte bearbeiten
4. Kontakte löschen
5. Alle Kontakte anzeigen
6. Kontakte nach Kriterien filtern

## Anforderungen

### Datenstruktur

```python
kontakte = {
    "anna.mueller@mail.ch": {
        "vorname": "Anna",
        "nachname": "Müller",
        "telefon": "079 123 45 67",
        "kategorie": "Freunde"
    },
    # weitere Kontakte...
}
```

### Zu implementierende Funktionen

```python
def kontakt_hinzufuegen(email, vorname, nachname, telefon="", kategorie="Allgemein"):
    """Fügt einen neuen Kontakt hinzu.

    - Email muss @ enthalten
    - Email darf nicht bereits existieren
    - Vorname und Nachname dürfen nicht leer sein
    """
    pass

def kontakt_suchen(suchbegriff):
    """Sucht Kontakte nach Name, Email oder Telefon.

    Returns:
        Liste der gefundenen Kontakte
    """
    pass

def kontakt_bearbeiten(email, feld, neuer_wert):
    """Bearbeitet ein Feld eines Kontakts.

    Args:
        email: Email des Kontakts
        feld: "vorname", "nachname", "telefon" oder "kategorie"
        neuer_wert: Neuer Wert für das Feld
    """
    pass

def kontakt_loeschen(email):
    """Löscht einen Kontakt nach Bestätigung."""
    pass

def alle_kontakte_anzeigen(sortiert_nach="nachname"):
    """Zeigt alle Kontakte sortiert an."""
    pass

def kontakte_filtern(kategorie=None, anfangsbuchstabe=None):
    """Filtert Kontakte nach Kategorie oder Anfangsbuchstaben."""
    pass

def exportiere_kontakte():
    """Gibt alle Kontakte als formatierten String zurück."""
    pass
```

### Hauptmenü

```python
def hauptmenu():
    """Zeigt das Hauptmenü und verarbeitet Benutzereingaben."""
    while True:
        print("\n=== KONTAKTVERWALTUNG ===")
        print("1. Neuer Kontakt")
        print("2. Kontakt suchen")
        print("3. Kontakt bearbeiten")
        print("4. Kontakt löschen")
        print("5. Alle Kontakte")
        print("6. Kontakte filtern")
        print("7. Beenden")

        wahl = input("\nIhre Wahl: ")
        # Implementieren Sie die Menülogik
```

## Bewertungskriterien

- [ ] Alle Funktionen implementiert
- [ ] Fehlerbehandlung mit try-except
- [ ] Eingabevalidierung
- [ ] Sinnvolle Ausgaben und Rückmeldungen
- [ ] Code ist gut strukturiert und kommentiert

## Beispielausgabe

```
=== KONTAKTVERWALTUNG ===
1. Neuer Kontakt
2. Kontakt suchen
...

Ihre Wahl: 1

--- Neuer Kontakt ---
Email: anna@mail.ch
Vorname: Anna
Nachname: Müller
Telefon (optional): 079 123 45 67
Kategorie [Allgemein]: Freunde

✓ Kontakt anna@mail.ch wurde hinzugefügt.

Ihre Wahl: 5

--- Alle Kontakte (1) ---
Anna Müller
  Email: anna@mail.ch
  Telefon: 079 123 45 67
  Kategorie: Freunde
```

## Tipps

- Beginnen Sie mit der Datenstruktur und einfachen Funktionen
- Fügen Sie Schritt für Schritt Fehlerbehandlung hinzu
- Testen Sie jede Funktion einzeln bevor Sie das Menü implementieren

## Abgabe

Speichern Sie Ihre Lösung als `kontaktverwaltung.py` im Ordner `05-beispiele/`.
