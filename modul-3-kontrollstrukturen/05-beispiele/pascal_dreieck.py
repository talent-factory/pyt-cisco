"""
Pascal'sches Dreieck
Berechnet und zeigt das Pascal'sche Dreieck an.

WICHTIG: Dieses Beispiel verwendet KEINE Funktionen,
da diese erst in Modul 4 behandelt werden.

Konzepte:
- Verschachtelte Listen (Liste von Listen)
- Verschachtelte Schleifen
- Zugriff auf vorherige Elemente
- String-Formatierung und Zentrierung
"""

print("=" * 50)
print("         PASCAL'SCHES DREIECK")
print("=" * 50)

# === EINGABE MIT VALIDIERUNG ===

while True:
    eingabe = input("\nAnzahl Zeilen (1-15): ")

    # Prüfen ob Eingabe eine Zahl ist
    if not eingabe.isdigit():
        print("❌ Bitte eine gültige Zahl eingeben!")
        continue

    anzahl_zeilen = int(eingabe)

    # Prüfen ob im gültigen Bereich
    if anzahl_zeilen < 1 or anzahl_zeilen > 15:
        print("❌ Bitte eine Zahl zwischen 1 und 15 eingeben!")
        continue

    # Gültige Eingabe
    break

# === BERECHNUNG DES DREIECKS ===

# Das Dreieck wird als Liste von Listen gespeichert
# Jede innere Liste ist eine Zeile
dreieck = []

for zeile_nr in range(anzahl_zeilen):
    # Neue Zeile erstellen
    neue_zeile = []

    for position in range(zeile_nr + 1):
        # Erste und letzte Position sind immer 1
        if position == 0 or position == zeile_nr:
            wert = 1
        else:
            # Summe der zwei Zahlen darüber
            vorherige_zeile = dreieck[zeile_nr - 1]
            wert = vorherige_zeile[position - 1] + vorherige_zeile[position]

        neue_zeile.append(wert)

    # Zeile zum Dreieck hinzufügen
    dreieck.append(neue_zeile)

# === AUSGABE ===

print()

# Breite für Zentrierung berechnen
# Basierend auf der breitesten Zeile (letzte Zeile)
letzte_zeile_str = ""
for zahl in dreieck[-1]:
    letzte_zeile_str += str(zahl) + " "
gesamt_breite = len(letzte_zeile_str) + 10

# Dreieck ausgeben
for zeile in dreieck:
    # Zeile als String formatieren
    zeile_str = ""
    for zahl in zeile:
        zeile_str += str(zahl) + " "

    # Zentriert ausgeben
    print(zeile_str.center(gesamt_breite))

print()
print(f"✓ Das Pascal'sche Dreieck hat {anzahl_zeilen} Zeilen.")

# === ERWEITERTE VERSION MIT ZEILENSUMMEN ===

print("\n" + "=" * 50)
print("      MIT ZEILENSUMMEN")
print("=" * 50)
print()

for i in range(len(dreieck)):
    zeile = dreieck[i]

    # Zeile als String
    zeile_str = ""
    for zahl in zeile:
        zeile_str += str(zahl) + " "

    # Summe berechnen
    summe = 0
    for zahl in zeile:
        summe += zahl

    # Formatierte Ausgabe
    zeile_formatiert = zeile_str.center(gesamt_breite - 15)
    print(f"{zeile_formatiert} | Summe: {summe}")

# === INTERESSANTE EIGENSCHAFTEN ===

print("\n" + "=" * 50)
print("      INTERESSANTE EIGENSCHAFTEN")
print("=" * 50)

# Eigenschaft 1: Zeilensummen sind Zweierpotenzen
print("\n📊 Zeilensummen sind Zweierpotenzen (2^n):")
for i in range(len(dreieck)):
    summe = 0
    for zahl in dreieck[i]:
        summe += zahl
    zweierpotenz = 2 ** i
    print(f"   Zeile {i + 1}: Summe = {summe} = 2^{i}")

