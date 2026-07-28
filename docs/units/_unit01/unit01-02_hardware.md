--- 
title: hardware basics
published: false
toc: true
header:
  image: /assets/images/01-splash.jpg
  image_description: "Dr. John Snow's map"
  caption: "Map: [**Dr. John Snow**](https://en.wikipedia.org/wiki/John_Snow) [Welcome Library via wikimedia](https://w.wiki/QtV)"
---

Stellen Sie sich vor, Sie messen in einem Kurs händisch Temperaturen quer durch Marburg. Das Gerät, das Sie dazu benutzen, speichert die Daten nicht ab, weswegen Sie diese händisch in eine Tabelle eintragen müssen.

Für die eigentliche Auswertung werden diese Daten digitalisiert – aber was geschieht dabei physisch, auf der Hardware, eigentlich genau?

Wie funktioniert ein Computer?
Eingabe: Von der Tastatur zum Scan Code

Sie tippen die Zahlen auf Ihrer Tastatur ein, die zum Beispiel über USB mit Ihrem Computer verbunden ist. Sobald Sie eine Taste anschlagen, wird ein Kontakt geschlossen. Ein kleiner Mikrocontroller in Ihrer Tastatur erkennt, an welcher Position dieser Kontakt entstanden ist. Daraus erzeugt er einen sogenannten Scan Code – eine Zahl, die codiert, welche Taste gedrückt wurde – und sendet diesen über USB an Ihren PC.

Vom Bit-Muster zum Zeichen:

Damit 01000001 als Buchstabe "A" erscheint, braucht es eine feste Zuordnungstabelle – z. B. ASCII: dort ist "A" = Dezimalzahl 65 = Binär 01000001
Genau das passiert bereits in Ihrem Beispiel: Der Scan Code der Tastatur ist selbst schon eine Binärzahl, die über USB übertragen wird – der Treiber ordnet sie dann per Tabelle einem Zeichen zu
Nicht nur Text, auch Zahlen, Bilder, Töne – alles, was im Computer verarbeitet wird, liegt letztlich als Folge von Bits vor, nur die Interpretationsregel (der Code) unterscheidet sic

Arbeitsspeicher (RAM)

Der Scan Code landet zunächst im Arbeitsspeicher – RAM (Random Access Memory). Stellen Sie sich das wie den Schreibtisch Ihres Computers vor: Nur Dinge, die auf dem Schreibtisch liegen, können schnell und direkt bearbeitet werden. Je mehr Platz – also Speicher – hier zur Verfügung steht, desto mehr Programme und Daten finden gleichzeitig Platz und können bei Bedarf sofort abgerufen werden. Wie viele Aufgaben tatsächlich gleichzeitig berechnet werden können, hängt allerdings nicht von der Größe des RAM ab, sondern von der Anzahl der Kerne im Prozessor (dazu gleich mehr).

Die Größe des Arbeitsspeichers wird in Byte gemessen – was ein Byte genau ist, erläutern wir im nächsten Kapitel.

Im Arbeitsspeicher liegen außerdem die gerade aktiven Treiber. Ein Treiber ist ein kleines Stück Software, das dem Betriebssystem "übersetzt", wie es mit einem bestimmten Hardware-Bauteil – etwa Ihrer Tastatur – kommunizieren muss. Ohne den passenden Treiber kann das Betriebssystem die Signale eines Geräts nicht sinnvoll interpretieren.

Wichtig: Der Arbeitsspeicher ist ein reiner Kurzzeitspeicher und flüchtig (englisch: volatile). Das bedeutet, sein Inhalt geht verloren, sobald der Computer neu startet oder die Stromversorgung unterbrochen wird. Genau deshalb reicht es nicht aus, dass Ihre Temperaturdaten "nur" im RAM liegen – sie müssen irgendwann dauerhaft gespeichert werden (siehe Abschnitt "Ausgabe" weiter unten).

Trifft ein Scan Code ein, übersetzt der passende Treiber ihn anhand der eingestellten Tastaturbelegung (z. B. QWERTZ) in ein konkretes Zeichen – etwa den Buchstaben "a" oder, bei gleichzeitig gedrückter Umschalttaste, "A". Der Scan Code selbst ist dabei bereits digital; was hier passiert, ist also eine Übersetzung von "welche Taste wurde gedrückt" zu "welches Zeichen ist gemeint" – nicht die Umwandlung in Binärcode, denn binär ist das Signal schon vorher.

