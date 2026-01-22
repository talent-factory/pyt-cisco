# Lektion 1: Boolean Values & Conditional Execution

**Dauer:** 50 Minuten  
**Format:** 15 Min Theorie + 20 Min Live-Coding + 15 Min Übung  
**CISCO Kapitel:** 3.1 Making decisions in Python

## 🎯 Lernziele

- Boolean Values (True/False) verstehen
- Vergleichsoperatoren kennen und anwenden
- If-Anweisungen nutzen
- If-else Strukturen verwenden
- If-elif-else Ketten implementieren
- Verschachtelte Bedingungen verstehen

## 📖 Theorie (15 Min)

### Boolean Values

Python kennt zwei Boolean-Werte:

```python
ist_student = True
ist_abgeschlossen = False

print(type(ist_student))  # <class 'bool'>
```

### Vergleichsoperatoren (Comparison Operators)

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

### If-Anweisung

Führt Code nur aus, wenn Bedingung `True` ist:

```python
if bedingung:
    # Code wird nur ausgeführt wenn bedingung True ist
    print("Bedingung erfüllt")
```

**Wichtig:** Einrückung (4 Leerzeichen oder Tab) ist zwingend!

### If-Else

Zwei Alternativen:

```python
if bedingung:
    print("Bedingung erfüllt")
else:
    print("Bedingung nicht erfüllt")
```

### If-Elif-Else

Mehrere Bedingungen prüfen:

```python
if bedingung1:
    print("Bedingung 1")
elif bedingung2:
    print("Bedingung 2")
elif bedingung3:
    print("Bedingung 3")
else:
    print("Keine Bedingung erfüllt")
```

**Wichtig:** Nur der erste zutreffende Block wird ausgeführt!

### Verschachtelte Bedingungen

```python
if bedingung1:
    if bedingung2:
        print("Beide Bedingungen erfüllt")
    else:
        print("Nur Bedingung 1 erfüllt")
else:
    print("Bedingung 1 nicht erfüllt")
```

## 💻 Live-Coding (20 Min)

### Beispiel 1: Alterscheck (CISCO LAB: Variables)

```python
"""
Alterscheck - Volljährigkeit prüfen
CISCO 3.1.6 LAB: Variables - Questions and answers
"""

print("=" * 40)
print("Alterscheck")
print("=" * 40)

alter = int(input("Wie alt sind Sie? "))

if alter >= 18:
    print("✅ Sie sind volljährig")
else:
    print("❌ Sie sind minderjährig")

print("\nProgramm beendet")
```

**Erklärung:**
- Input wird in Integer umgewandelt
- Vergleich mit `>=` Operator
- If-else für zwei Fälle

### Beispiel 2: Notensystem (CISCO LAB: if-elif-else)

```python
"""
Notensystem - Punkte in Noten umwandeln
CISCO 3.1.12 LAB: Essentials of the if-elif-else statement
"""

print("=" * 40)
print("Notensystem")
print("=" * 40)

punkte = int(input("Erreichte Punkte (0-100): "))

if punkte >= 90:
    note = 6
    bewertung = "Ausgezeichnet"
elif punkte >= 80:
    note = 5
    bewertung = "Sehr gut"
elif punkte >= 70:
    note = 4
    bewertung = "Gut"
elif punkte >= 60:
    note = 3
    bewertung = "Genügend"
else:
    note = 2
    bewertung = "Ungenügend"

print(f"\nBei {punkte} Punkten:")
print(f"Note: {note}")
print(f"Bewertung: {bewertung}")
```

**Erklärung:**
- Mehrere Bedingungen mit elif
- Nur die erste zutreffende Bedingung wird ausgeführt
- Else als "Auffangbecken"

### Beispiel 3: Rabatt-Rechner mit verschachtelten Bedingungen

```python
"""
Rabatt-Rechner - Verschiedene Rabattstufen
"""

print("=" * 40)
print("Rabatt-Rechner")
print("=" * 40)

preis = float(input("Preis (CHF): "))
ist_mitglied = input("Sind Sie Mitglied? (j/n): ").lower() == "j"
alter = int(input("Ihr Alter: "))

rabatt = 0

if ist_mitglied:
    if alter >= 65:
        rabatt = 20  # Senior-Mitglied
    elif alter < 18:
        rabatt = 15  # Junior-Mitglied
    else:
        rabatt = 10  # Normales Mitglied
else:
    if alter >= 65 or alter < 18:
        rabatt = 5   # Senior oder Junior ohne Mitgliedschaft

endpreis = preis * (1 - rabatt / 100)

print(f"\nOriginalpreis: {preis:.2f} CHF")
print(f"Rabatt: {rabatt}%")
print(f"Endpreis: {endpreis:.2f} CHF")
print(f"Ersparnis: {preis - endpreis:.2f} CHF")
```

**Erklärung:**
- Verschachtelte if-Anweisungen
- Kombination von Bedingungen
- Berechnung mit Rabatt

## ✏️ Übung (15 Min)

Jetzt sind Sie dran!

- [Übung 1: Notensystem implementieren](../02-uebungen/uebung-1-notensystem.md)
- [Übung 2: Rabattrechner mit Bedingungen](../02-uebungen/uebung-2-rabatt.md)

## 📝 Zusammenfassung

- `True` und `False` sind Boolean-Werte
- Vergleichsoperatoren: `==`, `!=`, `<`, `>`, `<=`, `>=`
- `if` für einfache Bedingungen
- `if-else` für zwei Fälle
- `if-elif-else` für mehrere Fälle
- Einrückung ist wichtig!
- Verschachtelte Bedingungen für komplexe Logik

## ⚠️ Häufige Fehler

1. **Vergessene Einrückung**
   ```python
   # FALSCH
   if alter >= 18:
   print("Volljährig")  # Fehler!
   
   # RICHTIG
   if alter >= 18:
       print("Volljährig")
   ```

2. **`=` statt `==`**
   ```python
   # FALSCH
   if alter = 18:  # Fehler! (Zuweisung statt Vergleich)
   
   # RICHTIG
   if alter == 18:
   ```

3. **Vergessener Doppelpunkt**
   ```python
   # FALSCH
   if alter >= 18  # Fehler!
   
   # RICHTIG
   if alter >= 18:
   ```

## 🔗 Weiter

[Lektion 2: Loops - While & For](./lektion-2-loops.md)

