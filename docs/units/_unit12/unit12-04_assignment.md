---
title: HA | Hausaufgabe Abschnitt 12
published: true
toc: true
header:
  image: /assets/images/unit12/hero-unit12.jpg
  image_description: "Flusslandschaft mit Schutzgebietsfläche und Beobachtungspunkten innerhalb und außerhalb des Gebietes"
  caption: "KI-generierte Illustration, bearbeitet für diesen Kurs"
---

<!-- Hausaufgabe 12: Linien, Polygone, Geoportale und räumliche Auswahl -->

## Hausaufgabe 12

In dieser Hausaufgabe wenden Sie die Inhalte aus Unit 12 selbstständig an. Sie dokumentieren zwei Vektordatenquellen, kombinieren Punkt-, Linien- und Polygondaten in QGIS und beantworten eine einfache räumliche Fragestellung.

| Rahmenbedingung | Festlegung |
|---|---|
| Bearbeitungszeit | etwa 90 Minuten |
| Abgabeformat | vollständiger Arbeitsordner als `unit12_nachname_vorname.zip` |
| Abgabeort | `[ILIAS-Ordner beziehungsweise Abgabeort ergänzen]` |
| Abgabetermin | `[Datum und Uhrzeit ergänzen]` |
| Arbeitsform | Einzelarbeit; räumliche Beziehungen und Entscheidungen müssen selbst dokumentiert werden. |

## Fragestellung

Untersuchen Sie:

> **Welche Artenbeobachtungen und Gewässer liegen in beziehungsweise schneiden die ausgewählten Schutzgebiete?**

Beachten Sie: Eine räumliche Überschneidung beschreibt zunächst nur die Lage der Objekte. Sie beweist keinen fachlichen oder ursächlichen Zusammenhang.

## Benötigte Daten

Für die Aufgabe benötigen Sie:

- `unit11_results.gpkg/gbif_checked` oder den schemaidentischen Ersatzlayer,
- den bereitgestellten Schutzgebiets-Layer,
- den bereitgestellten Gewässer-Layer,
- die Metadatenseiten oder Quellenangaben der beiden neuen Datensätze.

Falls Sie Unit 11 mit einer anderen Art bearbeitet haben, können Sie diesen Punktlayer weiterverwenden.

| Verbindliche Angabe | Festlegung |
|---|---|
| QGIS-Version | `[dieselbe verbindliche QGIS-LTR-Version wie in Unit 10 ergänzen]` |
| Gewässerdaten | `[Datei, Layer und Downloadlink ergänzen]` |
| Schutzgebietsdaten | `[Datei, Layer und Downloadlink ergänzen]` |
| Auswahlfeld und Zielwert | `[Feldname und Schutzgebietskategorie ergänzen]` |
| Ersatzdatenpaket | `[Downloadlink ergänzen]` |

## 1. Arbeitsumgebung vorbereiten

Erstellen Sie diese Ordnerstruktur:

```text
hausaufgabe12/
  data_raw/
  data_output/
  documentation/
```

Speichern Sie Ihr QGIS-Projekt als:

```text
hausaufgabe12.qgz
```

Verwenden Sie das seit Unit 10 eingesetzte Projekt-CRS: **`[EPSG-Code ergänzen; für Marburg voraussichtlich EPSG:25832]`**.

## 2. Datenquellen dokumentieren

Dokumentieren Sie den Schutzgebiets- und den Gewässerdatensatz.

| Merkmal | Schutzgebiete | Gewässer |
|---|---|---|
| genauer Titel | `[eintragen]` | `[eintragen]` |
| Herausgeber | `[eintragen]` | `[eintragen]` |
| Geometrietyp | `[eintragen]` | `[eintragen]` |
| räumliche Abdeckung | `[eintragen]` | `[eintragen]` |
| Datenstand | `[eintragen]` | `[eintragen]` |
| CRS | `[eintragen]` | `[eintragen]` |
| Zugang oder Dateiformat | `[eintragen]` | `[eintragen]` |
| Lizenz | `[eintragen]` | `[eintragen]` |
| Quelle/URL | `[eintragen]` | `[eintragen]` |

Beantworten Sie zusätzlich in ein bis zwei Sätzen:

1. Handelt es sich jeweils um einen Download, WFS oder WMS?
2. Sind die Daten für eine Vektoranalyse geeignet? Begründen Sie Ihre Antwort.

