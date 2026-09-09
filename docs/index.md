---
title: Geodaten
published: true
layout: splash
date: '2026-10-12 09:15:00 +0100'
header:
  overlay_color: "#000"
  overlay_filter: 0.6
  overlay_image: "/assets/images/title.png"
  caption: 'Image: [solar.empire via flickr.com](https://www.flickr.com/photos/solar-empire/23815961328/) [CC BY-NC 2.0 DEED](https://creativecommons.org/licenses/by-nc/2.0/)'
  cta_label: go to course units
  cta_url: "/units.html"
excerpt: Einführung in die Arbeit mit Geodaten.
feature_row_intro:
- excerpt: Bachelor level course at the Department of Geography at the University of Marburg.
feature_row_ilos:
- image_path: "/assets/images/envobs_ilos.jpg"
  alt: PC monitor laying in the garden of the institute.
  title: Intended learning outcomes
  excerpt: "Template..."
---

{% include feature_row id="feature_row_intro" type="center" %}


## Diese Seite ist in Bearbeitung! Bitte bis auf weiteres nicht verwenden!

## This page is under construction! Do not use!

## Motivation


Raumbezogene Daten spielen in Wissenschaft, Planung und Gesellschaft eine zentrale Rolle. Sie helfen dabei, räumliche Zusammenhänge zu erkennen, Entwicklungen zu analysieren und Entscheidungen zu unterstützen.

Durch neue Möglichkeiten der Datenerhebung und -analyse wächst die verfügbare Datenmenge stetig. Gleichzeitig wird gutes Datenmanagement immer wichtiger. Ein **Data Lake** ist ein gemeinsamer Speicher für unterschiedliche Daten, die sich für verschiedene Auswertungen nutzen lassen. Dafür müssen die Daten auffindbar, verständlich und technisch nutzbar sein. Auch ihre Qualität muss sich beurteilen lassen.

Fehlen dagegen aussagekräftige Dateinamen, klare Strukturen, geeignete Formate, Metadaten (beschreibende Angaben zu den Daten) oder nachvollziehbare Bearbeitungsschritte, kann aus dem Data Lake schnell ein **Data Swamp** werden. In diesem „Datensumpf“ sind Daten zwar vorhanden, lassen sich aber nur schwer finden, verlässlich interpretieren oder erneut verwenden. Schlimmstenfalls führen unklare Herkunft, ungeprüfte Qualität oder ein falsch verstandener Raumbezug zu fehlerhaften Ergebnissen.

Gutes Datenmanagement verhindert dieses Versumpfen. Es verbindet die strukturierte Ablage und Dokumentation von Daten mit ihrer kritischen Prüfung, Aufbereitung, Analyse und Visualisierung. Diese Fähigkeiten sind für wissenschaftliches und berufliches Arbeiten ebenso wichtig wie für das Studium: Wer Daten und Arbeitsschritte nachvollziehbar organisiert, kann Ergebnisse überprüfen, reproduzieren und später weiterverwenden.

Der Kurs vermittelt deshalb grundlegende Kompetenzen für den strukturierten und kritischen Umgang mit Daten. Von digitalen Grundlagen über Tabellen, Datenbereinigung und Dokumentation führt er bis zur Arbeit mit Geodaten im Geoinformationssystem QGIS. Anhand geographischer Fragestellungen lernen Sie, Daten zu recherchieren, zu beurteilen, aufzubereiten, zu analysieren und aussagekräftig zu visualisieren.


## Lernziele

Nach erfolgreichem Abschluss des Moduls sind Studierende in der Lage, 

* grundlegende Konzepte digitaler Daten, ihrer Speicherung, Formate und technischen Verarbeitung zu erklären,
* tabellarische Daten strukturiert aufzubauen, zu bereinigen, zu transformieren und mit Tabellenkalkulationssoftware auszuwerten,
* Datenqualität, Herkunft, Dokumentation und Eignung für eine Fragestellung kritisch zu beurteilen,
* grundlegende Verfahren der deskriptiven (beschreibenden) Statistik anzuwenden und Ergebnisse angemessen zu interpretieren,
* Daten, Metadaten und Bearbeitungsschritte nachvollziehbar und nach grundlegenden FAIR-Prinzipien zu organisieren,
* Geodaten zu recherchieren sowie Raumbezug, Koordinatenreferenzsysteme, Vektor- und Rasterdaten zu verstehen und zu unterscheiden,
* Geodaten in QGIS zu laden, aufzubereiten, zu analysieren und in geeigneten Formaten zu speichern,
* Geodaten angemessen zu symbolisieren, zu klassifizieren und in übersichtlichen Karten zu visualisieren und
* geographische Fragestellungen in nachvollziehbaren Schritten zu bearbeiten – von der Datenrecherche bis zur Dokumentation der räumlichen Ergebnisse.


