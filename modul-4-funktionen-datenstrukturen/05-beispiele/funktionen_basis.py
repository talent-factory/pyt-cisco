"""
Funktionen Basis - Modul 4

Dieses Modul demonstriert grundlegende Funktionskonzepte:
- Funktionen definieren mit def
- Funktionen aufrufen
- Docstrings schreiben
"""


def begruessung():
    """Gibt eine Begrüssung aus."""
    print("Willkommen zum Python-Kurs!")
    print("Heute lernen wir Funktionen.")


def zeige_trennlinie(zeichen: str = "-", laenge: int = 40):
    """Zeigt eine Trennlinie.

    Args:
        zeichen: Das Zeichen für die Linie (Standard: "-")
        laenge: Die Länge der Linie (Standard: 40)
    """
    print(zeichen * laenge)


def zeige_header(titel: str):
    """Zeigt einen formatierten Header.

    Args:
        titel: Der Titel für den Header
    """
    zeige_trennlinie("=")
    print(titel.upper())
    zeige_trennlinie("=")


def zeige_menu():
    """Zeigt ein einfaches Menü."""
    print("1. Option A")
    print("2. Option B")
    print("3. Option C")
    print("4. Beenden")


def zeige_footer():
    """Zeigt einen Footer."""
    zeige_trennlinie("-")
    print("© 2025 Python Kurs")


# Hauptprogramm
if __name__ == "__main__":
    # Funktionen aufrufen
    zeige_header("Mein Programm")
    print()
    begruessung()
    print()
    zeige_menu()
    zeige_footer()

    # Trennlinie mit verschiedenen Parametern
    print("\nVerschiedene Trennlinien:")
    zeige_trennlinie()
    zeige_trennlinie("*")
    zeige_trennlinie("=", 20)
    zeige_trennlinie(zeichen="#", laenge=15)
