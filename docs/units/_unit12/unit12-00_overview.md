---
title: Überblick
published: true
toc: true
header:
  image: /assets/images/unit12/hero-unit12.jpg
  image_description: "Flusslandschaft mit Schutzgebietsfläche und Beobachtungspunkten innerhalb und außerhalb des Gebietes"
  caption: "KI-generierte Illustration, bearbeitet für diesen Kurs"
---

<!-- Rückblick: Welche Themeninhalte wurden in der letzten Kurssitzung bearbeitet? Sind Fragen zur letzten Kurssitzung offen geblieben? -->

## Rückblick & Fragen

In der letzten Kurssitzung haben wir Punktdaten als Teil des Vektormodells untersucht. Aus tabellarischen GBIF-Nachweisen haben wir in QGIS einen Punktlayer erzeugt, Attribute und Qualitätsinformationen geprüft und eine dokumentierte Auswahl als GeoPackage gespeichert.

Zu Beginn besprechen wir **10 Minuten lang die JiTT-Antworten zu Unit 11**. An ein bis zwei ausgewählten Verständnisfragen klären wir die wichtigsten offenen Punkte und knüpfen an die vorige Sitzung an.

<!-- Introtext: Allgemeine Einleitung zum Thema im neuen Lernabschnitt und Verbindung zum vorangegangenen Thema. Worum geht es, welche Inhalte werden bearbeitet und warum sind diese wichtig? -->

## Einführung in Lernabschnitt 12

Punkte beschreiben einzelne Positionen. Viele geographische Objekte besitzen jedoch einen Verlauf oder eine räumliche Ausdehnung. Gewässer und Verkehrswege werden häufig als **Linien**, Schutzgebiete, Seen oder Verwaltungsgebiete als **Polygone** dargestellt.

In dieser Unit vervollständigen wir damit das grundlegende Vektormodell aus Punkt, Linie und Polygon. Wir untersuchen, wie diese Geometrien aufgebaut sind, welche Attribute sie besitzen und weshalb Maßstab und Fragestellung die gewählte Darstellung beeinflussen.

Anschließend beschaffen wir reale Vektordaten über Geoportale und kombinieren sie in QGIS mit den GBIF-Punkten aus Unit 11. Dadurch können wir erstmals räumliche Fragen beantworten, die mit einer gewöhnlichen Tabelle nur schwer zu bearbeiten wären:

> **Welche dokumentierten Artennachweise liegen innerhalb von Schutzgebieten, und welche Gewässer schneiden diese Flächen?**

<!-- Aktuelle Lerneinheit: Welcher konkrete Inhalt erwartet die Studierenden? -->

## In dieser Lerneinheit ...

In dieser Lerneinheit beschäftigen wir uns mit drei aufeinander aufbauenden Fragen:

1. **Wie funktionieren Linien- und Polygongeometrien?**  
   Wir betrachten Stützpunkte, Linienverläufe, geschlossene Flächen, Multipart-Geometrien sowie die Verbindung von Geometrie und Attributen.

2. **Wie finden und beurteilen wir Vektordaten in Geoportalen?**  
   Wir suchen nach Gewässer- und Schutzgebietsdaten, lesen Metadaten, unterscheiden Vorschau, Download und WFS und prüfen Format, CRS, Aktualität und Lizenz.

3. **Wie untersuchen und kombinieren wir Vektorlayer in QGIS?**  
   Wir laden Linien und Polygone, symbolisieren und filtern sie und verwenden eine räumliche Auswahl, um Punkt-, Linien- und Polygonlayer miteinander in Beziehung zu setzen.

Die wiederkehrende Arbeitslogik lautet:

> **Fragestellung → Datenquelle → Geometrietyp → Attribute → räumliche Beziehung → dokumentiertes Ergebnis**

<!-- Lernziele: Was sollten Studierende am Ende dieser Lerneinheit wissen und anwenden können? -->

## Lernziele

### Verbindliche Kernziele

Am Ende der gemeinsamen Sitzung sind Studierende in der Lage, ...

* Punkt, Linie und Polygon zu unterscheiden und für eine einfache Fragestellung einen passenden Vektorgeometrietyp auszuwählen,
* die Eignung einer Vektordatenquelle anhand zentraler Metadaten zu prüfen und einen WMS von einem analysierbaren Download beziehungsweise WFS zu unterscheiden,
* Linien- und Polygonlayer in QGIS zu laden und eine vorgegebene Attributauswahl durchzuführen,
* Punkte und Linien mit der räumlichen Beziehung „schneidet“ (`intersects`) zu Polygonen auszuwählen, die Behandlung eines Grenzfalls zu erklären und die Ergebnisse dauerhaft zu speichern und
* Datenquellen, CRS, Auswahlregeln, Featurezahlen und fachliche Grenzen des Ergebnisses nachvollziehbar zu dokumentieren.

