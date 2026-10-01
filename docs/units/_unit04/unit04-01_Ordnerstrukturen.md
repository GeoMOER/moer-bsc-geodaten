---
title: Ordner- und Projektstrukturen
published: true
toc: true
header:
  image: /assets/images/unit02/31031723265_0890cd9547_o.jpg
  image_description: "Cloudscape Over the Philippine Sea"
  caption: "Image: [NASA's Marshall Space Flight Center](https://www.nasa.gov/centers/marshall/home/index.html) [CC BY-NC 2.0] via [flickr.com](https://www.flickr.com/photos/nasamarshall/31031723265/)"
---

<!-- Kapitel 04-01: Ordnerstrukturen, Dateibenennung, Dateipfade -->

Sie haben in den letzten Kapiteln gelernt, wie Sie einzelne Dateien sauber formatieren, exportieren und importieren. Doch spätestens wenn Sie über mehrere Wochen hinweg Messdaten sammeln, Zwischenstände speichern und mit anderen austauschen, entsteht ein neues Problem: **Wo liegt eigentlich was, und welche Version ist die aktuelle?** Eine einzelne unsauber formatierte Zelle lässt sich meist noch reparieren – ein Datensatz, der in zwanzig verschieden benannten Dateien über drei Ordner verteilt ist, kostet dagegen im Zweifel Stunden, ihn wieder zusammenzusetzen. Dieses Kapitel behandelt deshalb, wie Sie Dateien von Anfang an so organisieren, dass genau das nicht passiert.

## Themenüberschrift 01: Warum Ordnung essentiell ist

Stellen Sie sich vor, Sie erhalten für ein Projekt Daten von drei Kommiliton:innen sowie zwei eigene Zwischenstände Ihrer Analyse. Ohne klare Struktur landen typischerweise Dateien wie diese in einem einzigen Ordner:

```
Daten.xlsx
Daten (1).xlsx
Daten_neu.xlsx
Daten_neu2.xlsx
Kopie von Daten_final.xlsx
Daten_final_FINAL.xlsx
Daten_final_FINAL_wirklich.xlsx
```


- **Welche Datei ist die aktuelle?** Ohne die Dateien zu öffnen, ist das nicht erkennbar.
- **Welche Datei stammt von wem?** Der Dateiname verrät nichts über Herkunft oder Bearbeitungsstand.
- **Was passiert, wenn zwei Personen gleichzeitig „Daten.xlsx" bearbeiten** und beide Versionen später zusammengeführt werden müssen?

Das ist kein hypothetisches Problem: Fehlerhafte Datenanalysen aufgrund verwechselter Dateiversionen sind einer der häufigsten und am leichtesten vermeidbaren Fehler in Projekt- und Forschungsarbeiten. Eine konsistente Ordner- und Namensstruktur kostet zu Beginn ein paar Minuten mehr Aufwand – sie erspart Ihnen aber, im Zweifel eine ganze Analyse noch einmal neu zu machen, weil unklar ist, mit welchem Datenstand Sie eigentlich gearbeitet haben. 

## Themenüberschrift 02: Namensregeln für Dateien

Ein guter Dateiname beantwortet auf einen Blick: **Was ist das, von wem, wann, welche Version?** Ein bewährtes Schema, das Sie bereits aus der Export-Übung kennen:

```
NAME_INHALT_DATUM_VERSION.ENDUNG
```


Beispiel: `Mueller_Klimadaten_20250316_v2.xlsx`

**Konkrete Empfehlungen:**

| Regel | Begründung | Beispiel |
|---|---|---|
| Datum im Format `JJJJMMTT` verwenden | Dateien sortieren sich dadurch automatisch chronologisch im Ordner | `20250316` statt `16.03.2025` |
| Keine Leerzeichen im Dateinamen | Leerzeichen verursachen bei manchen Programmen/Servern/URLs Probleme | `Klimadaten_Marburg` statt `Klimadaten Marburg` |
| Keine Umlaute, Sonderzeichen (`ä`, `ö`, `ü`, `ß`, `/`, `#`, `&`, `%`) | Können bei Übertragung zwischen Betriebssystemen zu Fehlern oder Encoding-Problemen führen | `Groesse` statt `Größe` |
| Versionsnummer statt „final", „neu", „aktuell" | Wörter wie „final" verlieren ihre Bedeutung, sobald eine weitere Änderung nötig wird | `v1`, `v2`, `v3` statt `final`, `final_neu` |
| Konsistente Reihenfolge der Bestandteile | Erleichtert das Sortieren und Wiederfinden über viele Dateien hinweg | immer `Name_Inhalt_Datum_Version` |

