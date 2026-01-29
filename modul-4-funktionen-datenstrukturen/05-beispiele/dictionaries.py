"""
Dictionary-Operationen - Modul 4

Dieses Modul demonstriert Dictionary-Operationen:
- Erstellen und Zugriff
- Methoden (keys, values, items, get)
- Iteration
- Verschachtelte Dictionaries
"""


def zeige_person(person: dict):
    """Zeigt Personendaten formatiert an.

    Args:
        person: Dictionary mit Personendaten
    """
    print(f"Name: {person.get('name', 'Unbekannt')}")
    print(f"Alter: {person.get('alter', 'N/A')}")
    print(f"Stadt: {person.get('stadt', 'N/A')}")
    print("-" * 30)


def zaehle_woerter(text: str) -> dict[str, int]:
    """Zählt die Häufigkeit jedes Wortes.

    Args:
        text: Der zu analysierende Text

    Returns:
        Dictionary mit Wort: Anzahl
    """
    woerter = text.lower().split()
    zaehler: dict[str, int] = {}

    for wort in woerter:
        # Satzzeichen entfernen
        wort = wort.strip(".,!?;:")
        if wort:
            zaehler[wort] = zaehler.get(wort, 0) + 1

    return zaehler


def finde_kontakt(kontakte: dict, suchbegriff: str) -> list[dict]:
    """Sucht Kontakte nach Name oder Stadt.

    Args:
        kontakte: Dictionary mit Kontakten
        suchbegriff: Suchbegriff

    Returns:
        Liste der gefundenen Kontakte
    """
    gefunden = []
    suchbegriff = suchbegriff.lower()

    for email, daten in kontakte.items():
        name = daten.get("name", "").lower()
        stadt = daten.get("stadt", "").lower()

        if suchbegriff in name or suchbegriff in stadt:
            gefunden.append({"email": email, **daten})

    return gefunden


def erstelle_kontakt(name: str, email: str, telefon: str = "", stadt: str = "") -> dict:
    """Erstellt einen Kontakt-Eintrag.

    Args:
        name: Name des Kontakts
        email: Email-Adresse
        telefon: Telefonnummer (optional)
        stadt: Stadt (optional)

    Returns:
        Dictionary mit Kontaktdaten
    """
    return {"name": name, "email": email, "telefon": telefon, "stadt": stadt}


# Hauptprogramm
if __name__ == "__main__":
    # Basis-Operationen
    print("=== Dictionary Erstellen ===")
    person = {"name": "Anna Müller", "alter": 25, "stadt": "Zürich"}

    print(f"Dictionary: {person}")
    print(f"Keys: {list(person.keys())}")
    print(f"Values: {list(person.values())}")

    # Zugriff
    print("\n=== Zugriff ===")
    print(f"person['name']: {person['name']}")
    print(f"person.get('beruf'): {person.get('beruf')}")
    print(f"person.get('beruf', 'N/A'): {person.get('beruf', 'N/A')}")

    # Ändern
    print("\n=== Ändern/Hinzufügen ===")
    person["alter"] = 26
    person["beruf"] = "Entwicklerin"
    print(f"Nach Änderung: {person}")

    # Iteration
    print("\n=== Iteration ===")
    for key, value in person.items():
        print(f"  {key}: {value}")

    # Wortzähler
    print("\n=== Wortzähler ===")
    text = "Python ist toll. Python macht Spass. Python ist einfach."
    zaehler = zaehle_woerter(text)
    print(f"Text: {text}")
    print("Häufigkeit:")
    for wort, anzahl in sorted(zaehler.items(), key=lambda x: -x[1]):
        print(f"  {wort}: {anzahl}")

    # Kontaktverwaltung
    print("\n=== Kontaktverwaltung ===")
    kontakte = {
        "anna@mail.ch": erstelle_kontakt("Anna Müller", "anna@mail.ch", "079 123", "Zürich"),
        "max@mail.ch": erstelle_kontakt("Max Weber", "max@mail.ch", "078 456", "Bern"),
        "lisa@mail.ch": erstelle_kontakt("Lisa Schmidt", "lisa@mail.ch", "077 789", "Zürich"),
    }

    print("Alle Kontakte:")
    for email, daten in kontakte.items():
        print(f"  {daten['name']} ({email})")

    print("\nSuche nach 'Zürich':")
    gefunden = finde_kontakt(kontakte, "Zürich")
    for kontakt in gefunden:
        print(f"  {kontakt['name']} - {kontakt['email']}")

    # Prüfen ob Key existiert
    print("\n=== Key prüfen ===")
    if "anna@mail.ch" in kontakte:
        print("Anna ist im Adressbuch")

    if "xyz@mail.ch" not in kontakte:
        print("xyz ist nicht im Adressbuch")
