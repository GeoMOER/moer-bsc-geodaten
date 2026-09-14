# Unit 14 – Moderation

Titelfolie, 35 Hauptfolien für 90 Minuten, zwei Reserve-/Quellenfolien und eine Abschlussfolie. Zeitangaben stehen nur in diesen Notizen.

## 01 · Kartengestaltung und Abschlusskarte

Titelfolie vor dem Einstieg zeigen.

Titelfolie beim Ankommen zeigen. Die Sitzung ist für 90 Minuten mit 100–150 Bachelor- und Lehramtsstudierenden ausgelegt. Vorbereitendes Lesen wird nicht vorausgesetzt. QGIS 3.40 und das vollständig entpackte Marburger Übungspaket müssen verfügbar sein. Alle beginnen mit unit14_start.qgz; eigene Ergebnisse aus Unit 13 sind nur Vertiefung.

Quellen / Anschluss an die HTML-Lernumgebung:
/home/dirk/GeoMOER/moer-bsc-geodaten/docs/slides/Vorlagen/präs_ms02_powerpoint_de.pptx

## 02 · JiTT · Rückblick auf Unit 13

Zeitfenster: Minute 0–10 (10 Minuten).

VOR DEM TERMIN: Den gesamten Platzhalter durch die aktuelle JiTT-Auswertung zu Unit 13 ersetzen. Bei Bedarf die Folie duplizieren. Nur tatsächliche, zusammengefasste und anonymisierte Rückmeldungen einsetzen. Die gesamte Phase dauert zehn Minuten. Verständnisfragen zu Rasterzellen, NoData, DGM oder hoehe_m klären.

## 03 · Von geprüften Höhenpunkten zur lesbaren Karte

Zeitfenster: Minute 10–11 (1 Minuten).

Den Ablauf ankündigen: Ausgangsprojekt prüfen, zwei Klassifizierungen vergleichen, eine Variante begründet gestalten, das vorbereitete Layout überarbeiten, beide Formate exportieren und eine Aussagegrenze dokumentieren.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit14/unit14-00_overview.html

## 04 · Startprojekt sofort als Arbeitskopie speichern

Zeitfenster: Minute 11–14 (3 Minuten).

Alle öffnen unit14_start.qgz im vollständig entpackten Paket und speichern sofort als unit14_abschluss.qgz. Nicht mit einem leeren Projekt beginnen und keine Analysen aus Units 11 bis 13 wiederholen. Bei technischen Problemen unit14_beispiel.qgz verwenden.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit14/unit14-00_overview.html
https://geomoer.github.io/moer-bsc-geodaten/material/qgis-kernpfade.html#unit14

## 05 · Kartenfrage und Zielgruppe zuerst festlegen

Zeitfenster: Minute 14–16 (2 Minuten).

Die Beispielkarte richtet sich an fachlich interessierte Personen ohne Detailkenntnis des Datensatzes. Titel, Legende und Symbolisierung müssen genau diese vorsichtige Frage beantworten. Zwei Minuten kurze Nachbarschaftsabsprache.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit14/unit14-00_overview.html
https://geomoer.github.io/moer-bsc-geodaten/unit14/unit14-03_kartenlayout.html

## 06 · Der Karteneingang umfasst 35 gültige Höhenwerte

Zeitfenster: Minute 16–18 (2 Minuten).

Den vorbereiteten Punktlayer prüfen: 35 Features, numerisches Feld hoehe_m, EPSG:25832. Die 21 weiteren qualitätsgeprüften Nachweise ohne DGM-Höhe sind nicht in dieser Höhenklassenkarte dargestellt. Diese Einschränkung muss sichtbar dokumentiert werden.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit14/unit14-00_overview.html
https://geomoer.github.io/moer-bsc-geodaten/material/qgis-kernpfade.html#unit14

## 07 · Klassengrenzen verändern die sichtbare Aussage

Zeitfenster: Minute 18–20 (2 Minuten).