<!-- Screenshot 18: Datei-Explorer-Fenster mit zwei Ordnern nebeneinander im Vergleich: links ein chaotischer Ordner mit Dateinamen wie `Daten_neu2_FINAL.xlsx`, rechts derselbe Datenbestand konsistent benannt nach dem Schema `Name_Inhalt_Datum_Version.xlsx`, dabei automatisch chronologisch sortiert.
Markdownlösung: ![Screenshot des Datei-Explorer-Fensters mit zwei Ordnern nebeneinander im Vergleich: rechts chaotisch benannte Dateien, links konsistent benannte Daten.]({{ '/assets/images/unit04/Screenshot18_Struktur.png' | relative_url }}) 
Oder als HTML (lightbox) mit Vergrößerungsoption, Beschreibungstext beim Hovern und Galerie zum durchklicken: -->

<a href="{{ '/assets/images/unit04/Screenshot18_Struktur.png' | relative_url }}" 
   data-lightbox="Screenshot18_Struktur" 
   title="Screenshot des Datei-Explorer-Fensters mit zwei Ordnern nebeneinander im Vergleich: rechts chaotisch benannte Dateien, links konsistent benannte Daten.">
  <img src="{{ '/assets/images/unit04/Screenshot18_Struktur.png' | relative_url }}" alt="Screenshot des Datei-Explorer-Fensters mit zwei Ordnern nebeneinander im Vergleich: rechts chaotisch benannte Dateien, links konsistent benannte Daten.">
</a>

## Themenüberschrift 03: Ordnerstrukturen

Neben dem Dateinamen selbst ist auch die **Ablage in Ordnern** entscheidend. Eine bewährte Grundstruktur für ein Datenprojekt:

```
Projektordner/
├── 01_Rohdaten/
├── 02_Bearbeitete_Daten/
├── 03_Analyse/
└── 04_Ergebnisse/
```


### Verbindliche Mindeststruktur

Unabhängig davon, wie Sie die übrigen Ordner benennen oder gliedern, sollte ein Ordner **nicht verhandelbar** sein:

- **`01_Rohdaten` (oder `Raw_Data`) ist Pflicht.** Hier landet ausschließlich das, was Sie ursprünglich erhoben oder erhalten haben – unverändert, so wie es hereinkam (auch wenn es unsauber formatiert oder fehlerhaft ist). Dieser Ordner wird **nie** überschrieben oder direkt bearbeitet. Jede Weiterverarbeitung erfolgt in einer Kopie in einem anderen Ordner. Der Grund: Sobald Sie an Rohdaten etwas verändert haben, können Sie im Nachhinein nicht mehr nachvollziehen, ob ein auffälliger Wert ein Original-Messfehler war oder erst durch Ihre eigene Bearbeitung entstanden ist

Alle weiteren Ordner (z.B. bearbeitete Daten, Analyse, Ergebnisse, Dokumentation) sind in Benennung und Anzahl flexibler an Ihr Projekt anpassbar – ein Rohdaten-Ordner mit diesem Prinzip dagegen sollte in jedem Datenprojekt vorhanden sein, das Sie im Studium oder danach anlegen.
rt.

- **Konsistenz über das ganze Projekt/Semester hinweg** ist wichtiger als die „perfekte" Struktur – wählen Sie ein Schema und behalten Sie es bei, statt es von Projekt zu Projekt neu zu erfinden.

- **Nummerierte Ordner** (`01_`, `02_`, …) sorgen dafür, dass die Ordner in der sinnvollen Reihenfolge angezeigt werden, statt alphabetisch durcheinander.

### Wie tief sollte die Ordnerstruktur sein - also wie viele Unterordner sollte man anlegen?

Eine gängige Faustregel: **maximal 3–4 Ordnerebenen** unterhalb des Projektordners, bevor eine Datei liegt.

