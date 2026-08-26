---
title: Geodaten finden und einbinden
published: true
toc: true
header:
  image: /assets/images/spotlight01/jekyll_github_pages.png
  image_description: "Cutout from Measured carbon dioxide concentrations in Vancouver"
  caption: "Bild: [jekyll](https://jekyllrb.com/)"
---

<!-- Introtext: Von lokalen Übungsdaten zu realen Geodatenquellen und webbasierten Diensten. -->

## Woher kommen Geodaten?

Auf der vorherigen Seite haben wir lokale Vektor- und Rasterdaten in QGIS geladen. In der Forschung und Planung müssen geeignete Geodaten jedoch häufig zunächst gefunden, bewertet und beschafft werden.

Geodaten werden unter anderem erhoben und veröffentlicht von:

* Vermessungs- und Katasterbehörden,
* Umwelt- und Naturschutzbehörden,
* statistischen Ämtern,
* Städten, Gemeinden und Landkreisen,
* Forschungseinrichtungen,
* internationalen Organisationen,
* Unternehmen sowie
* gemeinschaftlich getragenen Projekten wie OpenStreetMap.

Ein Datensatz ist nicht allein deshalb geeignet, weil er sich herunterladen oder in QGIS anzeigen lässt. Vor seiner Verwendung müssen Inhalt, räumliche Abdeckung, Aktualität, Qualität und Nutzungsbedingungen geprüft werden.

> **Merksatz:** Eine verlässliche Geodatenquelle liefert nicht nur Daten, sondern auch Informationen darüber, was die Daten bedeuten und wie sie entstanden sind.

## Geoportale und Open Data

Ein **Geoportal** ist ein Webangebot, über das räumliche Daten gesucht, betrachtet und teilweise heruntergeladen oder als Webdienst genutzt werden können. Geoportale bündeln häufig Daten verschiedener Behörden und Themenbereiche.

Typische Funktionen sind:

* Suche nach Themen, Orten oder Datensätzen,
* Vorschau in einer Webkarte,
* Anzeige von Metadaten,
* Download von Geodatendateien und
* Bereitstellung von Dienstadressen für GIS-Software.

**Open Data** bezeichnet Daten, die unter festgelegten offenen Bedingungen genutzt und weiterverwendet werden dürfen. „Im Internet sichtbar“ bedeutet jedoch nicht automatisch „frei verwendbar“. Prüfen Sie deshalb immer Lizenz, Quellenangabe und mögliche Einschränkungen.

<!-- Vor Veröffentlichung konkrete Geoportale ergänzen, beispielsweise Geoportal Hessen, BKG, BfN oder kommunale Portale. -->

## Metadaten prüfen

**Metadaten** sind Daten über Daten. Sie helfen zu beurteilen, ob ein Datensatz zur eigenen Fragestellung passt und korrekt interpretiert werden kann.

Prüfen Sie möglichst mindestens folgende Angaben:

| Frage | benötigte Metadaten |
|---|---|
| Was wird dargestellt? | Titel, Beschreibung, Variablen und Klassen |
| Wer ist verantwortlich? | herausgebende Stelle und Kontakt |
| Welches Gebiet wird abgedeckt? | räumliche Ausdehnung |
| Aus welchem Zeitraum stammen die Daten? | Erhebungsdatum und Aktualität |
| Wie detailliert sind die Daten? | Maßstab, Lagegenauigkeit oder Rasterauflösung |
| Wie sind die Daten räumlich referenziert? | CRS und EPSG-Code |
| Wie wurden die Daten erzeugt? | Erhebungs- und Verarbeitungsmethode |
| Darf ich die Daten verwenden? | Lizenz und Bedingungen der Quellenangabe |
| Wie kann ich sie beziehen? | Downloadformat oder Webdienst |

> **Wichtig:** Speichern Sie Metadaten und Quellenangaben gemeinsam mit den verwendeten Daten. Ein nicht mehr nachvollziehbarer Datensatz verliert einen großen Teil seines wissenschaftlichen Wertes.

## Download oder Webdienst?

Geodaten können auf unterschiedliche Weise bereitgestellt werden.

### Download

Bei einem **Download** wird eine Kopie des Datensatzes lokal gespeichert. Sie kann anschließend unabhängig vom Webangebot in QGIS geöffnet und – abhängig von Format und Lizenz – analysiert oder bearbeitet werden.