Klassifizierung fasst einzelne Zahlenwerte zu wenigen Gruppen zusammen. Dadurch wird die Karte übersichtlicher, aber Information geht verloren. Ein Punktwert bleibt gleich; nur seine Zuordnung zu einer visuellen Klasse kann sich ändern.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit14/unit14-02_klassifizierung.html

## 08 · Gleiche Intervalle: gleiche Breite

Zeitfenster: Minute 20–22 (2 Minuten).

Bei gleichen Intervallen ist der gesamte Wertebereich in fünf gleich breite Abschnitte geteilt. Die Methode ist leicht erklärbar; bei ungleich verteilen Werten können die Klassen aber sehr unterschiedlich besetzt sein.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit14/unit14-02_klassifizierung.html

## 09 · Quantile: ungefähr gleich viele Punkte

Zeitfenster: Minute 22–24 (2 Minuten).

Quantile teilen die sortierten Werte so, dass jede Klasse ungefähr gleich viele Features enthält. Dadurch erscheinen meist alle Farben, aber die Wertebereiche sind unterschiedlich breit und ähnliche Werte können getrennt werden.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit14/unit14-02_klassifizierung.html

## 10 · Dieselben 35 Punkte – zwei sichtbare Muster

Zeitfenster: Minute 24–27 (3 Minuten).

Beide Karten zeigen dieselben 35 Punkte, denselben Ausschnitt, dieselbe Symbolgröße und dieselbe Farbpalette. Links gleiche Intervalle, rechts Quantile. Erst still vergleichen, dann Unterschiede zu zweit benennen. Die 21 Punkte ohne Höhe fehlen in beiden Darstellungen.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit14/unit14-02_klassifizierung.html

## 11 · Rechenprinzip und Klassenbesetzung

Zeitfenster: Minute 27–29 (2 Minuten).

Die Grafik erklärt das Rechenprinzip mit zehn erfundenen Höhenwerten, nicht mit den 35 Marburger Nachweisen. Links entstehen bei gleichen Intervallen die Besetzungen 8/1/0/0/1; rechts enthalten die interpolierten Quantile je zwei Werte. Softwarekonventionen können bei kleinen Datensätzen abweichen.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit14/unit14-02_klassifizierung.html

## 12 · Die realen Klassengrenzen vergleichen

Zeitfenster: Minute 29–30 (1 Minuten).

Grenzen aus den beiden vorbereiteten Legenden ablesen. Die Quantilgrenzen liegen bei etwa 214,3, 230,0, 245,0 und 267,7 m. Bei gleichen Intervallen liegen die inneren Grenzen ungefähr bei 207,6, 236,7, 265,8 und 294,8 m. Werte bleiben unverändert; nur Klassen ändern sich.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit14/unit14-02_klassifizierung.html

## 13 · Abgestufte Darstellung in QGIS einstellen

Zeitfenster: Minute 30–33 (3 Minuten).

Layereigenschaften → Symbolisierung öffnen. Abgestuft wählen, hoehe_m als Wert, eine sequentielle Palette und genau fünf Klassen einstellen. Erst danach die gewählte Methode anwenden. Keine neue Datenquelle und keine zusätzliche Analyse starten.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit14/unit14-01_symbolisierung.html
https://geomoer.github.io/moer-bsc-geodaten/unit14/unit14-02_klassifizierung.html
https://docs.qgis.org/3.40/en/docs/user_manual/

## 14 · Eine Methode auswählen und begründen

Zeitfenster: Minute 33–36 (3 Minuten).

Zwei Minuten zu zweit entscheiden, danach die gewählte Methode anwenden. Die Begründung muss sich auf Frage, Zielgruppe und sichtbare Wirkung beziehen. „Sieht schöner aus“ reicht nicht. Es gibt nicht für jeden Datensatz genau eine einzig richtige Methode.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit14/unit14-02_klassifizierung.html

## 15 · Klassen eindeutig und lesbar beschriften

Zeitfenster: Minute 36–38 (2 Minuten).

