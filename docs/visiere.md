# Visiere in Videospielen – Typen, Durchblick, Form, Sitz und Zahlen

Referenzanalyse REF 0.14 „Eyebox“ (24.10.2026) für die Waffenreihe **BASIC** (Projekt `cubeescape-ballon`). Nur Videospiele, keine echten
Waffen. Hier stehen Beobachtungen und Messwerte. Der Abschnitt [Empfehlungen für BASIC](#11-empfehlungen-für-basic-cubeescape-ballon)
ist ein **Vorschlag**; entschieden wird in BASIC. Maschinenlesbare Fassung: [`data/visiere.json`](../data/visiere.json).

**Status:** **[M]** gemessen am Einzelbild (Raster 10 %, Mittenkreuz) oder per Bildvergleich; **[S]** Sekundärquelle (Wiki, Patchnotes,
Einblendung im Spiel); **[B]** Entwickler (Patchnotes, Studio, Community-Manager); **[C]** Community oder Zuarbeit einer anderen Sitzung (Antigravity), nur
stichprobenweise nachgeprüft; **[O]** Sichtung ohne belastbare Zahl. Mischangaben wie [C/S] nennen alle zutreffenden Stufen. Lage und Größe in Prozent der Bildbreite **B** bzw. Bildhöhe **H**, Ursprung oben links, Mitte 50/50 =
Zielpunkt, ±3 Prozentpunkte. Zeiten nur aus 60/s-Aufnahmen, ±1 Bild (16,7 ms). **Jede Zahl ist das Beispiel einer Optik mit
unbekanntem FOV des Aufnehmenden**, kein Klassenmittel.

## 1. Quellen und Methode

**Umfang:** 31 Spiele am Bild gesichtet (davon Halo Reach/5, Battlefield 1/V, Far Cry 6 und Metro Exodus nur durch Antigravity [C],
Quellen per yt-dlp geprüft): (Destiny 1/2, Marathon, Halo 3/Reach/5/Infinite, Battlefield 1/4/V/2042/6, CoD MW2019/BO6,
Apex, Titanfall 1/2, Valorant, CS2, Rainbow Six Siege, Overwatch 2, Borderlands 3, Cyberpunk 2077, Helldivers 2, The Finals, Warframe,
Arc Raiders, Tarkov, Insurgency Sandstorm, Far Cry 6, Metro Exodus), dazu ein Katalog der Scharfschützen-Darstellung in **100 Spielen**
und Spielerstimmen aus 51 Quellen. Gesichtet wurden rund 80 YouTube-Videos; die 34 Videos mit Zahlen in dieser Doku stehen mit
Kanal, ID und Hochladedatum in `data/visiere.json`, die Kernmessungen zusätzlich in `data/clips.json`. Videos und Bilder liegen nur im Cache
(`~/Library/Caches/CubeEscape/reference/visiere/`), nie im Repo.

**Ablauf:** wie [destiny2.md › 2](destiny2.md#2-messungen-an-60-fps-aufnahmen-ab-16-oktober-2026--m): `reference_frames.py fetch`
(yt-dlp, 1080p60 bevorzugt), Übersicht, dann Einzelbilder mit 10-%-Raster und Mittenkreuz; Zeiten bei `--fps native`.
Neu in dieser Version:

1. **Weltzoom als Bildmaßstab.** Verhältnis der Größe desselben Weltausschnitts im Zielbild zum Hüftbild, gemessen per
   Mehrskalen-Vorlagensuche (normierte Kreuzkorrelation; gültig ab corr ≥ 0,85 und Fundort nahe der Mitte) und gegengeprüft per
   Merkmalskette (ORB, RANSAC) über die Übergangsbilder. Ein HUD im Ausschnitt verfälscht die Kette (Halo Infinite: Kette 1,56, Vorlage
   4,15 – gilt die Vorlage).
2. **Glas gegen außen.** Dieselbe Messung einmal im Glas und einmal außerhalb: gleicher Wert = **eine Kamera**, größerer Wert im Glas =
   **eigenes Linsenbild (Bild in Bild, PiP)**.
3. **Bildmaßstab ist nicht der Winkelzoom eines Spiels.** Valorant nennt 1,25× / 1,5× / 2,5× als Winkelzoom; bei 103° horizontal
   ergibt das den Bildmaßstab tan(51,5°)/tan(51,5°/z) = 1,44 / 1,84 / 3,34 – gemessen 1,43–1,44 / 1,53–1,72 / 3,34 [M]
   ([Zeile](#v-valorant-operator)). Ein Zoomwert ohne Angabe der Art ist nicht vergleichbar.
4. **Werkzeugbefund:** `reference_frames.py sheet` beschriftet Kacheln bei niedriger Bildrate zu früh (jede Kachel zeigt ein Bild
   etwa eine halbe Abtastperiode **später**: 0,2/s ≈ +2,5 s, 0,1/s ≈ +5 s; von drei Sitzungen unabhängig gefunden). Zahlen hier
   stammen nur aus zeitgenauen Einzelbildern oder Bögen ≥ 5/s. Behebung als eigener Patch (siehe [LESSONS](LESSONS.md)).

**Arbeitsteilung und Prüfung:** Die Sichtung lief in dieser Sitzung (Battlefield, CoD, Apex, Halo, Titanfall 1) und in zwölf
Unteragenten nach gemeinsamer Methode; eine Antigravity-Sitzung lieferte den Hersteller-Katalog Destiny 2 und 14 weitere Spiele.
Nachgeprüft am eigenen Rasterbild (alle innerhalb ±3 Punkte): Destiny-Scout-Ring, Kasten-Reflex, SUROS-Glas, Häkke-Ringe,
Marathon Volt Thrower/Ares/Stryder/Longshot, Tex-Mechanica-Korn (Antigravity). **Nicht übernommen:** Antigravity-Angaben zu Ready or Not,
Delta Force, Payday 3, Crysis, Hunt und CoD 4 – die genannten Video-IDs gehören zu anderen Titeln/Kanälen (Prüfung per yt-dlp) – sowie
Spielerstimmen ohne prüfbare Adresse.

## 2. Durchblick – fünf Darstellungsarten

| Art | Was man im Zielen sieht | Waffe im Zielen | Außenwelt | Übergang | Beispiele |
|---|---|---|---|---|---|
| **A – 2D-Vollbild** <a id="v-art-a"></a> | gezeichnetes Bild (Kreis, Rechteck, Fenster), außen schwarz oder Vignette | ausgeblendet | schwarz | harter Schnitt nach kurzer Hebebewegung | Scharfschützen in Destiny 2, Halo, BF4 ab 6×, CS2, Valorant, Titanfall 2, Marathon, Overwatch 2, Borderlands 3 (Vladof/Hyperion/Jakobs/Maliwan), Arc Raiders |
| **B – HUD-Überlagerung** <a id="v-art-b"></a> | holografischer Rahmen mit Anzeigen über der Welt | ausgeblendet | sichtbar, abgedunkelt | Schnitt in 1 Bild | Halo 3 (Karabiner 2,33×, Schnitt 190,858 → 190,874), Halo Infinite Smart-Link, Warframe |
| **C – 3D-Visier, eine Kamera** <a id="v-art-c"></a> | Visiermodell vor dem Auge, Glas zeigt dasselbe Weltbild | sichtbar (Gehäuse, Sockel, teils Hände) | scharf oder tiefenunscharf | Modell wandert zur Achse, Zoom läuft mit | gemessen: Apex (3× Ranger: Glas 2,43× = außen 2,51×), BF2042 (mittleres ZF: Glas 3,83× = außen 3,86×); gesichtet: BF4 bis 4×, Valorant, Marathon, Siege, Destiny 1/2 (Holo, Ring, Scout – Glas gegen außen in Destiny **nicht belegt**, siehe [12](#12-offen-und-nicht-messbar)) |
| **D – 3D-Visier mit Linsenbild (PiP)** <a id="v-art-d"></a> | Glas zeigt ein eigenes, stärker vergrößertes Bild | sichtbar | außen weniger vergrößert | Modell wandert, Linse ggf. kurz dunkel | Tarkov (außen 2,4×, Glas zusätzlich 2,3–3,7×), Insurgency Sandstorm (schaltbar), Helldivers 2, The Finals, Cyberpunk (große Optiken), Wärmebild-Optiken in MW2019 und BF6 |
| **E – kein Zielen** <a id="v-art-e"></a> | Hüftbild bleibt, nur Fadenkreuz | Hüftlage | unverändert | – | CS2 (außer Zielfernrohren), Valorant-Pistolen/Schrot (nur Alternativfeuer), Overwatch Cassidy, Halo 3/Reach bei Nahkampfwaffen |

**Scharfschützen in 100 Spielen** (Katalogvideo Tigerfield `MM9db665Urg`, 60/s, ±4 Punkte; 101 Zuordnungen, weil *Rising Storm 2:
Vietnam* zwei Zielfernrohre zeigt) <a id="v-katalog-100"></a>: A 53, C 36, B 6, D 5, sonstige 1. A dominiert bis 2013 (80 % bis 2005, 60 % 2010–13), C steigt ab 2014 auf 55 %; D erst ab 2016 (Tarkov, Day of
Infamy, Sandstorm, Ring of Elysium; Ausnahme Contract Wars 2010). Call of Duty wechselt mit *Ghosts* (2013) von A auf C, Battlefield
bleibt überwiegend A (auch BF5), Counter-Strike, GTA und STALKER durchgehend A, Crysis und Killing Floor durchgehend C. Typ-A-Scheibe meist
80–100 % H (Median ≈ 90 %), Typ-C-Öffnung 40–85 % H.

**Was ausgeblendet wird:** In C/D blenden alle gesichteten Spiele beim Zielen das Okular-Rohr aus oder schieben es hinter die
Kamera; sichtbar bleiben Objektivring, Sockel und Waffenoberkante (Destiny-Scout: Ring, trapezförmiger Hals ≈ 16 % B, Kimmenblock
≈ 8 % B, keine Hände, kein Lauf). Hände verschwinden in Destiny im Zielen fast immer. In A und B verschwindet die ganze Waffe.

**Unschärfe außen:** scharf in Destiny 2, Marathon, Apex, Tarkov, Helldivers 2, The Finals, Titanfall; tiefenunscharf in Destiny 1,
BF2042/BF6, MW2019, Insurgency Sandstorm, Cyberpunk; abgedunkelt in Halo (Smart-Link-Vignette). BF6 schaltet seit Update 1.4.3.0
(15.09.2026) das Linsenbild auf Wunsch ab [S].

## 3. Visiertyp je Waffenklasse

Typ der Grundausstattung, wie gesichtet [M/O]. „Klammer“ = offenes Eisenvisier mit leuchtenden Klammern um den Punkt (Destiny).

| Klasse | Destiny 2 | Destiny 1 | Marathon | Halo Infinite | Apex | Titanfall 2 | Valorant | Battlefield / CoD |
|---|---|---|---|---|---|---|---|---|
| Automatik/Sturmgewehr | Ring (Häkke), Rundrechteck-Glas (SUROS), Keile (VEIST), Quadratglas (DEO) | Holo/Rotpunkt wählbar | Display-Visier, Ring | Holo-Anzeige auf Stiel | Kimme, Holo, HCOG | Kimme mit LED, HCOG-Ring | Kimme mit Dreieck | Rotpunkt/Holo/Prisma/ZF wählbar |
| Impuls/Salve | Ring, U-Rahmen, Hologramm | Holo, Ring | – | Rohr-ZF (BR75) | – | – | – | – |
| Scout/DMR | Ring-ZF (Scout), Kasten-Reflex | Ring-ZF, Kasten mit Rundloch | Kimme, Display | Rohr-ZF | ZF wählbar | – | – | ZF wählbar |
| Handfeuerwaffe/Pistole | Kimme/Korn + Klammer | Kimme | Kimme mit Mini-Display | Kimme | Kimme | Kimme mit Ziffer | Kimme (kein ADS) | Kimme, Pistolen-ZF (CoD) |
| Sidearm | Klammer „( • )“ / „[ • ]“ | – | – | – | – | – | – | – |
| MP | Rundrechteck, Keile, U-Rahmen | Holo | Reflex mit Display | – | Holo | Holo mit Klammern | Kimme | Rotpunkt |
| Schrotflinte | U-Kimme, Klammern | – | – | – | – | Kimme mit Lampen | – | Kimme, Ringkorn |
| Scharfschütze | A: Kreis 80–83 % H, kein Fadenkreuz | C: Ring-ZF | A: Rechteck/Display je Waffe | B: Rahmen 5×/10× | C: Ring/Display | A: Kreis 65 % B | A: Kreis ≈ 60 % B | A (BF4) / C (MW2019) |
| Fusion / Energie | Ring, Doppelring, Bögen | – | – | – | – | – | – | – |
| Werfer | runde Linse, Chevron statt Punkt | – | – | – | – | Klappvisier mit Display | – | – |
| Bogen | Pfeilspitze, kein Visier | – | – | – | Ständer am Griff | – | – | – |

**Muster:** Destiny ordnet die Form dem **Visiertyp** zu, nicht der Klasse – Eisen = Klammer, Holo/Reflex = Glas mit Grafik, ZF = Ring,
Scharfschütze = Vollbild; die **Farbe und Grafik** zeigt den Hersteller ([Abschnitt 5](#5-form-rahmen-gehäuse-silhouette)). Halo und
Valorant vermeiden echte Optiken (HUD statt Glas); Titanfall gibt fast jeder Waffe ein eigenes Visier mit digitaler Anzeige.

## 4. Zahlen im Zielen

Öffnung = lichte Öffnung (Glas, Ring innen); Gehäuse = Außenkontur in Bildbreite; Rahmen/Öffnung = Rahmenstärke je Seite geteilt durch
die Öffnung; Weltzoom = Bildmaßstab Hüfte → Zielen außen. Zeiten: Bewegungsbeginn bis ruhig, 60/s.

| Spiel · Optik | Art | Öffnung % B | Gehäuse % B | Rahmen/Öffnung | Weltzoom | ADS ein | Quelle (Kanal, ID, Datum, Zeit) |
|---|---|---|---|---|---|---|---|
| **Destiny 2 · Scout-Ring (Patron of Lost Causes)** <a id="v-d2-scout"></a> | C | 20,8 (36 % H) | 26,9 (46 % H) | 0,15 | 2,0 (ein Paar) | 0,20–0,25 s; aus 2–3 Bilder (Schnitt) | DFP, `1ERmScNiOk4`, 09.02.2023, 4:04,5 / 4:11,8 [M] |
| **Destiny 2 · Kasten-Reflex (andere Waffe)** <a id="v-d2-kasten"></a> | C | 19,8 (25,6 % H) | 23 (30 % H) | 0,08 | – | – | DFP, `1ERmScNiOk4`, 8:34 [M] |
| **Destiny 2 · SUROS-Glas (Foggy Notion, MP)** <a id="v-d2-suros"></a> | C | ≈ 11,5 (28,8 % H) | Glas ohne Gehäuse, Linie 2–3 px | – | – | – | Ultraclocked, `IG-GZ72Vbi0`, 14.02.2020, 207 s [M] |
| **Destiny 2 · Häkke-Ring (Call to Serve, Scout)** <a id="v-d2-haekke"></a> | C | ≈ 12 (Ø 22 % H) | Ring, Strich 1,4 % H, Lücke oben | ≈ 0,06 | – | – | Ultraclocked, `73lGCT7yOtk`, 25.01.2020, 131 s [M] |
| Destiny 2 · Automatik-Holo (Chroma Rush) | C | – | 16 (Holo 42–58 %) | – | 1,84 | 0,30 s (Modell 0,18 s) | [destiny2.md](destiny2.md#s-automatik-showcase) [M] |
| Destiny 2 · Saint's-Scout-Glas | C | – | – | – | – | Linse klar in ≤ 3 Bildern | DFP, `1ERmScNiOk4` [M] |
| Destiny 1 · Ranged Lens RLR5 | C | 24 (44 % H) | 31,6 (57 % H) | 0,15 | Einblendung 2,8× [S] | – (30/s) | Jumping Puzzle, `MkkQa1OIpDk`, 05.03.2015, 3:43 [M] |
| Destiny 1 · Focus Lens FLA5 (Kasten mit Rundloch) | C | 25,6 | 33,5 (56 % H) | 0,18 | 2,6× [S] | – | ebd., 4:32 [M] |
| Destiny 1 · Rotpunkt-Kasten OAS | C | 17,5 (28 % H) | 23,4 | 0,10–0,23 | 2,2× [S] | – | ebd., 1:55,5 [M] |
| **Marathon · V22 Volt Thrower (Display-Reflex)** <a id="v-marathon"></a> | C | 22 (19 % H) | 25 | 0,07 | ≈ 1 | – | soda, `QxZAflLtJRQ`, 04.06.2026, 150 s [M] |
| Marathon · Ares RG (Display, Pixel-Sockel) | C | 25 (20 % H) | 34,5 | 0,16–0,2 | ≈ 1 | 0,2–0,3 s | ebd., 800 s [M] |
| Marathon · Stryder M1T (Ring) | C | 9 | 13,8 | 0,26 | ≈ 1 | – | ebd., 676 s [M] |
| Marathon · V75 Scar (Kimme, Pixelkontur) | C | Kerbe 14 | 24 | – | ≈ 1 | 0,18 s (11 Bilder) | ebd., 364,45 s [M] |
| Marathon · Longshot / Channel Rifle / Thermal | A | Fenster 82 / 86 / 96 | – | – | ≈ 4–5 [O] | – | ebd., 734 / 763 s; Aculite `FEW1ZkadfM8` [M] |
| **Apex · 1× HCOG Classic** <a id="v-apex"></a> | C | 15 (22 % H) | Ring ≈ 1 % je Seite | ≈ 0,07 | – | – | ClawZ, `UetKaZiF9uA`, 25.11.2020, 75 s [M] |
| Apex · 1–2× Variable Holo | C | 18 (35 % H) | Leuchtrahmen dünn | ≈ 0,05 | Fenster bleibt bei 2× gleich groß | – | ebd., 87,5 / 95 s [M] |
| Apex · 3× HCOG Ranger (Kraber) | C | 26 | 37 | 0,21 | 2,5 (Glas 2,43 = außen) | 0,20 s (12 Bilder) | Skeptation, `gCQHKNsIU9w`, 08.11.2021, 28,3–28,5 s [M] (Mod-Client R5Reloaded) |
| **BF2042 · Rotpunkt** <a id="v-bf2042"></a> | C | 9,4 (10 % H) | ≈ 11 | ≈ 0,1 | **1,68** | 0,133 s (8 Bilder) | SammyBoiii: FPS, `enyEjb4dXU8`, 17.02.2022, 39,94–40,07 s [M] |
| BF2042 · mittleres ZF | C | 23 | 38 | 0,33 | 3,86 (Glas 3,83) | – (Schnitt) | ebd., 122,8 s [M] |
| BF2042 · Scharfschützen-ZF | C | Okularring füllt Bild | – | – | ≥ 8,8 | 0,35 s (≈ 21 Bilder) | ebd., 128,46–128,81 s [M] |
| BF4 · Holo EOTech | C | 23 (31 % H) | 39 | 0,35 | – | – (30/s) | WiciuXshooter, `q2j9kG3S4vA`, 30.08.2018, 17 s [M] |
| BF4 · Coyote / HD-33 / PKA-S | C | 21 / 20 / 24,5 | 22 / 33 / 34 | 0,05 / 0,3 / 0,2 | – | – | ebd., 32 / 62 / 72 s [M] |
| BF4 · M145 3,4× | C (Tunnel) | 30 (52 % H) | 60 | 0,5 | – | – | ebd., 107 s [M] |
| BF4 · Scharfschütze 6–40× | A | Kreis ≈ 45 % B / 80 % H | – | – | 6–40× [S] | – | ebd., 221 s [M] |
| CoD MW2019 · Cronen 2x2 Elite | C | 22 | 30 | 0,18 | 2,9 außen | – (30/s) | Hoodiewaffles, `qI_IWMuH_Zs`, 18.08.2020, 15,0–15,2 s [M] |
| CoD MW2019 · Reflex / Brownlee / PU Scope | C | 10 / 33 / 47 | ≈ 15 / 40 / 56 | ≈ 0,25 / 0,1 / 0,1 | – | – | ebd., 82 / 112 / 240 s [M] |
| **Halo Infinite · Commando 3,0×** <a id="v-halo"></a> | B | Rahmen 25–72 % B | – | – | **4,15** | Schnitt 134,500 → 134,517 | Abyssopelagic, `ZfNuA5r-470`, 30.07.2021, 134,5 s [M] |
| Halo 3 · Karabiner | B | Wabenrahmen 32–68 % B | – | – | 2,33 | Schnitt in 1 Bild | Weapons From Games, `X_ADv1HMwkg`, 14.07.2020, 190,86 s [M] |
| Titanfall 2 · HCOG (R-101) | C | 19 (34 % H) | 28 | 0,24 | 1,00 | ≈ 0,2 s | Weapons From Games, `4sDwTD9U8bw`, 184–188 s [M] |
| Titanfall 2 · Longbow / Kraber | A | Kreis 65 % B | – | – | – | Overlay ≤ 2 Bilder nach 0,2–0,25 s Hebung | ebd., 548,8 / 590,2 s [M] |
| **Valorant · Operator** <a id="v-valorant-operator"></a> | A | Kreis 58–62 % B | – | – | 3,34 (2,5× Winkel) | Schnitt | Skovos, `WH5xpA7tfY8`, 7:10 [M] (30/s) |
| Valorant · Stinger / Phantom (Kimme) | C | Kimme ≈ 10 | Waffe 22 | – | 1,25–1,27 / 1,43–1,44 | – | ebd., 233 / 367 s [M] |
| Siege · Reflex/Holo (#3, #4, #7) | C | 11–16 | 20–28 | 0,25–0,4 | – | – | BeastModPlayer, `Wib_5yd2mWk`, 15.04.2024 [M] |
| Siege · Ring-ZF (#1, #10) | C | 21–27 | 33–41 | 0,25–0,3 | Glas vergrößert [O] | – | ebd. [M] |
| CS:GO · AUG (Szene von 2018 im CS2-Video) | D | 28–31 | 61–74 | ≈ 0,6 | außen nicht gemessen; Glas 2,6–2,7 gegen Hüfte | – | NartOutHere, `fIscQmMHys4`, 02.05.2025, 0:15–0:25 [M] |
| Overwatch 2 · Widowmaker / Ashe | A / C | Ring ≈ 50 % B / Hörner-Korn 41–59 % | – | – | ≈ 6 [O] / 1,6 | Waffe weg innerhalb ≤ 0,1 s (nur 10/s abgetastet), Overlay 0,4–0,5 s | iFaiiLed `Qh7gYQpSq0Y`, 07.11.2022, 22,7–23,3 s; lonesomary `NH0Qs8EXWOY`, 08.06.2025, 37,2 s [M] |
| The Finals · Holo / Magnifex | D | 15,6–18 | 21–25 | ≈ 0,1–0,2 | 1,3 außen (Bildpaar 290,98 / 291,45 s) | Gesamtdauer nicht belegt; Wechsel Hüftbild → Zielbild zwischen 291,017 und 291,033 s (Schnitt im Video möglich) | HazedNConfused, `ILLTAgWBT4w`, 17.09.2025, 291 s [M] |
| The Finals · PIKE-556-ZF | D | 29–33 | 56 | 0,15 | – | aus ≤ 0,25 s | ebd., 63 s [M] |
| Helldivers 2 · Sightliner / AMR-20 | D | 18–21 / 20 | 22–31 / 38–42 | ≈ 0,15 | – | Schnitt, Linse 5 Bilder schwarz | Jumpycode, `VawsGNra7tg`, 20.10.2026, 113,75 s [M] |
| Tarkov · ACOG / PSO-1 / EOTech | D / D / C | 28 / 28 / 12 | 51 / 38 / 20 | – | außen 2,43 / 2,43 / 1,3; Glas gegen Hüfte 8,0 / 8,8 / – | – | Syrekx, `aGkRvi6V0O8`, 30.09.2023, 1:50 / 8:13 / 4:34 [M] |
| Borderlands 3 · Vladof 3,3× / 5,0× | A | Kreuz 23–76 % B / Kreis 93 % B | – | – | 3,32 / 4,99 (= Teilname) | 0,30 / 0,35 s | Agent Lomax, `Nwp4VJWUujY`, 02.10.2019, 334 / 337 s [M] |
| Borderlands 3 · Hyperion 4,4× | A | Fünfeck-Rahmen | – | – | 4,47 | 0,65 s inkl. Beruhigung | Agent Lomax, `3T2UZUYPzEc`, 15.03.2020, 384 s [M] |
| Cyberpunk · Prospecta / Reflexe | D / C | 41 / 4–10 | 53 / 6–14 | – | Glas > außen [O] | – | Akooma, `crGei3_OARY`, 16.12.2020 [M] |
| Warframe · Vulkar | A | Kreis 62 % B | – | – | 2,8 | – | MCGamerCZ, `te0K_V1U2ok`, 28.12.2015, 168 s [M] |
| Arc Raiders · Osprey-ZF | A | Kreis 50 % B (89 % H) | – | – | ≈ 4–6 [O] | – | TayXDc, `MlK0E83JfEE`, 03.11.2025, 332 s [M] |

**Bildanteil der Öffnung (Reflex/Holo/Kimme, offene Visiere):** Destiny 12–20 % B, Apex 15–18, Marathon 15–25, The Finals 16–18,
BF2042 9, BF4 20–24, Siege 11–16, Tarkov 12, CoD-Reflex 8–10. **Zielfernrohr (C/D):** Destiny 21–26, Apex 26, BF2042 23, BF4 30,
Helldivers 18–21, The Finals 29–33, Tarkov 28–36, CoD 14–47.

**Titanfall 1 – das Visier ist nicht FOV-unabhängig** <a id="v-tf1-fov"></a>: Bei FOV 70 → 90 → 112 wächst die Öffnung im Bild
(HCOG 12,4 → 14,1 → 15,7 % B, Holo innen 13,6 → 14,7 → 16,7 %, AOG-Ring 35,0 → 38,9 → 44,6 %; +23–28 %) [M] (Kat, `Ny7bw5dXwPo`,
11.07.2023). Bei fester Winkelgröße wäre sie auf ≈ 47 % geschrumpft; das Spiel skaliert das Waffenmodell also gegenläufig.
Bildanteile gelten deshalb nur zusammen mit dem FOV.

## 5. Form: Rahmen, Gehäuse, Silhouette

**Rahmenstärke ist nicht die Ursache von „klobig“.** Destiny-Ringoptiken haben über D1 und D2 stabil Rahmen/Öffnung 0,15–0,19 und
Außen/Innen 1,30–1,38 [M]; Reflex-Kästen 0,08. Klobig wirken Optiken, deren **Gehäuse groß und hoch im Bild steht** (D1-Zielfernrohre
33–36 % B, BF4-Holo 39 % B mit 8 % B Rahmen je Seite, Siege 3,5–4,5 % B je Seite bei 11–16 % Fenster, Sandstorm-Kasten bis 73 % B)
oder deren **Sockel als Block ohne Verjüngung** darunter steht.

**Destiny 2 – Hersteller-Sprache** (Antigravity [C], 8 Hersteller, 31 Waffen, 17 Videos; Stichprobe Tex Mechanica nachgeprüft;
dazu Absehen-Sichtung [M]) <a id="v-d2-hersteller"></a>:

| Hersteller | Silhouette | Rahmen ↔ Öffnung | Farbe, Leuchten | Sockel |
|---|---|---|---|---|
| Häkke | dünner Metallring mit Lücke oben (Ø 22–31 % H), flache Trapezprofile | Ring 1,2–1,5 % B bei ≈ 12 % B Öffnung | Oliv, Sand, Stahl; grüne Ziffern im Sockel | niedriger gefaster Trapezsockel |
| SUROS | glasloses Holo-Rundrechteck, Bögen, schlanke Trapezhauben | Leuchtlinie ≈ 0,4 % B; Wand 1,5 % B bei 9 % B | Weiß, Karmin, Chrom; Cyan/Violett-Linien, Munitionszähler | ins Gehäuse integriert, keine Schrauben |
| Omolon | dünnwandiger Tubus, rahmenloses Holo | Tubus 2,5 % B bei 25 % B (1:10); Holo 0 | Schiefer, Petrol, Koralle; Flüssigkeitstanks | eingegossen |
| VEIST | V-Zinken oben offen, Keile mit Skala | Seitenstege ≈ 2,5 % B bei 14–15 % B | Anthrazit, Tarnung; Neongrün | flach, keilförmig verjüngt |
| Tex Mechanica | U-Kimme, Korn mit Schutzflügeln, Messingbügel | U-Kerbe 1,2–3 % B | Brüniert, Nussbaum, Messing; kein Leuchten | in Lauf/Schlitten gefräst |
| Cassoid | schlanke Rohre, offene dünne Bronzeringe | 1,5–1,8 % B bei 11–18 % B | Bronze, Perlweiß, Gold; Void-Violett | Brückenmontage |
| Nadir | Trapezhauben, gefaste Rechteckkästen mit schmalem Dachsteg | 1,5 % B bei 13–17 % B | Weiß, Anthrazit, Blau; rote Pfeile | 45°-gefaste Sockel |
| Daito | schwebende Bögen, seitliches Display (Two-Tailed Fox) | 0,8 % B bei 11 % B | Mint, Weiß, Sakura; goldene Holo-Linien | eingegossen |

Wiederkehrende Mittel (Antigravity [C], an eigenen Bildern bestätigt): Wand ≤ 1,5–2,5 % B, Verhältnis Wand : Öffnung 1 : 8 bis 1 : 12;
offene Formen ohne Dachsteg (Häkke-Ringlücke, VEIST-Zinken, SUROS ohne Glasrahmen); Gehäuse verjüngt sich nach oben; Anzeigen
(Munition, Status) sitzen **unter** der Visierlinie im Sockel; die Waffe taucht im Zielen ab, ihre Oberkante liegt bei 62–70 % H,
die obere Bildhälfte bleibt frei; Visiergehäuse neutral dunkel oder hell poliert, das Absehen trägt die Farbe.

**Marathon (Bungie 2026)** [M] <a id="v-marathon-form"></a>: Blockformen mit Treppen-/Pixelkontur statt Fasen; Rahmen/Öffnung
0,07–0,2; Öffnungen abgerundete Rechtecke oder Ringe; im Glas Anzeigen (Mini-Absehen, Entfernungsstriche, Lineal, Ziffern); Visier
schwarz/dunkelgrau mit **einem** Akzent (Cyan-LED, Limonengrün `≈ #C8FF00`, rotes Band), Waffenkörper bunt; Zielfernrohre sind
2D-Vollbilder mit eigener Kontur je Waffe (4:3-Kasten, Rundrechteck, Camcorder, violettes Wärmebild), nie ein Kreis.

**Borderlands 3** [M]: das Absehen ist das Herstellerzeichen (Vladof rotes Kreuz mit Schrift, Hyperion Cyan-Fünfeck, Jakobs Goldring
≈ 7 % B mit Filigran, Maliwan Doppelring ≈ 36 % B mit Element). Vier Hersteller wechseln im Zielen auf Vollbild (A), Dahl/Torgue/
Tediore behalten das 3D-Visier; Dahl und Torgue haben bewusst dicke Rahmen (Markenmerkmal). Trotz Comic-Stil sind die Absehen dünne
Leuchtlinien (0,3–1 % B) vor dunkler Vignette.

**Titanfall 2 / Apex** [M]: dünne Leuchtrahmen (Cyan) um große Öffnung; fast jedes Titanfall-Visier hat eine digitale Anzeige
(LED-Balken, Ziffern); Apex-Waffen tragen einen Munitionszähler am Gehäuse.

**Silhouetten-Familien:** Ring (Rohr von hinten; Destiny, Apex, Titanfall), Kasten mit Rundloch (D1 FLA5, Halo S7), offenes
Rundrechteck/Holo (SUROS, Apex Holo, The Finals), Display/Bildschirm (Marathon, Cyberpunk Tsunami, Daito), offener Rahmen über die
Waffe (Apex L-STAR/Prowler, BF6 SU-231), Stiel mit Fenster (Halo MA40).

## 6. Sitz auf der Waffe

**Faustregeln von außen** (Gunsmith/Inspektion CoD MW2019, Apex, Halo Infinite, BF6; Schätzung am Raster, ±0,2 D bzw. ±5 % L;
D = Gehäusehöhe ohne Magazin/Griff, L = Waffenlänge) [M/O] <a id="v-sitz"></a>:

| Visiertyp | Laufachse → Visierlinie | Visier über Gehäuseoberkante | Länge | Lage | Sockel |
|---|---|---|---|---|---|
| Reflex / Holo | 1,0–1,3 D | 0,4–0,7 D | 8–12 % L | Mitte, über Auswurf/Magazin | flacher Block oder Schiene |
| Offener Rahmen / Tragegriff | 0,9–1,2 D | 0,3–0,6 D | 30–60 % L | über dem ganzen Gehäuse | integriert |
| Kurzes ZF (2–4×) | 1,3–1,7 D | 0,8–1,2 D | 12–18 % L | Mitte | Block oder zwei Ringe |
| Kasten / Prisma | 1,2–1,6 D | 0,6–1,1 D | 15–22 % L | hintere Hälfte (Bullpup vorn) | hoher Block mit Hebel |
| Langes ZF (4–7×) | 1,6–2,0 D | 1,1–1,6 D | 22–30 % L | Mitte bis hinten | zwei Ringe |
| Pistolen-Optik | 1,0–1,6 × Schlittenhöhe | – | – | hinterer Schlitten | Ring/Block |
| Eisenvisier | – | 0,25–0,5 D | – | Enden | Klappkimme/Korn |

**Destiny** sitzt tiefer als die Militär-Shooter: das Scout-Rohr liegt **direkt auf der Gehäuseoberkante** (Lücke ≈ 0), Rohr-Ø
≈ 0,45 × Gehäusehöhe, im hinteren Drittel [M]; D1-Kästen auf niedrigem Riser (Lücke ≈ 0,45 × Kastenhöhe). In der Hüfte ist das
Destiny-Okular nur 6–9 % B groß. **In der Ego-Ansicht** liegt jedes Visier im Zielen auf dem Zielpunkt; in der Hüfte rechts unten
(Tarkov x 60–85 %, y 46–78 %; Destiny siehe [Steckbriefe](destiny2.md#3-steckbriefe-je-waffentyp--lage-im-bild-zielpunkt-visier-arme-aktionen-bildvermessung-mit-mittenkreuz-18-oktober-2026--m)).

**Zielpunkt-Höhe Destiny** [M, offen]: In den Ultraclocked-Showcases von 2020 und in Destiny-1-Clips liegt der Punkt bei ≈ 57 % H
(7 % unter der Bildmitte), in Aufnahmen ab 2022 bei 50 % H. Ob Spielwert oder Aufnahmeversatz, ist nicht geklärt.

## 7. Absehen

**Destiny 2 – zwei Schichten** (50 Waffen, Ultraclocked 2020/2025/2026 und DFP 2023) [M] <a id="v-absehen"></a>: ein **HUD-Punkt**
fest am Zielpunkt (rot `#B90518`–`#EB2D43`, 8–16 px = 0,7–1,5 % H, ohne Glow) und das **3D-Visier** mit Glasgrafik, das mit der Waffe
kickt; der Punkt bleibt stehen. Glasgrafik 2–3 px (0,2–0,3 % H), Ringe 1–1,5 % H; nichts kreuzt den Punkt, keine durchgehenden
Fadenkreuze. **Schuss** = Ring um den Punkt (16–24 px) im Bild nach dem Mündungsfeuer; **Treffer** = rotes X (40–50 px, ≥ 0,17 s);
**kein Aufblühen im Zielen** (Ring konstant über 1,3 s Dauerfeuer). Glasgrafik leuchtet erst in den Waffen von 2025/26 (weicher
Bloom). Größen: Klammern 5–9 % H, Ringe 20–31 % H, Glas 20 × 23–33 % H, Scharfschützen-Kreis 80–83 % H.

**Vergleich:** Destiny 1 Ring-Punkt 6 % H mit Gegnerkasten; Apex dünner gelber Ring + Punkt 4,2 % H; Halo Infinite reines HUD,
weißer Ring 1,9 % H mit Bloom auf 7,8 % H bei Dauerfeuer; CoD MW2019 schwarze Fadenkreuze mit rotem/amber Punkt im Glas;
Marathon hauchdünne Linien (≈ 1 px, Ringe 0,3 % B); Borderlands Herstellerfarbe; Valorant sechseckiger HUD-Ring über dem Visier.

## 8. Glas und Leuchten

[M], Helligkeit innen/außen per Pixelprobe, ±10–15 Punkte <a id="v-glas"></a>:

- **Destiny:** kaum Tönung (Himmel in kurzen Ringoptiken 0,98–1,01 der Außenhelligkeit; Saint's Scout −20 bis −30 % mit
  Violettstich). Wertigkeit über einen **dünnen Leuchtring am Linsenrand** (2–5 % der Gehäusebreite) und mattes, verwittertes Metall.
  **Kein Staub, keine Kratzer, kein Zellmuster** auf dem Glas, keine Reflexe im Zielen. Von außen (Hüfte) ist die Linse eine dunkle
  violette/blaue Scheibe mit Glanzpunkt; beim Anlegen klar in ≤ 3 Bildern.
- **Vergleich:** MW2019 stärkste Tönung (20–35 %, Bernstein/Oliv); BF6 Grün-Grau-Stich, Objektiv von außen schwarz mit Lichtpunkt;
  Apex Leuchtränder Cyan/Blau; Halo kein Glas, nur Vignette; Titanfall der Leuchtring ist das Visier, Glas klar; Tarkov heller
  Glanzverlauf unten; Sandstorm dunkles Glas mit Randabfall.

## 9. Spielerstimmen

51 Quellen (Steam, EA-Foren, bungie.net, Presse mit Reddit-Zitaten, Patchnotes); Reddit war nicht direkt erreichbar, Threads klein
(2–70 Antworten) – **Richtungsindiz, keine Mehrheitsmeinung** <a id="v-stimmen"></a>:

1. **Gewünscht:** dünne, flache Gehäuse oder glaslose Punkte, die Ziel und Umfeld frei lassen (CoD Cronen Mini Pro, Slimline Pro,
   JAK Glassless; BF4 HD-33/Cobra; Apex 1× HCOG statt Holo) [C/S], wiederkehrend.
2. **Abgelehnt:** dicke Rahmen, die Ränder versperren (CoD Corio RE-X Pro, BF4 PKA-S/Holo), und zu große Rotpunkte (BF6-Start).
   DICE hat am 15.09.2026 (Update 1.4.3.0) alle Absehen verkleinert, Linien geschärft und das Leuchten verstärkt [B].
3. **Gewünscht:** Absehenfarbe, -größe und -kontrast einstellbar, vor allem bei Rot-Grün-Schwäche und hellem Himmel (BF6, Destiny 2
   seit 2019 – ADS-Absehen ignorieren dort die Farbeinstellung –, Apex 2021) [C], stark wiederkehrend.
4. **Abgelehnt:** nicht abschaltbare Unschärfe außerhalb der Optik (BF2042, BF6, Sandstorm), einzelne berichten Übelkeit [C].
5. **Gespalten:** eigenes Linsenbild (realistischer, aber Bildrate und Unschärfe; Squad-Entwickler hält es für zu teuer) [C/B];
   Scope-Glint (Fairness vs. Übergröße) [C].
6. **Destiny:** Wunsch nach wählbaren Visieren (wie in Destiny 1) statt fester Würfe; Bungie entfernte Ornamente, die die Sicht
   verdeckten (2026) [C/B].

Quellenliste mit Adressen: `data/visiere.json` › `community_sources`.

## 10. Muster und Unterschiede

1. **Stilisierte Spiele halten offene Visiere meist schlank:** Destiny 0,06–0,15 (Ringe, Kasten-Reflex), Apex 0,05–0,07, Marathon
   Volt Thrower 0,07, The Finals 0,1–0,2; Ausnahmen mit dickerem Ring sind Titanfall-2-HCOG 0,24, Marathon Stryder 0,26 und Ares bis 0,2.
   Öffnung 12–25 % B, Welt außen scharf. Militär-Realismus (BF4-Holo 0,35, Siege 0,25–0,4, Tarkov, Sandstorm) hat dickere Rahmen und
   größere Gehäuse.
2. **Das Waffenmodell zoomt nicht mit.** Das Fenster bleibt beim Wechsel der Vergrößerung gleich groß (Apex 1–2×), nur die Welt
   zoomt; das Visier steht im Zielen fest auf dem Zielpunkt.
3. **Zielfernrohre stilisierter Spiele sind Vollbilder (A) mit eigener Kontur je Waffe** (Destiny Kreis, Marathon Rechtecke,
   Borderlands Herstellerform, Warframe Ornament); mittlere Optiken bleiben 3D mit **einer** Kamera (gemessen Apex, BF2042; Destiny
   gesichtet, Glas gegen außen offen).
   Ein echtes Linsenbild (D) nutzen fast nur Realismus-Titel; es kostet Bildrate.
4. **Weltzoom Hüfte → Zielen (Bildmaßstab):** Rotpunkt/Kimme 1,3–1,7 (BF2042 1,68, Valorant 1,27–1,44, The Finals 1,3), Destiny
   Automatik 1,84, Impuls 2,1, Scout 2,0; mittlere ZF 2,5–4 (Apex 2,5, BF2042 3,86, Halo 4,15); Scharfschützen 5–10+.
   Titanfall 2 zoomt bei Kimme und HCOG **gar nicht** (1,00).
5. **ADS ein:** 0,13–0,35 s (BF2042 0,133, Marathon 0,18, Apex 0,20, Destiny 0,20–0,25, BF2042-Scharfschütze 0,35); Vollbilder
   schneiden nach der Hebebewegung in 1–2 Bildern um; aus dem Zielen oft ein harter Schnitt in 2–3 Bildern (Destiny).
6. **Farbe:** Visier neutral, ein Akzent; Absehen trägt Hersteller- oder Funktionsfarbe; Glas fast ungetönt.

## 11. Empfehlungen für BASIC (cubeescape-ballon)

**Vorschlag aus den Messungen, nicht entschieden.** Bezug: BASIC-Visier-Standard v2 (Branch `claude/basic-first-light`, Commit
`8205514`: Augenpunkt 90 mm vor der Öffnung, Visierhöhe 66 ± 4 mm, Waffenmodell ungezoomt, Weltzoom je Klasse; `reflex_sight_v21`,
`scope_v21`, `box_scope_v21`; Ziel-Öffnung Reflex 18–26 % B, Zielfernrohr 26–34 % B). Der Nutzer empfand die Visiere als „sehr
klobig“ und mag den Destiny-Stil, ohne ihn zu kopieren.

| Thema | Beobachtung | Vorschlag für BASIC |
|---|---|---|
| Visiertyp je Klasse | Destiny: Form nach Visiertyp, Farbe nach Hersteller ([3](#3-visiertyp-je-waffenklasse)) | Automatik/MP: offenes Holo-Rundrechteck oder Ring; Impuls/Scout: Ring-Zielfernrohr kurz; Handfeuerwaffe/Sidearm/Schrot: Kimme + leuchtende Klammern statt Optik; Scharfschütze: Vollbild (Art A) mit eigener Kontur; Fusion: Ring/Doppelring; Werfer: runde Linse mit Chevron. Der Prisma-/Flachkasten (`box_scope_v21`) nur als Variante, nicht als Standard am Scout |
| Rahmen und Öffnung | Destiny Ring 0,15, Reflex 0,08, Hersteller 1 : 8 bis 1 : 12; klobig = große, hohe Gehäuse | Ring/ZF: Rahmen ≤ 0,15 × Öffnung, Außen/Innen ≤ 1,3; Reflex/Holo: Rahmen ≤ 0,10 × Öffnung oder glaslos (nur Leuchtlinie); Haube oben offen oder sehr dünn (Häkke-Lücke, VEIST-Zinken) |
| Bildanteil im Zielen | offene Visiere 12–20 % B (Destiny), 15–25 % (Marathon, Apex); Destiny-Scout-Öffnung 21 %, außen 27 % | Reflex-Ziel von 18–26 % auf **12–20 % B** senken; Zielfernrohr von 26–34 % auf **20–26 % B** (außen ≤ 30 %); Bezugs-FOV im Standard festschreiben, weil der Anteil mit dem FOV wächst ([Titanfall 1](#v-tf1-fov)) |
| Durchblick | Apex/BF2042 gemessen: 3D-Visier mit **einer** Kamera; Destiny: 3D-Visier, Welt außen scharf, Glas gegen außen offen; Linsenbild sonst nur bei Realismus, kostet Bildrate | `lens_picture` als **gleiches** Weltbild (eine Kamera, Weltzoom) statt eigener Render-Textur; Außenwelt scharf, höchstens leichte Vignette; `ads_hide` für Rohr/Okular beibehalten (sichtbar bleiben Objektivring, Sockel, Waffenoberkante) |
| Sockel und Höhe | Destiny-Rohr direkt auf der Gehäuseoberkante, Sockel trapezförmig verjüngt, Waffe taucht im Zielen ab (Oberkante 62–70 % H) | Sockel als verjüngtes Trapez mit Fasen statt Block; Visier so tief wie die 66-mm-Visierlinie es erlaubt, eher über eine flachere Waffenoberkante als über einen hohen Sockel; Anzeigen (Munition, Batterie) in die Sockel-Vorderseite **unter** die Visierlinie |
| Weltzoom | Bildmaßstab: Automatik 1,84, Impuls 2,1, Scout 2,0, Rotpunkt 1,3–1,7, Scharfschütze 5–10 | Vorhandene Werte (Automatik ×1,9, Impuls ×2,0, Scout ×2,4) liegen im Bereich; im Standard angeben, ob Bildmaßstab oder Winkelzoom gemeint ist |
| Absehen | Destiny: roter Punkt 0,7–1,5 % H ohne Glow, Glasgrafik 2–3 px, Schuss = Ring, Treffer = X, kein Aufblühen im Zielen | Standard-Linienstärke `fine`; im Zielen kein Aufgehen (`spread` beim Zielen nahe 0), stattdessen kurzer Ring beim Schuss; Punkt getrennt vom Glas am Zielpunkt; Farbe einstellbar (Spielerwunsch) |
| Glas | Destiny kaum getönt, Leuchtring am Rand, keine Gebrauchsspuren im Glas | Tönung ≤ 5 %, Leuchtring 2–5 % der Gehäusebreite; `dust`/`scratch`/`crack`/`cells`/`worn` im Zielen nur am Rand und schwach (≤ 3 % Kontrast), Mitte klar |
| Farbe | Visier neutral dunkel oder hell poliert, **ein** Akzent; Absehen trägt Hersteller-/Funktionsfarbe | Visiergehäuse in `graphite`/`anodized`, ein `accent`-Teil; Absehenfarbe je Familie (BASIC: Cyan) |

## 12. Offen und nicht messbar

- **Glas gegen außen in Destiny** nicht per Vergleich belegt (corr < 0,85); Sichtung spricht für ein etwas stärker vergrößertes Bild.
- **Destiny-Zielpunkt 57 % H** (Showcases 2020, Destiny 1) gegen 50 % H (ab 2022) ungeklärt.
- Weltzoom der Marathon- und Arc-Raiders-Zielfernrohre und der Cyberpunk-Linsen nicht messbar (Nebel, Schwenk); nur Augenmaß [O].
- 30/s-Videos (BF4, MW2019, Apex ClawZ, Valorant, Destiny 1) liefern keine Zeiten.
- Destiny-Prismavisier und D2-Impuls-Optiken der aktuellen Seasons kaum abgedeckt; Bogen-Absehen nicht gesichtet.
- Antigravity-Sichtung weiterer 11 Spiele (Fortnite, Doom Eternal, Starfield u. a.) noch nicht abgeschlossen; nicht bestätigte
  Quellen sind nicht übernommen (siehe [1](#1-quellen-und-methode)).
- Getrennte Themen, nicht Teil dieser Version: Zielbewegung, Rückstoßmuster, Mündungsfeuer, Inspektion, Waffen-Proportionen,
  Oberflächenmuster – je eigene Version.