### Vertiefung und Nachschlagen

Die ausführlichen Unterseiten ermöglichen außerdem, ...

* Aufbau, Multipart-Geometrien, Generalisierung und Grenzdefinitionen von Linien und Polygonen genauer zu untersuchen,
* GeoPackage, GeoJSON und Shapefile mit ihren jeweiligen Eigenschaften einzuordnen und
* selbst nach Daten in Geoportalen zu suchen, einen WFS einzubinden sowie Längen- und Flächenattribute zu berechnen.

<!-- Organisatorisches: Gibt es Formalitäten, welche noch geklärt werden sollten? -->

## Organisatorisches

[Marburger Übungspaket und Anleitung]({{ '/material/marburg.html' | relative_url }}). Entpacken Sie das gesamte Paket in einen lokalen Arbeitsordner. Alle folgenden Dateipfade beziehen sich auf diesen Ordner; Quellen und vorbereitete Dokumentationsvorlagen liegen in `documentation/`.

Für die praktische Arbeit benötigen Sie QGIS, den geprüften GBIF-Punktlayer aus Unit 11 sowie die bereitgestellten Linien- und Polygondaten. Falls Ihr Ergebnis aus Unit 11 nicht verfügbar ist, wird ein einheitlicher Ersatzlayer bereitgestellt.

Speichern Sie die unveränderten Eingangsdaten, eigene Ausgaben und Metadaten erneut in getrennten Unterordnern. Verwenden Sie für räumliche Messungen und Auswahlen das vorgegebene Projekt- und Ausgabe-CRS.

Verwenden Sie dasselbe Projekt-CRS wie seit Unit 10: **`EPSG:25832`**. Erwarteter Eingang ist `unit11_results.gpkg/gbif_checked`; der Ersatzlayer muss dasselbe Schema besitzen.

Das verbindliche Übergabeprodukt ist `data_output/unit12_results.gpkg` mit:

* `schutzgebiete_auswahl`,
* `gbif_in_schutzgebieten` und
* `gewaesser_an_schutzgebieten`.

## Ablauf der Sitzung

Die Sitzung dauert **90 Minuten**: 10 Minuten JiTT-Besprechung, 75 Minuten für neue Inhalte und angeleitete Übungen sowie 5 Minuten Abschluss. Erklärungen und Beispiele setzen keine vorherige Lektüre der Kursseiten voraus. Kurze Austauschrunden finden mit den Sitznachbarinnen und Sitznachbarn statt.

| Zeit | Aktivität |
|---:|---|
| 0–10 Minuten | JiTT-Antworten zu Unit 11 besprechen und Verständnisfragen klären |
| 10–25 Minuten | Linien, Polygone und räumliche Beziehungen einschließlich eines Grenzfalls gemeinsam klären |
| 25–35 Minuten | An einem Geoportal Metadaten, Download und WFS unterscheiden |
| 35–50 Minuten | Vorbereitete Layer laden, Schutzgebiete über Attribute auswählen und als Vergleichslayer speichern |
| 50–70 Minuten | GBIF-Punkte und Gewässer mit „schneidet“ räumlich auswählen |
| 70–80 Minuten | Beide räumlichen Ergebnisse exportieren und prüfen |
| 80–85 Minuten | Ergebniszahlen und Unsicherheit an einer Schutzgebietsgrenze besprechen |
| 85–90 Minuten | Zentrale Ergebnisse sichern, eine Exit-Ticket-Frage gemeinsam beantworten und auf JiTT hinweisen |

### Schwerpunkt und Umfang

* **Kernübung:** Wir arbeiten mit einem vorgegebenen Schutzgebiets- und Gewässerdatensatz. Nach einer angeleiteten Attributauswahl der Schutzgebiete wählen wir zuerst Punkte und anschließend Gewässer räumlich aus.
* **Gemeinsame Besprechung:** Der Weg vom Geoportal zum Datenpaket wird demonstriert. „Schneidet“ und „liegt innerhalb“ vergleichen wir an einem Punkt auf der Polygongrenze.
* **Freiwillige Vertiefung:** Eigene Portalsuche, WFS-Einrichtung, das Berechnen zusätzlicher Längen- und Flächenattribute sowie weitere Auswahlvarianten gehören nicht zum Pflichtumfang.
* **Ergebnissicherung:** `schutzgebiete_auswahl`, `gbif_in_schutzgebieten` und `gewaesser_an_schutzgebieten` werden in `unit12_results.gpkg` gespeichert. Auswahlregeln und Featurezahlen werden kurz protokolliert.