Vorteile:

* Daten bleiben für den dokumentierten Arbeitsstand verfügbar,
* Verarbeitung ist auch ohne Internetverbindung möglich,
* umfangreiche Analysen sind meist einfacher und
* die verwendete Version kann archiviert werden.

Nachteile:

* Dateien benötigen lokalen Speicherplatz,
* Aktualisierungen müssen selbst beschafft werden und
* große Datensätze können lange Lade- und Downloadzeiten verursachen.

### Webdienst

Bei einem **Webdienst** fragt QGIS Daten oder Kartenansichten über das Internet direkt von einem Server ab. Es wird nicht zwingend eine vollständige lokale Kopie gespeichert.

Vorteile:

* Daten werden zentral bereitgestellt,
* aktuelle Inhalte können ohne erneuten manuellen Download erscheinen und
* große Datenbestände lassen sich zunächst betrachten, ohne sie vollständig herunterzuladen.

Nachteile:

* eine Internetverbindung ist erforderlich,
* Verfügbarkeit und Geschwindigkeit hängen vom Server ab,
* Funktionen können eingeschränkt sein und
* Änderungen des Dienstes können die Reproduzierbarkeit beeinträchtigen.

## WMS: eine Karte als Dienst

Ein **Web Map Service**, kurz **WMS**, liefert auf Anfrage gerenderte Kartenbilder. QGIS übermittelt unter anderem den gewünschten Kartenausschnitt, die Bildgröße und das CRS. Der Server erzeugt daraus eine passende Kartenansicht.

Ein WMS eignet sich besonders:

* als Hintergrundkarte,
* zur visuellen Orientierung,
* zur Vorschau auf verfügbare Themen und
* zum Überlagern eigener Daten mit amtlichen Karteninhalten.

Ein WMS liefert normalerweise nicht die vollständigen zugrunde liegenden Vektorobjekte oder Rasterwerte. Daher können die dargestellten Features meist nicht wie ein lokaler Vektorlayer bearbeitet oder frei analysiert werden. Manche Dienste erlauben über eine Objektabfrage dennoch den Abruf begrenzter Sachinformationen für einen angeklickten Ort.

> **Merksatz:** Ein WMS liefert in erster Linie eine fertige Kartenansicht – nicht den vollständigen ursprünglichen Geodatensatz.

## WFS: Vektorobjekte als Dienst

Ein **Web Feature Service**, kurz **WFS**, stellt Vektorfeatures mit Geometrien und Attributen bereit. Anders als bei einem WMS erhält QGIS nicht nur ein Kartenbild, sondern räumliche Objekte, die – abhängig vom Dienst – abgefragt, gefiltert und analysiert werden können.

| Merkmal | WMS | WFS |
|---|---|---|
| überträgt vor allem | Kartenbild | Vektorfeatures |
| Geometrien und Attribute frei verfügbar | normalerweise nein | grundsätzlich ja |
| Darstellung | weitgehend vom Server vorgegeben | in QGIS veränderbar |
| typische Nutzung | Orientierung und Hintergrund | Abfrage und Analyse von Vektordaten |
| Datenmenge | oft vergleichsweise klein pro Bild | kann bei vielen Features groß werden |

WFS wird in dieser Unit nur zur Abgrenzung eingeführt. Der praktische Schwerpunkt liegt zunächst auf WMS.

<!-- WMTS und WCS nur ergänzen, wenn sie im weiteren Kurs tatsächlich verwendet werden. -->

## Dienstadresse und Portalseite unterscheiden

Für die Verbindung in QGIS benötigen Sie die **Dienstadresse** des WMS. Das ist nicht immer dieselbe URL wie die sichtbare Seite des Geoportals.

Eine Portalseite ist für Menschen gestaltet und enthält Suche, Beschreibung und Vorschau. Die Dienstadresse ist ein technischer Endpunkt, über den QGIS standardisierte Anfragen an den Server sendet.

Geoportale kennzeichnen diese Adresse beispielsweise als:

* WMS-Adresse,
* Dienst-URL,
* GetCapabilities-URL oder
* Schnittstelle.

Kopieren Sie die angegebene Dienstadresse möglichst direkt aus den Metadaten. Versuchen Sie nicht, sie aus der Adresse der Webkarte zu erraten.

## Einen WMS in QGIS einbinden

