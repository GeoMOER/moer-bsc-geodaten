---
title: Überblick
published: true
toc: true
header:
  image: /assets/images/unit10/hero-unit10.jpg
  image_description: "Luftbildlandschaft mit überlagerten Punkten, Linien, Polygonflächen und Rasterzellen"
  caption: "KI-generierte Illustration, bearbeitet für diesen Kurs"
---

<!-- Rückblick: Welche Themeninhalte wurden in der letzten Kurssitzung bearbeitet? Sind Fragen zur letzten Kurssitzung offen geblieben? -->

## Rückblick & Fragen

In der letzten Kurssitzung haben wir die grundlegenden Eigenschaften von Geodaten kennengelernt. Wir haben untersucht, wie Orte durch Koordinaten beschrieben werden, warum Koordinaten nur gemeinsam mit einem Koordinatenreferenzsystem eindeutig sind und weshalb jede Übertragung der gekrümmten Erdoberfläche auf eine ebene Karte zu Verzerrungen führt.

Zu Beginn besprechen wir **10 Minuten lang die JiTT-Antworten zu Unit 09**. An ein bis zwei ausgewählten Verständnisfragen klären wir die wichtigsten offenen Punkte und knüpfen an die vorige Sitzung an.

<!-- Introtext: Allgemeine Einleitung zum Thema im neuen Lernabschnitt und Verbindung zum vorangegangenen Thema. Worum geht es, welche Inhalte werden bearbeitet und warum sind diese wichtig? -->

## Einführung in Lernabschnitt 10

Wir wissen nun, wodurch Daten einen räumlichen Bezug erhalten. Damit ist jedoch noch nicht entschieden, **wie** ein Ausschnitt der Wirklichkeit in einem Geodatensatz dargestellt werden soll. Eine Baumbeobachtung kann als Punkt erfasst werden, eine Straße als Linie und ein Landkreis als Fläche. Höhe oder Temperatur lassen sich dagegen häufig sinnvoll als regelmäßiges Raster beschreiben.

Geodaten sind deshalb keine vollständigen Abbilder der Realität, sondern zweckgebundene **Modelle**. Das gewählte Datenmodell entscheidet, welche Informationen gespeichert werden können und welche räumlichen Fragen sich später beantworten lassen.

In diesem Lernabschnitt lernen wir die beiden grundlegenden Geodatenmodelle **Vektor** und **Raster** kennen. Anschließend beginnen wir praktisch mit **QGIS**, einem freien Geoinformationssystem. Darin können wir Geodaten öffnen, gemeinsam darstellen, untersuchen und später auch bearbeiten und analysieren.

<!-- Aktuelle Lerneinheit: Welcher konkrete Inhalt erwartet die Studierenden? -->

## In dieser Lerneinheit ...

In dieser Lerneinheit beschäftigen wir uns mit drei grundlegenden Fragen:

1. **Wie wird die räumliche Wirklichkeit zu einem Datenmodell?**  
   Wir unterscheiden Vektor- und Rasterdaten und betrachten, wie Punkte, Linien, Polygone und Rasterzellen unterschiedliche räumliche Phänomene repräsentieren.

2. **Wie lassen sich Geodaten in einem GIS untersuchen?**  
   Wir lernen die wichtigsten Bereiche der QGIS-Oberfläche kennen, öffnen ein Projekt, laden Layer und betrachten deren räumliche und tabellarische Informationen.

3. **Woher kommen Geodaten und wie können sie eingebunden werden?**  
   Wir unterscheiden lokale Dateien von webbasierten Geodatendiensten und vollziehen an einer gemeinsamen Demonstration nach, wie ein Web Map Service, kurz WMS, in QGIS eingebunden wird.

Dabei wechseln sich kurze konzeptionelle Abschnitte und praktische Arbeitsschritte ab. Ziel ist noch keine umfassende Beherrschung von QGIS, sondern ein sicheres Grundverständnis von **Datenmodell, Layer, Karte, Attributen, Projekt und Datenquelle**.

<!-- Lernziele: Was sollten Studierende am Ende dieser Lerneinheit wissen und anwenden können? -->

## Lernziele

### Verbindliche Kernziele

Am Ende der gemeinsamen Sitzung sind Studierende in der Lage, ...

* Vektor und Raster als zweckgebundene Datenmodelle zu unterscheiden und für einfache räumliche Fragen ein passendes Modell beziehungsweise einen passenden Vektorgeometrietyp vorzuschlagen,
* QGIS-Projekt, Layer, Geodatendatei und Datenquelle voneinander zu unterscheiden,
* die zentralen Bereiche der QGIS-Oberfläche zu nutzen, um einen Vektor- und einen Rasterlayer zu laden, ein- und auszublenden sowie Attribute und CRS-Informationen zu prüfen,
* ein QGIS-Projekt mit nachvollziehbarer Ordnerstruktur zu speichern, erneut zu öffnen und die Verfügbarkeit seiner Datenquellen zu kontrollieren und
* lokale Geodatendateien von einem Web Map Service zu unterscheiden und die Einbindung eines vorgegebenen WMS in QGIS nachzuvollziehen.

