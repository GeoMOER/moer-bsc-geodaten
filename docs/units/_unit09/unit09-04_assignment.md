---
title: HA | Hausaufgabe Abschnitt 09
published: true
toc: true
header:
  image: /assets/images/unit09/hero-unit09.jpg
  image_description: "Breiter Blick auf Europa auf einer gekrümmten Erde mit feinem Koordinatengitter und markiertem Ort"
  caption: "KI-generierte Illustration, bearbeitet für diesen Kurs"
---

<!-- Hausaufgabe 09: Geodaten, Koordinaten und Projektionen -->

## Hausaufgabe 09

In dieser Hausaufgabe wenden Sie die Inhalte aus Abschnitt 09 selbstständig an. Sie untersuchen, wie Orte durch Koordinaten beschrieben werden, prüfen fehlerhafte Koordinatendaten und wählen für verschiedene Aufgaben ein geeignetes Koordinatenreferenzsystem aus.

Für die Bearbeitung benötigen Sie noch kein GIS. Verwenden Sie die Inhalte dieser Unit sowie die unten genannten Arbeitsmittel.

| Rahmenbedingung | Festlegung |
|---|---|
| Bearbeitungszeit | etwa 45–60 Minuten |
| Abgabeformat | eine PDF-Datei mit dem Namen `unit09_nachname_vorname.pdf` |
| Abgabeort | `[ILIAS-Ordner beziehungsweise Abgabeort ergänzen]` |
| Abgabetermin | `[Datum und Uhrzeit ergänzen]` |
| Arbeitsform | Einzelarbeit; ein fachlicher Austausch ist erlaubt, die eingereichten Antworten müssen selbst formuliert sein. |

## Arbeitsmittel

