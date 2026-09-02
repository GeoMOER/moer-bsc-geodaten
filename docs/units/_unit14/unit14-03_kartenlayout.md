---
title: Eine Karte erstellen
published: true
toc: true
header:
  image: /assets/images/unit14/hero-unit14.jpg
  image_description: "Workflow von der Fragestellung zur dokumentierten Karte"
  caption: "Eigene Darstellung"
---

<!-- Introtext: Von der QGIS-Kartenansicht zum zielgerichteten, exportierbaren Kartenlayout. -->

## Kartenansicht und Kartenlayout

![Ein vollständiger Kartenworkflow verbindet Fragestellung, Datenprüfung, Analyse, Gestaltung, Export und Interpretation.]({{ '/assets/images/unit14/karten-workflow.svg' | relative_url }})

In der QGIS-Kartenansicht untersuchen und bearbeiten wir Layer. Für ein fertiges Kartenprodukt benötigen wir zusätzlich ein **Kartenlayout**.

Das Layout legt unter anderem fest:

* Seitenformat und Ausrichtung,
* Größe und Ausschnitt der Karte,
* Titel und erläuternde Texte,
* Legende,
* Maßstabsangabe,
* Quellen und Urheberschaft sowie
* Exportformat und Auflösung.

Eine gute Karte ist nicht die Kartenansicht mit möglichst vielen zusätzlichen Elementen. Sie ist eine gezielt gestaltete Antwort auf eine Frage.

## Zweck und Zielgruppe festlegen

Bevor Sie ein Layout anlegen, beantworten Sie:

1. Welche Frage soll die Karte beantworten?
2. Für wen ist die Karte bestimmt?
3. Welche Vorkenntnisse besitzt die Zielgruppe?
4. Wo wird die Karte verwendet – Bildschirm, Bericht, Poster oder Präsentation?
5. Welche Informationen sind dafür unbedingt notwendig?

Unsere Beispielkarte richtet sich an fachlich interessierte Personen ohne detaillierte Kenntnis des Datensatzes. Sie soll zeigen:

> **Wo liegen die dokumentierten Beobachtungen, und welchen Höhenklassen sind sie zugeordnet?**

## Karteninhalt vorbereiten

Bereiten Sie die Kartenansicht vor dem Layout vor:

* nur benötigte Layer sichtbar,
* eindeutige Layernamen,
* passende Symbolisierung,
* begründete Klassifizierung,
* geeignete Layerreihenfolge,
* sinnvolle Beschriftungen,
* gewünschter Kartenausschnitt und
* korrektes Projekt-CRS.

Unnötige Layer sollten nicht allein deshalb sichtbar bleiben, weil sie im Projekt vorhanden sind.

## Neues Drucklayout anlegen

1. Öffnen Sie **Projekt → Neues Drucklayout**.
2. Geben Sie einen eindeutigen Namen ein, beispielsweise `abschlusskarte_unit14`.
3. Wählen Sie in den Seiteneigenschaften das vorgegebene Format, zum Beispiel A4.
4. Entscheiden Sie zwischen Hoch- und Querformat passend zur Form des Untersuchungsgebiets.
5. Speichern Sie das QGIS-Projekt.

Das Drucklayout ist Bestandteil des QGIS-Projekts. Ein Projekt kann mehrere Layouts enthalten.

## Kartenelement hinzufügen

1. Wählen Sie **Karte hinzufügen**.
2. Ziehen Sie auf der Seite einen Rahmen für das Kartenelement auf.
3. Passen Sie Ausschnitt und Maßstab innerhalb dieses Elements an.
4. Prüfen Sie, ob das gesamte relevante Untersuchungsgebiet sichtbar ist.
5. Lassen Sie ausreichend Platz für Titel, Legende und Quellenangaben.

Das Kartenelement zeigt einen Ausschnitt des QGIS-Projekts. Änderungen an Layern oder Symbolisierung können sich deshalb im Layout aktualisieren.

Wenn das Layout weitgehend fertig ist, können Layer und Stile für das Kartenelement gesperrt werden. Prüfen Sie anschließend trotzdem, ob spätere Änderungen bewusst übernommen werden sollen.

