"""
Exception Handling - Modul 4

Dieses Modul demonstriert Fehlerbehandlung:
- try-except Blöcke
- Verschiedene Exception-Typen
- finally
- Eigene Validierung
"""


def sichere_division(a: float, b: float) -> float | None:
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


def sichere_zahl_eingabe(prompt: str, min_wert: float = None, max_wert: float = None) -> float:
    """Liest eine Zahl sicher ein mit Validierung.

    Args:
        prompt: Eingabeaufforderung
        min_wert: Minimaler Wert (optional)
        max_wert: Maximaler Wert (optional)

    Returns:
        Gültige Zahl
    """
    while True:
        try:
            eingabe = input(prompt)
            zahl = float(eingabe)

            if min_wert is not None and zahl < min_wert:
                print(f"Zahl muss mindestens {min_wert} sein.")
                continue

            if max_wert is not None and zahl > max_wert:
                print(f"Zahl darf höchstens {max_wert} sein.")
                continue

            return zahl

        except ValueError:
            print("Bitte eine gültige Zahl eingeben.")


def sicherer_dict_zugriff(dictionary: dict, key: str, default=None):
    """Greift sicher auf Dictionary-Werte zu.

    Args:
        dictionary: Das Dictionary
        key: Der Schlüssel
        default: Standardwert wenn nicht gefunden

    Returns:
        Wert oder default
    """
    try:
        return dictionary[key]
    except KeyError:
        return default


def sicherer_listen_zugriff(liste: list, index: int, default=None):
    """Greift sicher auf Listen-Elemente zu.

    Args:
        liste: Die Liste
        index: Der Index
        default: Standardwert wenn ungültig

    Returns:
        Element oder default
    """
    try:
        return liste[index]
    except IndexError:
        return default


def konvertiere_zu_int(wert, default: int = 0) -> int:
    """Konvertiert einen Wert zu int.

    Args:
        wert: Der zu konvertierende Wert
        default: Standardwert bei Fehler

    Returns:
        Konvertierte Zahl oder default
    """
    try:
        return int(wert)
    except (ValueError, TypeError):
        return default


def demonstriere_finally():
    """Demonstriert den finally-Block."""
    print("\n=== Finally Demo ===")

    try:
        print("Versuche eine Operation...")
        # Hier könnte ein Fehler auftreten
        result = 10 / 2
        print(f"Ergebnis: {result}")
    except ZeroDivisionError:
        print("Division durch Null!")
    finally:
        print("Finally wird IMMER ausgeführt!")


def demonstriere_exception_info():
    """Zeigt Informationen über Exceptions."""
    print("\n=== Exception Info ===")

    try:
        int("abc")
    except ValueError as e:
        print(f"Exception-Typ: {type(e).__name__}")
        print(f"Exception-Nachricht: {e}")


def validiere_email(email: str) -> bool:
    """Validiert eine Email-Adresse (vereinfacht).

    Args:
        email: Die zu validierende Email

    Returns:
        True wenn gültig
    """
    if not email:
        raise ValueError("Email darf nicht leer sein")

    if "@" not in email:
        raise ValueError("Email muss @ enthalten")

    if "." not in email.split("@")[1]:
        raise ValueError("Domain muss einen Punkt enthalten")

    return True


# Hauptprogramm
if __name__ == "__main__":
    # Sichere Division
    print("=== Sichere Division ===")
    print(f"10 / 2 = {sichere_division(10, 2)}")
    print(f"10 / 0 = {sichere_division(10, 0)}")
    print(f"'a' / 2 = {sichere_division('a', 2)}")

    # Dictionary-Zugriff
    print("\n=== Sicherer Dictionary-Zugriff ===")
    person = {"name": "Anna", "alter": 25}
    print(f"name: {sicherer_dict_zugriff(person, 'name')}")
    print(f"stadt: {sicherer_dict_zugriff(person, 'stadt', 'Unbekannt')}")

    # Listen-Zugriff
    print("\n=== Sicherer Listen-Zugriff ===")
    zahlen = [1, 2, 3]
    print(f"Index 1: {sicherer_listen_zugriff(zahlen, 1)}")
    print(f"Index 10: {sicherer_listen_zugriff(zahlen, 10, 'N/A')}")

    # Konvertierung
    print("\n=== Sichere Konvertierung ===")
    print(f"'42' -> {konvertiere_zu_int('42')}")
    print(f"'abc' -> {konvertiere_zu_int('abc')}")
    print(f"'3.14' -> {konvertiere_zu_int('3.14')}")  # Floats funktionieren nicht direkt

    # Finally
    demonstriere_finally()

    # Exception Info
    demonstriere_exception_info()

    # Email-Validierung
    print("\n=== Email-Validierung ===")
    emails = ["test@example.com", "invalid", "", "no-at-sign.com"]

    for email in emails:
        try:
            validiere_email(email)
            print(f"'{email}' ist gültig")
        except ValueError as e:
            print(f"'{email}' ist ungültig: {e}")

    # Interaktive Eingabe (auskommentiert für automatische Ausführung)
    # print("\n=== Sichere Eingabe ===")
    # zahl = sichere_zahl_eingabe("Geben Sie eine Zahl (1-10) ein: ", 1, 10)
    # print(f"Sie haben {zahl} eingegeben.")
