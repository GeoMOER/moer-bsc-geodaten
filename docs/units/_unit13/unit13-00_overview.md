---
title: Überblick
published: true
toc: true
header:
  image: /assets/images/unit13/hero-unit13.jpg
  image_description: "Digitales Geländemodell, das in sichtbare Rasterzellen mit markierten Beobachtungspunkten übergeht"
  caption: "KI-generierte Illustration, bearbeitet für diesen Kurs"
---

<!-- Rückblick: Welche Themeninhalte wurden in der letzten Kurssitzung bearbeitet? Sind Fragen zur letzten Kurssitzung offen geblieben? -->

## Rückblick & Fragen

In der letzten Kurssitzung haben wir das Vektormodell vervollständigt. Wir haben Punkte, Linien und Polygone gemeinsam in QGIS untersucht, reale Datensätze aus Geoportalen eingebunden und Features anhand ihrer Attribute und räumlichen Lage ausgewählt.

Zu Beginn besprechen wir **10 Minuten lang die JiTT-Antworten zu Unit 12**. An ein bis zwei ausgewählten Verständnisfragen klären wir die wichtigsten offenen Punkte und knüpfen an die vorige Sitzung an.

<!-- Introtext: Allgemeine Einleitung zum Thema im neuen Lernabschnitt und Verbindung zum vorangegangenen Thema. Worum geht es, welche Inhalte werden bearbeitet und warum sind diese wichtig? -->

## Einführung in Lernabschnitt 13

Das Vektormodell eignet sich besonders für einzelne räumliche Objekte: eine Beobachtung, einen Fluss oder ein Schutzgebiet. Manche Phänomene lassen sich jedoch nicht sinnvoll in klar voneinander getrennte Objekte zerlegen. Höhe, Temperatur oder Niederschlag verändern sich kontinuierlich im Raum.

Für solche Daten wird häufig ein **Rastermodell** verwendet. Ein Raster teilt den Raum in ein regelmäßiges Gitter aus Zellen. Jede Zelle speichert einen Wert – beispielsweise die mittlere Geländehöhe in diesem Bereich.

In dieser Unit untersuchen wir ein digitales Geländemodell und verbinden es mit den GBIF-Punkten aus Unit 11. Damit beantworten wir die Leitfrage:

> **Auf welcher Geländehöhe liegen die dokumentierten Artenbeobachtungen?**

So lernen wir nicht nur einen neuen Geodatentyp kennen, sondern führen erstmals Vektor- und Rasterdaten in einer gemeinsamen Auswertung zusammen.

<!-- Aktuelle Lerneinheit: Welcher konkrete Inhalt erwartet die Studierenden? -->

## In dieser Lerneinheit ...

In dieser Lerneinheit beschäftigen wir uns mit drei aufeinander aufbauenden Fragen:

1. **Wie funktioniert das Rastermodell?**  
   Wir betrachten Rasterzellen, Zeilen, Spalten und Zellwerte und unterscheiden kontinuierliche von kategorialen Rasterdaten.

2. **Welche Eigenschaften bestimmen die Aussagekraft eines Rasters?**  
   Wir untersuchen Zellgröße, räumliche Auflösung, Ausdehnung, Ausrichtung, Datentyp, Bänder und NoData-Werte.

3. **Wie untersuchen und kombinieren wir Rasterdaten in QGIS?**  
   Wir laden ein digitales Geländemodell, prüfen seine Eigenschaften, gestalten eine Farbskala, fragen Zellwerte ab und übertragen Höhenwerte auf Beobachtungspunkte.

Die wiederkehrende Arbeitslogik lautet:

> **Fragestellung → Rasterquelle → Rastereigenschaften → Darstellung → Werte abfragen → Ergebnis prüfen und interpretieren**

<!-- Lernziele: Was sollten Studierende am Ende dieser Lerneinheit wissen und anwenden können? -->

## Lernziele

### Verbindliche Kernziele

Am Ende der gemeinsamen Sitzung sind Studierende in der Lage, ...

* das Rastermodell vom Vektormodell zu unterscheiden, den Aufbau eines Rasters zu erklären und ein digitales Geländemodell fachlich einzuordnen,
* Zellgröße, Ausdehnung, CRS, Einheit und NoData eines Rasterlayers zu prüfen sowie räumliche Auflösung von räumlicher Genauigkeit zu unterscheiden,
* ein kontinuierliches Höhenraster in QGIS geeignet darzustellen und einzelne Zellwerte abzufragen,
* Rasterwerte an Punktpositionen zu ermitteln, als Feld `hoehe_m` zu speichern und fehlende Werte als `NULL` zu erhalten und
* die Ausgabe durch Stichproben zu kontrollieren und ihre Aussagekraft anhand der Raster- und Koordinatenunsicherheit zu beurteilen.

