# Kontrollwerte zum Snapshot vom 08.09.2026

Diese Werte beziehen sich auf genau das bereitgestellte Paket, nicht auf spätere Liveabfragen.

| Schritt | Erwartetes Ergebnis |
|---|---:|
| Schutzgebiete im Basis-GeoPackage | 22 Features: 12 NSG, 10 FFH |
| Gewässer im Basis-GeoPackage | 412 Linienfeatures |
| CSV-Import | 79 Nachweise |
| Unsicherheit > 0 und <= 100 m | 56 Nachweise; 23 ausgeschlossen |
| Schutzgebietsauswahl `kategorie = 'FFH'` | 10 Features |
| Geprüfte Nachweise schneiden ausgewählte FFH-Gebiete | 4 Nachweise |
| Gewässer schneiden ausgewählte FFH-Gebiete | 106 Linienfeatures |
| Punkte nach Höhenabtastung | 56 Features, davon 35 mit Höhe und 21 mit NULL |
| Abschlusskarte: nur gültige Höhenwerte | 35 Features |

Das DGM besitzt 2000 × 2000 Zellen à 10 m. 1.600.200 Zellen enthalten Höhenwerte, 2.399.800 enthalten NoData (-9999). Die gültigen Rasterwerte reichen gerundet von 161,91 bis 414,12 m. Die 35 abgetasteten gültigen Punktwerte reichen gerundet von 178,55 bis 323,90 m.

Die geometrische Auswahl verwendet `intersects` mit den ausgewählten FFH-Geometrien. Ein Punkt in mehreren Gebieten wird nur einmal gezählt. Ein ausgewähltes Gewässerfeature kann nur teilweise im Schutzgebiet liegen. Die Daten sind nicht an der Untersuchungsgrenze abgeschnitten.

Fehlende Höhenwerte entstehen durch die begrenzte DGM-Abdeckung. Sie werden weder als Höhe null ersetzt noch aus dem Ergebnis der Unit 13 entfernt. Erst die kartierte Auswahl der Unit 14 beschränkt sich auf gültige Werte.

`pruefbericht.json` enthält genaue Klassenränder, alle GBIF-IDs mit erwarteten Höhenwerten und die SHA-256-Prüfsummen der Eingangsdaten. In den Beispiellegenden werden Höhen auf eine Nachkommastelle gerundet; die Klassifizierung verwendet die ungerundeten Werte.
