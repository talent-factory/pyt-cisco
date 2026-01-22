# Lektion 4: Logical & Bitwise Operations + Sorting

**Dauer:** 50 Minuten  
**Format:** 10 Min Theorie + 15 Min Live-Coding + 10 Min Sorting + 15 Min Übung  
**CISCO Kapitel:** 3.3 Logic and bit operations, 3.5 Bubble Sort

## 🎯 Lernziele

- Logische Operatoren (and, or, not) verstehen
- Short-circuit Evaluation kennen
- Bitweise Operatoren verstehen (Einführung)
- Bubble Sort Algorithm implementieren
- Komplexe Bedingungen formulieren

## 📖 Theorie Teil 1: Logische Operatoren (10 Min)

### And, Or, Not

```python
# AND - Beide Bedingungen müssen True sein
alter = 20
hat_fuehrerschein = True

if alter >= 18 and hat_fuehrerschein:
    print("Darf Auto fahren")

# OR - Mindestens eine Bedingung muss True sein
ist_wochenende = True
ist_feiertag = False

if ist_wochenende or ist_feiertag:
    print("Frei!")

# NOT - Negiert den Boolean-Wert
ist_regen = False
if not ist_regen:
    print("Kein Regen")
```

### Wahrheitstabellen

**AND:**
| A | B | A and B |
|---|---|---------|
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | F |

**OR:**
| A | B | A or B |
|---|---|--------|
| T | T | T |
| T | F | T |
| F | T | T |
| F | F | F |

**NOT:**
| A | not A |
|---|-------|
| T | F |
| F | T |

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

### Bitweise Operatoren (Einführung)

Arbeiten auf Bit-Ebene (0 und 1):

```python
a = 5   # Binär: 0101
b = 3   # Binär: 0011

print(a & b)   # 1  (0001) - Bitweises AND
print(a | b)   # 7  (0111) - Bitweises OR
print(a ^ b)   # 6  (0110) - Bitweises XOR
print(~a)      # -6        - Bitweises NOT
print(a << 1)  # 10 (1010) - Links verschieben
print(a >> 1)  # 2  (0010) - Rechts verschieben
```

**Unterschied zu logischen Operatoren:**
- Logisch: `and`, `or`, `not` - Arbeiten mit Boolean-Werten
- Bitweise: `&`, `|`, `^`, `~`, `<<`, `>>` - Arbeiten mit Bits

## 💻 Live-Coding Teil 1: Logische Operatoren (15 Min)

### Beispiel 1: Zugangsberechtigungen

```python
"""
Zugangsberechtigungen prüfen
CISCO 3.3.2: Logical expressions
"""

print("=" * 40)
print("Zugangsberechtigungen")
print("=" * 40)

alter = int(input("Alter: "))
hat_ticket = input("Ticket vorhanden? (j/n): ").lower() == "j"
ist_vip = input("VIP-Mitglied? (j/n): ").lower() == "j"

# Verschiedene Bedingungen
if alter >= 18 and hat_ticket:
    print("✅ Zugang gewährt (Erwachsener mit Ticket)")
elif alter < 18 and hat_ticket:
    print("✅ Zugang gewährt (Kind mit Ticket)")
elif ist_vip:
    print("✅ Zugang gewährt (VIP - kein Ticket nötig)")
else:
    print("❌ Zugang verweigert")

# Komplexe Bedingung
if (alter >= 18 and hat_ticket) or ist_vip:
    print("\n🎉 Willkommen!")
```

### Beispiel 2: Bitweise Operationen

```python
"""
Bitweise Operationen demonstrieren
CISCO 3.3.4: Bitwise operators
"""

print("=" * 40)
print("Bitweise Operationen")
print("=" * 40)

a = 12  # Binär: 1100
b = 10  # Binär: 1010

print(f"a = {a} (Binär: {bin(a)})")
print(f"b = {b} (Binär: {bin(b)})")
print()

print(f"a & b  = {a & b}  (Binär: {bin(a & b)})  - AND")
print(f"a | b  = {a | b}  (Binär: {bin(a | b)})  - OR")
print(f"a ^ b  = {a ^ b}  (Binär: {bin(a ^ b)})  - XOR")
print(f"~a     = {~a}     (Binär: {bin(~a)})     - NOT")
print(f"a << 1 = {a << 1} (Binär: {bin(a << 1)}) - Left Shift")
print(f"a >> 1 = {a >> 1} (Binär: {bin(a >> 1)}) - Right Shift")

# Praktisches Beispiel: Flags
LESEN = 1    # 0001
SCHREIBEN = 2  # 0010
AUSFUEHREN = 4  # 0100

# Berechtigungen kombinieren
berechtigungen = LESEN | SCHREIBEN  # 0011 = 3

# Prüfen ob Berechtigung vorhanden
if berechtigungen & LESEN:
    print("\n✅ Leseberechtigung vorhanden")
if berechtigungen & SCHREIBEN:
    print("✅ Schreibberechtigung vorhanden")
if not (berechtigungen & AUSFUEHREN):
    print("❌ Keine Ausführungsberechtigung")
```

