"""
Musterlösung Übung 5: Dictionary-Operationen

Themen: Dictionaries erstellen, zugreifen, manipulieren
"""


# Aufgabe 5.1: Wörterbuch
woerterbuch = {
    "hello": "hallo",
    "world": "welt",
    "python": "schlange",
    "computer": "computer",
    "programming": "programmierung",
}


def uebersetze(wort: str) -> str:
    """Übersetzt ein englisches Wort ins Deutsche.

    Args:
        wort: Englisches Wort

    Returns:
        Deutsche Übersetzung oder "Wort nicht gefunden"
    """
    # Gross/Klein-Schreibung ignorieren
    wort_lower = wort.lower()
    return woerterbuch.get(wort_lower, "Wort nicht gefunden")


# Aufgabe 5.2: Wortzähler
def zaehle_woerter(text: str) -> dict[str, int]:
    """Zählt die Häufigkeit jedes Wortes.

    Args:
        text: Der zu analysierende Text

    Returns:
        Dictionary mit Wort: Anzahl
    """
    # Text in Wörter aufteilen (lowercase)
    woerter = text.lower().split()

    zaehler: dict[str, int] = {}
    for wort in woerter:
        # Satzzeichen entfernen
        wort = wort.strip(".,!?;:\"'")
        if wort:
            zaehler[wort] = zaehler.get(wort, 0) + 1

    return zaehler


# Aufgabe 5.3: Telefonbuch
def telefonbuch_demo():
    """Einfaches Telefonbuch mit Dictionary."""
    kontakte: dict[str, str] = {}

    def hinzufuegen(name: str, nummer: str):
        """Fügt einen Kontakt hinzu."""
        kontakte[name] = nummer
        print(f"✓ {name} hinzugefügt.")

    def suchen(name: str) -> str:
        """Sucht eine Nummer."""
        return kontakte.get(name, "Nicht gefunden")

    def loeschen(name: str):
        """Löscht einen Kontakt."""
        if name in kontakte:
            del kontakte[name]
            print(f"✓ {name} gelöscht.")
        else:
            print(f"✗ {name} nicht gefunden.")

    def alle_anzeigen():
        """Zeigt alle Kontakte."""
        if not kontakte:
            print("Keine Kontakte vorhanden.")
            return

        print("\n--- Kontakte ---")
        for name, nummer in sorted(kontakte.items()):
            print(f"  {name}: {nummer}")

    # Tests
    hinzufuegen("Anna", "079 123 45 67")
    hinzufuegen("Max", "078 987 65 43")
    alle_anzeigen()
    print(f"\nAnna: {suchen('Anna')}")
    print(f"Xyz: {suchen('Xyz')}")
    loeschen("Max")
    alle_anzeigen()


# Aufgabe 5.4: Noten-Dictionary
def berechne_statistik(noten_dict: dict[str, list[float]]) -> dict[str, dict[str, float]]:
    """Berechnet Statistiken für Noten.

    Args:
        noten_dict: Dictionary {Name: [Noten]}

    Returns:
        Dictionary {Name: {"durchschnitt": x, "beste": y, "schlechteste": z}}
    """
    statistik = {}

    for name, noten in noten_dict.items():
        if noten:
            statistik[name] = {
                "durchschnitt": sum(noten) / len(noten),
                "beste": max(noten),
                "schlechteste": min(noten),
            }
        else:
            statistik[name] = {
                "durchschnitt": 0,
                "beste": 0,
                "schlechteste": 0,
            }

    return statistik


# Aufgabe 5.5: Inventar
def inventar_demo():
    """Einfache Inventarverwaltung."""
    inventar = {
        "Apfel": {"anzahl": 50, "preis": 0.50},
        "Brot": {"anzahl": 20, "preis": 3.50},
        "Milch": {"anzahl": 30, "preis": 1.80},
    }

    def zeige_inventar():
        """Zeigt das gesamte Inventar."""
        print("\n--- Inventar ---")
        print(f"{'Produkt':<15} {'Anzahl':>8} {'Preis':>10} {'Wert':>12}")
        print("-" * 47)
        for produkt, daten in inventar.items():
            wert = daten["anzahl"] * daten["preis"]
            print(f"{produkt:<15} {daten['anzahl']:>8} {daten['preis']:>10.2f} {wert:>12.2f}")

    def verkaufe(produkt: str, menge: int) -> bool:
        """Verkauft eine bestimmte Menge."""
        if produkt not in inventar:
            print(f"✗ Produkt '{produkt}' nicht gefunden.")
            return False

        if inventar[produkt]["anzahl"] < menge:
            print(f"✗ Nicht genug {produkt} vorhanden.")
            return False

        inventar[produkt]["anzahl"] -= menge
        print(f"✓ {menge}x {produkt} verkauft.")
        return True

    def nachfuellen(produkt: str, menge: int):
        """Füllt Bestand auf."""
        if produkt in inventar:
            inventar[produkt]["anzahl"] += menge
        else:
            # Neues Produkt (mit Standardpreis)
            inventar[produkt] = {"anzahl": menge, "preis": 0.0}
        print(f"✓ {menge}x {produkt} aufgefüllt.")

    def gesamtwert() -> float:
        """Berechnet den Gesamtwert des Inventars."""
        total = 0.0
        for daten in inventar.values():
            total += daten["anzahl"] * daten["preis"]
        return total

    # Tests
    zeige_inventar()
    verkaufe("Apfel", 5)
    nachfuellen("Brot", 10)
    zeige_inventar()
    print(f"\nGesamtwert: {gesamtwert():.2f} CHF")


# Tests
if __name__ == "__main__":
    print("=== Aufgabe 5.1: Wörterbuch ===")
    print(f"hello → {uebersetze('hello')}")
    print(f"HELLO → {uebersetze('HELLO')}")
    print(f"xyz → {uebersetze('xyz')}")

    print("\n=== Aufgabe 5.2: Wortzähler ===")
    text = "Python ist toll Python macht Spass Python ist einfach"
    ergebnis = zaehle_woerter(text)
    print(f"Text: {text}")
    print("Häufigkeit:")
    for wort, anzahl in sorted(ergebnis.items(), key=lambda x: -x[1]):
        print(f"  {wort}: {anzahl}")

    print("\n=== Aufgabe 5.3: Telefonbuch ===")
    telefonbuch_demo()

    print("\n=== Aufgabe 5.4: Noten-Statistik ===")
    noten = {
        "Anna": [5.5, 6.0, 5.0, 5.5],
        "Max": [4.5, 5.0, 4.0, 4.5],
        "Lisa": [6.0, 5.5, 6.0, 5.0],
    }
    statistik = berechne_statistik(noten)
    for name, stats in statistik.items():
        print(f"{name}: Ø {stats['durchschnitt']:.2f}, "
              f"Beste: {stats['beste']}, Schlechteste: {stats['schlechteste']}")

    print("\n=== Aufgabe 5.5: Inventar ===")
    inventar_demo()