## Kartenausschnitt und Maßstab

Der Ausschnitt entscheidet, was Teil der Aussage ist.

Ein guter Ausschnitt:

* zeigt alle für die Frage relevanten Daten,
* vermeidet große informationsleere Flächen,
* bietet ausreichend räumlichen Kontext und
* passt zum Seitenformat.

Je kleiner der Kartenmaßstab, desto größer ist das dargestellte Gebiet und desto weniger Details bleiben erkennbar. Symbole und Beschriftungen müssen deshalb bei der endgültigen Layoutgröße geprüft werden.

## Titel

Der Titel soll die wichtigste Aussage oder Frage der Karte benennen.

Wenig aussagekräftig:

> Karte Unit 14

Aussagekräftiger:

> Dokumentierte Feuersalamander-Beobachtungen nach Höhenlage im Raum Marburg

Ein Untertitel kann Zeitraum, Datenstand oder Untersuchungsgebiet ergänzen. Titel und Untertitel dürfen jedoch nicht mehr versprechen, als die Daten tatsächlich zeigen.

Vermeiden Sie deshalb Formulierungen wie **„Verbreitung der Art“**, wenn lediglich dokumentierte Beobachtungen dargestellt werden.

## Legende

Die Legende erklärt Symbole, Farben und Klassen. Sie sollte nur Inhalte enthalten, die zum Verständnis der Karte benötigt werden.

Überarbeiten Sie automatisch erzeugte Legenden:

* technische Dateinamen durch fachliche Begriffe ersetzen,
* nicht sichtbare oder selbsterklärende Layer entfernen,
* Einheiten ergänzen,
* Klassengrenzen verständlich runden,
* Reihenfolge an die Kartenlogik anpassen und
* unnötige Überschriften vermeiden.

Beispiel:

```text
Beobachtungen nach Geländehöhe
  150 bis unter 250 m
  250 bis unter 350 m
  350 bis unter 450 m
  ab 450 m
```

Die Legende soll die tatsächliche Symbolisierung exakt wiedergeben.

## Maßstab

Ein grafischer **Maßstabsbalken** ermöglicht das Abschätzen von Entfernungen. Er ist mit einem bestimmten Kartenelement verknüpft und passt sich dessen Maßstab an.

Prüfen Sie:

* passende Einheit, zum Beispiel Kilometer,
* leicht lesbare Segmentwerte,
* ausreichenden Kontrast,
* angemessene Größe und
* korrekte Verknüpfung mit dem Kartenelement.

Eine numerische Maßstabsangabe wie `1 : 100.000` ist bei unveränderter Ausgabegröße hilfreich, kann aber durch nachträgliches Skalieren der Karte ungültig werden. Ein grafischer Maßstab wird gemeinsam mit der Karte skaliert.

## Nordpfeil

Ein Nordpfeil zeigt die Orientierung der Karte. Er ist sinnvoll, wenn:

* die Karte gedreht wurde,
* Norden nicht offensichtlich oben liegt,
* die Zielgruppe Orientierungshilfe benötigt oder
* das Kartenprodukt dies ausdrücklich verlangt.

Bei einer kleinen, ungedrehten Standardkarte mit Norden oben kann ein Nordpfeil redundant sein. Er ist kein automatisches Qualitätsmerkmal.

Wenn Sie ihn verwenden:

* verknüpfen Sie ihn mit dem richtigen Kartenelement,
* wählen Sie eine schlichte Form,
* stellen Sie ihn nicht größer als die Hauptinformation dar und
* prüfen Sie die korrekte Orientierung.

## Quellenangabe und Urheberschaft

Eine Karte muss erkennen lassen, woher ihre Daten stammen.

Nennen Sie mindestens:

* Datenquelle beziehungsweise Herausgeber,
* Datenstand, soweit relevant,
* Lizenz oder vorgeschriebene Namensnennung,
* Hintergrundkartendienst, falls verwendet,
* eigene Bearbeitung,
* Erstellungsdatum und
* Autorin oder Autor, wenn gefordert.

Beispielstruktur:

```text
Daten: GBIF.org ([Download-Datum]); DGM: [Herausgeber, Datenstand];
Schutzgebiete: [Herausgeber, Datenstand].
Bearbeitung: [Name], [Datum].
```