Für die Übung wird folgende Verbindung verwendet:

| Angabe | Wert |
|---|---|
| Name der Verbindung | `[Name ergänzen]` |
| WMS-Dienstadresse | `[URL ergänzen]` |
| auszuwählender Layer | `[Layername ergänzen]` |

### 1. Datenquellenmanager öffnen

Öffnen Sie in QGIS den **Datenquellenmanager** und wählen Sie den Bereich **WMS/WMTS**.

### 2. Verbindung anlegen

1. Erstellen Sie eine neue Verbindung.
2. Tragen Sie einen eindeutigen Namen ein.
3. Fügen Sie die bereitgestellte Dienstadresse ein.
4. Speichern Sie die Verbindung.

Für frei zugängliche Dienste sind normalerweise keine Zugangsdaten nötig. Verwenden Sie Anmeldedaten nur, wenn der Anbieter dies ausdrücklich vorsieht.

### 3. Verbindung herstellen

Wählen Sie die gespeicherte Verbindung und stellen Sie die Verbindung zum Server her. QGIS ruft die vom Dienst angebotenen Informationen ab und zeigt die verfügbaren Layer an.

Prüfen Sie:

* Titel und Beschreibung der Layer,
* mögliche Unterlayer,
* angebotene Bildformate,
* verfügbare Koordinatenreferenzsysteme und
* gegebenenfalls verfügbare Stile.

### 4. Layer hinzufügen

1. Wählen Sie den vorgesehenen WMS-Layer aus.
2. Fügen Sie ihn dem Projekt hinzu.
3. Schließen Sie den Datenquellenmanager.
4. Verschieben Sie den WMS im Layer-Bereich an eine sinnvolle Position.
5. Zoomen Sie auf Ihr Untersuchungsgebiet.

Ein flächendeckender WMS liegt meist unter eigenen Punkt-, Linien- und Polygonlayern, damit diese sichtbar bleiben.

## Den WMS untersuchen

Beantworten Sie nach dem Laden des Dienstes folgende Fragen:

* Für welches Gebiet stellt der Dienst Karten bereit?
* Welche Themen oder Layer sind verfügbar?
* Welche herausgebende Stelle wird genannt?
* Welche CRS unterstützt der ausgewählte Layer?
* Ändert sich der sichtbare Detailgrad beim Hineinzoomen?
* Lassen sich Objektinformationen abfragen?
* Kann eine gewöhnliche Attributtabelle geöffnet werden?
* Ist die Darstellung in QGIS frei symbolisierbar oder vom Server vorgegeben?

Notieren Sie die Dienstadresse und die wichtigsten Metadaten. Der bloße Name im Layer-Bereich reicht für eine spätere Reproduktion nicht aus.

## Lokale Daten und WMS kombinieren

Laden Sie zusätzlich einen lokalen Vektorlayer aus der vorherigen Übung und legen Sie ihn über den WMS.

Prüfen Sie:

1. Liegen beide Layer räumlich korrekt übereinander?
2. Besitzen Layer und Projekt dasselbe CRS?
3. Falls nicht: Kann QGIS beide dennoch korrekt gemeinsam darstellen?
4. Welche Information stammt aus der lokalen Datei und welche vom WMS?
5. Welche Quelle wäre für eine räumliche Analyse geeignet und welche nur zur visuellen Orientierung?

Damit wird sichtbar, dass ein QGIS-Projekt gleichzeitig Daten aus sehr unterschiedlichen Quellen verwenden kann. Diese Quellen bleiben dennoch fachlich und technisch verschieden.

## Typische Probleme

| Problem | mögliche Ursache | erster Prüfschritt |
|---|---|---|
| Verbindung schlägt fehl | Portalseite statt Dienstadresse verwendet | WMS-URL in den Metadaten prüfen |
| keine Layer werden aufgelistet | Server nicht erreichbar oder URL fehlerhaft | URL und Internetverbindung prüfen |
| WMS bleibt leer | Ausschnitt oder Maßstab ungeeignet | auf Untersuchungsgebiet zoomen |
| Layer liegen nicht übereinander | CRS-Information fehlt oder ist ungeeignet | Layer- und Projekt-CRS prüfen |
| Darstellung lädt sehr langsam | Server oder Verbindung ist ausgelastet | kleineren Ausschnitt wählen und erneut laden |
| Attributtabelle fehlt | WMS liefert ein Kartenbild | WFS oder Downloadmöglichkeit suchen |
| gewünschte Analyse ist nicht möglich | zugrunde liegende Daten fehlen | geeigneten Download oder Datendienst suchen |

