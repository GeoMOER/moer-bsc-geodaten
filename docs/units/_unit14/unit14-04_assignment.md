---
title: HA | Hausaufgabe Abschnitt 14
published: true
toc: true
header:
  image: /assets/images/unit14/hero-unit14.jpg
  image_description: "Workflow von der Fragestellung zur dokumentierten Karte"
  caption: "Eigene Darstellung"
---

<!-- Hausaufgabe 14: Integrierter Geo-Workflow und Abschlusskarte -->

## Hausaufgabe 14

In dieser Abschlussaufgabe verbinden Sie die Inhalte der Units 09–14 zu einem vollständigen kleinen Geo-Workflow. Sie wählen und prüfen Geodaten, vergleichen Klassifizierungen, gestalten ein Kartenlayout und dokumentieren Ihre räumliche Aussage einschließlich ihrer Grenzen.

| Rahmenbedingung | Festlegung |
|---|---|
| Bearbeitungszeit | etwa 180 Minuten |
| Abgabeformat | vollständiger Arbeitsordner als `unit14_nachname_vorname.zip` |
| Abgabeort | `[ILIAS-Ordner beziehungsweise Abgabeort ergänzen]` |
| Abgabetermin | `[Datum und Uhrzeit ergänzen]` |
| Arbeitsform | Einzelarbeit; ein Peer-Feedback vor der finalen Überarbeitung ist ausdrücklich erlaubt. |

## Fragestellung

Erstellen Sie eine Karte zur Frage:

> **Wie verteilen sich die dokumentierten Beobachtungen einer Art im Untersuchungsgebiet, und in welchen Höhenlagen liegen sie?**

Die Karte richtet sich an fachlich interessierte Personen ohne genaue Kenntnis des Datensatzes. Sie muss deshalb ohne zusätzliche mündliche Erklärung verständlich sein.

## Benötigte Daten

Verwenden Sie mindestens:

* `unit13_results.gpkg/gbif_mit_hoehe` mit dem numerischen Feld `hoehe_m` oder den schemaidentischen Ersatzlayer,
* das bereitgestellte digitale Geländemodell und
* eine Grenze des Untersuchungsgebiets oder einen anderen begründeten räumlichen Kontextlayer.

Optional können Schutzgebiete, Gewässer oder eine Hintergrundkarte ergänzt werden. Jeder sichtbare Layer muss zur Fragestellung oder Orientierung beitragen.

Falls Ihre eigenen Ergebnisse aus den vorherigen Units fehlen, verwenden Sie die bereitgestellten Ersatzdaten.

| Verbindliche Angabe | Festlegung |
|---|---|
| QGIS-Version | `[dieselbe verbindliche QGIS-LTR-Version wie in Unit 10 ergänzen]` |
| Ersatzdatenpaket | `[Downloadlink ergänzen]` |
| Untersuchungsgebiet und Zeitraum | `[ergänzen]` |
| Seitenformat | `[zum Beispiel A4 quer ergänzen]` |
| PNG-Auflösung | `[zum Beispiel 300 dpi ergänzen]` |
| DGM im finalen Layout | `[verbindlich sichtbar oder nur als Analysequelle festlegen]` |

## 1. Arbeitsumgebung vorbereiten

Erstellen Sie diese Ordnerstruktur:

```text
hausaufgabe14/
  data_raw/
  data_intermediate/
  data_output/
  documentation/
  figures/
```

Speichern Sie Ihr QGIS-Projekt als:

```text
hausaufgabe14.qgz
```

Verwenden Sie das seit Unit 10 eingesetzte Projekt-CRS: **`[EPSG-Code ergänzen; für Marburg voraussichtlich EPSG:25832]`**.

## 2. Aussage und Zielgruppe festlegen

Füllen Sie vor der Gestaltung diese Tabelle aus:

| Entscheidung | Festlegung |
|---|---|
| Art oder Taxon | `[eintragen]` |
| Untersuchungsgebiet | `[eintragen]` |
| Beobachtungszeitraum | `[eintragen]` |
| Zielgruppe | `[eintragen]` |
| Hauptaussage der Karte | `[eintragen]` |
| geplantes Seitenformat | `[eintragen]` |

Formulieren Sie die Aussage so, dass dokumentierte Beobachtungen nicht mit der vollständigen Verbreitung der Art gleichgesetzt werden.