## 3. Layer laden und prüfen

Laden Sie die drei Layer in QGIS und dokumentieren Sie Ihre Eingangskontrolle.

| Kontrolle | GBIF-Punkte | Gewässer | Schutzgebiete |
|---|---|---|---|
| Geometrietyp | `[eintragen]` | `[eintragen]` | `[eintragen]` |
| CRS | `[eintragen]` | `[eintragen]` | `[eintragen]` |
| Anzahl Features | `[eintragen]` | `[eintragen]` | `[eintragen]` |
| wichtiges Attribut | `[eintragen]` | `[eintragen]` | `[eintragen]` |
| Ausdehnung plausibel? | ja / nein | ja / nein | ja / nein |

Prüfen Sie zusätzlich, ob die Layer räumlich plausibel übereinanderliegen.

## 4. Layer gestalten

Gestalten Sie die Layer so, dass alle drei Geometrietypen erkennbar bleiben:

- Beobachtungen als gut sichtbare Punkte,
- Gewässer als Linien,
- Schutzgebiete als transparente oder nur leicht gefüllte Polygone.

Ordnen Sie die Layer sinnvoll an. Verwenden Sie für mindestens einen Layer eine Attributinformation zur Symbolisierung oder Auswahl.

Fügen Sie einen Screenshot der Kartenansicht in Ihre Dokumentation ein.

## 5. Schutzgebiete auswählen

Wählen Sie über ein geeignetes Attribut die im Kurs vorgegebene Gruppe von Schutzgebieten aus.

- verwendetes Feld: **`[eintragen]`**
- verwendeter Wert oder Ausdruck: **`[eintragen]`**
- Anzahl ausgewählter Schutzgebiete: **`[eintragen]`**

Exportieren Sie die Auswahl in das GeoPackage:

```text
data_output/unit12_results.gpkg
```

Verwenden Sie den Layernamen:

```text
schutzgebiete_auswahl
```

<!-- Lehrende: Konkretes Attribut und auszuwählende Kategorie passend zum bereitgestellten Datensatz festlegen. -->

## 6. Räumliche Auswahl durchführen

Verwenden Sie **Nach Position selektieren** und die räumliche Beziehung **schneidet**.

### A: Beobachtungen

Wählen Sie alle GBIF-Beobachtungen aus, die den Layer `schutzgebiete_auswahl` schneiden.

- Anzahl aller Beobachtungen: **`[eintragen]`**
- Anzahl ausgewählter Beobachtungen: **`[eintragen]`**

Exportieren Sie die ausgewählten Punkte in `unit12_results.gpkg` als:

```text
gbif_in_schutzgebieten
```

### B: Gewässer

Wählen Sie alle Gewässer-Features aus, die den Layer `schutzgebiete_auswahl` schneiden.

- Anzahl aller Gewässer-Features: **`[eintragen]`**
- Anzahl ausgewählter Gewässer-Features: **`[eintragen]`**

Exportieren Sie die ausgewählten Linien in `unit12_results.gpkg` als:

```text
gewaesser_an_schutzgebieten
```

Kontrollieren Sie alle drei Ergebnislayer nach dem Export auf Geometrietyp, CRS und Featureanzahl.

## 7. Ergebnisse beschreiben

Beantworten Sie schriftlich:

1. Wie viele Beobachtungen wurden räumlich ausgewählt?
2. Wie viele Gewässer-Features wurden räumlich ausgewählt?
3. Was bedeutet die Beziehung **schneidet** bei einem Punkt und bei einer Linie jeweils?
4. Warum ist eine räumliche Auswahl nicht dasselbe wie ein Beleg für einen ökologischen Zusammenhang?
5. Nennen Sie mindestens zwei Unsicherheiten oder Einschränkungen der Auswertung.

Gehen Sie dabei mindestens auf einen der folgenden Aspekte ein:

- Koordinatenunsicherheit der Beobachtungen,
- Genauigkeit oder Generalisierung von Grenzen,
- unterschiedliche Datenstände,
- Maßstab und räumliche Auflösung der Datensätze,
- Bedeutung eines ausgewählten Linien-Features.

## 8. Arbeitsschritte dokumentieren

Erstellen Sie im Ordner `documentation/` eine kurze Datei mit dem Namen:

