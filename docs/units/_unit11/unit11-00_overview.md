---
title: Überblick
published: true
toc: true
header:
  image: /assets/images/unit11/hero-unit11.jpg
  image_description: "Wald- und Kulturlandschaft mit verteilten Beobachtungspunkten und angedeuteten Unsicherheitsbereichen"
  caption: "KI-generierte Illustration, bearbeitet für diesen Kurs"
---

<!-- Rückblick: Welche Themeninhalte wurden in der letzten Kurssitzung bearbeitet? Sind Fragen zur letzten Kurssitzung offen geblieben? -->

## Rückblick & Fragen

In der letzten Kurssitzung haben wir Vektor und Raster als grundlegende Modelle räumlicher Daten kennengelernt. Wir haben erste lokale Layer in QGIS geladen, ein Projekt organisiert und einen WMS aus einem Geoportal eingebunden. Dabei wurde deutlich, dass Datenmodell, Datenquelle und Darstellungsform voneinander unterschieden werden müssen.

Zu Beginn besprechen wir **10 Minuten lang die JiTT-Antworten zu Unit 10**. An ein bis zwei ausgewählten Verständnisfragen klären wir die wichtigsten offenen Punkte und knüpfen an die vorige Sitzung an.

<!-- Introtext: Allgemeine Einleitung zum Thema im neuen Lernabschnitt und Verbindung zum vorangegangenen Thema. Worum geht es, welche Inhalte werden bearbeitet und warum sind diese wichtig? -->

## Einführung in Lernabschnitt 11

In dieser Unit betrachten wir den ersten Vektordatentyp genauer: **Punktdaten**. Punkte eignen sich, wenn für eine Fragestellung vor allem die Position eines räumlichen Objektes oder Ereignisses wichtig ist. Typische Beispiele sind Messstationen, GPS-Positionen, Probeflächen oder Fundorte von Arten.

Als reales Forschungsbeispiel verwenden wir Beobachtungsdaten aus der **Global Biodiversity Information Facility (GBIF)**. GBIF führt Biodiversitätsdaten vieler Einrichtungen und Projekte zusammen und macht sie über ein gemeinsames Portal zugänglich. Ein einzelner Datensatz kann beispielsweise dokumentieren, dass eine bestimmte Art zu einem bestimmten Zeitpunkt an einem bestimmten Ort beobachtet oder gesammelt wurde.

Am Beispiel des Feuersalamanders untersuchen wir, wie aus einer Tabelle mit Längen- und Breitengraden ein Punktlayer entsteht. Gleichzeitig beschäftigen wir uns mit Datenqualität und Interpretation: Ein Punkt auf der Karte ist ein Nachweis – nicht automatisch eine vollständige Aussage über die tatsächliche Verbreitung einer Art.

<!-- Aktuelle Lerneinheit: Welcher konkrete Inhalt erwartet die Studierenden? -->

## In dieser Lerneinheit ...

In dieser Lerneinheit beschäftigen wir uns mit drei aufeinander aufbauenden Fragen:

1. **Wie sind Punktdaten aufgebaut?**  
   Wir betrachten Punkte als Vektorfeatures, verbinden Geometrien mit Attributen und unterscheiden Position, Beobachtung und dargestelltes Objekt.

2. **Was enthalten Biodiversitätsdaten von GBIF?**  
   Wir lernen Occurrence Records, wichtige Datenfelder, Filter, Lizenzen, Zitation und typische Qualitätsprobleme kennen.

3. **Wie werden tabellarische Beobachtungen in QGIS zu Punkten?**  
   Wir importieren Längen- und Breitengrade aus einer Textdatei, prüfen CRS und Lage, untersuchen Attribute, filtern Datensätze und speichern einen dauerhaften Punktlayer.

Die wiederkehrende Arbeitslogik lautet:

> **Fragestellung → Datenquelle → Tabellenstruktur → Qualitätsprüfung → Punktlayer → Interpretation**

<!-- Lernziele: Was sollten Studierende am Ende dieser Lerneinheit wissen und anwenden können? -->

## Lernziele

### Verbindliche Kernziele

Am Ende der gemeinsamen Sitzung sind Studierende in der Lage, ...

