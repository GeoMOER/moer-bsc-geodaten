--- 
title: Software Grundlagen
published: true
toc: true
header:
  image: /assets/images/01-splash.jpg
  image_description: "Dr. John Snow's map"
  caption: "Map: [**Dr. John Snow**](https://en.wikipedia.org/wiki/John_Snow) [Wellcome Library via wikimedia](https://w.wiki/QtV)"
---

<!-- Themenblock 01-01: Binärsystem, Bits & Bytes / Grundlegende Kodierung (Text, Zahlen, Bilder) / Dateiformate als Strukturierungsprinzip -->

Um zu verstehen, wie ein Computer funktioniert, müssen wir zunächst verstehen, wie Informationen überhaupt transportiert werden können. Ein Computer kann nur zwischen hoher bzw. niedriger elektrische Spannung unterscheiden, oder - anders gesagt - zwischen Strom an (1) und Strom aus (0). Diesen Zustand nennt man ein *Bit* (kurz für Binary Digit, also „Binärziffer").  

## Codierung

Mit diesen zwei Zuständen lässt sich grundsätzlich jede Information darstellen – man muss sich nur vorher auf eine feste Zuordnung, einen Code, einigen.
Dieses Prinzip wurde bereits kurz nach der Entwicklung des ersten Telegraphen genutzt, welcher 1837 von Samuel Morse entwickelt wurde. 

Morses Telegraph bestand im Kern aus zwei Stationen, die über einen einzelnen Draht miteinander verbunden waren – Sender und Empfänger konnten dabei mehrere Kilometer voneinander entfernt sein.

Der Sender drückte  die sogenannte Morsetaste – im Grunde ein einfacher Schalter. wodurchder Stromkreis geschlossen wurde und Strom durch die Leitung floss; ließ man los, wurde der Kreis wieder unterbrochen. Je nachdem, wie lange die Taste gedrückt wurde, entstand ein kurzer oder ein langer elektrischer Impuls.
Diese Impulse liefen als Stromstöße durch den Draht zur Empfangsstation – mehr als „Strom an" oder „Strom aus" wurde dabei nicht übertragen.
Am anderen Ende saß ein Elektromagnet mit einem beweglichen Anker, an dem ein Schreibstift befestigt war. Kam ein Stromimpuls an, wurde der Anker vom Elektromagneten angezogen und drückte den Stift gegen einen Papierstreifen, der von einem Uhrwerk gleichmäßig weitergezogen wurde. Je nachdem, wie lange der Strom floss, entstand so ein kurzer Punkt oder ein längerer Strich auf dem Papier.

Damit beruhte schon dieser rund 100 Jahre vor dem Computer entwickelte Apparat auf genau demselben Grundprinzip: Es gibt nur zwei mögliche Zustände – Stromkreis geschlossen oder offen –, und erst eine vorher vereinbarte Zuordnung (welche Folge aus Punkten und Strichen welchen Buchstaben bedeutet) macht daraus lesbare Information. Morse hatte ursprünglich sogar vor, ganzen Wörtern aus einem Wörterbuch einfach durchnummerierte Zahlencodes zuzuordnen; erst gemeinsam mit seinem Mitarbeiter Alfred Vail entwickelte er das bekannte Alphabet aus kurzen und langen Signalen, das wir heute als Morsecode kennen.

<!-- copyright free Bild einfügen -->

SOS ist ein gutes Einstiegsbeispiel für "Codierung": ... --- ... – drei kurze, drei lange, drei kurze Signale. Es werden nur zwei Zustände gebraucht (kurz/lang, bzw. Ton an/aus). 
Zwar übersetzen sowohl der Morsecode als auch der Computer diese binären Zeichen in Zahlen bzw. Buchstaben, es gibt aber wichtige Unterschiede:

1. Im Morsecode entsteht die Information durch die Dauer eines Signals: kurz = Punkt, lang = Strich. Zusätzlich braucht es unterschiedlich lange Pausen, um einzelne Signale, Buchstaben und Wörter voneinander zu trennen – genau genommen kommt der Morsecode also nicht mit zwei, sondern mit mehreren unterscheidbaren Elementen aus (Punkt, Strich, kurze Pause, lange Pause). 
Ein Bit im Computer dagegen hat immer dieselbe, fest getaktete Dauer. Ob es eine 0 oder eine 1 ist, hängt nicht davon ab, wie lange ein Signal anliegt, sondern nur davon, welchen Spannungswert es in diesem festen Zeitschlitz hat (hohe oder niedrige Spannung)

2. Der Morsecode hat unterschiedlich lange Zeichen, Bit-Muster sind (meist) gleich lang. Morse hat die Codes bewusst nach Häufigkeit vergeben: Das im Englischen sehr häufige „E" bekommt nur ein einziges kurzes Signal (·), das seltene „Q" dagegen vier Signale (– – · –). Dadurch werden im Schnitt weniger Signale pro Nachricht benötigt – ein cleverer Vorläufer moderner Kompressionsverfahren. Im Computer ist es meist umgekehrt: Kodierungen verwenden für jedes Zeichen dieselbe feste Anzahl an Bits, egal wie häufig das Zeichen vorkommt. Der Grund: feste Längen lassen sich von Maschinen viel einfacher verarbeiten, speichern und im Speicher gezielt ansteuern (adressieren) als unterschiedlich lange Codes, bei denen man immer erst wissen müsste, wo ein Zeichen endet.


## Vom Zustand zur Zahl:
Die Anzahl der Bits die zur Codierung genutzt werden, zB. also für ein Buchstabe genutzt werden, wird **Byte** genannt. 

Damit aus einer Bitfolge ein Buchstabe entsteht, braucht es eine feste Zuordnungstabelle. Ein bekanntes Beispiel ist ASCII: Dort entspricht „A" der Binärfolge 01000001. Dieses Prinzip beschränkt sich nicht auf Text: Auch Zahlen, Bilder und Töne liegen im Computer letztlich immer nur als Folge von Bits vor. Was diese Bitfolge tatsächlich bedeutet, entscheidet allein die jeweilige Interpretationsregel – der verwendete **Code**.

Jedes zusätzliche Bit verdoppelt die Anzahl der darstellbaren Kombinationen:

| Bits	| Mögliche Kombinationen |
|-------|------------------------|
| 1     |  	2                    |
| 2     | 	4                    |
| 4     | 	16                   |
| 8     | 	256                  |
| 16	  | 65.536                 |
| 32	  | über 4,3 Milliarden    |

<!-- 2^x -->
Die Anzahl von Bits in Bytes ist dabei grundsätzlich nicht festgelegt, allerdings hat sich mit dem IBM System/360 (1964) eine Anzahl von 8 durchgesetzt, da es sich sowohl gut adressieren als auch mit den damals gängigen Zeichensätzen sinnvoll kombinieren ließ.

## Dateiformate als Strukturierungsprinzip
 
Damit eine lange Bitfolge nicht nur *irgendeine* Information, sondern eine sinnvoll strukturierte Datei ergibt, braucht es zusätzlich zur Zeichenkodierung eine übergeordnete Struktur: das **Dateiformat**. Es legt fest,
 
- in welcher Reihenfolge welche Informationen abgelegt sind (z. B. zuerst ein „Header" mit Metadaten, dann die eigentlichen Nutzdaten),
- welcher Code für welchen Abschnitt gilt (z. B. ASCII/Unicode für Text, bestimmte Kompressionsverfahren für Bilder),
- und woran ein Programm erkennt, um welche Art von Datei es sich handelt.
Erst durch diese zusätzliche Strukturierungsebene wird aus einer bloßen Bitfolge eine Textdatei, ein Bild oder eine Tondatei – je nachdem, welches Format und welcher Code zugrunde gelegt werden.

### Gängige Kodierungsformate im Überblick
 
| Format | Bits/Zeichen | Zeichenumfang | Beispiel: „ü" | Typische Verwendung |
|---|---|---|---|---|
| **ASCII** | 7 Bit (fest) | 128 Zeichen: lateinisches Alphabet, Ziffern, Satzzeichen | nicht darstellbar | ältere/englischsprachige Systeme, Steuerzeichen in Protokollen |
| **ISO-8859-1** (*Latin-1*) | 8 Bit (fest) | 256 Zeichen: ASCII + westeuropäische Sonderzeichen (Umlaute, Akzente) | 1 Byte: `FC` | ältere westeuropäische Windows-/Web-Systeme |
| **Windows-1252** (*ANSI*) | 8 Bit (fest) | ähnlich Latin-1, mit einigen zusätzlichen Zeichen (z. B. „…", „€") | 1 Byte: `FC` | lange Standard-Kodierung unter Windows |
| **UTF-8** | 8–32 Bit (variabel, 1–4 Byte) | über 1 Mio. Zeichen (ganzer Unicode-Standard) | 2 Byte: `C3 BC` | heutiger Web-/Dateistandard, abwärtskompatibel zu ASCII |
| **UTF-16** | 16–32 Bit (variabel, 2 oder 4 Byte) | über 1 Mio. Zeichen (ganzer Unicode-Standard) | 2 Byte: `FC 00` (Little Endian) | intern u. a. in Windows, Java, JavaScript |
 
Man sieht hier bereits das Kernproblem, das die folgende Übung greifbar macht: Dasselbe Zeichen „ü" wird je nach Format durch völlig unterschiedliche Bytefolgen dargestellt. Ein Programm kann eine Datei nur dann korrekt anzeigen, wenn es weiß (oder richtig rät), in welchem Format sie gespeichert wurde.

<!--

Größe von TXT Datei

## Kurze Übung
**Durchführung:**
 
1. Öffnet einen neuen Texteditor und schreibt einen kurzen Satz mit möglichst vielen Umlauten und Sonderzeichen, z. B.: *„Übermäßig große Änderungen kosten viel Geld – über 100 €."*
2. Speichert die Datei einmal explizit als **UTF-8** (z. B. `text_utf8.txt`) und einmal als **ANSI/Windows-1252** (z. B. `text_ansi.txt`). Die meisten Editoren bieten dafür ein Dropdown-Menü im Speichern-Dialog.
3. Schließt beide Dateien und öffnet dann `text_utf8.txt` erneut – aber stellt dabei im Editor bewusst die Kodierung auf **ANSI/Windows-1252** um (bei vielen Editoren geht das über rechtsklick „Erneut öffnen mit Kodierung …" oder eine Codierungs-Auswahl unten in der Statusleiste).
4. Beobachtet, was mit den Umlauten passiert – vergleicht das Ergebnis mit dem Original
-->