Die ausführlichen Unterseiten dienen auch als Nachschlagewerk. Für die Sitzung gilt die oben beschriebene Auswahl; weitere Übungen sind freiwillige Vertiefung. Nicht abgeschlossene Arbeit wird nicht als Hausaufgabe nachgeholt. Zwischen den Terminen beantworten Sie ausschließlich die **JiTT-Fragen zu Unit 12 in ILIAS**.

<!-- Hinweise für Lehrende zur 90-Minuten-Sitzung:
Kleine räumliche Ausschnitte, eine konkrete Attributregel und ein Quellenblatt vorbereiten. Die ausgewählten Schutzgebiete vor der räumlichen Auswahl als eigenen Layer sichern und als Vergleichslayer verwenden. Für Portalprobleme eine lokale Metadatenseite oder einen Screenshot sowie geprüfte Ergebnislayer bereithalten. Bei Zeitverlust die zweite räumliche Auswahl gemeinsam demonstrieren und das geprüfte Ergebnis bereitstellen.
Bei mehr Klärungsbedarf im JiTT-Block einen zusätzlichen Vergleich oder eine Übungsvariante kürzen. Ergebnissicherung und Abschluss beibehalten. Aus den folgenden Exit-Ticket-Fragen eine passend zur Sitzung auswählen und kurz gemeinsam auflösen.
-->

## Exit-Ticket

Wir wählen zum Abschluss eine der folgenden Fragen aus und beantworten sie gemeinsam ohne Nachschlagen:

1. Wodurch unterscheiden sich Auswahl und neu gespeicherter Ergebnislayer?
2. Welche räumliche Beziehung wurde für Punkte beziehungsweise Gewässer verwendet?
3. Warum benötigen Messungen ein geeignetes projiziertes CRS?

<a id="transfer-für-lehramtsstudierende"></a>

## Gemeinsam einen räumlichen Grenzfall erklären

Diese Aktivität bearbeiten alle Studierenden im Zeitblock **80–85 Minuten**. Betrachten Sie einen schematischen Beobachtungspunkt genau auf einer Schutzgebietsgrenze. Besprechen Sie **2 Minuten zu zweit**:

1. Wird der Punkt bei „schneidet“ berücksichtigt, und wie unterscheidet sich das von „liegt innerhalb“?
2. Was können wir über die tatsächliche Lage der Beobachtung sagen, wenn ihre Koordinate unsicher ist?

Wir klären die Antworten **3 Minuten im Plenum** und beziehen sie auf die Auswahlregel unserer Übung. Halten Sie eine Einschränkung der räumlichen Aussage im Ergebnisprotokoll fest.

<!-- Erwartung: intersects berücksichtigt den Randpunkt, within für einen Punkt auf dem Polygonrand nicht. Eine rechnerisch eindeutige Auswahl beseitigt die Unsicherheit der Beobachtungskoordinate nicht. -->

<!-- Notizen: Ab hier folgen Vermerke, welche als Gedankenstütze oder Erinnerung dienen aber noch nicht in der vorhandenen Form veröffentlicht werden sollen. -->

<!--
Möglicher Einstieg:
- GBIF-Punkte allein zeigen und fragen: „Welche Beobachtungen liegen in einem Schutzgebiet?“
- Danach Schutzgebietspolygone einblenden und diskutieren, welche neue Information entsteht.

Didaktische Schwerpunkte:
- Punkt bleibt Teil des Vektormodells; Unit 12 ergänzt Linie und Polygon.
- Kartensymbol und tatsächliche Geometrie unterscheiden.
- Räumliche Auswahl als erste echte GIS-Operation einführen.
- „innerhalb“ und „schneidet“ an Grenzfällen anschaulich unterscheiden.
- Messungen nur in einem geeigneten projizierten CRS durchführen.

Vor Durchführung ergänzen:
- Gewässer- und Schutzgebietsdatensatz
- Geoportal- und Metadatenlinks
- Datenstand, Lizenz und Quellenangabe
- Projekt- und Ausgabe-CRS
- bereitgestellter GBIF-Punktlayer

Geplante Unterseiten:
- unit12-01_vektordaten.md
- unit12-02_geoportale.md
- unit12-03_vektoren_qgis.md
- unit12-04_assignment.md
-->
