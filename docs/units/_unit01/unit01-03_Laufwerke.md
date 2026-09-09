---
title: Laufwerke
published: true
toc: true
header:
  image: /assets/images/01-splash.jpg
  image_description: "Dr. John Snow's map"
  caption: "Map: [**Dr. John Snow**](https://en.wikipedia.org/wiki/John_Snow) [Wellcome Library via wikimedia](https://w.wiki/QtV)"
---

## Laufwerke, Netzwerke und Pfade
 
Im letzten Kapitel haben wir gesehen, dass Daten am Ende auf einem Langzeitspeicher landen müssen, um wirklich dauerhaft gesichert zu sein. In diesem Kapitel schauen wir uns genauer an, was für Arten von Speicherorten – sogenannte **Laufwerke** – es gibt, wie mehrere Computer über ein **Netzwerk** auch auf fremde Speicherorte zugreifen können, und wie man innerhalb dieser Speicherstruktur eine einzelne Datei über ihren **Pfad** eindeutig wiederfindet.
 
Ein Laufwerk ist ganz allgemein ein Gerät bzw. eine Speichereinheit, auf der Daten dauerhaft abgelegt und wieder gelesen werden können. Der Name kommt historisch daher, dass frühere Speichermedien tatsächlich mechanisch liefen – also rotierten, während ein Lese-/Schreibkopf darüberfuhr. Heute wird der Begriff weiter genutzt, auch wenn SSDs (siehe unten) gar keine beweglichen Teile mehr haben – „Laufwerk" ist eher zu einem Oberbegriff für „Speicherort, den das Betriebssystem als eigenständige Einheit erkennt" geworden.
 
Ein Laufwerk ist dabei immer nichtflüchtiger Langzeitspeicher (Daten bleiben ohne Strom erhalten) – im Gegensatz zum Arbeitsspeicher, der flüchtig ist. Genau das macht ein Laufwerk zum Ziel des letzten Schritts im Eingabe-Ausgabe-Beispiel aus dem vorherigen Kapitel: Erst wenn Ihre Daten auf einem Laufwerk landen, sind sie wirklich dauerhaft gesichert.
 
### Lokale Laufwerke
 
Es gibt verschiedene Varianten lokaler, also direkt am eigenen Gerät angeschlossener Laufwerke:
 
**Festplatte (HDD, Hard Disk Drive):**
- Speichert Daten magnetisch auf sich drehenden Metallscheiben – bei gängigen Consumer-Modellen typischerweise mit 5.400 oder 7.200 Umdrehungen pro Minute, bei speziellen Server-Festplatten auch deutlich mehr.
- Ein beweglicher Lese-/Schreibkopf fährt über die Scheibe, um Daten zu lesen oder zu schreiben – mechanisch, dadurch vergleichsweise langsam.
- Vorteil: viel Speicherplatz für relativ wenig Geld. Nachteil: langsamer und empfindlicher gegenüber Erschütterungen, da bewegliche Teile verbaut sind.
**SSD (Solid State Drive):**
- Speichert Daten rein elektronisch in Flash-Speicherchips – keine beweglichen Teile.
- Deutlich schneller als eine HDD (kürzere Ladezeiten, schnellerer Systemstart).
- Heute in den meisten neuen Laptops/PCs Standard, oft als NVMe-SSD direkt auf dem Mainboard verbaut statt über ein Kabel angebunden.
**Wechseldatenträger / externe Laufwerke:**
- USB-Stick / externe SSD/HDD: tragbarer Speicher, wird über USB angeschlossen und vom Betriebssystem wie ein zusätzliches Laufwerk erkannt.
- Optische Laufwerke (CD/DVD/Blu-ray): lesen bzw. schreiben Daten per Laserlicht auf eine reflektierende Scheibe – heute wegen SSDs, USB-Sticks und Cloud-Speicher stark rückläufig und kaum noch in neuen Geräten verbaut.
- Speicherkarten (SD-Karte etc.): ähnlich wie SSDs, aber kompakter – häufig in Kameras oder als Speichererweiterung bei Laptops/Tablets.
### Netzwerk
 
Ein Netzwerk verbindet mehrere Geräte, damit sie Daten austauschen können – vom kleinen Heimnetzwerk bis zum weltweiten Internet. Jedes Gerät im Netzwerk bekommt dabei eine eindeutige Adresse, die **IP-Adresse**, damit Datenpakete gezielt zugestellt werden können – vergleichbar mit einer Postanschrift.
 
