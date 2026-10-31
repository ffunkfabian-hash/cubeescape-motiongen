# Vom Schuss zum Einschlag – Projektil, Leuchtspur, Strahl, Einschlag, Explosion und Rauch je Waffenklasse

Referenzanalyse REF 0.36 „Impact“ (31.10.2026, Mac; Nachtrag REF 0.38 „Aftermath“ in [11](#11-nachtrag-aftermath)) für BALLON 0.34 „Payload“ (Projekt `cubeescape-ballon`, baut die Wirkung der Waffen) und
Cube Escape: was zwischen Abzug und Ziel sichtbar ist (sofortiger Treffer oder Projektil, Leuchtspur, Flugzeit, Bahn, Strahl, Schrotbild) und
was danach bleibt (Einschlag je Untergrund, Einschusslöcher, Explosion, Rauch, Laufeffekt). **Destiny 2 zuerst**, Vergleich mit Halo Infinite,
Titanfall 2 und Apex Legends. Hier stehen Beobachtungen und Zahlen; Schlüsse und Startwerte entstehen in BALLON bzw. Cube Escape.
Maschinenlesbar: [`data/einschlag.json`](../data/einschlag.json) (Messzeilen und Übernahmetabelle in den Feldnamen von BALLON).

Nachbarthemen, hier **nicht** wiederholt: [Mündungsfeuer und Hülsen](muendung.md) (0.19), Ballista 0.11.17 ([Methode 16](destiny2.md#methode-16):
Ignition Code, Eyes of Tomorrow, Cartesian Coordinate, Shock and Awe, Prometheus Lens, Chroma Rush, Baligant, Blue Shift, Imperial Needle),
[Rückstoß](rueckstoss.md) (0.16), [Waffenwerte](waffenwerte.md) (0.27). Die **Destiny-2-Messzeilen** stehen nach Repo-Regel in
[destiny2.md › 2](destiny2.md#2-messungen-an-60-fps-aufnahmen-ab-16-oktober-2026--m) (Anker `z-im-…`, [Methode „Impact“](destiny2.md#methode-impact)).

**Status:** **[M]** gemessen am nativen Einzelbild · **[O]** Sichtung ohne belastbare Zahl · **[S]** Datenbank/Wiki/Fachartikel · **[B]** Entwickler
(Patchnotes, Interview) · **[C]** Spielerstimme. **Jede Zahl ist das Beispiel einer Waffe** in einer Aufnahme mit unbekanntem FOV, unbekannten
Perks und **unbekannter Entfernung**, kein Klassenmittel. „Nicht sichtbar“ ist kein Nullwert.

## 1. Quellen und Methode

- **Bilder:** native Einzelbilder bei 60/s, exakt per ffmpeg-Suche (kein OpenCV-Suchsprung), 960-px-Rasterbilder mit 10-%-Raster bzw.
  2-%-Ausschnitten. **Dauer** = erstes sichtbares bis letztes sichtbares Bild bzw. bis zum ersten Bild ohne Effekt (je Zeile genannt), ±1 Bild;
  **Flugzeit** = erstes Blitzbild → erstes Einschlag-/Explosionsbild. **Größe** = Hüllrechteck im Peakbild in % der Bildbreite B / Bildhöhe H
  (Ursprung oben links), ±3 pp; Effekte rechts unten sind oft von der Waffe begrenzt (dann Mindestwert). Farben = gerenderte Pixel als Hex.
- **Hilfsmaß Hellwert-Differenz** gegen ein Bild vor dem Schuss (Anteil heller gewordener Pixel und ihr Hüllrechteck) zum Finden von
  Beginn und Ende; **jedes Ende am Einzelbild bestätigt** – Kamerabewegung verfälscht das Maß (Ikelos: Ende 20 Bilder zu spät, [9](#9-prüfung-und-zählung)).
- **Normaltempo:** Ultraclocked-Kapitel „Hip-fire“/„Weapon fire“ gegen „Slow-Motion/50 %“; Sammelvideos 2020 ohne Marke über gleiche
  Schussabstände (Methode 10). Halo-Drills über den Countdown; Titanfall/Apex über gleichmäßige Schussabstände. **Echte Bildrate** je Abschnitt
  über die Bilddifferenz (Paarduplikate = 30 echte Bilder/s → Dauer nur in echten Bildern).
- **Entfernung:** in keiner Destiny-Aufnahme belegt (kein Distanzmaß im Spiel). Halo-Academy-Schilder „5M/10M“ markieren Zielpositionen,
  nicht den Spielerstandort. Darum **keine m/s aus Bildern**; Geschwindigkeiten nur aus Text- und Datenquellen ([5](#5-text--und-datenwerte-s--b)).
- **Unteragenten:** sieben Messthemen (Destiny Primär, Spezial, Werfer, Lücken; Halo; Apex/Titanfall; Nexxoss-Nachtrag) und eine Text-
  recherche; zwei Sonnet-Anläufe ohne Messzahl wurden mit Opus wiederholt. Zweitprüfung durch den Koordinator in [9](#9-prüfung-und-zählung).

### Videos (alle am 31.10.2026 per yt-dlp geprüft: Kanal | Datum | Dauer | Titel)

| Spiel | Kanal · Datum · Video | Inhalt (Zeitfenster) | Bildrate |
|---|---|---|---|
| Destiny 2 | Ultraclocked · 07.04.2021 · [fkF9GjCDG0E](https://www.youtube.com/watch?v=fkF9GjCDG0E) | IKELOS_SMG (Kapitel Hipfire 3–13 s) | 60/s nativ |
| Destiny 2 | Ultraclocked · 30.05.2021 · [d4kzfq_ZRPg](https://www.youtube.com/watch?v=d4kzfq_ZRPg) | Outbreak Perfected (21–29 s = **Zeitlupe**) | 60/s |
| Destiny 2 | Ultraclocked · 14.02.2020 · [IG-GZ72Vbi0](https://www.youtube.com/watch?v=IG-GZ72Vbi0) | SUROS: Annual Skate, Solemn Hymn, Hoosegow | 60/s |
| Destiny 2 | Ultraclocked · 09.02.2020 · [afs_dhFDhQU](https://www.youtube.com/watch?v=afs_dhFDhQU) | VEIST: Blue Shift (zweiter Schuss 94,0 s), Valakadyn | 60/s |
| Destiny 2 | Ultraclocked · 30.01.2020 · [42zdQOVBAD0](https://www.youtube.com/watch?v=42zdQOVBAD0) | Omolon: Mos Epoch III | 60/s |
| Destiny 2 | Ultraclocked · 25.01.2020 · [73lGCT7yOtk](https://www.youtube.com/watch?v=73lGCT7yOtk) | Häkke: Minimum Distance | 60/s |
| Destiny 2 | Ultraclocked · 18.02.2021 · [RXgRxHESqHQ](https://www.youtube.com/watch?v=RXgRxHESqHQ) | Far Future (2–18 s Normaltempo) | 60/s |
| Destiny 2 | Ultraclocked · 20.02.2021 · [uoTaCBMXcFk](https://www.youtube.com/watch?v=uoTaCBMXcFk) | Threaded Needle (4–15 s) | 60/s |
| Destiny 2 | Ultraclocked · 26.09.2021 · [WtnYTQO2eJs](https://www.youtube.com/watch?v=WtnYTQO2eJs) | Ager's Scepter (4–14 s) | 60/s |
| Destiny 2 | Ultraclocked · 10.04.2021 · [ignEBRBZ0cU](https://www.youtube.com/watch?v=ignEBRBZ0cU) | The Fourth Horseman | 60/s |
| Destiny 2 | Ultraclocked · 10.06.2021 · [2PtNLNYrp88](https://www.youtube.com/watch?v=2PtNLNYrp88) | Jötunn | 60/s |
| Destiny 2 | Ultraclocked · 21.02.2021 · [75tJThF8RhQ](https://www.youtube.com/watch?v=75tJThF8RhQ) | Ticuu's Divination | 60/s |
| Destiny 2 | Ultraclocked · 20.10.2024 · [VAqIWLGMeGg](https://www.youtube.com/watch?v=VAqIWLGMeGg) | Vesper's Host: Velocity Baton, Chill Inhibitor | 60/s |
| Destiny 2 | Ultraclocked · 19.08.2022 · [nLnn5jLA0tw](https://www.youtube.com/watch?v=nLnn5jLA0tw) | Vow of the Disciple: Forbearance | 60/s |
| Destiny 2 | Ultraclocked · 28.06.2021 · [yRTm3U5NhVc](https://www.youtube.com/watch?v=yRTm3U5NhVc) | Witherhoard | 60/s |
| Destiny 2 | Nexxoss Gaming · 12.12.2019 · [yH6HtfktpC8](https://www.youtube.com/watch?v=yH6HtfktpC8) | Python-Review (Spielszene 104–136 s) | 60-Container, **30 echte/s** |
| Destiny 2 | Nexxoss Gaming · 07.03.2019 · [c5EHzSOGy4w](https://www.youtube.com/watch?v=c5EHzSOGy4w) | Sauerstoff-SG3-Review (45–58 s) | 60-Container, **30 echte/s** |
| Destiny 2 | Nexxoss Gaming · 16.10.2017 · [7aJg4idcsI4](https://www.youtube.com/watch?v=7aJg4idcsI4) | Der Kluge Tadel (109–123 s) | 29,97/s |
| Destiny 2 | Nexxoss Gaming · 16.06.2019 · [lR6e42dNZxw](https://www.youtube.com/watch?v=lR6e42dNZxw) | Schweigen (nur Sichtung) | 60-Container, 30 echte/s |
| Halo Infinite | GamesTunnel · 01.12.2021 · [wRFN8iiRvqs](https://www.youtube.com/watch?v=wRFN8iiRvqs) | Academy Weapon Drills Cindershot | 2560 × 1072, 60/s |
| Halo Infinite | GamesTunnel · 01.12.2021 · [f7c6sbLyepA](https://www.youtube.com/watch?v=f7c6sbLyepA) | Academy Weapon Drills Sentinel Beam | 2560 × 1072, 60/s |
| Halo Infinite | symphony · 18.11.2021 · [zbkW5WpXAlU](https://www.youtube.com/watch?v=zbkW5WpXAlU) | Weapon Drills CQS48 Bulldog | 1920 × 1080, 60/s |
| Titanfall 2 | Hectorlo · 08.12.2016 · [4WZ7kOJ9XjI](https://www.youtube.com/watch?v=4WZ7kOJ9XjI) | Softball, MGL, Charge Rifle, Cold War, EPG-1 | 59,94-Container, **30 echte/s** |
| Titanfall 2 | Weapons From Games · 14.03.2019 · [4sDwTD9U8bw](https://www.youtube.com/watch?v=4sDwTD9U8bw) | EPG-1 (339–358 s) | 60/s |
| Apex Legends | Cacek47 · 06.02.2019 · [R-BGChzYGpo](https://www.youtube.com/watch?v=R-BGChzYGpo) | Thermitgranate (Season 0) | 60-Container, ≈ 50–55 echte/s |

Gesichtet ohne Messwert (nicht erneut versuchen): Halo-Drills BR75, Plasma Pistol, Ravager (Ziele zu fern; Ravager nur [O]), MA40 (Mersa, 30 echte/s);
Apex Firing Range `ygAzc_w2nAQ`, `TbLFHWhLtzs` (30/s, keine Einschläge, gelbe Linie = Zipline), Bullet-Drop-Guide `XcqzZVEXSac` (30/s),
`pybDcz_tvjE` (30/s, Abgang außerhalb), `HyEYWNobD3Y` (Ziele zu fern); Titanfall WFG-Werfer im Sandsturm unsichtbar; Destiny Crux Celeritas IV
(nur Himmel), Raketen-/Granatwerfer-Ornamentvideos (Split-Screen, Schüsse ins Leere), Spiteful Fang (nur Nocken), Divinity, Beggar, Arbalest,
Lorentz Driver, Coldheart (Schüsse in den Himmel), Doom of Chelchis, Zaouli's Bane, Symmetry (Himmel/Split-Screen), Valakadyn (Einschlag vom
Visierrahmen verdeckt). `visiere/halo/WFG_X_ADv1HMwkg` ist Halo 3, nicht Infinite.

## 2. Destiny 2 – Tabelle je Klasse

Volle Zeilen mit Bildindizes: Spalte „Zeile“ (destiny2.md › 2). Bilder bei 60/s. „–“ = nicht im Bild.

| Klasse (Waffe) | Treffer | Spur / Projektil | Flugzeit | Einschlag (Untergrund) | Loch | Explosion / Rauch | Laufeffekt | Zeile |
|---|---|---|---|---|---|---|---|---|
| Maschinenpistole (IKELOS_SMG) | sofort (Blitz- oder Folgebild) | keine sichtbar | – | **Erde:** dunkle Rauchsäule ≈ 4–5 % B × 15–20 % H (#150F0D–#2A1D1A) über blau-weißem Ring ≈ 3 × 5 % (#9FC4FF), Säule bleibt nach dem letzten Schuss ≈ 15–18 Bilder | keines (Boden 40 Bilder nach Salvenende sauber) | – | – | [z-im-ikelos](destiny2.md#z-im-ikelos) |
| Impulsgewehr (Outbreak Perfected) | sofort | keine sichtbar | – | **Erde:** Säule ≈ 4 × 14 %, orange-rote Funken ≈ 2 × 8 % (#FF5A28/#FF9A50); Dauer nur in Zeitlupe | keines | – | – | [z-im-outbreak](destiny2.md#z-im-outbreak) |
| Automatik (Solemn Hymn) | – (Zielpunkt im Visierrahmen) | keine sichtbar | – | **Beton:** violettes Leuchten 1–2 Bilder je Schuss, orange Funken 8–12 Bilder [O] | **keine nach ≈ 3 s Dauerfeuer** (Wand 1,5 s später sauber) [M] | – | – | [z-im-solemn-hymn](destiny2.md#z-im-solemn-hymn) |
| Scout (Sauerstoff SG3, Nexxoss, 30 echte/s) | **sofort** (Treffermarke und Lebensleiste im Blitzbild) | keine sichtbar | – | **Gegner (Thrall):** Trefferleuchten violett-rosa ≈ 3 × 3 %, ≈ 6 Bilder; Schadenszahl ≈ 6 Bilder später, Präzisionszahl im Blitzbild | – | – | – | [z-im-sauerstoff](destiny2.md#z-im-sauerstoff) |
| Handfeuerwaffe / Seitenwaffe (Annual Skate, Minimum Distance) | – | keine sichtbar | – | auf Beton bzw. ferner Fassade nichts sichtbar [O] | keine | – | – | [z-im-hc-sidearm](destiny2.md#z-im-hc-sidearm) |
| Scharfschütze (Far Future) | **sofort** (erstes freies Bild nach 2 Blitzbildern) | keine Leuchtspur, kein Kondensstreifen | – | **Sand:** weiß-orange Funken ≈ 4 × 4 %, Splitter 7 × 8 %, 6 Bilder; dunkle Säule ≈ 6 × 6,5 %, ≈ 23 Bilder | keines | – | – | [z-im-far-future](destiny2.md#z-im-far-future) |
| Lineare Fusion (Threaded Needle) | **sofort** (+1 Bild) | **kein fester Strahl:** violett-weißer Schleier am Lauf 4 Bilder | – | **Sand:** violett-weiße Funkenkrone ≈ 8 × 5,5 %, ≈ 15 Bilder; schwarze Säule ≈ 3 × 11 %, 21–24 Bilder | keines | – | Aufladung 11 Bilder Blitzbögen | [z-im-threaded-needle](destiny2.md#z-im-threaded-needle) |
| Spurgewehr (Ager's Scepter, exotisch) | Dauerstrahl, Ziel sofort | **durchgehend ≥ 90 Bilder**, keilförmig ≈ 5 % B am Lauf → ≈ 2 % H am Ziel, blau-weiß (#D0D8FF, Rand #5060E0) | – | **Boden nah (Schätzung):** Punkt ≈ 4 × 7 %, **pulsiert im 5-Bilder-Takt (12/s)** | keines | – | – | [z-im-agers](destiny2.md#z-im-agers) |
| Schrotflinte (The Fourth Horseman, exotisch) | – (Blitz verdeckt ≈ 5 Bilder) | – | – | **Sand nah (Schätzung):** **ein** schwarzer Rauchball ≈ 10 × 22 % (#101828) mit ≈ 14 weißen Splittern, ≈ 30 Bilder; **kein Einzelkugelbild** | keines | – | kein Laufrauch sichtbar (40 Bilder) | [z-im-horseman](destiny2.md#z-im-horseman) |
| Schrotflinte (Python, legendär, Void, Dez. 2019 – vor 6.3.0; Nexxoss, 30 echte/s) | **sofort** (Leuchten an der Wand im Blitzbild) | – | – | **Wand nah:** **ein** zusammenhängender Funkenball ≈ 7,5 × 14,5 % (Kern #F1EBFA, Hof #B9B2E1), dicht ≈ 10 Bilder, Funken ≈ 30 Bilder; **Boden:** ein Funkenspringbrunnen ≈ 9 × 28 %, ≈ 16 Bilder (13 Schüsse gleich); **keine Einzelkugeln zählbar** | kein Decal | – | violette Void-Schwaden ≈ 8 Bilder, kein grauer Rauch | [z-im-python](destiny2.md#z-im-python) |
| Fusion (Der Kluge Tadel, legendär, Okt. 2017; Nexxoss, 29,97/s) | – | Ladering orange 6 echte Bilder; Auslösen weißer Ball ≈ 20 × 24 % mit Linsenstreifen über fast die ganze Breite ≈ 4 Bilder; **keine Bolzen im Flug sichtbar** | – | **Fliesenwand:** kein Einschlag, kein Decal sichtbar (zwei Schüsse) | kein Decal | – | orange Flammenzungen ≈ 9 echte Bilder | [z-im-tadel](destiny2.md#z-im-tadel) |
| Fusion (Jötunn, exotisch, Explosivschuss) | Projektil | weißer Ball ≈ 2–3 % B, 5 Bilder | **9** | Feuerball ≈ 36 × 39 % (#FFB070) mit blauen Bögen, Ring ≈ 40 % B 2 Bilder, Flammen ≥ 47 Bilder | – | s. Einschlag | Mündung 6 Bilder | [z-im-jotunn](destiny2.md#z-im-jotunn) |
| Bogen (Ticuu's Divination, exotisch, ungespannt) | Projektil | **Pfeil im Flug unsichtbar**, kein Schweif | **4** | Feuerball + Rauch ≈ 7,5 × 15,5 %, Rauch ≈ 27, Funken ≈ 39 Bilder; Pfeil steckt **nicht** (Exotic-Explosion) | – | s. Einschlag | – | [z-im-ticuu](destiny2.md#z-im-ticuu) |
| Granatwerfer, Spezial oder schwer offen (Velocity Baton, Area Denial, Void) | Projektil, 5er-Salve (Abstand 7–9 Bilder) | lavendel Punkt 0,4–0,6 % B (#CDB9FF), **kein Schweif** | **10–13** (nah) | Kern weiß-lavendel ≈ 9 × 11 %, 7 Bilder; Licht −16 % für 3 Bilder; **violette Flammenlache** ≈ 19 × 31 % (#5743BE), 5,6 s nach dem letzten Einschlag weg, brauner Fleck bleibt | – | kein Feuerball, kein dunkler Rauch | violette Wolke 7 Bilder | [z-im-velocity-baton](destiny2.md#z-im-velocity-baton) |
| Spezial-Granatwerfer (Forbearance, Arc) | Projektil | dunkle Kugel ≈ 1,5 % B im rosa-roten Halo 9,7 → 1,7 % B, kein Schweif | – (Leere) | – | – | – | **Arc-Bögen 5 + graue Wolke 8–12 Bilder** (#9EABBE → #4A536E) | [z-im-forbearance](destiny2.md#z-im-forbearance) |
| Spezial-Granatwerfer (Witherhoard, exotisch, Blight) | Projektil | dunkler Kern + weißer Ring 0,3–0,5 % B, kein Schweif; **Bildbahn fällt 0,7 → 1,5 pp/Bild** | **12** (nah) | Blitz cyan-weiß ≈ 34 × 46 % 2 Bilder + Funkenstrauß bis 23 Bilder; schwarzer Stachelstern ≥ 31 × 18 % in **einem** Bild, ≥ 6 s [O] | – | kein Belichtungseinbruch | orange-braune Wolke 3 Bilder | [z-im-witherhoard](destiny2.md#z-im-witherhoard) |
| Schwerer Granatwerfer (Chill Inhibitor, Area Denial, Stasis) | Projektil | rote Glühkugel ≈ 1 % B, Halo 2 % (#F198A9), kein Schweif; Bahn 0,5 → 1,0 pp/Bild (mit Kamera) | **11** (nah) | Kern cyan-weiß ≈ 9 × 11 % (#EEFEFE), blaues Glühen ≈ 30 × 33 % (#5151BA), 8 Bilder; **Belichtung −60 %**, Erholung ≥ 22 Bilder; Kristallfunken 10 Bilder; dunkler Staubfleck 50–75 Bilder | – | kein Feuerball | Eissplitter ≈ 9 Bilder | [z-im-chill-inhibitor](destiny2.md#z-im-chill-inhibitor) |
| Raketenwerfer (Blue Shift) | Projektil | oranger Glühkopf 12 → 3 % B (#DCC8A0), blasser Strich 15–20 % B, **kein Rauchzopf** | **39** | **Explosion in drei Stufen:** Vollbildblitz 2 Bilder (#FCECDE), Kern ≈ 13 Bilder; Kuppel Ø ≥ 22–24 % B, 5 Bilder; Feuerball ≈ 19–23 × 31–35 % (#E9B268 → #CA774A), ≈ 52 Bilder; rote Glut bis ≈ 100 Bilder | – | Rauch fast schwarz (#020C08), ≈ 70 Bilder | kein Laufrauch sichtbar | [z-im-blue-shift](destiny2.md#z-im-blue-shift) |
| Raketenwerfer (Hoosegow, Nacht) | Projektil | blauer Glühball 8 → 4 % B (#E8FCFD), Linsenstreifen 38 % B, **Lichtpfütze am Boden** | **28 / 19** | Vollbildblitz; Umgebungslicht 9–10 Bilder orange, danach **Unterbelichtung ≥ 18–25 Bilder**; Ring violett-rosa Ø 20–36 % B, 4–8 Bilder; Feuerball 17–21 × 45–55 % (#F3AF62 → #D53823), ≈ 60 Bilder; blau-weiße Funken ≥ 60 Bilder | – | Rauch im Dunkeln nicht sichtbar | Blitz 4–5 Bilder, kein Laufrauch | [z-im-hoosegow](destiny2.md#z-im-hoosegow) |
| Raketenwerfer (Mos Epoch III) | Projektil | blauer Punkt 3–4 % B, kurzer Schweif | **≈ 35 ±3** | Blitz 7 Bilder (≈ 25 × 40 %); Ring violett-rosa Ø ≈ 17 % B [O], 6 Bilder; Feuerball ≈ 11 × 24 %, ≈ 30 Bilder | – | schwarzer Brandfleck ≥ 45 Bilder | – | [z-im-mos-epoch](destiny2.md#z-im-mos-epoch) |

## 3. Vergleich: Halo Infinite, Titanfall 2, Apex Legends

Halo-Prozente aus 2560 × 1072-Videos (2,39 : 1) beziehen sich auf das ganze Bild – für 16 : 9 vor Übernahme umrechnen. Titanfall-Hectorlo
und Apex: Containerduplikate, Dauern in echten Bildern (×2 ≈ Bilder bei 60/s, ±2).

| Spiel · Waffe (Klasse) | Quelle · Zeit | Messung | Status |
|---|---|---|---|
| **Halo · Cindershot (Granatwerfer)** <a id="i-halo-cindershot"></a> | GamesTunnel wRFN8iiRvqs · 164,483 (f9869) → f9889 | **Projektil mit Spur bei jedem Schuss:** rosa Kopf + Spur 0,55–0,95 % B breit, bis 7,8 % H lang (#E9A6C0/#FDC4E2), ≥ 11 Bilder sichtbar. **Flugzeit 20 Bilder** (Ziel am Schild 10M) bzw. 8 Bilder (Schild 5M, 32,7 s). Explosion zweiphasig im Abstand von 7 Bildern: Kern ≈ 10 % B (7 Bilder, #F7E5F2), dann 18–21 % B (9 Bilder), violette Funken (#B49DEA) ≈ 15 Bilder, gesamt ≈ 31 Bilder, **kein grauer Rauch** | [M] |
| **Halo · Sentinel Beam (Strahl)** <a id="i-halo-sentinel"></a> | GamesTunnel f7c6sbLyepA · 32,667 (f1960) | durchgehender Strahl, Kern 0,7 % B am Ziel → 1,3–1,6 % B zur Mündung, weiß (#FFFAF6) mit cremefarbenem und lavendelfarbenem Saum (#FDE2BC / #C6BEFD); **kein An- und Ausklingen** (ein Bild auf das nächste), Trefferglut ≈ 5 % B bleibt 8 Bilder | [M] |
| **Halo · CQS48 Bulldog (Schrot)** <a id="i-halo-bulldog"></a> | symphony zbkW5WpXAlU · 34,950 (f2097) | **Jede Kugel mit Leuchtspur**, schon im Blitzbild bis ans Ziel (sofort, ≈ 5 m): je 0,2–0,35 % B, Kern hellgelb #FEEEB6, Saum orange; 7 Bilder hell, danach **graue Rauchfäden auf denselben Bahnen ≥ 5 Bilder**. Streuung am Ziel ≥ 3–4 % B × 8 % H (Untergrenze), Kugelzahl ≥ 6 [O] | [M]/[O] |
| Halo · MA40, Ravager | Mersa (30 echte/s); GamesTunnel | MA40 ohne sichtbare Leuchtspur, rote Schildfunken am Bot; Ravager: weiß-rosa Ball 0,6–1,1 % B, roter Brandrest (#F29086) ≥ 15 Bilder, Feuerfeld ≥ 40 Bilder – Projektil und Einschlag nicht trennbar | [O] |
| **Titanfall 2 · Softball (Granatwerfer, Kontakt)** <a id="i-tf2-softball"></a> | Hectorlo 4WZ7kOJ9XjI · 558,27 | Weißer Blitz 35–62 % B, dann 1–2 echte Bilder Überstrahlung ≥ 90 % B; Feuerball 20–75 % B × 15–75 % H, Feuer ≈ 16 Bilder bei 60/s (Kern #FBE9DE); grauer Rauch (#5F5C5C) > 0,7 s; Einschlag ≤ 1 echtes Bild nach dem Schuss (nahe Kisten) | [M] |
| **Titanfall 2 · MGL (Granatwerfer, Haft)** <a id="i-tf2-mgl"></a> | Hectorlo · 607,39 | dunkle Granate ≈ 1 % B ohne Spur; erstes Explosionsbild 8 × 11 %, Blitzhof danach 32–53 % B, Feuer #BC512B, schwarzer Ballen; Folgegranate +5 echte Bilder | [M] |
| **Titanfall 2 · Charge Rifle (Strahl)** <a id="i-tf2-charge"></a> | Hectorlo · 623,92 | **sofort**; Strahl 1–1,5 % H breit, #F9DFD5 → orange, die Strahlspur bleibt **schwach ≥ 24 echte Bilder (≈ 0,8 s)**; Schussbild hellt 31–87 % B auf | [M] |
| **Titanfall 2 · EPG-1 (Energiewerfer)** <a id="i-tf2-epg"></a> | WFG 4sDwTD9U8bw (60/s) · 339–358 | bläulich-weiße Leuchtkugel bleibt im Fadenkreuz (fliegt entlang der Blickachse), Hof 2,5–4 % B (+12 Bilder), Kern ≤ 2 % B (ab +27), ≥ 72 Bilder sichtbar; Einschlag im Dunst nicht sichtbar | [M] |
| Titanfall 2 · Cold War | Hectorlo | blau-weiße Wolke (#D5E2FA) bis 33–78 % B, ≈ 0,7 s; mehrere Schüsse überlagert | [O] |
| **Apex · Thermitgranate (Wurfgranate, Nebenbefund)** <a id="i-apex-thermit"></a> | Cacek47 R-BGChzYGpo · 345,73 | rote Granate ≈ 1 % B; Wurf → Zündung ≈ 45 Bilder, davon ≈ 19 Glimmen; Feuerwand mit zwei Fronten, ≈ 45 % B in 0,33 s, 13 % H hoch (#F0C38B / Kern #FEE2A7), steht ≥ 5,5 s | [M] |

Apex-Feuerwaffen: in den geprüften Quellen **keine lesbaren Einschlagfunken oder Leuchtspuren** (Firing-Range-Videos nur 30/s, Ziele fern) – Apex
steht deshalb nur mit [S]-Werten in [5](#5-text--und-datenwerte-s--b).

## 4. Muster (Beobachtung, keine Gestaltungsregel)

- **Destiny 2 zeigt keine Leuchtspuren bei Kugelwaffen** (MP, Impuls, Automatik, Scout, Handfeuerwaffe, Seitenwaffe, Scharfschütze in
  7 Beispielen, davon Handfeuerwaffe und Seitenwaffe nur [O]) und **keine Einschusslöcher** auf Beton (3 s Dauerfeuer), Fliesenwand, Erde und Sand – **Ausnahme Schrot auf Blech: bleibende Löcher** ([11](#11-nachtrag-aftermath)). **Schrot ist ein einziger Einschlag**
  (Funkenball an der Wand, Springbrunnen am Boden, Rauchball beim Horseman) – Einzelkugeln sind in Destiny vor 6.3.0 nicht zu sehen. Am Gegner:
  Treffermarke und Lebensleiste im Blitzbild, Trefferleuchten ≈ 6 Bilder, Schadenszahl danach. Der Treffer ist ein **kurzer Einschlag am Zielpunkt**: elementfarbene Funken
  oder Ring je Waffe (IKELOS blau-weiß, Outbreak orange-rot, Sauerstoff SG3 violett-rosa – eine Zuordnung zu Elementen ist nicht gemessen) plus eine **schmale, hohe dunkle Rauchsäule** (Breite : Höhe ≈ 1 : 3–4) von etwa
  15–25 Bildern. Halo (Bulldog, Cindershot) und Titanfall (Charge Rifle) zeichnen dagegen **sichtbare Spuren**, Halo bei jeder Schrotkugel.
- **Sofort ist sofort:** Scharfschütze, lineare Fusion, MP, Impuls und Spur treffen im Blitz- oder Folgebild. Projektile haben in Destiny
  **keinen Rauchschweif** – Raketen sind ein schrumpfender Glühpunkt (3–12 % B) mit Lichtpfütze, Granaten ein kleiner Leuchtpunkt in Element-
  farbe (0,3–1,5 % B), Pfeile im Flug unsichtbar. Halo-Cindershot dagegen mit deutlicher Spur.
- **Flugzeiten bei nahen Zielen** (Entfernung unbekannt): Granaten 10–13 Bilder, Raketen 19–39 Bilder, Jötunn 9, Ticuu's 4; Halo-Cindershot 8–20.
- **Explosionen in Destiny:** Raketen = **Vollbildblitz 1–2 Bilder → Kern 7–13 Bilder → violett-rosa Kuppel/Ring 4–8 Bilder → oranger Feuerball
  30–60 Bilder → schwarzer Rauch/Brandfleck 45–70 Bilder**; bei Nacht folgt dem Lichtschein (9–10 Bilder) eine **Unterbelichtung** von
  ≥ 18–25 Bildern. **Elementgranaten haben keinen Feuerball und keinen schwarzen Rauch** – die Elementfarbe ersetzt das Feuer (Void-Lache,
  Stasis-Glühen mit −60 % Belichtung, Blight-Stern). Titanfall-Softball ist ein kurzer orangefarbener Feuerball (≈ 16 Bilder) mit grauem Rauch.
- **Laufeffekt nach dem Schuss:** bei Destiny-Granatwerfern elementfarbig, 3–12 Bilder (violette Wolke, Eissplitter, Arc-Bögen + graue Wolke,
  orange-braune Wolke); bei Raketenwerfern und Fourth Horseman **kein sichtbarer Laufrauch**.
- **Strahlen:** Destiny-Spur keilförmig und durchgehend, Einschlag pulsiert im 5-Bilder-Takt; Halo-Sentinel-Beam dünn (0,7–1,6 % B) und ohne
  Ausklingen; Destiny-LFR ohne festen Strahl (Schleier am Lauf, sofortiger Treffer); Titanfall-Charge-Rifle mit langer schwacher Nachspur.

## 5. Text- und Datenwerte [S] / [B]

Alle Seiten am 31.10.2026 aufgerufen; Stichprobe des Koordinators 5 von 5 geladen ([9](#9-prüfung-und-zählung)). „Destiny-m“ = Spielmeter.

| Spiel · Gegenstand | Wert | Quelle | Status |
|---|---|---|---|
| Destiny 2 · Treffer sofort oder Projektil | Kugelwaffen (AR, HC, Impuls, Scout, MP, Sniper, MG, Seitenwaffe, meiste Schrotflinten) treffen sofort; Projektile: Raketen, Granaten, Bögen, Glefe, Heavy Crossbow, Skyburner's Oath (Hüfte); Fusion seit Season 15 sofort (Jötunn Ausnahme) | [Steam-Thread 07.12.2019](https://steamcommunity.com/app/1085660/discussions/0/1750142526436270141/); [MP1st, 20.08.2021](https://mp1st.com/news/destiny-2-season-15-weapon-tuning-changes-and-new-weapons-revealed) | [C]/[S] |
| Destiny 2 · Fusion-Bolzen je Salve | Stand 20.08.2021: High-Impact 5, Precision 7, Adaptive 7, Rapid-Fire 9; Stand 2025/26: Aggressive 3er-Salve × 4 | MP1st (zitiert Bungie); [Destiny Data Compendium](https://docs.google.com/spreadsheets/d/1WaxvbLx7UoSZaBqdFr1u32F2uWVLo-CJunJB4nlGUE4) | [S] – über die Zeit veränderlich |
| Destiny 2 · Schrotkugeln und Muster | 12 Kugeln belegt (Precision-Muster, Perk-Texte); **seit 6.3.0 (06.12.2022) feste Muster je Rahmen**: Aggressive Kegel, Precision Oval, Lightweight Raute, Rapid-Fire Quadrat, Slug ein Punkt; Streukegel in Grad nicht gefunden | [Dexerto 6.3.0](https://www.dexerto.com/destiny/destiny-2-update-6-3-0-patch-notes-season-19-weapon-changes-buffs-nerfs-2001255/); Compendium | [S]/[B] |
| Destiny 2 · Geschwindigkeiten | **keine m/s** für Rakete, Granate, Pfeil, Fusionsbolzen; Velocity und Blast Radius nur als Stat 0–100 (Impulse Amplifier +10 % Raketen); belegt nur Support-Frame-AR 40 Destiny-m/s, Winterbite-Kugel 9,5 Destiny-m/s; Maßstab Gehen 5,6–7, Sprint 8 Destiny-m/s | Compendium | [S] |
| Destiny 2 · VFX-Arbeitsweise | Bungie-VFX-Interview (Mike Stavrides) zu Effektproduktion | [80.lv, 06.02.2019](https://80.lv/articles/destiny-2-vfx-production-tips) | [B] |
| Titanfall 2 · Geschwindigkeiten (Patchnoten 2017, mph → m/s eigene Rechnung) | EPG-1 85,1 mph ≈ 38 m/s; Sidewinder 140,4 mph ≈ 63 m/s; MGL 51,1 mph ≈ 23 m/s; Archer 51 mph ≈ 23 m/s; Thunderbolt 21 mph ≈ 9,4 m/s; EVA-8 Streuung 6 → 8 Grad (25.04.2017) | [Fan-Tracker der Respawn-Patchnoten](https://github.com/Syampuuh/Titanfall2) | [S] aus [B] |
| Titanfall 2 · Einschlagmarken | Grenze 256 gleichzeitig (Konfiguration), Stufe Medium nur Funken | [NVIDIA-Leitfaden 02.11.2016](https://www.nvidia.com/en-us/geforce/news/titanfall-2-graphics-performance-and-tweaking-guide/) | [S] |
| Apex · Schrot und Geschwindigkeit | Mastiff 5 Kugeln, waagerechte Linie, 16 000 hu/s (Wiki: 305 m/s); Peacekeeper 9 Kugeln, 20 000 hu/s; Kraber 29 500 hu/s – das Wiki rechnet widersprüchlich um (mit 0,01905 m/hu ≈ 381 bzw. 562 m/s) | [apexlegends.wiki.gg Mastiff](https://apexlegends.wiki.gg/wiki/Mastiff) u. a. | [S] |
| Apex · Visual Clutter | „Takeover“: Mündungsfeuer erneuert, Rauschen über der Sichtlinie stark reduziert | [EA-Patchnoten 10.02.2025](https://www.ea.com/games/apex-legends/apex-legends/news/takeover-patch-notes); [Dexerto 08.01.2022](https://www.dexerto.com/apex-legends/respawn-finally-respond-to-apex-legends-visual-clutter-issues-1735929/) | [B] |
| Halo Infinite · Raketen und Splash | Season-1-Bericht: Splash-Konsistenz der Raketen, Schild-Effekte | [Halo Waypoint](https://www.halowaypoint.com/news/season-1-outcomes-report) | [B] |

## 6. Bewertung: gut, nicht so gut, für wen

| Spiel · Gegenstand | Gut (warum) | Nicht so gut (warum) | Für wen | Belege | Spielerstimmen | Entwickler / Fach |
|---|---|---|---|---|---|---|
| Destiny 2 · Kugeltreffer ohne Spur und Loch | ruhiges Bild trotz hoher Kadenz; der Treffer liest sich über Funken am Zielpunkt; keine Decal-Grenze nötig | kein Rückschluss auf die Schussrichtung aus der Umgebung; Wand „vergisst“ Feuer sofort | PvE-Massenkampf, Controller | [z-im-solemn-hymn](destiny2.md#z-im-solemn-hymn), [z-im-ikelos](destiny2.md#z-im-ikelos) | keine Kritik an Leuchtspuren oder Löchern gefunden (Suche ohne Treffer) | – |
| Destiny 2 · Explosionen und Verbündeten-Effekte | große Wucht durch Vollbildblitz, Kuppel, Feuerball und Lichtschein | Sicht verdeckt (Feuerball 17–23 % B, Unterbelichtung ≥ 18 Bilder nachts); keine Option zum Dämpfen | PvE-Spieler mögen Wucht, PvP/lichtempfindliche nicht | [z-im-hoosegow](destiny2.md#z-im-hoosegow) | **wiederkehrend:** [Bungie.net 07/2023](https://www.bungie.net/en/Forums/Post/263048057), [05/2025](https://www.bungie.net/en/Forums/Post/264761879), [Barrierefreiheit 09/2021](https://www.bungie.net/en/Forums/Post/259782088); Gegenstimmen: „Teamspiel“, große Monitore | Bungie leitete den Wunsch weiter, keine Zusage |
| Destiny 2 · Kamerawackeln | Treffer- und Explosionswucht | stapelt sich mit Waffen-Flinch, keine Option | PvP, bewegungsempfindliche Spieler | – | [Steam 04/2024](https://steamcommunity.com/app/1085660/discussions/0/4360121202644937396/), [Hardlight-Thread](https://www.bungie.net/en/Forums/Post/254320657) (bis 5 Zustimmungen; Gegenstimme: Ausgleich für Reichweite) | Bungie-Antwort im [Hardlight-Thread](https://www.bungie.net/en/Forums/Post/254320657) (12.11.2019): Wackeln bleibt, Ornament mit besserem Visier; Final Shape 8.0.0.1: HC-Trefferwackeln −33 % ([GameSpot](https://www.gamespot.com/articles/destiny-2-the-final-shape-patch-notes-are-a-massive-list-of-updates/1100-6523929/), Seite 403 – nur Suchauszug) |
| Destiny 2 · Spezial-Granatwerfer | klare Bahn mit kleinem Leuchtpunkt, Elementfarbe trägt Identität | Granaten fliegen durch Gegner, Lightweight explodiert nur bei Direkttreffer | PvE | [z-im-velocity-baton](destiny2.md#z-im-velocity-baton) | [Steam 22.03.2023](https://steamcommunity.com/app/1085660/discussions/0/3830914078556128855) (3 von 6 bestätigen; Ursache strittig) | – |
| Destiny 2 · Schrotmuster | feste Muster je Rahmen seit 6.3.0 machen die Streuung vorhersehbar | – | PvP | – | – | Update 6.3.0 (Dexerto) [B] |
| Halo Infinite · sichtbare Projektile | Spur je Schrotkugel und je Granate zeigt Richtung und Treffer | langsame Projektile fühlen sich schwach an (Pulse Carbine) | Profis/Vorhalten, Einsteiger tun sich schwer | [i-halo-bulldog](#i-halo-bulldog), [i-halo-cindershot](#i-halo-cindershot) | [Steam 23.11.2021](https://steamcommunity.com/app/1240440/discussions/0/3198114142308347430/) wiederkehrend; Gegenstimme „Skill“ | Season-1-Bericht: Raketen-Splash, Schild-Effekte |
| Apex · Effektmenge | – | Einschläge, Partikel und Mündungsfeuer überladen die Sichtlinie | alle, besonders PvP | – | [Dexerto 08.01.2022](https://www.dexerto.com/apex-legends/respawn-finally-respond-to-apex-legends-visual-clutter-issues-1735929/) wiederkehrend (Creator + Community) | Takeover 10.02.2025: Rauschen stark reduziert [B] |
| Titanfall 2 · Strahl mit Nachspur | lange schwache Spur zeigt Schützen und Richtung | – | PvP-Lesbarkeit | [i-tf2-charge](#i-tf2-charge) | – | – |

Spielerstimmen: 13 gesammelt (9 Destiny, Bungie.net/Steam/Presse), Reddit für die Agenten gesperrt. Mindestmaß 5 Spieler- und 2 Fachquellen erfüllt;
GDC-Vorträge zu Destiny- oder Respawn-Waffeneffekten und ein GMTK-Beitrag zu sofortigem Treffer gegen Projektil **nicht gefunden**.

**Spielerstimme Nexxoss Gaming [C] (0.37 „Verdict“, Einzelstimme aus Auto-Untertiteln, nie gegen eine [M]-Messung; Abgleich je Klasse in [destiny2 › Verdict](destiny2.md#s-verdict)):** Wucht beschreibt der Sprecher über Kills und Treffergefühl: die Python fühle sich nach einer „richtig starken Schrotflinte“ an, im PvP überleben Gegner aber Treffer ([yH6HtfktpC8](https://www.youtube.com/watch?v=yH6HtfktpC8) [03:51], [yH6HtfktpC8](https://www.youtube.com/watch?v=yH6HtfktpC8) [05:02]); Der Kluge Tadel tötet Hexe, Ritter und Centurio mit einem Schuss ([7aJg4idcsI4](https://www.youtube.com/watch?v=7aJg4idcsI4) [02:31]) und hat „Flugzeit“ ([7aJg4idcsI4](https://www.youtube.com/watch?v=7aJg4idcsI4) [04:46]) – das widerspricht [z-im-tadel](destiny2.md#z-im-tadel) nur scheinbar: „im Flug nicht sichtbar“ bei 30/s belegt keine fehlende Flugzeit ([z-v37-tadel-flug](destiny2.md#z-v37-tadel-flug)); Granatwerfer-Explosionen sind im PvP nicht groß genug ([2lpjbjC4878](https://www.youtube.com/watch?v=2lpjbjC4878) [02:41], Wendigo [OwXPZG7Sq1g](https://www.youtube.com/watch?v=OwXPZG7Sq1g) [04:56]).

### E2 – Lehren für BALLON (Vorschlag, dort entscheiden)

- **Übernehmen:** Kugelwaffen ohne Leuchtspur und ohne bleibendes Loch nach Destiny-Vorbild ist belegt (7 Beispiele: 5 [M] + 2 [O]) – der Treffer
  ist ein kurzer Einschlag (Funken in der Leuchtfarbe der Waffe 1–6 Bilder, dunkle schmale Säule 15–25 Bilder). Die bisherigen Decals (5 cm, 80 Stück) wären
  eine bewusste Abweichung; wenn Decals, dann eher kurz als ewig. **Ausnahme Schrot auf Blech nach 6.3.0:** bleibende Lochgruppe ([11](#11-nachtrag-aftermath)).
- **Übernehmen:** Explosion in Stufen nach den Raketenwerten: Blitz 1–2 Bilder bildweit → Kern 7–13 → Ring/Kuppel 4–8 (violett-rosa, schwach) →
  Feuerball 30–60 → Rauch 45–70 Bilder; bei Elementgranaten Feuer und Rauch durch Elementfarbe ersetzen.
- **Übernehmen:** Projektile als **Leuchtpunkt ohne Rauchschweif** (Rakete 3–12 % B schrumpfend, Granate ≤ 1,5 % B), Lichtpfütze am Boden bei Nacht.
- **Testen:** Laufeffekt nur bei Granatwerfern (3–12 Bilder, Elementfarbe); bei Raketenwerfern und Schrot war **kein** Laufrauch sichtbar – der
  bisherige Laufrauch 1,4–2 s ist länger als jedes Vorbild hier.
- **Testen:** Destiny-Schrot als **ein** Einschlag je Schuss (Funkenball an der Wand ≈ 7,5 × 14,5 %, dicht 10 Bilder) statt 12 Einzeleinschläge –
  oder bewusst dagegen Halo-Schrot mit Spur je Kugel (0,2–0,35 % B, 7 Bilder hell, dann Rauchfaden) als lesbare Alternative zum Destiny-Rauchball.
- **Vermeiden:** Unterbelichtung und Kamerastoß ohne Option – die meistgenannte Kritik an Destiny (Sichtverlust, Barrierefreiheit).

## 7. Für BALLON 0.34 „Payload“ – Übernahmetabelle

In den Feldnamen von `EgoFx`/`EgoExplosion` (BALLON `ego.PAYLOAD`). Zeiten aus Bildern bei 60/s (s = Bilder/60). **Meter-Felder
(`speed_mps`, `radius_m`, `width_m`, `length_m`, `size_m`) sind aus Bildern nicht ableitbar** (Entfernung und FOV unbekannt) und bleiben `null`;
Geschwindigkeiten in m/s nur aus [5](#5-text--und-datenwerte-s--b), für Destiny keine. Jede Zeile ist das Beispiel einer Waffe.

| BALLON-Klasse | kind (beobachtet) | Einschlag | Zeiten (s) | Farben | Beleg |
|---|---|---|---|---|---|
| `auto_rifle`, `submachine_gun`, `pulse_rifle`, `scout_rifle`, `hand_cannon`¹, `sidearm`¹ | `hitscan`, keine Spur | MP/Impuls: Funken + dunkle Säule (B : H ≈ 1 : 3–4); Automatik auf Beton nur Leuchten und Funken [O]; kein Decal; am Gegner Trefferleuchten ≈ 0,1 | Funken/Ring 0,02–0,1; Säule bis ≈ 0,25–0,3 nach dem letzten Schuss | Säule #150F0D–#2A1D1A; je Waffe: IKELOS #9FC4FF, Outbreak #FF5A28/#FF9A50, Sauerstoff violett-rosa (keine Elementzuordnung) | z-im-ikelos, z-im-outbreak, z-im-solemn-hymn, z-im-sauerstoff |
| `sniper_rifle` | `hitscan`, keine Spur | Funken 0,1; Säule ≈ 0,38 | `spark_s` 0,1, `dust_s` ≈ 0,38 | weiß-orange | z-im-far-future |
| `linear_fusion_rifle` | `rail` ohne festen Strahl (Schleier am Lauf) | Funkenkrone 0,25; Säule 0,35–0,4 | `beam_s` ≈ 0,07 (Schleier 4 Bilder) | violett-weiß | z-im-threaded-needle |
| `trace_rifle` | `beam`, durchgehend, keilförmig | Punkt pulsiert 12/s | Puls 5 Bilder | #D0D8FF / #5060E0 | z-im-agers |
| `fusion_rifle` | Bolzen im Bild nicht sichtbar ([S]: 5–9 je Salve, sofort) | kein Wandeinschlag sichtbar | Auslöseblitz ≈ 0,07 mit Linsenstreifen | weiß, Ladering orange | z-im-tadel; Jötunn ist Explosivschuss, kein Klassenwert |
| `shotgun` | `pellets` ([S] 12, feste Muster seit 6.3.0); Bild: **ein** Einschlag je Schuss | Funkenball dicht ≈ 0,17, Funken ≈ 0,5; Boden-Springbrunnen ≈ 0,27; Horseman-Rauchball ≈ 0,5 | Laufschwaden ≈ 0,13 (Void) | #F1EBFA / #B9B2E1; #101828 | z-im-python, z-im-horseman |
| `shotgun` (nach 6.3.0, Blech) | `pellets`; Bild: **2 Bursts** je Schuss (Glasscherben-Rosette + kleiner Burst) und **eine bleibende Lochgruppe** (Dreieck ≈ 12, Oval ≈ 9 Löcher je Muster, Loch ≈ 1,2 % B) | Bursts ≥ 0,17 (≥ 10 Bilder); Funkenbündel ≥ 0,13 (≥ 8 Bilder); Ovalgruppe ≥ 9 s sichtbar (Ende offen) | #C0BAC7 / #A497AC; #C5A98B / #936F59 | z-am-condfin-container, z-am-condfin-loecher, z-am-condfin-funken-blech |
| `combat_bow` | `arrow`, im Flug unsichtbar; kein Pfeil im Ziel sichtbar (nur ferne Gegner) | (Exotic explodiert); Steckdauer **nicht belegt** | Flug 0,07 nah (4 Bilder) | – | z-im-ticuu, z-am-hoh-pfeil (exotisch) |
| `grenade_launcher` | `projectile`, Leuchtpunkt ≤ 1,5 % B, kein Schweif, Bahn fällt | `kern_s` 0,12–0,13 (kein bildweiter Blitz gemessen), Elementeffekt statt Feuerball | Flug 0,17–0,22 nah; Laufeffekt 0,05–0,2; Lache ≈ 5,6 s nach letztem Einschlag | je Waffe: Velocity Baton #F0E9FE / #5743BE, Chill Inhibitor #EEFEFE / #5151BA | z-im-velocity-baton, z-im-chill-inhibitor, z-im-witherhoard, z-im-forbearance |
| `rocket_launcher` | `projectile`, Glühpunkt 3–12 % B, kein Rauchzopf | `flash_s` 0,02–0,03 (bildweiter Blitz), getrennt davon `kern_s` 0,12–0,22; `ring_s` 0,07–0,13; Feuer 0,5–1,0; `smoke_s` ≈ 0,75–1,2; `light_s` 0,15 | Flug 0,32–0,65 | `core_color` #FCECDE, `fire_color` #E9B268 → #CA774A / #F3AF62 → #D53823, `ring_color` violett-rosa, `smoke_color` #020C08 | z-im-blue-shift, z-im-hoosegow, z-im-mos-epoch |
| `machine_gun` | Leuchtspur **nicht belegt** (violette Streifen im Schießstand beginnen nicht an der Mündung, [O]) | – | – | – | z-am-range-streifen |

¹ Handfeuerwaffe und Seitenwaffe: Spur und Loch als „nicht sichtbar“ belegt [O], ein Einschlag auf Wand oder Boden fehlt weiter ([11](#11-nachtrag-aftermath)). **Metall als Untergrund:** Funken ohne Staub und Säule ([z-am-range-metall](destiny2.md#z-am-range-metall)), Vergleich mit Fels/Beton nicht möglich.

## 8. Offen und nicht messbar

Damit keine Sitzung dieselben Wege erneut versucht:

- **m/s, Reichweite, Fall in m/s²** aus fremden Aufnahmen: keine Entfernung im Bild (Destiny ohne Distanzmaß; Halo-Schilder markieren Ziele,
  nicht den Schützen; Apex-Firing-Range-Videos nur 30/s ohne Abgangsbild). Bildbahnen enthalten Kamerabewegung (Phasenkorrelation r < 0,5).
- **Destiny-Fusionsbolzen und Pfeilfall:** Showcases schießen Fusionen in den Himmel; Pfeile sind im Flug unsichtbar; legendäre Bögen ohne Ziel.
- **Schrotkugelzahl am Bild:** Destiny zeigt je Schuss **einen** Einschlag (Rauchball, Funkenball an der Wand, Springbrunnen am Boden), kein
  Einzelmuster – auch an einer glatten Wand (Python 2019); Halo-Bulldog-Spuren überlappen (≥ 6). Nach 6.3.0: [11](#11-nachtrag-aftermath) – zwei Bursts und eine Lochgruppe je Schuss auf Blech.
- **Fusionsbolzen am Bild:** auch an einer Wand (Der Kluge Tadel 2017, 30/s) keine Bolzen und kein Einschlag sichtbar.
- **Einschlag auf Metall** in Destiny: nur Funken ohne Staub gesehen ([11](#11-nachtrag-aftermath)), **Vergleich mit Fels/Beton** weiter offen; **Handfeuerwaffe** auf Wand/Boden: in keiner Quelle (Showcases, Nexxoss-Guides, Schießstand 2025).
- **Kamerastoß bei Explosionen:** in den Raketenfenstern nicht sichtbar, Phasenkorrelation scheitert am Lichtwechsel; als „nicht gemessen“ führen.
- **Rauchaufstieg in % H/s und Decal-Dauer bei Explosionen:** Kamera schwenkt weg.
- **Einzellache Velocity Baton:** fünf Lachen überlagert; Witherhoard-Stern über Nachladen hinaus ≥ 6 s, Ende überlagert.
- **Velocity Baton Spezial oder schwer:** Menübild zeigt nur „GRENADE LAUNCHER“; die Zuarbeit nennt Spezial (Destinypedia), die Seite war
  ohne Inhalt abrufbar – REF 0.34 führt ihn als schweren Granatwerfer. Offen, nicht korrigiert.
- **Apex-Feuerwaffen-Einschläge, Titanfall-Werfer bei WFG** (Sandsturm), **Halo-Wandtreffer** (Drills nur auf Bots): andere Quellen nötig.

## 9. Prüfung und Zählung

**Zweitprüfung durch den Koordinator (31.10.2026):** 25 Videoquellen per yt-dlp geprüft (alle Kanal/Datum/Titel passend), 5 von 5 Text-URLs per
`curl` geladen (80.lv, Bungie.net Hardlight, Dexerto 6.3.0, Steam Screen Shake, EA Takeover). Am eigenen Einzelbild nachgemessen:

| Wert | Zuarbeit | Nachmessung | Ergebnis |
|---|---|---|---|
| Ikelos-Säule (f372), Lage | 47,5–52 % B × 37–57 % H | ≈ 47–51 × 39–58 % | bestätigt |
| Ikelos-Säule, Ende | „weg ≈ f430“ (Differenzmaß) | am Bild schwach f402–f404, weg ≈ f408–410 | **korrigiert** (Kamerabewegung im Maß) |
| Blue Shift Flugzeit (zweiter Schuss) | 39 Bilder | f5642 → f5681 = 39 | bestätigt (Ballista-Schuss 88,85 s: 27 Intervalle, anderer Schuss) |
| Blue Shift Feuerball (f5708) / Kuppel (f5690) | 19 × 31 % / Ø 24 % B | ≈ 23 × 35 % / ≥ 22 % B | bestätigt, als Spanne geführt |
| Hoosegow Flugzeit, Blitz | 28 Bilder, Blitz 4 | f13599 → f13627 = 28, Blitz 4 | bestätigt |
| Far Future „sofort“ | Blitz f234, Einschlag f235 | **Blitz f233–f234**, Einschlag im ersten freien Bild f235 | bestätigt, Blitzbeginn korrigiert |
| Chill Inhibitor Flugzeit | 11 Bilder | f976 → f987 = 11 | bestätigt |
| Halo Cindershot Flugzeit | 20 Bilder | f9869 → f9889 = 20 | bestätigt |
| Titanfall Charge Rifle Nachspur | 24 echte Bilder | Strahl ab f37396/98, schwache Linie noch f37452 | bestätigt (Untergrenze) |
| Python (Nexxoss) Wand | Leuchten im Blitzbild f7928, ein Funkenball f7930 | dasselbe an f7928 / f7930 / f7934 | bestätigt |
| Sauerstoff SG3 (Nexxoss) Treffer | Treffermarke und Lebensleiste im Blitzbild f3180 | Lebensleiste f3178 voll, f3180 gekürzt mit rotem X | bestätigt |

**Nicht übernommen:** Hydra-Geschwindigkeit (nur Suchauszug), die Typkorrektur Velocity Baton (nicht belegbar), die Outbreak-Dauern (Zeitlupe), Ravager und MA40 als Messzahl ([O]),
Zwei Sonnet-Anläufe (Halo, Apex/Titanfall) ohne Messzahl, mit Opus wiederholt.

**Zählung:** 4 Spiele, 25 geprüfte Videoquellen (19 Destiny, davon 3 Nexxoss mit Messzeilen und 1 gesichtet; 3 Halo, 2 Titanfall, 1 Apex),
21 Destiny-Messzeilen in destiny2.md (davon 2 [O]), 10 Vergleichszeilen, 31 Text- und Datenquellen (13 Spielerstimmen); gemessene native Einzelbilder
≈ 1500 (Agenten) plus ≈ 70 vom Koordinator. Nachgemessen 11 Werte: 9 bestätigt, 2 korrigiert (Ikelos-Ende, Far-Future-Blitzbeginn).

## 10. Nachtrag Nexxoss Gaming

Auf Hinweis des Nutzers (31.10.2026: Kanal mit vielen Waffenreviews) hat ein Opus-Unteragent die Kanalliste (1447 Videos, 611 mit „Destiny 2“)
nach Spielszenen mit HUD durchsucht; 9 Videos geladen, 4 tragen Zeilen. **Quellenbefund:** die Nexxoss-Videos ab 2018 sind 60/s-Container mit
**30 echten Bildern/s** (Paarduplikate, in 5 Videos geprüft), die von 2017 nur 1080p30 – Dauern deshalb in echten Bildern, umgerechnet „≈ n bei
60/s“ ±2. Kurze Vorgänge (Bolzen, Leuchtspuren von 1 Bild) können in 30/s verschwinden.

| Video (Nexxoss Gaming) | Waffe (Klasse), Spielstand | Befund | Zeile |
|---|---|---|---|
| 12.12.2019 · [yH6HtfktpC8](https://www.youtube.com/watch?v=yH6HtfktpC8) · 132,133 (f7928); Boden 107,05 (f6423) | Python (Schrot, Void), Season of Dawn – **vor** den festen Mustern von 6.3.0 | Wand: Leuchten im Blitzbild, Peak f7930 ein Funkenball 46–53,5 % B × 62–76,5 % H, keine Einzelkugeln; Boden: 13 Schüsse, je ein Springbrunnen 39–48 % B × 42–70 % H; Lauf: violette Schwaden 56–70 % B × 18–38 % H | [z-im-python](destiny2.md#z-im-python) [M] |
| 07.03.2019 · [c5EHzSOGy4w](https://www.youtube.com/watch?v=c5EHzSOGy4w) · 53,000 (f3180), 53,900 (f3234) | Sauerstoff SG3 (Scout), Season of the Drifter | Treffermarke und Lebensleiste im Blitzbild, keine Leuchtspur, Trefferleuchten ≈ 48–51 % B × 49–52 % H, Zahl „600“ +3 echte Bilder; Präzisions-Todesschuss: Zahl im Blitzbild, Zerfall grün-weiß | [z-im-sauerstoff](destiny2.md#z-im-sauerstoff) [M] |
| 16.10.2017 · [7aJg4idcsI4](https://www.youtube.com/watch?v=7aJg4idcsI4) · 116,78–117,42 (f3500–f3524) | Der Kluge Tadel (Fusion, Eisenbanner), Jahr 1 | Ringleuchten 6 echte Bilder, weißer Ball 19–20 % B × 22–26 % H mit Linsenstreifen, Flammenzungen 9 echte Bilder; keine Bolzen, kein Wandeinschlag (zwei gleiche Schüsse) | [z-im-tadel](destiny2.md#z-im-tadel) [M] |
| 16.06.2019 · [lR6e42dNZxw](https://www.youtube.com/watch?v=lR6e42dNZxw) · 64,43–64,73 | Schweigen (Bogen), Season of Opulence | Pfeil im Flug nicht sichtbar, Treffer-Aufblitzen am Gegner; Szene von einer Schnittblende überlagert; weiße Vollbilder im Video sind Schnittblenden | [O] |

Verworfen: Handfeuerwaffen- und Bogen-Form-Guides 2018 (keine Wand-/Bodentreffer, dunkel), Mond-Waffen-Guides 2019 (andere Waffe gespielt).
**Weiter offen (Stand 0.37):** Handfeuerwaffe auf Wand/Boden, Metall als Untergrund, Schrotmuster nach 6.3.0 am Bild, Pfeil-Steckdauer, Spurgewehr legendär,
MG-Leuchtspur – in 0.38 bearbeitet, Ergebnis in [11](#11-nachtrag-aftermath).

## 11. Nachtrag Aftermath

REF 0.38 „Aftermath“ (31.10.2026, Mac, Auftrag von Sightline): die offenen Punkte aus [8](#8-offen-und-nicht-messbar) und [10](#10-nachtrag-nexxoss-gaming) an fünf neuen Videos nachgemessen
(Nexxoss Gaming Dez. 2022 – Juni 2025, **60 echte Bilder/s**, Methode wie [Methode 31](destiny2.md#methode-31), Nachtrag [Methode 33](destiny2.md#methode-33)). Je Punkt: gemessen / nicht belegt.

| Punkt | Ergebnis | Zeile / Video |
|---|---|---|
| **Schrotmuster nach 6.3.0** | **gemessen.** Bedingte Endgültigkeit (exotisch, Doppellauf) auf Containerblech: **2 Bursts** je Schuss (Rosette ≈ 52–72 × 37–54 %, kleiner Burst ≈ 46–53 × 52–63 %, ≥ 10 Bilder, kein Rauch). Auf Lkw-Blech **bleibende Lochgruppen**: ein Schuss = **eine Gruppe** (Oval ≈ 9, ältere Dreiecksgruppe ≈ 12 Löcher, ±1; Loch ≈ 1,2 % B), zwei verschiedene Muster; Ovalgruppe am Einzelbild ≥ 9 s sichtbar, im Kontaktbogen bis ≈ 480 s, Ende offen. Vor 6.3.0 (Python): ein Funkenball, kein Decal. Ursache der zwei Muster (Lauf/Element, Winkel, Entfernung), Rahmen und Kugelzahl je Rahmen: **nicht belegt** (Exot mit zwei Läufen) | [z-am-condfin-container](destiny2.md#z-am-condfin-container), [z-am-condfin-loecher](destiny2.md#z-am-condfin-loecher), [z-am-condfin-funken-blech](destiny2.md#z-am-condfin-funken-blech) · `3HgrGEjz4HU` |
| **Metall als Untergrund** | **teilweise gemessen:** Riffelblech im Schießstand: viele kleine weiß-blaue Funken ≥ 12 Bilder, **kein Staub, keine Säule**; Schrot auf Blech: Funkenbündel ≥ 8 Bilder, kein Rauch. **Vergleich mit Fels/Beton nicht belegt** (kein Treffer auf Fels/Beton im Material; Ikelos-Video zeigt nur Schüsse auf Gegner) | [z-am-range-metall](destiny2.md#z-am-range-metall) · `NBUB9qubl54`; `dtVH4DbpqLE` ohne Messung |
| **Handfeuerwaffe auf Wand und Boden** | **nicht belegt.** Handfeuerwaffe/Sidearm im Schießstand schießt nur auf ferne Ziele (Mündungsfeuer sichtbar, kein Einschlag); kein Handfeuerwaffen-Review nach 6.3.0 mit Wandtreffern gefunden | `NBUB9qubl54` |
| **Pfeil-Steckdauer** | **nicht belegt.** Hierarchie der Ansprüche: Flugzeit ≈ 4 Bilder (±1) über unbekannte Entfernung, im Flug kein Pfeil und kein Schweif, nach dem Treffer kein Pfeil im Ziel – alle Schüsse auf ferne Gegner, keiner auf Wand/Boden/Metall | [z-am-hoh-pfeil](destiny2.md#z-am-hoh-pfeil) · `KGtGEMpka18` |
| **Spurgewehr legendär** | **nicht belegt.** „Verlängertes Engagement“ (`HPdfLN6knaQ`) ist eine legendäre **Maschinenpistole**; im Material kein legendäres Spurgewehr; Mikrokosmos ist exotisch (Videos `hEQHYpurLkI`, `mp8ImI8UbUc` nicht geladen) | – |
| **MG-Leuchtspur** | **nicht belegt.** Violette Streifen im Schießstand (3–6 Bilder, alle ≈ 6 Bilder) beginnen **nicht an der Mündung**, Magazin blieb konstant, Zuordnung zum Schuss unmöglich; Quelle (Spur, Querschläger, Gegnereffekt) offen [O] | [z-am-range-streifen](destiny2.md#z-am-range-streifen) · `NBUB9qubl54` |

**Korrektur zu [4](#4-muster-beobachtung-keine-gestaltungsregel):** „keine Einschusslöcher“ gilt für Kugelwaffen auf Beton, Fliesen, Erde und Sand (0.36), **nicht** für Schrot auf Metall.

### E3 – Vorschlag für BALLON (dort entscheiden)

- **Prüfen:** Schrot auf Blech als **ein Lochmuster je Schuss** (9–12 Löcher, ≈ 1,2 % B, heller Rand) mit nachgewiesener Lebensdauer ≥ 9 s (Ende offen) statt 12 Einzeleinschläge; Funkenbündel ≥ 8 Bilder ohne Rauch. Schrot nach 6.3.0 auf Fels/Beton/Sand/Erde ist nicht belegt; Kugelwaffen dort ohne Decal (0.36); Patchstand (Python 2019 vor 6.3.0, Wand) und Material (Blech) sind im Material nicht getrennt.
- **Ohne Beleg bleiben:** Handfeuerwaffen-Einschlag, Pfeil-Steckdauer, Spurgewehr-Strahl legendär, MG-Leuchtspur – BALLON-Werte hier nur aus den bisherigen Zeilen ([7](#7-für-ballon-034-payload--übernahmetabelle)).

### Quellen, Prüfung, offen

| Video (Nexxoss Gaming) | Inhalt | Verwendung |
|---|---|---|
| [3HgrGEjz4HU](https://www.youtube.com/watch?v=3HgrGEjz4HU) · 14.03.2023 · „Destiny 2 Lightfall: Bedingte Endgültigkeit Review“ | Schrot exotisch | 3 Messzeilen |
| [KGtGEMpka18](https://www.youtube.com/watch?v=KGtGEMpka18) · 12.12.2022 · „Destiny 2 Hierarchie der Ansprüche Review Deutsch German“ | Bogen exotisch | 1 Messzeile |
| [NBUB9qubl54](https://www.youtube.com/watch?v=NBUB9qubl54) · 03.06.2025 · „Destiny 2 The Edge of Fate: Schießstand/ Shooting Range“ | Schießstand, Primär/Sidearm | 1 Messzeile (2 Anker) |
| [dtVH4DbpqLE](https://www.youtube.com/watch?v=dtVH4DbpqLE) · 14.12.2022 · „Destiny 2 Ikelos MP V1.0.3 Review Deutsch German“ | SMG, nur Gegnerschüsse | keine Messung |
| [HPdfLN6knaQ](https://www.youtube.com/watch?v=HPdfLN6knaQ) · 15.12.2022 · „Destiny 2 Verlängertes Engagement Review Deutsch German“ | SMG (kein Spurgewehr) | keine Messung |

Fünf Sonnet-Unteragenten (medium) sichteten und maßen je ein Video; der Koordinator prüfte die Belegbilder (Containerburst f26772, Tür f27913, Loch-Vorher/Nachher f27906/f27960/f28500, Schießstand f5738, Pfeil f6416/f6420) am Einzelbild und zählte die Lochgruppen selbst; Hüllrechtecke des Containerbursts sind seine Ablesung (die des Agenten wich ab). Videos im Cache, nicht im Repo.
**Weiter offen:** Handfeuerwaffe auf Wand/Boden (ein Review nach 6.3.0 mit Wandtreffern, oder eigener Mitschnitt), Fels-/Betonvergleich zu Metall, Schrot-Muster je Rahmen (Mitschnitt mit bekanntem Rahmen), Pfeil auf Wand, legendäres Spurgewehr, ungeprüfte Fenster im Ikelos-Video (195–218, 229–243, 291–304, 371–457 s nur mit 1 Bild/s gesichtet).
