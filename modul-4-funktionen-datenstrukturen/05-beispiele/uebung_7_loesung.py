"""
Musterlösung Übung 7: Verschachtelte Datenstrukturen

Themen: Dictionaries mit Listen, verschachtelte Strukturen
"""


# Aufgabe 7.1: Klassenliste
klasse = {
    "name": "Python Kurs 2025",
    "dozent": "Max Muster",
    "studenten": [
        {"name": "Anna", "noten": [5.5, 6.0, 5.0]},
        {"name": "Max", "noten": [4.5, 5.0, 4.5]},
        {"name": "Lisa", "noten": [6.0, 5.5, 5.5]},
    ],
}


def durchschnitt_student(klasse: dict, student_name: str) -> float | None:
    """Berechnet den Durchschnitt eines Studenten."""
    for student in klasse["studenten"]:
        if student["name"].lower() == student_name.lower():
            noten = student["noten"]
            if noten:
                return sum(noten) / len(noten)
            return 0.0
    return None


def klassenbester(klasse: dict) -> str | None:
    """Findet den Studenten mit dem besten Durchschnitt."""
    bester = None
    bester_durchschnitt = 0.0

    for student in klasse["studenten"]:
        noten = student["noten"]
        if noten:
            durchschnitt = sum(noten) / len(noten)
            if durchschnitt > bester_durchschnitt:
                bester_durchschnitt = durchschnitt
                bester = student["name"]

    return bester


def klassendurchschnitt(klasse: dict) -> float:
    """Berechnet den Durchschnitt der gesamten Klasse."""
    alle_noten = []
    for student in klasse["studenten"]:
        alle_noten.extend(student["noten"])

    if alle_noten:
        return sum(alle_noten) / len(alle_noten)
    return 0.0


# Aufgabe 7.2: Produktkatalog
katalog = {
    "Elektronik": {
        "Laptop": {"preis": 999, "bestand": 10},
        "Smartphone": {"preis": 699, "bestand": 25},
        "Tablet": {"preis": 499, "bestand": 15},
    },
    "Bücher": {
        "Python Grundlagen": {"preis": 49, "bestand": 50},
        "Data Science": {"preis": 59, "bestand": 30},
    },
}


def finde_produkt(katalog: dict, produktname: str) -> tuple[str, dict] | None:
    """Findet ein Produkt und gibt Kategorie und Details zurück."""
    for kategorie, produkte in katalog.items():
        if produktname in produkte:
            return (kategorie, produkte[produktname])
    return None


def produkte_in_kategorie(katalog: dict, kategorie: str) -> list[str]:
    """Listet alle Produkte einer Kategorie."""
    if kategorie in katalog:
        return list(katalog[kategorie].keys())
    return []


def gesamtwert_kategorie(katalog: dict, kategorie: str) -> float:
    """Berechnet den Gesamtwert einer Kategorie (Preis * Bestand)."""
    if kategorie not in katalog:
        return 0.0

    total = 0.0
    for produkt in katalog[kategorie].values():
        total += produkt["preis"] * produkt["bestand"]
    return total


def guenstigstes_produkt(katalog: dict) -> tuple[str, float] | None:
    """Findet das günstigste Produkt über alle Kategorien."""
    guenstigster_name = None
    guenstigster_preis = float("inf")

    for produkte in katalog.values():
        for name, daten in produkte.items():
            if daten["preis"] < guenstigster_preis:
                guenstigster_preis = daten["preis"]
                guenstigster_name = name

    if guenstigster_name:
        return (guenstigster_name, guenstigster_preis)
    return None


# Aufgabe 7.3: Rezeptbuch
rezepte = {
    "Pasta Carbonara": {
        "zutaten": {
            "Spaghetti": "500g",
            "Speck": "200g",
            "Eier": "4",
            "Parmesan": "100g",
        },
        "zeit": 30,
        "schwierigkeit": "mittel",
    },
    "Tomatensuppe": {
        "zutaten": {
            "Tomaten": "1kg",
            "Zwiebel": "2",
            "Knoblauch": "3 Zehen",
            "Brühe": "500ml",
        },
        "zeit": 45,
        "schwierigkeit": "einfach",
    },
}


def zeige_rezept(rezepte: dict, name: str):
    """Zeigt ein Rezept formatiert an."""
    if name not in rezepte:
        print(f"Rezept '{name}' nicht gefunden.")
        return

    rezept = rezepte[name]
    print(f"\n{'=' * 40}")
    print(f"  {name}")
    print(f"{'=' * 40}")
    print(f"Zeit: {rezept['zeit']} Minuten")
    print(f"Schwierigkeit: {rezept['schwierigkeit']}")
    print("\nZutaten:")
    for zutat, menge in rezept["zutaten"].items():
        print(f"  - {zutat}: {menge}")


