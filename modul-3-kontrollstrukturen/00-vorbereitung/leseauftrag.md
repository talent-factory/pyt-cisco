# Leseauftrag: Kontrollstrukturen, Listen und Logische Operationen

**Zeitaufwand:** 30-45 Minuten
**Ergänzung zu:** CISCO NetAcad Kapitel 3.1-3.7

> **Hinweis:** Dieser Leseauftrag fasst die wichtigsten Konzepte zusammen. Arbeiten Sie zuerst die CISCO NetAcad Kapitel durch!

## 1. Boolean Values (CISCO 3.1)

### Was sind Boolean Values?

In Python gibt es zwei Boolean-Werte:
- `True` (wahr)
- `False` (falsch)

```python
ist_student = True
ist_abgeschlossen = False
```

### Vergleichsoperatoren

Vergleiche erzeugen Boolean-Werte:

| Operator | Bedeutung | Beispiel | Ergebnis |
|----------|-----------|----------|----------|
| `==` | Gleich | `5 == 5` | `True` |
| `!=` | Ungleich | `5 != 3` | `True` |
| `<` | Kleiner | `3 < 5` | `True` |
| `>` | Größer | `5 > 3` | `True` |
| `<=` | Kleiner oder gleich | `5 <= 5` | `True` |
| `>=` | Größer oder gleich | `5 >= 3` | `True` |

```python
alter = 20
ist_volljaehrig = alter >= 18  # True
```

## 2. Bedingte Anweisungen (CISCO 3.1)

### If-Anweisung

Führt Code nur aus, wenn Bedingung `True` ist:

```python
alter = 18
if alter >= 18:
    print("Volljährig")  # Wird ausgeführt
```

### If-Else

Zwei Alternativen:

```python
alter = 16
if alter >= 18:
    print("Volljährig")
else:
    print("Minderjährig")  # Wird ausgeführt
```

### If-Elif-Else

Mehrere Bedingungen prüfen:

```python
punkte = 85

if punkte >= 90:
    note = 6
elif punkte >= 80:
    note = 5  # Diese Bedingung trifft zu
elif punkte >= 70:
    note = 4
else:
    note = 3

print(f"Note: {note}")  # Note: 5
```

### Verschachtelte Bedingungen

```python
alter = 20
hat_fuehrerschein = True

if alter >= 18:
    if hat_fuehrerschein:
        print("Darf Auto fahren")  # Wird ausgeführt
    else:
        print("Braucht Führerschein")
else:
    print("Zu jung")
```

## 3. While-Schleifen (CISCO 3.2)

### Grundprinzip

Wiederholt Code, solange Bedingung `True` ist:

```python
zaehler = 1
while zaehler <= 5:
    print(zaehler)  # 1, 2, 3, 4, 5
    zaehler += 1  # WICHTIG: Bedingung muss irgendwann False werden!
```

### Break - Schleife vorzeitig beenden

```python
while True:
    eingabe = input("Zahl (0 = Ende): ")
    if eingabe == "0":
        break  # Beendet die Schleife
    print(f"Sie haben {eingabe} eingegeben")
```

### Continue - Iteration überspringen

```python
zaehler = 0
while zaehler < 10:
    zaehler += 1
    if zaehler % 2 == 0:
        continue  # Überspringt gerade Zahlen
    print(zaehler)  # Gibt nur ungerade Zahlen aus: 1, 3, 5, 7, 9
```

### ⚠️ Endlosschleifen vermeiden!

```python
# FALSCH - Endlosschleife!
zaehler = 1
while zaehler <= 5:
    print(zaehler)
    # Fehler: zaehler wird nie erhöht!

# RICHTIG
zaehler = 1
while zaehler <= 5:
    print(zaehler)
    zaehler += 1  # Bedingung wird irgendwann False
```

## 4. For-Schleifen (CISCO 3.2)

### For mit range()

```python
# 0 bis 4
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# 1 bis 5
for i in range(1, 6):
    print(i)  # 1, 2, 3, 4, 5

# Mit Schrittweite
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8
```

### For über Listen

```python
fruechte = ["Apfel", "Banane", "Orange"]

for frucht in fruechte:
    print(frucht)
```

## 5. Listen (CISCO 3.4-3.7)

### Listen erstellen