### Vertiefung und Nachschlagen

Die ausführlichen Unterseiten ermöglichen außerdem, ...

* zu untersuchen, wie Fragestellung und Maßstab die Modellierung derselben räumlichen Wirklichkeit verändern,
* weitere Wege zum Laden und Organisieren von Layern kennenzulernen und
* Geoportale, Downloads und weitere Geodatendienste wie WFS genauer zu vergleichen.

<!-- Organisatorisches: Gibt es Formalitäten, welche noch geklärt werden sollten? -->

## Organisatorisches

Laden Sie das [Marburger Übungspaket mit Anleitung]({{ '/material/marburg.html' | relative_url }}) herunter und entpacken Sie es vollständig in einen lokalen Arbeitsordner. Alle folgenden Dateipfade beziehen sich auf diesen Ordner; Quellen und vorbereitete Dokumentationsvorlagen liegen in `documentation/`.

In dieser Lerneinheit arbeiten wir erstmals praktisch mit QGIS. Stellen Sie vor Beginn sicher, dass **QGIS `3.40`** auf dem verwendeten Rechner gestartet werden kann. Die Sprache der Oberfläche darf Deutsch oder Englisch sein; die Anleitung nennt zentrale Begriffe bei Bedarf in beiden Sprachen.

Benötigt werden:

* Übungsdaten: [Marburger Übungspaket und Anleitung]({{ '/material/marburg.html' | relative_url }}),
* lokaler Vektorlayer: `data_raw/marburg_basis.gpkg`, Layer `gewaesser`,
* lokaler Rasterlayer: `data_raw/dgm_marburg_10m.tif`,
* Projekt-CRS: `EPSG:25832`,
* WMS-Verbindung: HLNUG Schutzgebiete Hessen, Layer `Naturschutzgebiete`; Dienstadresse im [Abschnitt Datenquellen](unit10-03_datenquellen.html) und
* `ersatz/wms_schutzgebiete.png` samt `ersatz/wms_capabilities.xml` und `documentation/quellen.md` für den Fall, dass der WMS während der Sitzung ausfällt.

Bitte speichern Sie Ihr QGIS-Projekt und alle zugehörigen Dateien in einem gemeinsamen, eindeutig benannten Arbeitsordner. Ein Projekt speichert Verweise auf die verwendeten Daten; es enthält die eingebundenen Datensätze in der Regel nicht selbst.

## Ablauf der Sitzung

Die Sitzung dauert **90 Minuten**: 10 Minuten JiTT-Besprechung, 75 Minuten für neue Inhalte und angeleitete Übungen sowie 5 Minuten Abschluss. Erklärungen und Beispiele setzen keine vorherige Lektüre der Kursseiten voraus. Kurze Austauschrunden finden mit den Sitznachbarinnen und Sitznachbarn statt.

| Zeit | Aktivität |
|---:|---|
| 0–10 Minuten | JiTT-Antworten zu Unit 09 besprechen und Verständnisfragen klären |
| 10–22 Minuten | Vektor und Raster am selben Landschaftsausschnitt vergleichen; Modelle gemeinsam zuordnen |
| 22–30 Minuten | Projekt, Layer, Datendatei und Datenquelle an einem QGIS-Beispiel unterscheiden |
| 30–55 Minuten | Angeleitet Arbeitsordner und Projekt anlegen sowie je einen Vektor- und Rasterlayer laden |
| 55–68 Minuten | Attribute, Datenquellen und CRS beider Layer prüfen und kurz dokumentieren |
| 68–78 Minuten | Projekt speichern, QGIS schließen, Projekt erneut öffnen und Datenquellen kontrollieren |
| 78–85 Minuten | WMS am Beamer oder mit dem Offline-Ersatz demonstrieren und mit lokalen Daten vergleichen; bei fertigem Projekt optional selbst mitmachen |
| 85–90 Minuten | Zentrale Ergebnisse sichern, eine Exit-Ticket-Frage gemeinsam beantworten und auf JiTT hinweisen |

### Schwerpunkt und Umfang

* **Kernübung:** Wir verwenden genau einen lokalen Vektorlayer und einen Rasterlayer. Am Vektorlayer verbinden wir ein Feature in der Karte mit seiner Tabellenzeile; anschließend prüfen wir Datenquellen und CRS beider Layer. Das lokale Projekt wird gespeichert, geschlossen und erfolgreich erneut geöffnet.
* **Gemeinsame Besprechung:** Die WMS-Adresse und der Layer sind vorgegeben. Die Lehrperson zeigt die Verbindung am Beamer und wechselt bei einem Dienstausfall ohne Fehlersuche zum Offline-Ersatz. Studierende mit vollständig geprüftem lokalem Projekt können die Schritte auf dem eigenen Gerät mitvollziehen.
* **Freiwillige Vertiefung:** Die selbstständige WMS-Einrichtung, freie Geoportalsuche, weitere Dienste, alternative Ladewege und zusätzliche Modellierungsbeispiele bleiben zum Nachschlagen verfügbar.
* **Ergebnissicherung:** Das gespeicherte Projekt lässt sich mit den lokalen Daten erneut öffnen. Ein kurzes Protokoll enthält Datenquellen, Datenmodelle, CRS und das Ergebnis des Öffnungstests.

