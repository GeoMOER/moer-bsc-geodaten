---
title: HA | Hausaufgabe Abschnitt 13
published: true
toc: true
header:
  image: /assets/images/unit13/hero-unit13.jpg
  image_description: "Übertragung eines Rasterwertes auf einen Beobachtungspunkt"
  caption: "Eigene Darstellung"
---

<!-- Hausaufgabe 13: Rastereigenschaften und Höhenwerte an Beobachtungspunkten -->

## Hausaufgabe 13

In dieser Hausaufgabe wenden Sie die Inhalte aus Unit 13 selbstständig an. Sie prüfen und dokumentieren ein digitales Geländemodell, stellen seine Höhenwerte in QGIS dar und übertragen Rasterwerte auf die GBIF-Beobachtungspunkte.

| Rahmenbedingung | Festlegung |
|---|---|
| Bearbeitungszeit | etwa 90 Minuten |
| Abgabeformat | vollständiger Arbeitsordner als `unit13_nachname_vorname.zip` |
| Abgabeort | `[ILIAS-Ordner beziehungsweise Abgabeort ergänzen]` |
| Abgabetermin | `[Datum und Uhrzeit ergänzen]` |
| Arbeitsform | Einzelarbeit; Kontrollen und Unsicherheitsbeurteilung müssen selbst dokumentiert werden. |

## Fragestellung

Untersuchen Sie:

> **Auf welcher Geländehöhe liegen die dokumentierten Artenbeobachtungen?**

Die Antwort bezieht sich ausschließlich auf die bereitgestellten Beobachtungen und das verwendete Höhenmodell. Sie beschreibt nicht automatisch den gesamten Höhenbereich, in dem die Art vorkommt.

## Benötigte Daten

Für die Aufgabe benötigen Sie:

* den in Unit 11 geprüften GBIF-Punktlayer oder den bereitgestellten Ersatzlayer,
* das bereitgestellte digitale Geländemodell,
* die Metadaten und Quellenangaben des Höhenmodells.

| Verbindliche Angabe | Festlegung |
|---|---|
| QGIS-Version | `[dieselbe verbindliche QGIS-LTR-Version wie in Unit 10 ergänzen]` |
| DGM-Datei und Download | `[Dateiname und Downloadlink ergänzen]` |
| DGM-Einheit und Höhenbezug | `[ergänzen]` |
| Ersatzlayer `gbif_checked` | `[Downloadlink ergänzen]` |

Falls Sie Unit 11 mit einer anderen Art bearbeitet haben, können Sie diesen Punktlayer verwenden, sofern er im Gebiet des Höhenrasters liegt.

## 1. Arbeitsumgebung vorbereiten

Erstellen Sie diese Ordnerstruktur:

```text
hausaufgabe13/
  data_raw/
  data_output/
  documentation/
```

Speichern Sie Ihr QGIS-Projekt als:

```text
hausaufgabe13.qgz
```

Verwenden Sie das seit Unit 10 eingesetzte Projekt-CRS: **`[EPSG-Code ergänzen; für Marburg voraussichtlich EPSG:25832]`**.

## 2. Datenquelle dokumentieren

Dokumentieren Sie das digitale Geländemodell anhand seiner Metadaten.

| Merkmal | Angabe |
|---|---|
| genauer Titel | `[eintragen]` |
| Herausgeber | `[eintragen]` |
| dargestellte Größe | `[eintragen]` |
| Einheit | `[eintragen]` |
| Zellgröße | `[eintragen]` |
| CRS | `[eintragen]` |
| räumliche Abdeckung | `[eintragen]` |
| Datenstand | `[eintragen]` |
| Höhenbezug | `[eintragen]` |
| NoData-Wert | `[eintragen]` |
| Entstehungsmethode | `[eintragen]` |
| Lizenz | `[eintragen]` |
| Quelle/URL | `[eintragen]` |

