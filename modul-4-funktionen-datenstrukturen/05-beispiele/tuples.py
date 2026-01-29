"""
Tuple-Operationen - Modul 4

Dieses Modul demonstriert Tuple-Operationen:
- Erstellen
- Zugriff und Unpacking
- Verwendung als Return-Wert
- Vergleich mit Listen
"""


def berechne_distanz(punkt1: tuple[float, float], punkt2: tuple[float, float]) -> float:
    """Berechnet die Distanz zwischen zwei Punkten.

    Args:
        punkt1: Tuple (x, y) des ersten Punkts
        punkt2: Tuple (x, y) des zweiten Punkts

    Returns:
        Euklidische Distanz
    """
    x1, y1 = punkt1  # Tuple Unpacking
    x2, y2 = punkt2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def rgb_zu_hex(rgb: tuple[int, int, int]) -> str:
    """Konvertiert RGB zu Hex-Farbcode.

    Args:
        rgb: Tuple (r, g, b) mit Werten 0-255

    Returns:
        Hex-Farbcode als String
    """
    r, g, b = rgb
    return f"#{r:02x}{g:02x}{b:02x}"


def get_min_max(zahlen: list[float]) -> tuple[float, float]:
    """Gibt Minimum und Maximum einer Liste zurück.

    Args:
        zahlen: Liste von Zahlen

    Returns:
        Tuple (minimum, maximum)
    """
    if not zahlen:
        return (0, 0)
    return (min(zahlen), max(zahlen))


def get_statistics(zahlen: list[float]) -> tuple[float, float, float, int]:
    """Berechnet Statistiken für eine Zahlenliste.

    Args:
        zahlen: Liste von Zahlen

    Returns:
        Tuple (minimum, maximum, durchschnitt, anzahl)
    """
    if not zahlen:
        return (0, 0, 0, 0)

    return (min(zahlen), max(zahlen), sum(zahlen) / len(zahlen), len(zahlen))


def tausche(a, b) -> tuple:
    """Tauscht zwei Werte.

    Args:
        a: Erster Wert
        b: Zweiter Wert

    Returns:
        Tuple (b, a)
    """
    return b, a


# Hauptprogramm
if __name__ == "__main__":
    # Tuple erstellen
    print("=== Tuple Erstellen ===")
    punkt = (10, 20)
    farbe = (255, 128, 0)  # Orange
    person = ("Anna", 25, "Zürich")
    einzelwert = (42,)  # Beachte das Komma!

    print(f"Punkt: {punkt}")
    print(f"Farbe RGB: {farbe}")
    print(f"Person: {person}")
    print(f"Einzelwert: {einzelwert}, Typ: {type(einzelwert)}")

    # Zugriff
    print("\n=== Zugriff ===")
    print(f"punkt[0]: {punkt[0]}")
    print(f"person[1]: {person[1]}")
    print(f"farbe[-1]: {farbe[-1]}")

    # Unpacking
    print("\n=== Unpacking ===")
    x, y = punkt
    print(f"x={x}, y={y}")

    name, alter, stadt = person
    print(f"Name: {name}, Alter: {alter}, Stadt: {stadt}")

    # Unveränderbar
    print("\n=== Unveränderbar ===")
    print(f"Tuple: {punkt}")
    # punkt[0] = 15  # TypeError!
    print("Tuples können nicht verändert werden!")

    # Distanz berechnen
    print("\n=== Distanz ===")
    p1 = (0, 0)
    p2 = (3, 4)
    distanz = berechne_distanz(p1, p2)
    print(f"Distanz von {p1} zu {p2}: {distanz}")

    # RGB zu Hex
    print("\n=== RGB zu Hex ===")
    farben = [
        ((255, 0, 0), "Rot"),
        ((0, 255, 0), "Grün"),
        ((0, 0, 255), "Blau"),
        ((255, 128, 0), "Orange"),
    ]
    for rgb, name in farben:
        print(f"{name}: RGB{rgb} = {rgb_zu_hex(rgb)}")

    # Mehrere Rückgabewerte
    print("\n=== Mehrere Rückgabewerte ===")
    zahlen = [5, 2, 8, 1, 9, 3]
    minimum, maximum = get_min_max(zahlen)
    print(f"Zahlen: {zahlen}")
    print(f"Min: {minimum}, Max: {maximum}")

    min_val, max_val, avg, count = get_statistics(zahlen)
    print(f"Statistik: Min={min_val}, Max={max_val}, Avg={avg:.2f}, N={count}")

    # Werte tauschen
    print("\n=== Werte Tauschen ===")
    a, b = 10, 20
    print(f"Vorher: a={a}, b={b}")
    a, b = tausche(a, b)
    print(f"Nachher: a={a}, b={b}")

    # Tuple als Dictionary-Key
    print("\n=== Tuple als Dict-Key ===")
    koordinaten_namen = {
        (0, 0): "Ursprung",
        (1, 0): "Rechts",
        (0, 1): "Oben",
    }
    print(f"Position (0, 0): {koordinaten_namen[(0, 0)]}")
