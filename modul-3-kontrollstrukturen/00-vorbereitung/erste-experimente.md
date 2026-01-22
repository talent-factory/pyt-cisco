# Erste Experimente: Kontrollstrukturen und Listen

**Zeitaufwand:** 45-60 Minuten  
**Ziel:** Praktisches Ausprobieren der Konzepte aus dem Leseauftrag

> **Tipp:** Öffnen Sie VS Code oder GitHub Codespaces und probieren Sie jeden Code-Schnipsel aus!

## Experiment 1: Boolean Values und Vergleiche

Öffnen Sie die Python-Shell oder erstellen Sie eine neue `.py` Datei:

```python
# Boolean Values
ist_student = True
ist_abgeschlossen = False

print(f"Student: {ist_student}")
print(f"Abgeschlossen: {ist_abgeschlossen}")

# Vergleichsoperatoren
alter = 20
print(f"Volljährig? {alter >= 18}")  # True
print(f"Minderjährig? {alter < 18}")  # False

# Verschiedene Vergleiche
a = 10
b = 5
print(f"{a} == {b}: {a == b}")  # False
print(f"{a} != {b}: {a != b}")  # True
print(f"{a} > {b}: {a > b}")    # True
print(f"{a} < {b}: {a < b}")    # False
```

**Aufgabe:** Ändern Sie die Werte und beobachten Sie die Ergebnisse!

## Experiment 2: If-Anweisungen

```python
# Einfaches If
alter = 20
if alter >= 18:
    print("Sie sind volljährig")

# If-Else
alter = 16
if alter >= 18:
    print("Volljährig")
else:
    print("Minderjährig")

# If-Elif-Else
punkte = 85

if punkte >= 90:
    note = 6
elif punkte >= 80:
    note = 5
elif punkte >= 70:
    note = 4
elif punkte >= 60:
    note = 3
else:
    note = 2

print(f"Bei {punkte} Punkten: Note {note}")
```

**Aufgabe:** Testen Sie verschiedene Punktzahlen (0, 50, 75, 85, 95)!

## Experiment 3: While-Schleifen

```python
# Countdown
print("Countdown:")
zaehler = 5
while zaehler > 0:
    print(zaehler)
    zaehler -= 1
print("Start! 🚀")

# Summe berechnen
summe = 0
zahl = 1
while zahl <= 10:
    summe += zahl
    zahl += 1
print(f"Summe von 1 bis 10: {summe}")  # 55

# Mit break
print("\nZahlen eingeben (0 = Ende):")
while True:
    eingabe = input("Zahl: ")
    if eingabe == "0":
        break
    print(f"Sie haben {eingabe} eingegeben")
print("Programm beendet")
```

**Aufgabe:** Probieren Sie den Code aus und geben Sie verschiedene Zahlen ein!

## Experiment 4: For-Schleifen mit range()

```python
# Einfache For-Schleife
print("Zahlen 0 bis 4:")
for i in range(5):
    print(i)

# Mit Start und Ende
print("\nZahlen 1 bis 5:")
for i in range(1, 6):
    print(i)

# Mit Schrittweite
print("\nGerade Zahlen 0 bis 10:")
for i in range(0, 11, 2):
    print(i)

# Multiplikationstabelle
zahl = 7
print(f"\nMultiplikationstabelle für {zahl}:")
for i in range(1, 11):
    print(f"{zahl} x {i} = {zahl * i}")
```

**Aufgabe:** Erstellen Sie eine Multiplikationstabelle für Ihre Lieblingszahl!

## Experiment 5: Listen erstellen und manipulieren

```python
# Liste erstellen
fruechte = ["Apfel", "Banane", "Orange"]
print(f"Früchte: {fruechte}")

# Zugriff auf Elemente
print(f"Erste Frucht: {fruechte[0]}")
print(f"Letzte Frucht: {fruechte[-1]}")

# Hinzufügen
fruechte.append("Kiwi")
print(f"Nach append: {fruechte}")

fruechte.insert(1, "Mango")
print(f"Nach insert: {fruechte}")

# Entfernen
fruechte.remove("Banane")
print(f"Nach remove: {fruechte}")

# Länge
print(f"Anzahl Früchte: {len(fruechte)}")
```

**Aufgabe:** Erstellen Sie Ihre eigene Einkaufsliste und manipulieren Sie sie!

## Experiment 6: Listen durchlaufen

```python
# Direkt über Elemente
fruechte = ["Apfel", "Banane", "Orange", "Kiwi"]

print("Alle Früchte:")
for frucht in fruechte:
    print(f"- {frucht}")

# Mit Index
print("\nMit Index:")
for i in range(len(fruechte)):
    print(f"{i + 1}. {fruechte[i]}")

# Mit enumerate (elegant!)
print("\nMit enumerate:")
for index, frucht in enumerate(fruechte, start=1):
    print(f"{index}. {frucht}")
```

**Aufgabe:** Erstellen Sie eine Liste mit Ihren Hobbys und geben Sie sie nummeriert aus!

## Experiment 7: Continue Statement

```python
# Nur ungerade Zahlen ausgeben
print("Ungerade Zahlen von 1 bis 10:")
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Überspringt gerade Zahlen
    print(i)

# Nur positive Zahlen
zahlen = [-2, 5, -1, 8, 0, 3, -7, 4]
print("\nNur positive Zahlen:")
for zahl in zahlen:
    if zahl <= 0:
        continue
    print(zahl)
```

**Aufgabe:** Filtern Sie eine Liste und geben Sie nur Zahlen > 10 aus!

## Experiment 8: Logische Operatoren

```python
# AND
alter = 20
hat_fuehrerschein = True

if alter >= 18 and hat_fuehrerschein:
    print("Darf Auto fahren")

# OR
ist_wochenende = True
ist_feiertag = False

if ist_wochenende or ist_feiertag:
    print("Frei!")

# NOT
ist_regen = False
if not ist_regen:
    print("Kein Regen - gehen wir spazieren!")

# Kombiniert
temperatur = 25
ist_sonnig = True

if temperatur > 20 and ist_sonnig and not ist_regen:
    print("Perfektes Wetter für einen Ausflug!")
```

**Aufgabe:** Erstellen Sie eigene Bedingungen für verschiedene Szenarien!

## ✅ Checkliste

Haben Sie alle Experimente durchgeführt?

- [ ] Experiment 1: Boolean Values und Vergleiche
- [ ] Experiment 2: If-Anweisungen
- [ ] Experiment 3: While-Schleifen
- [ ] Experiment 4: For-Schleifen
- [ ] Experiment 5: Listen manipulieren
- [ ] Experiment 6: Listen durchlaufen
- [ ] Experiment 7: Continue Statement
- [ ] Experiment 8: Logische Operatoren

## 🔗 Weiter

Jetzt sind Sie bereit für das [Quiz](./quiz.md)!

