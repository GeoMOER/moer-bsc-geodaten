---
title: HA | Hausaufgabe Abschnitt 10
published: true
toc: true
header:
  image: /assets/images/unit10/hero-unit10.jpg
  image_description: "Luftbildlandschaft mit überlagerten Punkten, Linien, Polygonflächen und Rasterzellen"
  caption: "KI-generierte Illustration, bearbeitet für diesen Kurs"
---

<!-- Hausaufgabe 10: Geodatenmodelle, QGIS und WMS -->

## Hausaufgabe 10

In dieser Hausaufgabe wenden Sie die Inhalte aus Abschnitt 10 selbstständig an. Sie richten einen übersichtlichen Arbeitsordner ein, erstellen ein QGIS-Projekt, laden lokale Vektor- und Rasterdaten, untersuchen deren Eigenschaften und ergänzen einen WMS aus einem Geoportal.

| Rahmenbedingung | Festlegung |
|---|---|
| Bearbeitungszeit | etwa 75–90 Minuten |
| Abgabeformat | vollständiger Arbeitsordner als `unit10_nachname_vorname.zip` |
| Abgabeort | `[ILIAS-Ordner beziehungsweise Abgabeort ergänzen]` |
| Abgabetermin | `[Datum und Uhrzeit ergänzen]` |
| Arbeitsform | Einzelarbeit; ein fachlicher Austausch ist erlaubt, Projekt und Dokumentation müssen selbst erstellt sein. |

## Lernziele

Nach der Bearbeitung können Sie ...

* Vektor- und Rasterdaten anhand ihrer Struktur unterscheiden,
* Punkt, Linie und Polygon als Geometrietypen des Vektormodells erkennen,
* einen nachvollziehbaren Arbeitsordner und ein QGIS-Projekt anlegen,
* lokale Vektor- und Rasterlayer in QGIS laden und organisieren,
* Features und Attribute eines Vektorlayers untersuchen,
* Datenquelle und CRS eines Layers prüfen,
* einen vorgegebenen WMS in QGIS einbinden und
* lokale Daten und Webdienste nachvollziehbar dokumentieren.

## Vorbereitung

Für die Hausaufgabe benötigen Sie:

* eine funktionsfähige QGIS-Installation,
* die bereitgestellten Übungsdaten,
* die in der Lehrveranstaltung verwendete WMS-Dienstadresse und
* eine Internetverbindung.

Verwendete Materialien:

| Material | Angabe |
|---|---|
| QGIS-Version | `[verbindliche QGIS-LTR-Version ergänzen]` |
| Download der Übungsdaten | `[Link ergänzen]` |
| lokaler Vektorlayer | `[Datei beziehungsweise Layer ergänzen]` |
| lokaler Rasterlayer | `[Datei beziehungsweise Layer ergänzen]` |
| Projekt-CRS | `[gemeinsamen EPSG-Code ergänzen; für Marburg voraussichtlich EPSG:25832]` |
| WMS-Verbindungsname | `[Name ergänzen]` |
| WMS-Dienstadresse | `[URL ergänzen]` |
| WMS-Layer | `[Layername ergänzen]` |
| WMS-Metadatenseite | `[URL ergänzen]` |
| Ersatzmaterial bei Dienstausfall | `[Downloadlink ergänzen]` |

Verwenden Sie ausschließlich das bereitgestellte, kompakte Datenpaket. Verändern Sie die Dateien in `data_raw` nicht. Bei einem nachweisbaren WMS-Ausfall bearbeiten Sie Aufgabe 3 mit dem Ersatzmaterial; der Ausfall wird nicht als Fehler bewertet.

## Aufgabe 1: Arbeitsordner und Projekt

Legen Sie einen neuen Arbeitsordner mit folgender Struktur an:

```text
hausaufgabe10_nachname/
  data_raw/
  data_output/
  documentation/
  hausaufgabe10_nachname.qgz
```

1. Speichern Sie die unveränderten Übungsdaten im Ordner `data_raw`.
2. Starten Sie QGIS und erstellen Sie ein neues Projekt.
3. Speichern Sie das Projekt unter dem angegebenen Namen im Arbeitsordner.
4. Stellen Sie das vorgegebene Projekt-CRS ein und notieren Sie den EPSG-Code.
5. Konfigurieren Sie Projektpfade – soweit in der eingesetzten QGIS-Version verfügbar – relativ zum Projektordner.
6. Speichern Sie das Projekt.

Beantworten Sie anschließend kurz:

> Was speichert die `.qgz`-Datei, und warum reicht sie allein möglicherweise nicht aus, um das Projekt auf einem anderen Rechner vollständig zu öffnen?

## Aufgabe 2: Lokale Layer laden und untersuchen

1. Laden Sie den bereitgestellten Vektorlayer und Rasterlayer in das Projekt.
2. Benennen Sie beide Layer im Layer-Bereich eindeutig.
3. Ordnen Sie die Layer so an, dass beide sinnvoll sichtbar sind.
4. Zoomen Sie auf die Ausdehnung des Vektorlayers.
5. Öffnen Sie die Attributtabelle des Vektorlayers.
6. Wählen Sie ein Feature in der Tabelle aus und lokalisieren Sie es in der Karte.
7. Rufen Sie die Eigenschaften beider Layer auf.
8. Füllen Sie die folgende Tabelle aus.

