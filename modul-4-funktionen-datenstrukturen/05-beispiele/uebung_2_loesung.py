"""
Musterlösung Übung 2: Parameter

Themen: Positional, Keyword, Default-Parameter
"""


# Aufgabe 2.1: Personenbegrüssung
def begruesse_person(vorname: str, nachname: str, anrede: str = "Herr/Frau") -> str:
    """Begrüsst eine Person formell.

    Args:
        vorname: Vorname der Person
        nachname: Nachname der Person
        anrede: Anrede (Standard: "Herr/Frau")

    Returns:
        Begrüssungstext als String
    """
    return f"Guten Tag, {anrede} {vorname} {nachname}!"


# Aufgabe 2.2: Formatierte Ausgabe
def formatiere_text(text: str, breite: int = 50, ausrichtung: str = "links") -> str:
    """Formatiert Text mit bestimmter Breite und Ausrichtung.

    Args:
        text: Der zu formatierende Text
        breite: Zielbreite (Standard: 50)
        ausrichtung: "links", "rechts" oder "mitte" (Standard: "links")

    Returns:
        Formatierter Text als String
    """
    ausrichtung = ausrichtung.lower()

    if ausrichtung == "rechts":
        return text.rjust(breite)
    elif ausrichtung == "mitte":
        return text.center(breite)
    else:  # links (Standard)
        return text.ljust(breite)


# Aufgabe 2.3: Rechner-Funktion
def rechne(a: float, b: float, operation: str = "add") -> float | None:
    """Führt eine Berechnung durch.

    Args:
        a: Erste Zahl
        b: Zweite Zahl
        operation: "add", "sub", "mul", "div" (Standard: "add")

    Returns:
        Ergebnis der Berechnung oder None bei ungültiger Operation
    """
    operation = operation.lower()

    if operation == "add":
        return a + b
    elif operation == "sub":
        return a - b
    elif operation == "mul":
        return a * b
    elif operation == "div":
        if b == 0:
            print("Fehler: Division durch Null!")
            return None
        return a / b
    else:
        print(f"Fehler: Unbekannte Operation '{operation}'")
        return None


# Bonus: Preisberechnung
def berechne_preis(
    grundpreis: float, rabatt_prozent: float = 0, mwst_prozent: float = 7.7
) -> float:
    """Berechnet den Endpreis mit Rabatt und MwSt.

    Args:
        grundpreis: Preis ohne Rabatt und MwSt
        rabatt_prozent: Rabatt in Prozent (Standard: 0)
        mwst_prozent: MwSt in Prozent (Standard: 7.7)

    Returns:
        Endpreis als float
    """
    # Rabatt abziehen
    preis_nach_rabatt = grundpreis * (1 - rabatt_prozent / 100)

    # MwSt hinzufügen
    endpreis = preis_nach_rabatt * (1 + mwst_prozent / 100)

    return endpreis


# Tests
if __name__ == "__main__":
    print("=== Aufgabe 2.1: Personenbegrüssung ===")
    print(begruesse_person("Max", "Müller"))
    print(begruesse_person("Anna", "Schmidt", anrede="Frau"))
    print(begruesse_person(nachname="Weber", vorname="Lisa", anrede="Dr."))

    print("\n=== Aufgabe 2.2: Formatierte Ausgabe ===")
    print(f"|{formatiere_text('Hallo')}|")
    print(f"|{formatiere_text('Hallo', ausrichtung='rechts')}|")
    print(f"|{formatiere_text('Hallo', breite=20, ausrichtung='mitte')}|")

    print("\n=== Aufgabe 2.3: Rechner ===")
    print(f"10 + 5 = {rechne(10, 5)}")
    print(f"10 - 5 = {rechne(10, 5, 'sub')}")
    print(f"10 * 5 = {rechne(10, 5, operation='mul')}")
    print(f"10 / 2 = {rechne(b=2, a=10, operation='div')}")

    print("\n=== Bonus: Preisberechnung ===")
    print(f"100 CHF ohne Rabatt: {berechne_preis(100):.2f} CHF")
    print(f"100 CHF mit 10% Rabatt: {berechne_preis(100, rabatt_prozent=10):.2f} CHF")
    print(f"100 CHF mit 20% Rabatt, 8.1% MwSt: {berechne_preis(100, 20, 8.1):.2f} CHF")
