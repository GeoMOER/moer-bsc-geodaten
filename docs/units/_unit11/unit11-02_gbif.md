---
title: Biodiversitätsdaten von GBIF
published: true
toc: true
header:
  image: /assets/images/unit11/hero-unit11.jpg
  image_description: "Wald- und Kulturlandschaft mit verteilten Beobachtungspunkten und angedeuteten Unsicherheitsbereichen"
  caption: "KI-generierte Illustration, bearbeitet für diesen Kurs"
---

<!-- Introtext: Reale Punktdaten anhand einer wissenschaftlich relevanten Dateninfrastruktur kennenlernen. -->

## Was ist GBIF?

![Der Kurs verwendet einen dokumentierten GBIF-API-Snapshot ohne eigenen Download-DOI. Der DOI 10.15468/uc1apo bezeichnet den Quelldatensatz; ein optionaler eigener Occurrence Download würde einen eigenen DOI erhalten. Danach folgen Tabellenprüfung, Punktimport, Qualitätsregel und dokumentierter Export.]({{ '/assets/images/unit11/gbif-workflow.svg' | relative_url }})

Die **Global Biodiversity Information Facility (GBIF)** ist eine internationale Dateninfrastruktur für Informationen zur biologischen Vielfalt. Einrichtungen und Projekte aus vielen Ländern veröffentlichen darüber Daten zu Arten und anderen Organismen nach gemeinsamen Standards.

Über GBIF können unter anderem Daten aus:

* naturkundlichen Sammlungen,
* wissenschaftlichen Erfassungsprogrammen,
* Citizen-Science-Projekten,
* Umweltbeobachtungen,
* Literaturauswertungen und
* automatisierten Sensoren

gemeinsam gesucht und heruntergeladen werden.

GBIF ist dabei nicht die ursprüngliche Quelle jeder einzelnen Beobachtung. Die Daten stammen von vielen veröffentlichenden Einrichtungen und Datensätzen. GBIF macht sie auffindbar, vereinheitlicht wichtige Felder und ergänzt Prüfhinweise.

> **Merksatz:** GBIF führt Daten vieler Quellen zusammen. Herkunft und Verantwortung des jeweiligen Datensatzes bleiben deshalb für die Interpretation wichtig.

## Was ist ein Occurrence Record?

Ein **Occurrence Record** dokumentiert einen Nachweis, dass ein Organismus beziehungsweise ein Taxon an einem bestimmten Ort und häufig zu einem bestimmten Zeitpunkt erfasst wurde.

Ein solcher Nachweis kann beispielsweise beruhen auf:

* einer direkten menschlichen Beobachtung,
* einem Foto oder einer Tonaufnahme,
* einem gesammelten Museumsexemplar,
* einer Probe,
* einem Literaturbeleg oder
* einer maschinellen Erfassung.

Der Begriff *Occurrence* ist daher weiter als „Beobachtung“. Das Feld `basisOfRecord` beschreibt, auf welcher Grundlage der Datensatz beruht.

> **Wichtig:** Ein GBIF-Punkt bedeutet nicht automatisch, dass eine Person ein lebendes Tier genau an dieser Stelle gesehen hat.

## Herausgeber, Datensatz und einzelner Nachweis

GBIF-Daten besitzen mehrere Ebenen der Herkunft:

1. Eine **veröffentlichende Einrichtung** stellt Daten bereit.
2. Ein **Datensatz** bündelt zusammengehörige Records.
3. Ein **Occurrence Record** beschreibt einen einzelnen Nachweis.
4. GBIF verarbeitet und indexiert den Record für die gemeinsame Suche.

Bei einer wissenschaftlichen Nutzung müssen deshalb sowohl der konkrete GBIF-Download als auch die darin enthaltenen Datenquellen nachvollziehbar bleiben.

## Wichtige Datenfelder

GBIF-Downloads enthalten viele Spalten. Für einen ersten Einstieg sind besonders folgende Felder relevant:

