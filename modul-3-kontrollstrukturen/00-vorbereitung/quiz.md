# Quiz: Selbsttest Modul 3

**Zeitaufwand:** 15-30 Minuten  
**Bestehensgrenze:** 7 von 10 Punkten  
**Themen:** Boolean Values, Conditionals, Loops, Lists, Logical Operators

> **Hinweis:** Versuchen Sie zuerst alle Fragen zu beantworten, bevor Sie die Lösungen ansehen!

---

## Frage 1: Boolean Values

Was ist das Ergebnis dieses Ausdrucks?

```python
ergebnis = (10 > 5) and (3 < 2)
print(ergebnis)
```

- [ ] A) `True`
- [ ] B) `False`
- [ ] C) `10`
- [ ] D) Fehler

---

## Frage 2: If-Elif-Else

Was gibt dieser Code aus?

```python
punkte = 75

if punkte >= 90:
    print("A")
elif punkte >= 80:
    print("B")
elif punkte >= 70:
    print("C")
else:
    print("D")
```

- [ ] A) `A`
- [ ] B) `B`
- [ ] C) `C`
- [ ] D) `D`

---

## Frage 3: While-Schleife

Wie oft wird "Hallo" ausgegeben?

```python
zaehler = 3
while zaehler > 0:
    print("Hallo")
    zaehler -= 1
```

- [ ] A) 0 mal
- [ ] B) 1 mal
- [ ] C) 2 mal
- [ ] D) 3 mal

---

## Frage 4: For-Schleife mit range()

Was gibt dieser Code aus?

```python
for i in range(2, 5):
    print(i)
```

- [ ] A) `2 3 4 5`
- [ ] B) `2 3 4`
- [ ] C) `1 2 3 4`
- [ ] D) `0 1 2 3 4`

---

## Frage 5: Listen - Indexing

Was ist der Wert von `x`?

```python
fruechte = ["Apfel", "Banane", "Orange"]
x = fruechte[-1]
```

- [ ] A) `"Apfel"`
- [ ] B) `"Banane"`
- [ ] C) `"Orange"`
- [ ] D) Fehler

---

## Frage 6: List Methods

Was enthält die Liste nach diesem Code?

```python
zahlen = [1, 2, 3]
zahlen.append(4)
zahlen.insert(0, 0)
```

- [ ] A) `[1, 2, 3, 4, 0]`
- [ ] B) `[0, 1, 2, 3, 4]`
- [ ] C) `[1, 2, 3, 0, 4]`
- [ ] D) `[4, 0, 1, 2, 3]`

---

## Frage 7: Break Statement

Was gibt dieser Code aus?

```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

- [ ] A) `0 1 2 3 4`
- [ ] B) `0 1 2 3`
- [ ] C) `0 1 2`
- [ ] D) `0 1 2 4`

---

## Frage 8: Continue Statement

Was gibt dieser Code aus?

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

- [ ] A) `0 1 2 3 4`
- [ ] B) `0 1 3 4`
- [ ] C) `0 1`
- [ ] D) `3 4`

---

## Frage 9: Logische Operatoren

Was ist das Ergebnis?

```python
a = True
b = False
ergebnis = a or b and not a
print(ergebnis)
```

- [ ] A) `True`
- [ ] B) `False`
- [ ] C) Fehler
- [ ] D) `None`

---

## Frage 10: Listen durchlaufen

Wie viele Zahlen werden ausgegeben?

```python
zahlen = [1, 2, 3, 4, 5]
for zahl in zahlen:
    if zahl % 2 == 0:
        print(zahl)
```

- [ ] A) 0
- [ ] B) 2
- [ ] C) 3
- [ ] D) 5

---

## 📝 Lösungen

<details>
<summary>Klicken Sie hier für die Lösungen (erst nach dem Versuch!)</summary>

### Antworten:

1. **B) `False`**  
   Erklärung: `(10 > 5)` ist `True`, aber `(3 < 2)` ist `False`. `True and False` ergibt `False`.

2. **C) `C`**  
   Erklärung: 75 ist >= 70, also wird "C" ausgegeben.

3. **D) 3 mal**  
   Erklärung: Die Schleife läuft bei zaehler = 3, 2, 1 (3 Durchläufe).

4. **B) `2 3 4`**  
   Erklärung: `range(2, 5)` erzeugt 2, 3, 4 (5 ist exklusiv).

5. **C) `"Orange"`**  
   Erklärung: Index -1 gibt das letzte Element zurück.

6. **B) `[0, 1, 2, 3, 4]`**  
   Erklärung: `append(4)` fügt 4 am Ende hinzu, `insert(0, 0)` fügt 0 am Anfang ein.

7. **C) `0 1 2`**  
   Erklärung: Bei i=3 wird die Schleife mit `break` beendet.

8. **B) `0 1 3 4`**  
   Erklärung: Bei i=2 wird mit `continue` übersprungen, die anderen werden ausgegeben.

9. **A) `True`**  
   Erklärung: `and` hat höhere Priorität als `or`. `b and not a` = `False and False` = `False`. `a or False` = `True`.

10. **B) 2**  
    Erklärung: Nur 2 und 4 sind gerade Zahlen (durch 2 teilbar ohne Rest).

</details>

---

## ✅ Auswertung

Zählen Sie Ihre richtigen Antworten:

- **10 Punkte:** Ausgezeichnet! Sie sind bestens vorbereitet! 🌟
- **7-9 Punkte:** Sehr gut! Sie können am Präsenztag teilnehmen. ✅
- **4-6 Punkte:** Wiederholen Sie den Leseauftrag und die Experimente. 📚
- **0-3 Punkte:** Arbeiten Sie CISCO NetAcad Kapitel 3 nochmals durch. ⚠️

## 🔗 Weiter

Wenn Sie mindestens 7 Punkte erreicht haben, sind Sie bereit für den Präsenztag!  
Ansonsten wiederholen Sie:
- [Leseauftrag](./leseauftrag.md)
- [Erste Experimente](./erste-experimente.md)
- CISCO NetAcad Kapitel 3.1-3.7

