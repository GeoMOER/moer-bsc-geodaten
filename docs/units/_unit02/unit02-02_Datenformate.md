---
title: Datentypen und -strukturen
published: true
toc: true
header:
  image: /assets/images/unit02/31031723265_0890cd9547_o.jpg
  image_description: "Cloudscape Over the Philippine Sea"
  caption: "Image: [NASA's Marshall Space Flight Center](https://www.nasa.gov/centers/marshall/home/index.html) [CC BY-NC 2.0] via [flickr.com](https://www.flickr.com/photos/nasamarshall/31031723265/)"
---
<!-- Themenblock 02-02: Datentypen, Encoding-Probleme, Tidy Data, Koordinatenformate (Basic) -->

Im letzten Kapitel haben Sie Ihre eigenen Klimadaten in Excel eingegeben. Nun müssen Sie verstehen, **wie Excel diese Daten intern behandelt** – denn nicht jede Zelle, die wie eine Zahl aussieht, wird von Excel auch als Zahl erkannt. Genau hier entstehen die häufigsten Fehlerquellen bei der Datenerfassung: falsch erkannte Datentypen, unsichtbare Zeichencodierungsprobleme, z.B. bei Ortsnamen, uneinheitlich strukturierte Koordinatenspalten und Einheiten, die versehentlich direkt mit in die Zahl geschrieben werden. Dieses Kapitel schafft die Grundlage, um solche Probleme künftig zu erkennen und zu vermeiden.

## Skalenniveau und Excel Zellformat

Um mit Daten sinnvoll zu arbeiten, müssen zwei unterschiedliche Ebenen auseinandergehalten werden:

1. **Skalenniveau** – eine statistische Eigenschaft der Variable selbst: Welche Vergleiche und Berechnungen sind inhaltlich überhaupt sinnvoll? Diese Eigenschaft hat nichts mit Excel zu tun, sie gilt unabhängig vom verwendeten Programm. In der Statistik wird "Datentyp" manchmal synonym zu "Skalenniveau" benutzt. 
2. **Excel-Zellformat** – wie Excel den Wert technisch speichert und anzeigt. Dieses Format entscheidet, ob Excel mit dem Wert rechnen kann.

Beide Ebenen hängen zusammen, sind aber nicht dasselbe: Eine Variable auf Verhältnisskala (z. B. Temperatur) kann in Excel trotzdem fälschlich als Text gespeichert sein – und wäre dann nicht rechenfähig, obwohl das Skalenniveau es erlauben würde.

### Skalenniveau

| Skalenniveau | Bedeutung | Beispiel aus unserem Datensatz |
|---|---|---|
| Nominal | Kategorie ohne Rangfolge | Standortname, Messmethode (Thermometer, Wetter-App) |
| Ordinal | Kategorie *mit* sinnvoller Rangfolge, aber ohne gleichmäßige Abstände | *(kommt in unserem bisherigen Datensatz nicht vor)* – z. B. Bewölkungsgrad (klar < leicht bewölkt < bewölkt < bedeckt), falls Sie diesen zusätzlich erheben würden |
| Intervall | Numerisch, gleiche Abstände vergleichbar, aber **kein echter Nullpunkt** | Temperatur in °C, Uhrzeit |
| Verhältnis (Ratio) | Numerisch, **echter Nullpunkt** vorhanden, auch Verhältnisse sinnvoll interpretierbar | Luftdruck (hPa), Distanz/Höhe |

> Was ist ein echter Nullpunkt? Beispiel Temperaturmessung in °C - `0 °C` bedeutet nicht "keine Temperatur", sondern ist ein willkürlich gesetzter Nullpunkt (Gefrierpunkt von Wasser). Deshalb gilt: Eine **Differenz** ist sinnvoll interpretierbar (`10 °C – 5 °C = 5 °C` Unterschied), ein **Verhältnis** dagegen nicht (`10 °C` ist nicht "doppelt so warm" wie `5 °C`). Für die Kelvin-Skala hingegen, die einen echten Nullpunkt hat (absoluter Nullpunkt), wären Verhältnisse sinnvoll. Für unsere Zwecke reicht es zu wissen: Mittelwert und Differenz von Temperaturen sind erlaubt, direkte Verhältnisaussagen ("doppelt so warm") sind es nicht.


