"""
Musterlösung Übung 8: Datenverarbeitung (CISCO LAB 4.3.8)

Themen: Kombination aller Konzepte
"""


# Aufgabe 8.1: Kraftstoffverbrauch (CISCO LAB 4.3.8)
def liter_pro_100km_zu_mpg(l_pro_100km: float) -> float:
    """Konvertiert l/100km zu Miles per Gallon (US).

    Formeln:
    - 1 Meile = 1.609344 km
    - 1 US Gallone = 3.785411784 Liter
    - mpg = 235.215 / l_pro_100km

    Args:
        l_pro_100km: Verbrauch in Liter pro 100km

    Returns:
        Verbrauch in Miles per Gallon
    """
    if l_pro_100km <= 0:
        return 0.0
    return 235.215 / l_pro_100km


def mpg_zu_liter_pro_100km(mpg: float) -> float:
    """Konvertiert Miles per Gallon zu l/100km.

    Args:
        mpg: Verbrauch in Miles per Gallon

    Returns:
        Verbrauch in Liter pro 100km
    """
    if mpg <= 0:
        return 0.0
    return 235.215 / mpg


# Aufgabe 8.2: Notenstatistik
def notensystem():
    """Komplettes Notenverwaltungssystem."""

    daten: dict[str, dict[str, list[float]]] = {}

    def note_hinzufuegen(student: str, fach: str, note: float) -> bool:
        """Fügt eine Note hinzu."""
        if note < 1.0 or note > 6.0:
            print(f"Ungültige Note: {note}")
            return False

        if student not in daten:
            daten[student] = {}
        if fach not in daten[student]:
            daten[student][fach] = []

        daten[student][fach].append(note)
        return True

    def durchschnitt_student(student: str) -> float | None:
        """Berechnet Durchschnitt eines Studenten."""
        if student not in daten:
            return None

        alle_noten = []
        for noten in daten[student].values():
            alle_noten.extend(noten)

        if alle_noten:
            return sum(alle_noten) / len(alle_noten)
        return None

    def durchschnitt_fach(fach: str) -> float | None:
        """Berechnet Durchschnitt eines Fachs."""
        alle_noten = []
        for student_daten in daten.values():
            if fach in student_daten:
                alle_noten.extend(student_daten[fach])

        if alle_noten:
            return sum(alle_noten) / len(alle_noten)
        return None

    def beste_note(fach: str) -> tuple[float, str] | None:
        """Findet die beste Note in einem Fach."""
        beste = None
        bester_student = None

        for student, faecher in daten.items():
            if fach in faecher and faecher[fach]:
                max_note = max(faecher[fach])
                if beste is None or max_note > beste:
                    beste = max_note
                    bester_student = student

        if beste:
            return (beste, bester_student)
        return None

    def bericht_erstellen():
        """Erstellt einen vollständigen Bericht."""
        print("\n" + "=" * 50)
        print("NOTENBERICHT")
        print("=" * 50)

        for student, faecher in sorted(daten.items()):
            print(f"\n{student}:")
            for fach, noten in sorted(faecher.items()):
                avg = sum(noten) / len(noten) if noten else 0
                print(f"  {fach}: {noten} (Ø {avg:.2f})")

            gesamt = durchschnitt_student(student)
            if gesamt:
                print(f"  → Gesamtdurchschnitt: {gesamt:.2f}")

    # Tests
    note_hinzufuegen("Anna", "Mathe", 5.5)
    note_hinzufuegen("Anna", "Deutsch", 5.0)
    note_hinzufuegen("Max", "Mathe", 4.5)
    note_hinzufuegen("Max", "Deutsch", 5.5)
    note_hinzufuegen("Lisa", "Mathe", 6.0)
    note_hinzufuegen("Lisa", "Deutsch", 5.0)

    print(f"Anna Durchschnitt: {durchschnitt_student('Anna'):.2f}")
    print(f"Mathe Durchschnitt: {durchschnitt_fach('Mathe'):.2f}")
    print(f"Beste Note Mathe: {beste_note('Mathe')}")
    bericht_erstellen()


