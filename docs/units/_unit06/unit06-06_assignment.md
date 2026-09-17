--- 
title: ÜA | Übungsaufgabe Abschnitt 06
published: true
toc: true
header:
  image: /assets/images/01-splash.jpg
  image_description: "Dr. John Snow's map"
  caption: "Map: [**Dr. John Snow**](https://en.wikipedia.org/wiki/John_Snow) [Wellcome Library via wikimedia](https://w.wiki/QtV)"
---

<!-- Übungsaufgabe 06: Zusammenführen, SVERWEIS, Pivot, Häufigkeitstabellen, Korrelation -->
## Übungsaufgabe 06

In dieser Übungsaufgabe wenden Sie das Gelernte aus Lernabschnitt 06 selbstständig an. Grundlage sind erneut `Abschlusstest_Datensatz.xlsx` (Tabellenblatt „Testdaten") sowie `Stationsmetadaten.xlsx`.

---

**1.** Sie erhalten zwei Tabellen mit denselben Messgrößen, aber unterschiedlich benannten und angeordneten Spalten. Warum reicht es nicht, die zweite Tabelle einfach unterhalb der ersten einzufügen, ohne vorher etwas anzupassen?

**2.** Eine Spalte `Zeitstempel` enthält Datum und Uhrzeit kombiniert. Mit welcher Formel erhalten Sie daraus **nur** das Datum?

**3.** Mit welcher Formel erhalten Sie aus demselben Zeitstempel **nur** die Uhrzeit?

**4.** Nutzen Sie `SVERWEIS`, um aus `Stationsmetadaten.xlsx` die Höhe über NN für „Firmaneiplatz" nachzuschlagen. Welcher Wert kommt heraus?

**5.** Schlagen Sie auf dieselbe Weise die Höhe über NN für „Neuhöfe" nach. Welcher Wert kommt heraus?

**6.** Wofür steht das vierte Argument `FALSCH` in `=SVERWEIS(Suchkriterium;Matrix;Spaltenindex;FALSCH)`?

**7.** Sie erhalten bei einem `SVERWEIS` den Fehler `#NV`. Nennen Sie einen typischen Grund dafür, bezogen auf mögliche Probleme in Ihren eigenen Daten.

**8.** Zählen Sie mit `=ZÄHLENWENN(...)`, wie oft der **exakte** Wert `"Firmaneiplatz"` (Groß-/Kleinschreibung wie geschrieben) in der Spalte `Standort` vorkommt. Wie viele sind es?

**9.** Erstellen Sie eine Pivot-Tabelle mit `Standort` in den Zeilen (ohne vorherige Bereinigung der Schreibweise). Wie viele unterschiedliche Zeilen/Kategorien zeigt die Pivot-Tabelle für `Standort`?

**10.** Was sagt das Ergebnis aus Frage 9 darüber aus, ob eine Pivot-Tabelle Schreibweise-Inkonsistenzen automatisch zusammenfasst?

**11.** Berechnen Sie mit `=KORREL(...)` den Korrelationskoeffizienten zwischen `Datum` und `Temperatur` für alle **exakt** als `"Firmaneiplatz"` geschriebenen Zeilen. Wie lautet der Wert (2 Nachkommastellen)?

**12.** Ordnen Sie den Wert aus Frage 11 anhand der Faustregel ein: schwacher, mittlerer oder starker Zusammenhang – und positiv oder negativ?

**13.** Erstellen Sie zusätzlich ein Streudiagramm derselben beiden Variablen. Was zeigt Ihnen dieses Diagramm, das der reine `KORREL`-Wert allein nicht zeigen würde?

**14.** Richtig oder falsch: Ein hoher Korrelationswert beweist, dass die eine Variable die andere ursächlich beeinflusst.

**15.** Sie ändern nachträglich einen Wert in Ihren Ausgangsdaten. Aktualisiert sich Ihre bereits erstellte Pivot-Tabelle automatisch? Falls nicht, was müssen Sie tun?

<!-- Musterlösung (nicht für Studierende sichtbar):
1. Die Spalten haben unterschiedliche Namen und stehen in unterschiedlicher Reihenfolge; ohne Angleichen wuerden Werte in falschen Spalten landen bzw. gleichartige Werte nicht in derselben Spalte zusammengefuehrt
2. =GANZZAHL(Zelle)
3. =Zelle-GANZZAHL(Zelle)
4. 187
5. 267
6. Exakte Uebereinstimmung erzwingen (statt einer ungefaehren, sortierabhaengigen Suche mit WAHR)
7. Z. B. uneinheitliche Schreibweise/Leerzeichen im Suchwert, die noch nicht bereinigt wurde
8. 5
9. 6 (Pivot behandelt jede Rohschreibweise als eigene Kategorie)
10. Nein - eine Pivot-Tabelle fasst Schreibweise-Varianten NICHT automatisch zusammen, Bereinigung (GROSS2/GLÄTTEN) muss vorher erfolgen
11. -0,88
12. Starker, negativer Zusammenhang (Temperatur sinkt mit steigendem Datum in diesem Ausschnitt)
13. Ob der Zusammenhang tatsaechlich linear ist bzw. wie die Punktwolke konkret aussieht (Form, Ausreisser)
14. Falsch
15. Nein; Rechtsklick in die Pivot-Tabelle -> "Aktualisieren"
-->
