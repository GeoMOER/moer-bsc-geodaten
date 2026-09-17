---
title: ÜA | Übungsaufgabe Abschnitt 03
published: true
toc: true
header:
  image: /assets/images/01-splash.jpg
  image_description: "Dr. John Snow's map"
  caption: "Map: [**Dr. John Snow**](https://en.wikipedia.org/wiki/John_Snow) [Wellcome Library via wikimedia](https://w.wiki/QtV)"
---

<!-- Übungsaufgabe 03: Excel-Grundlagen, Datentypen, Zellformate, Textfunktionen, Import/Export -->
## Übungsaufgabe 03

In dieser Übungsaufgabe wenden Sie das Gelernte aus Lernabschnitt 03 selbstständig an. Grundlage sind zwei neue, eigenständige Dateien – nicht identisch mit den Übungsdatensätzen aus dem Kurs, aber aus denselben echten Sensordaten:

* `Abschlusstest_Datensatz.xlsx` (Tabellenblatt „Testdaten")
* `Abschlusstest_Import_roh.csv`

Beantworten Sie die folgenden 15 Fragen, indem Sie die jeweils beschriebene Bearbeitung tatsächlich in Excel durchführen.

---

**1.** Öffnen Sie `Abschlusstest_Datensatz.xlsx` und springen Sie mit `Strg`+`Ende` zur letzten benutzten Zelle. In welcher Zeile befindet sich diese?

**2.** Auf welchem Skalenniveau liegt die Variable `Standort`?

**3.** Auf welchem Skalenniveau liegt die Variable `Temperatur`?

**4.** Auf welchem Skalenniveau liegt die Variable `Datum`?

**5.** Fügen Sie ganz links eine Spalte `ID` mit fortlaufender Nummerierung (1, 2, 3, …) ein und formatieren Sie sie mit dem benutzerdefinierten Format `00`. Wie wird der Wert der zweiten Datenzeile angezeigt?

**6.** Formatieren Sie die Spalte `Temperatur` mit dem benutzerdefinierten Format `0,0" °C"`. Wie wird der Wert in Zeile 8 danach angezeigt?

**7.** Geben Sie in eine leere Zelle `+49` ein (ohne Hochkomma). Was passiert, und warum?

**8.** Extrahieren Sie mit `TEIL` und `FINDEN` den Gradanteil der Latitude aus `Koordinaten_roh` in Zeile 5. Welcher Wert kommt heraus?

**9.** Extrahieren Sie auf dieselbe Weise den Minutenanteil der Longitude aus Zeile 5. Welcher Wert kommt heraus?

**10.** In welcher Zeile der Spalte `Koordinaten_roh` liegt ein Formatfehler vor (Hochkomma `'` anstelle des Anführungszeichens `"`)?

**11.** Wozu dient die Funktion `WERT`, und was würde ohne sie bei den Ergebnissen aus Frage 8/9 fehlen?

**12.** Importieren Sie `Abschlusstest_Import_roh.csv` über „Daten → Aus Text/CSV". Welche Zeichenkodierung müssen Sie wählen, damit „Schloßpark" korrekt angezeigt wird?

**13.** Welches Datum steht nach korrektem Import in Zeile 4 (Format TT.MM.JJJJ)?

**14.** Welches Zeichen trennt die Spalten in `Abschlusstest_Import_roh.csv`?

**15.** Warum ist eine `.xlsx`-Datei bei identischem Inhalt in der Regel größer als eine vergleichbare `.csv`-Datei?

<!-- Musterlösung (nicht für Studierende sichtbar):
1. Zeile 22
2. Nominal
3. Intervall
4. Intervall
5. 02
6. 24,9 °C
7. Excel interpretiert die Eingabe als Formelbeginn / Fehler, da "+" ein Rechenzeichen ist; mit vorangestelltem Hochkomma würde es als Text erkannt
8. 50
9. 46
10. Zeile 14
11. Wandelt Text in eine echte, rechenfähige Zahl um; ohne WERT bliebe das Ergebnis von TEIL immer Text, rechtsbündig waere es trotzdem nicht rechenfaehig
12. Windows-1252 (ANSI)
13. 12.03.2026
14. Semikolon
15. xlsx enthält zusätzlich Formatierung, Metadaten, mehrere Tabellenblätter etc., während CSV nur die reinen Werte speichert
-->
