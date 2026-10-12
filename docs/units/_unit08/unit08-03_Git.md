---
title: Automation
published: true
toc: true
header:
  image: assets/images/unit08/DataSwamp_Stage08.png
  image_description: "Streuobstwiese"
  caption: "Image: ulrichstill [CC BY-SA 2.0 DE] via [wikimedia.org](https://commons.wikimedia.org/wiki/File:Tuebingen_Streuobstwiese.jpg)"
---

Im Kapitel zur Benennung von Dateien haben Sie gelernt, Bearbeitungsstände mit Dateinamen wie `_v01` und `_v02` zu unterscheiden. Das funktioniert, wird aber Scripten schnell unübersichtlich: Es entstehen viele Kopien, und niemand weiß, was sich zwischen `_v02` und `_v03` geändert hat. **Versionskontrolle** löst genau dieses Problem. In diesem Kapitel betrachten Sie, wie das mit dem Programm Git funktioniert.
 
## Was ist Git?
 
**Git** ist ein Programm, das den Verlauf einer Sammlung von Dateien festhält. Zu jedem Zeitpunkt, den Sie festlegen, speichert Git den aktuellen Stand und merkt sich, was sich seit dem letzten Stand geändert hat.
 
- Ein **Repository** ist ein Ordner, dessen Verlauf Git verwaltet.
- Ein **Commit** ist ein gespeicherter Bearbeitungsstand mit einer kurzen Nachricht, einem Datum und dem Namen der Person, die ihn angelegt hat.
- Der **Verlauf** (englisch *log*) ist die Liste aller Commits.
- Eine **Differenz** (englisch *diff*) zeigt, was sich zwischen zwei Ständen geändert hat.
Git ist das Programm auf Ihrem Rechner. GitHub und GitLab sind Plattformen im Netz, auf denen man ein Repository zusätzlich ablegen und mit anderen teilen kann.
 
## Der grundlegende Ablauf
 
```
git init                                  # Ordner zum Repository machen
git status                                # was hat sich geändert?
git add 02_Bearbeitete_Daten/temperatur.csv   # Änderung für den nächsten Commit vormerken
git commit -m "Platzhalter -999 durch leere Zellen ersetzt"   # Stand speichern
git log --oneline                         # Verlauf anzeigen
git diff                                  # Änderungen seit dem letzten Commit anzeigen
```
 
Der Ablauf besteht immer aus denselben Schritten: ändern, vormerken, speichern. Entscheidend ist die **Nachricht** des Commits. Sie sollte kurz sagen, **was** geändert wurde und **warum**. Die Liste der Nachrichten ist dann Ihr Bearbeitungsprotokoll aus dem letzten Kapitel, nur dass es sich fast von selbst schreibt.
 

## Was Git gut kann und was nicht
 
| Git eignet sich gut für | Git eignet sich schlecht für |
|---|---|
| Textdateien: CSV, README, Skripte | Excel-Dateien (`.xlsx`): Git speichert jeden Stand, zeigt aber keine zellenweisen Änderungen |
| nachvollziehbare Bearbeitungsstände | sehr große Dateien, etwa Satellitenbilder |
| Zusammenarbeit mehrerer Personen | als alleinige Datensicherung |
 
**Git ist kein Backup.** Ein Repository, das nur auf einem Rechner liegt, geht mit diesem Rechner verloren. Eine zweite Kopie, etwa auf einer Plattform wie GitLab, hilft, ersetzt aber nicht die Backup-Regel aus dem Kapitel zur Datensicherung.
 