| Feld | Bedeutung | Prüffrage |
|---|---|---|
| `gbifID` | von GBIF verwendete Kennung des Records | Ist jeder Datensatz unterscheidbar? |
| `occurrenceID` | vom Datenherausgeber vergebene Kennung | Lässt sich der Originalrecord identifizieren? |
| `scientificName` | übermittelter beziehungsweise interpretierter wissenschaftlicher Name | Welches Taxon wird genannt? |
| `species` | von GBIF zugeordnete Art | Wurde der Record tatsächlich bis zur Art bestimmt? |
| `taxonKey` | GBIF-Kennung des zugeordneten Taxons | Welchem Taxon in der GBIF-Taxonomie wurde er zugeordnet? |
| `basisOfRecord` | Grundlage des Nachweises | Beobachtung, Belegexemplar oder andere Quelle? |
| `occurrenceStatus` | gemeldeter Anwesenheitsstatus | Handelt es sich um einen Präsenz- oder Absenzrecord? |
| `eventDate` | Datum beziehungsweise Zeitraum des Ereignisses | Wann wurde erfasst? |
| `year` | von GBIF interpretiertes Jahr | Ist ein zeitlicher Filter möglich? |
| `decimalLongitude` | geographische Länge in Dezimalgrad | Ist der Wert plausibel? |
| `decimalLatitude` | geographische Breite in Dezimalgrad | Ist der Wert plausibel? |
| `coordinateUncertaintyInMeters` | angegebene räumliche Unsicherheit | Passt die Genauigkeit zur Fragestellung? |
| `countryCode` | Ländercode | Liegt der Punkt im erwarteten Land? |
| `recordedBy` | erfassende Person oder Personen | Ist die Erfassung dokumentiert? |
| `datasetKey` | Kennung des veröffentlichenden Datensatzes | Aus welcher Datenquelle stammt der Record? |
| `license` | Lizenz des Records | Darf er für den vorgesehenen Zweck genutzt werden? |
| `issue` | von GBIF vergebene Prüfhinweise | Welche möglichen Probleme wurden erkannt? |

Nicht jedes Feld ist in jedem Record ausgefüllt. Fehlende Werte müssen deshalb bewusst behandelt werden.

## Originalwerte und interpretierte Werte

GBIF übernimmt Daten aus sehr unterschiedlichen Quellen. Für eine gemeinsame Suche werden viele Angaben standardisiert und interpretiert. Beispielsweise können wissenschaftliche Namen taxonomisch zugeordnet, Datumsangaben vereinheitlicht und Koordinaten geprüft werden.

Ein GBIF-Download kann daher sowohl:

* von GBIF interpretierte Felder als auch
* ursprünglich veröffentlichte Angaben

enthalten. Die Interpretation erleichtert die gemeinsame Nutzung, ersetzt aber nicht die fachliche Prüfung. Bei auffälligen Records sollte nach Möglichkeit auch die ursprüngliche Angabe und der veröffentlichende Datensatz betrachtet werden.

## Nach einer Art suchen

Als Beispiel verwenden wir den **Feuersalamander** (*Salamandra salamandra*).

1. Öffnen Sie die GBIF-Webseite.
2. Suchen Sie nach dem wissenschaftlichen Namen `Salamandra salamandra`.
3. Öffnen Sie die passende Artseite.
4. Wechseln Sie zu den Occurrence Records.
5. Prüfen Sie Karte, Anzahl der Records und angebotene Filter.

Verwenden Sie möglichst den wissenschaftlichen Namen und kontrollieren Sie die taxonomische Zuordnung. Trivialnamen können mehrdeutig sein oder in verschiedenen Sprachen variieren.

## Suchergebnisse sinnvoll filtern

Für eine überschaubare und reproduzierbare Auswahl können unter anderem folgende Filter sinnvoll sein:

* **Taxon:** *Salamandra salamandra*
* **Land:** Deutschland
* **Koordinaten vorhanden:** ja
* **Zeitraum:** passend zur Fragestellung
* **Occurrence Status:** Präsenz, sofern für die Aufgabe erforderlich
* **Basis of Record:** gegebenenfalls auf bestimmte Nachweisarten begrenzen
* **Geospatial Issues:** je nach Ziel prüfen oder gezielt ausschließen

Jeder Filter verändert die fachliche Bedeutung des Ergebnisses. Dokumentieren Sie deshalb nicht nur die Anzahl der verbleibenden Records, sondern alle verwendeten Filter.

> **Wichtig:** „Koordinaten vorhanden“ bedeutet noch nicht „Koordinaten sind für meine Analyse ausreichend genau und korrekt“.

## Einen einzelnen Record prüfen

Öffnen Sie vor dem Download mehrere einzelne Records und prüfen Sie:

* wissenschaftlichen Namen und taxonomische Zuordnung,
* Datum und Grundlage des Nachweises,
* Position und Koordinatenunsicherheit,
* veröffentlichenden Datensatz und Einrichtung,
* Lizenz,
* von GBIF gemeldete Issues sowie
* gegebenenfalls Verweise auf Medien oder Originalinformationen.

Diese Stichprobe hilft zu verstehen, welche heterogenen Quellen später in einer gemeinsamen Tabelle zusammengeführt werden.

## GBIF-Issues und Qualitätsflags

GBIF prüft Records automatisiert und kennzeichnet mögliche Probleme im Feld `issue`. Beispiele betreffen:

* nicht interpretierbare oder außerhalb des gültigen Wertebereichs liegende Koordinaten,
* widersprüchliche räumliche Angaben,
* Probleme mit Datum oder Taxonomie und
* mögliche Abweichungen zwischen Koordinaten und angegebenem Land.

Ein leerer `issue`-Eintrag ist kein Beweis vollständiger Fehlerfreiheit. Umgekehrt muss ein markierter Record nicht für jede Fragestellung unbrauchbar sein. Die Bedeutung des Flags muss gelesen und im Kontext der geplanten Analyse beurteilt werden.

> **Arbeitsregel:** Qualitätsflags unterstützen die Prüfung; sie ersetzen keine fachliche Entscheidung.

## Koordinatenunsicherheit und sensible Daten

Die räumliche Genauigkeit von Biodiversitätsdaten kann stark variieren. Das Feld `coordinateUncertaintyInMeters` beschreibt – sofern angegeben – die Unsicherheit der Position in Metern.

Hohe oder fehlende Unsicherheitswerte können für kleinräumige Analysen problematisch sein. Zusätzlich können genaue Fundorte gefährdeter oder sensibler Arten zum Schutz absichtlich verallgemeinert oder zurückgehalten werden.

Prüfen Sie deshalb:

* ob eine Unsicherheit angegeben ist,
* ob sie zur räumlichen Auflösung der Fragestellung passt,
* ob Koordinaten möglicherweise gerundet wurden und
* ob sensible Informationen absichtlich nicht punktgenau veröffentlicht sind.

## Beobachtungsbias

GBIF-Occurrence-Daten stammen häufig nicht aus einer flächendeckenden, überall gleich intensiven Stichprobe. Mehr Records finden sich oft:

* in der Nähe von Städten und Wegen,
* in gut zugänglichen Gebieten,
* an beliebten Beobachtungsorten,
* in Regionen mit aktiven Meldeplattformen oder Forschungseinrichtungen und
* für auffällige oder besonders interessante Arten.

Eine hohe Punktdichte kann daher sowohl häufiges Vorkommen als auch intensive Beobachtung und Meldung widerspiegeln.

Außerdem gilt:

> **Das Fehlen eines GBIF-Records ist ohne dokumentierte Suche kein Nachweis der Abwesenheit.**

## Daten herunterladen

Für wissenschaftliche Arbeiten sollte eine gefilterte Auswahl als dokumentierter **GBIF Occurrence Download** erzeugt werden. Dafür ist ein GBIF-Benutzerkonto erforderlich. Der Download wird vorbereitet und erhält eine dauerhafte Kennung in Form eines **DOI**.