## 📖 Theorie Teil 2: Bubble Sort (10 Min)

### Bubble Sort Algorithm

Der Bubble Sort ist ein einfacher Sortieralgorithmus:

**Prinzip:**
1. Durchlaufe die Liste mehrmals
2. Vergleiche benachbarte Elemente
3. Tausche sie, wenn sie in falscher Reihenfolge sind
4. Wiederhole, bis Liste sortiert ist

**Visualisierung:**
```
[5, 3, 8, 4, 2]
[3, 5, 4, 2, 8]  # 8 "blubbert" nach oben
[3, 4, 2, 5, 8]  # 5 "blubbert" nach oben
[3, 2, 4, 5, 8]
[2, 3, 4, 5, 8]  # Sortiert!
```

### Implementierung

```python
zahlen = [64, 34, 25, 12, 22, 11, 90]

n = len(zahlen)
for i in range(n):
    for j in range(0, n - i - 1):
        if zahlen[j] > zahlen[j + 1]:
            # Tauschen
            zahlen[j], zahlen[j + 1] = zahlen[j + 1], zahlen[j]

print(zahlen)  # [11, 12, 22, 25, 34, 64, 90]
```

## 💻 Live-Coding Teil 2: Bubble Sort (Demo)

```python
"""
Bubble Sort - Interaktive Version
CISCO 3.5.2: Sorting a list
"""

print("=" * 40)
print("Bubble Sort")
print("=" * 40)

zahlen = [64, 34, 25, 12, 22, 11, 90]
print(f"Unsortiert: {zahlen}")
print()

n = len(zahlen)
durchlaeufe = 0

for i in range(n):
    getauscht = False
    print(f"Durchlauf {i + 1}:")
    
    for j in range(0, n - i - 1):
        if zahlen[j] > zahlen[j + 1]:
            # Tauschen
            zahlen[j], zahlen[j + 1] = zahlen[j + 1], zahlen[j]
            getauscht = True
            print(f"  Tausche {zahlen[j + 1]} und {zahlen[j]}")
    
    print(f"  Ergebnis: {zahlen}")
    durchlaeufe += 1
    
    # Optimierung: Wenn nichts getauscht wurde, ist Liste sortiert
    if not getauscht:
        print("  Liste ist sortiert!")
        break

print()
print(f"Sortiert: {zahlen}")
print(f"Anzahl Durchläufe: {durchlaeufe}")
```

## ✏️ Übung (15 Min)

Jetzt sind Sie dran!

- [Übung 7: Multiplikationstabelle](../02-uebungen/uebung-7-multiplikationstabelle.md)
- [Übung 8: Zahlen-Pyramide](../02-uebungen/uebung-8-zahlen-pyramide.md)

## 📝 Zusammenfassung

**Logische Operatoren:**
- `and` - Beide Bedingungen müssen True sein
- `or` - Mindestens eine Bedingung muss True sein
- `not` - Negiert Boolean-Wert
- Short-circuit Evaluation spart Rechenzeit

**Bitweise Operatoren:**
- `&` (AND), `|` (OR), `^` (XOR), `~` (NOT)
- `<<` (Left Shift), `>>` (Right Shift)
- Arbeiten auf Bit-Ebene

**Bubble Sort:**
- Einfacher Sortieralgorithmus
- Vergleicht benachbarte Elemente
- Tauscht bei falscher Reihenfolge
- Nicht effizient für große Listen

## ⚠️ Häufige Fehler

1. **Verwechslung logisch/bitweise**
   ```python
   # FALSCH für Boolean-Logik
   if True & False:  # Bitweise Operation!
   
   # RICHTIG
   if True and False:
   ```

2. **Falsche Priorität**
   ```python
   # Vorsicht bei Prioritäten!
   if a or b and c:  # and hat höhere Priorität!
   if a or (b and c):  # Besser: Klammern nutzen
   ```

## 🎉 Modul 3 abgeschlossen!

Sie haben alle 4 Lektionen absolviert und können nun:
- ✅ Bedingungen und Schleifen nutzen
- ✅ Listen verarbeiten
- ✅ Logische Operationen durchführen
- ✅ Einfache Algorithmen implementieren

## 🔗 Weiter

Arbeiten Sie die [Nachbearbeitungsaufgaben](../03-nachbearbeitung/) durch!

