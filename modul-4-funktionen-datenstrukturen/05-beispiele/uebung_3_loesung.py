"""
Musterlösung Übung 3: Schaltjahr (CISCO LAB 4.3.4-4.3.6)

Themen: Return-Werte, Bedingte Logik
"""


# Aufgabe 3.1: Schaltjahr prüfen
def ist_schaltjahr(jahr: int) -> bool:
    """Prüft ob ein Jahr ein Schaltjahr ist.

    Regeln:
    1. Durch 4 teilbar → Schaltjahr
    2. ABER durch 100 teilbar → KEIN Schaltjahr
    3. ABER durch 400 teilbar → DOCH Schaltjahr

    Args:
        jahr: Das zu prüfende Jahr (int)

    Returns:
        True wenn Schaltjahr, sonst False
    """
    if jahr % 400 == 0:
        return True
    if jahr % 100 == 0:
        return False
    if jahr % 4 == 0:
        return True
    return False


# Alternative kompakte Variante:
def ist_schaltjahr_kompakt(jahr: int) -> bool:
    """Kompakte Variante der Schaltjahr-Prüfung."""
    return (jahr % 4 == 0 and jahr % 100 != 0) or (jahr % 400 == 0)


# Aufgabe 3.2: Tage im Monat
def tage_im_monat(jahr: int, monat: int) -> int:
    """Gibt die Anzahl Tage eines Monats zurück.

    Args:
        jahr: Das Jahr (für Schaltjahr-Berechnung)
        monat: Der Monat (1-12)

    Returns:
        Anzahl Tage im Monat, oder 0 bei ungültigem Monat
    """
    if monat < 1 or monat > 12:
        return 0

    # Monate mit 31 Tagen
    if monat in [1, 3, 5, 7, 8, 10, 12]:
        return 31

    # Monate mit 30 Tagen
    if monat in [4, 6, 9, 11]:
        return 30

    # Februar
    if ist_schaltjahr(jahr):
        return 29
    return 28


# Aufgabe 3.3: Tag des Jahres
def tag_des_jahres(jahr: int, monat: int, tag: int) -> int:
    """Berechnet den wievielten Tag des Jahres ein Datum ist.

    Args:
        jahr: Das Jahr
        monat: Der Monat (1-12)
        tag: Der Tag (1-31)

    Returns:
        Tag des Jahres (1-366), oder 0 bei ungültigem Datum
    """
    # Validierung
    if not ist_gueltig(jahr, monat, tag):
        return 0

    # Tage aller vorherigen Monate summieren
    tage = 0
    for m in range(1, monat):
        tage += tage_im_monat(jahr, m)

    # Tag des aktuellen Monats addieren
    tage += tag

    return tage


# Bonus: Datum validieren
def ist_gueltig(jahr: int, monat: int, tag: int) -> bool:
    """Prüft ob ein Datum gültig ist.

    Args:
        jahr: Das Jahr
        monat: Der Monat (1-12)
        tag: Der Tag

    Returns:
        True wenn gültig, sonst False
    """
    # Monat prüfen
    if monat < 1 or monat > 12:
        return False

    # Tag prüfen
    if tag < 1:
        return False

    max_tage = tage_im_monat(jahr, monat)
    if tag > max_tage:
        return False

    return True


# Tests
if __name__ == "__main__":
    print("=== Aufgabe 3.1: Schaltjahr ===")
    testjahre = [2024, 2023, 2000, 1900, 2100]
    for jahr in testjahre:
        ergebnis = ist_schaltjahr(jahr)
        print(f"{jahr}: {'Schaltjahr' if ergebnis else 'Kein Schaltjahr'}")

    print("\n=== Aufgabe 3.2: Tage im Monat ===")
    testfaelle = [(2024, 2), (2023, 2), (2024, 4), (2024, 12)]
    for jahr, monat in testfaelle:
        tage = tage_im_monat(jahr, monat)
        print(f"{monat}/{jahr}: {tage} Tage")

    print("\n=== Aufgabe 3.3: Tag des Jahres ===")
    testdaten = [
        (2024, 1, 1),
        (2024, 1, 31),
        (2024, 2, 29),
        (2024, 12, 31),
        (2023, 12, 31),
    ]
    for jahr, monat, tag in testdaten:
        tag_nr = tag_des_jahres(jahr, monat, tag)
        print(f"{tag}.{monat}.{jahr}: Tag {tag_nr}")

    print("\n=== Bonus: Datum validieren ===")
    validierdaten = [
        (2024, 2, 29),
        (2023, 2, 29),
        (2024, 4, 31),
        (2024, 13, 1),
    ]
    for jahr, monat, tag in validierdaten:
        gueltig = ist_gueltig(jahr, monat, tag)
        print(f"{tag}.{monat}.{jahr}: {'Gültig' if gueltig else 'Ungültig'}")