def rezepte_nach_zeit(rezepte: dict, max_zeit: int) -> list[str]:
    """Findet Rezepte die in max_zeit fertig sind."""
    gefunden = []
    for name, daten in rezepte.items():
        if daten["zeit"] <= max_zeit:
            gefunden.append(name)
    return gefunden


def zutaten_liste(rezepte: dict, rezept_namen: list[str]) -> dict[str, str]:
    """Erstellt eine Einkaufsliste für mehrere Rezepte."""
    einkaufsliste: dict[str, str] = {}

    for name in rezept_namen:
        if name in rezepte:
            for zutat, menge in rezepte[name]["zutaten"].items():
                if zutat in einkaufsliste:
                    # Zutat bereits vorhanden, Menge anhängen
                    einkaufsliste[zutat] += f" + {menge}"
                else:
                    einkaufsliste[zutat] = menge

    return einkaufsliste


# Aufgabe 7.4: Umfrageergebnisse
umfrage = [
    {"name": "Anna", "alter": 25, "antworten": {"q1": "ja", "q2": "nein", "q3": "ja"}},
    {"name": "Max", "alter": 30, "antworten": {"q1": "nein", "q2": "ja", "q3": "ja"}},
    {"name": "Lisa", "alter": 22, "antworten": {"q1": "ja", "q2": "ja", "q3": "nein"}},
    {"name": "Tom", "alter": 35, "antworten": {"q1": "ja", "q2": "nein", "q3": "ja"}},
]


def zaehle_antworten(umfrage: list, frage: str) -> dict[str, int]:
    """Zählt die Antworten für eine Frage."""
    zaehler: dict[str, int] = {}

    for teilnehmer in umfrage:
        antwort = teilnehmer["antworten"].get(frage)
        if antwort:
            zaehler[antwort] = zaehler.get(antwort, 0) + 1

    return zaehler


def durchschnittsalter(umfrage: list, frage: str, antwort: str) -> float:
    """Berechnet das Durchschnittsalter für eine bestimmte Antwort."""
    alter_liste = []

    for teilnehmer in umfrage:
        if teilnehmer["antworten"].get(frage) == antwort:
            alter_liste.append(teilnehmer["alter"])

    if alter_liste:
        return sum(alter_liste) / len(alter_liste)
    return 0.0


def zusammenfassung(umfrage: list):
    """Erstellt eine Zusammenfassung der Umfrage."""
    print("\n=== Umfrage-Zusammenfassung ===")
    print(f"Teilnehmer: {len(umfrage)}")

    # Alle Fragen sammeln
    alle_fragen = set()
    for t in umfrage:
        alle_fragen.update(t["antworten"].keys())

    for frage in sorted(alle_fragen):
        antworten = zaehle_antworten(umfrage, frage)
        print(f"\n{frage}:")
        for antwort, anzahl in antworten.items():
            prozent = anzahl / len(umfrage) * 100
            print(f"  {antwort}: {anzahl} ({prozent:.0f}%)")


# Tests
if __name__ == "__main__":
    print("=== Aufgabe 7.1: Klassenliste ===")
    print(f"Durchschnitt Anna: {durchschnitt_student(klasse, 'Anna'):.2f}")
    print(f"Klassenbester: {klassenbester(klasse)}")
    print(f"Klassendurchschnitt: {klassendurchschnitt(klasse):.2f}")

    print("\n=== Aufgabe 7.2: Produktkatalog ===")
    print(f"Finde Laptop: {finde_produkt(katalog, 'Laptop')}")
    print(f"Produkte in Bücher: {produkte_in_kategorie(katalog, 'Bücher')}")
    print(f"Gesamtwert Elektronik: {gesamtwert_kategorie(katalog, 'Elektronik'):.2f} CHF")
    print(f"Günstigstes Produkt: {guenstigstes_produkt(katalog)}")

    print("\n=== Aufgabe 7.3: Rezeptbuch ===")
    zeige_rezept(rezepte, "Pasta Carbonara")
    print(f"\nRezepte unter 35 Min: {rezepte_nach_zeit(rezepte, 35)}")
    print(f"Einkaufsliste: {zutaten_liste(rezepte, ['Pasta Carbonara', 'Tomatensuppe'])}")

    print("\n=== Aufgabe 7.4: Umfrageergebnisse ===")
    print(f"Antworten q1: {zaehle_antworten(umfrage, 'q1')}")
    print(f"Durchschnittsalter (q1=ja): {durchschnittsalter(umfrage, 'q1', 'ja'):.1f}")
    zusammenfassung(umfrage)