## 3. Dateninventar und Eingangskontrolle

Dokumentieren Sie alle verwendeten Layer:

| Layer | Quelle/Herausgeber | Datenstand | Datenmodell | CRS | relevante Werte/Felder | Lizenz |
|---|---|---|---|---|---|---|
| `[eintragen]` | `[eintragen]` | `[eintragen]` | `[eintragen]` | `[eintragen]` | `[eintragen]` | `[eintragen]` |

Prüfen Sie mindestens:

* räumliche Ausdehnung,
* Geometrie- oder Rastertyp,
* CRS,
* Featurezahl beziehungsweise Rastergröße,
* Höhenfeld und Einheit,
* fehlende Höhenwerte,
* DGM-Zellgröße und NoData,
* Datenstand und Lizenz.

Notieren Sie gefundene Probleme und Ihre Entscheidung dazu.

## 4. Hauptlayer vorbereiten

Verwenden Sie einen Punktlayer, der für jede gültige Beobachtung einen Geländehöhenwert enthält.

Falls dieser noch nicht vorliegt:

1. prüfen Sie die GBIF-Punkte,
2. tasten Sie das DGM mit **Rasterwerte abtasten** ab,
3. verwenden Sie das Präfix `hoehe_`,
4. speichern Sie das Ergebnis in:

   ```text
   data_output/unit14_results.gpkg
   ```

5. nennen Sie den Layer:

   ```text
   gbif_mit_hoehe_final
   ```

Liegt bereits ein geprüfter Ergebnislayer vor, kopieren oder exportieren Sie ihn unter diesem eindeutigen Namen in das Abgabe-GeoPackage.

Dokumentieren Sie:

| Kontrolle | Ergebnis |
|---|---:|
| Beobachtungspunkte insgesamt | `[eintragen]` |
| Punkte mit gültigem Höhenwert | `[eintragen]` |
| Punkte ohne gültigen Höhenwert | `[eintragen]` |
| Höhenminimum | `[eintragen]` |
| Höhenmaximum | `[eintragen]` |
| verwendete Einheit | `[eintragen]` |

## 5. Zwei Klassifizierungen vergleichen

Stellen Sie den Punktlayer anhand des Höhenfeldes abgestuft dar. Vergleichen Sie mindestens zwei Methoden:

* gleiche Intervalle und
* Quantile.

Optional können Sie zusätzlich natürliche Unterbrechungen prüfen.

Verwenden Sie zunächst dieselbe Klassenzahl und Farbpalette, damit der Einfluss der Methode erkennbar bleibt.

| Methode | Zahl der Klassen | Klassengrenzen | Features je Klasse | Wirkung |
|---|---:|---|---|---|
| gleiche Intervalle | `[eintragen]` | `[eintragen]` | `[eintragen]` | `[eintragen]` |
| Quantile | `[eintragen]` | `[eintragen]` | `[eintragen]` | `[eintragen]` |
| optional: Natural Breaks | `[eintragen]` | `[eintragen]` | `[eintragen]` | `[eintragen]` |

Entscheiden Sie sich für eine Variante und begründen Sie in drei bis fünf Sätzen:

1. Warum beantwortet sie die Fragestellung besser?
2. Welche Wirkung besitzen ihre Klassengrenzen?
3. Welche Einschränkung hat die gewählte Methode?

## 6. Symbolisierung und visuelle Hierarchie

Gestalten Sie die Karte so, dass die Beobachtungen und ihre Höhenklassen zuerst auffallen.

Anforderungen:

* sequentielle, gut unterscheidbare Farbpalette für die Höhenklassen,
* verständliche und gerundete Klassenbezeichnungen mit Einheit,
* DGM gemäß der verbindlichen Vorgabe entweder als zurückhaltender Kontext oder ausschließlich als dokumentierte Analysequelle,
* Untersuchungsgebiets- oder Schutzgebietsgrenzen ohne verdeckende Füllung,
* optionale Gewässer oder Hintergrundkarte nur bei erkennbarem Mehrwert,
* keine unnötigen Beschriftungen oder Layer.

Dokumentieren Sie jede sichtbare Ebene:

| Layer | Rolle | Symbolisierung | Begründung |
|---|---|---|---|
| `[eintragen]` | `[eintragen]` | `[eintragen]` | `[eintragen]` |

## 7. Kartenlayout erstellen

Erstellen Sie ein Layout im festgelegten Seitenformat.