**Wie Daten im Netzwerk reisen:**
- Größere Datenmengen werden in kleine Pakete zerlegt, einzeln über das Netzwerk verschickt und beim Empfänger wieder zusammengesetzt.
- Dafür sorgen Protokolle wie **TCP/IP** – feste Regeln, nach denen Geräte im Netzwerk miteinander „sprechen", damit Pakete korrekt und vollständig ankommen.

### Netzlaufwerke im Uninetz (Laufwerk H:)
 
Ein Netzwerk kann nicht nur einzelne Datenpakete austauschen, sondern auch ganze Speicherorte gemeinsam nutzbar machen. An vielen Hochschulen ist das so organisiert: Jede Studierende bzw. jeder Studierende bekommt einen persönlichen Ordner auf einem zentralen Server der Universität – dort liegen die eigenen Dateien nicht lokal auf dem PC, sondern zentral im Rechenzentrum.
 
Damit man mit diesem Ordner genauso einfach arbeiten kann wie mit einer lokalen Festplatte, bindet das Betriebssystem ihn als sogenanntes **Netzlaufwerk** ein und vergibt dafür einen eigenen Laufwerksbuchstaben –  **H:** (für „Home-Verzeichnis"). Für Sie als Nutzer:in sieht es dann so aus, als hätten Sie ein ganz normales zusätzliches Laufwerk – tatsächlich liegen die Daten aber auf einem Server, der über das Universitätsnetzwerk angesprochen wird.
 
Das hat einen praktischen Vorteil: Melden Sie sich an einem beliebigen Uni-Rechner an, taucht Ihr H:-Laufwerk mit denselben Dateien wieder auf – die Daten „folgen" Ihnen also über Ihren Account, unabhängig vom Gerät.
Es hat aber auch den Nachteil, dass Ihr verfügbarer Speicherplatz begrenzt ist. 
<!-- Aufgabe an Lisa: herausfinden, ob das noch aktuell ist und wie viel Platz zur Verfügung steht -->
### Pfade
 
Damit ein Programm oder Betriebssystem eine bestimmte Datei unter den vielen Millionen Dateien auf einem oder mehreren Laufwerken eindeutig finden kann, braucht es eine genaue Adresse – den **Pfad**. Ein Pfad beschreibt, über welche Laufwerke und Ordner (Verzeichnisse) hinweg man zu einer Datei gelangt.
 
**Zwei Arten von Pfaden:**
- **Absoluter Pfad:** beschreibt den kompletten Weg vom Laufwerk aus, z. B. `H:\Dokumente\Uni\Hausarbeit.docx`. Er funktioniert unabhängig davon, wo man sich gerade befindet, ist dafür aber länger.
- **Relativer Pfad:** beschreibt den Weg ausgehend vom aktuellen Ordner, z. B. `..\Hausarbeit.docx` (eine Ebene nach oben, dann die Datei). Das `..` steht dabei für „ein Verzeichnis nach oben", ein einzelner Punkt `.` für „das aktuelle Verzeichnis".
**Ein kleiner, aber wichtiger Unterschied zwischen Betriebssystemen:** Windows trennt Ordnernamen im Pfad traditionell mit einem Backslash `\` (z. B. `C:\Users\Name\Bilder`), während macOS und Linux den regulären Schrägstrich `/` verwenden (z. B. `/home/name/bilder`). Zusätzlich kennt Windows Laufwerksbuchstaben wie `C:` oder `H:`, während Unix-artige Systeme (Linux, macOS) alle Laufwerke in einen einzigen gemeinsamen Verzeichnisbaum einhängen, der immer bei `/` (dem sogenannten „Root"-Verzeichnis) beginnt – es gibt dort also gar keine Laufwerksbuchstaben.
 
**Netzwerkpfade:** Ein Netzlaufwerk wie das H:-Laufwerk aus dem vorherigen Abschnitt ist im Kern nur eine Abkürzung für einen sogenannten **UNC-Pfad** (*Universal Naming Convention*), der Server und Freigabe direkt benennt, z. B. `\\uni-server\home\mustermann`. Das Betriebssystem „übersetzt" diesen langen Netzwerkpfad für Sie bequem in den kurzen Laufwerksbuchstaben `H:` – dahinter steckt aber technisch derselbe Mechanismus wie bei jedem anderen Pfad auch.

<!-- Notizen: Ab hier folgen Vermerke, welche als Gedankenstütze oder Erinnerung dienen aber noch nicht in der vorhandenen Form veröffentlicht werden sollen. -->
<!-- Bitte Gedanken innerhalb der Kommentarfunktion einfügen. -->
