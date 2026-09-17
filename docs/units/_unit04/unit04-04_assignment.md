--- 
title: ÜA | Übungsaufgabe Abschnitt 04
published: true
toc: true
header:
  image: /assets/images/01-splash.jpg
  image_description: "Dr. John Snow's map"
  caption: "Map: [**Dr. John Snow**](https://en.wikipedia.org/wiki/John_Snow) [Wellcome Library via wikimedia](https://w.wiki/QtV)"
---
## Übungsaufgabe 04

In dieser Übungsaufgabe wenden Sie das Gelernte aus Lernabschnitt 04 selbstständig an. Grundlage ist erneut `Abschlusstest_Datensatz.xlsx` (Tabellenblatt „Testdaten") – ein neuer, eigenständiger Datensatz, der auf denselben echten Sensordaten wie die Kursübungen beruht.

---

**1.** Welcher der folgenden Dateinamen entspricht dem empfohlenen Schema `NAME_INHALT_DATUM_VERSION`?
a) `Sensordaten_final_NEU.xlsx`
b) `Müller Sensordaten 16032026.xlsx`
c) `Mueller_Sensordaten_20260316_v1.xlsx`
d) `v1_Mueller_Sensordaten.xlsx`

**2.** Wie viele Ordnerebenen unterhalb des Projektordners werden als Obergrenze empfohlen, bevor eine Datei liegt?

**3.** Welcher Ordner ist in jedem Datenprojekt Pflicht, unabhängig von der übrigen Ordnerstruktur?

**4.** Was ist der Unterschied zwischen einem absoluten und einem relativen Dateipfad, und welcher ist beim Austausch mit anderen Personen meist robuster?

**5.** Filtern Sie die Spalte `Standort` so, dass **alle Schreibweisen** von „Firmaneiplatz" gemeinsam angezeigt werden. Wie viele Zeilen sind danach sichtbar?

**6.** Sortieren Sie die gesamte Tabelle zuerst nach `Standort` (A–Z), dann nach `Datum` (aufsteigend). Welcher Wert steht danach in der Temperaturspalte von Zeile 15?

**7.** Was passiert, wenn Sie beim Sortieren nur die Spalte `Temperatur` markieren (nicht die ganze Tabelle) und im Warndialog „Mit der aktuellen Auswahl fortfahren" statt „Auswahl erweitern" wählen?

**8.** Was ist der Unterschied zwischen `=SUMME(Bereich)` und `=TEILERGEBNIS(9;Bereich)` bei einer gefilterten Tabelle?

**9.** Wenden Sie „Daten → Duplikate entfernen" (alle Spalten) auf die Tabelle an. Wie viele Zeilen bleiben danach übrig?

**10.** Wie viele **unterschiedliche Rohschreibweisen** zeigt das Filter-Dropdown der Spalte `Standort`, bevor Sie irgendetwas bereinigen?

**11.** Wenden Sie `=GROSS2(...)` auf den Wert `"FIRMANEIPLATZ"` an. Welches Ergebnis liefert die Formel?

**12.** Wozu dient die Funktion `GLÄTTEN`, und woran erkennen Sie in der Bearbeitungsleiste, dass eine Zelle ein überflüssiges Leerzeichen enthält?

**13.** Welchen Wert liefert `=LÄNGE(...)` für den Standort-Eintrag `"Friedhofsweg (Ost)"`?

**14.** Wozu dient die bedingte Formatierung „Doppelte Werte", und warum ist sie vor dem endgültigen Löschen von Duplikaten sinnvoll?

**15.** Nach Anwendung von „Duplikate entfernen": Welche der beiden identischen Zeilen (die ursprüngliche oder die weiter unten stehende Kopie) bleibt erhalten?
<!-- Musterlösung (nicht für Studierende sichtbar):
1. c)
2. 3-4 Ebenen
3. 01_Rohdaten (bzw. Raw_Data) - wird nie ueberschrieben
4. Absoluter Pfad: vollstaendiger Weg vom Laufwerk aus; Relativer Pfad: ausgehend vom aktuellen Ordner. Relative Pfade sind robuster, da sie nicht von individuellem Nutzernamen/Laufwerksbuchstaben abhaengen
5. 6 Zeilen
6. 21,01
7. Nur die Temperaturspalte wird umsortiert, alle anderen Spalten bleiben an ihrer Position -> Datensaetze passen nicht mehr zusammen
8. SUMME bezieht ausgeblendete/gefilterte Zeilen weiterhin mit ein, TEILERGEBNIS(9;...) nur die aktuell sichtbaren Zeilen
9. 20 Zeilen (eine exakte Duplikat-Zeile wird entfernt)
10. 6 (Firmaneiplatz, FIRMANEIPLATZ, Friedhofsweg, Friedhofsweg (Ost), Neuhöfe, Wilhelm-Roser-Str.)
11. "Firmaneiplatz"
12. Entfernt fuehrende/nachfolgende sowie doppelte Leerzeichen; in der Bearbeitungsleiste ist ein Leerzeichen als kleiner Abstand nach dem letzten sichtbaren Zeichen erkennbar
13. 19 Zeichen
14. Markiert Duplikate farblich, ohne sie zu loeschen, sodass man vorab pruefen kann, ob es sich wirklich um Duplikate handelt
15. Die ursprüngliche (weiter oben stehende) Zeile bleibt erhalten, die später stehende Kopie wird entfernt
-->