Die QGIS-Grenzen nicht unbesehen übernehmen. Legendenwerte sinnvoll runden, Einheit ergänzen und Überschneidungen vermeiden. Die tatsächlichen Grenzen bleiben korrekt, auch wenn die sichtbaren Beschriftungen lesefreundlich formuliert werden.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit14/unit14-02_klassifizierung.html

## 16 · Für Höhenwerte eine sequentielle Palette wählen

Zeitfenster: Minute 38–40 (2 Minuten).

Die Palette muss zur fachlichen Bedeutung passen. Qualitative Farben zeigen gleichrangige Kategorien, sequentielle Farben eine geordnete Zahl und divergierende Farben Abweichungen um einen Bezugspunkt. Für Geländehöhe verwenden wir heute eine sequentielle Palette.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit14/unit14-01_symbolisierung.html

## 17 · Symbolwahl folgt der Datenart

Zeitfenster: Minute 40–42 (2 Minuten).

Die Grafik zeigt dieselben drei Positionen. Formen beantworten die kategoriale Typfrage; geordnete Helligkeit beantwortet die numerische Höhenfrage. Die Beispieldaten sind erfunden. Heute ist hoehe_m die Hauptinformation.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit14/unit14-01_symbolisierung.html

## 18 · Die Hauptinformation muss zuerst auffallen

Zeitfenster: Minute 42–44 (2 Minuten).

Beide schematischen Karten zeigen identische Positionen, Fluss und Höhenlinien. Links dominiert der Hintergrund, rechts die Punktinformation. Im Startprojekt höchstens den vorbereiteten Hintergrund verwenden; zusätzliche Layer sind Vertiefung. Spätestens nach dieser Folie zum Layout wechseln.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit14/unit14-01_symbolisierung.html

## 19 · Vor dem Layout die Kartenansicht prüfen

Zeitfenster: Minute 44–45 (1 Minuten).

Gemeinsam kurz prüfen: gewählte Methode, fünf Klassen, hoehe_m, sequentielle Palette, lesbare Klassenbezeichnungen und zurückhaltender Hintergrund. Auch wenn einzelne Personen noch optimieren möchten, jetzt zum vorbereiteten Layout wechseln.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/material/qgis-kernpfade.html#unit14

## 20 · Das vorbereitete Layout gezielt ausarbeiten

Zeitfenster: Minute 45–46 (1 Minuten).

Im Projekt das vorhandene A4-Querformatlayout abschlusskarte_unit14 öffnen. Kein neues Layout anlegen. Aktiv geändert werden Titel und Legende; Kartenausschnitt, Maßstab und Quellen werden kontrolliert und nur bei einem konkreten Fehler korrigiert.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit14/unit14-03_kartenlayout.html
https://geomoer.github.io/moer-bsc-geodaten/material/qgis-kernpfade.html#unit14

## 21 · Die Beispielkarte ist eine Prüfreferenz

Zeitfenster: Minute 46–49 (3 Minuten).

Die Beispielkarte gemeinsam lesen: Was fällt zuerst auf, welche Information liefert die Legende, wo stehen Datenumfang und Quellen? Sie ist bei technischen Problemen eine Arbeitsgrundlage, aber kein Grund, Entscheidungen ungeprüft zu kopieren.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit14/unit14-03_kartenlayout.html

## 22 · Der Titel benennt den tatsächlichen Inhalt

Zeitfenster: Minute 49–51 (2 Minuten).

Titel in der Vorlage aktiv überarbeiten. Die Formulierung muss dokumentierte Nachweise statt vollständiger Verbreitung benennen und den Raumbezug verständlich machen.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit14/unit14-03_kartenlayout.html

## 23 · Die Legende erklärt Klassen statt Dateinamen

Zeitfenster: Minute 51–54 (3 Minuten).

Legendentitel und Klassentexte fachlich überarbeiten. Technische Layernamen und nicht sichtbare oder nicht benötigte Einträge entfernen. Höhenbezug verständlich als Geländehöhe am Nachweisort in Metern benennen.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit14/unit14-03_kartenlayout.html

## 24 · Kartenausschnitt und Maßstab funktional prüfen

Zeitfenster: Minute 54–56 (2 Minuten).

