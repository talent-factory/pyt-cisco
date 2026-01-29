"""
Rekursion - Modul 4

Dieses Modul demonstriert rekursive Funktionen:
- Fakultät
- Fibonacci
- Summe
- Countdown
"""


def fakultaet(n: int) -> int:
    """Berechnet n! rekursiv.

    Args:
        n: Eine nicht-negative ganze Zahl

    Returns:
        n! = n * (n-1) * ... * 1
    """
    if n <= 1:  # Basisfall
        return 1
    return n * fakultaet(n - 1)  # Rekursiver Aufruf


def fakultaet_iterativ(n: int) -> int:
    """Berechnet n! iterativ (zum Vergleich).

    Args:
        n: Eine nicht-negative ganze Zahl

    Returns:
        n!
    """
    ergebnis = 1
    for i in range(2, n + 1):
        ergebnis *= i
    return ergebnis


def fibonacci(n: int) -> int:
    """Berechnet die n-te Fibonacci-Zahl rekursiv.

    Args:
        n: Index der Fibonacci-Zahl (0, 1, 2, ...)

    Returns:
        F(n) = F(n-1) + F(n-2)
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_iterativ(n: int) -> int:
    """Berechnet die n-te Fibonacci-Zahl iterativ (effizienter).

    Args:
        n: Index der Fibonacci-Zahl

    Returns:
        F(n)
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def summe_bis(n: int) -> int:
    """Berechnet 1 + 2 + ... + n rekursiv.

    Args:
        n: Obergrenze

    Returns:
        Summe von 1 bis n
    """
    if n <= 0:
        return 0
    return n + summe_bis(n - 1)


def countdown(n: int):
    """Zeigt einen Countdown von n bis 0.

    Args:
        n: Startwert
    """
    if n < 0:
        print("Start!")
        return
    print(n)
    countdown(n - 1)


def potenz(basis: float, exponent: int) -> float:
    """Berechnet basis^exponent rekursiv.

    Args:
        basis: Die Basis
        exponent: Der Exponent (nicht-negativ)

    Returns:
        basis hoch exponent
    """
    if exponent == 0:
        return 1
    return basis * potenz(basis, exponent - 1)


def ggt(a: int, b: int) -> int:
    """Berechnet den grössten gemeinsamen Teiler (Euklid).

    Args:
        a: Erste Zahl
        b: Zweite Zahl

    Returns:
        GGT von a und b
    """
    if b == 0:
        return a
    return ggt(b, a % b)


# Hauptprogramm
if __name__ == "__main__":
    # Fakultät
    print("=== Fakultät ===")
    for i in range(6):
        print(f"{i}! = {fakultaet(i)}")

    # Fibonacci
    print("\n=== Fibonacci ===")
    print("F(n):", end=" ")
    for i in range(12):
        print(fibonacci_iterativ(i), end=" ")
    print()

    # Summe
    print("\n=== Summe 1 bis n ===")
    for n in [5, 10, 100]:
        print(f"1+2+...+{n} = {summe_bis(n)}")

    # Countdown
    print("\n=== Countdown ===")
    countdown(5)

    # Potenz
    print("\n=== Potenz ===")
    print(f"2^10 = {potenz(2, 10)}")
    print(f"3^4 = {potenz(3, 4)}")

    # GGT
    print("\n=== Grösster gemeinsamer Teiler ===")
    print(f"GGT(48, 18) = {ggt(48, 18)}")
    print(f"GGT(100, 35) = {ggt(100, 35)}")