### Excel-Zellformat

| Zellformat | Bedeutung | Rechenfähig? |
|---|---|---|
| Standard | Excel erkennt den Datentyp automatisch (Zahl, Text, Datum) | abhängig von der Erkennung |
| Zahl | fester numerischer Wert, mit definierbarer Nachkommastellenzahl | ja |
| Datum/Uhrzeit | intern als fortlaufende Zahl gespeichert (Tage bzw. Bruchteile eines Tages) | ja (z. B. Datumsdifferenz) |
| Text | Zeichenkette, kein numerischer Wert | nein |
| Benutzerdefiniert | frei definierbares Anzeigeformat auf Basis eines Zahl- oder Datumswerts | ja (Wert bleibt Zahl, nur Anzeige ändert sich) |

### Wie beide Ebenen zusammenhängen

| Skalenniveau | Sinnvolles Excel-Zellformat | Beispiel |
|---|---|---|
| Nominal | Text | Standortname |
| Ordinal | Text (ggf. mit benutzerdefinierter Sortierreihenfolge) oder Zahl als Rang-Code | Bewölkungsgrad, falls erhoben |
| Intervall | Zahl bzw. Datum/Uhrzeit | Temperatur, Uhrzeit |
| Verhältnis | Zahl | Luftdruck |

Wichtig: Excel „kennt" das Skalenniveau nicht – es unterscheidet nur zwischen Zahl, Text und Datum. Ob eine Zahl auf Intervall- oder Verhältnisskala liegt (also ob z. B. Verhältnisaussagen erlaubt sind), müssen **Sie** wissen und bei der Interpretation der Ergebnisse berücksichtigen – Excel würde eine Verhältnisrechnung mit Temperaturwerten in °C anstandslos ausführen, obwohl sie inhaltlich falsch ist.

### Besonderheiten 

**Datum/Uhrzeit ist Intervallskala – aber technisch trotzdem eine Zahl.**
Excel speichert ein Datum intern als fortlaufende Zahl (Anzahl Tage seit dem 01.01.1900), eine Uhrzeit als Dezimalbruch eines Tages. Deshalb lassen sich Datumsdifferenzen problemlos berechnen (`Datum2 - Datum1` ergibt die Anzahl Tage dazwischen) – ein "Verhältnis zweier Daten" wäre aber inhaltlich sinnlos.

**Latitude/Longitude sind ein Grenzfall.**
Der Nullpunkt (Äquator bzw. Nullmeridian) ist eine willkürliche, aber feste Referenz – das spricht für Intervallskala. In der Praxis werden Koordinaten trotzdem meist wie Verhältnisskala behandelt, weil mit ihnen Distanzen berechnet werden. Wie wir sie genau formatieren können, werden wir am Ende dieser Unit behandeln.

**Nur weil eine Zahl auf Verhältnisskala liegt, erkennt Excel sie nicht automatisch als rechenfähig.**
Wenn Ihre Luftdruckwerte z. B. beim Import aus einer CSV-Datei als Text erkannt wurden (`"1013,2"` statt `1013,2`), müssen Sie diese erst in eine echte Zahl umwandeln – unabhängig davon, dass Luftdruck vom Skalenniveau her problemlos rechenfähig wäre.

Deswegen gilt: Einheiten werden **nicht** direkt mit in die Zelle geschrieben, z. B. `8,4` statt `8,4 °C`, da ansonsten der **Zahlencharakter der Zelle** zerstört wird. Excel behandelt den Zellinhalt dann als Text, und es kann nicht mehr gerechnet werden: Aus einer Spalte mit `8,4 °C`, `6,1 °C`, `9,0 °C` lässt sich kein Mittelwert bilden. Natürlich müssen Sie festhalten, in welcher Einheit der Wert gemessen wurde - doch darum kümmern wir uns später in der Unit X