Prozessor (CPU) - Rechenwerk & Steuerwerk

Das übersetzte Zeichen kann jetzt an den Prozessor weitergegeben werden. Der Prozessor – die (Central Processing Unit, kurz CPU) – ist das Gehirn Ihres Computers: Er bearbeitet alle Befehle und Anweisungen, die ihm gegeben werden.

Wie schnell die CPU einzelne Befehle abarbeitet, wird unter anderem in Gigahertz (GHz) gemessen: Das gibt an, wie viele Milliarden Rechenzyklen pro Sekunde die CPU ausführen kann. Ein höherer Takt bedeutet grundsätzlich schnellere Verarbeitung – allerdings ist die Taktfrequenz nicht der einzige Faktor. Moderne Prozessoren besitzen mehrere Kerne, die jeweils eigenständig Aufgaben bearbeiten können.
Im Taskmanager können Sie ablesen, wie stark Ihre CPU ausgelastet ist.
Das Ergebnis der Verarbeitung wird anschließend wieder im Arbeitsspeicher zwischengespeichert, bevor es weitergeleitet wird.

Festplatte / SSD: Der Langzeitspeicher

Weil der Arbeitsspeicher flüchtig und außerdem begrenzt ist, gibt es zusätzlich einen Langzeitspeicher: die Festplatte (HDD, Hard Disk Drive) oder – in moderneren Geräten üblicher – eine SSD (Solid State Drive). Im Unterschied zum RAM behält dieser Speicher seinen Inhalt auch ohne Stromversorgung. Hier landen zum Beispiel gespeicherte Dateien, installierte Programme und das Betriebssystem selbst.

Ein Sonderfall: Wenn der Arbeitsspeicher voll ist, kann das Betriebssystem einen Teil der Festplatte bzw. SSD als sogenannten Auslagerungsspeicher (Swap) nutzen – also vorübergehend Daten dorthin auslagern, die eigentlich im RAM liegen sollten. Das funktioniert, ist aber deutlich langsamer als echter Arbeitsspeicher, weshalb ein Computer merklich langsamer wird, wenn er "swappen" muss.

Im Taskmanager können Sie ablesen, wie viel Prozent Ihres Arbeitsspeichers gerade belegt sind.


Ausgabe: Anzeige und Speicherung

Damit schließt sich der Kreis von der Eingabe zur Ausgabe. Vom Arbeitsspeicher aus kann das verarbeitete Ergebnis auf zwei Wegen "nach außen" gelangen:

Anzeige auf dem Bildschirm: Die Grafikkarte (GPU) übernimmt die Daten aus dem Arbeitsspeicher und berechnet daraus ein Bild, das über das Anzeigekabel (z. B. HDMI) an den Monitor gesendet und dort dargestellt wird. Das passiert kontinuierlich und sehr schnell – deshalb sehen Sie die eingetippte Zahl praktisch sofort auf dem Bildschirm erscheinen.
Dauerhafte Speicherung: Wenn Sie Ihre Tabelle speichern, schreibt das Betriebssystem die Daten aus dem Arbeitsspeicher auf die Festplatte bzw. SSD. Erst ab diesem Moment sind Ihre Temperaturwerte auch nach einem Neustart des Computers noch vorhanden.
Der Weg im Überblick, am Beispiel Ihrer Temperaturmessung

Nehmen wir an, Sie tippen den Wert "21,5" ein:

Der Tastendruck erzeugt einen Scan Code, der über USB an den Computer gesendet wird.
Der Scan Code landet im Arbeitsspeicher; ein Treiber übersetzt ihn Zeichen für Zeichen in "2", "1", "," und "5".
Die CPU verarbeitet diese Zeichen – etwa, um sie in der Tabellenkalkulationssoftware in die richtige Zelle einzutragen und ggf. mit anderen Werten zu verrechnen.
Das Ergebnis wird zurück in den Arbeitsspeicher geschrieben.
Über die Grafikkarte erscheint der Wert sofort sichtbar auf Ihrem Bildschirm.
Sobald Sie die Datei speichern, wird sie dauerhaft auf der Festplatte bzw. SSD abgelegt – erst dann ist Ihre Messung wirklich "gesichert".



> Rufen Sie den Taskmanager mittels shortcut (STR + ALT + ENTF) auf


