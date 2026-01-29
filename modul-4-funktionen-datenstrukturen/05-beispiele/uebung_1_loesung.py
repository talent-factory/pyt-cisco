"""
Musterlösung Übung 1: Funktionen Basis

Themen: def, Parameter, Default-Werte
"""


# Aufgabe 1.1: Trennlinie
def trennlinie(zeichen: str = "-", laenge: int = 40):
    """Gibt eine Trennlinie aus.

    Args:
        zeichen: Das Zeichen für die Linie (Standard: "-")
        laenge: Die Länge der Linie (Standard: 40)
    """
    print(zeichen * laenge)


# Aufgabe 1.2: Box zeichnen
def zeichne_box(breite: int = 10, hoehe: int = 5, zeichen: str = "*"):
    """Zeichnet eine Box aus Zeichen.

    Args:
        breite: Breite der Box
        hoehe: Höhe der Box
        zeichen: Zeichen für die Box
    """
    # Obere Kante
    print(zeichen * breite)

    # Mittlere Zeilen (mit Leerzeichen innen)
    for _ in range(hoehe - 2):
        if breite > 2:
            print(zeichen + " " * (breite - 2) + zeichen)
        else:
            print(zeichen * breite)

    # Untere Kante (nur wenn Höhe > 1)
    if hoehe > 1:
        print(zeichen * breite)


# Aufgabe 1.3: Begrüssungstext
def begruessung(name: str, sprache: str = "de"):
    """Begrüsst eine Person in verschiedenen Sprachen.

    Args:
        name: Name der Person
        sprache: Sprachcode (de, en, fr, it)
    """
    gruesse = {
        "de": "Hallo",
        "en": "Hello",
        "fr": "Bonjour",
        "it": "Ciao",
    }

    # Sprache normalisieren (lowercase)
    sprache = sprache.lower()

    # Gruss holen oder Standard verwenden
    gruss = gruesse.get(sprache, "Hallo")

    print(f"{gruss} {name}!")


# Tests
if __name__ == "__main__":
    print("=== Aufgabe 1.1: Trennlinie ===")
    trennlinie()
    trennlinie("*")
    trennlinie("=", 20)
    trennlinie("#", 10)

    print("\n=== Aufgabe 1.2: Box zeichnen ===")
    zeichne_box()
    print()
    zeichne_box(5, 3, "#")

    print("\n=== Aufgabe 1.3: Begrüssung ===")
    begruessung("Anna")
    begruessung("Max", "en")
    begruessung("Pierre", "fr")
    begruessung("Marco", "it")
    begruessung("Lisa", sprache="de")