Alle relevanten Punkte müssen sichtbar sein, leere Flächen sollen die Karte nicht unnötig verkleinern. Maßstabseinheit und Teilung müssen zur Ausdehnung passen. Nur bei einem erkennbaren Fehler verändern; heute wird kein neuer Ausschnitt gestaltet.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit14/unit14-03_kartenlayout.html

## 25 · Quellen und Bearbeitung gehören in die Karte

Zeitfenster: Minute 56–59 (3 Minuten).

Die vorbereiteten Quellenangaben kontrollieren: NABU|naturgucker via GBIF, DGM1 des Hessen Geodatenmanagements, Bearbeitung und Datenabruf. Keinen neuen DOI erfinden. Zusätzlich 35 gültige Höhenpunkte und die 21 nicht dargestellten Nachweise transparent benennen.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit14/unit14-03_kartenlayout.html
https://www.gbif.org/dataset/6ac3f774-d9fb-4796-b3e9-92bf6c81c084
https://hvbg.hessen.de/landesvermessung/geotopographie/3d-daten/digitale-gelaendemodelle

## 26 · Layout in tatsächlicher Ausgabegröße prüfen

Zeitfenster: Minute 59–62 (3 Minuten).

Vor dem Export die Seite als Ganzes prüfen. Titel, fünf Klassen, Einheiten und Quellen müssen ohne starkes Zoomen lesbar sein. Hintergrund und Nebenelemente dürfen nicht mit den Punkten konkurrieren. Spätestens jetzt zum Export wechseln.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit14/unit14-03_kartenlayout.html

## 27 · Zwei Formate mit verbindlichen Dateinamen exportieren

Zeitfenster: Minute 62–65 (3 Minuten).

Im Layout zuerst PDF exportieren, danach als Bild PNG wählen und 150 dpi einstellen. Beide Dateien gehören in figures. Vorhandene Beispielausgaben nicht versehentlich überschreiben; die eigenen Ausgaben tragen die verbindlichen Namen.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit14/unit14-03_kartenlayout.html
https://geomoer.github.io/moer-bsc-geodaten/material/qgis-kernpfade.html#unit14

## 28 · PDF und PNG außerhalb von QGIS öffnen

Zeitfenster: Minute 65–68 (3 Minuten).

Beide Dateien mit einem unabhängigen Anzeigeprogramm öffnen und in der vorgesehenen Größe prüfen. Auf abgeschnittene Elemente, Ersatzschriften, unlesbare Klassen, unerwartete Rasterflächen und unvollständige Quellen achten.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit14/unit14-03_kartenlayout.html

## 29 · Vier Produkte vor dem Partnercheck sichern

Zeitfenster: Minute 68–70 (2 Minuten).

Arbeitsprojekt speichern und prüfen, ob beide Exporte und das vorbereitete Protokoll am erwarteten Ort vorhanden sind. Die Dokumentation wird erst nach dem Partnercheck vervollständigt.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit14/unit14-00_overview.html

## 30 · Partnercheck: Karte ohne Zusatzwissen lesen

Zeitfenster: Minute 70–73 (3 Minuten).

Zu zweit die exportierten Karten tauschen. Drei Minuten: Die betrachtende Person beschreibt zuerst ohne Erklärung die sichtbare Kernaussage. Bei technischen Problemen die bereitgestellte Beispielkarte verwenden.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit14/unit14-00_overview.html

## 31 · Eine konkrete Verbesserung priorisieren

Zeitfenster: Minute 73–76 (3 Minuten).

Zwei Minuten Rückmeldung: Nur die wichtigste fachliche oder gestalterische Verbesserung auswählen. Priorität haben missverständliche Aussagen, unklare Klassen oder fehlende Quellen, nicht persönliche Geschmacksfragen.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit14/unit14-00_overview.html

## 32 · Korrektur übernehmen und betroffenen Export erneuern

Zeitfenster: Minute 76–80 (4 Minuten).

