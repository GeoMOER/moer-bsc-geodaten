---
title: Einführung Excel
published: true
toc: true
header:
  image: /assets/images/unit02/31031723265_0890cd9547_o.jpg
  image_description: "Cloudscape Over the Philippine Sea"
  caption: "Image: [NASA's Marshall Space Flight Center](https://www.nasa.gov/centers/marshall/home/index.html) [CC BY-NC 2.0] via [flickr.com](https://www.flickr.com/photos/nasamarshall/31031723265/)"
---

<!-- Themenblock 02-01: Einführung in Excel, Grundlagen -->
Hier sollte ein Einführungstext zum Thema "Einführung in Excel, Grundlagen" stehen.

## Themenüberschrift 01

A brief introduction to Excel

- Geschichte
- Oberfläche
- Unterschiede zu open software

- Überblick über Möglichkeiten (pivot etc pp)


Menüband (Ribbon): oben angeordnete Registerkarten (Start, Einfügen, Formeln, Daten, Überprüfen, Ansicht …), jede mit thematisch gruppierten Befehlen
Namensfeld: zeigt links oben die Adresse der aktuell markierten Zelle (z. B. B3) – kann auch genutzt werden, um direkt zu einer Zelle zu springen
Bearbeitungsleiste (Formelleiste): zeigt den tatsächlichen Inhalt der aktiven Zelle (Formel statt Ergebnis) – wichtig, um zu prüfen, ob eine Zelle eine Formel oder einen festen Wert enthält
Tabellenblatt-Reiter: unten am Bildschirmrand, zum Wechseln zwischen mehreren Sheets einer Arbeitsmappe (wie in unserer Übungsdatei: Anleitung, Rohdaten, Bearbeitung …)
Statusleiste: unten, zeigt bei markierten Zellbereichen automatisch Summe, Mittelwert und Anzahl an – praktisch für einen schnellen Check ohne extra Formel
Schnellzugriffsleiste: oben links, frei anpassbar mit häufig genutzten Befehlen (z. B. Speichern, Rückgängig)
Excel vs. Open-Source-Software
Wichtigste Alternative: LibreOffice Calc (kostenlos, quelloffen) – funktional ähnlich, aber nicht identisch
Formelkompatibilität: LibreOffice unterstützt einen etwas kleineren Funktionsumfang als Excel; manche neuere Excel-Funktionen (z. B. XVERWEIS) werden von LibreOffice nicht immer korrekt berechnet – das haben wir bei der Erstellung eurer Übungsdatei bewusst berücksichtigt (nur "klassische" Funktionen verwendet)
Dateiformate: Excel nutzt standardmäßig .xlsx, LibreOffice .ods – beide können das jeweils andere Format öffnen/speichern, aber komplexe Formatierungen oder Makros gehen dabei manchmal verloren
Makros/Automatisierung: Excel nutzt VBA (Visual Basic for Applications), LibreOffice eine eigene Basic-Variante – Code ist nicht 1:1 übertragbar
Kosten: Excel/Microsoft 365 ist kostenpflichtig (Abo), LibreOffice komplett kostenlos
Zusammenarbeit: Excel (über Microsoft 365/OneDrive) und Google Sheets (cloudbasiert, ebenfalls nicht Open Source) bieten Echtzeit-Zusammenarbeit; LibreOffice ist primär für lokale Einzelnutzung ausgelegt
Support & Verbreitung: Excel ist im professionellen/universitären Umfeld der De-facto-Standard – wichtig zu wissen, wenn ihr später Dateien mit anderen austauscht
Überblick über Excels Möglichkeiten
Formeln & Funktionen: mathematische (SUMME, MITTELWERT), logische (WENN, UND/ODER), Text- (die schon behandelten TEIL, GLÄTTEN, ERSETZEN), Datums- sowie Nachschlage-Funktionen (SVERWEIS, INDEX+VERGLEICH) zum Verknüpfen mehrerer Tabellen
PivotTables (Pivot-Tabellen): fassen große Datensätze interaktiv zusammen, ohne eine einzige Formel zu schreiben – Beispiel mit unserem Datensatz: durchschnittliche Temperatur automatisch gruppiert nach Ort_Typ (Stadtzentrum/Vorort/Dorf), einfach per Drag-and-Drop
Diagramme/Charts: visuelle Darstellung von Zahlenreihen (Balken, Linien, Streudiagramme) – z. B. Temperaturverlauf über die Messstationen hinweg
Bedingte Formatierung: Zellen färben sich automatisch abhängig vom Wert (z. B. hohe Temperaturen rot, niedrige blau) – nützlich, um Auffälligkeiten im Datensatz auf einen Blick zu erkennen
Datenvalidierung: schränkt ein, was in eine Zelle eingegeben werden darf (z. B. nur Zahlen zwischen -20 und 50 für Temperaturwerte) – verhindert Eingabefehler direkt an der Quelle
Power Query: Werkzeug zum Importieren und automatisierten Bereinigen/Transformieren von Daten aus externen Quellen (CSV, Datenbanken, Webseiten) – im Grunde eine grafische Oberfläche für genau die Art von Datenbereinigung, die wir in dieser Unit von Hand gemacht haben
Makros/VBA: Automatisierung wiederkehrender Arbeitsschritte per aufgezeichnetem oder selbst geschriebenem Code
Solver / Zielwertsuche: Werkzeuge zur Optimierung – Excel sucht automatisch den Eingabewert, der zu einem gewünschten Ergebnis führt


<!-- Notizen: Ab hier folgen Vermerke, welche als Gedankenstütze oder Erinnerung dienen aber noch nicht in der vorhandenen Form veröffentlicht werden sollen. -->
<!-- Bitte Gedanken innerhalb der Kommentarfunktion einfügen. -->
