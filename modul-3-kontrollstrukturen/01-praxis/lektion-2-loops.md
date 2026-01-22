# Lektion 2: Loops - While & For

**Dauer:** 50 Minuten  
**Format:** 15 Min Theorie + 20 Min Live-Coding + 15 Min Übung  
**CISCO Kapitel:** 3.2 Loops in Python

## 🎯 Lernziele

- While-Schleifen verstehen und anwenden
- For-Schleifen mit range() nutzen
- Break-Statement zum vorzeitigen Beenden
- Continue-Statement zum Überspringen
- Zählervariablen korrekt verwenden
- Endlosschleifen vermeiden

## 📖 Theorie (15 Min)

### While-Schleife

Wiederholt Code, solange Bedingung `True` ist:

```python
zaehler = 1
while zaehler <= 5:
    print(zaehler)
    zaehler += 1  # Wichtig: Bedingung muss irgendwann False werden!
```

**Ausgabe:** 1, 2, 3, 4, 5

### For-Schleife mit range()

Durchläuft eine Sequenz von Zahlen:

```python
# 0 bis 4
for i in range(5):
    print(i)

# 1 bis 5
for i in range(1, 6):
    print(i)

# Mit Schrittweite
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8
```

**range() Syntax:**
- `range(stop)` - Von 0 bis stop-1
- `range(start, stop)` - Von start bis stop-1
- `range(start, stop, step)` - Von start bis stop-1 mit Schrittweite

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
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Überspringt gerade Zahlen
    print(i)  # Gibt nur ungerade Zahlen aus
```

### Else-Zweig bei Schleifen

```python
for i in range(5):
    if i == 10:
        break
else:
    print("Schleife normal beendet (kein break)")
```

**Wichtig:** Else wird nur ausgeführt, wenn kein `break` erfolgte!

### ⚠️ Endlosschleifen vermeiden

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

**Tipp:** Ctrl+C beendet ein laufendes Python-Programm!

## 💻 Live-Coding (20 Min)

### Beispiel 1: Countdown mit while

```python
"""
Countdown - Von 10 bis 0 zählen
CISCO 3.2.1: Looping your code with while
"""

print("=" * 40)
print("Countdown")
print("=" * 40)

countdown = 10

while countdown >= 0:
    print(countdown)
    countdown -= 1

print("Start! 🚀")
```

**Erklärung:**
- Start bei 10
- Jede Iteration: Ausgabe und Dekrement
- Stoppt bei -1 (Bedingung wird False)

### Beispiel 2: Summe berechnen mit while

```python
"""
Summe berechnen - Von 1 bis N
CISCO 3.2.3: The while loop - more examples
"""

print("=" * 40)
print("Summe berechnen")
print("=" * 40)

n = int(input("Bis zu welcher Zahl summieren? "))

summe = 0
zaehler = 1

while zaehler <= n:
    summe += zaehler
    zaehler += 1

print(f"\nSumme von 1 bis {n}: {summe}")

# Formel zur Überprüfung
formel_ergebnis = n * (n + 1) // 2
print(f"Überprüfung mit Formel: {formel_ergebnis}")
```

**Erklärung:**
- Akkumulator-Variable `summe`
- Zähler-Variable `zaehler`
- Formel: n * (n+1) / 2

### Beispiel 3: Zahlenraten-Spiel (CISCO LAB)

```python
"""
Zahlenraten-Spiel
CISCO 3.2.4 LAB: Guess the secret number
"""

print("=" * 40)
print("Zahlenraten-Spiel")
print("=" * 40)

geheimzahl = 42
versuche = 0
max_versuche = 5

print(f"Ich habe mir eine Zahl zwischen 1 und 100 ausgedacht.")
print(f"Sie haben {max_versuche} Versuche.\n")

while versuche < max_versuche:
    versuch = int(input(f"Versuch {versuche + 1}: "))
    versuche += 1
    
    if versuch == geheimzahl:
        print(f"🎉 Richtig! Sie haben die Zahl in {versuche} Versuchen erraten!")
        break
    elif versuch < geheimzahl:
        print("📈 Zu klein!")
    else:
        print("📉 Zu groß!")
else:
    print(f"\n😞 Leider verloren! Die Zahl war {geheimzahl}")

print("\nSpiel beendet")
```

**Erklärung:**
- While-Schleife mit Zähler
- Break bei richtigem Versuch
- Else-Zweig bei normalem Ende (kein break)
- Feedback für den Spieler

## ✏️ Übung (15 Min)

Jetzt sind Sie dran!

- [Übung 3: Fakultät mit while-Schleife](../02-uebungen/uebung-3-fakultaet.md)
- [Übung 4: Zahlenraten-Spiel erweitern](../02-uebungen/uebung-4-zahlenraten.md)

## 📝 Zusammenfassung

- `while` wiederholt Code solange Bedingung True ist
- `for` mit `range()` für feste Anzahl Wiederholungen
- `break` beendet Schleife vorzeitig
- `continue` überspringt Rest der Iteration
- `else` bei Schleifen wird nur ohne `break` ausgeführt
- Zähler-Variable muss aktualisiert werden!
- Endlosschleifen mit Ctrl+C beenden

## ⚠️ Häufige Fehler

1. **Vergessene Inkrementierung**
   ```python
   # FALSCH - Endlosschleife!
   i = 0
   while i < 5:
       print(i)
       # i wird nie erhöht!
   ```

2. **Off-by-one Fehler**
   ```python
   # range(5) erzeugt 0, 1, 2, 3, 4 (NICHT 5!)
   for i in range(5):
       print(i)  # 0 bis 4
   ```

3. **Break außerhalb Schleife**
   ```python
   # FALSCH
   if bedingung:
       break  # Fehler! Kein break außerhalb von Schleifen
   ```

## 🔗 Weiter

[Lektion 3: Lists and List Processing](./lektion-3-lists.md)

