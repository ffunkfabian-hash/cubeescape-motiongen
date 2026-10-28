# Hüftlage – Mündung, Visier, Griff und Körper der Waffe im Ruhebild

Referenzanalyse REF 0.22 „Hipline“ (25.10.2026) für die Waffenreihe **BASIC** (Projekt `cubeescape-ballon`) und Cube Escape:
wo die Waffe in der ruhigen Hüfthaltung im Bild liegt – Mündung, hintere Visieröffnung, Griffhand, Hüllrechteck des Waffenkörpers und
projizierte Neigung, je Waffe und Klasse. Gemessen hat eine Codex-Mac-Sitzung (Auftrag „Ego-Bewegung“, Thema 1, 25.10.2026). Diese Version
hat die Zuarbeit nach dem [Analyse-Standard](standard.md) geprüft, gegen den Bestand abgeglichen und nur Neues übernommen
([8](#8-prüfung-und-zählung)). Hier stehen Beobachtungen und Messwerte; Schlüsse und Startwerte entstehen in BASIC bzw. Cube Escape.
Maschinenlesbare Fassung: [`data/huefte.json`](../data/huefte.json). Getrennte Nachbarthemen: [Visiere](visiere.md) (0.14),
[Waffenproportionen](proportionen.md) (0.15), [Zielbewegung](zielbewegung.md) (0.17), [Mündungsfeuer](muendung.md) (0.19),
[Inspektion](inspektion.md) (0.20). Die übrigen Themen derselben Codex-Zuarbeit (Waffenwechsel, Nachladen, Kamera, Ton, Rutschen) sind hier
**nicht** enthalten und bekommen eigene Versionen.

Destiny 2 hat Vorrang: 28 neue Waffen aus 16 Klassen (der Bestand in [destiny2.md › 3](destiny2.md#3-steckbriefe-je-waffentyp--lage-im-bild-zielpunkt-visier-arme-aktionen-bildvermessung-mit-mittenkreuz-18-oktober-2026--m)
hatte je Klasse meist eine Waffe). Die acht Destiny-Quellvideos mit übernommenen Waffen stehen nach Repo-Regel als Messzeilen in
[destiny2.md › 2](destiny2.md#2-messungen-an-60-fps-aufnahmen-ab-16-oktober-2026--m) (Anker `z-hl-…`).

**Status:** **[M]** am Einzelbild mit 10-%-Raster und Mittenkreuz gemessen; **[O]** Sichtung ohne ruhige Pose; **[C]** Spielerstimme;
**[B]** Entwickler- oder Supportquelle. **Jede Zahl ist das Beispiel einer Waffe** in einer Aufnahme mit unbekanntem FOV, Viewmodel-Einstellung,
Skin und Spielstand – kein Klassenmittel.

## 1. Quellen und Methode

- **Videos:** 19 YouTube-Videos aus 10 Spielen bzw. Fassungen, alle am 25.10.2026 per yt-dlp geprüft (Kanal, Datum, Titel, Länge; alle
  Zeitstempel innerhalb der Länge). Destiny 2: zehn Showcases (Ultraclocked 2020/21, Boosh Ninja 2022/23) bei 60/s. Vergleich: Destiny 1
  (MadladDeluxe, D1-gegen-D2-Video, 29,97/s), Marathon (soda, 04.06.2026), Titanfall 2 (Weapons From Games, 2019), Apex (Cacek47, 2019),
  Halo Infinite (Abyssopelagic, Technical Preview 2021), CoD MW2019 (Tigerfield, 2019), Battlefield 6 (Torbis, **Vorabfassung** 2025),
  Valorant (Skovos, 2020, 29,97/s), The Finals (Game Arsenal, 2025). Liste mit Titeln in `data/huefte.json` › `entries`.
- **Lage:** Prozent der Bildbreite / Bildhöhe, Ursprung oben links, Mitte 50 / 50, **±3 pp**. Mündung = sichtbares Laufende;
  Visier = hintere Öffnung bzw. Okular (kein Ersatz für die Mündung); Griff = rechte Griffhand (Bogen: linke Griffhand).
- **Körper:** Hüllrechteck `[xmin, ymin, xmax, ymax]` des sichtbaren Waffenkörpers mit Optik, ohne Arme. Es ist **keine verdeckte
  Pixelfläche** (Bogenlöcher und Zwischenräume zeigen Welt); wo es bis 100 reicht, schneidet der Bildrand ab und die Größe ist eine Untergrenze.
- **Neigung:** „Lauf“ = projizierte Lauflinie, „Kante“ = sichtbare Gehäuse- oder Mantelkante, wenn der Lauf verdeckt ist; 0° = waagerecht
  nach links, positiv = nach links oben, 2D-Winkel auf 16:9, **±10°** (kurze Läufe ±15°). Keine 3D-Achse.
- **Ruhepose:** Codex hat je Waffe ein Bild gewählt, dessen Nachbarbilder dieselbe Lage zeigen (keine Zieh-, Nachlade- oder Rückstoßphase).
  30/s-Quellen liefern nur Lage, keine Zeiten. Gehen-Bob ist nicht gemessen.
- **Vergleichsspiele** stehen wie in 0.19/0.20 nur hier und in `data/clips.json`, nicht als Messzeilen in den Spiel-Docs: Destiny 1, Marathon,
  Halo, CoD, Battlefield, Valorant und The Finals haben kein eigenes Doc; Titanfall 2 bekommt einen Hinweis im Steckbrief, Apex nicht
  (dort nur R-99, hier R-301 – kein Widerspruch).
- **Nicht übernommen:** das Codex-Feld `convergence` (nur 50 minus Mündungswert, keine Konvergenz oder Flugbahn) und die je Zeile kopierten
  Bewertungstexte – die Bewertung steht je Spiel in [5](#5-bewertung-gut-nicht-so-gut-für-wen).
- **Unbekannt = null:** fehlende Mündung, Griffhand oder Neigung heißt verdeckt oder ohne sichere Landmarke, nie Nullversatz.

## 2. Messtabelle

Spalten in % B / % H; Körper als „x-Bereich × y-Bereich“. Nur übernommene Zeilen; Doppelungen und Verworfenes stehen in [3](#3-abgleich-mit-dem-bestand).

### Destiny 2

| Waffe (Klasse) | Quelle | Zeit | Mündung | Visier | Griff | Körper (B × H) | Neigung | Hinweis |
|---|---|---|---|---|---|---|---|---|
| **A Single Clap** (Scharfschützengewehr) <a id="hl-destiny-2-a-single-clap"></a> | Ultraclocked, [IG-GZ72Vbi0](https://www.youtube.com/watch?v=IG-GZ72Vbi0) | 0:06,000 | 56 / 68 | 70 / 54 | – | 55–100 × 44–100 | Kante 40° | – |
| **Annual Skate** (Handfeuerwaffe) <a id="hl-destiny-2-annual-skate"></a> | Ultraclocked, [IG-GZ72Vbi0](https://www.youtube.com/watch?v=IG-GZ72Vbi0) | 1:19,500 | 57 / 63 | 64 / 66 | 67 / 87 | 55–70 × 60–84 | Kante 35° | Codex-Eigenprüfung |
| **Dead Man Walking** (Sidearm) <a id="hl-destiny-2-dead-man-walking"></a> | Ultraclocked, [IG-GZ72Vbi0](https://www.youtube.com/watch?v=IG-GZ72Vbi0) | 1:41,000 | 57 / 64 | 66 / 71 | 67 / 87 | 56–71 × 60–84 | Kante 35° | – |
| **First In, Last Out** (Schrotflinte) <a id="hl-destiny-2-first-in-last-out"></a> | Ultraclocked, [IG-GZ72Vbi0](https://www.youtube.com/watch?v=IG-GZ72Vbi0) | 2:16,000 | 57 / 63 | 66 / 68 | – | 56–83 × 60–100 | Kante 35° | – |
| **Foggy Notion** (Maschinenpistole) <a id="hl-destiny-2-foggy-notion"></a> | Ultraclocked, [IG-GZ72Vbi0](https://www.youtube.com/watch?v=IG-GZ72Vbi0) | 3:05,000 | 57 / 67 | 72 / 67 | – | 56–100 × 60–100 | – | – |
| **Hoosegow** (Raketenwerfer) <a id="hl-destiny-2-hoosegow"></a> | Ultraclocked, [IG-GZ72Vbi0](https://www.youtube.com/watch?v=IG-GZ72Vbi0) | 3:46,200 | – | 65 / 68 | – | 60–100 × 0–100 | – | – |
| **Nox Echo III** (kurzes Fusionsgewehr) <a id="hl-destiny-2-nox-echo-iii"></a> | Ultraclocked, [IG-GZ72Vbi0](https://www.youtube.com/watch?v=IG-GZ72Vbi0) | 4:50,000 | 59 / 68 | 71 / 68 | – | 58–100 × 63–100 | Kante 40° | – |
| **Solemn Hymn** (Automatikgewehr) <a id="hl-destiny-2-solemn-hymn"></a> | Ultraclocked, [IG-GZ72Vbi0](https://www.youtube.com/watch?v=IG-GZ72Vbi0) | 5:21,000 | 57 / 69 | 77 / 57 | – | 57–100 × 56–100 | – | – |
| **Swift Ride** (Impulsgewehr) <a id="hl-destiny-2-swift-ride"></a> | Ultraclocked, [IG-GZ72Vbi0](https://www.youtube.com/watch?v=IG-GZ72Vbi0) | 5:55,000 | 59 / 67 | 73 / 55 | – | 58–100 × 49–100 | Kante 40° | – |
| **Bad News** (Handfeuerwaffe) <a id="hl-destiny-2-bad-news"></a> | Ultraclocked, [73lGCT7yOtk](https://www.youtube.com/watch?v=73lGCT7yOtk) | 0:08,000 | 54 / 69 | 62 / 62 | 67 / 89 | 53–70 × 59–84 | Kante 30° | – |
| **Belfry Bounty** (Scharfschützengewehr) <a id="hl-destiny-2-belfry-bounty"></a> | Ultraclocked, [73lGCT7yOtk](https://www.youtube.com/watch?v=73lGCT7yOtk) | 0:54,000 | 56 / 66 | 81 / 73 | – | 55–100 × 58–100 | Lauf 30° | – |
| **Call to Serve** (Scoutgewehr) <a id="hl-destiny-2-call-to-serve"></a> | Ultraclocked, [73lGCT7yOtk](https://www.youtube.com/watch?v=73lGCT7yOtk) | 1:44,000 | 58 / 61 | 72 / 52 | – | 56–100 × 47–100 | Kante 35° | – |
| **Eystein-D** (Impulsgewehr) <a id="hl-destiny-2-eystein-d"></a> | Ultraclocked, [73lGCT7yOtk](https://www.youtube.com/watch?v=73lGCT7yOtk) | 3:46,000 | 58 / 64 | 74 / 55 | – | 57–100 × 50–100 | Kante 35° | – |
| **Flash and Thunder** (Granatwerfer) <a id="hl-destiny-2-flash-and-thunder"></a> | Ultraclocked, [73lGCT7yOtk](https://www.youtube.com/watch?v=73lGCT7yOtk) | 4:27,000 | 58 / 67 | 66 / 55 | – | 57–95 × 43–100 | Lauf 35° | eigene Bildprüfung ≈ 58 / 64–68 |
| **Minimum Distance** (Sidearm) <a id="hl-destiny-2-minimum-distance"></a> | Ultraclocked, [73lGCT7yOtk](https://www.youtube.com/watch?v=73lGCT7yOtk) | 6:55,000 | 59 / 67 | 66 / 73 | 67 / 88 | 58–70 × 64–84 | Kante 35° | – |
| **New City** (Maschinenpistole) <a id="hl-destiny-2-new-city"></a> | Ultraclocked, [73lGCT7yOtk](https://www.youtube.com/watch?v=73lGCT7yOtk) | 7:36,000 | 56 / 71 | 63 / 57 | – | 54–87 × 54–100 | Kante 40° | – |
| **Scathelocke** (Automatikgewehr) <a id="hl-destiny-2-scathelocke"></a> | Ultraclocked, [73lGCT7yOtk](https://www.youtube.com/watch?v=73lGCT7yOtk) | 8:24,000 | 59 / 71 | 70 / 66 | – | 57–90 × 61–100 | Lauf 40° | – |
| **Berenger's Memory** (Granatwerfer) <a id="hl-destiny-2-berengers-memory"></a> | Ultraclocked, [afs_dhFDhQU](https://www.youtube.com/watch?v=afs_dhFDhQU) | 0:44,000 | 56 / 63 | 90 / 63 | – | 54–100 × 54–100 | – | – |
| **Man O' War** (Lineares Fusionsgewehr) <a id="hl-destiny-2-man-o-war"></a> | Ultraclocked, [afs_dhFDhQU](https://www.youtube.com/watch?v=afs_dhFDhQU) | 2:50,000 | 58 / 69 | 73 / 57 | – | 57–100 × 49–100 | Kante 30° | – |
| **Tarantula** (Lineares Fusionsgewehr) <a id="hl-destiny-2-tarantula"></a> | Ultraclocked, [afs_dhFDhQU](https://www.youtube.com/watch?v=afs_dhFDhQU) | 3:31,000 | 58 / 68 | 73 / 60 | – | 57–100 × 51–100 | Kante 30° | – |
| **Blue Shift** (Raketenwerfer) <a id="hl-destiny-2-blue-shift"></a> | Ultraclocked, [afs_dhFDhQU](https://www.youtube.com/watch?v=afs_dhFDhQU) | 1:28,500 | – | 68 / 57 | – | 60–100 × 17–100 | – | – |
| **Hammerhead** (Maschinengewehr) <a id="hl-destiny-2-hammerhead"></a> | Ultraclocked, [oauUQuhlwGs](https://www.youtube.com/watch?v=oauUQuhlwGs) | 0:55,000 | 56,2 / 64 | 65,9 / 48,2 | – | 47,9–100 × 43,5–100 | – | – |
| **Coldheart** (Spurgewehr) <a id="hl-destiny-2-coldheart"></a> | Boosh Ninja, [WgBf7P6wzCE](https://www.youtube.com/watch?v=WgBf7P6wzCE) | 0:02,002 | – | – | – | 56,2–100 × 48,5–100 | – | – |
| **Imperial Needle** (Bogen) <a id="hl-destiny-2-imperial-needle"></a> | Ultraclocked, [dKNTDzi__Qo](https://www.youtube.com/watch?v=dKNTDzi__Qo) | 0:47,000 | – | 57,3 / 75,2 | 46,6 / 84,8 | 7,6–100 × 68,6–100 | – | – |
| **The Spiteful Fang** (Bogen) <a id="hl-destiny-2-the-spiteful-fang"></a> | Ultraclocked, [oauUQuhlwGs](https://www.youtube.com/watch?v=oauUQuhlwGs) | 4:32,000 | – | 58,2 / 78 | 46,6 / 85,6 | 5,2–100 × 68,9–100 | – | – |
| **Lubrae's Ruin** (Glefe) <a id="hl-destiny-2-lubraes-ruin"></a> | Boosh Ninja, [O9QEU2RzB28](https://www.youtube.com/watch?v=O9QEU2RzB28) | 2:23,002 | – | – | 73 / 92,4 | 46–74,5 × 45,3–100 | – | – |
| **Nezarec's Whisper** (Glefe) <a id="hl-destiny-2-nezarecs-whisper"></a> | Boosh Ninja, [1pH6zS-lj5g](https://www.youtube.com/watch?v=1pH6zS-lj5g) | 3:54,002 | – | – | – | 52,3–83 × 50–100 | – | – |
| **Hollow Denial** (Spurgewehr) <a id="hl-destiny-2-hollow-denial"></a> | Boosh Ninja, [1pH6zS-lj5g](https://www.youtube.com/watch?v=1pH6zS-lj5g) | 6:25,002 | 57,7 / 59,6 | 66,9 / 45,6 | – | 56,9–100 × 40–100 | – | – |

### Destiny 1

| Waffe (Klasse) | Quelle | Zeit | Mündung | Visier | Griff | Körper (B × H) | Neigung | Hinweis |
|---|---|---|---|---|---|---|---|---|
| **Hand Cannon (Modellname nicht eingeblendet)** (Handfeuerwaffe) <a id="hl-destiny-1-hand-cannon"></a> | MadladDeluxe, [lTMKIvPrJZc](https://www.youtube.com/watch?v=lTMKIvPrJZc) | 0:24,992 | – | 62 / 61 | 61 / 81 | 54–67 × 57–78 | – | 30/s – nur Lage |
| **Pulse Rifle (Modellname nicht eingeblendet)** (Impulsgewehr) <a id="hl-destiny-1-pulse-rifle"></a> | MadladDeluxe, [lTMKIvPrJZc](https://www.youtube.com/watch?v=lTMKIvPrJZc) | 0:54,988 | 56 / 65 | 70 / 59 | – | 55–100 × 54–100 | – | 30/s – nur Lage; Bildprüfung ok |
| **Auto Rifle (Modellname nicht eingeblendet)** (Automatikgewehr) <a id="hl-destiny-1-auto-rifle"></a> | MadladDeluxe, [lTMKIvPrJZc](https://www.youtube.com/watch?v=lTMKIvPrJZc) | 1:22,015 | – | 75 / 51 | – | 58–100 × 47–100 | – | 30/s – nur Lage |
| **Scout Rifle (Modellname nicht eingeblendet)** (Scoutgewehr) <a id="hl-destiny-1-scout-rifle"></a> | MadladDeluxe, [lTMKIvPrJZc](https://www.youtube.com/watch?v=lTMKIvPrJZc) | 1:48,008 | – | 71 / 47 | – | 57–100 × 40–100 | – | 30/s – nur Lage |
| **Sniper Rifle (Modellname nicht eingeblendet)** (Scharfschützengewehr) <a id="hl-destiny-1-sniper-rifle"></a> | MadladDeluxe, [lTMKIvPrJZc](https://www.youtube.com/watch?v=lTMKIvPrJZc) | 2:13,000 | 54 / 65 | 74 / 54 | – | 54–100 × 45–100 | – | 30/s – nur Lage |
| **Shotgun (Modellname nicht eingeblendet)** (Schrotflinte) <a id="hl-destiny-1-shotgun"></a> | MadladDeluxe, [lTMKIvPrJZc](https://www.youtube.com/watch?v=lTMKIvPrJZc) | 2:30,984 | 55 / 64 | 75 / 69 | – | 55–100 × 60–100 | Lauf 26,2° | 30/s – nur Lage |
| **Fusion Rifle (Modellname nicht eingeblendet)** (Fusionsgewehr) <a id="hl-destiny-1-fusion-rifle"></a> | MadladDeluxe, [lTMKIvPrJZc](https://www.youtube.com/watch?v=lTMKIvPrJZc) | 3:02,015 | 61 / 72 | 73 / 65 | – | 60–100 × 59–100 | – | 30/s – nur Lage |
| **Rocket Launcher (Modellname nicht eingeblendet)** (Raketenwerfer) <a id="hl-destiny-1-rocket-launcher"></a> | MadladDeluxe, [lTMKIvPrJZc](https://www.youtube.com/watch?v=lTMKIvPrJZc) | 3:15,996 | – | 65 / 57 | – | 56–100 × 27–100 | – | 30/s – nur Lage |
| **Machine Gun (Modellname nicht eingeblendet)** (Maschinengewehr) <a id="hl-destiny-1-machine-gun"></a> | MadladDeluxe, [lTMKIvPrJZc](https://www.youtube.com/watch?v=lTMKIvPrJZc) | 3:30,010 | – | 67 / 50 | – | 54–100 × 45–100 | – | 30/s – nur Lage |

### Marathon (2026)

| Waffe (Klasse) | Quelle | Zeit | Mündung | Visier | Griff | Körper (B × H) | Neigung | Hinweis |
|---|---|---|---|---|---|---|---|---|
| **CE Tactical Sidearm** (Pistole) <a id="hl-marathon-ce-tactical-sidearm"></a> | soda, [QxZAflLtJRQ](https://www.youtube.com/watch?v=QxZAflLtJRQ) | 0:08,000 | – | 60 / 54 | 64 / 77 | 57–69 × 51–72 | – | – |
| **V11 Punch** (Pistole) <a id="hl-marathon-v11-punch"></a> | soda, [QxZAflLtJRQ](https://www.youtube.com/watch?v=QxZAflLtJRQ) | 0:35,500 | – | 59 / 52 | 65 / 83 | 56–69 × 49–79 | – | – |
| **Bully SMG** (Maschinenpistole) <a id="hl-marathon-bully-smg"></a> | soda, [QxZAflLtJRQ](https://www.youtube.com/watch?v=QxZAflLtJRQ) | 1:53,000 | 58 / 66 | 66 / 50 | – | 58–100 × 46–100 | – | – |
| **V22 Volt Thrower** (Maschinenpistole) <a id="hl-marathon-v22-volt-thrower"></a> | soda, [QxZAflLtJRQ](https://www.youtube.com/watch?v=QxZAflLtJRQ) | 2:19,000 | – | 60 / 58 | – | 55–80 × 52–100 | – | – |
| **WSTR Combat Shotgun** (Schrotflinte) <a id="hl-marathon-wstr-combat-shotgun"></a> | soda, [QxZAflLtJRQ](https://www.youtube.com/watch?v=QxZAflLtJRQ) | 3:56,000 | 56 / 59 | 71 / 58 | 70 / 87 | 55–82 × 55–100 | – | Bildprüfung Δ bis 4 pp (Grenzfall) |
| **Misriah 2442** (Schrotflinte) <a id="hl-marathon-misriah-2442"></a> | soda, [QxZAflLtJRQ](https://www.youtube.com/watch?v=QxZAflLtJRQ) | 4:30,000 | 57 / 65 | 75 / 67 | – | 55–100 × 59–100 | – | – |
| **M77 Assault Rifle** (Automatikgewehr) <a id="hl-marathon-m77-assault-rifle"></a> | soda, [QxZAflLtJRQ](https://www.youtube.com/watch?v=QxZAflLtJRQ) | 5:34,500 | – | 71 / 57 | – | 55–100 × 51–100 | – | – |
| **Demolition HMG** (Maschinengewehr) <a id="hl-marathon-demolition-hmg"></a> | soda, [QxZAflLtJRQ](https://www.youtube.com/watch?v=QxZAflLtJRQ) | 8:13,500 | – | 65 / 59 | – | 50–94 × 53–100 | – | – |
| **Longshot** (Scharfschützengewehr) <a id="hl-marathon-longshot"></a> | soda, [QxZAflLtJRQ](https://www.youtube.com/watch?v=QxZAflLtJRQ) | 12:10,000 | 55 / 59 | 84 / 66 | – | 54–100 × 37–100 | – | – |

### Titanfall 2

| Waffe (Klasse) | Quelle | Zeit | Mündung | Visier | Griff | Körper (B × H) | Neigung | Hinweis |
|---|---|---|---|---|---|---|---|---|
| **CAR** (Maschinenpistole) <a id="hl-titanfall-2-car"></a> | Weapons From Games, [4sDwTD9U8bw](https://www.youtube.com/watch?v=4sDwTD9U8bw) | 1:28,000 | 56 / 65 | 72 / 57 | – | 55–100 × 50–100 | – | Bildprüfung Mündung Δy 3–4 pp (Grenzfall) |
| **R-201 Carbine** (Automatikgewehr) <a id="hl-titanfall-2-r-201-carbine"></a> | Weapons From Games, [4sDwTD9U8bw](https://www.youtube.com/watch?v=4sDwTD9U8bw) | 2:43,300 | 55 / 65 | 74 / 68 | – | 54–100 × 55–100 | – | – |

### Apex Legends

| Waffe (Klasse) | Quelle | Zeit | Mündung | Visier | Griff | Körper (B × H) | Neigung | Hinweis |
|---|---|---|---|---|---|---|---|---|
| **R-301** (Automatikgewehr) <a id="hl-apex-legends-r-301"></a> | Cacek47, [R-BGChzYGpo](https://www.youtube.com/watch?v=R-BGChzYGpo) | 0:39,500 | – | 71 / 69 | – | 54–100 × 58–100 | – | – |

### Halo Infinite

| Waffe (Klasse) | Quelle | Zeit | Mündung | Visier | Griff | Körper (B × H) | Neigung | Hinweis |
|---|---|---|---|---|---|---|---|---|
| **MA40 Assault Rifle** (Automatikgewehr) <a id="hl-halo-infinite-ma40-assault-rifle"></a> | Abyssopelagic, [ZfNuA5r-470](https://www.youtube.com/watch?v=ZfNuA5r-470) | 0:06,000 | 61 / 67 | 73 / 61 | – | 60–100 × 51–100 | – | – |
| **BR75** (Impulsgewehr) <a id="hl-halo-infinite-br75"></a> | Abyssopelagic, [ZfNuA5r-470](https://www.youtube.com/watch?v=ZfNuA5r-470) | 0:49,000 | 61 / 65 | 80 / 47 | – | 60–100 × 38–100 | – | Bildprüfung < 1 pp |

### Call of Duty: Modern Warfare (2019)

| Waffe (Klasse) | Quelle | Zeit | Mündung | Visier | Griff | Körper (B × H) | Neigung | Hinweis |
|---|---|---|---|---|---|---|---|---|
| **X16** (Pistole) <a id="hl-call-of-duty-modern-warfare-x16"></a> | Tigerfield, [_KTdg4YM1fQ](https://www.youtube.com/watch?v=_KTdg4YM1fQ) | 0:04,000 | – | 54 / 73 | 55 / 90 | 51–60 × 69–91 | – | Visier unsicher (Bildprüfung eher 52 / 78–80) |
| **1911** (Pistole) <a id="hl-call-of-duty-modern-warfare-1911"></a> | Tigerfield, [_KTdg4YM1fQ](https://www.youtube.com/watch?v=_KTdg4YM1fQ) | 0:32,000 | – | 52 / 78 | 53 / 92 | 49–57 × 74–95 | – | – |

### Battlefield 6 (pre-launch build)

| Waffe (Klasse) | Quelle | Zeit | Mündung | Visier | Griff | Körper (B × H) | Neigung | Hinweis |
|---|---|---|---|---|---|---|---|---|
| **B36A4** (Automatikgewehr) <a id="hl-battlefield-6-b36a4"></a> | Torbis, [ROUP1z62caA](https://www.youtube.com/watch?v=ROUP1z62caA) | 0:41,200 | 54 / 59 | 66,5 / 71 | – | 53–82 × 57–100 | – | Bildprüfung ok |
| **AK4D** (Automatikgewehr) <a id="hl-battlefield-6-ak4d"></a> | Torbis, [ROUP1z62caA](https://www.youtube.com/watch?v=ROUP1z62caA) | 0:42,200 | 54 / 58 | 66 / 63 | – | 53–84 × 51–100 | – | – |

### Valorant

| Waffe (Klasse) | Quelle | Zeit | Mündung | Visier | Griff | Körper (B × H) | Neigung | Hinweis |
|---|---|---|---|---|---|---|---|---|
| **Classic** (Pistole) <a id="hl-valorant-classic"></a> | Skovos, [WH5xpA7tfY8](https://www.youtube.com/watch?v=WH5xpA7tfY8) | 1:22,015 | – | 72 / 66 | 72 / 84 | 63–76 × 59–79 | – | 30/s – nur Lage; Bildprüfung ok |
| **Bulldog** (Automatikgewehr) <a id="hl-valorant-bulldog"></a> | Skovos, [WH5xpA7tfY8](https://www.youtube.com/watch?v=WH5xpA7tfY8) | 5:53,286 | 57 / 57 | 76 / 64 | – | 56–100 × 53–100 | – | [O] bewegt, keine Ruhepose; 30/s – nur Lage |

### The Finals

| Waffe (Klasse) | Quelle | Zeit | Mündung | Visier | Griff | Körper (B × H) | Neigung | Hinweis |
|---|---|---|---|---|---|---|---|---|
| **M26 Matter** (Schrotflinte) <a id="hl-the-finals-m26-matter"></a> | Game Arsenal, [1QFjDZBh3GE](https://www.youtube.com/watch?v=1QFjDZBh3GE) | 0:35,300 | 55,5 / 64,5 | 67,5 / 66 | – | 55–100 × 60–100 | – | Bildprüfung ok |

## 3. Abgleich mit dem Bestand

| Waffe | Bestand | Codex | Entscheidung |
|---|---|---|---|
| Tone Patrol (Scout) | [destiny2.md › 3](destiny2.md#3-steckbriefe-je-waffentyp--lage-im-bild-zielpunkt-visier-arme-aktionen-bildvermessung-mit-mittenkreuz-18-oktober-2026--m): Mündung 57 / 63, Körper 56–100 × 57–100 | 57 / 65, 56–100 × 57–100 | **verworfen** – Doppelung (Δ ≤ 2 pp) |
| Cartesian Coordinate (kurze Fusion) | Mündung 58 / 66, Körper 57–100 × 60–100 | 58 / 67, 57–100 × 60–100 | **verworfen** – Doppelung |
| Hawthorne's Field-Forged Shotgun | Mündung 58 / 66, Körper 50–95 × 63–100 | 58 / 64, 57–96 × 60–100; Lauf 40° | **verworfen** – Doppelung; neu nur die projizierte Laufneigung ≈ 40° (±10°) |
| Shattered Cipher (MG) | Mündung 56 / 54, Körper 46–100 × 38–100, Optik 63–72 × 38–48 | 56 / 55, 46–100 × 36–100, Visier 66 / 40 | **verworfen** – Doppelung |
| Prometheus Lens (Spurgewehr) | Mündung 57 / 60, Körper 56–100 × 57–100 | Mündung **61,7 / 68,9**, Körper 56–100 × 59–100 | **verworfen** – Codex-Mündung am Bild widerlegt (Nachprüfung ≈ 57 / 61, 4,0 s); Bestand gilt |
| Flash and Thunder (Granatwerfer) | Steckbriefzeile „Granatwerfer Spezial“ nannte Mündung 57 / 54 für Ignition Code **und** Flash and Thunder | 58 / 67, Körper 57–95 × 43–100 | **übernommen**; 57 / 54 stammt aus der Ignition-Code-Zeile in [destiny2.md › 2](destiny2.md#2-messungen-an-60-fps-aufnahmen-ab-16-oktober-2026--m) – Steckbrief präzisiert, eigene Bildprüfung ≈ 58 / 64–68 |
| Negative Space, Unspoken Promise (Schwerter) | Schulteransicht bekannt (Steckbrief „Schwert“) | nur „nicht anwendbar“ | **verworfen** – kein Ego-Wert |
| Titanfall 2 Gewehr | [titanfall2.md › 3](titanfall2.md#3-steckbrief--lage-im-bild-zielpunkt-bewegung--m): Twitch-Spielclip, **klein und tief**, Körper 35–60 × 65–100, Mündung 45 / 68 | Showcase CAR / R-201: Körper 55–100 × 50–100 bzw. 54–100 × 55–100, Mündung 56 / 65 bzw. 55 / 65 | **beide stehen lassen** – andere Waffe, andere Aufnahme; FOV und Viewmodel-Einstellung unbekannt |

Valorant Bulldog (Skovos, 5:53,286) bleibt **offen**: Kamera dreht, Waffe schwingt, keine ruhige Grundpose ([O], Zahlen nur als Sichtungsanker in der Tabelle).

## 4. Muster

- **Destiny 2, lange Waffen:** Die Mündung liegt in allen 21 Destiny-Beispielen mit sichtbarer Mündung **rechts unter der Mitte** bei
  x 54–59 / y ≈ 60–71 % – Showcase-Modelle bei fester Kamera. Die PvP-Twitch-Zeile des Bestands mit Mündung weit links oben
  (langes Gewehr ≈ 28 / 28) ist ein anderes Modell bei unbekanntem FOV; die neuen Zeilen ersetzen sie nicht.
- **Höhe der Kontur:** Die Oberkante liegt bei sechs großen Waffen bei y ≤ 45 % – Hoosegow 0 (ganze Bildhöhe), Blue Shift 17, Hollow Denial 40,
  Flash and Thunder 43, Hammerhead 43,5, A Single Clap 44 –, bei Coldheart, Berenger's Memory und Belfry Bounty bei 48–58 %; Handfeuerwaffen und Sidearms bleiben kompakt bei x 53–71 × y 59–84 %.
- **Visier gegen Mündung:** Die hintere Visieröffnung liegt in 13 von 21 Destiny-Paaren 5–16 pp höher und in allen 21 Paaren 7–34 pp weiter rechts
  (Median 12) als die Mündung, in 3 gleich hoch, in 5 Paaren 3–7 pp tiefer. Das Visier ist kein Ersatz für die Mündung.
- **Griffhand:** sichtbar in 14 von 57 Beispielen, fast nur bei kompakten Waffen und Bögen (Ausnahmen: Marathon-Schrotflinte WSTR,
  Glefe Lubrae's Ruin); bei Schrot, MP und langen Waffen verdeckt sonst das Gehäuse die rechte Hand, sichtbar ist die linke Stützhand.
- **Sonderformen:** Bögen liegen quer im unteren Bild (x 5–100 × y 69–100 %), Mündung und Lauf n. a.; Glefen bleiben Ego, die Spitze ist
  kein Mündungsersatz; Schwerter wechseln in die dritte Person. Glefen-Hüfte nachgemessen, Schuss, Schlag und Schild in
  [nahkampf.md › 6](nahkampf.md#6-destiny-glefe-in-der-ego-sicht) (0.29; Nezarec-Rand 83 gilt mit Ärmel, Waffe allein ≈ 77).
- **Vergleichsspiele:** Mündungen x 54–61 / y 58–67 % (Titanfall, Halo, BF6, Finals). CoD-MW2019- und Valorant-Pistolen liegen am tiefsten
  (Körper ab y 59–74 %), die CoD-Pistolen zugleich am mittigsten (x 49–60 %). Halo BR75 reicht bis y 38 %, MA40 bis 51 %.

## 5. Bewertung: gut, nicht so gut, für wen

Eigene Einschätzungen der Codex-Sitzung aus den Messzeilen, keine Spielerprobung. Spielerquellen [C] sind Reddit-Threads; bei der Abnahme
war Reddit nicht abrufbar, ihr Inhalt ist **nicht nachgeprüft** (Liste und Zitate in `data/huefte.json` › `player_sources`).

| Spiel | Gegenstand | Gut (warum) | Nicht so gut (warum) | Für wen | Belege | Spielerstimmen | Entwickler / Fach |
|---|---|---|---|---|---|---|---|
| Destiny 2 | kompakte Handfeuerwaffe gegen hohe schwere Modelle und breiten Bogen | sehr verschiedene Konturen machen Waffenfamilien leicht unterscheidbar (Annual Skate tief und kompakt, Imperial Needle breit im unteren Bild) | Hoosegow füllt rechts die ganze Bildhöhe, Shattered Cipher reicht bis ≈ 38 % H über die Mitte (Bestand) – Sicht nach rechts muss eigens geprüft werden | Orientierung und Zielsuche, PvE und PvP; Anfänger profitieren von klarer Silhouette | [M] Annual Skate, Hoosegow, Imperial Needle | [C] zwei Threads (15. und 21.10.2024) zu zu großen Modellen seit Echoes, Wunsch nach tieferen oder einstellbaren Modellen – **dieselbe Woche, dasselbe Update, nicht unabhängig wiederkehrend**; Gegenstimme: „sehe trotzdem gut“ | [B] Bungie 15.10.2020: FOV-Regler für neue Konsolen (Welt-FOV, kein Modellregler; nicht abrufbar bei der Abnahme) |
| Destiny 1 | Handfeuerwaffe gegen Scout- und Werferkontur | kleine rechte Kontur der Handfeuerwaffe | Scout und Werfer reichen viel höher; eine gemeinsame Standardgröße würde das verdecken | Gestaltung kompakter und schwerer Waffen | [M] Handfeuerwaffe 0:24,992, Scout 1:48,008 | keine | keine |
| Marathon (2026) | kleine Pistole gegen hohes Langwaffenmodell | Pistole kompakt, ruhige Ausgangskontur | Longshot bis 37 % H, Okular weit rechts | Erkundung und Gegnerwahrnehmung | [M] CE Tactical Sidearm, Longshot | [C] Einzelstimme 06.06.2026: Bild eng trotz hohem FOV, Wunsch nach Waffen-FOV-Regler; keine Gegenstimme | keine |
| Titanfall 2 | CAR und R-201 | Konturen unterhalb bzw. an der Bildmitte | am Rand abgeschnitten, Mündungsrichtung unsicher | Vergleich von Gewehrformen | [M] CAR 1:28, R-201 2:43,3 | keine | keine |
| Apex Legends | R-301 | Kontur unter 58 % H rechts der Mitte | ein Beispiel; mehr Welt-FOV macht ferne Ziele kleiner | Nah- gegen Fernorientierung | [M] R-301 0:39,5 | [C] ein Thread 2026, gegensätzliche FOV-Vorlieben (Weite gegen Fischauge) | [B] EA Help: FOV-Zielkonflikt (Welt-FOV, kein Modell; nicht abrufbar) |
| Halo Infinite | MA40 gegen BR75 | klare obere Konturen; Waffenlage im Spiel einstellbar | BR75 bis 38 % H statt 51 % der MA40 | Spieler mit eigener Vorliebe für sichtbare Waffe | [M] MA40 0:06, BR75 0:49 | [C] ein Thread 2023: Offsets weit aus dem Bild gegen „merkwürdig“, kein Konsens | [B] Halo Support: horizontale, vertikale und Tiefen-Offsets je Waffenklasse (nicht abrufbar) |
| CoD MW2019 | X16 und 1911 | tief und mittig, viel freier Bildraum oben | kleine Silhouette belegt keine gute Mündungserkennbarkeit | PC-Spieler mit weitem Weltblick; kompakte BASIC-Pistolen | [M] X16 0:04, 1911 0:32 | [C] Einzelstimme 2019: Wunsch nach Modell-FOV getrennt vom Welt-FOV | [B] Activision 25.10.2019: Welt-FOV und ADS-FOV getrennt (bestätigt) – kein Modellregler |
| Battlefield 6 (Vorabfassung) | B36A4 und AK4D | Gehäuse enden vor dem rechten Rand | Vorabstand, zwei Beispiele | Vergleich langer Gewehre | [M] B36A4 0:41,2, AK4D 0:42,2 | keine | keine |
| Valorant | Classic (Bulldog nur [O]) | kompakte abgegrenzte Kontur | Bulldog ohne ruhige Pose | Klarheit der Form für neue Spieler | [M] Classic 1:22,015 | keine | keine |
| The Finals | M26 Matter | Pose unter 60 % H, obere Hälfte frei | rechts/unten abgeschnitten, ein Beispiel | Spieler mit Vorliebe für Nähe oder Übersicht | [M] M26 Matter 0:35,3 | [C] Einzelstimme 2024: Modell zu nah, Regler gewünscht; Gegenstimme: so hält man eine Waffe | keine |

### E2 – Lehren für BASIC und Cube Escape (Vorschlag, dort entscheiden)

- **übernehmen:** je Waffenfamilie eine klar lesbare Silhouette; Hüft-Grundpose nur an ruhigen Nachbarbildern beurteilen (Annual Skate,
  CE Tactical Sidearm, R-301).
- **vermeiden:** Hüllrechteckfläche als Verdeckungsanteil ausgeben – dafür braucht es eine Silhouettenmaske; große Waffen nicht allein über
  hohe, nach innen ragende Gehäuse schwer wirken lassen (Hoosegow, Shattered Cipher).
- **testen:** Waffenlage je Waffengruppe horizontal, vertikal und in der Tiefe einstellbar (Halo-Offsets [B]); Welt-FOV und Waffenprojektion
  als getrennte Größen auf schmalem und breitem Seitenverhältnis abnehmen; Lesbarkeit und Verdeckung mit verschiedenen Spielern prüfen,
  statt eine Pose für alle festzulegen. Destiny-Prozentwerte nicht als universelle Startwerte kopieren.

## 6. Für Cube Escape

Cube Escape vergleicht seine Hüftposen am besten gegen die Destiny-Showcase-Zeilen (feste Kamera, 60/s): Mündung, Visier und Körper je Klasse
stehen in [2](#2-messtabelle). Werte gelten mit unbekanntem FOV; ein Vergleich braucht eine eigene Aufnahme mit bekanntem FOV
(Messplan BASIC). Keine Startwerte hier.

## 7. Offen und nicht messbar

- **Lücken je Feld:** Mündung fehlt bei 21 von 57 übernommenen Beispielen (Werfer, Bögen, Glefen, viele Marathon- und D1-Waffen), Griffhand bei 43,
  projizierte Laufneigung bei 53 (nur Belfry Bounty 30°, Flash and Thunder 35°, Scathelocke 40°, D1-Schrotflinte 26°; dazu Kantenwinkel).
  Armanteil nur als Hüllrechteck der sichtbaren Hand, kein anatomischer Anteil.
- **Gehen-Bob:** nicht gemessen; der Bestand hat keinen D2-Gehbeleg ([destiny2.md › 3](destiny2.md#3-steckbriefe-je-waffentyp--lage-im-bild-zielpunkt-visier-arme-aktionen-bildvermessung-mit-mittenkreuz-18-oktober-2026--m)).
- **Je Klasse nur ein Beispiel** bei Apex, Halo, Finals und den meisten Vergleichsspielen; D1-Modellnamen sind im Video nicht eingeblendet.
- **FOV** aller Clips unbekannt; Battlefield 6 ist eine Vorabfassung, Halo die Technical Preview 2021.
- **Quellen nicht nachgeprüft:** von 11 Webquellen (7 Reddit-Threads, 4 Fachquellen) waren 10 bei der Abnahme nicht abrufbar; bestätigt ist
  nur der Activision-Blog.
- **Klasse unsicher:** The Finals M26 Matter ist als Schrotflinte geführt (Videoangabe), nicht weiter geprüft.
- **Nicht wieder versuchen:** Menü-, Crafting- und geteilte Ornamentbilder (Heir Apparent, Trinity Ghoul, Enigma) liefern keine Vollbildlage;
  Apex RE-45 (Inspektion geht in Schüsse über), CS2-Übersicht mit eingeblendeten CS:GO-Szenen, BF2042-Übersicht ohne gesicherte Ruhepose.

## 8. Prüfung und Zählung

- **Zuarbeit:** 65 Einträge (62 [M], 3 [O]), 10 Spiele, 19 Videos. **Übernommen 57** (28 Destiny 2, 9 Destiny 1, 9 Marathon, 11 Vergleich),
  **verworfen 7** (5 Doppelungen, darunter Prometheus Lens mit widerlegter Mündung, 2 Schwerter ohne Ego-Wert), **offen 1** (Bulldog).
- **Quellen:** 19 von 19 Videos per yt-dlp bestätigt; Webquellen 1 von 11 inhaltlich bestätigt (Activision), 10 nicht abrufbar und damit nicht
  prüfbar (nicht falsch).
- **Bild:** zehn Zahlen nachgemessen (Prüfagent Sonnet 5.5 und Koordinator, `grid.sh`): 7 innerhalb ±3 pp, 2 Grenzfälle (Marathon WSTR, Titanfall
  CAR, Δ bis 4 pp, in der Tabelle vermerkt), **1 widerlegt** (Prometheus Lens). Projizierte Neigung an drei Waffen nachgerechnet (32–38°, in ±10°).
- **Bewertung:** Abschnitt E der Zuarbeit übernommen; „wiederkehrend“ bei den Destiny-Stimmen zurückgestuft (zwei Threads derselben Woche).

Schlusszeile: 10 Spiele · 57 Beispiele übernommen · 17 Videos (Zuarbeit 19) · 7 Spieler- und 4 Fachquellen (1 bestätigt) · 57 gemessene
Einzelbilder.