# Eigenschaft 2: Symmetrie
print("\n🔄 Jede Zeile ist symmetrisch (palindrom):")
for i in range(len(dreieck)):
    zeile = dreieck[i]
    # Prüfen ob symmetrisch
    ist_symmetrisch = True
    for j in range(len(zeile) // 2):
        if zeile[j] != zeile[len(zeile) - 1 - j]:
            ist_symmetrisch = False
            break

    status = "✓" if ist_symmetrisch else "✗"
    print(f"   Zeile {i + 1}: {zeile} {status}")

# === INTERAKTIVES MENÜ (BONUS) ===

print("\n" + "=" * 50)
print("      INTERAKTIVES MENÜ")
print("=" * 50)

while True:
    print("\n--- Optionen ---")
    print("1. Neues Dreieck generieren")
    print("2. Bestimmte Zeile anzeigen")
    print("3. Bestimmten Wert anzeigen")
    print("4. Beenden")

    wahl = input("\nIhre Wahl (1-4): ")

    if wahl == "1":
        # Neues Dreieck
        eingabe = input("Anzahl Zeilen (1-15): ")
        if eingabe.isdigit():
            n = int(eingabe)
            if 1 <= n <= 15:
                # Neues Dreieck berechnen
                dreieck = []
                for zeile_nr in range(n):
                    neue_zeile = []
                    for position in range(zeile_nr + 1):
                        if position == 0 or position == zeile_nr:
                            wert = 1
                        else:
                            vorherige_zeile = dreieck[zeile_nr - 1]
                            wert = vorherige_zeile[position - 1] + vorherige_zeile[position]
                        neue_zeile.append(wert)
                    dreieck.append(neue_zeile)

                # Ausgabe
                print()
                letzte_zeile_str = ""
                for zahl in dreieck[-1]:
                    letzte_zeile_str += str(zahl) + " "
                breite = len(letzte_zeile_str) + 10

                for zeile in dreieck:
                    zeile_str = ""
                    for zahl in zeile:
                        zeile_str += str(zahl) + " "
                    print(zeile_str.center(breite))
            else:
                print("❌ Ungültiger Bereich!")
        else:
            print("❌ Keine gültige Zahl!")

    elif wahl == "2":
        # Bestimmte Zeile anzeigen
        eingabe = input(f"Welche Zeile (1-{len(dreieck)})? ")
        if eingabe.isdigit():
            zeile_nr = int(eingabe)
            if 1 <= zeile_nr <= len(dreieck):
                zeile = dreieck[zeile_nr - 1]
                print(f"\nZeile {zeile_nr}: {zeile}")

                summe = 0
                for zahl in zeile:
                    summe += zahl
                print(f"Summe: {summe}")
                print(f"Anzahl Elemente: {len(zeile)}")
            else:
                print("❌ Zeile existiert nicht!")
        else:
            print("❌ Keine gültige Zahl!")

    elif wahl == "3":
        # Bestimmten Wert anzeigen (n über k)
        print("\nDer Wert an Position (Zeile, Spalte) entspricht")
        print("dem Binomialkoeffizienten 'n über k'.")

        zeile_eingabe = input(f"Zeile (1-{len(dreieck)}): ")
        spalte_eingabe = input("Spalte (beginnend bei 1): ")

        if zeile_eingabe.isdigit() and spalte_eingabe.isdigit():
            zeile_nr = int(zeile_eingabe)
            spalte_nr = int(spalte_eingabe)

            if 1 <= zeile_nr <= len(dreieck):
                zeile = dreieck[zeile_nr - 1]
                if 1 <= spalte_nr <= len(zeile):
                    wert = zeile[spalte_nr - 1]
                    n = zeile_nr - 1
                    k = spalte_nr - 1
                    print(f"\nWert an ({zeile_nr}, {spalte_nr}): {wert}")
                    print(f"Dies entspricht: {n} über {k} = {wert}")
                else:
                    print("❌ Spalte existiert nicht in dieser Zeile!")
            else:
                print("❌ Zeile existiert nicht!")
        else:
            print("❌ Ungültige Eingabe!")

    elif wahl == "4":
        print("\n👋 Auf Wiedersehen!")
        break

    else:
        print("❌ Ungültige Auswahl!")

print("\n" + "=" * 50)
print("Programm beendet.")
print("=" * 50)
