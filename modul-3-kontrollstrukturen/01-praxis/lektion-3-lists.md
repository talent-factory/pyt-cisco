# Lektion 3: Lists and List Processing

**Dauer:** 50 Minuten  
**Format:** 15 Min Theorie + 20 Min Live-Coding + 15 Min Übung  
**CISCO Kapitel:** 3.4-3.7 Lists

## 🎯 Lernziele

- Listen erstellen und initialisieren
- Auf Listenelemente zugreifen (Indexing)
- Listen manipulieren (append, insert, remove, pop)
- Slicing für Teilbereiche nutzen
- Listen durchlaufen (Iteration)
- In und not in Operatoren verwenden
- 2D Arrays (Listen in Listen) verstehen

## 📖 Theorie (15 Min)

### Listen erstellen

```python
# Leere Liste
zahlen = []

# Liste mit Werten
fruechte = ["Apfel", "Banane", "Orange"]
noten = [5, 4, 6, 5, 4]
gemischt = [1, "Text", 3.14, True]  # Verschiedene Typen möglich
```

### Indexing - Zugriff auf Elemente

```python
fruechte = ["Apfel", "Banane", "Orange"]

# Positiver Index (von vorne)
print(fruechte[0])   # Apfel (erstes Element)
print(fruechte[1])   # Banane
print(fruechte[2])   # Orange

# Negativer Index (von hinten)
print(fruechte[-1])  # Orange (letztes Element)
print(fruechte[-2])  # Banane
print(fruechte[-3])  # Apfel

# Länge der Liste
print(len(fruechte))  # 3
```

### List Methods - Listen manipulieren

```python
fruechte = ["Apfel", "Banane"]

# Hinzufügen
fruechte.append("Orange")      # Am Ende hinzufügen
fruechte.insert(1, "Kiwi")     # An Position 1 einfügen

# Entfernen
fruechte.remove("Banane")      # Bestimmtes Element entfernen
letztes = fruechte.pop()       # Letztes Element entfernen und zurückgeben
element = fruechte.pop(0)      # Element an Index 0 entfernen

# Weitere Operationen
fruechte.sort()                # Liste sortieren
fruechte.reverse()             # Liste umkehren
fruechte.clear()               # Alle Elemente entfernen
```

### Slicing - Teilbereiche

```python
zahlen = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(zahlen[2:5])    # [2, 3, 4] - Von Index 2 bis 4
print(zahlen[:3])     # [0, 1, 2] - Von Anfang bis Index 2
print(zahlen[7:])     # [7, 8, 9] - Von Index 7 bis Ende
print(zahlen[::2])    # [0, 2, 4, 6, 8] - Jedes zweite Element
print(zahlen[::-1])   # [9, 8, 7, ..., 0] - Liste umkehren
```

### In und not in Operatoren

```python
fruechte = ["Apfel", "Banane", "Orange"]

if "Apfel" in fruechte:
    print("Apfel ist in der Liste")

if "Kiwi" not in fruechte:
    print("Kiwi ist nicht in der Liste")
```

### Listen durchlaufen

```python
fruechte = ["Apfel", "Banane", "Orange"]

# Direkt über Elemente
for frucht in fruechte:
    print(frucht)

# Mit Index
for i in range(len(fruechte)):
    print(f"{i}: {fruechte[i]}")

# Mit enumerate (elegant!)
for index, frucht in enumerate(fruechte):
    print(f"{index}: {frucht}")
```

### Listen in Listen (2D Arrays)

```python
# Matrix 3x3
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0][0])  # 1 - Erste Zeile, erste Spalte
print(matrix[1][2])  # 6 - Zweite Zeile, dritte Spalte
```

## 💻 Live-Coding (20 Min)

### Beispiel 1: Einkaufsliste (CISCO LAB: The Beatles)

```python
"""
Einkaufsliste verwalten
CISCO 3.4.11 LAB: The basics of lists - the Beatles
"""

print("=" * 40)
print("Einkaufsliste")
print("=" * 40)

# Leere Liste erstellen
einkaufsliste = []

# Elemente hinzufügen
einkaufsliste.append("Milch")
einkaufsliste.append("Brot")
einkaufsliste.append("Eier")
einkaufsliste.insert(0, "Butter")  # Am Anfang einfügen

print("\nAktuelle Einkaufsliste:")
for index, artikel in enumerate(einkaufsliste, start=1):
    print(f"{index}. {artikel}")

# Element entfernen
if "Brot" in einkaufsliste:
    einkaufsliste.remove("Brot")
    print("\n'Brot' wurde entfernt")

# Sortieren
einkaufsliste.sort()
print("\nSortierte Liste:")
for artikel in einkaufsliste:
    print(f"- {artikel}")

print(f"\nAnzahl Artikel: {len(einkaufsliste)}")
```

