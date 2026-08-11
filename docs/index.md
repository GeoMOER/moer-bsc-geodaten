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

## Motivation
<!-- Ursprünglicher Text: Daten mit Raumbezug liefern betreffen alle Bereiche des Lebens; sie helfen z.B. Enscheidungsträgern oder können in der Prognose zukünftiger Bedingungen eingesetzt werden. 

Mit fortschreitenden technologischen Möglichkeiten - sowohl in der Datenaufnahme, als auch in Analysemöglichkeiten, ist die Menge an Daten allerdings exponentiell gestiegen. Das Potential, dass mit diesem  sog. "Datalake" (Datensee, also Datendepot), in dem all diese Daten hereinfließen, kann aber nur genutzt werden, wenn die Daten nutzbar gemacht werden - und auch so bleiben.

In der Realität sieht das aber häufig anders - wichtige Informationen gehen verloren, so dass z.B. keine Informationen zur Datenherkunft mehr vorhanden sind, sie sind nicht gut strukturiert oder auffindbar. Damit "versumpft" der datalake schnell - und wird zu einem dataswamp, durch den es kein Durchkommen gibt. Deswegen ist vernünftiges Datenmanagement entscheident - sowohl im wissenschaftlichen, wirtschaftlichen als auch im Kontext eines möglichst effizienten Studiums, immerhin wollen Sie Daten, die sie in späteren Übungen und ihrer Abschlussarbeit bearbeiten, nicht erst lange suchen müssen und noch  wissen, was sie wann mit den Daten gemacht haben, sowie relevante Informationen parat haben.  

In diesem Kurs werden Sie.... -->

<!-- Textvorschlag: -->
Raumbezogene Daten betreffen nahezu alle Bereiche unseres Lebens. Sie erleichtern die Planung von Infrastruktur, optimieren das Management von Ressourcen und liefern die Basis für Umweltprognosen.

Mit foranschreitenden technologischen Möglichkeiten in der Datenerhebung und den Analysemöglichkeiten wächst die verfügbare Datenmenge jedoch exponentiell. Das Potential dieses sogenannten "Data Lake" (einem zentralen Datenspeicher in den sämtliche Daten fließen) lässt sich allerdings nur nutzen, wenn die Daten auch strukturiert nutzbar gemacht werden und langfristig nutzbar bleiben.

Die Realität sieht häufig anders aus. Fehlen Metadaten, sind Formate chaotisch oder Dateien unauffindbar, „versumpft“ der Data Lake rasch zu einem unzugänglichen "Data Swamp". So gehen wichtige Zusammenhänge verloren oder es entstehen falsche Rückschlüsse.
Ein gutes Datenmanagement wirkt dem Informationsverlust entgegen und schont die Nerven. Ob in der Wissenschaft, der Wirtschaft oder in Ihrem Studium: Wer Daten nicht erst stundenlang suchen muss, behält den Kopf frei für das Wesentliche!

In diesem Kurs lernen Sie ... :

* ...wo und wie Daten gespeichert werden.
* ...die Handhabung von Daten in Excel.
* ...die Darstellung von Datenübersichten.
* ...das Reinigen von Datensätzen.
* ...die Beschaffung und Nutzbarmachung von Daten.
* ...die Verarbeitung von Daten mit QGIS.


## Lernziele

Nach Abschluss können Studierende:

* Daten strukturiert organisieren & Methoden zur Datenbereinigung anwenden
* Einfache deskriptive Statistik anwenden
* Punkt-, Raster- und Vektordaten unterscheiden  
* Datensätze nach FAIR-Prinzipien dokumentieren
<!-- Dirk: bitte Lernziele ergänzen -->