# Aufgabe 8.3: Textanalyse
def analysiere_text(text: str) -> dict:
    """Führt eine umfassende Textanalyse durch.

    Returns:
        Dictionary mit:
        - anzahl_woerter
        - anzahl_saetze
        - anzahl_zeichen
        - durchschnitt_wortlaenge
        - haeufigste_woerter (Top 5)
        - laengstes_wort
    """
    # Bereinigung
    text = text.strip()

    # Zeichen zählen (ohne Leerzeichen)
    anzahl_zeichen = len(text.replace(" ", "").replace("\n", ""))

    # Sätze zählen (. ! ?)
    anzahl_saetze = sum(1 for char in text if char in ".!?")
    if anzahl_saetze == 0:
        anzahl_saetze = 1

    # Wörter extrahieren
    woerter = []
    for wort in text.lower().split():
        wort = wort.strip(".,!?;:\"'()-")
        if wort:
            woerter.append(wort)

    anzahl_woerter = len(woerter)

    # Durchschnittliche Wortlänge
    if woerter:
        durchschnitt_wortlaenge = sum(len(w) for w in woerter) / len(woerter)
    else:
        durchschnitt_wortlaenge = 0

    # Häufigste Wörter
    zaehler: dict[str, int] = {}
    for wort in woerter:
        zaehler[wort] = zaehler.get(wort, 0) + 1

    sortiert = sorted(zaehler.items(), key=lambda x: -x[1])
    haeufigste_woerter = sortiert[:5]

    # Längstes Wort
    laengstes_wort = max(woerter, key=len) if woerter else ""

    return {
        "anzahl_woerter": anzahl_woerter,
        "anzahl_saetze": anzahl_saetze,
        "anzahl_zeichen": anzahl_zeichen,
        "durchschnitt_wortlaenge": round(durchschnitt_wortlaenge, 2),
        "haeufigste_woerter": haeufigste_woerter,
        "laengstes_wort": laengstes_wort,
    }


# Aufgabe 8.4: Bankkonten-Simulation
def bank_simulation():
    """Einfache Bankkonten-Simulation."""

    konten: dict[str, dict] = {}

    def konto_erstellen(kontonummer: str, inhaber: str, startguthaben: float = 0) -> bool:
        """Erstellt ein neues Konto."""
        if kontonummer in konten:
            print(f"Konto {kontonummer} existiert bereits.")
            return False

        konten[kontonummer] = {"inhaber": inhaber, "saldo": startguthaben, "transaktionen": []}
        print(f"✓ Konto {kontonummer} für {inhaber} erstellt.")
        return True

    def einzahlen(kontonummer: str, betrag: float) -> bool:
        """Zahlt einen Betrag ein."""
        if kontonummer not in konten:
            print(f"Konto {kontonummer} nicht gefunden.")
            return False

        if betrag <= 0:
            print("Betrag muss positiv sein.")
            return False

        konten[kontonummer]["saldo"] += betrag
        konten[kontonummer]["transaktionen"].append(f"+{betrag:.2f}")
        print(f"✓ {betrag:.2f} CHF eingezahlt.")
        return True

    def abheben(kontonummer: str, betrag: float) -> bool:
        """Hebt einen Betrag ab."""
        if kontonummer not in konten:
            print(f"Konto {kontonummer} nicht gefunden.")
            return False

        if betrag <= 0:
            print("Betrag muss positiv sein.")
            return False

        if konten[kontonummer]["saldo"] < betrag:
            print("Nicht genügend Guthaben.")
            return False

        konten[kontonummer]["saldo"] -= betrag
        konten[kontonummer]["transaktionen"].append(f"-{betrag:.2f}")
        print(f"✓ {betrag:.2f} CHF abgehoben.")
        return True

    def ueberweisen(von_konto: str, nach_konto: str, betrag: float) -> bool:
        """Überweist von einem Konto auf ein anderes."""
        if von_konto not in konten:
            print(f"Konto {von_konto} nicht gefunden.")
            return False

        if nach_konto not in konten:
            print(f"Konto {nach_konto} nicht gefunden.")
            return False

        if konten[von_konto]["saldo"] < betrag:
            print("Nicht genügend Guthaben.")
            return False

        konten[von_konto]["saldo"] -= betrag
        konten[nach_konto]["saldo"] += betrag
        konten[von_konto]["transaktionen"].append(f"-{betrag:.2f} → {nach_konto}")
        konten[nach_konto]["transaktionen"].append(f"+{betrag:.2f} ← {von_konto}")
        print(f"✓ {betrag:.2f} CHF überwiesen.")
        return True

    def kontoauszug(kontonummer: str):
        """Zeigt den Kontostand."""
        if kontonummer not in konten:
            print(f"Konto {kontonummer} nicht gefunden.")
            return

        konto = konten[kontonummer]
        print(f"\n--- Kontoauszug {kontonummer} ---")
        print(f"Inhaber: {konto['inhaber']}")
        print(f"Saldo: {konto['saldo']:.2f} CHF")
        if konto["transaktionen"]:
            print("Letzte Transaktionen:")
            for t in konto["transaktionen"][-5:]:
                print(f"  {t}")

    def alle_konten():
        """Zeigt alle Konten."""
        print("\n--- Alle Konten ---")
        for nr, konto in konten.items():
            print(f"{nr}: {konto['inhaber']} - {konto['saldo']:.2f} CHF")

    # Tests
    konto_erstellen("CH001", "Anna Müller", 1000)
    konto_erstellen("CH002", "Max Weber", 500)

    einzahlen("CH001", 200)
    abheben("CH002", 100)
    ueberweisen("CH001", "CH002", 300)

    alle_konten()
    kontoauszug("CH001")


