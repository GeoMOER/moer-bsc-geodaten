---
title: Betriebssystem und BIOS
published: true
toc: true
header:
  image: /assets/images/01-splash.jpg
  image_description: "Dr. John Snow's map"
  caption: "Map: [**Dr. John Snow**](https://en.wikipedia.org/wiki/John_Snow) [Wellcome Library via wikimedia](https://w.wiki/QtV)"
---



## Betriebssystem
 
Das **Betriebssystem** (*Operating System*, OS) ist die Software-Schicht zwischen Hardware und Anwendungsprogrammen. Ohne diese Vermittlerschicht müsste jedes einzelne Programm selbst ganz genau wissen, wie es mit der jeweiligen Grafikkarte, Festplatte oder Tastatur eines konkreten Geräts spricht – das Betriebssystem übernimmt diese Vermittlerrolle einmal zentral für alle Programme. So müssen Sie sich als Nutzer:in um diese Details nicht mehr kümmern.
 
Konkret übernimmt das Betriebssystem im Hintergrund vor allem vier zentrale Aufgaben:
 
- **Speicherverwaltung:** entscheidet, welches Programm wie viel Arbeitsspeicher (RAM) bekommt, und sorgt dafür, dass sich Programme dabei nicht gegenseitig in die Quere kommen.
- **Prozessverwaltung:** verteilt die Rechenzeit der CPU auf die gleichzeitig laufenden Programme (Prozesse) – dadurch entsteht der Eindruck, dass mehrere Programme parallel laufen.
- **Dateisystemverwaltung:** organisiert, wie und wo Dateien auf Laufwerken abgelegt werden, und stellt darüber die Ordner- und Pfadstruktur bereit, die wir im vorherigen Abschnitt besprochen haben.
- **Treiberkommunikation:** vermittelt zwischen der eigentlichen Anwendungssoftware und den Treibern, die wiederum mit der konkreten Hardware sprechen (siehe das Tastatur-Beispiel aus dem Kapitel „Wie funktioniert ein Computer?").
### Gängige Betriebssysteme im Vergleich
 
| | Windows | macOS | Linux | Android | iOS |
|---|---|---|---|---|---|
| **Entwickler** | Microsoft | Apple | offene Community (verschiedene Firmen wie Red Hat, Canonical u. a. beteiligt) | Google | Apple |
| **Lizenzmodell** | proprietär, kostenpflichtig | proprietär, im Kaufpreis der Apple-Hardware enthalten | meist Open Source und kostenlos | Kernel Open Source, viele Geräte mit zusätzlichen proprietären Google-Diensten | proprietär, nur auf Apple-Hardware |
| **Technische Basis** | eigener NT-Kernel | Unix-basiert (Darwin/BSD) | Linux-Kernel | basiert auf dem Linux-Kernel | Unix-basiert (Darwin, wie macOS) |
| **Läuft auf** | PCs/Laptops verschiedenster Hersteller | ausschließlich Apple-Geräten (Mac) | PCs, Server, eingebettete Systeme, sehr variabel | Smartphones/Tablets verschiedenster Hersteller | ausschließlich iPhone/iPad |
| **Typischer Einsatz** | Privat-PCs, Büro, Gaming | Privat- und Kreativ-PCs (Design, Video) | Server, Entwicklung, wissenschaftliches Rechnen | mobile Endgeräte | mobile Endgeräte |
| **Beispiele/Versionen** | Windows 10, Windows 11 | macOS Sonoma, Sequoia | Ubuntu, Fedora, Debian | Android 14, 15 | iOS 17, 18 |
 
Auffällig dabei: macOS, Linux und Android/iOS teilen sich technisch enger verwandte Wurzeln (Unix bzw. Linux-Kernel), während Windows historisch auf einer komplett eigenen Codebasis aufbaut – ein Nachwirken der in der Zeittabelle unten skizzierten getrennten Entwicklungslinien.
 
*Kurze Randnotiz zur Geschichte:*
 
| Jahr | Meilenstein |
|---|---|
| 1940er/50er | noch kein Betriebssystem – Programme liefen einzeln, direkt „verdrahtet" oder per Lochkarte eingespeist |
| 1960er | erste echte Betriebssysteme bei Großrechnern, die mehrere Programme/Nutzer gleichzeitig verwalten konnten |
| 1974 | CP/M – eines der ersten verbreiteten Betriebssysteme für frühe Heimcomputer |
| 1981 | MS-DOS (Microsoft) zum IBM PC – textbasiert, wurde zur Grundlage von Windows |
| 1984 | Macintosh (Apple) – eines der ersten massentauglichen Betriebssysteme mit grafischer Oberfläche (Fenster, Maus) |
| 1985 | Windows 1.0 als grafische Oberfläche auf Basis von MS-DOS; erst Windows 95 vereinte beides endgültig |
| 1991 | Linux – freies, quelloffenes Betriebssystem, heute u. a. auf Servern, in Android und in eingebetteten Systemen verbreitet |
 
## BIOS und UEFI
 
Jetzt, wo klar ist, was ein Betriebssystem überhaupt leistet, stellt sich eine Frage: Wie startet dieses Betriebssystem eigentlich, wenn Sie den Computer einschalten? Direkt nach dem Einschalten ist ja noch gar nichts geladen – der Computer muss also erst einmal grundlegend wissen, wie er mit seiner eigenen Hardware (RAM, Tastatur, Festplatte) kommuniziert, bevor er das Betriebssystem überhaupt finden und starten kann. Genau diese Vorstufe übernimmt das BIOS.
 
Das **BIOS** (*Basic Input/Output System*) ist eine kleine Firmware, die fest auf einem Chip des Mainboards gespeichert ist – kein Programm, das irgendwo auf der Festplatte liegt, sondern quasi fest „eingebrannte" Software. Beim Einschalten des Computers übernimmt es drei Aufgaben:
 
1. **Hardware-Test (POST, *Power-On Self-Test*):** Es prüft, ob RAM, Tastatur, Laufwerke usw. grundsätzlich funktionieren und erkannt werden.
2. **Betriebssystem suchen:** Es sucht auf den angeschlossenen Laufwerken nach einem startfähigen Betriebssystem.
3. **Übergabe:** Es übergibt die Kontrolle an das gefundene Betriebssystem und „zieht sich zurück" – ab hier übernimmt das Betriebssystem selbst die weitere Steuerung, so wie im Abschnitt oben beschrieben.
Das BIOS ist damit die Brücke zwischen reiner Elektronik und Software: Ohne diese Grundausstattung wüsste der Computer beim Einschalten gar nicht, wie er überhaupt etwas mit seinen eigenen Bauteilen anfangen soll.
 
**UEFI** (*Unified Extensible Firmware Interface*) ist der technische Nachfolger des klassischen BIOS und heute in praktisch allen neuen Geräten verbaut – umgangssprachlich wird trotzdem oft weiterhin einfach „BIOS" gesagt. Der wichtigste Unterschied:
 
| | BIOS (klassisch) | UEFI |
|---|---|---|
| Bedienung | rein textbasiert, nur Tastatur | grafische Oberfläche, oft auch Maus nutzbar |
| Startgeschwindigkeit | langsamer | deutlich schneller |
| Unterstützte Festplattengröße | begrenzt (klassisch max. ca. 2 TB) | praktisch keine relevante Grenze |
| Sicherheit | keine eingebauten Schutzmechanismen | z. B. „Secure Boot" gegen manipulierte Startsoftware |