Es muss enthalten:

* einen passenden Kartenausschnitt,
* einen aussagekräftigen Titel,
* eine fachlich überarbeitete Legende,
* eine geeignete Maßstabsangabe,
* Datenquellen, Datenstände und notwendige Lizenzhinweise,
* Name beziehungsweise Bearbeitungshinweis und Datum.

Ein Nordpfeil, Koordinatengitter oder eine Übersichtskarte wird nur ergänzt, wenn Sie den Nutzen begründen können.

Der Titel darf nicht behaupten, die vollständige Artverbreitung zu zeigen.

## 8. Karte exportieren und prüfen

Exportieren Sie das Layout als:

```text
figures/abschlusskarte_unit14.pdf
figures/abschlusskarte_unit14.png
```

Verwenden Sie für die PNG-Datei die vorgegebene Auflösung: **`[Auflösung ergänzen, zum Beispiel 300 dpi]`**.

Öffnen Sie beide Dateien außerhalb von QGIS und prüfen Sie:

* Sind alle Elemente vollständig sichtbar?
* Ist die Schrift bei normaler Ansicht lesbar?
* Stimmen Farben und Klassen mit der Legende überein?
* Sind Einheit und Datenquellen erkennbar?
* Bleibt die Hauptaussage klar?

Dokumentieren Sie mindestens eine Änderung, die Sie nach der Exportkontrolle vorgenommen haben. Falls keine Änderung nötig war, benennen Sie den besonders geprüften Aspekt.

## 9. Ergebnis interpretieren

Verfassen Sie einen kurzen Ergebnistext von etwa **150 bis 250 Wörtern**. Gehen Sie ein auf:

1. räumliche Verteilung der dokumentierten Beobachtungen,
2. häufige und seltene Höhenklassen,
3. mögliche auffällige Einzelbeobachtungen,
4. Bedeutung der gewählten Klassifizierung,
5. mindestens drei Unsicherheiten oder Einschränkungen,
6. eine Aussage, die aus der Karte ausdrücklich nicht abgeleitet werden kann.

Unterscheiden Sie klar zwischen:

* dem sichtbaren Muster,
* einer möglichen fachlichen Erklärung und
* einer durch die Daten tatsächlich belegten Aussage.

## 10. Workflow dokumentieren

Erstellen Sie:

```text
documentation/processing_notes.md
```

Die Datei soll enthalten:

```markdown
# Fragestellung und Zielgruppe

# Datenquellen und Lizenzen

# Eingangskontrolle

# Auswahl und Verarbeitung

# Symbolisierung

# Vergleich der Klassifizierungen

# Gewählte Klassifizierung und Begründung

# Kartenlayout und Export

# Ergebnisse

# Unsicherheiten

# Bearbeitungsdatum
```

Nennen Sie die verwendeten QGIS-Werkzeuge und wichtigen Parameter so, dass der Workflow grundsätzlich nachvollzogen werden kann.

## 11. Selbstkontrolle

Beantworten Sie vor der Abgabe mit ja oder nein:

| Prüffrage | Antwort |
|---|---|
| Beantwortet die Karte die festgelegte Frage? | ja / nein |
| Ist die Hauptinformation innerhalb weniger Sekunden erkennbar? | ja / nein |
| Werden dokumentierte Beobachtungen korrekt bezeichnet? | ja / nein |
| Sind Klassen, Grenzen und Einheit verständlich? | ja / nein |
| Sind alle sichtbaren Layer notwendig? | ja / nein |
| Sind Quellen und Datenstände vollständig? | ja / nein |
| Ist die Karte in Ausgabegröße lesbar? | ja / nein |
| Sind Verarbeitung und Unsicherheiten dokumentiert? | ja / nein |

Überarbeiten Sie alle Punkte, die Sie mit **nein** beantworten.

## Abgabe

Geben Sie den vollständigen Ordner `hausaufgabe14/` als `unit14_nachname_vorname.zip` ab. Er soll mindestens enthalten:

* `hausaufgabe14.qgz`,
* `data_output/unit14_results.gpkg` mit `gbif_mit_hoehe_final`,
* `figures/abschlusskarte_unit14.pdf`,
* `figures/abschlusskarte_unit14.png`,
* `documentation/processing_notes.md`,
* die ausgefüllten Tabellen,
* die Begründung der Klassifizierung und
* den Ergebnistext.