| Merkmal | Vektorlayer | Rasterlayer |
|---|---|---|
| Anzeigename in QGIS |  |  |
| Datenquelle / Dateiname |  |  |
| Datenmodell |  |  |
| Geometrietyp beziehungsweise Rasterinhalt |  |  |
| CRS / EPSG-Code |  |  |
| räumliche Ausdehnung |  |  |
| wichtigste Attribute beziehungsweise Zellwerte |  |  |
| geeignete Fragestellung |  |  |

Erklären Sie in zwei bis drei Sätzen, warum der jeweilige Inhalt als Vektor beziehungsweise Raster modelliert wurde. Nennen Sie dabei mindestens eine sinnvolle Alternative, falls derselbe Ausschnitt der Realität auch anders modelliert werden könnte.

## Aufgabe 3: Einen WMS ergänzen

1. Öffnen Sie den Datenquellenmanager und wählen Sie **WMS/WMTS**.
2. Legen Sie mit dem vorgegebenen Namen und der bereitgestellten Dienstadresse eine neue Verbindung an.
3. Stellen Sie die Verbindung zum Dienst her.
4. Wählen Sie den vorgegebenen WMS-Layer aus und fügen Sie ihn dem Projekt hinzu.
5. Ordnen Sie den WMS sinnvoll im Layer-Bereich an.
6. Prüfen Sie, ob lokale Layer und WMS räumlich korrekt übereinanderliegen.
7. Speichern Sie das Projekt erneut.

Dokumentieren Sie den Dienst:

| Angabe | Ihre Dokumentation |
|---|---|
| vollständiger Titel des Dienstes |  |
| herausgebende Stelle |  |
| WMS-Dienstadresse |  |
| verwendeter WMS-Layer |  |
| räumliche Abdeckung |  |
| unterstütztes beziehungsweise verwendetes CRS |  |
| Datenstand / Aktualität |  |
| Lizenz / Quellenangabe |  |
| Zugriffsdatum |  |

Falls eine Angabe nicht zu finden ist, schreiben Sie nicht einfach „unbekannt“. Dokumentieren Sie zusätzlich, wo Sie danach gesucht haben.

## Aufgabe 4: Lokale Daten und WMS vergleichen

Beantworten Sie die folgenden Fragen jeweils in zwei bis drei Sätzen:

1. Welche Informationen liegen in Ihren lokalen Datendateien vor, welche werden über den WMS abgerufen?
2. Warum können Sie bei einem lokalen Vektorlayer eine gewöhnliche Attributtabelle öffnen, bei einem WMS aber meist nicht?
3. Für welche Aufgabe in Ihrem Projekt ist der WMS geeignet?
4. Für welche weitergehende Analyse würden Sie stattdessen einen Download oder WFS benötigen?
5. Was würde beim Öffnen des Projekts ohne Internetverbindung voraussichtlich mit den lokalen Layern und dem WMS geschehen?

## Aufgabe 5: Ergebnis sichern

Speichern Sie das Projekt und schließen Sie QGIS. Öffnen Sie es anschließend erneut und prüfen Sie:

* Werden alle lokalen Layer gefunden?
* Wird der WMS geladen?
* Ist die Layerreihenfolge erhalten?
* Ist der gewünschte Kartenausschnitt sichtbar?
* Sind die Layer eindeutig benannt?

Erstellen Sie danach einen Screenshot, auf dem mindestens Kartenansicht und Layer-Bereich sichtbar sind.

Erstellen Sie außerdem `documentation/processing_notes.md` mit folgenden Überschriften:

```markdown
# Arbeitsumgebung und QGIS-Version
# Projekt und Ordnerstruktur
# Lokale Datenquellen
# Projekt- und Layer-CRS
# WMS und Metadaten
# Vergleich lokaler Daten und Webdienst
# Öffnungstest
# Bearbeitungsdatum
```

Tragen Sie die Tabellen und Antworten aus dieser Aufgabe unter den passenden Überschriften ein. Vermerken Sie einen möglichen WMS-Ausfall und die Verwendung des Ersatzmaterials.

## Einzureichende Ergebnisse

Reichen Sie folgende Bestandteile ein:

1. `hausaufgabe10_nachname.qgz`,
2. die bereitgestellten lokalen Daten im unveränderten Ordner `data_raw`,
3. den Screenshot im Ordner `data_output`,
4. `documentation/processing_notes.md` mit den ausgefüllten Tabellen und Antworten.

Komprimieren Sie den vollständigen Ordner als `unit10_nachname_vorname.zip`. Öffnen Sie das ZIP-Archiv probeweise und kontrollieren Sie seine Struktur. Das von der Lehrperson bereitgestellte Datenpaket muss deshalb klein genug für die Lernplattform sein.

## Abgabecheck

Prüfen Sie vor der Abgabe, ob ...

