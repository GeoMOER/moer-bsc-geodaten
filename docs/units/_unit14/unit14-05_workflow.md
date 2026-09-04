---
title: Vom Datensatz zur räumlichen Aussage
published: true
toc: true
header:
  image: /assets/images/unit14/hero-unit14.jpg
  image_description: "Fertig gestaltete thematische Karte mit Höhenrelief, Flusslauf und kartographischen Nebenelementen"
  caption: "KI-generierte Illustration, bearbeitet für diesen Kurs"
---

<!-- Introtext: Die bisher einzeln erlernten Schritte zu einem vollständigen, nachvollziehbaren Geo-Workflow verbinden. -->

## Der vollständige Workflow

In den vorherigen Units haben wir einzelne Bestandteile räumlicher Datenarbeit kennengelernt:

* Geodaten, Koordinaten und Projektionen,
* Vektor- und Rastermodelle,
* QGIS und Geoportale,
* GBIF-Punktdaten,
* Linien und Polygone,
* digitale Geländemodelle,
* räumliche Auswahl und Rasterwerte an Punkten,
* Symbolisierung, Klassifizierung und Kartenlayout.

Nun verbinden wir diese Bestandteile zu einem vollständigen kleinen Workflow:

> **Fragestellung → Zielgruppe → Daten → Prüfung → Verarbeitung → Visualisierung → Layout → Export → Interpretation → Dokumentation**

Das Ziel ist nicht, jeden verfügbaren Layer zu verwenden. Das Ziel ist eine nachvollziehbare räumliche Aussage.

## 1. Fragestellung präzisieren

Unsere Leitfrage lautet:

> **Wie verteilen sich die dokumentierten Beobachtungen einer Art im Untersuchungsgebiet, und in welchen Höhenlagen liegen sie?**

Diese Formulierung ist bewusst vorsichtig:

* Wir untersuchen dokumentierte Beobachtungen, nicht die vollständige Verbreitung der Art.
* Wir beschreiben den verwendeten Datensatz und Zeitraum.
* Wir betrachten Geländehöhen aus einem bestimmten DGM.
* Wir behaupten keinen ursächlichen Zusammenhang zwischen Höhe und Vorkommen.

Ergänzen Sie für Ihr Projekt:

| Frage | Festlegung |
|---|---|
| Art oder Taxon | `[eintragen]` |
| Untersuchungsgebiet | `[eintragen]` |
| Beobachtungszeitraum | `[eintragen]` |
| Zielgruppe der Karte | `[eintragen]` |
| wichtigste räumliche Aussage | `[eintragen]` |

## 2. Benötigte Daten auswählen

Erstellen Sie vor dem Öffnen von QGIS eine Datenübersicht.

| Datensatz | Rolle im Workflow | notwendig? |
|---|---|---|
| GBIF-Beobachtungen mit Höhenwert | Hauptinformation | ja |
| digitales Geländemodell | Höhenkontext | ja oder begründet weglassen |
| Untersuchungsgebietsgrenze | räumliche Abgrenzung | meist sinnvoll |
| Schutzgebiete | zusätzlicher Kontext | optional |
| Gewässer | Orientierung oder fachlicher Kontext | optional |
| Hintergrundkarte | allgemeine Orientierung | nur bei Bedarf |

Für jeden zusätzlichen Layer gilt:

> **Welche Information trägt dieser Layer zur Leitfrage bei?**

Wenn darauf keine klare Antwort möglich ist, sollte der Layer nicht in der Abschlusskarte erscheinen.

## 3. Arbeitsstruktur anlegen

Verwenden Sie eine vollständige Projektstruktur:

```text
unit14_workflow/
  data_raw/
  data_intermediate/
  data_output/
  documentation/
  figures/
  unit14_workflow.qgz
```

* `data_raw/`: unveränderte Eingangsdaten,
* `data_intermediate/`: geprüfte oder bearbeitete Zwischenergebnisse,
* `data_output/`: finale Datenprodukte,
* `documentation/`: Quellen, Metadaten und Arbeitsschritte,
* `figures/`: exportierte Karten.