* Geometrie und Attribute eines Punktfeatures zu unterscheiden und einen GBIF Occurrence Record als dokumentierten Nachweis einzuordnen,
* Koordinatenfelder einer Textdatei zu erkennen, auf Plausibilität zu prüfen und mit dem richtigen Import-CRS als Punktlayer in QGIS zu laden,
* zentrale GBIF-Felder und Einschränkungen der Beobachtungsdaten zu beurteilen und eine begründete Qualitätsregel als Auswahl anzuwenden,
* die ausgewählten Punktfeatures in das gemeinsame Ausgabe-CRS zu transformieren, als GeoPackage zu speichern und das Ergebnis zu kontrollieren und
* Datenquelle, Lizenz, Auswahlregel und Verarbeitung zu dokumentieren sowie eine durch die Daten gedeckte Aussage zur Punktkarte zu formulieren.

### Vertiefung und Nachschlagen

Die ausführlichen Unterseiten ermöglichen außerdem, ...

* weitere Anwendungen und Grenzen des Punktmodells zu vergleichen,
* eigene GBIF-Suchen und Downloads einschließlich DOI und Zitation vorzubereiten und
* zusätzliche zeitliche und fachliche Filter, Dublettenprüfungen, Qualitätsflags und Symbolisierungen zu untersuchen.

<!-- Organisatorisches: Gibt es Formalitäten, welche noch geklärt werden sollten? -->

## Organisatorisches

[Marburger Übungspaket und Anleitung]({{ '/material/marburg.html' | relative_url }}). Entpacken Sie das gesamte Paket in einen lokalen Arbeitsordner. Alle folgenden Dateipfade beziehen sich auf diesen Ordner; Quellen und vorbereitete Dokumentationsvorlagen liegen in `documentation/`.

Für die praktische Arbeit benötigen Sie QGIS sowie die bereitgestellte Auswahl von GBIF-Beobachtungen. Verwenden Sie während der Lehrveranstaltung den vorbereiteten Datensatz, damit alle mit derselben dokumentierten Datenversion arbeiten.

Verwenden Sie **QGIS `3.40`** und das gemeinsame Projekt-CRS **`EPSG:25832`**.

Das verbindliche Übergabeprodukt dieser Unit ist:

```text
data_output/unit11_results.gpkg
└── gbif_checked
```

Falls das eigene Ergebnis nicht verwendbar ist, steht ein schemaidentischer Ersatzlayer bereit: `ersatz/unit11_results.gpkg`, Layer `gbif_checked`, im Übungspaket.

## Ablauf der Sitzung

Die Sitzung dauert **90 Minuten**: 10 Minuten JiTT-Besprechung, 75 Minuten für neue Inhalte und angeleitete Übungen sowie 5 Minuten Abschluss. Erklärungen und Beispiele setzen keine vorherige Lektüre der Kursseiten voraus. Kurze Austauschrunden finden mit den Sitznachbarinnen und Sitznachbarn statt.

| Zeit | Aktivität |
|---:|---|
| 0–10 Minuten | JiTT-Antworten zu Unit 10 besprechen und Verständnisfragen klären |
| 10–25 Minuten | Punktfeature, Beobachtung und Verbreitung an einer Karte und einem GBIF-Record unterscheiden |
| 25–35 Minuten | Vorbereitete Tabelle, Koordinatenfelder, Import-CRS und Quellenangabe gemeinsam prüfen |
| 35–60 Minuten | Tabelle angeleitet importieren, Lage prüfen und eine begründete Qualitätsregel anwenden |
| 60–75 Minuten | Auswahl als `gbif_checked` exportieren, erneut laden und kontrollieren |
| 75–85 Minuten | Qualitätsentscheidung dokumentieren und eine vorsichtige Aussage zur Punktkarte formulieren |
| 85–90 Minuten | Zentrale Ergebnisse sichern, eine Exit-Ticket-Frage gemeinsam beantworten und auf JiTT hinweisen |

### Schwerpunkt und Umfang

* **Kernübung:** Wir importieren die bereitgestellte GBIF-Tabelle und prüfen Koordinatenreihenfolge, Import-CRS und Lage. Eine gemeinsame Qualitätsregel wird auf den Datensatz angewendet; die Entscheidung und betroffene Recordzahl werden dokumentiert.
* **Gemeinsame Besprechung:** An einem GBIF-Record erläutern wir Herkunft, DOI, Lizenz und Koordinatenunsicherheit. Fehlende Unsicherheitsangaben bedeuten nicht automatisch hohe Genauigkeit.
* **Freiwillige Vertiefung:** Eigene GBIF-Suche und Downloads, weitere Filtervarianten, systematische Dublettenprüfung und zusätzliche Symbolisierungen sind nicht Teil der Kernübung.
* **Ergebnissicherung:** `unit11_results.gpkg/gbif_checked` sowie Quellenangabe, Auswahlregel und Recordzahlen werden in der Sitzung gesichert. Die Punktkarte wird als Karte dokumentierter Nachweise interpretiert.

