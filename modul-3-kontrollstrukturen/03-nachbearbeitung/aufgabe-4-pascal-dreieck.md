# Aufgabe 4: Pascal'sches Dreieck

**Zeitaufwand:** 1.5 Stunden
**Schwierigkeit:** ⭐⭐⭐ Schwer

## 🎯 Ziel

Erstellen Sie ein Programm, das das Pascal'sche Dreieck berechnet und formatiert ausgibt - **ohne Funktionen** zu verwenden.

## 📐 Was ist das Pascal'sche Dreieck?

Das Pascal'sche Dreieck ist ein mathematisches Zahlenschema:

```
        1
       1 1
      1 2 1
     1 3 3 1
    1 4 6 4 1
   1 5 10 10 5 1
```

**Regeln:**
- Jede Zeile beginnt und endet mit 1
- Jede andere Zahl ist die Summe der zwei Zahlen darüber
- Die n-te Zeile hat n Elemente

## 📝 Anforderungen

### Basis-Features (Pflicht)

1. **Benutzereingabe:**
   - Fragen Sie nach der Anzahl der Zeilen
   - Validieren Sie die Eingabe (1-15)

2. **Berechnung:**
   - Berechnen Sie jede Zeile basierend auf der vorherigen
   - Speichern Sie die Werte in einer Liste

3. **Ausgabe:**
   - Formatierte, zentrierte Darstellung
   - Alle Zahlen sichtbar

### Erweiterte Features (Optional)

4. **Zeilensummen:**
   - Zeigen Sie die Summe jeder Zeile an
   - (Tipp: Die Summe der n-ten Zeile ist 2^(n-1))

5. **Interaktives Menü:**
   - Mehrere Dreiecke generieren
   - Beenden-Option

6. **Schöne Formatierung:**
   - Dynamische Breite basierend auf grösster Zahl
   - Rahmen um das Dreieck

## 💡 Beispiel-Ablauf

```
=== PASCAL'SCHES DREIECK ===

Anzahl Zeilen (1-15): 6

           1
          1 1
         1 2 1
        1 3 3 1
       1 4 6 4 1
      1 5 10 10 5 1

Fertig! Das Dreieck hat 6 Zeilen.
```

### Mit Zeilensummen (Optional)

```
=== PASCAL'SCHES DREIECK ===

Anzahl Zeilen (1-15): 5

         1          | Summe: 1
        1 1         | Summe: 2
       1 2 1        | Summe: 4
      1 3 3 1       | Summe: 8
     1 4 6 4 1      | Summe: 16
```

## ✅ Checkliste

### Basis
- [ ] Eingabe wird validiert
- [ ] Dreieck wird korrekt berechnet
- [ ] Ausgabe ist zentriert
- [ ] Programm funktioniert für 1-15 Zeilen

### Erweitert
- [ ] Zeilensummen angezeigt
- [ ] Menü-System implementiert
- [ ] Schöne Formatierung

## 🎯 Lernziele

- Verschachtelte Listen (Liste von Listen)
- Zugriff auf vorherige Zeile
- String-Formatierung und Zentrierung
- Verschachtelte Schleifen
- Mathematische Muster erkennen

## 💻 Hilfe

### Grundstruktur (Pseudocode)

```
dreieck = []

für jede zeile von 0 bis n-1:
    neue_zeile = []

    für jede position von 0 bis zeile:
        wenn position == 0 oder position == zeile:
            wert = 1
        sonst:
            wert = vorherige_zeile[position-1] + vorherige_zeile[position]

        neue_zeile.append(wert)

    dreieck.append(neue_zeile)
```

### Liste von Listen

```python
# Erstellen
dreieck = []
dreieck.append([1])           # Erste Zeile
dreieck.append([1, 1])        # Zweite Zeile

# Zugriff auf vorherige Zeile
vorherige = dreieck[-1]       # Letzte Zeile
vorherige = dreieck[i - 1]    # Zeile vor i
```

### Zentrierte Ausgabe

```python
# Zeile als String
zeile_str = " ".join(str(x) for x in zeile)

# oder mit Schleife:
zeile_str = ""
for zahl in zeile:
    zeile_str += str(zahl) + " "

# Zentrieren
breite = 40
print(zeile_str.center(breite))
```

### Eingabe-Validierung

```python
while True:
    eingabe = input("Anzahl Zeilen (1-15): ")

    if not eingabe.isdigit():
        print("Bitte eine Zahl eingeben!")
        continue

    n = int(eingabe)

    if n < 1 or n > 15:
        print("Bitte eine Zahl zwischen 1 und 15!")
        continue

    break
```

## ⚠️ Wichtig

**Keine Funktionen verwenden!**

Dieses Programm soll nur mit den Konzepten aus Modul 1-3 gelöst werden:
- Variablen
- Listen
- Schleifen (for, while)
- Bedingungen (if, elif, else)
- Eingabe/Ausgabe

Funktionen werden erst in Modul 4 behandelt.

## 📦 Abgabe

**Datei:** `pascal_dreieck.py`

**Testen Sie mit:**
- 1 Zeile (nur eine 1)
- 5 Zeilen (Standard-Test)
- 10 Zeilen (grössere Zahlen)
- 15 Zeilen (Maximum)
- Ungültige Eingaben

## 🌟 Bonus-Ideen

- Fibonacci-Zahlen im Pascal-Dreieck finden (Diagonalen!)
- Gerade/ungerade Zahlen farblich markieren
- Das Dreieck in eine Datei speichern
- Binomialkoeffizienten berechnen (n über k)

## 🔗 Weiter

[Reflexion](./reflexion.md)