Die ausführlichen Unterseiten dienen auch als Nachschlagewerk. Für die Sitzung gilt die oben beschriebene Auswahl; weitere Übungen sind freiwillige Vertiefung. Nicht abgeschlossene Arbeit wird nicht als Hausaufgabe nachgeholt. Zwischen den Terminen beantworten Sie ausschließlich die **JiTT-Fragen zu Unit 10 in ILIAS**.

<!-- Hinweise für Lehrende zur 90-Minuten-Sitzung:
QGIS muss zu Sitzungsbeginn startbereit sein. Ein kleines Datenpaket mit Ordnerstruktur und vorausgefüllter Dokumentationsvorlage vorbereiten; das Verteilen und Öffnen gehört zum Praxisblock. Das geprüfte lokale Projekt ist das verbindliche Ergebnis der Sitzung und wird vor dem WMS behandelt. Die WMS-Demonstration beginnt spätestens in Minute 78 und endet in Minute 85. Bei Verbindungsproblemen sofort am Ersatzmaterial vergleichen, ohne eine andere Adresse oder einen anderen Dienst zu suchen.
Bei mehr Klärungsbedarf im JiTT-Block einen zusätzlichen Vergleich oder eine Übungsvariante kürzen. Ergebnissicherung und Abschluss beibehalten. Aus den folgenden Exit-Ticket-Fragen eine passend zur Sitzung auswählen und kurz gemeinsam auflösen.
-->

## Exit-Ticket

Wir wählen zum Abschluss eine der folgenden Fragen aus und beantworten sie gemeinsam ohne Nachschlagen:

1. Was enthält eine `.qgz`-Projektdatei, und was enthält sie normalerweise nicht?
2. Woran erkennen Sie in QGIS, ob ein Layer Vektor- oder Rasterdaten enthält?
3. Weshalb eignet sich ein WMS als Hintergrund, aber meist nicht für eine Vektoranalyse?

<a id="transfer-für-lehramtsstudierende"></a>

## Gemeinsam Datenmodelle auswählen

Diese Aktivität bearbeiten alle Studierenden im Zeitblock **10–22 Minuten**. Betrachten Sie den gezeigten Landschaftsausschnitt und besprechen Sie **2 Minuten zu zweit**:

1. Wie würden Sie die Grenze eines Schutzgebiets darstellen?
2. Wie würden Sie die Geländehöhe im gesamten Ausschnitt darstellen?
3. Begründen Sie, welche Information das jeweilige Datenmodell für die Frage bereitstellt.

Anschließend sammeln wir **3 Minuten im Plenum** die Vorschläge. Wir halten gemeinsam fest, wie sich einzelne Objekte und ein flächendeckendes Wertefeld unterscheiden.

<!-- Erwartung: Ein Polygon beschreibt die Schutzgebietsfläche samt Grenze, ein Höhenraster das Wertefeld. Andere Modellierungen sind möglich, müssen aber zur Frage passen. -->

<!-- Notizen: Ab hier folgen Vermerke, welche als Gedankenstütze oder Erinnerung dienen aber noch nicht in der vorhandenen Form veröffentlicht werden sollen. -->

<!-- Hinweise für Lehrende:
Mögliche Einstiegsfrage:
- Wie könnte dieselbe Stadt auf einer Deutschlandkarte, einer Stadtkarte und in einem Satellitenbild dargestellt werden?

Mögliche Demonstrationen:
- Marburg als Punkt, Polygon und Ausschnitt eines Rasters zeigen
- ein QGIS-Projekt ohne die zugehörigen Datendateien öffnen und fehlende Layerpfade thematisieren
- denselben Datensatz als lokale Datei und einen vergleichbaren Inhalt als WMS gegenüberstellen

Didaktische Schwerpunkte:
- Vektor und Raster zunächst nur konzeptionell unterscheiden; die vertiefte praktische Arbeit folgt in den Units 11 bis 13.
- QGIS-Oberfläche nur so weit einführen, wie sie für die ersten Arbeitsschritte benötigt wird.
- Projektdatei und Datendatei von Beginn an sprachlich sauber trennen.

Vor Durchführung prüfen beziehungsweise ergänzen:
- verwendete QGIS-Installation und Arbeitsumgebung
- Downloadpfad der Übungsdaten
- URL und Name des verwendeten WMS

Unterseiten:
- unit10-01_datenmodelle.html
- unit10-02_qgis.html
- unit10-03_datenquellen.html
- unit10-04_assignment.html
-->