## Syllabus

<style>
.syllabus-table {
  width: 100%;
  border-collapse: collapse;
  text-align: left;
  font-size: 0.95rem;
  color: inherit;
}

.syllabus-table th {
  background-color: inherit;
  color: inherit;
  font-weight: 600;
  padding: 0.75rem 1rem;
  border-bottom: 2px solid var(--border-color, #e2e8f0);
}

.syllabus-table td {
  padding: 0.65rem 1rem;
  border-bottom: 1px solid var(--border-color, rgba(0, 0, 0, 0.08));
  vertical-align: middle;
}

.syllabus-table td:nth-child(2) {
  white-space: nowrap;
}

.term-number {
  font-weight: normal;
  text-align: center;
  border-right: 1px solid var(--border-color, #e2e8f0);
  background-color: var(--block-bg, rgba(0, 0, 0, 0.01));
}

.date-cell {
  white-space: nowrap;
  font-weight: normal;
  border-right: 1px solid var(--border-color, #e2e8f0);
  background-color: var(--block-bg, rgba(0, 0, 0, 0.01));
}

.topic-cell {
  font-weight: normal;
  border-right: 2px solid var(--border-color, #e2e8f0);
  background-color: var(--block-bg, rgba(0, 0, 0, 0.01));
}

.syllabus-table tbody tr td[rowspan] {
  border-bottom: 2px solid var(--border-color, #cbd5e1);
}

.syllabus-table tbody tr:has(+ tr td[rowspan]) td {
  border-bottom: 2px solid var(--border-color, #cbd5e1);
}

.unit-tag {
  display: inline-block;
  white-space:nowrap;
  background-color: var(--tag-bg, rgba(0, 0, 0, 0.06));
  color: inherit;
  font-size: 0.8rem;
  font-weight: 600;
  padding: 0.2rem 0.5rem;
  border-radius: 4px;
  border: 1px solid var(--border-color, transparent);
}

.break-row td {
  background-color: var(--break-bg, rgba(239, 68, 68, 0.08)) !important;
  color: inherit;
  text-align: center;
  padding: 1rem !important;
  border-top: 2px solid var(--border-color, #e2e8f0);
  border-bottom: 2px solid var(--border-color, #e2e8f0) !important;
}
</style>

<div>
  <table class="syllabus-table">
    <thead>
      <tr>
        <th>Termin</th>
        <th>Datum</th>
        <th>Thema</th>
        <th>Inhalt</th>
      </tr>
    </thead>
    <tbody>
      <!-- Termin 01 -->
      <tr>
        <td class="term-number"><a href="unit01/unit01-00_overview.html">01</a></td>
        <td class="date-cell">14.10.2026</td>
        <td class="topic-cell">Bits & Bytes - ein Einstieg in digitale Daten</td>
        <td>Einführung und Erwartungen an den Kurs, Hardware und Software, Laufwerke</td>
      </tr>
      <!-- Termin 02 -->
      <tr>
        <td class="term-number"><a href="unit02/unit02-00_overview.html">02</a></td>
        <td class="date-cell">21.10.2026</td>
        <td class="topic-cell">Dateneinträge und Datentypen in Excel</td>
        <td>Datentypen und -strukturen, Zellbezüge, Koordinatenformate</td>
      </tr>
      <!-- Termin 03 -->
      <tr>
        <td class="term-number"><a href="unit03/unit03-00_overview.html">03</a></td>
        <td class="date-cell">28.10.2026</td>
        <td class="topic-cell">Daten organisieren und bereinigen</td>
        <td>Ordnerstrukturen, Sortieren und Filtern, Datenbereinigung und Protokollierung</td>
      </tr>
      <!-- Termin 04 -->
      <tr>
        <td class="term-number"><a href="unit04/unit04-00_overview.html">04</a></td>
        <td class="date-cell">04.11.2026</td>
        <td class="topic-cell">Daten mit Kennwerten beschreiben</td>
        <td>Mittelwert, Median und Modus, Streuung und Verteilungen</td>
      </tr>
      <!-- Termin 05 -->
      <tr>
        <td class="term-number"><a href="unit05/unit05-00_overview.html">05</a></td>
        <td class="date-cell">11.11.2026</td>
        <td class="topic-cell">Daten zusammenfassen und Zusammenhänge betrachten</td>
        <td>Häufigkeits- und Pivot-Tabellen, Streudiagramme und Pearson-Korrelation</td>
      </tr>
      <!-- Termin 06 -->
      <tr>
        <td class="term-number"><a href="unit06/unit06-00_overview.html">06</a></td>
        <td class="date-cell">18.11.2026</td>
        <td class="topic-cell">Wiederkehrende Schritte in Excel</td>
        <td>Formeln, Kopieren und Serien in Excel</td>
      </tr>
      <!-- Termin 07 -->
      <tr>
        <td class="term-number"><a href="unit07/unit07-00_overview.html">07</a></td>
        <td class="date-cell">25.11.2026</td>
        <td class="topic-cell">FAIR, README und Versionskontrolle</td>
        <td>FAIR-Prinzipien, README-Dokumentation und Versionskontrolle mit Git</td>
      </tr>
      <!-- Termin 08 -->
      <tr>
        <td class="term-number"><a href="unit08/unit08-00_overview.html">08</a></td>
        <td class="date-cell">02.12.2026</td>
        <td class="topic-cell">Automatisierung</td>
        <td>Wiederkehrende Arbeitsschritte automatisieren und Ergebnisse kontrollieren</td>
      </tr>
      <!-- Termin 09 -->
      <tr>
        <td class="term-number"><a href="unit09/unit09-00_overview.html">09</a></td>
        <td class="date-cell">09.12.2026</td>
        <td class="topic-cell">Eigenschaften von Geodaten, Koordinaten & Projektionen</td>
        <td>Eigenschaften von Geodaten, Koordinaten, Kartenprojektionen</td>
      </tr>
      <!-- Termin 10 -->
      <tr>
        <td class="term-number"><a href="unit10/unit10-00_overview.html">10</a></td>
        <td class="date-cell">16.12.2026</td>
        <td class="topic-cell">Geodatenmodelle & Einstieg in QGIS</td>
        <td>Geodatenmodelle, QGIS-Oberfläche und Projekte, lokale Datenquellen, Web Map Services</td>
      </tr>
      <!-- Winterpause Row -->
      <tr class="break-row">
        <td colspan="4">
          <strong>Winterpause:</strong> 23.12.2026 bis 06.01.2027 (Ausfalltermine: 23.12., 30.12.2026 & 06.01.2027)
        </td>
      </tr>
      <!-- Termin 11 -->
      <tr>
        <td class="term-number"><a href="unit11/unit11-00_overview.html">11</a></td>
        <td class="date-cell">13.01.2027</td>
        <td class="topic-cell">Vektordaten I: Punkte & Beobachtungen</td>
        <td>Punktdaten, GBIF-Occurrence-Records, Koordinaten in QGIS importieren, Punktlayer prüfen und interpretieren</td>
      </tr>
      <!-- Termin 12 -->
      <tr>
        <td class="term-number"><a href="unit12/unit12-00_overview.html">12</a></td>
        <td class="date-cell">20.01.2027</td>
        <td class="topic-cell">Vektordaten II: Linien & Flächen</td>
        <td>Linien- und Polygongeometrien, Geoportale und Metadaten, Vektordaten in QGIS, räumliche Auswahl</td>
      </tr>
      <!-- Termin 13 -->
      <tr>
        <td class="term-number"><a href="unit13/unit13-00_overview.html">13</a></td>
        <td class="date-cell">27.01.2027</td>
        <td class="topic-cell">Rasterdaten</td>
        <td>Rastermodell, Rastereigenschaften, digitales Geländemodell, Rasterwerte in QGIS abfragen, Raster- und Vektordaten kombinieren</td>
      </tr>
      <!-- Termin 14 -->
      <tr>
        <td class="term-number"><a href="unit14/unit14-00_overview.html">14</a></td>
        <td class="date-cell">03.02.2027</td>
        <td class="topic-cell">Karten & Geo-Workflow</td>
        <td>Symbolisierung, Klassifizierung, Kartenlayout, vollständiger Geo-Workflow</td>
      </tr>
      <!-- Termin 15 -->
      <tr>
        <td class="term-number"><a href="unit15/unit15-00_overview.html">15</a></td>
        <td class="date-cell">10.02.2027</td>
        <td class="topic-cell">Abschluss</td>
        <td>Ergebnisse zusammenführen, Karten und Analysen dokumentieren, Abschluss und Ausblick</td>
      </tr>
    </tbody>
  </table>
</div>



 


<!--
Der Kurs umfasst 9 Units:

1) Von bits zu Informationen - Wie Daten und Computer funktionieren
   Am Ende der Unit sind Sie in der Lage
   * Binärsystem, Bits & Bytes erklären
   * Unterschied zwischen Speicher, RAM und Prozessor verstehen
   * Neu! Laufwerke, Netzwerke und Pfade
   * Kodierung (Text, Zahlen, Bilder) grundlegend erklären
   * Dateiformate als Strukturierungsprinzip verstehen

2) Daten basics - Datentypen und -Formate (in Excel)
   Am Ende der Unit sind Sie in der Lage
   * Unterschiede zwischen verschiedenen Datentypen zu erklären
   * Encoding-Probleme (z.B. Umlaute) erkennen
   * „Tidy Data“-Prinzip verstehen (eine Beobachtung pro Zeile)
   * Koordinatenformate (dezimal vs. Grad/Minute/Sekunde) unterscheiden
   (* Metadaten anzulegen)
   * grundlegende Excel-Funktionalitäten zu beherrschen (zB. absolute vs. relative Zellbezüge)

3) Daten organisieren - Aufbereitung von Daten mit Textfunktionen, Sortieren, Filterfunktion
   Am Ende dieser Unit sind Sie in der Lage:
   * Sinnvolle Ordnerstrukturen anzulegen
   * Daten zu sortieren und filtern
   * Doppelte Einträge zu identifizieren
   * Textfunktionen anwenden (z.B. TEIL, GLÄTTEN, ERSETZEN)
   * Fehlende Werte identifizieren
   * einfache Qualitätskontrollen durchzuführen
   * Bereinigungsschritte zu dokumentieren (ReadMe)

4) Daten verstehen - deskriptive Statistik (Streuung, Mittelwerte, Korrelationen)
   Am Ende dieser Unit sind Sie in der Lage:
   * Mittelwert, Median und Modus zu berechnen und zu interpretieren
   * Varianz und Standardabweichung zu erklären
   * Verteilungen zu interpretieren


5) Zusammenhänge erkennen - Korrelationen und Zusammenhänge
   <!-- Recap: Dateinamen der letzten Übungen, Zeit messen, ohne in das vorherige Chapter zu schauen; was wurde gemacht? / Quiz und wordbubble / 

   Am Ende dieser Unit sind Sie in der Lage
   * Pearson-Korrelation zu berechnen
   * Scatterplots zu interpretieren
   * Pivot-Tabellen zu erstellen
   * Häufigkeitstabellen zu erzeugen

6) Exkurs: Fuktionen und Automatisierung
   Am Ende dieser Unit sind Sie in der Lage:
   * Einfache Automatisierung (Formeln, Kopieren, Serien)

7) Daten zugänglich machen
   Am Ende dieser Unit sind Sie in der Lage:
   * FAIR Prinzipien zu erklären
   * Dokumentation / ReadMe zu erstellen
   * Git nachzuvollziehen

8) QGIS & WMS
   eine Einführung

