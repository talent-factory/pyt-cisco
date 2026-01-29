"""
Musterlösung Übung 4: Primzahlen (CISCO LAB 4.3.7)

Themen: Return-Werte, Schleifen, Algorithmen
"""

import math


# Aufgabe 4.1: Primzahl prüfen
def ist_primzahl(n: int) -> bool:
    """Prüft ob n eine Primzahl ist.

    Args:
        n: Die zu prüfende Zahl

    Returns:
        True wenn Primzahl, sonst False
    """
    # Sonderfälle
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Prüfe nur bis Wurzel von n
    grenze = int(math.sqrt(n)) + 1
    for i in range(3, grenze, 2):  # Nur ungerade Zahlen
        if n % i == 0:
            return False

    return True


# Aufgabe 4.2: Primzahlen bis n
def primzahlen_bis(n: int) -> list[int]:
    """Findet alle Primzahlen bis n.

    Args:
        n: Obergrenze

    Returns:
        Liste aller Primzahlen bis n
    """
    primzahlen = []
    for zahl in range(2, n + 1):
        if ist_primzahl(zahl):
            primzahlen.append(zahl)
    return primzahlen


# Aufgabe 4.3: Erste n Primzahlen
def erste_primzahlen(anzahl: int) -> list[int]:
    """Findet die ersten n Primzahlen.

    Args:
        anzahl: Anzahl gewünschter Primzahlen

    Returns:
        Liste der ersten n Primzahlen
    """
    primzahlen = []
    kandidat = 2

    while len(primzahlen) < anzahl:
        if ist_primzahl(kandidat):
            primzahlen.append(kandidat)
        kandidat += 1

    return primzahlen


# Aufgabe 4.4: Primfaktorzerlegung
def primfaktoren(n: int) -> list[int]:
    """Zerlegt n in Primfaktoren.

    Args:
        n: Die zu zerlegende Zahl

    Returns:
        Liste der Primfaktoren (mit Wiederholungen)
    """
    if n <= 1:
        return []

    faktoren = []

    # Durch 2 teilen solange möglich
    while n % 2 == 0:
        faktoren.append(2)
        n //= 2

    # Ungerade Faktoren prüfen
    faktor = 3
    while faktor * faktor <= n:
        while n % faktor == 0:
            faktoren.append(faktor)
            n //= faktor
        faktor += 2

    # Falls n noch > 1 ist, ist es selbst ein Primfaktor
    if n > 1:
        faktoren.append(n)

    return faktoren


# Bonus: Zwillingsprimzahlen
def zwillingsprimzahlen_bis(n: int) -> list[tuple[int, int]]:
    """Findet alle Zwillingsprimzahlen bis n.

    Zwillingsprimzahlen sind Paare (p, p+2) wo beide Primzahlen sind.

    Args:
        n: Obergrenze

    Returns:
        Liste von Tupeln (p, p+2)
    """
    zwillinge = []

    for p in range(2, n - 1):
        if ist_primzahl(p) and ist_primzahl(p + 2):
            zwillinge.append((p, p + 2))

    return zwillinge


# Sieb des Eratosthenes (effizienterer Algorithmus)
def sieb_eratosthenes(n: int) -> list[int]:
    """Findet alle Primzahlen bis n mit dem Sieb des Eratosthenes.

    Args:
        n: Obergrenze

    Returns:
        Liste aller Primzahlen bis n
    """
    if n < 2:
        return []

    # Initialisiere alle als potentielle Primzahlen
    ist_prim = [True] * (n + 1)
    ist_prim[0] = ist_prim[1] = False

    # Sieben
    for i in range(2, int(math.sqrt(n)) + 1):
        if ist_prim[i]:
            # Alle Vielfachen von i streichen
            for j in range(i * i, n + 1, i):
                ist_prim[j] = False

    # Primzahlen extrahieren
    return [i for i in range(n + 1) if ist_prim[i]]


# Tests
if __name__ == "__main__":
    print("=== Aufgabe 4.1: Primzahl prüfen ===")
    testzahlen = [2, 7, 10, 23, 1, 0, -5]
    for zahl in testzahlen:
        ergebnis = ist_primzahl(zahl)
        print(f"{zahl}: {'Primzahl' if ergebnis else 'Keine Primzahl'}")

    print("\n=== Aufgabe 4.2: Primzahlen bis n ===")
    print(f"Primzahlen bis 10: {primzahlen_bis(10)}")
    print(f"Primzahlen bis 20: {primzahlen_bis(20)}")
    print(f"Primzahlen bis 2: {primzahlen_bis(2)}")
    print(f"Primzahlen bis 1: {primzahlen_bis(1)}")

    print("\n=== Aufgabe 4.3: Erste n Primzahlen ===")
    print(f"Erste 5 Primzahlen: {erste_primzahlen(5)}")
    print(f"Erste 10 Primzahlen: {erste_primzahlen(10)}")
    print(f"Erste 1 Primzahl: {erste_primzahlen(1)}")

    print("\n=== Aufgabe 4.4: Primfaktorzerlegung ===")
    testzahlen = [12, 100, 17, 1]
    for zahl in testzahlen:
        faktoren = primfaktoren(zahl)
        print(f"{zahl} = {' × '.join(map(str, faktoren)) if faktoren else '[]'}")

    print("\n=== Bonus: Zwillingsprimzahlen ===")
    print(f"Zwillingsprimzahlen bis 50: {zwillingsprimzahlen_bis(50)}")

    print("\n=== Bonus: Sieb des Eratosthenes ===")
    print(f"Sieb bis 30: {sieb_eratosthenes(30)}")