## Syllabus
<!--
| Termin | Datum | Thema | Uhrzeit | Einheit | Inhalt |
|---|---|---|---|---|---|
| 01 | 14.10.2026 | Bits & Bytes - ein Einstieg in digitale Daten | 09:15 – 09:45 | Input: Intro & Erwartungsmanagement | Unit 00 |
|   |   |   | 09:45 – 10:15 | Input & Übung: Hard- & Software       | Unit 01 |
|   |   |   | 10:15 – 10:45 | Input & Übung: Laufwerke              | Unit 01 |
|---|---|---|---|---|---| 
| 02 | 21.10.2026 | Dateneinträge & -Typen in Excel | 09:15 – 09:30 | Recap & offene Fragen | Unit 01 |
|   |   |   | 09:30 – 10:00 | Input & Übung: Datentypen und -strukturen | Unit 02 |
|   |   |   | 10:00 – 10:15 | Input & Übung: Zellbezüge | Unit 02 |
|   |   |   | 10:15 – 10:45 | Input & Übung: Koordinatenformate | Unit 02 |
|---|---|---|---|---|---| 
| 03 | 28.10.2026 | Datenübersicht in Excel I | 09:15 – 09:30 | Recap & offene Fragen | Unit 02 |
|   |   |   | 09:30 – 10:15 | Input & Übung: Mittelwert und Co | Unit 03 |
|   |   |   | 10:15 – 10:45 | Input & Übung: Zusammenfassen | Unit 03 |
|---|---|---|---|---|---| 
| 04 | 04.11.2026 | Datenübersicht in Excel II | 09:15 – 09:30 | Recap & offene Fragen | Unit 03 |
|   |   |   | 09:30 – 10:15 | Input & Übung: Histogram & Co | Unit 03 |
|   |   |   | 10:15 – 10:45 | Input & Übung: Zusammenfassen | Unit 03 |
|---|---|---|---|---|---|
| 05 | 11.11.2026 | Datencleaning & Protokollierung | 09:15 – 09:30 | Recap & offene Fragen | Unit 03 |
|   |   |   | 09:30 – 10:15 | Input & Übung: Daten filtern | Unit 04 |
|   |   |   | 10:15 – 10:45 | Input & Übung: Änderungen Protokollieren | Unit 04 |
|---|---|---|---|---|---|
| 06 | 18.11.2026 | Daten nutzbar machen - offline Erfahrung | ??:00 – ??:00 | Input | Unit ?? |
|   |   |   | ??:00 – ??:00 | Demonstration | Unit ?? |
|   |   |   | ??:00 – ??:00 | Übung | Unit ?? |
|   |   |   | ??:00 – ??:00 | Wiederholung & Fragen | Unit ?? |
|---|---|---|---|---|---|
| 07 | 25.11.2026 | FAIR & Metadaten | ??:00 – ??:00 | Input | Unit ?? |
|   |   |   | ??:00 – ??:00 | Demonstration | Unit ?? |
|   |   |   | ??:00 – ??:00 | Übung | Unit ?? |
|   |   |   | ??:00 – ??:00 | Wiederholung & Fragen | Unit ?? |
|---|---|---|---|---|---|
| 08 | 02.12.2026| Automatisierung | ??:00 – ??:00 | Input | Unit ?? |
|   |   |   | ??:00 – ??:00 | Demonstration | Unit ?? |
|   |   |   | ??:00 – ??:00 | Übung | Unit ?? |
|   |   |   | ??:00 – ??:00 | Wiederholung & Fragen | Unit ?? |
|---|---|---|---|---|---|
| 09 | 09.12.2026 | Eigenschaften von Geodaten, Projektionen | ??:00 – ??:00 | Input | Unit ?? |
|   |   |   | ??:00 – ??:00 | Demonstration | Unit ?? |
|   |   |   | ??:00 – ??:00 | Übung | Unit ?? |
|   |   |   | ??:00 – ??:00 | Wiederholung & Fragen | Unit ?? |
|---|---|---|---|---|---|
| 10 | 16.12.2026 | räuml. Autokorrelation & Datentypen | ??:00 – ??:00 | Input | Unit ?? |
|   |   |   | ??:00 – ??:00 | Demonstration | Unit ?? |
|   |   |   | ??:00 – ??:00 | Übung | Unit ?? |
|   |   |   | ??:00 – ??:00 | Wiederholung & Fragen | Unit ?? |
|---|---|---|---|---|---|
| **Hinweis:** | Winterpause vom 23.12.2026 bis 06.01.2027 | Es finden keine Kurstermine statt! | Ausfalltermine: | 23.12.2026, 30.12.2026, 06.01.2027. |   |
|---|---|---|---|---|---|
| 11 | 13.01.2027 | QGIS | ??:00 – ??:00 | Input | Unit ?? |
|   |   |   | ??:00 – ??:00 | Demonstration | Unit ?? |
|   |   |   | ??:00 – ??:00 | Übung | Unit ?? |
|   |   |   | ??:00 – ??:00 | Wiederholung & Fragen | Unit ?? |
|---|---|---|---|---|---|
| 12 | 20.01.2027 | Punktdaten | ??:00 – ??:00 | Input | Unit ?? |
|   |   |   | ??:00 – ??:00 | Demonstration | Unit ?? |
|   |   |   | ??:00 – ??:00 | Übung | Unit ?? |
|   |   |   | ??:00 – ??:00 | Wiederholung & Fragen | Unit ?? |
|---|---|---|---|---|---|
| 13 | 27.01.2027 | Rasterdaten | ??:00 – ??:00 | Input | Unit ?? |
|   |   |   | ??:00 – ??:00 | Demonstration | Unit ?? |
|   |   |   | ??:00 – ??:00 | Übung | Unit ?? |
|   |   |   | ??:00 – ??:00 | Wiederholung & Fragen | Unit ?? |
|---|---|---|---|---|---|
| 14 | 03.02.2027 | Vectordaten | ??:00 – ??:00 | Input | Unit ?? |
|   |   |   | ??:00 – ??:00 | Demonstration | Unit ?? |
|   |   |   | ??:00 – ??:00 | Übung | Unit ?? |
|   |   |   | ??:00 – ??:00 | Wiederholung & Fragen | Unit ?? |
|---|---|---|---|---|---|
| 15 | 10.02.2027 | Abschluss | ??:00 – ??:00 | Input | Unit ?? |
|   |   |   | ??:00 – ??:00 | Demonstration | Unit ?? |
|   |   |   | ??:00 – ??:00 | Übung | Unit ?? |
|   |   |   | ??:00 – ??:00 | Wiederholung & Fragen | Unit ?? |
|---|---|---|---|---|---|
-->

