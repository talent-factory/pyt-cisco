# Übung 7: Verschachtelte Datenstrukturen

**Schwierigkeit:** Mittel
**Thema:** Dictionaries mit Listen, verschachtelte Strukturen

## Aufgabe 7.1: Klassenliste

```python
klasse = {
    "name": "Python Kurs 2025",
    "dozent": "Max Muster",
    "studenten": [
        {"name": "Anna", "noten": [5.5, 6.0, 5.0]},
        {"name": "Max", "noten": [4.5, 5.0, 4.5]},
        {"name": "Lisa", "noten": [6.0, 5.5, 5.5]}
    ]
}

def durchschnitt_student(klasse, student_name):
    """Berechnet den Durchschnitt eines Studenten."""
    # Ihr Code hier
    pass

def klassenbester(klasse):
    """Findet den Studenten mit dem besten Durchschnitt."""
    # Ihr Code hier
    pass

def klassendurchschnitt(klasse):
    """Berechnet den Durchschnitt der gesamten Klasse."""
    # Ihr Code hier
    pass

# Tests
print(durchschnitt_student(klasse, "Anna"))  # 5.5
print(klassenbester(klasse))                 # Lisa
print(klassendurchschnitt(klasse))           # ~5.17
```

## Aufgabe 7.2: Produktkatalog

```python
katalog = {
    "Elektronik": {
        "Laptop": {"preis": 999, "bestand": 10},
        "Smartphone": {"preis": 699, "bestand": 25},
        "Tablet": {"preis": 499, "bestand": 15}
    },
    "Bücher": {
        "Python Grundlagen": {"preis": 49, "bestand": 50},
        "Data Science": {"preis": 59, "bestand": 30}
    }
}

def finde_produkt(katalog, produktname):
    """Findet ein Produkt und gibt Kategorie und Details zurück."""
    # Ihr Code hier
    pass

def produkte_in_kategorie(katalog, kategorie):
    """Listet alle Produkte einer Kategorie."""
    # Ihr Code hier
    pass

def gesamtwert_kategorie(katalog, kategorie):
    """Berechnet den Gesamtwert einer Kategorie (Preis * Bestand)."""
    # Ihr Code hier
    pass

def guenstigstes_produkt(katalog):
    """Findet das günstigste Produkt über alle Kategorien."""
    # Ihr Code hier
    pass

# Tests
print(finde_produkt(katalog, "Laptop"))
# ('Elektronik', {'preis': 999, 'bestand': 10})

print(produkte_in_kategorie(katalog, "Bücher"))
# ['Python Grundlagen', 'Data Science']

print(gesamtwert_kategorie(katalog, "Elektronik"))
# 999*10 + 699*25 + 499*15 = 34950

print(guenstigstes_produkt(katalog))
# ('Python Grundlagen', 49)
```

## Aufgabe 7.3: Rezeptbuch

```python
rezepte = {
    "Pasta Carbonara": {
        "zutaten": {
            "Spaghetti": "500g",
            "Speck": "200g",
            "Eier": "4",
            "Parmesan": "100g"
        },
        "zeit": 30,
        "schwierigkeit": "mittel"
    },
    "Tomatensuppe": {
        "zutaten": {
            "Tomaten": "1kg",
            "Zwiebel": "2",
            "Knoblauch": "3 Zehen",
            "Brühe": "500ml"
        },
        "zeit": 45,
        "schwierigkeit": "einfach"
    }
}

def zeige_rezept(rezepte, name):
    """Zeigt ein Rezept formatiert an."""
    # Ihr Code hier
    pass

def rezepte_nach_zeit(rezepte, max_zeit):
    """Findet Rezepte die in max_zeit fertig sind."""
    # Ihr Code hier
    pass

def zutaten_liste(rezepte, rezept_namen):
    """Erstellt eine Einkaufsliste für mehrere Rezepte."""
    # Ihr Code hier
    pass

# Tests
zeige_rezept(rezepte, "Pasta Carbonara")
print(rezepte_nach_zeit(rezepte, 35))  # ["Pasta Carbonara"]
print(zutaten_liste(rezepte, ["Pasta Carbonara", "Tomatensuppe"]))
```

## Aufgabe 7.4: Umfrageergebnisse

```python
umfrage = [
    {"name": "Anna", "alter": 25, "antworten": {"q1": "ja", "q2": "nein", "q3": "ja"}},
    {"name": "Max", "alter": 30, "antworten": {"q1": "nein", "q2": "ja", "q3": "ja"}},
    {"name": "Lisa", "alter": 22, "antworten": {"q1": "ja", "q2": "ja", "q3": "nein"}},
    {"name": "Tom", "alter": 35, "antworten": {"q1": "ja", "q2": "nein", "q3": "ja"}},
]

def zaehle_antworten(umfrage, frage):
    """Zählt die Antworten für eine Frage."""
    # Ihr Code hier
    pass

def durchschnittsalter(umfrage, frage, antwort):
    """Berechnet das Durchschnittsalter für eine bestimmte Antwort."""
    # Ihr Code hier
    pass

def zusammenfassung(umfrage):
    """Erstellt eine Zusammenfassung der Umfrage."""
    # Ihr Code hier
    pass

# Tests
print(zaehle_antworten(umfrage, "q1"))  # {"ja": 3, "nein": 1}
print(durchschnittsalter(umfrage, "q1", "ja"))  # ~27.3
zusammenfassung(umfrage)
```

## Musterlösung

Versuchen Sie zuerst selbst zu lösen! Die Musterlösung finden Sie in [../05-beispiele/uebung_7_loesung.py](../05-beispiele/uebung_7_loesung.py)