## Datenquellen dokumentieren

Für jeden verwendeten Datensatz oder Dienst sollten mindestens folgende Angaben gespeichert werden:

* vollständiger Titel,
* herausgebende Stelle,
* URL der Portalseite beziehungsweise des Dienstes,
* Zugriffs- oder Downloaddatum,
* Datenstand oder Aktualisierungsdatum,
* räumliche Abdeckung und Auflösung beziehungsweise Maßstab,
* CRS,
* Lizenz und geforderte Quellenangabe sowie
* verwendeter Layer oder verwendete Datei.

Diese Informationen gehören zur wissenschaftlichen Dokumentation und werden später für Metadaten, Methodenbeschreibung und Quellenangaben benötigt.

## Kurze Übung

1. Öffnen Sie das in der Lehrveranstaltung ausgewählte Geoportal.
2. Suchen Sie dort nach dem vorgegebenen Thema.
3. Finden Sie die Metadatenseite und die WMS-Dienstadresse.
4. Legen Sie die Verbindung in QGIS an.
5. Laden Sie den vorgesehenen WMS-Layer.
6. Kombinieren Sie ihn mit einem lokalen Vektorlayer.
7. Dokumentieren Sie Quelle, Layername, URL, CRS, Lizenz und Zugriffsdatum.
8. Erklären Sie in zwei Sätzen, warum der WMS für die Darstellung geeignet ist, für eine weitergehende Vektoranalyse aber möglicherweise nicht ausreicht.

<!-- Konkretes Geoportal, Suchbegriff, Dienst und lokaler Vergleichslayer vor Veröffentlichung ergänzen. -->

## Zusammenfassung

* Geodaten stammen von vielen unterschiedlichen öffentlichen, wissenschaftlichen und privaten Stellen.
* Geoportale helfen beim Suchen, Betrachten und Beziehen räumlicher Daten.
* Metadaten sind notwendig, um Eignung, Qualität, Aktualität und Nutzungsbedingungen zu beurteilen.
* Ein Download erzeugt eine lokale Kopie; ein Webdienst stellt Inhalte über das Internet bereit.
* Ein WMS liefert vor allem gerenderte Kartenbilder.
* Ein WFS stellt Vektorfeatures mit Geometrien und Attributen bereit.
* Für QGIS wird die technische Dienstadresse benötigt, nicht lediglich die Adresse einer Portalseite.
* Datenquelle, Layer, CRS, Lizenz und Zugriffsdatum müssen nachvollziehbar dokumentiert werden.

## Weiterführende Informationen

* [QGIS: WMS/WMTS Client](https://docs.qgis.org/latest/en/docs/user_manual/working_with_ogc/ogc_client_support.html#wms-wmts-client)
* [QGIS-Übung zu Web Map Services](https://docs.qgis.org/latest/en/docs/training_manual/online_resources/wms.html)
* [QGIS-Übung zu Web Feature Services](https://docs.qgis.org/latest/en/docs/training_manual/online_resources/wfs.html)

<!-- Notizen: Ab hier folgen Vermerke, welche als Gedankenstütze oder Erinnerung dienen, aber noch nicht in der vorhandenen Form veröffentlicht werden sollen. -->

<!--
Didaktische Hinweise:
- Mit einem realen, frei zugänglichen und erfahrungsgemäß stabilen WMS arbeiten.
- Dienstadresse bereits bereithalten, Studierende aber zusätzlich im Geoportal danach suchen lassen.
- WMS bewusst mit einem lokalen Vektorlayer vergleichen.
- WFS nur konzeptionell abgrenzen; praktische Vertiefung kann später folgen.

Vor Veröffentlichung ergänzen:
- Geoportal und Suchbegriff
- WMS-Verbindungsname und URL
- auszuwählender Layer
- lokaler Vergleichslayer
- erwartete Lizenz- und Quellenangabe
- alternative Dienstadresse für den Fall eines Ausfalls

Anschluss an unit10-04_assignment.md:
- QGIS-Projekt selbstständig strukturieren, lokale Daten laden, einen WMS ergänzen und die Quellen dokumentieren.
-->