### Vertiefung und Nachschlagen

Die ausführlichen Unterseiten ermöglichen außerdem, ...

* kontinuierliche und kategoriale Raster sowie Gelände- und Oberflächenmodelle genauer zu vergleichen,
* Rasterausrichtung, Datentypen, Bänder und Neuabtastung zu untersuchen und
* Werteverteilungen mit Histogrammen zu analysieren und mehrere Raster systematisch zu vergleichen.

<!-- Organisatorisches: Gibt es Formalitäten, welche noch geklärt werden sollten? -->

## Organisatorisches

[Marburger Übungspaket und Anleitung]({{ '/material/marburg.html' | relative_url }}). Entpacken Sie das gesamte Paket in einen lokalen Arbeitsordner. Alle folgenden Dateipfade beziehen sich auf diesen Ordner; Quellen und vorbereitete Dokumentationsvorlagen liegen in `documentation/`.

Für die praktische Arbeit benötigen Sie QGIS, den geprüften GBIF-Punktlayer aus Unit 11 und das bereitgestellte digitale Geländemodell. Falls Ihr eigener Punktlayer nicht verfügbar ist, wird ein einheitlicher Ersatzlayer bereitgestellt.

Das Übungsraster `data_raw/dgm_marburg_10m.tif` enthält 10-m-Mittelwerte aus dem Marburger DGM1-Paket. Es deckt nicht alle Nachweisorte im Untersuchungsrechteck ab; fehlende Höhenwerte bleiben als `NULL` erhalten.

Rasterdateien können deutlich größer als Vektordateien sein. Kopieren Sie die benötigten Daten deshalb vor Beginn der Übung in Ihren Arbeitsordner und verwenden Sie erneut getrennte Ordner für unveränderte Eingangsdaten, Ergebnisse und Dokumentation.

Verwenden Sie dasselbe Projekt-CRS wie in Units 10–12: **`EPSG:25832`**. Erwarteter Punkteingang ist `unit11_results.gpkg/gbif_checked`; ein Ersatzlayer muss identische Feldnamen und Datentypen besitzen.

Das verbindliche Übergabeprodukt ist:

```text
data_output/unit13_results.gpkg
└── gbif_mit_hoehe
```

Das neue Höhenfeld heißt im gesamten weiteren Kurs **`hoehe_m`**. Falls das QGIS-Werkzeug zunächst einen anderen Feldnamen erzeugt, benennen oder berechnen Sie das finale Feld kontrolliert und dokumentiert.

## Ablauf der Sitzung

Die Sitzung dauert **90 Minuten**: 10 Minuten JiTT-Besprechung, 75 Minuten für neue Inhalte und angeleitete Übungen sowie 5 Minuten Abschluss. Erklärungen und Beispiele setzen keine vorherige Lektüre der Kursseiten voraus. Kurze Austauschrunden finden mit den Sitznachbarinnen und Sitznachbarn statt.

| Zeit | Aktivität |
|---:|---|
| 0–10 Minuten | JiTT-Antworten zu Unit 12 besprechen und Verständnisfragen klären |
| 10–25 Minuten | Rasterzellen, Zellwerte sowie DGM und DOM an einem Beispiel unterscheiden |
| 25–40 Minuten | DGM laden; Zellgröße, Ausdehnung, CRS, Einheit und NoData gemeinsam prüfen |
| 40–55 Minuten | Höhenwerte abfragen und darstellen; Auflösung und Genauigkeit besprechen |
| 55–75 Minuten | Rasterwerte an `gbif_checked` angeleitet abtasten und Stichproben kontrollieren |
| 75–85 Minuten | `gbif_mit_hoehe` mit `hoehe_m` speichern und Unsicherheiten dokumentieren |
| 85–90 Minuten | Zentrale Ergebnisse sichern, eine Exit-Ticket-Frage gemeinsam beantworten und auf JiTT hinweisen |

### Schwerpunkt und Umfang

* **Kernübung:** Wir untersuchen einen kleinen DGM-Ausschnitt, fragen einzelne Zellwerte ab und übertragen Höhenwerte auf die geprüften GBIF-Punkte.
* **Gemeinsame Besprechung:** Ein Beispiel verdeutlicht NoData gegenüber null und Zellgröße gegenüber Genauigkeit. Am Ergebnis prüfen wir einen gültigen Höhenwert und, anhand eines vorbereiteten Beispiels, einen Punkt ohne gültigen Rasterwert.
* **Freiwillige Vertiefung:** Ausführlicher Vergleich mehrerer Raster, Histogrammvarianten, Mehrkanalbilder und eigenes Neuabtasten eines Rasters bleiben zusätzliche Vertiefungen.
* **Ergebnissicherung:** `unit13_results.gpkg/gbif_mit_hoehe` enthält das kontrollierte Feld `hoehe_m`. Rasterquelle, Einheit, Höhenbezug und die Unsicherheiten von Raster und Beobachtungspunkten werden festgehalten.