# Bonus: Datenvalidierung
def validiere_person(daten: dict) -> tuple[bool, list[str] | None]:
    """Validiert Personendaten.

    Erwartete Struktur:
    {
        "name": str (nicht leer),
        "alter": int (0-150),
        "email": str (enthält @),
        "telefon": str (optional)
    }

    Returns:
        (True, None) wenn gültig
        (False, [Fehlermeldungen]) wenn ungültig
    """
    fehler = []

    # Name prüfen
    name = daten.get("name", "")
    if not name or not isinstance(name, str):
        fehler.append("Name darf nicht leer sein")

    # Alter prüfen
    alter = daten.get("alter")
    if alter is None:
        fehler.append("Alter ist erforderlich")
    elif not isinstance(alter, int):
        fehler.append("Alter muss eine Ganzzahl sein")
    elif alter < 0 or alter > 150:
        fehler.append("Alter muss zwischen 0 und 150 sein")

    # Email prüfen
    email = daten.get("email", "")
    if not email:
        fehler.append("Email ist erforderlich")
    elif "@" not in email:
        fehler.append("Email muss @ enthalten")

    if fehler:
        return (False, fehler)
    return (True, None)


# Tests
if __name__ == "__main__":
    print("=== Aufgabe 8.1: Kraftstoffverbrauch ===")
    print(f"7.5 l/100km = {liter_pro_100km_zu_mpg(7.5):.1f} mpg")
    print(f"30 mpg = {mpg_zu_liter_pro_100km(30):.1f} l/100km")

    print("\n=== Aufgabe 8.2: Notensystem ===")
    notensystem()

    print("\n=== Aufgabe 8.3: Textanalyse ===")
    text = """
    Python ist eine grossartige Programmiersprache. Sie ist einfach zu lernen
    und sehr mächtig. Viele Unternehmen nutzen Python für Datenanalyse,
    Webentwicklung und künstliche Intelligenz. Python hat eine grosse
    Community und viele hilfreiche Bibliotheken.
    """
    ergebnis = analysiere_text(text)
    for key, value in ergebnis.items():
        print(f"{key}: {value}")

    print("\n=== Aufgabe 8.4: Bankkonten ===")
    bank_simulation()

    print("\n=== Bonus: Validierung ===")
    testdaten = [
        {"name": "Anna", "alter": 25, "email": "anna@mail.ch"},
        {"name": "", "alter": 200, "email": "invalid"},
    ]
    for daten in testdaten:
        gueltig, fehler = validiere_person(daten)
        print(f"{daten}")
        if gueltig:
            print("  → Gültig")
        else:
            print(f"  → Ungültig: {fehler}")