Erklären Sie in ein bis zwei Sätzen, weshalb der Datensatz ein **kontinuierliches Raster** ist.

## 3. Raster in QGIS prüfen

Laden Sie das DGM und kontrollieren Sie seine technischen Eigenschaften.

| Kontrolle | Ergebnis |
|---|---|
| Anzahl Zeilen | `[eintragen]` |
| Anzahl Spalten | `[eintragen]` |
| Anzahl Bänder | `[eintragen]` |
| Datentyp | `[eintragen]` |
| Zellgröße x/y | `[eintragen]` |
| CRS | `[eintragen]` |
| Minimum | `[eintragen]` |
| Maximum | `[eintragen]` |
| NoData definiert? | `[eintragen]` |
| Ausdehnung plausibel? | ja / nein |

Beantworten Sie zusätzlich:

1. Ist die Zellgröße in Metern oder Grad angegeben?
2. Sind Minimum und Maximum für das Untersuchungsgebiet plausibel?
3. Belegt die Zellgröße allein, wie genau die Höhenwerte sind? Begründen Sie.

## 4. Rasterwerte darstellen und abfragen

Stellen Sie das DGM als **Einkanal-Pseudofarbe** dar.

* Verwenden Sie einen geeigneten sequentiellen Farbverlauf.
* Niedrige und hohe Geländehöhen müssen unterscheidbar sein.
* Prüfen Sie, ob NoData-Zellen sinnvoll behandelt werden.

Fragen Sie anschließend drei Zellen mit dem Abfragewerkzeug ab:

| Position oder Ort | Rasterwert | Einheit | plausibel? |
|---|---:|---|---|
| `[eintragen]` | `[eintragen]` | `[eintragen]` | ja / nein |
| `[eintragen]` | `[eintragen]` | `[eintragen]` | ja / nein |
| `[eintragen]` | `[eintragen]` | `[eintragen]` | ja / nein |

Fügen Sie Ihrer Dokumentation einen Screenshot der Rasterdarstellung mit eingeblendeter Legende im Layerfenster hinzu.

## 5. Beobachtungspunkte kontrollieren

Laden Sie den geprüften GBIF-Punktlayer und legen Sie ihn über das DGM.

Notieren Sie:

| Kontrolle | Ergebnis |
|---|---|
| Art beziehungsweise Taxon | `[eintragen]` |
| Anzahl Punkte | `[eintragen]` |
| CRS | `[eintragen]` |
| Punkte im Rastergebiet? | vollständig / teilweise / nein |
| Koordinatenunsicherheit berücksichtigt? | `[eintragen]` |

Gestalten Sie die Punkte so, dass sie auf dem Höhenraster gut erkennbar sind.

## 6. Höhenwerte abtasten

Verwenden Sie das Werkzeug **Rasterwerte abtasten** beziehungsweise **Sample raster values**:

1. Eingabelayer: geprüfte GBIF-Punkte,
2. Rasterlayer: digitales Geländemodell,
3. Spaltenpräfix: `hoehe_`,
4. Ausgabe: `data_output/unit13_results.gpkg`,
5. Layername: `gbif_mit_hoehe`.

Das verbindliche finale Höhenfeld heißt **`hoehe_m`**. Falls QGIS zunächst einen anderen Feldnamen erzeugt, erstellen Sie `hoehe_m` kontrolliert als numerisches Feld, übernehmen Sie die Werte und dokumentieren Sie diesen Schritt.

Öffnen Sie die Attributtabelle des Ergebnislayers und tragen Sie ein:

| Ergebnis | Wert |
|---|---:|
| Anzahl Eingabepunkte | `[eintragen]` |
| Anzahl Ergebnispunkte | `[eintragen]` |
| Name des neuen Höhenfeldes | `[eintragen]` |
| Punkte mit gültigem Höhenwert | `[eintragen]` |
| Punkte ohne gültigen Höhenwert | `[eintragen]` |