> **Grundregel:** Quantitative Daten werden **immer ohne Einheitssymbol** gespeichert. Die Einheit ist Information über die Spalte (gehört z. B. in die Überschrift, etwa `Temperatur (°C)`, wie Sie es bereits gemacht haben), nicht Teil des einzelnen Zahlenwerts. Wollen Sie die Einheit trotzdem direkt neben jedem einzelnen Wert anzeigen, ohne die Rechenfähigkeit zu verlieren, nutzen Sie ein **benutzerdefiniertes Zellformat**.
### Kurzanleitung: Zellen benutzerdefiniert formatieren

**So wenden Sie ein benutzerdefiniertes Format an:**

1. Zelle(n) markieren, die formatiert werden sollen
2. `Strg` + `1` drücken (öffnet den Dialog „Zellen formatieren") – oder Rechtsklick → „Zellen formatieren…"
3. Im Reiter „Zahlen" die Kategorie **„Benutzerdefiniert"** auswählen (meist unterster Eintrag in der Liste)
4. Im Feld „Typ" den gewünschten Formatcode eingeben (siehe Beispiele unten)
5. Vorschau rechts im Dialog prüfen – zeigt bereits, wie der aktuelle Zellwert aussehen würde
6. Mit „OK" bestätigen


<!-- **Screenshot 7:** Geöffneter Dialog „Zellen formatieren“ auf dem Reiter „Zahlen“, Kategorie „Benutzerdefiniert“ markiert, im Eingabefeld ein Beispiel-Format wie `0" °C"`, rechts die Live-Vorschau des formatierten Werts. -->


### Benutzerdefinierte Formate – zwei Beispiele aus unserem Datensatz

**1. Einheit anzeigen, Zahl bleibt Zahl:**
Format `0" °C"` zeigt den Wert `8,4` als `8,4 °C` an – gerechnet wird aber weiterhin mit der reinen Zahl `8,4`.

**2. Führende Nullen erzwingen:**
Format `00` zeigt den Wert `1` in einer Spalte `Unit` als `01` an, `12` bleibt `12`. Der gespeicherte Wert ist weiterhin die Zahl `1`, nur die Anzeige ändert sich – nützlich z. B. bei fortlaufender Messungsnummerierung.

**Tipp:** Ein einmal erstelltes Format lässt sich mit dem **Format-Übertragen-Pinsel** (Start → Zwischenablage → Pinsel-Symbol) schnell auf weitere Zellen oder Spalten übertragen, ohne den Dialog erneut zu öffnen.

---

## Übung: Units und Zellformate in den Klimadaten

Nutzen Sie Ihre Excel-Datei mit den Klimadaten (bzw. die im letzten Kapitel zusammengeführte Tabelle mit den zusätzlichen Messungen Ihrer Kommiliton:innen).

1. Ergänzen Sie, falls noch nicht vorhanden, ganz links eine Spalte **„ID“** mit fortlaufender Nummerierung Ihrer Messungen (1, 2, 3, …).
2. Formatieren Sie **die IDs** so, dass einstellige Zahlen zweistellig angezeigt werden (aus „1“ soll „01“ werden, aus „2“ „02“, aus „3“ „03“).
   - *Hinweis:* Excel verwendet standardmäßig den Zellentyp „Zahl“, führende Nullen werden dabei automatisch entfernt. Lösen Sie die Aufgabe **nicht** durch Eingabe von Text (also nicht `'01`), sondern über ein passendes **Zahlenformat**.
3. Prüfen Sie in der Bearbeitungsleiste (bei markierter Zelle), welcher Wert tatsächlich gespeichert ist – unterscheidet sich der gespeicherte Wert von der Anzeige in der Zelle?
4. Sorgen Sie dafür, dass **hinter jedem Temperatur-Wert** dieser Spalte automatisch `°C` angezeigt wird – der Zellinhalt soll aber eine **echte Zahl** bleiben, mit der weitergerechnet werden kann.
   - *Hinweis:* Nutzen Sie dafür ein benutzerdefiniertes Zellformat, **nicht** die Einheit direkt im Zelltext oder nur in der Überschrift.
6. Übertragen Sie das neu erstellte Format mit dem **Pinsel** auf alle weiteren Zellen der Spalte, ohne den Dialog erneut zu öffnen.
7. Speichern Sie Ihre Datei abschließend.