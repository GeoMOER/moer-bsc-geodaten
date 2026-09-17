---
title: SVERWEIS
published: true
toc: true
header:
  image: /assets/images/unit04/streuobst.jpg
  image_description: "Streuobstwiese"
  caption: "Image: ulrichstill [CC BY-SA 2.0 DE] via [wikimedia.org](https://commons.wikimedia.org/wiki/File:Tuebingen_Streuobstwiese.jpg)"
---
## Mit SVERWEIS Informationen nachschlagen

Sie erhalten eine zusätzliche kleine Tabelle `Stationsmetadaten.xlsx` mit der Höhenlage jeder Station über Normalnull (NN). Diese Information steht in einer **separaten Tabelle**, nicht in Ihren Messdaten – ein sehr häufiger Fall: Stammdaten (die sich selten ändern, z. B. die Höhenlage einer Station) werden getrennt von Messdaten (die sich laufend ändern) gepflegt.

`SVERWEIS` ("Senkrechter Verweis") sucht einen Wert in der **ersten Spalte** einer Tabelle und gibt einen Wert aus einer **anderen Spalte derselben Zeile** zurück:

```
=SVERWEIS(Suchkriterium; Matrix; Spaltenindex; [Bereich_Verweis])
```

| Argument | Bedeutung |
|---|---|
| `Suchkriterium` | Der Wert, nach dem gesucht wird (z. B. eine Zelle mit einem Standortnamen) |
| `Matrix` | Der Tabellenbereich, in dem gesucht wird – die **erste Spalte** dieses Bereichs muss das Suchkriterium enthalten |
| `Spaltenindex` | Die wievielte Spalte der Matrix (von links gezählt) den gewünschten Wert enthält |
| `Bereich_Verweis` | `FALSCH` für eine **exakte** Übereinstimmung (fast immer die richtige Wahl); `WAHR` sucht nur eine ungefähre Übereinstimmung |

**Beispiel:** In Ihrer zusammengeführten Tabelle steht in Zelle `A2` der Standortname. In `Stationsmetadaten.xlsx` steht in Spalte A der Standortname, in Spalte B die Höhe über NN. Die Formel

```
=SVERWEIS(A2;Stationsmetadaten!A:B;2;FALSCH)
```

sucht den Wert aus `A2` in Spalte A des Blatts `Stationsmetadaten`, findet die passende Zeile und gibt den Wert aus deren zweiter Spalte zurück (die Höhe über NN).

<!-- Screenshot: Excel-Formel =SVERWEIS(A2;Stationsmetadaten!A:B;2;FALSCH) in der Bearbeitungsleiste, daneben in der Zelle das korrekte Ergebnis (eine Höhenangabe in Metern), sowie ein zweites Tabellenblatt "Stationsmetadaten" mit der Nachschlage-Tabelle im Hintergrund sichtbar. -->

**Wichtige Stolperfalle:** `FALSCH` (exakte Übereinstimmung) sollten Sie fast immer verwenden. Mit `WAHR` sortiert Excel die Suche anders und liefert bei nicht exakt passenden Werten stillschweigend ein falsches Ergebnis, statt einen Fehler zu melden – das fällt oft erst bei einer späteren Prüfung auf.

**Wenn `SVERWEIS` einen Fehler liefert (`#NV`):** Das bedeutet meist, dass der gesuchte Wert nicht exakt in der ersten Spalte der Matrix vorkommt – z. B. weil eine Schreibweise noch nicht bereinigt ist (siehe Kapitel zur Datenbereinigung) oder ein Leerzeichen übrig geblieben ist.

> **Ausblick:** In neueren Excel-Versionen (Microsoft 365) gibt es mit `XVERWEIS` eine modernere, flexiblere Nachfolgefunktion von `SVERWEIS` – u. a. muss die Suchspalte dort nicht mehr zwingend die erste Spalte der Matrix sein. Für den Einstieg reicht `SVERWEIS` aber völlig aus, da es in jeder Excel-Version funktioniert und Sie das Grundprinzip des Nachschlagens ohnehin identisch verstehen müssen.