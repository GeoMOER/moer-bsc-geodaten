---
title: Überblick
published: true
toc: true
header:
  image: /assets/images/spotlight01/jekyll_github_pages.png
  image_description: "Cutout from Measured carbon dioxide concentrations in Vancouver"
  caption: "Bild: [jekyll](https://jekyllrb.com/)"
---
---
title: ÜA | Übungsaufgabe Abschnitt 02
published: true
toc: true
header:
  image: /assets/images/01-splash.jpg
  image_description: "Dr. John Snow's map"
  caption: "Map: [**Dr. John Snow**](https://en.wikipedia.org/wiki/John_Snow) [Wellcome Library via wikimedia](https://w.wiki/QtV)"
---

<!-- Übungsaufgabe 02: Excel-Grundlagen, Datentypen, Zellformate, Textfunktionen, Import/Export -->
## Übungsaufgabe 02

In dieser Übungsaufgabe wenden Sie das Gelernte aus Lernabschnitt 02 selbstständig an. Grundlage sind zwei neue, eigenständige Dateien – nicht identisch mit den Übungsdatensätzen aus dem Kurs, aber aus denselben echten Sensordaten:

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

<!-- Lernziele: Was sollten Studierende am Ende dieser Lerneinheit wissen und anwenden können? -->

## Lernziele

Am Ende dieser Unit sind Studierende in der Lage, ...

* Geodaten von nicht räumlich referenzierten Daten zu unterscheiden,
* den Raumbezug einfacher Datensätze zu erkennen und zu beschreiben,
* geographische Koordinaten als Längen- und Breitengrad zu lesen,
* die Reihenfolge und Einheit von Koordinatenangaben zu überprüfen,
* den Unterschied zwischen geographischen und projizierten Koordinatensystemen grundlegend zu erklären,
* zu erläutern, warum Kartenprojektionen zu Verzerrungen führen,
* die Bedeutung eines Koordinatenreferenzsystems und eines EPSG-Codes für die Arbeit mit Geodaten zu beschreiben und
* typische Probleme durch fehlende oder falsch zugewiesene Koordinatenreferenzsysteme zu erkennen.

<!-- Organisatorisches: Gibt es Formalitäten, welche noch geklärt werden sollten? -->

## Organisatorisches

Für diese Lerneinheit sind keine zusätzlichen organisatorischen Vorbereitungen erforderlich. Bitte bringen Sie offene Fragen aus den vorherigen Kurssitzungen mit.

<!-- Notizen: Ab hier folgen Vermerke, welche als Gedankenstütze oder Erinnerung dienen aber noch nicht in der vorhandenen Form veröffentlicht werden sollen. -->

<!--
Mögliche Einstiegsfrage: Was bedeuten die beiden Zahlen 50.8 und 8.8 – und reichen sie aus, um einen Ort eindeutig zu beschreiben?

Mögliche Demonstrationen:
- Marburg in geographischen Koordinaten lokalisieren
- dieselbe Position in WGS 84 und UTM vergleichen
- Verzerrungen verschiedener Weltkarten gegenüberstellen
- einen Datensatz mit falsch zugewiesenem CRS zeigen

Geplante Unterseiten:
- unit09-01_geodaten.html
- unit09-02_koordinaten.html
- unit09-03_projektionen.html
-->