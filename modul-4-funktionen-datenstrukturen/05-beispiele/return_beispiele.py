"""
Return-Werte - Modul 4

Dieses Modul demonstriert Return-Werte:
- Einzelne Rückgabewerte
- Mehrere Rückgabewerte (Tuple)
- None als Rückgabewert
- Funktionen kombinieren
"""


def quadrat(x: float) -> float:
    """Berechnet das Quadrat einer Zahl.

    Args:
        x: Die Zahl

    Returns:
        x zum Quadrat
    """
    return x * x


def berechne_rechteck(laenge: float, breite: float) -> tuple[float, float]:
    """Berechnet Fläche und Umfang eines Rechtecks.

    Args:
        laenge: Länge des Rechtecks
        breite: Breite des Rechtecks

    Returns:
        Tuple mit (Fläche, Umfang)
    """
    flaeche = laenge * breite
    umfang = 2 * (laenge + breite)
    return flaeche, umfang


def statistik(zahlen: list[float]) -> tuple[float, float, float]:
    """Berechnet Statistiken für eine Zahlenliste.

    Args:
        zahlen: Liste von Zahlen

    Returns:
        Tuple mit (Minimum, Maximum, Durchschnitt)
    """
    if not zahlen:
        return 0, 0, 0

    minimum = min(zahlen)
    maximum = max(zahlen)
    durchschnitt = sum(zahlen) / len(zahlen)
    return minimum, maximum, durchschnitt


def finde_element(liste: list, gesucht) -> int | None:
    """Findet den Index eines Elements.

    Args:
        liste: Die zu durchsuchende Liste
        gesucht: Das gesuchte Element

    Returns:
        Index des Elements oder None wenn nicht gefunden
    """
    for i, element in enumerate(liste):
        if element == gesucht:
            return i
    return None


def ist_gerade(zahl: int) -> bool:
    """Prüft ob eine Zahl gerade ist.

    Args:
        zahl: Die zu prüfende Zahl

    Returns:
        True wenn gerade, sonst False
    """
    return zahl % 2 == 0


def zaehle_gerade(zahlen: list[int]) -> int:
    """Zählt gerade Zahlen in einer Liste.

    Args:
        zahlen: Liste von Zahlen

    Returns:
        Anzahl gerader Zahlen
    """
    anzahl = 0
    for zahl in zahlen:
        if ist_gerade(zahl):
            anzahl += 1
    return anzahl


def berechne_bmi(gewicht: float, groesse: float) -> float:
    """Berechnet den Body-Mass-Index.

    Args:
        gewicht: Gewicht in kg
        groesse: Grösse in m

    Returns:
        BMI-Wert
    """
    return gewicht / (groesse**2)


def bewerte_bmi(bmi: float) -> str:
    """Bewertet den BMI.

    Args:
        bmi: BMI-Wert

    Returns:
        Bewertung als String
    """
    if bmi < 18.5:
        return "Untergewicht"
    elif bmi < 25:
        return "Normalgewicht"
    elif bmi < 30:
        return "Übergewicht"
    else:
        return "Adipositas"


# Hauptprogramm
if __name__ == "__main__":
    # Einzelner Return-Wert
    print("=== Einzelner Return-Wert ===")
    ergebnis = quadrat(5)
    print(f"5² = {ergebnis}")

    # Mehrere Return-Werte
    print("\n=== Mehrere Return-Werte ===")
    flaeche, umfang = berechne_rechteck(5, 3)
    print(f"Rechteck 5x3: Fläche={flaeche}, Umfang={umfang}")

    # Statistik
    print("\n=== Statistik ===")
    zahlen = [1, 5, 3, 8, 2, 9, 4]
    min_val, max_val, avg = statistik(zahlen)
    print(f"Zahlen: {zahlen}")
    print(f"Min: {min_val}, Max: {max_val}, Durchschnitt: {avg:.2f}")

    # None als Return
    print("\n=== None als Return ===")
    index = finde_element([1, 2, 3, 4, 5], 3)
    print(f"Index von 3: {index}")

    index = finde_element([1, 2, 3, 4, 5], 10)
    if index is None:
        print("Element 10 nicht gefunden")

    # Funktionen kombinieren
    print("\n=== Funktionen kombinieren ===")
    zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    gerade = zaehle_gerade(zahlen)
    print(f"Gerade Zahlen in {zahlen}: {gerade}")

    # BMI-Rechner
    print("\n=== BMI-Rechner ===")
    gewicht, groesse = 75, 1.80
    bmi = berechne_bmi(gewicht, groesse)
    bewertung = bewerte_bmi(bmi)
    print(f"Gewicht: {gewicht}kg, Grösse: {groesse}m")
    print(f"BMI: {bmi:.1f} - {bewertung}")
