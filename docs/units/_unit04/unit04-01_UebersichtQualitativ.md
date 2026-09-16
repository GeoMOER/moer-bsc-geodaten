

**Überblick über qualitative Daten verschaffen:**

| Frage | Excel-Funktion | Beispiel |
|---|---|---|
| Wie oft kommt jeder Wert vor? | `=ZÄHLENWENN(Bereich;"Marburg")` für einen einzelnen Wert, oder eine kleine Übersichtstabelle mit einer Zeile je Kategorie | „Marburg": 12 Messungen |
| Gibt es unbeabsichtigt mehrere Schreibweisen derselben Kategorie? | Häufigkeitstabelle durchsehen: Tauchen inhaltlich identische Werte mehrfach mit leicht unterschiedlicher Schreibweise auf? | „Marburg" und „marburg" separat gezählt → Hinweis auf Bereinigungsbedarf |

**Praxisbeispiel:** Eine Häufigkeitsübersicht Ihrer Spalte `Messmethode` könnte etwa zeigen: `Thermometer`: 15, `Wetter-App`: 8, `thermometer`: 3. Die drei letzten Einträge gehören inhaltlich zur ersten Kategorie – ohne eine solche Übersicht würde diese Aufteilung unbemerkt bleiben und spätere Auswertungen (z. B. „Wie viele Messungen wurden mit welcher Methode erhoben?") verfälschen.

**Kurzcheck:** Erstellen Sie eine Häufigkeitsübersicht für Ihre Spalte `Messmethode` bzw. `Standortname`. Tauchen darin Kategorien auf, die eigentlich zusammengehören, aber durch uneinheitliche Schreibweise getrennt gezählt werden?