Die ausführlichen Unterseiten dienen auch als Nachschlagewerk. Für die Sitzung gilt die oben beschriebene Auswahl; weitere Übungen sind freiwillige Vertiefung. Nicht abgeschlossene Arbeit wird nicht als Hausaufgabe nachgeholt. Zwischen den Terminen beantworten Sie ausschließlich die **JiTT-Fragen zu Unit 11 in ILIAS**.

<!-- Hinweise für Lehrende zur 90-Minuten-Sitzung:
Einen kleinen dokumentierten GBIF-Ausschnitt, eine passende Qualitätsregel und eine Dokumentationsvorlage mit DOI und Lizenz vorbereiten. Die Regel muss zum tatsächlichen Schema passen; keine pauschale Löschung aller Records mit Qualitätsflags. Schemaidentischen Ersatzlayer für technische Probleme bereithalten, damit Exportprüfung und Interpretation gemeinsam abgeschlossen werden können.
Bei mehr Klärungsbedarf im JiTT-Block einen zusätzlichen Vergleich oder eine Übungsvariante kürzen. Ergebnissicherung und Abschluss beibehalten. Aus den folgenden Exit-Ticket-Fragen eine passend zur Sitzung auswählen und kurz gemeinsam auflösen.
-->

## Exit-Ticket

Wir wählen zum Abschluss eine der folgenden Fragen aus und beantworten sie gemeinsam ohne Nachschlagen:

1. Weshalb ist ein GBIF-Punkt nicht automatisch eine exakt lokalisierte Lebendbeobachtung?
2. Welche drei Angaben müssen beim Import von `decimalLongitude` und `decimalLatitude` stimmen?
3. Warum beschreibt `gbif_checked` dokumentierte Nachweise und nicht die vollständige Verbreitung einer Art?

<a id="transfer-für-lehramtsstudierende"></a>

## Gemeinsam eine Punktkarte interpretieren

Diese Aktivität bearbeiten alle Studierenden im Zeitblock **75–85 Minuten** anhand der erzeugten Punktkarte oder des bereitgestellten Ersatzes. Prüfen Sie **2 Minuten zu zweit** die Aussage:

> „In Bereichen ohne Punkte kommt der Feuersalamander nicht vor.“

1. Erklären Sie, warum die Karte diese Aussage nicht belegt.
2. Ersetzen Sie die Aussage durch einen fachlich angemessenen Satz über die dargestellten Nachweise.

Wir besprechen **3 Minuten im Plenum** ausgewählte Formulierungen. Halten Sie den gemeinsam geklärten Satz im kurzen Ergebnisprotokoll fest.

<!-- Erwartung: Die Karte zeigt dokumentierte Nachweise des verwendeten Datenausschnitts. Fehlende Punkte können unter anderem auf fehlende Erfassung oder die Datenauswahl zurückgehen; sie belegen keine Abwesenheit. -->

<!-- Notizen: Ab hier folgen Vermerke, welche als Gedankenstütze oder Erinnerung dienen aber noch nicht in der vorhandenen Form veröffentlicht werden sollen. -->

<!--
Mögliche Einstiegsfrage:
- Eine Karte mit GBIF-Punkten des Feuersalamanders zeigen und fragen: „Wo kommt die Art vor?“
- Anschließend problematisieren: Zeigt die Karte Vorkommen, Beobachtungen oder Beobachtungsaktivität?

Didaktische Schwerpunkte:
- Punkte ausdrücklich als Vektordaten benennen.
- Beobachtung, Individuum, Fundort und Punktfeature sprachlich unterscheiden.
- Datenqualität nicht als nachträgliches Spezialthema, sondern bei jedem Arbeitsschritt behandeln.
- Keine Verbreitungskarte im strengen Sinn versprechen; zunächst Nachweisdaten kartieren.

Vor Durchführung ergänzen:
- API-Snapshot und Quelldatensatz-DOI
- Datenstand und Filter des Downloads
- verwendeter Artenname beziehungsweise alternatives Beispiel
- Deutschland- oder Hessen-Grenzlayer
- lokale Arbeits- und Datenpfade

Geplante Unterseiten:
- unit11-01_punktdaten.md
- unit11-02_gbif.md
- unit11-03_punkte_qgis.md
- unit11-04_assignment.md
-->