* Kursseiten der Unit 9,
* [OpenStreetMap](https://www.openstreetmap.org/){:target="_blank"} zum Auffinden eines öffentlich bekannten Ortes,
* [EPSG.io](https://epsg.io/){:target="_blank"} zum Prüfen von CRS-Bezeichnungen und EPSG-Codes und
* die Abbildungen auf der Seite „Koordinatenreferenzsysteme & Projektionen“.

Ein anderer Kartendienst darf verwendet werden, wenn Koordinaten, CRS beziehungsweise Koordinatenkonvention und Quelle nachvollziehbar dokumentiert werden. Beachten Sie: Das CRS der sichtbaren Webkarte und das CRS ausgegebener Positionskoordinaten können verschieden sein.

## Lernziele

Nach der Bearbeitung können Sie ...

* einen Ort durch geographische Koordinaten in Dezimalgrad beschreiben,
* Breiten- und Längengrad sowie deren Reihenfolge eindeutig dokumentieren,
* Koordinaten durch einfache Plausibilitätsprüfungen kontrollieren,
* geographische und projizierte Koordinaten unterscheiden,
* für eine konkrete Aufgabe ein grundsätzlich geeignetes CRS auswählen und
* erklären, warum Koordinatenwerte ohne Angabe des CRS nicht eindeutig sind.

## Aufgabe 1: Einen Ort dokumentieren

Wählen Sie einen öffentlich bekannten Ort, beispielsweise ein Universitätsgebäude, einen Bahnhof, einen Aussichtspunkt oder eine Sehenswürdigkeit. Verwenden Sie aus Datenschutzgründen nicht Ihre private Wohnadresse.

Ermitteln Sie die geographischen Koordinaten dieses Ortes in Dezimalgrad und dokumentieren Sie:

1. den Namen und eine kurze Beschreibung des Ortes,
2. den Breitengrad (*Latitude*),
3. den Längengrad (*Longitude*),
4. das Koordinatenpaar in der Reihenfolge `(Längengrad, Breitengrad)`,
5. das verwendete Koordinatenreferenzsystem beziehungsweise den EPSG-Code und
6. die verwendete Datenquelle als Link und
7. das Zugriffsdatum.

Verwenden Sie für Ihre Antwort folgende Tabelle:

| Angabe | Ihre Antwort |
|---|---|
| Name des Ortes |  |
| kurze Beschreibung |  |
| Breitengrad / Latitude |  |
| Längengrad / Longitude |  |
| Koordinatenpaar `(lon, lat)` |  |
| CRS / EPSG-Code |  |
| Datenquelle |  |
| Zugriffsdatum |  |

Beantworten Sie anschließend in einem Satz:

> Welche Informationen würden fehlen, wenn Sie lediglich das Zahlenpaar ohne Spaltennamen, Reihenfolge, Einheit und CRS weitergeben würden?

> **Kurskonvention:** Geben Sie das Koordinatenpaar in dieser Aufgabe als `(longitude, latitude)` beziehungsweise `(x, y)` an. Andere Dienste oder Standards können eine andere Achsenreihenfolge erwarten; übernehmen Sie Werte deshalb nie ohne Prüfung der Beschriftung.

## Aufgabe 2: Koordinaten prüfen

Die folgende Tabelle soll Orte in Hessen enthalten. Die Koordinaten sind als Dezimalgrad gespeichert. Die Spaltenreihenfolge ist eindeutig als `longitude, latitude` angegeben.

| id | ort | longitude | latitude |
|---:|---|---:|---:|
| 1 | Marburg | 8.77 | 50.81 |
| 2 | Kassel | 51.31 | 9.49 |
| 3 | Frankfurt am Main | 8.68 | 50.11 |
| 4 | Fulda | 9.68 | 91.15 |
| 5 | unbekannter Ort | 0.00 | 0.00 |

Prüfen Sie jede Zeile und ergänzen Sie eine eigene Ergebnistabelle mit den folgenden Spalten:

| id | Bewertung | vermutetes Problem | mögliche Korrektur oder weiterer Prüfschritt |
|---:|---|---|---|
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |
| 4 |  |  |  |
| 5 |  |  |  |

Nutzen Sie dabei mindestens diese Prüffragen:

* Liegt der Breitengrad zwischen `−90` und `+90`?
* Liegt der Längengrad zwischen `−180` und `+180`?
* Ist die angegebene Reihenfolge eingehalten?
* Ist die Position für einen Ort in Hessen plausibel?
* Könnte `(0, 0)` als Platzhalter für fehlende Werte verwendet worden sein?

> **Wichtig:** Verändern oder löschen Sie auffällige Daten nicht stillschweigend. Dokumentieren Sie immer, welches Problem Sie vermuten und auf welcher Grundlage eine Korrektur erfolgen könnte.

## Aufgabe 3: Ein geeignetes CRS auswählen

Wählen Sie für jedes Szenario eines der folgenden Koordinatenreferenzsysteme aus:

* `EPSG:4326` – WGS 84, geographische Koordinaten in Grad
* `EPSG:25832` – ETRS89 / UTM Zone 32N, projizierte Koordinaten in Metern
* `EPSG:3857` – WGS 84 / Pseudo-Mercator, häufige Darstellung in Webkarten

Begründen Sie jede Auswahl in ein bis zwei Sätzen. Gehen Sie dabei auf Untersuchungsgebiet, Einheit und Verwendungszweck ein.

### Szenario A

Artenbeobachtungen aus verschiedenen Ländern sollen mit den von GPS-Geräten gelieferten Längen- und Breitengraden in einer gemeinsamen Tabelle gespeichert werden.

### Szenario B

Für mehrere Untersuchungsflächen rund um Marburg sollen Entfernungen in Metern und Flächen in Quadratmetern berechnet werden.

### Szenario C

Geodaten sollen gemeinsam mit den Kartenkacheln eines üblichen Online-Kartendienstes im Browser dargestellt werden. Präzise Flächenberechnungen sind nicht vorgesehen.

| Szenario | gewähltes CRS | Begründung |
|---|---|---|
| A |  |  |
| B |  |  |
| C |  |  |

## Aufgabe 4: Kurz erklärt

Beantworten Sie die folgenden Fragen jeweils in zwei bis drei Sätzen:

1. Warum lässt sich die gekrümmte Erdoberfläche nicht ohne Verzerrungen auf einer ebenen Karte darstellen?
2. Worin unterscheiden sich geographische und projizierte Koordinatensysteme?
3. Was ist der Unterschied zwischen dem **Zuweisen** eines CRS und dem **Transformieren** von Geodaten in ein anderes CRS?

## Abgabecheck

Prüfen Sie vor der Abgabe, ob ...

* alle vier Aufgaben bearbeitet sind,
* Koordinaten eindeutig beschriftet und in der geforderten Reihenfolge angegeben sind,
* Datenquelle und CRS des selbst gewählten Ortes dokumentiert sind,
* das Zugriffsdatum angegeben ist,
* Auffälligkeiten in der Koordinatentabelle nachvollziehbar begründet sind und
* die CRS-Auswahl nicht nur genannt, sondern mit dem jeweiligen Zweck begründet wurde.

## Bewertung

Die Hausaufgabe wird anhand von **20 Punkten** bewertet.

| Bereich | Punkte | vollständig erfüllt, wenn ... |
|---|---:|---|
| Aufgabe 1: Ort dokumentieren | 4 | Ort, Latitude, Longitude, Paar, CRS, Quelle und Zugriffsdatum sind eindeutig und plausibel angegeben. |
| Aufgabe 2: Koordinaten prüfen | 6 | Alle Zeilen werden auf Wertebereich, Reihenfolge und räumliche Plausibilität geprüft; Vermutungen und Korrekturen werden nachvollziehbar getrennt. |
| Aufgabe 3: CRS auswählen | 6 | Für alle Szenarien wird ein grundsätzlich geeignetes CRS gewählt und mit Raum, Einheit und Zweck begründet. |
| Aufgabe 4: Begriffe erklären | 4 | Projektion, CRS-Gruppen sowie Zuweisen und Transformieren werden fachlich korrekt unterschieden. |

Für das Bestehen sind **`[Mindestpunktzahl ergänzen, Vorschlag: 10 von 20 Punkten]`** erforderlich. Fachlich gleichwertige, nachvollziehbar begründete Lösungen sind zulässig. Ein Fehler wird nicht mehrfach abgezogen, wenn spätere Antworten auf einem klar dokumentierten vorherigen Ergebnis aufbauen.

<!-- Lösungshinweise für Lehrende:

Aufgabe 1:
- Erwartet wird eine eindeutige Dokumentation von Latitude, Longitude, Reihenfolge, Einheit, CRS und Quelle.
- Das Zugriffsdatum muss enthalten sein.
- Bei einem üblichen Online-Kartendienst muss geprüft werden, ob ausgegebene Positionsangaben tatsächlich WGS 84 / EPSG:4326 sind. Die Projektion der sichtbaren Hintergrundkarte kann davon abweichen.

Aufgabe 2:
- ID 1: formal und räumlich plausibel.
- ID 2: Beide Werte liegen in ihren allgemeinen Wertebereichen, für die ausdrücklich angegebene Reihenfolge und Kassel sind sie aber unplausibel. Longitude und Latitude wurden vermutlich vertauscht. Plausible Werte wären ungefähr 9.49, 51.31; eine Korrektur muss anhand der Quelle geprüft werden.
- ID 3: formal und räumlich plausibel.
- ID 4: Latitude 91.15 liegt außerhalb des zulässigen Wertebereichs. Die korrekte Position muss anhand der Quelle geprüft werden; aus der Tabelle allein ist keine sichere Korrektur möglich.
- ID 5: formal gültiges Koordinatenpaar im Golf von Guinea, für Hessen aber unplausibel. Vermutlich Platzhalter für fehlende Werte; Originaldaten oder Metadaten prüfen und gegebenenfalls als fehlend kennzeichnen.

Aufgabe 3:
- A: EPSG:4326, weil globale Längen- und Breitengrade in Grad gespeichert werden sollen.
- B: EPSG:25832, weil Marburg in UTM-Zone 32N liegt und lineare Einheiten für regionale Entfernungs- und Flächenberechnungen benötigt werden.
- C: EPSG:3857 für die hier vereinfachte gemeinsame Darstellung mit üblichen Webkartenkacheln; keine präzisen Flächenberechnungen damit durchführen.
- Die Begründung ist wichtiger als die bloße Nennung des Codes.

Aufgabe 4:
- Projektionen verursachen unvermeidliche Verzerrungen von Fläche, Form, Entfernung oder Richtung.
- Geographische Systeme verwenden Winkelkoordinaten, meist in Grad; projizierte Systeme bilden einen Teil der Erdoberfläche auf einer Ebene ab und verwenden häufig Meter.
- Zuweisen interpretiert unveränderte Koordinatenwerte in einem angegebenen CRS; Transformieren berechnet neue Koordinatenwerte für dasselbe Objekt in einem anderen CRS.
-->

<!-- Notizen: Ab hier folgen Vermerke, welche als Gedankenstütze oder Erinnerung dienen, aber noch nicht in der vorhandenen Form veröffentlicht werden sollen. -->

<!--
Vor Durchführung ergänzen:
- Abgabefrist
- Abgabeort beziehungsweise Lernplattform
- verbindliche Mindestpunktzahl
- prüfen, ob PDF-Erzeugung für alle Studierenden barrierearm möglich ist

Mögliche Kürzung:
- Wenn die Bearbeitungszeit unter 45 Minuten bleiben soll, Aufgabe 4 auf eine der drei Fragen reduzieren.

Mögliche Erweiterung:
- Studierende vergleichen den gewählten Ort zusätzlich in zwei Kartenprojektionen und beschreiben sichtbare Unterschiede.
-->