**Erklärung:**
- Liste dynamisch aufbauen
- Verschiedene Methoden nutzen
- Mit enumerate nummeriert ausgeben

### Beispiel 2: Notenstatistik

```python
"""
Notenstatistik - Durchschnitt, Min, Max berechnen
CISCO 3.6.6 LAB: Operating with lists - basics
"""

print("=" * 40)
print("Notenstatistik")
print("=" * 40)

noten = []

# Noten eingeben
anzahl = int(input("Wie viele Noten? "))

for i in range(anzahl):
    note = float(input(f"Note {i + 1}: "))
    noten.append(note)

# Statistik berechnen
durchschnitt = sum(noten) / len(noten)
minimum = min(noten)
maximum = max(noten)

# Ausgabe
print("\n" + "=" * 40)
print("Statistik")
print("=" * 40)
print(f"Noten: {noten}")
print(f"Anzahl: {len(noten)}")
print(f"Durchschnitt: {durchschnitt:.2f}")
print(f"Beste Note: {maximum}")
print(f"Schlechteste Note: {minimum}")

# Noten über Durchschnitt
print("\nNoten über Durchschnitt:")
for note in noten:
    if note > durchschnitt:
        print(f"- {note}")
```

**Erklärung:**
- Liste mit Input füllen
- Built-in Funktionen: sum(), min(), max()
- Liste filtern

### Beispiel 3: 2D Array - Schachbrett

```python
"""
2D Array - Schachbrett darstellen
CISCO 3.7.3: Multidimensional nature of lists
"""

print("=" * 40)
print("Schachbrett (8x8)")
print("=" * 40)

# Schachbrett erstellen (8x8)
schachbrett = []

for zeile in range(8):
    reihe = []
    for spalte in range(8):
        # Schachbrettmuster: Abwechselnd 0 und 1
        if (zeile + spalte) % 2 == 0:
            reihe.append(0)
        else:
            reihe.append(1)
    schachbrett.append(reihe)

# Schachbrett ausgeben
for zeile in schachbrett:
    for feld in zeile:
        if feld == 0:
            print("⬜", end="")
        else:
            print("⬛", end="")
    print()  # Neue Zeile

# Zugriff auf einzelne Felder
print(f"\nFeld [0][0]: {schachbrett[0][0]}")
print(f"Feld [3][4]: {schachbrett[3][4]}")
```

**Erklärung:**
- Verschachtelte Schleifen für 2D Array
- Liste in Liste
- Zugriff mit zwei Indizes

## ✏️ Übung (15 Min)

Jetzt sind Sie dran!

- [Übung 5: Gerade Zahlen filtern](../02-uebungen/uebung-5-gerade-zahlen.md)
- [Übung 6: Notenliste verarbeiten](../02-uebungen/uebung-6-notenliste.md)

## 📝 Zusammenfassung

- Listen mit `[]` erstellen
- Indexing: `liste[0]`, `liste[-1]`
- Methods: `append()`, `insert()`, `remove()`, `pop()`
- Slicing: `liste[start:stop:step]`
- `in` und `not in` für Mitgliedschaft
- Iteration mit `for element in liste`
- 2D Arrays: `matrix[zeile][spalte]`

## ⚠️ Häufige Fehler

1. **Index out of range**
   ```python
   liste = [1, 2, 3]
   print(liste[3])  # Fehler! Index 3 existiert nicht (0, 1, 2)
   ```

2. **Liste vs. Element**
   ```python
   fruechte = ["Apfel"]
   print(fruechte)    # ['Apfel'] - Liste
   print(fruechte[0]) # Apfel - String
   ```

3. **Vergessene Klammern bei Methoden**
   ```python
   liste.append(5)  # RICHTIG
   liste.append 5   # FALSCH
   ```

## 🔗 Weiter

[Lektion 4: Logical & Bitwise Operations + Sorting](./lektion-4-logic-sorting.md)

