# Aufgabe 3: Mini-Projekt nach Wahl

**Zeitaufwand:** ca. 2-3 Stunden
**Thema:** Freie Anwendung aller gelernten Konzepte

## Beschreibung

Wählen Sie eines der folgenden Mini-Projekte und implementieren Sie es vollständig.

## Option A: Quiz-Spiel

Erstellen Sie ein interaktives Quiz mit:
- Mindestens 10 Fragen aus verschiedenen Kategorien
- Multiple-Choice Antworten
- Punktesystem
- Highscore-Liste
- Verschiedene Schwierigkeitsgrade

```python
fragen = {
    "Python": [
        {
            "frage": "Was gibt print(type([])) aus?",
            "optionen": ["list", "tuple", "dict", "set"],
            "antwort": 0,
            "schwierigkeit": "einfach"
        },
        # ...
    ],
    "Allgemeinwissen": [
        # ...
    ]
}
```

## Option B: Rezeptbuch

Erstellen Sie eine Rezeptverwaltung mit:
- Rezepte mit Zutaten und Mengenangaben
- Portionen anpassen (Zutaten umrechnen)
- Einkaufsliste generieren
- Rezepte nach Zutaten suchen
- Kategorien (Vorspeise, Hauptgang, Dessert)

## Option C: Vokabeltrainer

Erstellen Sie einen Vokabeltrainer mit:
- Wörter hinzufügen (DE ↔ EN)
- Abfrage in beide Richtungen
- Fortschritt tracken (richtig/falsch)
- Schwierige Wörter häufiger abfragen
- Statistik anzeigen

## Option D: Ausgabenverwaltung

Erstellen Sie eine einfache Finanzverwaltung mit:
- Einnahmen und Ausgaben erfassen
- Kategorien (Essen, Transport, Unterhaltung, etc.)
- Monatliche Zusammenfassung
- Budget-Warnung
- Statistiken

## Option E: Eigene Idee

Sie können auch ein eigenes Projekt vorschlagen. Besprechen Sie es mit Ihrem Kursleiter.

## Anforderungen (für alle Projekte)

### Pflicht

- [ ] Mindestens 5 verschiedene Funktionen
- [ ] Verwendung von Dictionaries
- [ ] Verwendung von Listen
- [ ] Exception Handling
- [ ] Benutzermenü mit Eingabevalidierung
- [ ] Sinnvolle Dokumentation (Docstrings)

### Bonus

- [ ] Daten speichern/laden (Textdatei)
- [ ] Erweiterte Funktionen
- [ ] Besonders schöne Ausgaben/Formatierung

## Projektstruktur

```python
"""
Mini-Projekt: [Name]
Autor: [Ihr Name]
Datum: [Datum]

Beschreibung:
[Kurze Beschreibung was das Programm macht]
"""

# Globale Variablen / Datenstrukturen
daten = {}

# Hilfsfunktionen
def funktion_1():
    """Beschreibung."""
    pass

def funktion_2():
    """Beschreibung."""
    pass

# Hauptfunktionen
def hauptmenu():
    """Zeigt das Hauptmenü."""
    pass

# Programmstart
if __name__ == "__main__":
    print("Willkommen zu [Projektname]!")
    hauptmenu()
```

## Bewertungskriterien

| Kriterium | Punkte |
|-----------|--------|
| Funktionalität vollständig | 30 |
| Code-Qualität und Struktur | 20 |
| Fehlerbehandlung | 15 |
| Benutzerfreundlichkeit | 15 |
| Dokumentation | 10 |
| Kreativität/Bonus | 10 |
| **Total** | **100** |

## Abgabe

- Speichern Sie Ihre Lösung als `miniprojekt_[name].py`
- Fügen Sie eine kurze README.md bei mit:
  - Projektbeschreibung
  - Anleitung zur Verwendung
  - Bekannte Einschränkungen

## Tipps

1. Planen Sie zuerst die Datenstruktur
2. Implementieren Sie eine Funktion nach der anderen
3. Testen Sie regelmässig
4. Fügen Sie Fehlerbehandlung zum Schluss hinzu
5. Dokumentieren Sie während dem Programmieren