Für die Lehrveranstaltung verwenden wir einen kleinen, festgehaltenen **API-Snapshot** aus einem Quelldatensatz. Er lässt sich ohne GBIF-Benutzerkonto als Bestandteil des [Marburger Übungspaket und Anleitung]({{ '/material/marburg.html' | relative_url }}) herunterladen.

| Angabe | Wert |
|---|---|
| Taxon | *Salamandra salamandra*, GBIF-Schlüssel 2431776 |
| Quelle | NABU&#124;naturgucker, Datensatz `6ac3f774-d9fb-4796-b3e9-92bf6c81c084` |
| räumlicher Filter | 20 × 20 km um Marburg; Grenzen in `documentation/quellen.md` |
| zeitlicher Filter | keine zusätzliche zeitliche Einschränkung |
| weitere Filter | Nachweis vorhanden, Koordinaten vorhanden; einheitlicher Quelldatensatz |
| Abrufdatum | 08.09.2026 |
| Datensatz-DOI | [10.15468/uc1apo](https://doi.org/10.15468/uc1apo) |
| eigener Download-DOI | keiner; der DOI oben bezeichnet den Quelldatensatz |
| bereitgestellte Datei | `data_raw/gbif_feuersalamander_marburg.csv`, 79 Nachweise |
| Lizenz | CC BY 4.0 |

Die genaue API-Abfrage, räumliche Auswahl und Eingangsprüfsummen sind im Paket dokumentiert. Bewahren Sie CSV, CSVT und den Ordner `documentation/` gemeinsam auf. In Unit 11 wenden wir darauf eine zusätzliche, begründete Regel zur Koordinatenunsicherheit an.

## GBIF-Daten korrekt zitieren

Ein GBIF-Download-DOI bezeichnet eine zeitlich festgehaltene Auswahl von Occurrence Records. Er ermöglicht, die verwendete Datengrundlage später nachzuvollziehen und die beteiligten Datenherausgeber anzuerkennen.

Verwenden Sie für eine Veröffentlichung die von GBIF bereitgestellte Zitation des konkreten Downloads. Ein allgemeiner Link auf die GBIF-Startseite oder eine dynamische Suchergebnisseite ersetzt diese Zitation nicht.

Wenn Sie die Daten nach dem Download filtern oder bereinigen, bleibt der ursprüngliche Download-DOI relevant. Dokumentieren Sie zusätzlich, welche Records lokal ausgeschlossen oder verändert wurden.

## Lizenzen beachten

Occurrence Records können aus verschiedenen Datensätzen mit unterschiedlichen Creative-Commons-Lizenzen stammen. Prüfen Sie die Lizenzfelder und die Bedingungen des Downloads, bevor Daten weitergegeben oder veröffentlicht werden.

Unabhängig von der konkreten Lizenz gehören zu guter wissenschaftlicher Praxis:

* Zitation des GBIF-Downloads,
* Anerkennung der ursprünglichen Datenherausgeber,
* Dokumentation eigener Filter und Veränderungen sowie
* Beachtung möglicher Einschränkungen für sensible Daten.

## Kurze Übung

In der Sitzung lesen wir einen bereitgestellten Record gemeinsam. Eigene Recordsuchen und weitere Filtervarianten dienen der freiwilligen Vertiefung.

### 1. Einen Record lesen

Wählen Sie einen GBIF-Record des Feuersalamanders und dokumentieren Sie:

* wissenschaftlichen Namen,
* Grundlage des Nachweises,
* Datum,
* Koordinaten,
* Koordinatenunsicherheit,
* Datensatz und herausgebende Stelle,
* Lizenz und
* gemeldete Issues.

### 2. Filter bewerten

Sie möchten Feuersalamander-Nachweise in Deutschland seit dem Jahr 2000 kartieren. Welche Filter würden Sie bereits im GBIF-Portal setzen? Welche Qualitätsprüfungen müssten nach dem Download trotzdem noch erfolgen?

### 3. Aussage formulieren

Welche der folgenden Aussagen ist fachlich angemessener? Begründen Sie.

1. „Die Karte zeigt, wo der Feuersalamander in Deutschland lebt.“
2. „Die Karte zeigt die in der verwendeten GBIF-Auswahl dokumentierten Nachweise des Feuersalamanders.“

<!-- Lösungshinweise für Lehrende:
Übung 1:
- Antwort hängt vom ausgewählten Record ab; entscheidend ist die vollständige Quellen- und Qualitätsprüfung.

Übung 2:
- mögliche Portalfilter: Taxon, Land Deutschland, Jahr ab 2000, Koordinaten vorhanden, gegebenenfalls Präsenzstatus und räumliche Issues.
- zusätzliche Prüfung: Plausibilität der Position, Koordinatenunsicherheit, Dubletten, taxonomische Bestimmung, Basis of Record, zeitliche Vollständigkeit, sensible/generalisierten Daten und räumlicher Beobachtungsbias.

Übung 3:
- Aussage 2 ist angemessener, da die Records Nachweise aus einer gefilterten, heterogenen und räumlich verzerrten Datengrundlage darstellen.
-->

## Zusammenfassung

* GBIF macht Biodiversitätsdaten vieler veröffentlichender Einrichtungen gemeinsam auffindbar und nutzbar.
* Ein Occurrence Record dokumentiert einen Nachweis und kann auf unterschiedlichen Grundlagen beruhen.
* Koordinaten, Datum, Taxonomie, Basis of Record, Unsicherheit, Datensatz, Lizenz und Issues müssen gemeinsam betrachtet werden.
* GBIF interpretiert und prüft Daten automatisiert; diese Verarbeitung ersetzt keine fachliche Qualitätskontrolle.
* Beobachtungspunkte zeigen dokumentierte Nachweise und keine vollständige Verbreitung oder sichere Abwesenheit.
* Wissenschaftlich verwendete Occurrence-Auswahlen sollten als Download mit DOI gesichert und zitiert werden.
* Lokale Filter- und Bereinigungsschritte müssen zusätzlich dokumentiert werden.

## Weiterführende Informationen

* [GBIF-Startseite](https://www.gbif.org/)
* [GBIF Occurrence Search](https://www.gbif.org/occurrence/search)
* [GBIF Citation Guidelines](https://www.gbif.org/citation-guidelines)
* [GBIF: Occurrence issues and flags](https://techdocs.gbif.org/en/data-use/occurrence-issues-and-flags)
* [GBIF: Download formats](https://techdocs.gbif.org/en/data-use/download-formats)

<!-- Notizen: Ab hier folgen Vermerke, welche als Gedankenstütze oder Erinnerung dienen, aber noch nicht in der vorhandenen Form veröffentlicht werden sollen. -->

<!--
Vor Durchführung zwingend ergänzen:
- tatsächliche GBIF-Filter
- Download-Datum und DOI
- Dateiname und gegebenenfalls entpackte Teildatei
- Lizenz- und Zitationsdateien des Downloads
- Entscheidung, ob Deutschland oder ein kleineres Untersuchungsgebiet verwendet wird

Didaktische Hinweise:
- Zuerst einzelne Records öffnen, erst danach die große Punktwolke zeigen.
- basisOfRecord an zwei unterschiedlichen Beispielen vergleichen.
- einen Record mit Issue und einen ohne Issue gegenüberstellen.
- einen Punkt mit hoher coordinateUncertaintyInMeters diskutieren.
- dynamische Recordzahl nicht fest in den Text schreiben.

Anschluss an unit11-03_punkte_qgis.md:
- Wie wird aus der tabellarischen GBIF-Auswahl ein korrekt referenzierter, geprüfter und dauerhaft gespeicherter Punktlayer in QGIS?
-->