```text
processing_notes.md
```

Notieren Sie darin:

- Fragestellung,
- verwendete Datenquellen,
- Projekt-CRS,
- verwendete Attributauswahl,
- räumliche Beziehung,
- Ergebniszahlen,
- mögliche Einschränkungen,
- Datum der Bearbeitung.

Die Beschreibung soll so genau sein, dass eine andere Person Ihre grundlegenden Schritte nachvollziehen kann.

## Abgabe

Geben Sie den vollständigen Ordner `hausaufgabe12/` als `unit12_nachname_vorname.zip` ab. Er soll mindestens enthalten:

- `hausaufgabe12.qgz`,
- `data_output/unit12_results.gpkg` mit den drei Ergebnislayern,
- `documentation/processing_notes.md`,
- die ausgefüllten Tabellen und Antworten,
- einen Screenshot der gestalteten Kartenansicht.

Kontrollieren Sie vor der Abgabe, ob sich das QGIS-Projekt öffnen lässt und alle Ergebnislayer vorhanden sind.

## Bewertungskriterien

| Kriterium | Erwartung |
|---|---|
| Datenquellen | vollständig und nachvollziehbar dokumentiert |
| Eingangskontrolle | Geometrietyp, CRS, Featurezahl und Ausdehnung geprüft |
| Darstellung | Punkte, Linien und Polygone gemeinsam lesbar |
| Attributauswahl | passendes Feld und nachvollziehbarer Ausdruck verwendet |
| räumliche Auswahl | Eingabe-, Vergleichslayer und Beziehung korrekt gewählt |
| Ergebnisdatei | drei eindeutig benannte Layer im GeoPackage |
| Interpretation | Ergebniszahlen korrekt und Einschränkungen reflektiert |
| Reproduzierbarkeit | Projekt, Daten und Arbeitsschritte geordnet abgegeben |

## Punkteverteilung

| Bereich | Punkte |
|---|---:|
| Datenquellen und Eingangskontrolle | 10 |
| Darstellung und Attributauswahl | 8 |
| räumliche Auswahl der Punkte | 8 |
| räumliche Auswahl der Gewässer | 8 |
| Interpretation und Unsicherheiten | 8 |
| Reproduzierbarkeit und Abgabe | 8 |

Gesamt: **50 Punkte**. Für das Bestehen sind **`[Mindestpunktzahl ergänzen, Vorschlag: 25 von 50 Punkten]`** erforderlich. Fachlich gleichwertige räumliche Beziehungen sind nur dann zulässig, wenn sie zur formulierten Frage passen und dokumentiert werden. Folgefehler werden nicht mehrfach bewertet.

## Checkliste

- [ ] Datenquellen und Lizenzen dokumentiert
- [ ] drei Eingabelayer kontrolliert
- [ ] Layer sinnvoll gestaltet
- [ ] Schutzgebiete nach Attribut ausgewählt
- [ ] Beobachtungen räumlich ausgewählt
- [ ] Gewässer räumlich ausgewählt
- [ ] drei Ergebnislayer in `unit12_results.gpkg` gespeichert
- [ ] Ergebnisse und Unsicherheiten beschrieben
- [ ] `processing_notes.md` erstellt
- [ ] QGIS-Projekt gespeichert und getestet

<!-- Notizen: Ab hier folgen Vermerke, welche als Gedankenstütze oder Erinnerung dienen, aber noch nicht in der vorhandenen Form veröffentlicht werden sollen. -->

<!--
TODO Lehrende vor Durchführung:
- Projekt-CRS und EPSG-Code ergänzen.
- Konkrete Schutzgebietskategorie und Feldnamen vorgeben.
- Datendateien beziehungsweise belastbare Downloadlinks bereitstellen.
- Erwartete Featurezahlen mit dem finalen Datenstand berechnen.
- Musterlösung mit Auswahlparametern und Ergebnis-Screenshots erstellen.
- Prüfen, ob 90 Minuten mit der gewählten Datengröße realistisch sind.

Musterlösung – intern:
- Schutzgebiete ausgewählt: [Anzahl ergänzen]
- GBIF-Punkte ausgewählt: [Anzahl ergänzen]
- Gewässer-Features ausgewählt: [Anzahl ergänzen]
- erwartetes Projekt-CRS: [EPSG ergänzen]
-->
