--- 
title: ÜA | Übungsaufgabe Abschnitt 04
published: true
toc: true
header:
  image: /assets/images/unit04/DataSwamp_Stage04.png
  image_description: "Datensumpf Level 04"
  caption: "Level 4: Gesunkene Teilchen wiederfinden."
---


 
<!-- Übungsaufgabe 04: Ordnerstrukturen, Sortieren, Filtern, Datenbereinigung -->
## Übungsaufgabe 04
 
In dieser Übungsaufgabe wenden Sie das Gelernte aus Lernabschnitt 04 selbstständig an. Grundlage sind zwei Dateien:
 
* `Uebungsaufgabe04_Ordnerstruktur.zip`
* `Uebungsaufgabe04_Datensatz.xlsx` (Tabellenblatt „Testdaten“)
Führen Sie die folgenden zwölf Aufgaben tatsächlich durch. Notieren Sie sich Ihre Antworten und führen Sie im Anschluss „Übungsaufgabe 04“ in Ilias durch. Dort werden Ihnen die Fragen mit Antwortmöglichkeiten gestellt, hier steht, was Sie dafür vorbereiten müssen.
 
Arbeiten Sie bei allen Aufgaben, die Daten verändern (Sortieren, Duplikate entfernen, Bereinigen), auf einer Kopie des Tabellenblatts. Zeilennummern zählen immer mit der Überschrift als Zeile 1.
 
---
 
**1.** Laden Sie `Uebungsaufgabe04_Ordnerstruktur.zip` herunter und entzippen Sie den Ordner (Rechtsklick → „Alle extrahieren…“). Schauen Sie sich die Ordnerstruktur kritisch an. Prüfen Sie, inwieweit sie den Empfehlungen aus dem Kapitel zu Ordnerstrukturen entspricht, und notieren Sie sich für jeden Punkt „ja“ oder „nein“:
* Die Rohdaten liegen in einem eigenen Ordner.
* Die empfohlene maximale Tiefe von 3–4 Ordnerebenen unterhalb des Projektordners wird eingehalten.
* Ordner- und Dateinamen enthalten keine Umlaute und kein ß.
* Ordner- und Dateinamen enthalten keine Leerzeichen.

**2.** Notieren Sie den **relativen** Pfad der Datei `Messungen_Juni.xlsx`, ausgehend vom Projektordner `Sensorprojekt_Marburg`.

 
**3.** Öffnen Sie `Uebungsaufgabe04_Datensatz.xlsx`. Sortieren Sie die gesamte Tabelle zuerst nach `Standort` (A–Z), dann nach `Datum` (aufsteigend). Notieren Sie den Wert der Spalte `Temperatur` in Zeile 15.
 
**4.** Filtern Sie die Spalte `Standort` so, dass **alle Schreibweisen** von „Firmaneiplatz“ gemeinsam angezeigt werden. Notieren Sie, wie viele Datensätze (Zeilen ohne Überschrift) sichtbar sind. Die Statusleiste zeigt „x von 21 Datensätzen gefunden“. Entfernen Sie den Filter danach wieder.
 
<!-- Screenshot [Nr]: Filter-Dropdown der Spalte Standort mit angehakten Einträgen für Firmaneiplatz; im Hintergrund die gefilterte Tabelle, unten links die Statusleiste mit der Anzahl der gefundenen Datensätze.
Markdownlösung: ![Screenshot des Filter-Dropdowns der Spalte Standort mit gefilterter Tabelle und Statusleiste.]({{ '/assets/images/unit04/Screenshot[Nr]_Filter.png' | relative_url }})
Oder als HTML (lightbox) mit Vergrößerungsoption, Beschreibungstext beim Hovern und Galerie zum durchklicken:-->
 
**5.** Filtern Sie die Spalte `Temperatur` mit dem Zahlenfilter „größer als“ 25. Notieren Sie, wie viele Datensätze sichtbar sind. Entfernen Sie den Filter danach wieder.
 
**6.** Filtern Sie wie in Aufgabe 5 nach allen Schreibweisen von „Firmaneiplatz“. Tragen Sie unterhalb der Tabelle in zwei freie Zellen die Formeln `=SUMME(E2:E22)` und `=TEILERGEBNIS(9;E2:E22)` ein. Notieren Sie beide Ergebnisse.
 
**7.** Wenden Sie auf einer **Kopie** „Daten → Duplikate entfernen“ an (alle Spalten). Notieren Sie, wie viele Datenzeilen (ohne Überschrift) danach übrig bleiben.
 
** 8.** Bestimmen Sie mit `=LÄNGE(...)` die Länge des Eintrags XXX. Notieren Sie das Ergebnis.
 
** 9.** Bereinigen Sie die Spalte `Standort` auf einer Kopie, wie im Kapitel zur Datenreinigung beschrieben: Schreibweise vereinheitlichen, überflüssige Leerzeichen entfernen, Klammerzusatz entfernen. Notieren Sie, wie viele verschiedene Standortnamen danach übrig bleiben.

** 10. ** Führen Sie den Ilias-Test durch. 