Verändern Sie die Originaldaten nicht direkt.

## 4. Dateninventar erstellen

Verbindlicher Eingang für die Hauptinformation ist `unit13_results.gpkg/gbif_mit_hoehe` mit dem numerischen Feld `hoehe_m`. Falls Sie den Ersatzlayer verwenden, muss er dasselbe Schema besitzen.

Dokumentieren Sie alle tatsächlich verwendeten Daten:

| Layer | Quelle | Datenstand | Geometrietyp | CRS | wichtige Felder/Werte | Lizenz |
|---|---|---|---|---|---|---|
| `[eintragen]` | `[eintragen]` | `[eintragen]` | `[eintragen]` | `[eintragen]` | `[eintragen]` | `[eintragen]` |

Prüfen Sie für jeden Layer:

* Quelle und Herausgeber,
* räumliche Abdeckung,
* Datenstand,
* CRS,
* Geometrie- oder Rastertyp,
* relevante Attribute beziehungsweise Zellwerte,
* Einheit,
* NoData oder fehlende Attribute,
* Lizenz und Zitieranforderung.

## 5. QGIS-Projekt einrichten

1. Erstellen Sie ein neues QGIS-Projekt.
2. Speichern Sie es als `unit14_workflow.qgz`.
3. Stellen Sie das seit Unit 10 verwendete Projekt-CRS ein: **`[EPSG-Code ergänzen; für Marburg voraussichtlich EPSG:25832]`**.
4. Prüfen Sie, ob relative Pfade für das gemeinsam abgegebene Projekt verwendet werden sollen.
5. Laden Sie zunächst nur die notwendigen Layer.
6. Benennen Sie die Layer fachlich verständlich.

Die Layernamen im Projekt können später automatisch in der Legende erscheinen. Technische Namen wie `final_v3_checked_2` sollten deshalb frühzeitig ersetzt werden.

## 6. Eingangsdaten prüfen

Führen Sie vor jeder Gestaltung eine Eingangskontrolle durch.

### Punktlayer

* richtige Art und richtiger Zeitraum,
* erwartete Featureanzahl,
* plausible räumliche Ausdehnung,
* bekanntes CRS,
* gültiges Höhenattribut,
* fehlende Höhenwerte,
* Koordinatenunsicherheit.

### Raster

* dargestellte Größe und Einheit,
* Zellgröße,
* CRS und Ausdehnung,
* Bandzahl,
* Minimum und Maximum,
* NoData.

### Kontextlayer

* richtiger Geometrietyp,
* räumliche Abdeckung,
* sinnvolle Attribute,
* Datenstand und Genauigkeit.

Halten Sie fest, welche Features oder Werte ausgeschlossen wurden und warum.

## 7. Notwendige Verarbeitung durchführen

Verwenden Sie möglichst bereits geprüfte Ergebnisse aus den vorherigen Units. Für die Abschlusskarte kann beispielsweise erforderlich sein:

1. GBIF-Daten nach Art, Zeitraum oder Datenqualität filtern,
2. Rasterwerte an den geprüften Punkten abtasten,
3. Punkte ohne gültigen Höhenwert kennzeichnen oder begründet ausschließen,
4. Kontextlayer auf das Untersuchungsgebiet beschränken,
5. Ergebnisse in einem GeoPackage speichern.

Ein möglicher Ergebnislayer lautet:

```text
data_output/unit14_results.gpkg
  gbif_mit_hoehe_final
```

Für jeden Verarbeitungsschritt sollten Eingabe, Werkzeug, Parameter und Ausgabe nachvollziehbar sein.

## 8. Hauptinformation symbolisieren

Stellen Sie die Beobachtungspunkte anhand ihres Höhenattributs abgestuft dar.

Vor der Klassifizierung prüfen Sie:

* Einheit des Feldes,
* Minimum und Maximum,
* fehlende Werte,
* mögliche Ausreißer und
* Zahl der gültigen Beobachtungen.

Vergleichen Sie mindestens zwei Methoden, beispielsweise:

* gleiche Intervalle und
* Quantile.

Entscheiden Sie sich anschließend für eine Methode und dokumentieren Sie:

| Entscheidung | Festlegung |
|---|---|
| Attribut | `[eintragen]` |
| Einheit | `[eintragen]` |
| Klassifizierungsmethode | `[eintragen]` |
| Zahl der Klassen | `[eintragen]` |
| Klassengrenzen | `[eintragen]` |
| Farbpalette | `[eintragen]` |
| Begründung | `[eintragen]` |

## 9. Kontext gestalten

Gestalten Sie weitere Layer zurückhaltend.

Eine mögliche visuelle Hierarchie:

1. Beobachtungspunkte mit Höhenklassen,
2. Untersuchungsgebiets- oder Schutzgebietsgrenzen,
3. DGM gemäß Aufgabenstellung entweder in einer hellen, zurückhaltenden Darstellung oder nur als dokumentierte Analysequelle,
4. Gewässer oder Hintergrundkarte nur bei erkennbarem Mehrwert.

Prüfen Sie die Karte sowohl in Gesamtansicht als auch in der späteren Layoutgröße.

## 10. Kartenlayout erstellen

Erstellen Sie ein Drucklayout mit dem vorgegebenen Seitenformat.

Mindestens erforderlich sind:

* Kartenelement,
* aussagekräftiger Titel,
* überarbeitete Legende mit Höhenangabe und Einheit,
* geeignete Maßstabsangabe,
* Datenquellen und Datenstände,
* Name beziehungsweise Bearbeitungshinweis und Datum.

Optional, wenn begründet:

* Nordpfeil,
* Übersichtskarte,
* Koordinatengitter,
* erläuternder Untertitel.

Die Legende darf nur Informationen enthalten, die in der Karte benötigt werden.

## 11. Karte exportieren und prüfen

Exportieren Sie die Karte als:

```text
figures/beobachtungen_hoehenlagen.pdf
figures/beobachtungen_hoehenlagen.png
```

Prüfen Sie beide Dateien außerhalb von QGIS:

* vollständig und nicht abgeschnitten,
* Schrift in Ausgabegröße lesbar,
* Klassen unterscheidbar,
* Legende korrekt,
* Quellen vollständig,
* keine unerwarteten weißen oder schwarzen Rasterbereiche,
* Dateigröße angemessen.

## 12. Räumliche Aussage formulieren

Eine Karte benötigt eine kurze fachliche Interpretation.

Beantworten Sie:

1. Wo konzentrieren sich die dokumentierten Beobachtungen?
2. Welche Höhenklassen kommen häufig beziehungsweise selten vor?
3. Gibt es Beobachtungen außerhalb des vorherrschenden Höhenbereichs?
4. Welche räumlichen Muster sind sichtbar?
5. Welche Aussage lässt sich aus der Karte **nicht** ableiten?

Eine mögliche Formulierung:

> Im verwendeten GBIF-Datensatz liegen die meisten dokumentierten Beobachtungen im Höhenbereich von `[Klasse]`. Einzelne Nachweise treten auch in `[Klasse]` auf. Die Karte beschreibt die vorhandenen Beobachtungen, nicht die flächendeckende Verbreitung oder Höhenpräferenz der Art.

## 13. Unsicherheiten dokumentieren

Nennen Sie mindestens:

* räumliche und zeitliche Abdeckung der Beobachtungen,
* ungleichmäßige Beobachtungsintensität,
* Koordinatenunsicherheit,
* Zellgröße und Genauigkeit des DGM,
* gewählte Klassengrenzen,
* mögliche fehlende Höhenwerte,
* Datenstände der verschiedenen Layer und
* Grenzen der visuellen Interpretation.

Die Klassifizierung ist selbst eine Quelle möglicher Interpretationsunterschiede. Eine andere Methode kann ein anderes sichtbares Muster erzeugen.

## 14. Workflow dokumentieren

Erstellen Sie `documentation/processing_notes.md` mit dieser Struktur:

