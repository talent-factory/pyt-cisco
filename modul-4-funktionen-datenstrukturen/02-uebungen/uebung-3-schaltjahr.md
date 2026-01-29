# Übung 3: Schaltjahr (CISCO LAB 4.3.4)

**Schwierigkeit:** Mittel
**Thema:** Return-Werte, Bedingte Logik

## Hintergrund

Ein Schaltjahr hat 366 Tage statt 365. Die Regeln sind:
1. Durch 4 teilbar → Schaltjahr
2. ABER durch 100 teilbar → KEIN Schaltjahr
3. ABER durch 400 teilbar → DOCH Schaltjahr

## Aufgabe 3.1: Schaltjahr prüfen

```python
def ist_schaltjahr(jahr):
    """Prüft ob ein Jahr ein Schaltjahr ist.

    Args:
        jahr: Das zu prüfende Jahr (int)

    Returns:
        True wenn Schaltjahr, sonst False
    """
    # Ihr Code hier
    pass

# Tests
print(ist_schaltjahr(2024))  # True  (durch 4 teilbar)
print(ist_schaltjahr(2023))  # False (nicht durch 4 teilbar)
print(ist_schaltjahr(2000))  # True  (durch 400 teilbar)
print(ist_schaltjahr(1900))  # False (durch 100, aber nicht durch 400)
print(ist_schaltjahr(2100))  # False (durch 100, aber nicht durch 400)
```

## Aufgabe 3.2: Tage im Monat (CISCO LAB 4.3.5)

Erweitern Sie die Funktion um die Anzahl Tage pro Monat:

```python
def tage_im_monat(jahr, monat):
    """Gibt die Anzahl Tage eines Monats zurück.

    Args:
        jahr: Das Jahr (für Schaltjahr-Berechnung)
        monat: Der Monat (1-12)

    Returns:
        Anzahl Tage im Monat
    """
    # Tipp: Februar hat 28 oder 29 Tage
    # Tipp: April, Juni, September, November haben 30 Tage
    # Tipp: Rest hat 31 Tage
    # Ihr Code hier
    pass

# Tests
print(tage_im_monat(2024, 2))   # 29 (Schaltjahr)
print(tage_im_monat(2023, 2))   # 28
print(tage_im_monat(2024, 4))   # 30
print(tage_im_monat(2024, 12))  # 31
```

## Aufgabe 3.3: Tag des Jahres (CISCO LAB 4.3.6)

Berechnen Sie den Tag des Jahres:

```python
def tag_des_jahres(jahr, monat, tag):
    """Berechnet den wievielten Tag des Jahres ein Datum ist.

    Args:
        jahr: Das Jahr
        monat: Der Monat (1-12)
        tag: Der Tag (1-31)

    Returns:
        Tag des Jahres (1-366)
    """
    # Tipp: Nutzen Sie tage_im_monat()
    # Ihr Code hier
    pass

# Tests
print(tag_des_jahres(2024, 1, 1))    # 1
print(tag_des_jahres(2024, 1, 31))   # 31
print(tag_des_jahres(2024, 2, 29))   # 60 (31 + 29)
print(tag_des_jahres(2024, 12, 31))  # 366 (Schaltjahr)
print(tag_des_jahres(2023, 12, 31))  # 365
```

## Bonus: Datum validieren

```python
def ist_gueltig(jahr, monat, tag):
    """Prüft ob ein Datum gültig ist.

    Args:
        jahr: Das Jahr
        monat: Der Monat (1-12)
        tag: Der Tag

    Returns:
        True wenn gültig, sonst False
    """
    # Ihr Code hier
    pass

# Tests
print(ist_gueltig(2024, 2, 29))   # True (Schaltjahr)
print(ist_gueltig(2023, 2, 29))   # False (kein Schaltjahr)
print(ist_gueltig(2024, 4, 31))   # False (April hat 30 Tage)
print(ist_gueltig(2024, 13, 1))   # False (kein 13. Monat)
```

## Musterlösung

Versuchen Sie zuerst selbst zu lösen! Die Musterlösung finden Sie in [../05-beispiele/uebung_3_loesung.py](../05-beispiele/uebung_3_loesung.py)
