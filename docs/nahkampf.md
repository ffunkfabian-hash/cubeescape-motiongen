# Schwert und Glefe – Form, Schulteransicht und Ego-Vorbilder

Referenzanalyse REF 0.29 „Bladework“ (28.10.2026) für **BALLON Paket 7** (Projekt `cubeescape-ballon`: BASIC-16 Schwert „Klingenlauf“,
BASIC-17 Glefe „Schildwacht“, Stil v2.1, Ego-Prototyp in Unity). Zwei Hauptziele: **(1) Schwert** – Form an Destiny-Manifestbildern, die
Schulteransicht von Destiny und Ego-Vorbilder anderer Spiele mit einer Entscheidungsvorlage A/B/C; **(2) Glefe** – Form und Ego-Ablauf
(Hüfte, Schuss, Schlag, Schild, Nachladen, Fadenkreuz). Hier stehen Beobachtungen und Zahlen; entschieden wird in BALLON. Maschinenlesbar:
[`data/nahkampf.json`](../data/nahkampf.json). Bestand, auf dem diese Version aufbaut: [Proportionen](proportionen.md#p-d2-glefe) (0.15,
Glefe dort 0/2), [Hüftlage](huefte.md) (0.22, zwei Glefen), [Wechsel](wechsel.md#sw-h06) (0.26, Schwert = Ansichtswechsel),
[Nachladen](nachladen.md) (0.25) und die Messzeilen [Schwert](destiny2.md#z-schwert-unspoken) und [Glefe](destiny2.md#z-glefe-vexcalibur) in destiny2.md (0.7).

**Status:** **[M]** am eigenen Einzelbild gemessen (Manifestbild oder 60/s-Bild mit 10-%-Raster und Mittenkreuz); **[O]** Sichtung ohne
belastbare Zahl; **[C]** Spielerstimme oder Zuarbeit, nicht vollständig nachgeprüft; **[S]** Sekundär-/Fachquelle; **[B]** Entwickler.
**Jede Zahl ist das Beispiel einer Waffe** in einer Ansicht oder Aufnahme mit unbekanntem FOV, Perks und Eingabe – kein Klassenmittel.
Zeiten aus Showcases sind **Quellmedienzeit**; wo Normaltempo nicht belegt ist, steht es dabei.

## 1. Quellen und Methode

- **Manifestbilder [M]:** `screenshot` der `DestinyInventoryItemDefinition` (Manifest 245114.26.10.13.2000-1-bnet.66137, abgerufen 28.10.2026,
  `https://www.bungie.net/common/destiny2_content/screenshots/<hash>.jpg`, 1920 × 1080 bzw. 1051). Je Bild: Waffe gegen den glatten Hintergrund
  freigestellt (Lab-Abstand zu einem Median-Hintergrund ≥ 8), Hauptachse per Hauptkomponente, Bild achsparallel gedreht, Lineal in 0,05 L
  darübergelegt, Grenzen (Knauf, Parierstück, Kopfbeginn, Schneidenbeginn, Wicklung) **am gedrehten Bild abgelesen**; Breiten aus dem
  Hüllprofil quer zur Achse (100 Scheiben). **L = 1** ist die sichtbare Länge entlang der projizierten Achse. Genauigkeit der Grenzen
  ±0,02 L, Breiten ±0,01 L; die Manifestbilder sind **3/4-Ansichten** (Achse −18 … −31°), also wie in [proportionen.md](proportionen.md#1-quellen-und-methode)
  nur als Größenordnung mit orthografischen BASIC-Maßen vergleichbar. Die Schwelle 16 schnitt dunkle Endkappen ab (Judgment of Kelgorath,
  Edge of Intent: L −18 %); alle Zahlen hier mit Schwelle 8, jede Achse am Bild auf Kappe und Spitze geprüft.
- **Videos [M]:** jede Quelle per `yt-dlp --print "%(channel)s|%(upload_date)s|%(title)s|%(duration)s"` am 28.10.2026 geprüft; Einzelbilder
  nach Bildnummer bei nativer Rate (Ultraclocked 60/s, Twitch 60/s, Boosh Ninja 59,94/s), 10-%-Raster mit Mittenkreuz; Bögen mit jedem
  2.–4. Bild nur zum Finden, Marker aus Einzelbildern. Marker ±1 Bild, Differenzen ±2 Bilder. Third-Person-Lagen in % B/H und in
  **Körperhöhen (KH)** der stehenden Figur am selben Bild.

| Quelle | Kanal | Datum | Inhalt | fps | hier |
|---|---|---|---|---|---|
| [`afs_dhFDhQU`](https://www.youtube.com/watch?v=afs_dhFDhQU) <a id="n-q-io"></a> | Ultraclocked | 09.02.2020 | All Io Legendary Weapons … w/ Slow-Motion (429 s) | 60 | Unspoken Promise (Adaptive): Einstieg, Ruhe, leichte Folge, schwerer Angriff |
| [`tTjwM26ilgo`](https://www.youtube.com/watch?v=tTjwM26ilgo) <a id="n-q-uc"></a> | Ultraclocked | 21.04.2026 | Destiny 2 vs Warframe – Sword Animations (210 s, Kapitel) | 60 | Lightweight-Schwert leicht (0:00), Block/Guard (3:16) |
| [Twitch-Clip Aztecross](https://twitch.tv/aztecross/clip/OpenNeighborlyScallionBCWarrior-3dlnXDdiG0r-2y-K) <a id="n-q-az"></a> | Aztecross (Clip: Cobrachaos96) | 05.07.2024 | „CAUGHT IN 4K“ (48 s), 1280 × 720 | 60 | Ausstieg Schwert → Ego |
| [`O9QEU2RzB28`](https://www.youtube.com/watch?v=O9QEU2RzB28) <a id="n-q-lubrae"></a> | Boosh Ninja | 18.11.2022 | Vow of the Disciple … Showcase (704 s), Kapitel Lubrae's Ruin 141–260 s | 59,94 | Glefe Hüfte, Schuss, Kadenz, Schlag, Schild, Nachladen |
| [`1pH6zS-lj5g`](https://www.youtube.com/watch?v=1pH6zS-lj5g) | Boosh Ninja | 14.03.2023 | Season of The Haunted … Showcase (941 s), Kapitel Nezarec's Whisper 232–383 s | 59,94 | Glefe Hüfte, Kadenz, Nachladen |
| [`BqVfcsg3nYU`](https://www.youtube.com/watch?v=BqVfcsg3nYU) | Ultraclocked | 26.11.2024 | Galatine Protocol – Vexcalibur (geteiltes Bild) | 60 | Bestandsprüfung Nachladen |
| [`QOQsRsqwekg`](https://www.youtube.com/watch?v=QOQsRsqwekg) | CoolGuy | 23.05.2022 | The fully crafted Lubrae's Ruin … (642 s), Schmelztiegel mit HUD | 60 | Fadenkreuz in der Hüfte |
| [`6-26SH5jSwQ`](https://www.youtube.com/watch?v=6-26SH5jSwQ) <a id="n-q-insights"></a> | Destiny 2 | 14.02.2022 | The Witch Queen – The Glaive – Developer Insights (225 s) | – | Entwickleraussage Kamera ([7](#n-e-schwert)) |
| Ego-Vorbilder | Pauleh, Najius Maximus, Hamo clips, VideoGamesTV | 2015–2022 | Dark Messiah, Chivalry 2, Halo Infinite, Ghostrunner | 60 | [5](#5-ego-schwerter-anderer-spiele) |

Abschnittsdateien (`--download-sections`) sind per Bildabgleich am Originalstream verortet: Lubrae Datei + 141,008 s, Nezarec + 232,015 s
(±1 Bild); alle Glefen-Zeitstempel hier sind **Originalzeit**.

## 2. Form: Destiny-Schwerter (Manifestbilder)

Acht legendäre Schwerter aus allen sechs Rahmen. **Griff** = Knaufende bis Beginn von Parierstück oder Kragen (mit Knauf), **Parierstück**
= dessen Länge entlang der Achse, **Klinge** = Parierstückende bis Spitze (= Klinge/Gesamt, weil L = 1), **Spanne** = Hüllhöhe am
Parierstück, **Klingenbreite** = Median der Hülle im mittleren Klingendrittel (max. in Klammern), **H/L** = ganze Waffe.

| Schwert (Rahmen) | Knauf | Griff | Parierstück | Klinge | Spanne | Griff-Ø | Klingenbreite | H/L | Form |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **Unspoken Promise** (Adaptive) <a id="n-s-unspoken"></a> | 0,07 | 0,25 | 0,05 | 0,70 | 0,06 | 0,04 | 0,05 (0,06) | 0,07 | gerade, Kragen statt Parierstück, Klingenblock 0,30–0,45 |
| **Negative Space** (Adaptive) | 0,09 | 0,25 | 0,05 | 0,70 | 0,05 | 0,04 | 0,07 (0,08) | 0,09 | Säbelbauch, Haken an der Wurzel |
| **Crown-Splitter** (Aggressive) | 0,05 | 0,30 | 0,05 | 0,65 | 0,20 | 0,04 | 0,06 (0,08) | 0,21 | Langschwert, Flügel-Parierstück |
| **Quickfang** (Lightweight) | 0,03 | 0,27 | 0,06 | 0,67 | 0,08 | 0,06 | 0,05 (0,05) | 0,10 | Katana-artig, Griffgehäuse |
| **Goldtusk** (Lightweight) | 0,04 | 0,28 | 0,06 | 0,66 | 0,09 | 0,04 | 0,05 (0,05) | 0,10 | gekrümmt, Block-Parierstück |
| **Temptation's Hook** (Caster) | 0,03 | 0,22 | 0,02 | 0,76 | 0,12 | 0,04 | 0,08 (0,18) | 0,23 | gebogen, breiter Gehäuseblock statt Parierstück |
| **Falling Guillotine** (Vortex) | 0,04 | 0,30 | 0,06 | 0,64 | 0,20 | 0,04 | 0,20 (0,23) | 0,25 | Hackmesser |
| **Abyssal Edge** (Wave) | 0,04 | 0,22 | 0,08 | 0,70 | 0,32 | 0,04 | 0,04 (–) | 0,33 | Kreuzgriff schräg, gezahnte Klinge; H/L vom Kreuz bestimmt |

**Muster [M]:** Klinge **0,64–0,76 L** (sechs von acht 0,65–0,70), Griff mit Knauf **0,22–0,30 L**, Parierstück entlang der Achse nur
0,02–0,08 L; der Griff ist bei allen ≈ 0,04 L dick (Quickfang-Gehäuse 0,06). **H/L trennt zwei Formfamilien:** schlanke Klingen
0,07–0,10 (Adaptive, Lightweight) gegen breite Parier- oder Klingenformen 0,21–0,33 (Aggressive, Caster, Vortex, Wave); die Spanne am
Parierstück macht den Unterschied, nicht die Klinge (Klingenbreite bei sieben von acht 0,04–0,08). BASIC-16 hat H/L 0,067
([proportionen.md › 4](proportionen.md#4-formbefund-basic-bildstand-24102026), orthografisch) und liegt damit bei Unspoken Promise.

## 3. Form: Destiny-Glefen (Manifestbilder)

Neun Glefen (acht legendär aus allen drei Rahmen, ein Exotic). **Schaft** = Endkappe bis Kopfbeginn (erstes Gehäuse, das breiter ist als
der Schaft), **Kopf** = Kopfbeginn bis Spitze, darin **Emitter/Gehäuse** bis zum Schneidenbeginn und **Klinge**; **Kragen** = Absatz
zwischen hinterem und vorderem Schaft; **Wicklung** = vordere Griffzone. Breiten wie in › 2.

| Glefe (Rahmen) | Schaft | Kopf | davon Gehäuse | Klinge | Kragen | Wicklung | Schaft-Ø | Kopf max. | Klingenbreite | H/L | Familie |
|---|---:|---:|---:|---:|---:|---|---:|---:|---:|---:|---|
| **The Enigma** (Adaptive) <a id="n-g-enigma"></a> | 0,55 | 0,45 | 0,15 | 0,30 | 0,30 | 0,37–0,55 | 0,04 | 0,08 | 0,04 | 0,10 | Ring (Abzugsring am Kopf) |
| **Nezarec's Whisper** (Adaptive) | 0,55 | 0,45 | 0,13 | 0,32 | 0,30 | 0,37–0,55 | 0,04 | 0,11 | 0,04 | 0,12 | Ring |
| **Refusal of the Call** (Adaptive) | 0,52 | 0,48 | 0,16 | 0,32 | 0,30 | 0,31–0,35 | 0,03 | 0,10 | 0,06 | 0,11 | Ring, Knochenklinge |
| **Backfang** (Rapid-Fire) | 0,55 | 0,45 | 0,14 | 0,31 | 0,30 | 0,38–0,55 | 0,04 | 0,08 | 0,05 | 0,10 | Ring, Gliederung wie The Enigma |
| **Forthcoming Deviance** (Rapid-Fire) | 0,53 | 0,47 | 0,13 | 0,34 | 0,30 | 0,36–0,53 | 0,03 | 0,11 | 0,09 | 0,12 | Ring, Haken unter dem Kopf |
| **Rake Angle** (Aggressive) | 0,52 | 0,48 | 0,13 | 0,35 | 0,30 | 0,36–0,53 | 0,03 | 0,11 | 0,08 | 0,11 | Optik (Visierblock mit Laser) |
| **Albedo Wing** (Aggressive) | 0,52 | 0,48 | 0,13 | 0,35 | 0,30 | 0,35–0,52 | 0,04 | 0,08 | 0,08 | 0,09 | Optik |
| **Judgment of Kelgorath** (Aggressive) | 0,53 | 0,47 | 0,12 | 0,35 | 0,30 | 0,36–0,53 | 0,03 | 0,10 | 0,07 | 0,11 | Optik |
| **Edge of Intent** (Exotic) | 0,55 | 0,45 | 0,11 | 0,34 | 0,31 | 0,38–0,55 | 0,04 | 0,09 | 0,07 | 0,11 | Axtklinge |

**Muster [M]:** Die Glefen teilen **ein Gerüst**: Kragen bei **0,30 L** (neun von neun, ±0,01), vordere Wicklung 0,35–0,55 L (Refusal of the Call nur 0,31–0,35), Kopfbeginn
0,52–0,55 L, Schneidenbeginn 0,65–0,70 L – die Rahmen unterscheiden sich nur im Kopf (Ring-Familie mit Abzugsring, Optik-Familie mit
Visierblock und Laser). Das spricht für ein gemeinsames Animationsgerüst mit festen Handlagen (Einschätzung; Bungie hat das nicht belegt).
Schaft 0,03–0,04 L dünn, Kopf 0,08–0,11 L breit, H/L **0,09–0,12**; Klinge 0,30–0,35 L ist gut halb so lang wie bei den Schwertern
(0,64–0,76). BASIC-17 hat H/L 0,111 ([proportionen.md › 4](proportionen.md#4-formbefund-basic-bildstand-24102026)) und liegt mitten darin –
damit ist die frühere Lücke „Glefe 0/2“ ([proportionen.md](proportionen.md#p-d2-glefe)) geschlossen. **Nicht verwendet:** Lubrae's Ruin
(Endstachel berührt im Manifestbild den unteren Rand, H/L 0,21 durch die Axtform), The Heron und Vexcalibur (Schaftende abgeschnitten) – [O].

## 4. Destiny-Schwert in der Schulteransicht

**Kamera [M].** Stehend misst die Figur **42–43 % H** (Io f17808 und f18000: Kopfoberkante 54–55 % H, Füße 96–97 % H; Ultraclocked 2026
Block f11940: 46 % H, Kamera dort näher); die Figur steht **links der Mitte**, Körpermitte 44–48 % B, Kopfoberkante 3–5 pp **unter** der Bildmitte. Daraus:
Sichtlinie ≈ 0,1 KH über dem Scheitel, Figur 0,13–0,25 KH links der Sichtlinie (Kamera rechts hinter der Schulter). Der Abstand hängt am
unbekannten FOV: bei 16:9 und horizontal 74° / 90° / 105° wären es **2,8 / 2,1 / 1,6 KH** bis zur Figur. In Bewegung schwankt die Figurgröße
(Kamera folgt mit Verzug: 290,5 s Füße unter dem Bildrand, 292,0 s ≈ 45 % H), im Ultraclocked-Video von 2026 steht die Figur in Ruhe
größer (Kopf 53 % H, Füße unter dem Rand, Körpermitte ≈ 38 % B). Ein Winkel-FOV ist nicht trennbar: der Hintergrund schrumpft vom letzten
Ego- zum Schulterbild auf 0,59–0,76 je nach Tiefe (Vorlagensuche, Korrelation 0,70–0,88) – das ist Parallaxe des Kamerarückzugs, kein FOV-Maß [O].

| Vorgang | Quelle, Zeit (Bilder) | Messung |
|---|---|---|
| **Einstieg** (Menüschnitt → Schulter) <a id="n-s-ein"></a> | Io, 289,450 → 289,933 s (f17367 → f17396) | **9 Bilder Ego ohne Waffe** (f17367–f17375), ab f17376 die Figur bildfüllend links (Umhang dicht vor der Kamera), **Rückzug 20 Bilder** bis f17396; bestätigt den Bestand ([destiny2.md](destiny2.md#z-schwert-unspoken)). Ob der Menüschnitt einem Wechsel entspricht, bleibt offen |
| **Ausstieg** (Schulter → Ego) <a id="n-s-aus"></a> | Aztecross-Clip, 44,333 → 44,433 s (f2660 → f2666) | Kamera **fährt in 6 Bildern** auf die Figur zu (Figur wächst über den rechten Bildrand), ab f2666 Ego mit Händen unten rechts; die neue Waffe erreicht die Hüfte erst ≈ 45,5–45,8 s, durch Spielerbewegung nicht als Ziehen isoliert |
| **Ruhe** (Adaptive) <a id="n-s-ruhe"></a> | Io f17808, f18000 | Schwert **senkrecht** in der rechten Hand rechts neben der Figur: Heft ≈ (50, 70–71), **Spitze ≈ (50, 51–53)** – die Klinge steht direkt unter dem Mittenkreuz; Figur ohne Schwert 39–48 % B (f17808) bzw. 43–52 % B (f18000), Körpermitte 44–48 % B |
| **Ruhe** (Lightweight, 2026) | Ultraclocked 2026 f24 | Klinge **tief nach vorn-rechts**: Heft ≈ (40, 87), Spitze ≈ (56, 95); Figur 32–43 % B |
| **Leichter Angriff** (Adaptive, Folge) <a id="n-s-leicht"></a> | Io f17440 → f17494 (290,667 → 291,567 s) | erste Bewegung f17440, Schwert über den Kopf bis f17442, erste Bahn bis f17452 (Spitze kommt bis ≈ (52–55, 50–52)), zweite Bahn f17454–f17466 seitlich tief (y ≈ 60–65 %), Figur macht dabei einen Ausfallschritt nach vorn; Ruhe ≈ f17494. **Erster Schlag ≈ 14 Bilder, Folge bis Ruhe ≈ 54 Bilder (0,90 s)**; Zahl der Schläge im 2-Bild-Bogen nicht sicher (2–3) |
| **Leichter Angriff** (Lightweight, 2026) | Ultraclocked 2026 f30 → f88 | Drehschlag: Start f30, Klinge waagrecht rechts f32, Drehung f34–f46, **Schlagspur f48–f52** links (x 30–45, y 72–80 %), Rückkehr bis f88: **18 Bilder bis zur Spur, 58 Bilder bis Ruhe** |
| **Schwerer Angriff** (Adaptive) <a id="n-s-schwer"></a> | Io f17734 → f17784 (295,567 → 296,400 s) | Ducken mit Klinge tief hinten f17734–f17738, Aufwärtsbahn f17740–f17746, **Weißblitz f17748–f17756 (9 Bilder, verdeckt das ganze Bild)**, blauer Effekt bis f17762, Rückkehr bis ≈ f17784: **14 Bilder Ausholen, 50 Bilder gesamt (0,83 s)** |
| **Block/Wache** <a id="n-s-block"></a> | Ultraclocked 2026, 196,800 → 196,950 s (f11808 → f11817); 198,5–200,0 s | Klinge aus der Tiefe vor die Brust gehoben, **Schutzkuppel sichtbar ≤ 9 Bilder** nach f11808 (Bogen jedes 3. Bild); Kuppel vor der Figur ≈ 16–47 × 42–95 % (f11817) bzw. 35–60 × 46–95 % (f11940), Oberkante **an der Bildmitte**; gehalten ≥ 90 Bilder mit Trefferaufblitzen. Ablegen nicht im Material (Schnitt) |
| **Sprint** | Io 307,4–308,6 s | Figur läuft vom Betrachter weg, Schwert nicht sicher abgegrenzt [O]; kein Sprintwert |

**Tempo:** Für keinen Schwertablauf ist Normaltempo belegt (das Io-Video führt „w/ Slow-Motion“ im Titel, die Abschnitte tragen keine
Einblendung); die Zeiten sind Medienzeit und als Größenordnung zu lesen. Das Lightweight-Beispiel ist ein anderer Rahmen und eine andere
Spielversion (2026) als Unspoken Promise (2020).

## 5. Ego-Schwerter anderer Spiele

Gemessen von einem Opus-Unteragenten an vier Titeln ([11](#11-prüfung-und-zählung)); vier seiner Zahlen sind am eigenen Bild nachgemessen und
bestätigt. Alle vier Quellen haben echte 60/s (Doppelbilder gezählt), FOV überall unbekannt; Neigung in Grad gegen die Senkrechte, Spitze
links negativ. Marker: *Ausholen* = erste Bewegung aus Ruhe bis Umkehr-/Haltepunkt, *Schlag* = Umkehrpunkt bis Ende der schnellen Bahn,
*Rückkehr* = Ende Schlag bis Ruhe ±3 pp, *Block ein* = erste Bewegung bis Endlage. **Skyrim** ist nicht belegt: die 60/s-Quellen ohne Mods
zeigen in den gesichteten Teilen nur Magie und Bogen, fast alle Schwert-Treffer laufen mit Animationsmods.

| Titel · Waffe | Quelle | Ruhe (Spitze / Heft, Neigung) | Ausholen | Schlag (Fadenkreuz verdeckt) | Rückkehr / Block |
|---|---|---|---|---|---|
| **Dark Messiah** · Prolog-Schwert <a id="n-ego-dm"></a> | Pauleh, [`hLR0jFXRIjc`](https://www.youtube.com/watch?v=hLR0jFXRIjc), 30.09.2015, 242,1–253,5 s | Spitze 69/42, Heft unter dem Rand, Hülle 68–74 × 41–100, −7° | Kraftschlag **28 Bilder** über die Mitte bis über die rechte Schulter, danach 43 Bilder Halten (Eingabe) | **16 Bilder** bis Klinge aus dem Bild, schnelle Bahn ≈ 10, rechts oben → links unten, **3–4 Bilder** verdeckt | Wechsel in Ruhe 6 Bilder (nach Ladehaltung); **Block ein 23 Bilder** über die Mitte (Parierstange 57/53) in die Endlage rechts x 80–86, Block aus ≥ 8 |
| **Chivalry 2** · Langschwert (Ego-Option) <a id="n-ego-c2"></a> | Najius Maximus, [`DCn-SfNQwQI`](https://www.youtube.com/watch?v=DCn-SfNQwQI), 22.02.2022, 22,4–24,4 s | Spitze 63/0 (über den Rand), Parierstange 64/72, Hülle 61–69 × 0–100, −2° | **13 Bilder** nach rechts unten | waagrecht **7 Bilder** bei y 56–60, 6–10 pp **unter** der Mitte (0 verdeckt); Folgeschlag deckt die obere Mitte ≈ 11 Bilder [O] | verkettet, keine Rückkehr; Haltungswechsel 15 Bilder, ob Parade ist unbelegt [O] |
| **Halo Infinite** · Energieschwert <a id="n-ego-halo"></a> | Hamo clips, [`ICqehEtHVdg`](https://www.youtube.com/watch?v=ICqehEtHVdg), 21.11.2021, 276,2–279,5 s | Spitze 50/61, Heft 78/80, Hülle 50–92 × 40–100, −69°; Sprint: Spitze 52/80, flach unten rechts | **≤ 3 Bilder**, davor ≈ 7 Bilder Lunge (Kamera fährt auf das Ziel) | **3 Bilder** rechts unten → links oben, **1 Bild** verdeckt (Heft 52/52); Durchschwung links ≈ 35 Bilder | **Rückkehr 23 Bilder** (≈ 10 Bilder ohne Schwert) |
| **Ghostrunner** · Katana <a id="n-ego-gr"></a> | VideoGamesTV, [`-9LfAI3_Vlo`](https://www.youtube.com/watch?v=-9LfAI3_Vlo), 08.05.2021, 57,1–58,1 s | Spitze 45/87, Hand 90/88, Hülle 45–96 × 80–95, −88° (flach am unteren Rand) | liegt im Dash, unscharf | **7 sichtbare Bilder** links oben → rechts unten, Treffereffekt füllt danach das Bild | nicht gemessen |

**Muster [M]:** In allen vier Ruhelagen liegt das Schwert **rechts oder unten**, das Fadenkreuz ist frei (Dark Messiah 19 pp Abstand,
Halo 6–11 pp unter der Mitte, Ghostrunner flach am Rand). Die Bahn quert die Mitte nur **1–4 Bilder** (Chivalry-Waagrechtschlag gar
nicht, Folgeschlag ≈ 11). Eine Rollneigung der Kamera beim Schlag ist in keinem Titel zu sehen; Halo erzeugt die Wucht über die
Lunge-Fahrt, Dark Messiah über lange Lade- und Haltephasen. Im Vergleich zur Destiny-Ruhe (Spitze direkt unter dem Mittenkreuz,
[4](#n-s-ruhe)) liegt kein Ego-Vorbild so mittig. Die Dark-Messiah-Zeiten stammen teils aus 30/s-Bögen (±2 Bilder).


## 6. Destiny-Glefe in der Ego-Sicht

Gemessen von einem Opus-Unteragenten an Lubrae's Ruin und Nezarec's Whisper (beide Adaptive) und dem Vexcalibur-Bestand; vier Zahlen am
eigenen Bild nachgemessen und bestätigt ([11](#11-prüfung-und-zählung)). In allen Messfenstern echte 60/s (Ausnahme Lubrae-Schuss 3:
fünf Doppelbilder, ±2). FOV unbekannt, Schießstand ohne HUD (außer Fadenkreuz). **Normaltempo nicht belegt:** die Schussabstände sind bis ≈ 22 % kürzer als im Manifest, alle Zeiten sind Medienzeit.

| Vorgang | Quelle, Zeit | Messung |
|---|---|---|
| **Hüfte (Ruhe)** <a id="n-g-huefte"></a> | Lubrae 143,010 s; Nezarec 234,000 s | Lubrae: **Spitze 63,2/45,5**, Kopfbeginn 60,0/69,2, rechte Hand 72,9/90,8, Hülle 46,3–77 × 45,5–100, Schaft **39°**; Nezarec: Spitze 68,6/50,3, Kopfbeginn 60,0/69,4, Finger 68/73, Hülle 52,5–77 × 50,3–100, Schaft 46°. Unteres Schaftende verdeckt bzw. außerhalb; **Bildmitte frei**, die Spitze liegt 13–19 pp rechts der Mitte auf Höhe des Zielpunkts |
| **Schuss** <a id="n-g-schuss"></a> | Lubrae 151,468–152,085 s | Glefe stößt zur Kamera und glüht ≈ 7 Bilder; **Projektil 2 Bilder nach Beginn links über der Mitte** (Flammenzunge um 46/50, später weißglühende Kugel ≈ 3 pp Ø bei 48/43) – nicht am Kopf (56/61); Nezarec: weißblaue Kugel bei 49/46 |
| **Rückstoß** | Lubrae, acht Schüsse | Waffe im Bild: Spitze **+8,4 pp hoch nach 17–21 Bildern**, zurück auf ±3 pp nach **33 Bildern**; Kamera gegen zwei Weltanker (NCC ≥ 0,92): **9,6–13,1 pp H hoch**, Spitze nach 4–6 Bildern, ≤ 3 pp nach 16–21, abgeklungen nach 22–31 Bildern (Netto aus Spiel und Eingabe) |
| **Kadenz** | Lubrae ×2, Nezarec ×3 Magazine | Magazin **6** (je zweimal leergeschossen); Abstände **51–63 Bilder** (0,85–1,05 s), schnellster ≈ 65–70/min gegen 55/min im Manifest ([waffenwerte.md](waffenwerte.md)) – Ursache offen, Normaltempo damit weder belegt noch widerlegt |
| **Nahkampfschlag** <a id="n-g-schlag"></a> | Lubrae 175,292–179,096 s | aus der Hüfte: **Ausholen nach rechts unten 8 Bilder** bis zum Umkehrpunkt, **schnelle Bahn rechts → links 10 Bilder** (Kopf ≈ 10 pp B je Bild), Fadenkreuz **3 Bilder** verdeckt (Kopf auf 50/52); Kombo **5 Schläge** im Takt **37–43 Bilder**, Waffe dazwischen außerhalb des Bilds; Hüfte ±3 pp **59 Bilder** nach dem letzten Mittendurchgang |
| **Schild** <a id="n-g-schild"></a> | Lubrae 145,012–145,178 s; 165,682–166,600 s; 149,566–149,616 s | **Ein 10–11 Bilder** (erste Bewegung → Schildpose ±1 pp); gehalten: Klinge senkrecht (70°), obere Spitze **59,2/35,9**, Kopfbeginn 63,9/62,9, rechte Hand 82,3/80,3, Hülle 51,5–100 × 35,9–100, **Bildmitte frei**; Schildeffekt nur schwache Verzerrung über das ganze Bild, kein abgrenzbares Rechteck (Weltmaßstab 1,05×, Zoom oder Verzerrung nicht trennbar). **Aus** beide Male durch einen Schuss: 3 bzw. 13 Bilder bis zur Hüfte |
| **Nachladen** <a id="n-g-nachladen"></a> | Lubrae 156,306–159,393 / 171,405–174,474 s; Nezarec 250,467–253,970 s; Vexcalibur 9,300–11,583 s | Lubrae: erste Hüftpassage 2,853 / 2,753 s, **Überschwingen 7,0 / 7,4 pp hoch**, Hüfte ±3 pp 3,020 / 2,970 s, ruhig **3,086 / 3,070 s**; Nezarec: Hüfte ±3 pp 3,303 s, ruhig 3,504 s; **Vexcalibur-Bestand bestätigt** (9,300 → 11,583 s = 137 Bilder ist „ruhig“), erste Hüftpassage 11,367 s (124 Bilder), Überschwingen 7,8 pp, ±3 pp 11,517 s |
| **Fadenkreuz** <a id="n-g-fadenkreuz"></a> | CoolGuy `QOQsRsqwekg`, ≈ 129,0 s | Kreis **Ø 3,4 % H**, Mitte **50,0/57,5 – 7,5 pp unter der Bildmitte**, Bogenanzeige Ø 10,3 % H (Schildenergie); eine Quelle mit HUD, Ursache der tiefen Lage (Glefen-HUD, Plattform, Einstellung) offen |
| **Zielen (ADS)** | alle Quellen | **kein Visier- oder Zoomzustand**; die Zieltaste löst den Schild aus |
| **Sprint** | – | nicht im Material (Schießstand-Showcases) [O] |

**Muster [M]:** Die Glefe liegt unten rechts, Kopf und Spitze auf Höhe des Zielpunkts, die Mitte bleibt in Ruhe und im Schild frei. Das
Projektil startet sichtbar **an der Bildmitte**, nicht am Kopf. Nach dem Nachladen schwingen Lubrae (2×) und Vexcalibur 7–8 pp über die Hüfte
hinaus (Nezarec: kein Überschwingwert) (wie die Lehre zu „hüftähnlich“ in [wechsel.md](wechsel.md#3-abgleich-mit-dem-bestand)). **Bestandsabgleich:** Hüfte Lubrae
(huefte.json Griff 73/92,4, Hülle bis 74,5) innerhalb ±3 pp, Nezarec-Rand 83 gilt nur mit Ärmel (Waffe allein ≈ 77) – Hüllendefinition
nennen. Die Vorab-Sichtung dieser Sitzung (Schläge bei ≈ 149,6 und 154,4 s) war falsch: dort sind Schüsse.


## 7. Bewertung: gut, nicht so gut, für wen

Spieler- und Fachstimmen sammelte ein Sonnet-Unteragent ([11](#11-prüfung-und-zählung)); jede Zeile nennt nur, was auf der geladenen Seite stand.
Reddit war nicht erreichbar (403, Archiv gesperrt) – dort ist nichts eingetragen. „Einschätzung“ = eigene Deutung dieser Version.

| Spiel · Gegenstand | Gut (warum) | Nicht so gut (warum) | Für wen | Spielerstimmen | Entwickler/Fachquelle |
|---|---|---|---|---|---|
| **Destiny 2 · Schwert in der Schulteransicht** <a id="n-e-schwert"></a> | Übersicht und Rundumsicht, eigene Schlagbahn am Körper lesbar [C] | „3-Peeking“ um Ecken in PvP [C]; einige wollen das Schwert in Ego ([D1-Thread 2015](https://www.bungie.net/en/Forums/Post/151134371)) [C]; Guard war vor 2020 „fast sinnlos“ [C] | PvE und Übersicht; PvP-Spieler fordern Beschränkung | **wiederkehrend:** Wunsch nach Third-Person-Modus in 5 Threads 2019–2025 ([1](https://www.bungie.net/en/Forums/Post/252397152), [2](https://steamcommunity.com/app/1085660/discussions/0/4042608198329991312), [3](https://steamcommunity.com/app/1085660/discussions/0/4299320215882183471), [4](https://steamcommunity.com/app/1085660/discussions/0/4631485178655632889), [5](https://steamcommunity.com/app/1085660/discussions/0/673972930559987754)), 3-Peeking in 3 Threads ([45 Stimmen](https://www.bungie.net/en/Forums/Post/257215736), 28.09.2020; [2](https://www.bungie.net/en/Forums/Post/256491031); [3](https://www.bungie.net/en-us/Forums/Post/239292077)); Guard-Kritik [141 Stimmen](https://www.bungie.net/en/Forums/Post/253398475) (31.08.2019); Gegenstimmen „es ist ein Ego-Shooter“ | **[B]** [Glaive Developer Insights](https://www.youtube.com/watch?v=6-26SH5jSwQ) (Destiny 2, 14.02.2022, 2:05–2:33): Schwerter ziehen die Kamera heraus, weil große Schläge Ziele außerhalb des Ego-Sichtfelds treffen; **[B]** TWAB 06.02.2020 ([Spiegel](https://destiny.bungie.org/bwu/304)): Energie für Guard und schwere Angriffe, endlose leichte Folge; **[B über S]** Blackburn 25.02.2021 ([Vortainment](https://vortainment.com/2021/02/25/bungie-details-destiny-2-2021-update-road-to-witch-queen/)): keine Third-Person-Waffe ohne Munition in Trials |
| **Destiny 2 · Glefe in Ego** <a id="n-e-glefe"></a> | eine Perspektive für Schuss, Schild und Schlag, kein Kamerawechsel ([Kotaku](https://kotaku.com/destiny-2-glaives-new-weapon-witch-queen-dlc-melee-bung-1848646309), 12.03.2022) [S]; Schild 97,5 % Schadensminderung PvE, 75 % PvP ([TWAB 21.04.2022](https://destiny.bungie.org/bwu/409)) [B] | Schild wirkt verzögert/Desync bis ≈ 1 s ([Steam 18.05.2022](https://steamcommunity.com/app/1085660/discussions/0/3271314133306549689/), [Bungie.net 28.05.2022](https://www.bungie.net/en/Forums/Post/261160090)) [C]; Projektiltreffer inkonsistent [C]; Nahkampf zählt nicht als Waffenschaden (Perks) [C]; Effektdichte verdeckt das Bild ([Vexcalibur, 13 Stimmen](https://www.bungie.net/en/Forums/Post/264761879), 22.05.2025) [C] | PvE-Nahkampf, „Waffe + Schild“ | **wiederkehrend:** Perk-/Mod-Frust in 3 Spielerquellen ([18 Stimmen](https://www.bungie.net/en/Forums/Post/260767505), [Steam 27.09.2022](https://steamcommunity.com/app/1085660/discussions/0/3364775865378444067), [Steam 21.04.2022](https://steamcommunity.com/app/1085660/discussions/0/3266807987598689550)), Trefferinkonsistenz in 3 ([Steam 2022](https://steamcommunity.com/app/1085660/discussions/0/3271314133306549689/), [13 Stimmen](https://www.bungie.net/en/Forums/Post/264602271), [Bungie.net 2025](https://www.bungie.net/hi/Forums/Post/264549926)); Gegenstimmen „Glefen sind in Ordnung“, Buffs „enorm“ | **[B]** [Developer Insights](https://www.youtube.com/watch?v=6-26SH5jSwQ) (2:05–2:33): die Glefe zeigt klar in eine Richtung, Ego behält eine „Unmittelbarkeit“, die in Third Person verloren ginge; **[B]** [TWAB 21.04.2022](https://destiny.bungie.org/bwu/409) (Chris Proctor): Nahkampf bewusst einfacher Schlag, Lunge schon lang, Schildverbrauch −30 %; **[B über S]** [GamesRadar](https://www.gamesradar.com/the-first-glaives-in-destiny-2-the-witch-queen-were-way-too-strong-and-broke-the-game/) 14.02.2022: einzige Ego-Nahkampfwaffe, ein Designer fast ein Jahr, 6 Monate Animation |
| **Dark Messiah · Ego-Schwert, Tritt, Block** | Gewicht und Timing, Konter, Tritt und Umgebung als Waffe [S] | Tritt zu stark; Entfernung abschätzen | Umgebungs-Kills | wiederkehrend „bestes Ego-Nahkampfsystem“ ([Steam 2012](https://steamcommunity.com/app/2100/discussions/0/882957625837028722/)); Gegenstimmen Chivalry/Mount & Blade | **[B über S]** Colantonio (Arkane), GDC 07.03.2007 ([Game Developer](https://www.gamedeveloper.com/game-platforms/gdc-arkane-s-colantonio-takes-on-first-person-melee)): Entfernung schätzen „nie vollständig gelöst“, mit größerer Trefferzone überbrückt |
| **Skyrim · Ego-Nahkampf** | Schild und Zweihand-System, Stagger ([Game Informer](https://gameinformer.com/b/features/archive/2011/01/24/skyrim-building-better-combat.aspx), 24.01.2011) [B über S] | „Fuchteln“ ohne Gewicht ([Kotaku](https://kotaku.com/five-disappointing-things-about-the-elder-scrolls-v-sk-5858474) 11.11.2011) [S], Tastenhämmern | Magie/Bogen-Spieler, Nahkampf meist mit Mods | Spieler-Threads nur Suchauszug (Steam-Altersschranke, NeoGAF/GameFAQs gesperrt) | **[B über S]** Todd Howard (Game Informer): Kampf „greifbarer“ machen |
| **Chivalry 2 / Mordhau · Ego gegen Third Person** | Ego für Duelle und Stiche, Bahn am Fadenkreuz ([Chivalry 2, Steam 14.06.2022](https://steamcommunity.com/app/1824220/discussions/0/3414305949100931803/)) [C] | Tiefenwahrnehmung: Reichweite in Ego schwer zu schätzen ([Mordhau, Steam 31.05.2019](https://steamcommunity.com/app/629760/discussions/0/1643164649207550435/), in Antworten bestätigt; [Steam 28.05.2019](https://steamcommunity.com/app/629760/discussions/0/1643164558917088382/)) [C] | Duelle (Ego) gegen Massenschlacht (Third Person) | wiederkehrend (7 Threads in der Zuarbeit, 3 hier verlinkt), uneins, welche Kamera Reichweite lesbarer macht | keine Entwickleraussage zur Kamera gefunden; [Kotaku 13.03.2012](https://kotaku.com/these-guys-hope-to-solve-the-problem-of-first-person-me-5892918) zu Ego-Nahkampf bei Chivalry [S] |
| **Halo · Energieschwert** | Reichweite lesbar: Fadenkreuz wird rot in Lunge-Reichweite ([Halopedia](https://www.halopedia.org/Type-1_energy_sword/Gameplay), Abruf 28.10.2026) [S] | „billig“, Gegenspiel schwach ([Steam 29.11.2021](https://steamcommunity.com/app/1240440/discussions/0/3195862975798039670)) [C] | Kurzstrecken-PvP | Einzelstimme | keine Entwicklerquelle gefunden (Halo-Waypoint-Patchnotes 06.12.2022 nur Suchauszug) |
| **Ghostrunner · Katana in Ego** | Ein-Treffer-Tod, Parade befriedigend ([NME, Alan Wen](https://www.nme.com/reviews/game-reviews/ghostrunner-review-a-deadly-cyberpunk-first-person-slasher-that-tests-your-patience-2803103), 29.10.2020) [S] | Steuerung „rutschig“, Schwierigkeit frustrierend (NME); Kampf bremst das Tempo, „unbeholfen“ ([Windows Central](https://www.windowscentral.com/ghostrunner-review-thrilling-parkour-platformer-marred-combat), 26.10.2020) [S] | reaktionsstarke Spieler | zwei verlinkte Rezensionen, gemischt (zwei weitere der Zuarbeit ohne URL nicht übernommen) | **[B über S]** One More Level ([GamingBolt](https://gamingbolt.com/ghostrunner-interview-combat-setting-and-more) 02.10.2019): Distanz schwer, deshalb Heranziehen an den Gegner |

### E2 – Lehren für BALLON (Vorschlag, dort entscheiden)

- **Übernehmen:** die Destiny-Begründung als Prüffrage – Schläge, die außerhalb des Ego-Sichtfelds treffen sollen, brauchen Third Person oder
  eine Bahn, die vor der Kamera bleibt; eine gerichtete Stangenwaffe bleibt in Ego (Bungie, Developer Insights).
- **Übernehmen:** ein Reichweitensignal im Ego-Nahkampf (Halo: Fadenkreuz färbt sich in Reichweite; Ghostrunner/Arkane: Heranziehen oder
  größere Trefferzone) – das ist in allen Fachquellen das Kernproblem.
- **Vermeiden:** Schild/Guard mit sichtbarer Verzögerung zur Wirkung (Destiny-Glefen-Kritik 2022) und Effekte, die die Bildmitte füllen
  (Vexcalibur-Kritik 2025).
- **Testen:** ob der Schlag des Ego-Prototyps die Bildmitte kreuzt und wie lange das Fadenkreuz verdeckt ist (Zahlen in [5](#5-ego-schwerter-anderer-spiele)).

## 8. Für BALLON Paket 7

Zahlen für den Entwurf, je mit dem Beispiel, aus dem sie stammen (Lagen % B/H, Zeiten in Bildern bei 60/s; Showcase-Medienzeit, wo
nicht anders gesagt). Vorschläge, keine Vorgaben – entschieden wird in BALLON.

**Schwert (BASIC-16)**
- **Maße** (Anteil der Gesamtlänge): Klinge 0,64–0,76 (meist 0,65–0,70), Griff mit Knauf 0,22–0,30, Knauf 0,03–0,09, Parierstück entlang
  der Achse 0,02–0,08, Griff-Ø ≈ 0,04, Klingenbreite 0,04–0,08; H/L schlank 0,07–0,10, mit breitem Parierstück 0,21–0,33 ([2](#2-form-destiny-schwerter-manifestbilder)).
- **Ego-Lage** (bei Option B, [5](#5-ego-schwerter-anderer-spiele)): Ruhe rechts oder unten, Spitze z. B. 69/42 (Dark Messiah, senkrecht),
  50/61 mit Heft 78/80 (Halo, schräg zur Mitte), 45/87 (Ghostrunner, flach); Fadenkreuz frei. Sprint: flach unten rechts (Halo Spitze 52/80).
- **Ego-Zeiten:** Ausholen 3–28 Bilder (Halo ≤ 3, Chivalry 13, Dark Messiah 28), Schlag 3–16 (schnelle Bahn 3–10), Mitte 1–4 Bilder
  verdeckt, Rückkehr 23 Bilder (Halo), Block ein 23 Bilder (Dark Messiah), Lunge-Kamerafahrt ≈ 7 Bilder (Halo).
- **Destiny-Bezug** ([4](#4-destiny-schwert-in-der-schulteransicht)): leichter Schlag ≈ 14 Bilder, Folge bis Ruhe 54–58 Bilder, schwerer
  Angriff 14 Bilder Ausholen / 50 gesamt, Block ≤ 9 Bilder; bei Option A Einstieg 9 + 20 Bilder, Ausstieg 6 Bilder, Figur 42 % H,
  Körpermitte 44–48 % B, Kopfoberkante 3–5 pp unter der Mitte.

**Glefe (BASIC-17)**
- **Maße:** Schaft 0,52–0,55, Kopf 0,45–0,48 (Gehäuse/Emitter 0,11–0,16, Klinge 0,30–0,35), Kragen 0,30, vordere Griffzone 0,35–0,55 (Refusal of the Call 0,31–0,35),
  Schaft-Ø 0,03–0,04, Kopf max. 0,08–0,11, H/L 0,09–0,12 ([3](#3-form-destiny-glefen-manifestbilder)). BASIC-17 H/L 0,111 passt.
- **Hüfte:** Spitze 63–69/46–50, Kopfbeginn 60/69, Hand 73/91, Hülle ≈ 46–77 × 46–100, Schaft 39–46° ([6](#n-g-huefte)).
- **Schuss:** Projektil sichtbar 2 Bilder nach Auslösen an der Bildmitte (46–49/43–50), Glühen ≈ 7 Bilder; Waffe +8 pp hoch nach
  17–21 Bildern, zurück nach 33; Kamera +10–13 pp H, Spitze nach 4–6, abgeklungen nach 22–31 Bildern; Kadenz 51–63 Bilder, Magazin 6.
- **Schlag:** Ausholen 8, Bahn 10, Mitte 3 Bilder verdeckt; Kombo-Takt 37–43 Bilder; zurück in Hüfte 59 Bilder.
- **Schild:** ein 10–11 Bilder, Klinge senkrecht (Spitze 59/36, Hülle 51,5–100 × 36–100), Mitte frei, Effekt als Vollbild-Verzerrung;
  aus per Schuss 3–13 Bilder.
- **Nachladen:** 3,07–3,50 s bis ruhig (Lubrae, Nezarec), Vexcalibur 2,283 s (137 Bilder); erste Hüftpassage 0,2–0,3 s früher,
  Überschwingen 7–8 pp hoch.
- **Fadenkreuz:** Kreis Ø 3,4 % H; in der einen HUD-Quelle 7,5 pp unter der Mitte (offen). **Kein ADS**, Zieltaste = Schild.

## 9. Entscheidungsvorlage Schwert (für den Nutzer, über Sightline)

<a id="n-entscheidung"></a>
Ausgangslage: BALLON Paket 7 ist ein **Ego-Prototyp** in Unity (Arme und Waffe im Bild, keine Spielerfigur). Destiny begründet die
Schulteransicht mit Schlägen, die außerhalb des Ego-Sichtfelds treffen ([7](#n-e-schwert)); die Glefe bleibt dort bewusst in Ego.

| Option | Was es heißt | Zahlen, die tragen | Aufwand im BALLON-Prototyp (Einschätzung) | Risiko |
|---|---|---|---|---|
| **A – wie Destiny** | beim Ziehen Wechsel in die Schulteransicht, Angriffe/Block/Sprint in Third Person | Einstieg 9 + 20 Bilder, Ausstieg 6 Bilder; Figur 42 % H links der Mitte, Kamera ≈ 0,1 KH über dem Scheitel, 0,13–0,25 KH seitlich; Schläge 14–58 Bilder, Block ≤ 9 Bilder ([4](#4-destiny-schwert-in-der-schulteransicht)) | **hoch:** ganze Spielerfigur mit Rig und eigenem Satz (Ruhe, Lauf, Sprint, 2–3 leichte, schwerer Angriff, Block, Übergänge), Schulterkamera mit Kollision und Ein-/Ausfahrt, Umschalten von Eingabe und Fadenkreuz; Bruch zum Ego-Rest des Pakets | Peek-Vorteil (Destiny-Kritik), doppelte Animationspflege; im Prototyp wenig Rückmeldung zum Ego-Gefühl |
| **B – Ego nach Vorbildern** | Schwert bleibt in der Ego-Sicht wie Glefe und Gewehre | Ruhe rechts/unten, Mitte frei; Ausholen 3–28, Schlag 3–16 Bilder, Mitte 1–4 Bilder verdeckt; Block ein 23 Bilder (Dark Messiah); Halo: Lunge 7 Bilder + Schlag 3 + Rückkehr 23 ([5](#5-ego-schwerter-anderer-spiele)); Form aus › 2 | **niedrig bis mittel:** Arme + Schwert als Ego-Modell, 5–7 Clips (Ruhe, Sprint, 2 Schlagrichtungen, schwerer Schlag, Block ein/halten/aus), Kamera-Impuls; gleiche Technik wie BASIC-17 | Reichweite in Ego schwer zu schätzen (alle Fachquellen) → Reichweitensignal oder Heranziehen nötig; breite Schläge außerhalb des Bilds nicht sichtbar |
| **C – Mischform** | Ego für Ruhe, leichte Schläge, Block; kurzer Kamerarückzug (Destiny-artig, 6–20 Bilder) nur für den schweren Angriff | B plus Destiny-Einstieg/-Ausstieg für einen Vorgang | **mittel bis hoch:** alles aus B, dazu für den einen Third-Person-Moment doch eine sichtbare Figur und die Kamerafahrt | zwei Darstellungen eines Schwerts; kurze Fahrten können Übelkeit auslösen (Einzelstimmen) |

**Empfehlung dieser Version: B.** Sie hält das Paket in einer Perspektive, nutzt dieselbe Ego-Technik wie die Glefe und ist der
kleinste Aufwand für einen Prototyp. Übernehmen lässt sich aus Destiny die Form (Klinge 0,65–0,70 L, H/L 0,07–0,10 für ein schlankes
Schwert) und aus Halo das Reichweitensignal plus kurze Lunge. A lohnt erst, wenn BALLON ohnehin eine Third-Person-Figur bekommt;
C nur, wenn der schwere Angriff ausdrücklich „groß“ wirken soll. Entschieden wird in BALLON.

## 10. Offen und nicht messbar

- **Schulteransicht:** Winkel-FOV (Hintergrundmaßstab ist Parallaxe), Kameraabstand in Metern, Normaltempo der Schwertabläufe, Ablegen
  des Blocks, Sprint mit Schwert, ob der Io-Menüschnitt einem Waffenwechsel entspricht; Ausstieg nur an einem Twitch-Clip (Spieler in Bewegung).
- **Ego-Vorbilder:** Skyrim ohne Mods (keine 60/s-Quelle mit Schwert gefunden), Mordhau und Titanfall 2 nicht untersucht, Kamera-Kick nicht
  quantifiziert, Parade bei Chivalry 2 ohne Eingabespur unbelegt, Rückkehr nach einem Einzelschlag nur bei Halo.
- **Glefe:** Nachladen mit HUD-Zunahme, Treffer am Schild, Schild loslassen ohne Schuss, Sprint, Kamerakick bei Nezarec, Kadenz gegen
  Manifest (51–63 statt 65,4 Bilder), tiefe Fadenkreuzlage (zweite HUD-Quelle nötig); legendäre Glefe der Optik-Familie (Aggressive) in Ego.
- **Form:** keine orthografische Seitenansicht; 3/4-Werte nur als Größenordnung. Lubrae's Ruin, The Heron und Vexcalibur im Manifestbild
  beschnitten.
- **Bewertung:** Reddit nicht erreichbar; Spielerstimmen zu Wucht und Kamera beim Block nicht gefunden; keine Entwicklerquelle zu Halo-Lunge
  und Mordhau-Kamera.

## 11. Prüfung und Zählung

- **Gemessen:** 17 Manifestbilder (8 Schwerter, 9 Glefen) [M]; Destiny-Schulteransicht 10 Einträge (8 [M], 2 [O]) aus 3 Quellen; Ego-Vorbilder
  17 Einträge (15 [M], 2 [O]) aus 4 Titeln; Glefe in Ego 18 Einträge (15 [M], 3 [O]).
- **Unteragenten** (Nutzerentscheidung über Sightline, 28.10.2026: Unteragenten ausdrücklich erwünscht): Opus high „Ego-Vorbilder Schwert“
  (10 Videos geprüft, 4 gemessen), Opus high „Glefe in Ego“ (4 Videos, Versatz der Abschnittsdateien am Originalstream bestimmt), Sonnet
  medium „Spieler- und Entwicklerstimmen“ (Schwert 13 + 5, Glefe 10 + 4, andere 19 + 11 geladene Quellen, ≈ 28 nur Suchauszug).
- **Koordinator-Prüfung:** 6 Videoquellen selbst per yt-dlp geprüft (Io, Ultraclocked 2026, Aztecross-Clip, beide Boosh-Ninja-Showcases, Developer Insights), die übrigen 12 von den Unteragenten (Kanal, Datum, Titel, Länge); **8 von 8 nachgemessenen Zahlen bestätigt**
  (Ego: Dark Messiah Spitze 69/42 und Parierstange 57/53, Chivalry 2 Parierstange 64/72, Halo Heft 52/52; Glefe: Lubrae Spitze 63/46,
  Projektil 46/50, Schildspitze 59/36, Fadenkreuz 50/57,5 Ø 3,4 % H); 3 von 3 Stimmen-URLs geladen und Titel passend; Entwicklerzitat
  Glefe/Schwert selbst aus den Untertiteln von `6-26SH5jSwQ` gelesen. **Nicht übernommen:** Skyrim-Fehlanzeige (keine Quelle), Sichtungen
  ohne Zahl als [O] gekennzeichnet; eigene Vorab-Sichtung „Schläge“ bei Lubrae widerlegt (Schüsse).
- **Belege** (außerhalb des Repos, `~/Library/Caches/CubeEscape/reference/nahkampf-0.29/`): `manifest/axis8/s1.png`, `s2.png`, `g1.png`, `g2.png`
  (Lineale der Manifestbilder), `schwert/entry.jpg`, `light1.jpg`, `heavy1.jpg`, `uc_guard1.jpg`, `guard_full.jpg`, `rest_io.jpg`, `az_exit.jpg`,
  `ego-vorbilder/frames/*`, `glefe/*.jpg`, `pruefung/check_ego.jpg`, `gl.jpg`, `cg.jpg` (Nachmessung).
