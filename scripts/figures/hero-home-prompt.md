# Startseiten-Heroteaser: Vom Data Swamp zum Data Lake

## Grundlage und Einbindung

- Entwurf: `GeoData_Gamification.pdf` von Lisa Schepers (drei Seiten), vom Kursverantwortlichen als Gestaltungsgrundlage bereitgestellt.
- Umsetzung: integrierte Bildgenerierung (`image_gen`), 15.09.2026.
- Originalausgabe: `docs/assets/images/home/hero-data-swamp-data-lake.png`, 2172 × 724 Pixel, unverändert übernommen.
- Eine zusammenhängende Pixelgrafik mit Sumpf, Netz, Filter, Datenkisten und klarem See mit Kartenebenen. Die Grafik ist eine Metapher, keine Darstellung eines konkreten Datenbestands oder Ortes.
- Titel, Unterzeile und Link sind separat in `docs/index.md` editierbar. Das Startseiten-CSS liegt in `docs/assets/css/course-hero.css` und wird nur bei `course_hero: true` geladen. Bis 900 Pixel Bildschirmbreite stehen die Texte über dem vollständigen Panorama.
- Die PNG-Datei ist ein zusammengeführtes Bild; separate transparente Einzelmotive aus der Ideenskizze wurden in diesem Auftrag nicht erstellt.

## Verwendeter Prompt

```text
Use case: illustration-story.
Create a finished panoramic website hero illustration for a German university introductory geodata course, based on the provided PDF concept (described here). ONE coherent side-scrolling pixel-art panorama, aspect ratio 3:1, ideally 2400 x 800 or 3072 x 1024. Refined 16-bit adventure-game pixel graphics with crisp square pixels, consistent pixel scale, carefully designed silhouettes, restrained detail and beautiful atmospheric colour. This is an educational metaphor: "Vom Data Swamp zum Data Lake". Do NOT put any text or typography inside the image.

Scene: one continuous landscape that transitions from a dark olive-brown data swamp on the left to a sparkling turquoise-blue data lake on the right. Left third: muddy water, twisted bare trees framing the far left edge, tangled cables and a handful of floating disorganised file-sheet symbols, a couple of small yellow warning triangles. The swamp conveys confusion, not horror. Middle: a small wooden jetty and a simple fishing net lifting file-shaped data items from the swamp, then a compact, charming water-filter machine with a visible funnel symbol, transforming murky water into a short clear stream into the lake. Nearby wooden sorting crates bear pictograms only: table grid, raster checkerboard, vector points connected by lines. Right third: clear lake with lush green banks, healthy trees and three elegant floating isometric geographic map layers above the water: terrain raster, line network, green landscape with river and fields. Fine vertical alignment guides connect these three sheets. A small globe and a simple spreadsheet symbol on the dock suggest usable geodata tools.

Composition: full-bleed landscape, no borders, no panels or infographic arrows. Horizon about 40% down. Keep the TOP 35% mostly quiet sky with very little detail, especially top left, to allow website title text added separately. All main data objects fit clearly in lower 60%; no cropped map layers. Dark desaturated cloudy sky at left gradually becomes pale clear sky at right. Broad readable shapes so the story works when scaled down on a website; do not crowd with tiny items. A continuous natural shoreline connects both halves. Pixel art throughout, no photorealism, no smooth 3D rendering, no antialiased vector look, no watermarks, no letters, no logos, no people. Make the filtering and sorting metaphor visible and the result inviting for adult students.
```