9) Besonderheiten Geodaten: point, raster und vector Daten
   (3 Kurstage)

<!-- Probleme: anfangs zur Übung, shortcuts, Datenorganisation -->
<!-- nur als Idee (nicht einbauen) QField, Laptop oder nur Tablets? -> vllt. Umfrage erstellen, bis jetzt noch keine Beschwerde dass es daheim kein Laptop/PC vorhanden ist, einen link zu Android oder IOS erstellen vs. keine Tür öffnen, Anspruchshaltung auch in anderen Kursen -->

<!-- Datenverknüpfung (als Verweis gespeichert) in QGIS als wichtiger Punkt wenn Dateipfade erklärt werden,
H Laufwerk, Beispiel: Daten die auf einem Server gespeichert sind, gleichnamige Datei ein Mal auf Server, ein Mal lokal, Verknüpfung zu Server -->

<!-- vermutlich besser Teil 3 zu 2 vorzuziehen, damit die Studis schon Mal Daten in der Hand hatten (Aufgabe dann in Datenmanagement: Findet die Daten der letzten ~ 6 sessions wieder) -->

<!-- statt Karten (ist schon in QGIS) noch andere open source + coding/scriptsteuerung Möglichkeiten anteasen, bsp. R/python. Hier nur wirklich ganz grob das Prinip solcher programmiersprachen als Möglichkeit der automatisierung darstellen, Level "Hello World", einbinden wie zB im R Kurs, auf die Aufbauenden Kurse (BaseR, python, Grass: Chris? Christiane vllt?) verweisen 

-->





## Team

{% for author in site.data.authors %}
  {% include author-profile.html %}
 <br />
{% endfor %}