```markdown
# Fragestellung

# Zielgruppe und Kartenformat

# Datenquellen und Lizenzen

# Eingangskontrolle

# Datenbereinigung und Auswahl

# Räumliche Verarbeitung

# Symbolisierung und Klassifizierung

# Kartenlayout und Export

# Ergebnisse

# Unsicherheiten

# Bearbeitungsdatum
```

Die Dokumentation muss keine lange wissenschaftliche Arbeit sein. Sie soll jedoch ermöglichen, Entscheidungen und zentrale Schritte nachzuvollziehen.

## Qualitätskontrolle

Führen Sie vor Abschluss vier getrennte Prüfungen durch:

### Daten

* Quellen, CRS, Werte, Einheiten und Datenstände korrekt?

### Verarbeitung

* Eingabelayer, Filter, Werkzeuge und Ausgaben dokumentiert?

### Karte

* Hauptaussage sichtbar, Farben und Klassen verständlich, Layout vollständig?

### Interpretation

* Aussage durch Daten gedeckt, Unsicherheiten benannt, keine unzulässige Verallgemeinerung?

## Peer-Check

Tauschen Sie die exportierte Karte mit einer anderen Person. Ohne zusätzliche Erklärung beantwortet diese:

1. Was ist die Hauptaussage der Karte?
2. Welche Daten zeigen die Farben der Beobachtungspunkte?
3. Welche Einheit wird verwendet?
4. Woher stammen die Daten?
5. Was ist unklar oder schwer lesbar?

Überarbeiten Sie die Karte anhand der Rückmeldung, wenn die beabsichtigte Aussage nicht erkennbar ist.

## Zusammenfassung

* Ein Geo-Workflow beginnt mit einer präzisen Frage und einer Zielgruppe, nicht mit der Gestaltung.
* Nur Daten, die zur Frage beitragen, gehören in die Abschlusskarte.
* Eingangsdaten und Zwischenergebnisse müssen geprüft und getrennt gespeichert werden.
* Symbolisierung und Klassifizierung sind begründete analytische Entscheidungen.
* Layout und Quellenangaben machen aus der Kartenansicht ein verständliches Kartenprodukt.
* Exportdateien müssen unabhängig von QGIS kontrolliert werden.
* Interpretation und Unsicherheit gehören gemeinsam zur Karte.
* Eine kurze Prozessdokumentation macht den Workflow nachvollziehbar und wiederholbar.

## Weiterführende Informationen

* [QGIS-Dokumentation: Vektorsymbolisierung](https://docs.qgis.org/latest/en/docs/user_manual/working_with_vector/vector_properties.html)
* [QGIS-Dokumentation: Drucklayout](https://docs.qgis.org/latest/en/docs/user_manual/print_layout/overview_layout.html)
* [QGIS-Dokumentation: Kartenexport](https://docs.qgis.org/latest/en/docs/user_manual/print_layout/create_output.html)

<!-- Notizen: Ab hier folgen Vermerke, welche als Gedankenstütze oder Erinnerung dienen, aber noch nicht in der vorhandenen Form veröffentlicht werden sollen. -->

<!--
TODO Lehrende vor Durchführung:
- finale Leitfrage, Art, Untersuchungsgebiet und Zielgruppe vorgeben.
- Ersatzdatensätze und verbindliches Projekt-CRS bereitstellen.
- Feldname des Höhenwertes und zulässige Datenqualitätsfilter ergänzen.
- Seitenformat und Exportauflösung festlegen.
- Quellenangaben für alle bereitgestellten Daten vorbereiten.
- Musterprojekt und vollständige Musterkarte erstellen.
- Peer-Check zeitlich in die Sitzung einplanen.

Didaktisch wichtig:
- Workflow nicht als lineare Einbahnstraße darstellen: Kontrollen können Rücksprünge erfordern.
- nicht verlangen, alle Layer aus Units 11–13 sichtbar zu verwenden.
- Kriterien für das Weglassen von Daten ebenso bewerten wie das Hinzufügen.
- klare Trennung zwischen beobachtetem Muster und ökologischer Erklärung.
-->