Die ausführlichen Unterseiten dienen auch als Nachschlagewerk. Für die Sitzung gilt die oben beschriebene Auswahl; weitere Übungen sind freiwillige Vertiefung. Nicht abgeschlossene Arbeit wird nicht als Hausaufgabe nachgeholt. Zwischen den Terminen beantworten Sie ausschließlich die **JiTT-Fragen zu Unit 13 in ILIAS**.

<!-- Hinweise für Lehrende zur 90-Minuten-Sitzung:
Einen kleinen DGM-Ausschnitt mit Metadaten, den geprüften Punkteingang und eine Dokumentationsvorlage vorbereiten. Rechenzeit und erzeugten Feldnamen vorher prüfen. Einen NoData-Fall und einen schemaidentischen Ergebnislayer als Ersatz bereithalten. Bei technischen Verzögerungen das Abtasten am Beamer zeigen; Stichproben und Interpretation gemeinsam am Ersatzlayer durchführen.
Bei mehr Klärungsbedarf im JiTT-Block einen zusätzlichen Vergleich oder eine Übungsvariante kürzen. Ergebnissicherung und Abschluss beibehalten. Aus den folgenden Exit-Ticket-Fragen eine passend zur Sitzung auswählen und kurz gemeinsam auflösen.
-->

## Exit-Ticket

Wir wählen zum Abschluss eine der folgenden Fragen aus und beantworten sie gemeinsam ohne Nachschlagen:

1. Warum ist eine kleine Rasterzelle kein Beweis für hohe Genauigkeit?
2. Warum darf NoData nicht als Höhenwert null interpretiert werden?
3. Welche Unsicherheiten treffen beim Feld `hoehe_m` zusammen?

<a id="transfer-für-lehramtsstudierende"></a>

## Gemeinsam Auflösung und Genauigkeit unterscheiden

Diese Aktivität bearbeiten alle Studierenden im Zeitblock **40–55 Minuten**. Prüfen Sie **2 Minuten zu zweit** die Aussage:

> „Das Höhenraster hat eine Zellgröße von einem Meter. Deshalb ist jeder Höhenwert auf einen Meter genau.“

1. Erklären Sie, welche räumliche Eigenschaft die Zellgröße beschreibt.
2. Nennen Sie eine zusätzliche Angabe aus den Metadaten, die Sie zur Beurteilung der Höhengenauigkeit benötigen.

Wir sammeln **3 Minuten im Plenum** die Begründungen und formulieren gemeinsam eine korrigierte Aussage. Das Ein-Meter-Raster ist hier ein Gedankenbeispiel; maßgeblich für unsere Übungsdaten sind deren tatsächliche Metadaten.

<!-- Erwartung: Die Zellgröße beschreibt die horizontale Rasterunterteilung und belegt keine vertikale Genauigkeit. Diese muss etwa anhand dokumentierter Höhenfehler und der Erfassungsmethode beurteilt werden. -->

<!-- Notizen: Ab hier folgen Vermerke, welche als Gedankenstütze oder Erinnerung dienen aber noch nicht in der vorhandenen Form veröffentlicht werden sollen. -->

<!--
Möglicher Einstieg:
- Nur die GBIF-Punkte zeigen und fragen: „Welche Geländehöhe gehört zu jedem Punkt?“
- Danach ein DGM einblenden und zunächst die sichtbaren Zellen beziehungsweise Zellwerte untersuchen.

Didaktische Schwerpunkte:
- Raster nicht als „Bild“, sondern als georeferenziertes Wertefeld einführen.
- Zellgröße nicht mit Genauigkeit gleichsetzen.
- NoData ausdrücklich von 0 unterscheiden.
- Farbe ist Darstellung; der Zellwert ist die gespeicherte Information.
- Beim Übertragen der Höhe auf GBIF-Punkte auch die Koordinatenunsicherheit der Beobachtungen diskutieren.

Vor Durchführung ergänzen:
- konkreter DGM-Datensatz und Download
- Datenstand, Lizenz und Quellenangabe
- Zellgröße, Höhenbezug und Einheit
- Projekt- und Ausgabe-CRS
- bereitgestellter GBIF-Punktlayer
- erwartete Ergebniswerte für die Übungen

Geplante Unterseiten:
- unit13-01_rasterdaten.md
- unit13-02_rastereigenschaften.md
- unit13-03_raster_qgis.md
- unit13-04_assignment.md
-->

## Folien zu dieser Unit

{% include pdf pdf="Geodaten_Slides_Unit13.pdf" %}
