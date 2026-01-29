"""
Musterlösung Übung 6: Exception Handling

Themen: try-except, Fehlerbehandlung
"""


# Aufgabe 6.1: Sichere Division
def sichere_division(a, b) -> float | None:
    """Teilt a durch b mit Fehlerbehandlung.

    Args:
        a: Dividend
        b: Divisor

    Returns:
        Ergebnis oder None bei Fehler
    """
    try:
        return a / b
    except ZeroDivisionError:
        print("Fehler: Division durch Null!")
        return None
    except TypeError:
        print("Fehler: Ungültiger Datentyp!")
        return None


# Aufgabe 6.2: Sichere Eingabe
def lese_ganzzahl(prompt: str, min_wert: int = None, max_wert: int = None) -> int:
    """Liest eine Ganzzahl mit Validierung.

    Args:
        prompt: Eingabeaufforderung
        min_wert: Minimaler Wert (optional)
        max_wert: Maximaler Wert (optional)

    Returns:
        Gültige Ganzzahl
    """
    while True:
        try:
            eingabe = input(prompt)
            zahl = int(eingabe)

            if min_wert is not None and zahl < min_wert:
                print(f"Zahl muss mindestens {min_wert} sein.")
                continue

            if max_wert is not None and zahl > max_wert:
                print(f"Zahl darf höchstens {max_wert} sein.")
                continue

            return zahl

        except ValueError:
            print("Bitte eine gültige Ganzzahl eingeben.")


# Aufgabe 6.3: Dictionary-Zugriff
def sicherer_zugriff(dictionary: dict, *keys):
    """Greift sicher auf verschachtelte Dictionary-Werte zu.

    Args:
        dictionary: Das Dictionary
        *keys: Schlüssel-Pfad

    Returns:
        Wert oder None wenn nicht gefunden
    """
    result = dictionary

    for key in keys:
        try:
            result = result[key]
        except (KeyError, TypeError):
            return None

    return result


# Aufgabe 6.4: Datei lesen
def lese_datei_sicher(dateiname: str) -> str | None:
    """Liest eine Datei mit Fehlerbehandlung.

    Args:
        dateiname: Name der Datei

    Returns:
        Inhalt als String oder None bei Fehler
    """
    try:
        with open(dateiname, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Fehler: Datei '{dateiname}' nicht gefunden.")
        return None
    except PermissionError:
        print(f"Fehler: Keine Berechtigung für '{dateiname}'.")
        return None
    except OSError as e:
        print(f"Fehler beim Lesen: {e}")
        return None


# Aufgabe 6.5: Taschenrechner
def taschenrechner_demo():
    """Einfacher Taschenrechner mit Fehlerbehandlung."""

    def berechne(ausdruck: str) -> float | None:
        """Berechnet einen Ausdruck wie '10 + 5'."""
        try:
            teile = ausdruck.split()

            if len(teile) != 3:
                print("Fehler: Format muss sein: Zahl Operator Zahl")
                return None

            zahl1 = float(teile[0])
            operator = teile[1]
            zahl2 = float(teile[2])

            if operator == "+":
                return zahl1 + zahl2
            elif operator == "-":
                return zahl1 - zahl2
            elif operator == "*":
                return zahl1 * zahl2
            elif operator == "/":
                if zahl2 == 0:
                    print("Fehler: Division durch Null!")
                    return None
                return zahl1 / zahl2
            else:
                print(f"Fehler: Unbekannter Operator '{operator}'")
                return None

        except ValueError:
            print("Fehler: Ungültige Zahlen!")
            return None

    # Demo-Berechnungen (ohne interaktive Eingabe)
    testfaelle = ["10 + 5", "20 - 8", "7 * 6", "100 / 4", "10 / 0", "abc + 5", "1 2 3 4"]

    print("Taschenrechner Demo:")
    for ausdruck in testfaelle:
        print(f"> {ausdruck}")
        ergebnis = berechne(ausdruck)
        if ergebnis is not None:
            print(f"= {ergebnis}")
        print()


# Aufgabe 6.6: Robuste Konvertierung
def konvertiere_zu_zahl(wert, typ: str = "float") -> int | float | None:
    """Konvertiert einen Wert zu int oder float.

    Args:
        wert: Der zu konvertierende Wert
        typ: "int" oder "float"

    Returns:
        Konvertierte Zahl oder None bei Fehler
    """
    try:
        if typ == "int":
            # Erst zu float, dann zu int (für "3.14" → 3)
            return int(float(wert))
        else:
            return float(wert)
    except (ValueError, TypeError):
        return None


# Tests
if __name__ == "__main__":
    print("=== Aufgabe 6.1: Sichere Division ===")
    print(f"10 / 2 = {sichere_division(10, 2)}")
    print(f"10 / 0 = {sichere_division(10, 0)}")
    print(f"'a' / 2 = {sichere_division('a', 2)}")

    print("\n=== Aufgabe 6.3: Sicherer Zugriff ===")
    daten = {
        "person": {
            "name": "Anna",
            "adresse": {"stadt": "Zürich", "plz": 8000},
        }
    }
    print(f"person.name: {sicherer_zugriff(daten, 'person', 'name')}")
    print(f"person.adresse.stadt: {sicherer_zugriff(daten, 'person', 'adresse', 'stadt')}")
    print(f"person.alter: {sicherer_zugriff(daten, 'person', 'alter')}")
    print(f"firma: {sicherer_zugriff(daten, 'firma')}")

    print("\n=== Aufgabe 6.4: Datei lesen ===")
    inhalt = lese_datei_sicher("gibts_nicht.txt")

    print("\n=== Aufgabe 6.5: Taschenrechner ===")
    taschenrechner_demo()

    print("=== Aufgabe 6.6: Robuste Konvertierung ===")
    testwerte = [("42", "float"), ("42", "int"), ("3.14", "float"), ("3.14", "int"), ("abc", "float"), (None, "int")]
    for wert, typ in testwerte:
        ergebnis = konvertiere_zu_zahl(wert, typ)
        print(f"konvertiere_zu_zahl({wert!r}, {typ!r}) = {ergebnis}")

    # Interaktive Eingabe (auskommentiert)
    # print("\n=== Aufgabe 6.2: Sichere Eingabe ===")
    # alter = lese_ganzzahl("Ihr Alter (0-150): ", 0, 150)
    # print(f"Eingegebenes Alter: {alter}")