Die Zahl der Ergebnisfeatures sollte grundsätzlich der Zahl der Eingabepunkte entsprechen. Fehlende Rasterwerte werden als fehlende Attribute gespeichert; die betreffenden Punkte sollten nicht ohne Begründung verschwinden.

## 7. Ergebnis kontrollieren

Wählen Sie fünf Punkte aus verschiedenen Teilen des Untersuchungsgebiets. Vergleichen Sie den neuen Attributwert mit einer direkten Abfrage des Rasters an derselben Position.

| Punkt-ID | Höhenattribut | direkt abgefragter Wert | Übereinstimmung? |
|---|---:|---:|---|
| `[eintragen]` | `[eintragen]` | `[eintragen]` | ja / nein |
| `[eintragen]` | `[eintragen]` | `[eintragen]` | ja / nein |
| `[eintragen]` | `[eintragen]` | `[eintragen]` | ja / nein |
| `[eintragen]` | `[eintragen]` | `[eintragen]` | ja / nein |
| `[eintragen]` | `[eintragen]` | `[eintragen]` | ja / nein |

Falls ein Wert nicht übereinstimmt, prüfen und dokumentieren Sie die mögliche Ursache.

## 8. Höhenverteilung beschreiben

Ermitteln Sie für alle Beobachtungspunkte mit gültigem Höhenwert:

| Kennwert | Ergebnis |
|---|---:|
| Minimum | `[eintragen]` |
| Maximum | `[eintragen]` |
| Median oder anderer vorgegebener mittlerer Wert | `[eintragen]` |
| Spannweite | `[eintragen]` |

Formulieren Sie daraus zwei bis drei Sätze. Verwenden Sie eine vorsichtige Formulierung, beispielsweise:

> Im untersuchten Datensatz liegen die dokumentierten Beobachtungen zwischen `[Minimum]` und `[Maximum]` Metern Geländehöhe. Der mittlere beziehungsweise typische Wert beträgt `[Wert]` Meter. Diese Werte beschreiben die vorhandenen Nachweise und nicht zwangsläufig den vollständigen Höhenbereich der Art.

## 9. Unsicherheiten beurteilen

Beantworten Sie schriftlich:

1. Welche räumliche Fläche repräsentiert eine Rasterzelle?
2. Warum ist der abgetastete Höhenwert nicht zwingend die exakt bekannte Höhe der Beobachtung?
3. Welche Rolle spielt die Koordinatenunsicherheit der GBIF-Punkte?
4. Weshalb darf NoData nicht als Höhenwert null interpretiert werden?
5. Nennen Sie mindestens zwei weitere Einschränkungen der Auswertung.

## 10. Arbeitsschritte dokumentieren

Erstellen Sie im Ordner `documentation/` eine Datei mit dem Namen:

```text
processing_notes.md
```

Dokumentieren Sie darin:

* Fragestellung,
* Datenquellen und Datenstand,
* Projekt-CRS,
* Zellgröße, Höhenbezug und Einheit des DGM,
* verwendete Darstellung,
* Parameter des Abtastwerkzeugs,
* Ergebniszahlen,
* durchgeführte Kontrollen,
* Unsicherheiten und
* Datum der Bearbeitung.

## Abgabe

Geben Sie den vollständigen Ordner `hausaufgabe13/` als `unit13_nachname_vorname.zip` ab. Er soll mindestens enthalten:

* `hausaufgabe13.qgz`,
* `data_output/unit13_results.gpkg` mit dem Layer `gbif_mit_hoehe` und dem Feld `hoehe_m`,
* `documentation/processing_notes.md`,
* die ausgefüllten Tabellen und Antworten und
* einen Screenshot der gestalteten Kartenansicht.

Kontrollieren Sie vor der Abgabe, ob sich das QGIS-Projekt öffnen lässt und der Ergebnislayer vorhanden ist.

## Bewertungskriterien