Kontrollieren Sie vor der Abgabe, ob sich das QGIS-Projekt öffnen lässt und keine Dateien ausschließlich über nicht mehr erreichbare absolute Pfade eingebunden sind.

## Bewertungskriterien

| Kriterium | Erwartung |
|---|---|
| Fragestellung | präzise, beantwortbar und korrekt auf Beobachtungsdaten bezogen |
| Dateninventar | Quellen, Datenstände, CRS, Einheiten und Lizenzen vollständig |
| Eingangskontrolle | Punkt-, Raster- und Kontextdaten nachvollziehbar geprüft |
| Klassifizierungsvergleich | mindestens zwei Methoden korrekt verglichen |
| Methodenwahl | verständlich und fachlich begründet |
| Symbolisierung | passend zu Datenart und klar hierarchisiert |
| Kartenlayout | vollständig, übersichtlich und in Ausgabegröße lesbar |
| Quellenangabe | Datenherkunft und Bearbeitung direkt auf der Karte erkennbar |
| Interpretation | Muster korrekt beschrieben und nicht überinterpretiert |
| Unsicherheit | mindestens drei relevante Einschränkungen reflektiert |
| Reproduzierbarkeit | Projekt, Daten, Parameter und Entscheidungen geordnet dokumentiert |

## Punkteverteilung

| Bereich | Punkte |
|---|---:|
| Fragestellung, Zielgruppe und Dateninventar | 10 |
| Eingangskontrolle und Verarbeitung | 10 |
| Klassifizierungsvergleich und Methodenwahl | 15 |
| Symbolisierung und visuelle Hierarchie | 15 |
| Layout, Quellenangabe und Exportprüfung | 20 |
| Interpretation und Unsicherheiten | 20 |
| Reproduzierbarkeit und vollständige Abgabe | 10 |

Gesamt: **100 Punkte**. Für das Bestehen sind **`[Mindestpunktzahl ergänzen, Vorschlag: 50 von 100 Punkten]`** erforderlich. Kartographische Alternativen sind zulässig, wenn sie zur Datenart, Leitfrage und Zielgruppe passen und nachvollziehbar begründet werden. Folgefehler werden nicht mehrfach bewertet.

## Checkliste

- [ ] Fragestellung und Zielgruppe festgelegt
- [ ] Dateninventar vollständig
- [ ] Eingangsdaten kontrolliert
- [ ] finaler Punktlayer im GeoPackage gespeichert
- [ ] mindestens zwei Klassifizierungen verglichen
- [ ] Methodenwahl begründet
- [ ] visuelle Hierarchie hergestellt
- [ ] Legende fachlich überarbeitet
- [ ] Quellen und Einheiten im Layout angegeben
- [ ] PDF und PNG exportiert und geöffnet
- [ ] Ergebnistext verfasst
- [ ] Unsicherheiten dokumentiert
- [ ] `processing_notes.md` vollständig
- [ ] QGIS-Projekt auf funktionierende Pfade geprüft

<!-- Notizen: Ab hier folgen Vermerke, welche als Gedankenstütze oder Erinnerung dienen, aber noch nicht in der vorhandenen Form veröffentlicht werden sollen. -->

<!--
TODO Lehrende vor Durchführung:
- Art, Untersuchungsgebiet, Zeitraum und Zielgruppe endgültig festlegen.
- Projekt-CRS, Seitenformat und Exportauflösung ergänzen.
- vollständige Ersatzdaten samt Metadaten und Lizenzen bereitstellen.
- Höhenfeld und erwartete Wertebereiche prüfen.
- festlegen, ob DGM zwingend sichtbar sein muss oder nur als Analysequelle verwendet werden darf.
- Mustervergleich für gleiche Intervalle und Quantile vorbereiten.
- Musterlayout, Quellenzeile und Bewertungsraster erstellen.
- prüfen, ob 180 Minuten für die konkrete Datengröße und Abgabeform realistisch sind.

Musterlösung – intern:
- erwartete Punktzahl: [ergänzen]
- gültige Höhenwerte: [ergänzen]
- Höhenminimum/-maximum: [ergänzen]
- empfohlene Klassenzahl: [ergänzen]
- mögliche Klassengrenzen: [ergänzen]
- erwartetes Projekt-CRS: [EPSG ergänzen]
- verbindliche Quellenzeile: [ergänzen]
-->