```
Projektordner
  |- 01_Rohdaten
      |- Klimadaten_Giessen
      |- Klimadaten_Marburg
          |-2025
          |-2026
            |- Klimadaten_20260301-20260331_v0.xlsx
            |- Klimadaten_20260401-20260430_v0.xlsx


**Warum eine Obergrenze sinnvoll ist:**
- **Kognitive Überlastung:** Ab etwa 4–5 Ebenen verlieren die meisten Menschen den Überblick, wo sich eine bestimmte Datei befindet, ohne die Ordnerstruktur aktiv zu durchsuchen
- **Technische Pfadlängen-Begrenzung (Windows):** Windows begrenzt den vollständigen Pfad (Laufwerk + alle Ordner + Dateiname) historisch auf 260 Zeichen. Bei tief verschachtelten Ordnern mit langen, sprechenden Namen wird dieses Limit überraschend schnell erreicht – die Folge sind Dateien, die sich nicht mehr öffnen, verschieben oder manchmal nicht einmal löschen lassen
- **Cloud-Synchronisation:** Dienste wie OneDrive, Google Drive oder Dropbox synchronisieren tief verschachtelte, stark verzweigte Ordnerstrukturen spürbar langsamer und fehleranfälliger als flache Strukturen

## Dateipfade

Ein **Dateipfad** beschreibt, wo genau eine Datei im Dateisystem liegt – vergleichbar mit einer Adresse.

- **Absoluter Pfad:** beschreibt den vollständigen Weg vom obersten Verzeichnis aus, z. B. `C:\Nutzer\Mueller\Dokumente\Projekt\01_Rohdaten\Klimadaten.xlsx` (Windows) oder `/Users/Mueller/Dokumente/Projekt/01_Rohdaten/Klimadaten.xlsx` (Mac)
- **Relativer Pfad:** beschreibt den Weg ausgehend vom aktuellen Ordner, z. B. `01_Rohdaten/Klimadaten.xlsx`, wenn Sie sich bereits im Projektordner befinden

**Warum das relevant ist:** Wenn Sie später mit anderer Software arbeiten (z. B. R, QGIS), die auf Ihre Excel- oder CSV-Dateien zugreifen soll, müssen Sie den korrekten Pfad angeben. Ein Pfad, der auf Ihrem Rechner funktioniert, kann bei einer anderen Person mit anderer Ordnerstruktur ins Leere laufen – ein klassischer Fallstrick beim Datenaustausch. **Relative Pfade** innerhalb eines gemeinsam geteilten Projektordners sind deshalb meist robuster als absolute Pfade, da sie nicht vom individuellen Nutzernamen oder Laufwerksbuchstaben abhängen.

**Weitere Stolperfallen bei Pfaden:**
- Leerzeichen und Umlaute in **Ordnernamen** verursachen dieselben Probleme wie in Dateinamen – auch hier gilt: vermeiden
- Windows verwendet `\` als Trennzeichen zwischen Ordnern, Mac/Linux verwenden `/` – die meisten aktuellen Programme kommen mit beidem zurecht, aber nicht ausnahmslos alle
- Ein zu tief verschachtelter Ordnerpfad (viele Unterordner ineinander) kann unter Windows an eine Zeichenlängen-Begrenzung stoßen und die Datei dann nicht mehr auffindbar sein (siehe oben)

### Wie Sie den Pfad einer Datei herausfinden

- **Windows:** Datei mit `Shift` + Rechtsklick anklicken → „Als Pfad kopieren" – oder in der Adressleiste des Explorers oben auf den Ordnerpfad klicken, er wird dann als Text angezeigt
- **Mac:** Datei im Finder markieren, `Cmd` + `Option` (Alt) gedrückt halten, im Menü „Ablage" erscheint dann „[Dateiname] als Pfadname kopieren"
- **In Excel selbst:** Über `Datei → Informationen` wird der vollständige Speicherort der aktuell geöffneten Datei angezeigt

<!-- **Screenshot 15:** Windows-Explorer mit Rechtsklick-Kontextmenü auf eine Datei, in dem die Option „Als Pfad kopieren" sichtbar/hervorgehoben ist, sowie zum Vergleich die Adressleiste des Explorers, in der derselbe Pfad als klickbarer Text angezeigt wird. -->

**Praxistipp:** Wenn Sie eine Datei später in R oder QGIS einlesen möchten und der Pfad nicht funktioniert, prüfen Sie zuerst: Enthält der Pfad Leerzeichen oder Umlaute? Ist er über eine Cloud-Synchronisation (OneDrive etc.) eingebunden, wodurch sich der tatsächliche Pfad von dem unterscheiden kann, der im Explorer angezeigt wird? Diese beiden Ursachen erklären einen Großteil aller „Datei nicht gefunden"-Fehler beim Programmstart mit externen Dateien.