Übernehmen Sie die konkrete Zitierempfehlung und Lizenzangabe aus den Metadaten. Eine bloße Angabe wie „Quelle: Internet“ ist nicht ausreichend.

## CRS und Projektion angeben

Das verwendete CRS kann in der Quellen- oder Methodenangabe genannt werden, besonders wenn:

* räumliche Messungen dargestellt werden,
* mehrere Karten verglichen werden,
* eine fachliche Dokumentation gefordert ist oder
* die Projektion die sichtbare Form deutlich beeinflusst.

Ein EPSG-Code allein ist für viele Zielgruppen wenig verständlich. Kombinieren Sie ihn gegebenenfalls mit dem Namen des Koordinatenreferenzsystems.

## Koordinatengitter und Übersichtskarte

Ein Koordinatengitter oder eine zusätzliche Übersichtskarte kann die Orientierung verbessern. Beide Elemente benötigen jedoch Platz und erhöhen die Komplexität.

Verwenden Sie sie nur, wenn sie eine konkrete Frage beantworten:

* Wo liegt das Untersuchungsgebiet in Hessen oder Deutschland?
* Welche Koordinaten besitzt ein Kartenbereich?
* Muss eine Position ohne weitere Software bestimmbar sein?

Für eine einfache Abschlusskarte sind diese Elemente optional.

## Visuelle Hierarchie im Layout

Nicht nur die Layer, sondern auch die Layoutelemente benötigen eine Hierarchie.

Eine mögliche Reihenfolge der Aufmerksamkeit:

1. Karte und Hauptthema,
2. Titel,
3. Legende,
4. räumliche Orientierung,
5. Quellen- und Methodenangaben.

Hilfreich sind:

* ausreichend Weißraum,
* klare Ausrichtung von Elementen,
* wenige Schriftgrößen,
* einheitliche Schriftfamilie,
* zurückhaltende Rahmen und
* kurze Texte.

Ein Element sollte nicht allein durch Schatten, Rahmen oder kräftige Farbe hervorgehoben werden, wenn es fachlich unwichtig ist.

## Lesbarkeit prüfen

Betrachten Sie die Karte in ihrer tatsächlichen Ausgabegröße.

Prüfen Sie:

* Sind Titel und Legende ohne Vergrößerung lesbar?
* Lassen sich alle Symbolklassen unterscheiden?
* Sind Punkte oder Linien zu klein?
* Verdecken sich Beschriftungen?
* Ist der Hintergrund zu dominant?
* Bleiben wichtige Unterschiede in Graustufen oder bei eingeschränktem Farbsehen erkennbar?
* Sind Einheiten und Quellen vollständig?

Bitten Sie nach Möglichkeit eine andere Person, die Kernaussage der Karte ohne zusätzliche Erklärung zu beschreiben.

## Export

QGIS kann Layouts unter anderem als PDF, SVG oder Bilddatei exportieren.

### PDF

Geeignet für:

* Berichte,
* Druck,
* Weitergabe eines vollständigen Kartenprodukts.

Vektorelemente können dabei scharf skalierbar bleiben, sofern sie nicht als Raster ausgegeben werden.

### PNG

Geeignet für:

* Präsentationen,
* Webseiten,
* schnelle Vorschau.

Für eine druckfähige Abgabe kann beispielsweise eine Auflösung von **300 dpi** sinnvoll sein. Für reine Bildschirmdarstellung genügt häufig weniger. Beachten Sie die konkrete Aufgabenstellung.

Exportieren Sie die Abschlusskarte beispielsweise als:

```text
figures/abschlusskarte_unit14.pdf
figures/abschlusskarte_unit14.png
```

Öffnen und prüfen Sie beide exportierten Dateien. Ein erfolgreicher Export bedeutet nicht automatisch, dass Schrift, Legende und Farben lesbar sind.

## Häufige Probleme