```python
# Leere Liste
zahlen = []

# Liste mit Werten
fruechte = ["Apfel", "Banane", "Orange"]
noten = [5, 4, 6, 5, 4]
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

# Weitere Operationen
anzahl = len(fruechte)         # Länge der Liste
fruechte.sort()                # Liste sortieren
fruechte.reverse()             # Liste umkehren
```

### Slicing - Teilbereiche

```python
zahlen = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(zahlen[2:5])    # [2, 3, 4] - Von Index 2 bis 4
print(zahlen[:3])     # [0, 1, 2] - Von Anfang bis Index 2
print(zahlen[7:])     # [7, 8, 9] - Von Index 7 bis Ende
print(zahlen[::2])    # [0, 2, 4, 6, 8] - Jedes zweite Element
```

### In und not in Operatoren

```python
fruechte = ["Apfel", "Banane", "Orange"]

if "Apfel" in fruechte:
    print("Apfel ist in der Liste")  # Wird ausgeführt

if "Kiwi" not in fruechte:
    print("Kiwi ist nicht in der Liste")  # Wird ausgeführt
```

### Listen in Listen (2D Arrays)

```python
# Schachbrett-ähnliche Struktur
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0][0])  # 1 - Erste Zeile, erste Spalte
print(matrix[1][2])  # 6 - Zweite Zeile, dritte Spalte
```

## 6. Logische Operatoren (CISCO 3.3)

### And, Or, Not

```python
alter = 20
hat_fuehrerschein = True

# AND - Beide Bedingungen müssen True sein
if alter >= 18 and hat_fuehrerschein:
    print("Darf Auto fahren")

# OR - Mindestens eine Bedingung muss True sein
ist_wochenende = True
ist_feiertag = False

if ist_wochenende or ist_feiertag:
    print("Frei!")  # Wird ausgeführt

# NOT - Negiert den Boolean-Wert
ist_regen = False
if not ist_regen:
    print("Kein Regen")  # Wird ausgeführt
```

### Short-circuit Evaluation

Python wertet logische Ausdrücke von links nach rechts aus und stoppt, sobald das Ergebnis feststeht:

```python
# Bei AND: Stoppt bei erstem False
if False and print("Wird nicht ausgeführt"):
    pass

# Bei OR: Stoppt bei erstem True
if True or print("Wird nicht ausgeführt"):
    pass
```

## 7. Bitweise Operatoren (CISCO 3.3) - Einführung

Bitweise Operatoren arbeiten auf Bit-Ebene (0 und 1):

```python
# & (AND), | (OR), ^ (XOR), ~ (NOT), << (Left Shift), >> (Right Shift)

a = 5   # Binär: 0101
b = 3   # Binär: 0011

print(a & b)   # 1  (0001) - Bitweises AND
print(a | b)   # 7  (0111) - Bitweises OR
print(a ^ b)   # 6  (0110) - Bitweises XOR
print(~a)      # -6        - Bitweises NOT
print(a << 1)  # 10 (1010) - Links verschieben
print(a >> 1)  # 2  (0010) - Rechts verschieben
```

> **Hinweis:** Bitweise Operatoren werden in Lektion 4 ausführlicher behandelt.

## 8. Bubble Sort Algorithm (CISCO 3.5) - Vorschau

Der Bubble Sort ist ein einfacher Sortieralgorithmus:

```python
zahlen = [64, 34, 25, 12, 22, 11, 90]

# Bubble Sort
n = len(zahlen)
for i in range(n):
    for j in range(0, n - i - 1):
        if zahlen[j] > zahlen[j + 1]:
            # Tauschen
            zahlen[j], zahlen[j + 1] = zahlen[j + 1], zahlen[j]

print(zahlen)  # [11, 12, 22, 25, 34, 64, 90]
```

> **Hinweis:** Bubble Sort wird in Lektion 4 ausführlich erklärt.

## ✅ Zusammenfassung

Sie haben gelernt:

- ✅ Boolean Values und Vergleichsoperatoren
- ✅ If/elif/else für Entscheidungen
- ✅ While-Schleifen für Wiederholungen
- ✅ For-Schleifen für Iteration
- ✅ Break und continue
- ✅ Listen erstellen und manipulieren
- ✅ Logische Operatoren (and, or, not)
- ✅ Bitweise Operatoren (Einführung)
- ✅ Bubble Sort (Vorschau)

## 🔗 Weiter

Jetzt sind Sie bereit für die [Ersten Experimente](./erste-experimente.md)!