| Kriterium | Erwartung |
|---|---|
| Datenquelle | vollständig und nachvollziehbar dokumentiert |
| Rasterprüfung | Zellgröße, CRS, Bänder, Wertebereich und NoData kontrolliert |
| Darstellung | kontinuierliches Raster sachgerecht und lesbar dargestellt |
| Punktlayer | räumliche Lage und Koordinateninformationen geprüft |
| Abtastung | richtige Eingaben, eindeutiges Präfix und korrekt gespeicherte Ausgabe |
| Qualitätskontrolle | mindestens fünf Höhenwerte mit dem Ursprungsraster verglichen |
| Beschreibung | Wertebereich korrekt und vorsichtig zusammengefasst |
| Unsicherheit | Auflösung, NoData und Punktunsicherheit fachlich reflektiert |
| Reproduzierbarkeit | Projekt, Ergebnis und Arbeitsschritte geordnet abgegeben |

## Punkteverteilung

| Bereich | Punkte |
|---|---:|
| DGM-Quelle und Rasterprüfung | 10 |
| Darstellung und direkte Wertabfrage | 7 |
| Punktkontrolle und Rasterabtastung | 10 |
| Ergebnis- und Feldkontrolle `hoehe_m` | 8 |
| Beschreibung und Unsicherheiten | 10 |
| Reproduzierbarkeit und Abgabe | 5 |

Gesamt: **50 Punkte**. Für das Bestehen sind **`[Mindestpunktzahl ergänzen, Vorschlag: 25 von 50 Punkten]`** erforderlich. Ein dokumentierter NoData-Fall oder fehlender Höhenwert ist nicht automatisch ein Fehler. Folgefehler werden nicht mehrfach bewertet.

## Checkliste

- [ ] DGM-Quelle und Lizenz dokumentiert
- [ ] Rastereigenschaften vollständig geprüft
- [ ] DGM mit geeigneter Farbskala dargestellt
- [ ] drei Rasterzellen direkt abgefragt
- [ ] GBIF-Punkte räumlich kontrolliert
- [ ] Höhenwerte auf Punkte übertragen
- [ ] Ergebnislayer als `gbif_mit_hoehe` gespeichert
- [ ] verbindliches numerisches Feld `hoehe_m` vorhanden und geprüft
- [ ] fünf Ergebniswerte kontrolliert
- [ ] Höhenverteilung beschrieben
- [ ] Unsicherheiten diskutiert
- [ ] `processing_notes.md` erstellt
- [ ] QGIS-Projekt gespeichert und getestet

<!-- Notizen: Ab hier folgen Vermerke, welche als Gedankenstütze oder Erinnerung dienen, aber noch nicht in der vorhandenen Form veröffentlicht werden sollen. -->

<!--
TODO Lehrende vor Durchführung:
- Projekt-CRS und EPSG-Code ergänzen.
- DGM und GBIF-Punktlayer bereitstellen und gemeinsam testen.
- Quellenangabe, Datenstand, Höhenbezug, Einheit und Lizenz vorgeben.
- Erwartete Zeilen-/Spaltenzahlen, Zellgröße, Minimum, Maximum und NoData dokumentieren.
- erwartete Feldbezeichnung und Punktzahlen nach Abtastung prüfen.
- Musterwerte für Minimum, Maximum, Median und Spannweite berechnen.
- festlegen, ob Median oder ein anderer bereits eingeführter Kennwert verwendet wird.
- Musterlösung mit Kontrollpunkten und Screenshots erstellen.
- prüfen, ob 90 Minuten mit der Datengröße realistisch sind.

Musterlösung – intern:
- Rasterzeilen/-spalten: [ergänzen]
- Zellgröße: [ergänzen]
- DGM-Minimum/-Maximum: [ergänzen]
- gültige Höhenwerte: [ergänzen]
- fehlende Höhenwerte: [ergänzen]
- Höhenminimum/-maximum/-median der Punkte: [ergänzen]
- erwartetes Projekt-CRS: [EPSG ergänzen]
-->
