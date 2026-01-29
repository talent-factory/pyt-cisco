"""
Parameter-Varianten - Modul 4

Dieses Modul demonstriert verschiedene Parameter-Typen:
- Positional Arguments
- Keyword Arguments
- Default Values
- Mixing
"""


def gruesse(name: str, gruss: str = "Hallo"):
    """Begrüsst eine Person.

    Args:
        name: Name der Person
        gruss: Begrüssung (Standard: "Hallo")
    """
    print(f"{gruss}, {name}!")


def zeige_info(name: str, alter: int, stadt: str = "Unbekannt"):
    """Zeigt Informationen über eine Person.

    Args:
        name: Name der Person
        alter: Alter in Jahren
        stadt: Wohnort (Standard: "Unbekannt")
    """
    print(f"Name: {name}")
    print(f"Alter: {alter} Jahre")
    print(f"Stadt: {stadt}")
    print("-" * 30)


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
    preis_nach_rabatt = grundpreis * (1 - rabatt_prozent / 100)
    endpreis = preis_nach_rabatt * (1 + mwst_prozent / 100)
    return endpreis


def formatiere_preis(betrag: float, waehrung: str = "CHF") -> str:
    """Formatiert einen Preis mit Währung.

    Args:
        betrag: Der Betrag
        waehrung: Währungscode (Standard: "CHF")

    Returns:
        Formatierter Preis als String
    """
    return f"{betrag:.2f} {waehrung}"


# Hauptprogramm
if __name__ == "__main__":
    print("=== Positional Arguments ===")
    gruesse("Anna", "Hallo")
    gruesse("Max", "Guten Tag")

    print("\n=== Keyword Arguments ===")
    gruesse(name="Lisa", gruss="Hi")
    gruesse(gruss="Servus", name="Tom")

    print("\n=== Default Values ===")
    gruesse("Peter")  # Verwendet Default "Hallo"

    print("\n=== Mixing ===")
    gruesse("Sara", gruss="Willkommen")

    print("\n=== Informationen ===")
    zeige_info("Anna", 25, "Zürich")
    zeige_info("Max", 30)  # Stadt = "Unbekannt"
    zeige_info(alter=22, name="Lisa", stadt="Bern")

    print("\n=== Preisberechnung ===")
    preis1 = berechne_preis(100)
    print(f"100 CHF ohne Rabatt: {formatiere_preis(preis1)}")

    preis2 = berechne_preis(100, rabatt_prozent=10)
    print(f"100 CHF mit 10% Rabatt: {formatiere_preis(preis2)}")

    preis3 = berechne_preis(100, 20, 8.1)
    print(f"100 CHF mit 20% Rabatt, 8.1% MwSt: {formatiere_preis(preis3)}")