| Problem | Wirkung | Verbesserung |
|---|---|---|
| Titel benennt nur das Thema | Aussage bleibt unklar | räumliche Frage oder Inhalt konkret benennen |
| automatische Legende bleibt unverändert | Dateinamen und unnötige Layer sichtbar | Legende fachlich überarbeiten |
| zu viele Kartenelemente | Hauptkarte wird klein und unruhig | nur funktional notwendige Elemente verwenden |
| Nordpfeil dominiert | Dekoration konkurriert mit Daten | verkleinern oder weglassen |
| Maßstabsbalken mit ungeeigneter Einheit | schwer interpretierbare Werte | Kilometer oder Meter passend wählen |
| Quellen fehlen | Datenherkunft nicht nachvollziehbar | Quellen- und Lizenzangaben ergänzen |
| Schrift erst beim Zoomen lesbar | Karte funktioniert in Ausgabegröße nicht | tatsächliche Größe prüfen |
| Export wird nicht geöffnet | abgeschnittene oder fehlende Elemente bleiben unbemerkt | Exportdatei kontrollieren |

## Kurze Übung

Erstellen Sie ein A4-Layout mit:

* einem Kartenelement,
* einem aussagekräftigen Titel,
* einer überarbeiteten Legende,
* einem Maßstabsbalken,
* einer Quellenangabe und
* optional einem begründeten Nordpfeil.

Beantworten Sie anschließend:

1. Welche Information soll zuerst auffallen?
2. Welches Element haben Sie bewusst weggelassen?
3. Ist jede Legendenposition zum Verständnis nötig?
4. Sind Datenquelle, Einheit und Datenstand erkennbar?
5. Bleibt die Karte in der exportierten Größe lesbar?

## Zusammenfassung

* Das Drucklayout überführt die QGIS-Kartenansicht in ein fertiges Kartenprodukt.
* Zweck, Zielgruppe und Ausgabeformat bestimmen die Gestaltung.
* Titel und Legende müssen die tatsächliche fachliche Aussage verständlich benennen.
* Maßstabsbalken, Nordpfeil, Gitter und Übersichtskarte werden nach Funktion eingesetzt.
* Datenquellen, Lizenz und Bearbeitung müssen nachvollziehbar angegeben werden.
* Weißraum, Ausrichtung und visuelle Hierarchie verbessern die Lesbarkeit.
* PDF- und Bildexport müssen nach dem Erstellen in der endgültigen Größe geprüft werden.

## Weiterführende Informationen

* [QGIS-Dokumentation: Überblick über das Drucklayout](https://docs.qgis.org/latest/en/docs/user_manual/print_layout/overview_layout.html)
* [QGIS-Dokumentation: Legenden im Drucklayout](https://docs.qgis.org/latest/en/docs/user_manual/print_layout/layout_items/layout_legend.html)
* [QGIS-Dokumentation: Maßstabsbalken](https://docs.qgis.org/latest/en/docs/user_manual/print_layout/layout_items/layout_scale_bar.html)
* [QGIS-Dokumentation: Karten exportieren](https://docs.qgis.org/latest/en/docs/user_manual/print_layout/create_output.html)

<!-- Notizen: Ab hier folgen Vermerke, welche als Gedankenstütze oder Erinnerung dienen, aber noch nicht in der vorhandenen Form veröffentlicht werden sollen. -->

<!--
Mögliche Abbildungen:
- Kartenansicht und fertiges Drucklayout nebeneinander
- automatische und fachlich überarbeitete Legende
- überladenes und reduziertes Layout
- Beispiel für visuelle Hierarchie und Weißraum
- Exportkontrolle bei 100 Prozent Ansicht

Didaktisch wichtig:
- Kartenelemente nicht als starre Pflichtliste lehren.
- Legende immer aktiv überarbeiten lassen.
- Titel muss Beobachtungen statt vollständiger Artverbreitung benennen.
- Quellenangabe bereits im Template verbindlich vorsehen.
- Kartenexport im Unterricht tatsächlich öffnen und prüfen lassen.

TODO Lehrende vor Durchführung:
- Seitenformat, Ausrichtung und gewünschte Exportauflösung festlegen.
- verbindliche Quellenformulierung für die bereitgestellten Daten vorbereiten.
- Musterlayout mit finalen Layernamen und Klassen erstellen.
- prüfen, ob PDF, PNG oder beide Formate abgegeben werden sollen.
-->