* der Arbeitsordner übersichtlich strukturiert ist,
* das QGIS-Projekt einen eindeutigen Dateinamen besitzt,
* mindestens ein Vektor-, ein Raster- und ein WMS-Layer enthalten sind,
* Layernamen und Reihenfolge verständlich sind,
* die Attributtabelle des Vektorlayers untersucht wurde,
* CRS von Projekt und Layern dokumentiert sind,
* Quelle, Lizenz und Zugriffsdatum des WMS angegeben sind,
* die Unterschiede zwischen lokalen Daten und WMS verständlich erklärt sind und
* das Projekt nach dem erneuten Öffnen noch funktioniert.

## Bewertung

Die Hausaufgabe wird anhand von **40 Punkten** bewertet.

| Bereich | Punkte | vollständig erfüllt, wenn ... |
|---|---:|---|
| Arbeitsordner und Projekt | 6 | Struktur, Dateinamen, Projekt-CRS und möglichst relative Pfade sind korrekt; Projekt und Daten werden unterschieden. |
| Lokale Layer untersuchen | 12 | Vektor und Raster sind richtig geladen, geordnet und anhand von Quelle, Modell, Inhalt, CRS, Ausdehnung und geeigneter Fragestellung dokumentiert. |
| WMS einbinden und dokumentieren | 10 | Dienst oder Ersatzmaterial wird korrekt verwendet; Layer, technische URL, Herausgeber, Datenstand, CRS, Lizenz und Zugriff sind nachvollziehbar dokumentiert. |
| Vergleich und Reflexion | 8 | Lokale Daten, WMS und WFS werden hinsichtlich Inhalt, Analysefähigkeit, Internetabhängigkeit und Reproduzierbarkeit fachlich unterschieden. |
| Öffnungstest und Abgabe | 4 | Projekt wurde erneut geöffnet; Screenshot, Arbeitsnotizen und vollständige ZIP-Struktur sind vorhanden. |

Für das Bestehen sind **`[Mindestpunktzahl ergänzen, Vorschlag: 20 von 40 Punkten]`** erforderlich. Fachlich gleichwertige Lösungen sind zulässig. Ein klar dokumentierter technischer Dienstausfall führt nicht zu Punktabzug. Folgefehler werden nicht mehrfach bewertet.

<!-- Lösungshinweise für Lehrende:

Aufgabe 1:
- Die Projektdatei speichert unter anderem Layerverweise, Darstellung, Reihenfolge, Kartenausschnitt und Projekt-CRS.
- Lokale Datendateien sind normalerweise nicht vollständig in der qgz-Datei enthalten. Verschobene, umbenannte oder nicht mitgelieferte Daten führen zu defekten Pfaden.

Aufgabe 2:
- Erwartete Dateinamen, Featurezahl, Rastergröße, CRS, Ausdehnungen und zentrale Felder vor Kursbeginn mit dem finalen Datenpaket ergänzen.
- Entscheidend sind korrekte Zuordnung von Vektor/Raster, Geometrietyp beziehungsweise Rasterinhalt, CRS und eine fachlich passende Fragestellung.
- Die alternative Modellierung soll zeigen, dass Datenmodelle von Maßstab und Fragestellung abhängen.

Aufgabe 3:
- Angaben mit Metadatenseite des ausgewählten Dienstes abgleichen.
- Die technische Dienstadresse muss von der Portalseite unterschieden werden.
- Fehlende Metadaten sollen als Problem erkannt und der Suchweg dokumentiert werden.
- Bei Dienstausfall werden dieselben Punkte anhand des Ersatzmaterials bewertet.

Aufgabe 4:
- Lokale Dateien stehen ohne Internet zur Verfügung; der WMS benötigt den erreichbaren Server.
- Ein WMS liefert primär Kartenbilder, ein WFS Vektorfeatures mit Geometrien und Attributen.
- Für räumliche Vektoranalysen ist ein geeigneter Download oder WFS erforderlich.

Aufgabe 5:
- Beim erneuten Öffnen sollten relative beziehungsweise funktionierende Datenpfade erhalten bleiben.
- Der Screenshot dient als schnell sichtbarer Nachweis von Layerreihenfolge und gemeinsamer Darstellung.
-->

<!-- Notizen: Ab hier folgen Vermerke, welche als Gedankenstütze oder Erinnerung dienen, aber noch nicht in der vorhandenen Form veröffentlicht werden sollen. -->

<!--
Vor Durchführung ergänzen:
- Übungsdaten und Downloadlink
- konkreter Vektor- und Rasterlayer
- WMS-Verbindungsname, Dienstadresse und Layer
- Projekt-CRS
- erwartete Metadaten und Quellenangabe
- erwartete Featurezahl, Rastergröße, CRS und Ausdehnungen
- Ersatzmaterial bei WMS-Ausfall
- Abgabetermin und Abgabeort
- verbindliche Mindestpunktzahl
- Upload-Limit der Lernplattform gegen das fertige ZIP testen

Mögliche Vereinfachung:
- Aufgabe 4 auf die Fragen 2, 3 und 5 reduzieren.

Mögliche Erweiterung:
- Studierende suchen selbstständig einen zweiten thematisch passenden WMS und begründen dessen Auswahl anhand der Metadaten.
-->
