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
Hier sollte ein Einführungstext zum Thema "Binärsystem, Bits & Bytes / Grundlegende Kodierung (Text, Zahlen, Bilder) / Dateiformate als Strukturierungsprinzip" stehen.

## Codierung

Grundidee anhand Morse Code Morse-Code:

Alle notwendigen Informationen müssen für den Computer lesbar gemacht werden.
Dies kann durch zwei Zustände erreicht werden: Strom an (1) und Strom aus (0), technisch meist als hohe bzw. niedrige elektrische Spannung realisiert
Mit diesen zwei Zuständen kann jede Information dargestellt werden – man muss sich nur vorher auf eine Zuordnung (einen Code) einigen.

SOS ist ein gutes Einstiegsbeispiel für "Codierung": ... --- ... – drei kurze, drei lange, drei kurze Signale
Es werden nur zwei Zustände gebraucht (kurz/lang, bzw. Ton an/aus).


Vom Zustand zur Zahl:

Ein einzelner Zustand (0 oder 1) heißt Bit (Binary Digit)
8 Bit = 1 Byte → damit lassen sich 2⁸ = 256 verschiedene Kombinationen darstellen (z. B. 01000001)
Je mehr Bits zur Verfügung stehen, desto mehr unterschiedliche Werte lassen sich codieren (2 Bit = 4 Möglichkeiten, 8 Bit = 256, 16 Bit = 65.536 usw.)

Vom Bit-Muster zum Zeichen:

Damit 01000001 als Buchstabe "A" erscheint, braucht es eine feste Zuordnungstabelle – z. B. ASCII: dort ist "A" = Dezimalzahl 65 = Binär 01000001
Genau das passiert bereits in Ihrem Beispiel: Der Scan Code der Tastatur ist selbst schon eine Binärzahl, die über USB übertragen wird – der Treiber ordnet sie dann per Tabelle einem Zeichen zu
Nicht nur Text, auch Zahlen, Bilder, Töne – alles, was im Computer verarbeitet wird, liegt letztlich als Folge von Bits vor, nur die Interpretationsregel (der Code) unterscheidet sich


<!-- Notizen: Ab hier folgen Vermerke, welche als Gedankenstütze oder Erinnerung dienen aber noch nicht in der vorhandenen Form veröffentlicht werden sollen. -->
<!-- überarbeiten

- hinzufügen wie Bilder etc codiert werden


## BIOS
Was ist das BIOS – kurz zusammengefasst
Das BIOS (Basic Input/Output System) ist eine kleine, fest auf einem Chip des Mainboards gespeicherte Firmware – kein Programm, das "irgendwo" auf der Festplatte liegt
Seine Aufgabe: Beim Einschalten die Hardware grundlegend testen (POST), das Betriebssystem finden und dessen Start anstoßen – danach zieht es sich zurück
Es ist die Brücke zwischen reiner Elektronik und Software: Ohne BIOS/UEFI wüsste der Computer beim Einschalten gar nicht, wie er überhaupt mit RAM, Tastatur oder Festplatte "sprechen" soll
Heute meist als UEFI umgesetzt, dem technischen Nachfolger – der Begriff "BIOS" wird umgangssprachlich aber oft weiterbenutzt

Etwas Geschichte:

Der Begriff "BIOS" stammt aus den 1970er-Jahren, geprägt im Umfeld des Betriebssystems CP/M
Richtig bekannt wurde das BIOS 1981 mit dem IBM PC – IBM veröffentlichte den BIOS-Quellcode offen mit, was es anderen Herstellern ermöglichte, kompatible ("IBM-kompatible") PCs zu bauen, indem sie das BIOS nachbauten
Über Jahrzehnte änderte sich das BIOS kaum – textbasiert, per Tastatur bedient
Ab Mitte der 2000er-Jahre wurde UEFI entwickelt (ursprünglich von Intel), um Beschränkungen des alten BIOS zu überwinden (u. a. Festplattengröße, Startgeschwindigkeit, fehlende grafische Bedienung) – seit den 2010er-Jahren ist UEFI bei neuen Geräten der Standard


## Was ist ein Betriebssystem – kurz zusammengefasst
Das Betriebssystem (Operating System, OS) ist die Software-Schicht zwischen Hardware und Anwendungsprogrammen
Es sorgt dafür, dass Sie sich als Nutzer:in nicht selbst um Hardware-Details kümmern müssen: Speicherverwaltung, Prozessverwaltung, Dateisystem, Treiber-Kommunikation laufen im Hintergrund
Ohne Betriebssystem müsste jedes einzelne Programm selbst wissen, wie es exakt mit der jeweiligen Grafikkarte, Festplatte usw. spricht – das Betriebssystem übernimmt diese Vermittlerrolle einmal zentral für alle Programme

Etwas Geschichte:

Frühe Computer (1940er/50er) hatten noch kein Betriebssystem – Programme wurden direkt in die Maschine "verdrahtet" oder über Lochkarten eingespeist, ein Job nach dem anderen
In den 1960ern entstanden erste echte Betriebssysteme, die mehrere Programme/Nutzer verwalten konnten (z. B. bei Großrechnern von IBM)
1974 erschien CP/M, eines der ersten verbreiteten Betriebssysteme für Heimcomputer/frühe PCs
1981 brachte Microsoft mit dem IBM PC MS-DOS heraus – textbasiert, ohne grafische Oberfläche, wurde aber der Grundstein für Windows
Apple veröffentlichte 1984 mit dem Macintosh eines der ersten Betriebssysteme mit grafischer Oberfläche (Fenster, Maus) für den Massenmarkt
1985 folgte Windows 1.0 als grafische Oberfläche auf Basis von MS-DOS; erst mit Windows 95 wurde diese Trennung endgültig aufgehoben
Parallel entstand 1991 Linux, ein freies, quelloffenes Betriebssystem, das bis heute z. B. auf Servern, in Android-Smartphones und in eingebetteten Systemen läuft
-->