Die wichtigste Korrektur direkt in Projekt oder Layout übernehmen. Betrifft sie Karteninhalt, Klassen oder gemeinsame Texte, beide Formate erneut exportieren und öffnen. Betrifft sie ausschließlich ein formatbezogenes Exportproblem, nur den betroffenen Export erneuern. Projekt danach speichern.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit14/unit14-00_overview.html
https://geomoer.github.io/moer-bsc-geodaten/material/qgis-kernpfade.html#unit14

## 33 · Entscheidungen im vorhandenen Protokoll festhalten

Zeitfenster: Minute 80–83 (3 Minuten).

Nur den vorhandenen Abschnitt Unit 14: Abschlusskarte ergänzen. Gewählte Methode, fünf Klassengrenzen, Palette, Datenquellen, 35/21-Einschränkung, Partnerkorrektur und Exportpfade dokumentieren. Keine vollständige Workflowdokumentation neu schreiben.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit14/unit14-05_workflow.html

## 34 · Beobachtungen beschreiben – keine Verbreitung behaupten

Zeitfenster: Minute 83–85 (2 Minuten).

Gemeinsam eine belastbare und eine unzulässige Formulierung unterscheiden. Die Karte zeigt räumlich und zeitlich ungleich erhobene Nachweise; sie belegt weder vollständige Verbreitung noch eine ursächliche Höhenpräferenz. Außerdem fehlen 21 Nachweise ohne gültige DGM-Höhe.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit14/unit14-05_workflow.html

## 35 · Exit Ticket · eine Frage auswählen

Zeitfenster: Minute 85–88 (3 Minuten).

Eine der drei Fragen passend zum tatsächlichen Sitzungsverlauf auswählen. Zwei Minuten einzeln notieren, danach per Handzeichen oder mit zwei bis drei kurzen Antworten auflösen. Nicht alle drei Fragen bearbeiten lassen.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit14/unit14-00_overview.html

## 36 · Nachbereitung · JiTT zu Unit 14

Zeitfenster: Minute 88–90 (2 Minuten).

Die einzige Übungsaufgabe ankündigen: JiTT-Fragen zu Unit 14 im ILIAS-Kurs. Fragen und Frist ausschließlich aus ILIAS nennen; der Link auf der Kursseite ist noch ein sichtbarer Platzhalter. Nicht abgeschlossene Layoutvarianten werden nicht als zusätzliche Übungsaufgabe aufgegeben. Unit 15 beginnt mit der JiTT-Auswertung und schließt den Kurs ab.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit14/unit14-04_assignment.html

## 37 · Vertiefung: den vollständigen Workflow rekonstruieren

Reserve; nicht zusätzlich in die 90 Minuten einplanen.

Nur bei Bedarf zeigen. Der verbindliche Präsenzweg beginnt mit dem vorbereiteten Projekt. Die Rekonstruktion von Datenprüfung, Auswahl, Rasterabtastung und neuem Layout ist freiwillige Vertiefung und darf nicht den Export- und Partnercheck verdrängen.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit14/unit14-05_workflow.html

## 38 · Quellen und Arbeitsstand

Reserve; nicht zusätzlich in die 90 Minuten einplanen.

Nur bei Bedarf zeigen. Die Folie dokumentiert Kursseiten, QGIS-Dokumentation und Datenquellen. Die Live-Erreichbarkeit externer Seiten ist für den Präsenzkern nicht erforderlich.

Quellen / Anschluss an die HTML-Lernumgebung:
https://geomoer.github.io/moer-bsc-geodaten/unit14/unit14-00_overview.html

## 39 · Vielen Dank für Ihre Aufmerksamkeit

Abschluss nach der Nachbereitung; kein zusätzlicher Zeitblock.

Die Sitzung mit dieser Folie beenden. Die Abschlussgestaltung nutzt den Kontakt-Master der universitären Vorlage sowie das originale Foto-/Kartenmotiv aus der FB19-Titelseite.

Quellen / Anschluss an die HTML-Lernumgebung:
/home/dirk/GeoMOER/moer-bsc-geodaten/docs/slides/Vorlagen/präs_ms02_powerpoint_de.pptx