<!-- HTML Vorschlag -->
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

.syllabus-table td:nth-child(4) {
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
        <th>Uhrzeit</th>
        <th>Einheit</th>
        <th>Inhalt</th>
      </tr>
    </thead>
    <tbody>
      <!-- Termin 01 -->
      <tr>
        <td rowspan="3" class="term-number">01</td>
        <td rowspan="3" class="date-cell">14.10.2026</td>
        <td rowspan="3" class="topic-cell">Bits & Bytes - ein Einstieg in digitale Daten</td>
        <td>09:15 – 09:45</td>
        <td>Input: Intro & Erwartungsmanagement</td>
        <td><span class="unit-tag"><a href="unit00/unit00-01_Digitales_Lernen.html">Einheit 00</a></span></td>
      </tr>
      <tr>
        <td>09:45 – 10:15</td>
        <td>Input & Übung: Hard- & Software</td>
        <td><span class="unit-tag"><a href="unit01/unit01-01_byte.html">Einheit 01</a></span></td>
      </tr>
      <tr>
        <td>10:15 – 10:45</td>
        <td>Input & Übung: Laufwerke</td>
        <td><span class="unit-tag"><a href="unit01/unit01-03_Laufwerke.html">Einheit 01</a></span></td>
      </tr>
      <!-- Termin 02 -->
      <tr>
        <td rowspan="4" class="term-number">02</td>
        <td rowspan="4" class="date-cell">21.10.2026</td>
        <td rowspan="4" class="topic-cell">Dateneinträge & -Typen in Excel</td>
        <td>09:15 – 09:30</td>
        <td>Recap & offene Fragen</td>
        <td><span class="unit-tag"><a href="unit01/unit01-00_overview.html">Einheit 01</a></span></td>
      </tr>
      <tr>
        <td>09:30 – 10:00</td>
        <td>Input & Übung: Datentypen und -strukturen</td>
        <td><span class="unit-tag"><a href="unit02/unit02-02_Datenformate.html">Einheit 02</a></span></td>
      </tr>
      <tr>
        <td>10:00 – 10:15</td>
        <td>Input & Übung: Zellbezüge</td>
        <td><span class="unit-tag"><a href="unit02/unit02-03_Zellbezüge.html">Einheit 02</a></span></td>
      </tr>
      <tr>
        <td>10:15 – 10:45</td>
        <td>Input & Übung: Koordinatenformate</td>
        <td><span class="unit-tag"><a href="unit02/unit02-04_Koordinatenformate.html">Einheit 02</a></span></td>
      </tr>
      <!-- Termin 03 -->
      <tr>
        <td rowspan="3" class="term-number">03</td>
        <td rowspan="3" class="date-cell">28.10.2026</td>
        <td rowspan="3" class="topic-cell">Datenübersicht in Excel I</td>
        <td>09:15 – 09:30</td>
        <td>Recap & offene Fragen</td>
        <td><span class="unit-tag"><a href="unit02/unit02-00_overview.html">Einheit 02</a></span></td>
      </tr>
      <tr>
        <td>09:30 – 10:15</td>
        <td>Input & Übung: Mittelwert und Co</td>
        <td><span class="unit-tag"><a href="unit03/unit03-01_wichtigeWerte.html">Einheit 03</a></span></td>
      </tr>
      <tr>
        <td>10:15 – 10:45</td>
        <td>Input & Übung: Zusammenfassen</td>
        <td><span class="unit-tag"><a href="unit03/unit03-02_Zusammenfassen.html">Einheit 03</a></span></td>
      </tr>
      <!-- Termin 04 -->
      <tr>
        <td rowspan="3" class="term-number">04</td>
        <td rowspan="3" class="date-cell">04.11.2026</td>
        <td rowspan="3" class="topic-cell">Datenübersicht in Excel II</td>
        <td>09:15 – 09:30</td>
        <td>Recap & offene Fragen</td>
        <td><span class="unit-tag"><a href="unit03/unit03-00_overview.html">Einheit 03</a></span></td>
      </tr>
      <tr>
        <td>09:30 – 10:15</td>
        <td>Input & Übung: Histogram & Co</td>
        <td><span class="unit-tag"><a href="unit03/unit03-05_GraphischeKontrolle.html">Einheit 03</a></span></td>
      </tr>
      <tr>
        <td>10:15 – 10:45</td>
        <td>Input & Übung: Zusammenfassen</td>
        <td><span class="unit-tag"><a href="unit03/unit03-02_Zusammenfassen.html">Einheit 03</a></span></td>
      </tr>
      <!-- Termin 05 -->
      <tr>
        <td rowspan="3" class="term-number">05</td>
        <td rowspan="3" class="date-cell">11.11.2026</td>
        <td rowspan="3" class="topic-cell">Datencleaning & Protokollierung</td>
        <td>09:15 – 09:30</td>
        <td>Recap & offene Fragen</td>
        <td><span class="unit-tag"><a href="unit03/unit03-00_overview.html">Einheit 03</a></span></td>
      </tr>
      <tr>
        <td>09:30 – 10:15</td>
        <td>Input & Übung: Daten filtern</td>
        <td><span class="unit-tag"><a href="unit04/unit04-01_DatenFiltern.html">Einheit 04</a></span></td>
      </tr>
      <tr>
        <td>10:15 – 10:45</td>
        <td>Input & Übung: Änderungen Protokollieren</td>
        <td><span class="unit-tag"><a href="unit04/unit04-02_Protokollieren.html">Einheit 04</a></span></td>
      </tr>
      <!-- Termin 06 -->
      <tr>
        <td rowspan="4" class="term-number">06</td>
        <td rowspan="4" class="date-cell">18.11.2026</td>
        <td rowspan="4" class="topic-cell">Daten nutzbar machen - offline Erfahrung</td>
        <td>09:15 – 09:30</td>
        <td>Recap & offene Fragen</td>
        <td><span class="unit-tag"><a href="unit04/unit04-00_overview.html">Einheit 04</a></span></td>
      </tr>
      <tr>
        <td>09:30 – 10:00</td>
        <td>Input</td>
        <td><span class="unit-tag"><a href="unit??/unit??-??_?????.html">Einheit 05</a></span></td>
      </tr>
      <tr>
        <td>10:00 – 10:30</td>
        <td>Demonstration & Übung</td>
        <td><span class="unit-tag"><a href="unit??/unit??-??_?????.html">Einheit 05</a></span></td>
      </tr>
      <tr>
        <td>10:30 – 10:45</td>
        <td>Wiederholung & Fragen</td>
        <<td><span class="unit-tag"><a href="unit??/unit??-??_?????.html">Einheit 05</a></span></td>
      </tr>
      <!-- Termin 07 -->
      <tr>
        <td rowspan="4" class="term-number">07</td>
        <td rowspan="4" class="date-cell">25.11.2026</td>
        <td rowspan="4" class="topic-cell">FAIR & Metadaten</td>
        <td>09:15 – 09:30</td>
        <td>Recap & offene Fragen</td>
        <td><span class="unit-tag"><a href="unit05/unit05-00_overview.html">Einheit 05</a></span></td>
      </tr>
      <tr>
        <td>09:30 – 10:00</td>
        <td>Input</td>
        <td><span class="unit-tag"><a href="unit??/unit??-??_?????.html">Einheit 06</a></span></td>
      </tr>
      <tr>
        <td>10:00 – 10:30</td>
        <td>Demonstration & Übung</td>
        <td><span class="unit-tag"><a href="unit??/unit??-??_?????.html">Einheit 06</a></span></td>
      </tr>
      <tr>
        <td>10:30 – 10:45</td>
        <td>Wiederholung & Fragen</td>
        <td><span class="unit-tag"><a href="unit??/unit??-??_?????.html">Einheit 06</a></span></td>
      </tr>
      <!-- Termin 08 -->
      <tr>
        <td rowspan="4" class="term-number">08</td>
        <td rowspan="4" class="date-cell">02.12.2026</td>
        <td rowspan="4" class="topic-cell">Automatisierung</td>
        <td>09:15 – 09:30</td>
        <td>Recap & offene Fragen</td>
        <td><span class="unit-tag"><a href="unit06/unit06-00_overview.html">Einheit 06</a></span></td>
      </tr>
      <tr>
        <td>09:30 – 10:00</td>
        <td>Input</td>
        <td><span class="unit-tag"><a href="unit??/unit??-??_?????.html">Einheit 07</a></span></td>
      </tr>
      <tr>
        <td>10:00 – 10:30</td>
        <td>Demonstration & Übung</td>
        <td><span class="unit-tag"><a href="unit??/unit??-??_?????.html">Einheit 07</a></span></td>
      </tr>
      <tr>
        <td>10:30 – 10:45</td>
        <td>Wiederholung & Fragen</td>
        <td><span class="unit-tag"><a href="unit??/unit??-??_?????.html">Einheit 07</a></span></td>
      </tr>
      <!-- Termin 09 -->
      <tr>
        <td rowspan="4" class="term-number">09</td>
        <td rowspan="4" class="date-cell">09.12.2026</td>
        <td rowspan="4" class="topic-cell">Eigenschaften von Geodaten, Projektionen</td>
        <td>09:15 – 09:30</td>
        <td>Recap & offene Fragen</td>
        <td><span class="unit-tag"><a href="unit07/unit07-00_overview.html">Einheit 07</a></span></td>
      </tr>
      <tr>
        <td>09:30 – 10:00</td>
        <td>Input</td>
        <td><span class="unit-tag"><a href="unit??/unit??-??_?????.html">Einheit 08</a></span></td>
      </tr>
      <tr>
        <td>10:00 – 10:30</td>
        <td>Demonstration & Übung</td>
        <td><span class="unit-tag"><a href="unit??/unit??-??_?????.html">Einheit 08</a></span></td>
      </tr>
      <tr>
        <td>10:30 – 10:45</td>
        <td>Wiederholung & Fragen</td>
        <td><span class="unit-tag"><a href="unit??/unit??-??_?????.html">Einheit 08</a></span></td>
      </tr>
      <!-- Termin 10 -->
      <tr>
        <td rowspan="4" class="term-number">10</td>
        <td rowspan="4" class="date-cell">16.12.2026</td>
        <td rowspan="4" class="topic-cell">räuml. Autokorrelation & Datentypen</td>
        <td>09:15 – 09:30</td>
        <td>Recap & offene Fragen</td>
        <td><span class="unit-tag"><a href="unit08/unit08-00_overview.html">Einheit 08</a></span></td>
      </tr>
      <tr>
        <td>09:30 – 10:00</td>
        <td>Input</td>
        <td><span class="unit-tag"><a href="unit??/unit??-??_?????.html">Einheit 09</a></span></td>
      </tr>
      <tr>
        <td>10:00 – 10:30</td>
        <td>Demonstration & Übung</td>
        <td><span class="unit-tag"><a href="unit??/unit??-??_?????.html">Einheit 09</a></span></td>
      </tr>
      <tr>
        <td>10:30 – 10:45</td>
        <td>Wiederholung & Fragen</td>
        <td><span class="unit-tag"><a href="unit??/unit??-??_?????.html">Einheit 09</a></span></td>
      </tr>
      <!-- Winterpause Row -->
      <tr class="break-row">
        <td colspan="6">
          <strong>Winterpause:</strong> 23.12.2026 bis 06.01.2027 (Ausfalltermine: 23.12., 30.12.2026 & 06.01.2027)
        </td>
      </tr>
      <!-- Termin 11 -->
      <tr>
        <td rowspan="4" class="term-number">11</td>
        <td rowspan="4" class="date-cell">13.01.2027</td>
        <td rowspan="4" class="topic-cell">QGIS</td>
        <td>09:15 – 09:30</td>
        <td>Recap & offene Fragen</td>
        <td><span class="unit-tag"><a href="unit09/unit09-00_overview.html">Einheit 09</a></span></td>
      </tr>
      <tr>
        <td>09:30 – 10:00</td>
        <td>Input</td>
        <td><span class="unit-tag"><a href="unit??/unit??-??_?????.html">Einheit ??</a></span></td>
      </tr>
      <tr>
        <td>10:00 – 10:30</td>
        <td>Demonstration & Übung</td>
        <td><span class="unit-tag"><a href="unit??/unit??-??_?????.html">Einheit ??</a></span></td>
      </tr>
      <tr>
        <td>10:30 – 10:45</td>
        <td>Wiederholung & Fragen</td>
        <td><span class="unit-tag"><a href="unit??/unit??-??_?????.html">Einheit ??</a></span></td>
      </tr>
      <!-- Termin 12 -->
      <tr>
        <td rowspan="4" class="term-number">12</td>
        <td rowspan="4" class="date-cell">20.01.2027</td>
        <td rowspan="4" class="topic-cell">Punktdaten</td>
        <td>09:15 – 09:30</td>
        <td>Recap & offene Fragen</td>
        <td><span class="unit-tag"><a href="unit??/unit??-??_overview.html">Einheit ??</a></span></td>
      </tr>
      <tr>
        <td>09:30 – 10:00</td>
        <td>Input</td>
        <td><span class="unit-tag"><a href="unit??/unit??-??_?????.html">Einheit ??</a></span></td>
      </tr>
      <tr>
        <td>10:00 – 10:30</td>
        <td>Demonstration & Übung</td>
        <td><span class="unit-tag"><a href="unit??/unit??-??_?????.html">Einheit ??</a></span></td>
      </tr>
      <tr>
        <td>10:30 – 10:45</td>
        <td>Wiederholung & Fragen</td>
        <td><span class="unit-tag"><a href="unit??/unit??-??_?????.html">Einheit ??</a></span></td>
      </tr>
      <!-- Termin 13 -->
      <tr>
        <td rowspan="4" class="term-number">13</td>
        <td rowspan="4" class="date-cell">27.01.2027</td>
        <td rowspan="4" class="topic-cell">Rasterdaten</td>
        <td>09:15 – 09:30</td>
        <td>Recap & offene Fragen</td>
        <td><span class="unit-tag"><a href="unit??/unit??-??_overview.html">Einheit ??</a></span></td>
      </tr>
      <tr>
        <td>09:30 – 10:00</td>
        <td>Input</td>
        <td><span class="unit-tag"><a href="unit??/unit??-??_?????.html">Einheit ??</a></span></td>
      </tr>
      <tr>
        <td>10:00 – 10:30</td>
        <td>Demonstration & Übung</td>
        <td><span class="unit-tag"><a href="unit??/unit??-??_?????.html">Einheit ??</a></span></td>
      </tr>
      <tr>
        <td>10:30 – 10:45</td>
        <td>Wiederholung & Fragen</td>
        <td><span class="unit-tag"><a href="unit??/unit??-??_?????.html">Einheit ??</a></span></td>
      </tr>
      <!-- Termin 14 -->
      <tr>
        <td rowspan="4" class="term-number">14</td>
        <td rowspan="4" class="date-cell">03.02.2027</td>
        <td rowspan="4" class="topic-cell">Vectordaten</td>
        <td>09:15 – 09:30</td>
        <td>Recap & offene Fragen</td>
        <td><span class="unit-tag"><a href="unit??/unit??-??_overview.html">Einheit ??</a></span></td>
      </tr>
      <tr>
        <td>09:30 – 10:00</td>
        <td>Input</td>
        <td><span class="unit-tag"><a href="unit??/unit??-??_?????.html">Einheit ??</a></span></td>
      </tr>
      <tr>
        <td>10:00 – 10:30</td>
        <td>Demonstration & Übung</td>
        <td><span class="unit-tag"><a href="unit??/unit??-??_?????.html">Einheit ??</a></span></td>
      </tr>
      <tr>
        <td>10:30 – 10:45</td>
        <td>Wiederholung & Fragen</td>
        <td><span class="unit-tag"><a href="unit??/unit??-??_?????.html">Einheit ??</a></span></td>
      </tr>
      <!-- Termin 15 -->
      <tr>
        <td rowspan="4" class="term-number">15</td>
        <td rowspan="4" class="date-cell">10.02.2027</td>
        <td rowspan="4" class="topic-cell">Abschluss</td>
        <td>09:15 – 09:30</td>
        <td>Recap & offene Fragen</td>
        <td><span class="unit-tag"><a href="unit??/unit??-??_overview.html">Einheit ??</a></span></td>
      </tr>
      <tr>
        <td>09:30 – 10:00</td>
        <td>Input</td>
        <td><span class="unit-tag"><a href="unit??/unit??-??_?????.html">Einheit ??</a></span></td>
      </tr>
      <tr>
        <td>10:00 – 10:30</td>
        <td>Demonstration & Übung</td>
        <td><span class="unit-tag"><a href="unit??/unit??-??_?????.html">Einheit ??</a></span></td>
      </tr>
      <tr>
        <td>10:30 – 10:45</td>
        <td>Wiederholung & Abschlussfragen</td>
        <td><span class="unit-tag"><a href="unit??/unit??-??_?????.html">Einheit ??</a></span></td>
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
