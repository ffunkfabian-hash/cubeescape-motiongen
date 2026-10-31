# Waffenwerte – Kennzahlen, Trefferschwellen und Bedienkosten je Waffe

Referenzanalyse REF 0.27 „Statline“ (25.10.2026) für die Waffenreihe **BASIC** (Projekt `cubeescape-ballon`) und Cube Escape: welche Zahlen eine Waffenkarte oder
Datenquelle nennt (Kadenz, Magazin, Schaden je Trefferzone und Entfernung, Stat-Balken, Ziehen/Nachladen) und wie sich daraus Trefferzahl und ideale
Tötungszeit (TTK) ergeben – bei Destiny 2 (Waffenkarte, Manifest-Basiswerte, Modell von 2025) und im Vergleich bei Halo Infinite, Apex Legends, Valorant und
Call of Duty: Warzone. Gesammelt hat eine Codex-Mac-Sitzung (Auftrag „Ego-Bewegung“ Runde 2, Thema Waffenwerte, 25.10.2026). Diese Version hat die Zuarbeit nach dem
[Analyse-Standard](standard.md) geprüft, gegen den Bestand abgeglichen und nur Belegtes übernommen ([8](#8-prüfung-und-zählung)). Hier stehen Beobachtungen und
Quellenzahlen; Schlüsse und Startwerte entstehen in BASIC bzw. Cube Escape. Maschinenlesbar: [`data/waffenwerte.json`](../data/waffenwerte.json). Nachbarthemen:
[Nachladen](nachladen.md) (0.25), [Waffenwechsel](wechsel.md) (0.26), [Rückstoß](rueckstoss.md) (0.16), [Zielbewegung](zielbewegung.md) (0.17); die Zielhilfe (Aim-Assist-Stat und Zielhilfe im Spiel) ist ein eigenes Thema: [Zielhilfe](zielhilfe.md) (0.28).

**Status:** **[M]** am Einzelbild gemessen; **[S]** Sekundärquelle (Datenbank, API, Rechenmodell, eingeblendete Menüzahl); **[B]** Entwickler (Patchnotes, Blog);
**[C]** Spielerstimme, Beitrag bestätigt, Kommentare nicht gelesen; **[O]** Sichtung ohne belastbare Zahl. **Fast alle Zahlen sind [S] oder [B] und keine eigene Messung**: gemessen ist nur
die Füllung zweier Handling-Balken. TTK-Werte sind **Rechnungen** aus Quellwerten (erster Treffer bei t = 0, ohne Verfehlen, Reaktion, Ziehen, ADS, Flug), keine Spielmessung. **Jede Zahl gilt
für das genannte Beispiel, den genannten Zeitstand und Modus** – kein Klassenmittel, keine Rangliste über Spiele hinweg. Die Stat-Zahlen von Destiny (0–100) sind weder Meter noch Sekunden noch Prozent.

## 1. Quellen und Methode

- **Videos (3, am 25.10.2026 per yt-dlp geprüft):** Ultraclocked, `QxSa4m3wIEA` (15.05.2021, „Destiny 2 - Chroma Rush (Legendary Auto Rifle) - Animations & Sounds“, 60 fps, 40 s) und `DFn14wAPluA`
  (13.05.2021, „Destiny 2 - Gridskipper (Legendary Pulse Rifle) - Animations & Sounds“, 60 fps, 45 s): Menü-Waffenkarte bei Bild 60 (t = 1,000 s); Skovos, `WH5xpA7tfY8` (18.04.2020, „Valorant: Weapons and Guns Guide + Alternate Fire [Explained in Detail]“, 30000/1001 fps, 484 s): Kaufmenü der Beta, Ghost-Karte bei 60 s. Alle Zeitstempel liegen innerhalb der Länge.
- **Datenquellen [S]:** Bungie-Manifest (DestinyInventoryItemDefinition, Build 245114.26.10.13.2000-1-bnet.66137, Abruf 25.10.2026, **als Kopie der Zuarbeit gegen die 113 Gruppen geprüft, nicht erneut von Bungie geladen**);
  D2Foundry Oracle Engine (`weapon_formulas.json`, letzter Dateicommit 07.05.2025, Patch 8.2.6; Code `build.rs`, `stat_calc.rs`, `ttk_calc.rs`; **Quelltext und Formeldatei nicht live geladen** (Kopie der Zuarbeit), nur die Commit-Historie der Formeldatei per GitHub-API abgefragt); valorant-api.com (Community-Dienst, keine Riot-API, kein Versionsdatum);
  ttkdb.com (Apex R-301, Basis 16.09.2026); allmeta.gg (Warzone XM4, Stand 19.10.2026).
- **Entwickler [B]:** Bungie Dev Insights Season 22 (16.08.2023: Zoom und Schadensabfall getrennt; Live-Seite ist nur eine JavaScript-Hülle, **über das Wayback-Archiv bestätigt**); Halo Waypoint Season 5 Ranked (13.10.2023) und Reckoning (17.10.2023);
  Halo Fleetcom (30.07.2024, Direktabruf 403, **per Wayback bestätigt**); Riot Patch 9.10 (19.11.2024); Respawn Takeover (10.02.2025); Call of Duty BO6 Preseason (Sammelstand 08.11.2024).
- **Spielerstimmen [C]:** sechs Reddit-Threads (C1–C6); per Pullpush als **Beiträge** bestätigt (Subreddit, Titel, Datum). Die Kommentarverläufe wurden nicht nachgelesen; Zustimmungszahlen stammen aus Suchauszügen der Zuarbeit und werden nicht übernommen.
- **Zeitstände getrennt halten:** Manifest 13.10.2026 (Basiswerte), Formeln Patch 8.2.6 vom 07.05.2025 (nur als historisches Rechenmodell bei einem synthetischen Statwert 50), Menü-Aufnahmen 2021 (mit Ausrüstung), Apex 16.09.2026, Warzone 19.10.2026, Valorant-API 25.10.2026, Halo 2023 und 2024.
  Nie Schaden aus 2025 mit Stats aus 2026 zu einem „echten Roll“ verbinden.
- **TTK-Definition:** ideale Zeit vom ersten bis zum letzten Treffer = (Treffer − 1) · 60 / RPM (Salven: (Pause + (n − 1) · Binnenabstand)/30); Gesundheit je Beispiel genannt (Valorant 150, Apex 200, Warzone 300, Destiny-Modell 230 nur Präzision).
- **Eigene Bildprüfung:** Balkenfüllung und Karten-Zahlen am Einzelbild (Bild 60, 1920 × 1080, Leiste x = 1539–1744); ±3 Prozentpunkte der Leistenlänge.

## 2. Messtabelle

### 2.1 Waffenkarten im Bild
<a id="w-karten"></a>

| Karte | Quelle | Zeitstempel | Wert | Status |
|---|---|---|---|---|
| **Chroma Rush** (Auto Rifle, Rapid-Fire Frame, Menü 2021) | Ultraclocked `QxSa4m3wIEA` | Bild 60 (1,000 s) | eingeblendet **720 RPM, Magazin 57**; Handling-Balken gefüllt **≈ 37 % der Leiste** (76 von 206 px; ±3 pp) | RPM/Magazin [S], Balken [M] |
| **Gridskipper** (Pulse Rifle, Rapid-Fire Frame, Menü 2021) | Ultraclocked `DFn14wAPluA` | Bild 60 (1,000 s) | eingeblendet **540 RPM, Magazin 36**; Handling-Balken **≈ 30 %** (61 von 206 px; ±3 pp) | RPM/Magazin [S], Balken [M] |
| **Ghost** (Valorant-Beta, Kaufmenü) | Skovos `WH5xpA7tfY8` | 60 s | eingeblendet: halbautomatisch, **6,75 Schuss/s, Magazin 15**, Wandpenetration „Medium“; **0–30 m Körper 30 / Kopf 105 / Bein 26**, **30–50 m 25 / 88 / 21** | [S] (Einblendung), [O] für den Vorgang |

**Die Zuarbeit las 36 % und 29 % (±3 pp), Prüfer und Koordinator 36,9 % und 29,6 %; der Bestand ([destiny2.md](destiny2.md#z-chroma-rush)) hat 37 und 30 (±2) – drei unabhängige Ablesungen derselben Balken, kein neuer Messwert.**
Die Ghost-Karte las erst diese Version aus; die Zuarbeit nannte sie nur als „Kaufmenü mit Waffenkarte“. Die API-Kopie (25.10.2026) nennt für die Ghost dieselben 6,75 Schuss/s und 30 / 105 / 25,5 bzw. 25 / 87,5 / 21,25 (die Karte rundet:
26 und 88 und 21), aber **Magazin 13 statt 15** – ein Unterschied zwischen Beta 2020 und Stand 2026, dessen Ursache nicht geprüft ist.

### 2.2 Destiny 2: Menü mit Ausrüstung gegen Manifest-Basis
<a id="w-menue-basis"></a>

| Waffe | Quelle | Menü 2021, ausgerüstet (Balken ±2 [M], Magazin eingeblendet [S]) | Manifest-Basis 2026 [S] | Unterschied |
|---|---|---|---|---|
| Chroma Rush (D2-006) | `QxSa4m3wIEA` | Range 32 · Stability 71 · Handling 37 · Reload 52 · **57 Magazin** | Range 25 · Stability 56 · Handling 35 · Reload 47 · **51 Magazin** | +7 · +15 · +2 · +5 · +6 |
| Gridskipper (D2-057) | `DFn14wAPluA` | Range 58 · Stability 54 · Handling 30 · Reload 42 · **36 Magazin** | Range 33 · Stability 47 · Handling 27 · Reload 35 · **35 Magazin** | +25 · +7 · +3 · +7 · +1 |

Menü-Werte aus der Bestandszeile ([Chroma Rush](destiny2.md#z-chroma-rush), [Gridskipper](destiny2.md#z-gridskipper-salve)); Basis aus dem Manifest. Die Menükarten zeigen ausgerüstete Werte (Perks, Aufsätze, Waffenveredelung unbekannt), die
Basiswerte nicht; zusätzlich liegen fünf Jahre Balance dazwischen. **Eine Ursache ist aus den Bildern nicht zuordenbar**; der Handling-Balken liegt bei Chroma Rush innerhalb ±2, bei Gridskipper um 3 darüber.

### 2.3 Destiny 2: Manifest-Basiswerte je Rahmen (113 Gruppen)

Gewählt wurde je **Typ × Munitionsart × Intrinsic-Hash** ein konkretes legendäres Beispiel – 113 Gruppen, nicht 113 entworfene Rahmen (gleich benannte Intrinsics tragen teils verschiedene Hashes; Alias-Gruppen nicht ausgeschlossen).
Die Tabelle steht im [Anhang A](#anhang-a-manifest-basiswerte-113-gruppen) und in `data/waffenwerte.json › groups`. **Rohdaten, nicht bewertet** (`evaluated=false`); kein Mittel, keine Perkbelegung, keine Aussage zur Erwerbbarkeit.
`R/H/L/S/Z/AA` = Reichweiten-, Handling-, Reload-, Stabilitäts-, Zoom- und Aim-Assist-Stat (API-Zahlen, **keine Einheiten**). Nullungen (`—`): 17 Gruppen ohne Kadenz (Bögen 4, Fusionsgewehre 5, lineare Fusionsgewehre 2, Schwerter 6) und 20 ohne Magazin (Heat-Waffen 10, Bögen 4, Schwerter 6); Hitzewaffen und Schwerter haben kein reguläres Schussmagazin. Acht Werte, die das Manifest trägt, hat die Zuarbeit bewusst genullt (die sechs Schwert-Magazine sowie Magazin 0 und Kadenz 80 des Bogens A Good Shout); Heat-Waffen tragen im Manifest gar keinen Magazin-Stat.

Aus den 113 Gruppen folgt **ohne Mittelung**: gleich benannte Rahmen unterscheiden sich in den Stats (Support Frame, fünf Gruppen: Handling 63–82, Reload 57–68, Magazin 44–47 bei gleichen 600 RPM), und „Rapid-Fire Frame“ bedeutet beim Automatikgewehr 720 RPM (Chroma Rush), beim Impulsgewehr 540 RPM (Gridskipper), beim Scout 260 RPM (Manifest). Der Name allein trägt keine Zahlen.

### 2.4 Destiny 2: historisches Schadens- und Handlingmodell (Patch 8.2.6, 07.05.2025)
<a id="w-modell-2025"></a>

**Kein Live-Balancenachweis für Oktober 2026.** 83 der 113 Gruppen haben eine Modellformel, 30 nicht (10 Heat-Waffen, drei der fünf Support Frames, High-Impact Longbow und der schwere Bogen A Good Shout, Area Denial Frame, Spread Shot, MIDA Synergy (Schrotflinte), Rapid Fire Slug, Micro-Missile Frame des Impulsgewehrs, Together Forever als Spezialmunition, High-Impact-Scharfschützengewehr The Helmsman, Disruption, Aggressive Burst der Maschinenpistole, sechs Schwerter – nicht still dem ähnlich benannten Modell zugeordnet; Pinpoint Slug und die übrigen Micro-Missile Frames haben ein Modell).
Die Modellkadenz weicht bei **13 der 48 Zuordnungen mit beidseitiger Kadenz** vom Manifest ab (reine Rundungsunterschiede unter 0,1 % – drei Fälle – nicht mitgezählt): zwei deutlich (Age-Old Bond 360 gegen 400, Retraced Path 900 gegen 1000), elf um 0,7–1,1 % (z. B. 138,5 gegen 140; 257,1 gegen 260). Das Modell ist damit veraltet und
nur als **historische Parametervariation** brauchbar. Umrechnung nach `build.rs`: Präzisionsfaktor = 1,5 + Datenwert/51; Salvenzeiten = Datenwert/30. PvE-Spalten sind **unskalierte Referenzschäden** vor Gegnerklasse, Aktivität, Power und Buffs.
TTK: synthetisch an 230 HP, ausschließlich Präzision, ohne Abfall, Perks, Latenz, Eingabe- oder ADS-Zeit; erster Treffer bei t = 0. Bei Geschossen mit Explosion, Pellets, Aufladen oder Sonderprojektilen bleibt der einfache Schaden leer.
Die 43 Zeilen wurden von einem Prüfer aus den Formeldaten unabhängig nachgerechnet (0 Abweichungen über 0,01 s).

| Typ / Modellrahmen (2025) | Körper / Präzision PvP | Faktor PvP | PvE-Referenz Körper / Präzision | Modell-RPM | TTK 230 HP (nur Präzision) |
|---|---:|---:|---:|---:|---:|
| Auto Rifle / Adaptive Frame | 15,03 / 26,38 | 1,75 | 15,01 / 23,40 | 600,0 | 0,80 s |
| Auto Rifle / High-Impact Frame | 24,00 / 43,06 | 1,79 | 22,00 / 35,16 | 360,0 | 0,83 s |
| Auto Rifle / Lightweight Frame | 13,60 / 23,06 | 1,70 | 13,41 / 20,11 | 720,0 | 0,75 s |
| Auto Rifle / Precision Frame | 20,00 / 33,92 | 1,70 | 20,00 / 31,18 | 450,0 | 0,80 s |
| Auto Rifle / Rapid-Fire Frame | 13,60 / 23,06 | 1,70 | 13,41 / 20,11 | 720,0 | 0,75 s |
| Auto Rifle / Support Frame | 18,63 / 29,93 | 1,61 | 18,63 / 29,93 | 600,0 | 0,70 s |
| Hand Cannon / Adaptive Frame | 44,50 / 79,84 | 1,79 | 46,50 / 69,75 | 138,5 | 0,87 s |
| Hand Cannon / Aggressive Frame | 49,03 / 90,85 | 1,85 | 50,00 / 79,90 | 120,0 | 1,00 s |
| Hand Cannon / Heavy Burst | 24,00 / 52,93 | 2,21 | 25,01 / 44,86 | 257,1 | 0,93 s |
| Hand Cannon / Lightweight Frame | 44,50 / 79,84 | 1,79 | 46,50 / 69,75 | 138,5 | 0,87 s |
| Hand Cannon / Precision Frame | 45,30 / 70,61 | 1,56 | 40,00 / 60,00 | 180,0 | 1,00 s |
| Machine Gun / Adaptive Frame | 40,99 / 57,47 | 1,40 | 34,26 / 48,03 | 450,0 | 0,53 s |
| Machine Gun / Aggressive Frame | 36,15 / 47,14 | 1,30 | 36,15 / 47,14 | 600,0 | 0,40 s |
| Machine Gun / High-Impact Frame | 47,57 / 69,50 | 1,46 | 39,60 / 57,85 | 360,0 | 0,50 s |
| Machine Gun / Rapid-Fire Frame | 25,52 / 33,27 | 1,30 | 21,40 / 27,90 | 900,0 | 0,40 s |
| Pulse Rifle / Adaptive Frame | 22,00 / 36,44 | 1,66 | 22,81 / 37,80 | 385,7 | 0,93 s |
| Pulse Rifle / Aggressive Burst | 15,49 / 30,23 | 1,95 | 18,60 / 31,55 | 450,0 | 0,73 s |
| Pulse Rifle / Heavy Burst | 23,00 / 42,61 | 1,85 | 18,79 / 34,34 | 327,3 | 0,80 s |
| Pulse Rifle / High-Impact Frame | 21,50 / 38,57 | 1,79 | 26,40 / 42,19 | 337,5 | 0,67 s |
| Pulse Rifle / Legacy PR-55 Frame | 19,70 / 31,48 | 1,60 | 19,20 / 31,81 | 450,0 | 0,87 s |
| Pulse Rifle / Lightweight Frame | 19,70 / 31,48 | 1,60 | 19,20 / 31,81 | 450,0 | 0,87 s |
| Pulse Rifle / Rapid-Fire Frame | 15,00 / 27,79 | 1,85 | 16,80 / 28,49 | 540,0 | 0,80 s |
| Scout Rifle / Aggressive Frame | 53,99 / 91,58 | 1,70 | 70,20 / 103,92 | 120,0 | 1,00 s |
| Scout Rifle / High-Impact Frame | 42,00 / 84,41 | 2,01 | 40,00 / 70,20 | 150,0 | 0,80 s |
| Scout Rifle / Lightweight Frame | 38,01 / 64,46 | 1,70 | 32,02 / 56,20 | 200,0 | 0,90 s |
| Scout Rifle / Precision Frame | 38,51 / 69,08 | 1,79 | 38,00 / 60,73 | 180,0 | 1,00 s |
| Scout Rifle / Rapid-Fire Frame | 28,00 / 54,62 | 1,95 | 27,50 / 46,64 | 257,1 | 0,93 s |
| Sidearm / Adaptive Burst | 20,09 / 36,44 | 1,81 | 20,00 / 31,96 | 490,9 | 0,73 s |
| Sidearm / Adaptive Frame | 36,08 / 57,66 | 1,60 | 36,00 / 50,47 | 300,0 | 0,60 s |
| Sidearm / Heavy Burst | 33,08 / 52,86 | 1,60 | 30,00 / 42,06 | 327,3 | 0,73 s |
| Sidearm / Lightweight Frame | 31,04 / 49,60 | 1,60 | 31,00 / 43,46 | 360,0 | 0,67 s |
| Sidearm / Precision Frame | 40,15 / 64,17 | 1,60 | 40,00 / 56,08 | 257,1 | 0,70 s |
| Sidearm / Rapid-Fire Frame | 25,11 / 39,64 | 1,58 | 25,00 / 35,05 | 450,0 | 0,67 s |
| Sidearm / Together Forever | 36,08 / 57,66 | 1,60 | 36,00 / 50,47 | 300,0 | 0,60 s |
| Sniper Rifle / Adaptive Frame | 119,00 / 386,16 | 3,25 | 127,33 / 413,19 | 90,0 | 0,00 s |
| Sniper Rifle / Aggressive Frame | 135,01 / 472,52 | 3,50 | 144,46 / 505,60 | 72,0 | 0,00 s |
| Sniper Rifle / Rapid-Fire Frame | 85,00 / 292,51 | 3,44 | 90,95 / 312,98 | 138,5 | 0,00 s |
| Submachine Gun / Adaptive Frame | 11,50 / 19,73 | 1,72 | 11,25 / 16,88 | 900,0 | 0,73 s |
| Submachine Gun / Aggressive Frame | 13,60 / 23,87 | 1,75 | 14,00 / 21,00 | 720,0 | 0,75 s |
| Submachine Gun / Lightweight Frame | 10,60 / 20,27 | 1,91 | 10,86 / 17,99 | 900,0 | 0,73 s |
| Submachine Gun / MIDA Synergy | 10,60 / 20,27 | 1,91 | 10,86 / 17,99 | 900,0 | 0,73 s |
| Submachine Gun / Precision Frame | 16,55 / 26,45 | 1,60 | 17,01 / 23,85 | 600,0 | 0,80 s |
| Trace Rifle / Adaptive Frame | 15,04 / 19,90 | 1,32 | 12,51 / 16,80 | 900,0 | 0,73 s |

**Handling und Nachladen als Kennlinie bei einem synthetischen Statwert 50** (nicht auf reale Rolls anwendbar; Chroma Rush hat z. B. Basis-Handling 35). Gerundete Rechenwerte, keine Bildmessung:

| Historische Modellfamilie | Ziehen / Wegstecken / ADS bei Handling 50 | Nachladen bei Reloadstat 50 | Hüft-Schadensabfall bei Rangestat 50 |
|---|---|---:|---|
| Auto Rifle | 0,38 / 0,35 / 0,30 s | 1,81 s | 17,0–40,0 m; Boden 0,50 |
| Combat Bow | 0,59 / 0,45 / 0,44 s | — | — |
| Fusion Rifle | 0,43 / 0,30 / 0,33 s | 1,99 s | 12,8–30,6 m; Boden 0,45 |
| Glaive | 0,32 / 0,37 / 0,00 s | 2,62 s | 17,7–40,2 m; Boden 0,33 |
| Grenade Launcher | 0,41 / 0,37 / 0,41 s | 2,34 s | — |
| Hand Cannon | 0,33 / 0,37 / 0,25 s | 2,56 s | 20,5–30,5 m; Boden 0,33 |
| Linear Fusion Rifle | 0,43 / 0,30 / 0,33 s | 2,02 s | — |
| Machine Gun | 0,38 / 0,35 / 0,40 s | 4,82 s | 29,6–38,2 m; Boden 0,50 |
| Pulse Rifle | 0,39 / 0,37 / 0,36 s | 1,87 s | 19,8–40,0 m; Boden 0,50 |
| Rocket Launcher | 0,46 / 0,38 / 0,42 s | 3,09 s | — |
| Scout Rifle | 0,40 / 0,38 / 0,33 s | 1,99 s | 38,1–60,8 m; Boden 0,50 |
| Shotgun | 0,38 / 0,40 / 0,33 s | — | 5,2–14,5 m; Boden 0,00 |
| Sidearm | 0,29 / 0,33 / 0,23 s | 1,58 s | 13,0–23,5 m; Boden 0,50 |
| Sniper Rifle | 0,38 / 0,34 / 0,41 s | 2,85 s | — |
| Submachine Gun | 0,35 / 0,32 / 0,26 s | 1,82 s | 13,6–23,0 m; Boden 0,50 |
| Trace Rifle | 0,38 / 0,35 / 0,30 s | 2,00 s | 19,8–35,9 m; Boden 0,40 |

ADS-Abfallmeter werden nicht aus Zoom berechnet: Bungie trennte Zoom und Schadensabfall in Season 22 (ein eigener ADS-Falloff-Scalar [B]); aktuelle ADS-Meter bleiben `null`. Ein hoher Aim-Assist-Stat ist weder eine Trefferwahrscheinlichkeit noch eine Prozentstärke (Zielhilfe: eigenes Thema).

### 2.5 Vergleich: Kadenz, Schwellen, ideale TTK mit benanntem Szenario
<a id="w-vergleich"></a>

Alle Werte [S] oder [B] plus **Rechnung**, keine neuen Tötungszeitmessungen; verschiedene Zeitstände und Gesundheitsmodelle – **keine Rangliste**. Alle neun Zeilen von einem Prüfer aus den Quellwerten nachgerechnet (0 Abweichungen).

| Spiel / Beispiel · Stand | RPM / Magazin | Körper / Kopf im ersten Bereich | Ziehen / ADS / Nachladen | Trefferbedingung und ideale TTK ab erstem Treffer | Quelle |
|---|---|---|---|---|---|
| Halo Infinite Bandit Evo · 13./17.10.2023 | 174 (2,9/s) / unbekannt | Schaden unbekannt; 5 Kopftreffer (B3: „five headshots“) oder 7 Körpertreffer; Zoom 1,6× | unbekannt | (5 − 1)/2,9 = **1,38 s**; Körpertreffer (7 − 1)/2,9 = **2,07 s** (Rechnung) | B2/B3 |
| Halo Infinite Bandit Evo · 30.07.2024 | 162,9 (2,715/s) / unbekannt | Trefferzahl **aus 2023 angenommen** | unbekannt | **1,47 s** / **2,21 s** (Rechnung); keine Aussage über den Stand 2026 | B4 + B3 |
| Apex R-301 · Quelldaten 16.09.2026 | 810 / 21 | Körper 15; Kopf unbekannt (UI 20, Rohmodell 15 × 1,3 = 19,5) | 0,60 / 0,27 / 2,40 s taktisch, 3,20 s leer | 200 HP: 14 Körpertreffer = **0,96 s** (225 HP: 15 Treffer, 1,04 s); ohne Aufsätze | S6 |
| Valorant Vandal · API 25.10.2026 | 585 / 25; ADS 526,5 | 40 / 160 (0–50 m) | 1,00 / unbekannt / 2,50 s | 150 HP: Kopf 1 Treffer, **0 s**; Körper 4 Treffer **0,31 s**; ADS-Körper **0,34 s** | S5 |
| Valorant Phantom · API 25.10.2026 | 660 / 30; ADS 594 | 39 / 156 bis 20 m; 35 / 140 darüber | 1,00 / unbekannt / 2,50 s | 150 HP: nah Kopf 0 s, Körper **0,27 s**; > 20 m Kopf 2 Treffer **0,09 s**, Körper **0,36 s** | S5; B5 |
| Valorant Guardian · API 25.10.2026 | 315 / 12 | 65 / 195 | 1,00 / unbekannt / 2,50 s | 150 HP: Kopf 0 s, Körper 3 Treffer **0,38 s** | S5 |
| Valorant Operator · API 25.10.2026 | 36 / 5 | 150 / 255; Winkelzoom 2,5× laut API (Bildmaßstab im Bestand 3,34, [visiere.md](visiere.md#v-valorant-operator)) | 1,50 / unbekannt / 3,70 s | 150 HP: Körper und Kopf 1 Treffer, 0 s; Scopezeit und Reaktion nicht enthalten | S5 |
| Valorant Sheriff · API 25.10.2026 | 240 / 6 | 55 / 159,5 bis 30 m; 50 / 145 darüber | 1,00 / unbekannt / 2,25 s | 150 HP: nah Kopf 0 s, fern Kopf **0,25 s**; Körper 3 Treffer **0,50 s** in beiden Bändern | S5 |
| Warzone XM4 (BO6-Waffenmodell) · Anbieter 19.10.2026 | 800 / 30 | Schaden und Kopffaktor unbekannt (Panel 1,33×, Verlauf 1,35×) | unbekannt / ADS 0,27 / 2,43 s; Sprint→Schuss 0,19 s | 300 HP, 3 Platten: Körper 10 / 12 / 15 Treffer bis 33 / bis 51 / über 51 m = **0,675 / 0,825 / 1,050 s**; Kopf **0,525 / 0,675 / 0,825 s** | S7; B7 |

Halo-Zeilen: Status **[B] + Rechnung** – die Quelle nennt Kadenz, Trefferzahl und Zoom, die Sekunden sind eigene Arithmetik. Warzone: BO6-Multiplayer und Warzone haben getrennte Schadensmodelle [B7]; die Zeile ist ausdrücklich Warzone.

## 3. Abgleich mit dem Bestand

| Eintrag | Bestand | Zuarbeit | Entscheidung |
|---|---|---|---|
| Chroma Rush, Gridskipper (Menükarte) | [destiny2.md](destiny2.md#z-chroma-rush) (0.7.0): Menü 720/57, Handling 37 ±2; [Gridskipper](destiny2.md#z-gridskipper-salve): 540/36, Handling 30 ±2 | Balken 36 % / 29 %, RPM und Magazin gleich | **ergänzt**, deckungsgleich; neu ist der Vergleich mit dem Manifest ([2.2](#w-menue-basis)) |
| Valorant Ghost-Karte (Beta 2020) | Video `WH5xpA7tfY8` nur in [huefte.md](huefte.md) (Hüftlage Classic, Bulldog) und [visiere.md](visiere.md) (Operator; Stinger/Phantom-Kimme bei 233 und 367 s); verworfen in [rueckstoss.md](rueckstoss.md) für Rückstoß und in `data/oberflaechen.json` für sechs Skin-Angaben (Classic, Vandal, Phantom: Skins nicht zu sehen); keine Waffenkarte | „Kaufmenü mit Waffenkarte“ [O] | **neu** ([O] für den Vorgang, Kartenzahlen [S]); erst von dieser Version gelesen |
| Valorant Operator | [visiere.md](visiere.md#v-valorant-operator): Bildmaßstab 3,34 (2,5× Winkel) | Winkelzoom 2,5, 36 RPM, Magazin 5 | **ergänzt**, beide Zoomwerte getrennt: Bestand Bildmaßstab 3,34 (Winkel 2,5×), API Winkelzoom 2,5 – deckt sich |
| Valorant Phantom | [visiere.md](visiere.md) (Stinger / Phantom, Kimme): Bildmaßstab 1,43–1,44 (laut `data/visiere.json` Winkelzoom 1,25×); [rueckstoss.md](rueckstoss.md): Patch-11.08-Werte der geschützten Kugeln [S]; keine Waffenwerte (Kadenz, Schaden, Magazin) | API: Winkelzoom 1,25, 660 RPM, Magazin 30, Bänder 156/39 und 140/35 | **ergänzt**, beide Zoomwerte getrennt (Bildmaßstab im Bestand, Winkelzoom API – deckt sich); Kadenz, Magazin und Schaden **neu** |
| Valorant Vandal, Sheriff, Guardian | keine Waffenwerte im Bestand (Sheriff nur Inspektion in [inspektion.md](inspektion.md)) | API-Werte, Bänder, Rechnung | **neu** |
| Halo Bandit Evo, Warzone XM4 | keine Waffenwerte im Bestand | Entwicklerstände bzw. Anbieterstand | **neu** |
| Apex R-301 | [nachladen.md](nachladen.md#rl-av03) (0.25): 2019, leer 2,38 s bis Hüfte, Magazin 18 – anderes Modell und Stand | 2026: Magazin 21, leer 3,2 s, taktisch 2,4 s | **kein Widerspruch, getrennte Zeitstände** (2019: Nachladen bis Hüfte als Pose, Magazin 18; 2026: Datenbankwerte, Magazin 21) |
| 113 Destiny-Gruppen, Modell 2025 | keine Stat-Tabelle im Bestand | siehe 2.3 und 2.4 | **neu**, als Rohdaten bzw. historisches Modell |

## 4. Muster

**Destiny 2**
1. Ein Rahmenname bestimmt nicht die Werte: 113 Gruppen, innerhalb des Support Frames Handling 63–82 und Magazin 44–47 bei gleichen 600 RPM ([Anhang A](#anhang-a-manifest-basiswerte-113-gruppen)).
2. Menükarte (ausgerüstet) und Manifest-Basis liegen bei denselben Waffen um 1–25 Stat-Punkte auseinander ([2.2](#w-menue-basis)); Zahlen einer Karte gehören mit Roll, Jahr und Ausrüstung genannt.
3. Impulsgewehre brauchen Salvenlänge, Binnenabstand und Salvenpause; reine RPM verkürzen einen TTK-Vergleich ([2.4](#w-modell-2025), Pulse-Zeilen).
4. Handling ist ein Stat mit getrennten Ziehen-/Wegstecken-/ADS-Kennlinien; derselbe Statwert bedeutet je Familie andere Sekunden (50 → 0,29–0,59 s Ziehen). Der Reloadstat ist keine Nachladezeit.
5. Zoom und Schadensabfall sind seit Season 22 getrennte Größen [B1]; Aim Assist ist ein weiterer eigener Stat.

**Halo Infinite** – Bandit Evo: ein Präzisions-Einzelschuss (2,9 Schuss/s, 1,6×; 5 Kopf- oder 7 Körpertreffer) [B2/B3]. 2024 sank die Kadenz auf 2,715/s, **mit der erklärten Absicht, mehr Reaktionszeit zu geben**, und gleichzeitig bessere Genauigkeit bei rotem Reticle [B4] –
langsamer und besser kontrollierbar wurden gemeinsam eingestellt. Die ideale TTK beginnt am ersten Treffer und ist keine Reaktionszeit.

**Apex Legends** – R-301: 810 RPM, 21 Schuss; 14 Körpertreffer an 200 HP (zwei Drittel des Magazins), 15 an 225 HP – der Gesundheitskontext gehört zur TTK. Taktisches und leeres Nachladen sind getrennte Zustände (2,4 gegen 3,2 s). Im historischen Entwicklerstand Februar 2025 hatte sie 13 → 14 Körper, Kopf 18 [B6]; nicht mit der Datenbasis 2026 verbinden.

**Valorant** – Die Waffenkarte der Beta verband Kadenz, Magazin und Schaden je Zone schon 2020 ([2.1](#w-karten)). Die API liefert Schadensbänder: Vandal und Phantom senken die Kadenz im ADS um 10 % (585 → 526,5; 660 → 594); die Phantom wechselt jenseits 20 m von 156 auf 140 Kopfschaden und damit die Einzelschuss-Schwelle gegen 150 HP; Riot reduzierte die frühere Dreiteilung auf zwei Bänder (Patch 9.10), weil Kopftreffer weniger Schaden machten als erwartet [B5]; der Sheriff verliert die Schwelle jenseits 30 m (145).

**Call of Duty: Warzone** – XM4: die ideale TTK springt mit jedem Entfernungsband (10 → 12 → 15 Treffer, +0,15 und +0,225 s); ein Treffer kostet bei 800 RPM 0,075 s. ADS und Sprint→Schuss sind eigene Bedienkosten und werden nicht pauschal addiert. Widersprüchliche Quellwerte (Kopffaktor 1,33 / 1,35) bleiben `null`.

## 5. Bewertung: gut, nicht so gut, für wen

Eigene Einschätzungen aus den Zahlen der Tabellen, keine Spielerprobung. **Die Bewertung steht je Spiel; die je Eintrag kopierten Bewertungsfelder der Zuarbeit wurden nicht übernommen.** Die sechs Spielerthreads sind als **Beiträge** bestätigt (Titel, Datum),
Kommentare nicht nachgelesen; alle sind **Einzelstimmen** (je ein unabhängiger Thread). Inhalte der Antworten stehen nur als „Suchauszug der Zuarbeit, nicht geprüft“. Die 113 Rohgruppen sind unbewertet.

| Spiel | Gegenstand | Gut (warum) | Nicht so gut (warum) | Für wen | Belege | Spielerstimmen | Entwickler / Fach |
|---|---|---|---|---|---|---|---|
| Destiny 2 | Waffenkarte (Menü) und Stat-Balken | Kadenz und Magazin als Zahl, die fünf Stats als Balken: ein Blick genügt für Vergleiche (Einschätzung). | Die Balken zeigen ausgerüstete Werte ohne Einheit; Basis (Manifest) und Menü liegen bis zu 25 Punkte auseinander, Handling-Sekunden stehen nirgends ([2.2](#w-menue-basis)). | Einsteiger lesen Balken, Designer brauchen die Kennlinien (Modell 2025). | [M] Balken, [S] RPM/Magazin: `QxSa4m3wIEA`, `DFn14wAPluA` bei 1,000 s | C1 (11.03.2025, allgemeiner PvP-Tuning-Ausblick) und C2 (12.01.2024, Frage nach Hand-Cannon-Rolls: Reichweite gegen Stabilität): **Einzelstimmen**, nicht als „wiederkehrend“ gewertet; nur Titel, Datum und Thema bestätigt. | [B1] Zoom und Schadensabfall seit Season 22 getrennt |
| Valorant | Waffenkarte im Kaufmenü; Vandal gegen Phantom | Kadenz, Magazin und Schaden je Zone schon in der Beta nebeneinander ([2.1](#w-karten)); die Kopf-Schwelle gegen 150 HP ist je Band klar ablesbar (Vandal 160 Kopf). | Die Schwelle hängt am Entfernungsband (Phantom > 20 m, Sheriff > 30 m): „1 Schuss“ gilt nur nah; 0 s ideale TTK ersetzt weder ADS noch Reaktion (Operator). | Kompetitive PvP-Spieler mit Kaufentscheidung; Einsteiger bei der Schwellenfrage. | [S] API-Bänder 25.10.2026; [O] Karte `WH5xpA7tfY8` 60 s | C5 (04.12.2024, „Vandal or phantom?“): Einzelstimme; der Titel stellt genau diese Wahl; Inhalt der Antworten nicht gelesen (Suchauszug der Zuarbeit, nicht geprüft: Einzeltreffer gegen Spray und Distanz). | [B5] Riot Patch 9.10: Phantom von drei auf zwei Schadensbereiche, weil Kopftreffer weniger Schaden machten als erwartet |
| Halo Infinite | Bandit Evo (Präzisions-Einzelschuss) | Klare Trefferzahl (5 Kopf- oder 7 Körpertreffer) und 1,6×-Optik begründen die Rolle als kontrollierte Startwaffe; 2024 wurde die Reaktionszeit ausdrücklich als Ziel genannt. | Kadenzsenkung 2,9 → 2,715 verlängert die ideale TTK bei gleicher Trefferzahl von 1,38 auf 1,47 s: weniger Schaden pro Sekunde als Preis für mehr Reaktionszeit (Rechnung, Trefferzahl 2024 angenommen). | Kompetitives PvP, längere Duelle. | [B2/B3/B4] plus Rechnung | C3 (08./09.03.2023): betrifft die ursprüngliche Bandit **vor** Evo, nur Kontext; keine Evo-Meinung. | [B4] Fleetcom 30.07.2024: Absicht „mehr Zeit zu reagieren“ (Wayback) |
| Apex Legends | R-301 (Magazin, Nachladezustände) | Getrennte Werte für taktisch und leer (2,4 / 3,2 s) belohnen rechtzeitiges Nachladen (Einschätzung). | 14 nötige Körpertreffer verbrauchen zwei Drittel des Magazins; die ideale 0,96 s sagt nichts über Verfehlen und Bewegung. | PvP-Spieler mit Wunsch nach kontrollierbarer Dauerfeuerwaffe. | [S] ttkdb.com, Basis 16.09.2026 | C4 (23.07.2025, Waffenwahl der Saison): ein Thread, Inhalt der Antworten nicht gelesen (Suchauszug der Zuarbeit, nicht geprüft: Kontrolle gegen Schaden); vor der Zahlenbasis 2026, keine Aussage zur aktuellen Balance. | [B6] Takeover 10.02.2025: Schaden 13 → 14 (historisch) |
| Call of Duty: Warzone | XM4 (Warzone, 300 HP) | Trefferzahl, Gesundheitsmodell und Entfernungsstufen stehen in der Quelle; dadurch ist die Rechnung nachvollziehbar. | Von 10 auf 15 Körpertreffer steigt die ideale TTK um 56 % (0,675 → 1,05 s) – die Fernstufe ist deutlich unfreundlicher. Spielerkritik 2025 (Suchauszug der Zuarbeit, nicht geprüft) betraf einen älteren Aufsatzstand. | Warzone-PvP; keine Übertragung auf BO6-Multiplayer. | [S] allmeta.gg 19.10.2026 | C6 (27./28.01.2025, Reaktionen auf die Patchnotes Season 2): ein Thread, Inhalt der Antworten nicht gelesen (Suchauszug der Zuarbeit, nicht geprüft: Kontrolle, Reichweite, Magazin). | [B7] BO6 Preseason: XM4-Schadensstufen (Sammelstand 08.11.2024) |

**Spielerstimme Nexxoss Gaming [C] (0.37 „Verdict“, Einzelstimme aus Auto-Untertiteln, nie gegen eine [M]-Messung; Abgleich je Klasse in [destiny2 › Verdict](destiny2.md#s-verdict)):** „Für wen“ entscheidet der Sprecher je Waffe nach PvE/PvP, nicht nach Stat-Zahlen: die Automatik sei in PvP und PvE gut spielbar ([MpYNiAGiyOI](https://www.youtube.com/watch?v=MpYNiAGiyOI) [00:34]), Impuls im PvP sehr stark ([89v3B8Vpkvk](https://www.youtube.com/watch?v=89v3B8Vpkvk) [00:18]), Scharfschütze und Bogen keine PvE- bzw. PvP-Waffe ([53v8UnJ9xDY](https://www.youtube.com/watch?v=53v8UnJ9xDY) [04:04], [lR6e42dNZxw](https://www.youtube.com/watch?v=lR6e42dNZxw) [03:59]), Granatwerfer Durchschnitt ([2lpjbjC4878](https://www.youtube.com/watch?v=2lpjbjC4878) [02:57]). Magazin- und Kadenzangaben (Automatik 50 statt 43 Schuss, Scout 13, Scharfschütze 3, MG 120) sind Jahr-1- bzw. Forsaken-Stand und nicht gegen das Manifest geprüft. Bestätigt: die relativ geringe Feuerrate der Handfeuerwaffe ([GgcO_mG25i4](https://www.youtube.com/watch?v=GgcO_mG25i4) [02:10]) – Annual Skate und Rose 140/min im Manifest.

### E2 – Lehren für BASIC und Cube Escape (Vorschlag, dort entscheiden)

- **übernehmen:** eine Waffenkarte nennt Roll, Datum, Modus und ob die Werte Basis oder ausgerüstet sind (Destiny-Menü gegen Manifest: 1–25 Punkte Unterschied).
- **übernehmen:** Trefferschwelle und Reaktionsfenster zusammen einstellen und im selben Test beurteilen (Halo Evo 2023/2024).
- **testen:** Entfernungsbänder auf überraschende Kopf-Schwellen prüfen (Phantom > 20 m, Sheriff > 30 m) und im UI verständlich machen.
- **testen:** taktisch und leer getrennt bewerten; Magazin, Kontrolle und Reichweite einer Dauerfeuerwaffe gemeinsam begrenzen (Apex R-301, Warzone XM4) und den Trefferpfad mit realer Trefferrate neben der idealen TTK probieren.
- **vermeiden:** aus einem Rahmennamen ein fertiges Zahlenpaket ableiten; eine ideale TTK von 0 s als sofortige Reaktion lesen (Operator); Stat-Zahlen als Einheiten behandeln.

## 6. Für Cube Escape

**Vorschlag (dort entscheiden):** Cube Escape könnte eigene Waffenkarten mit denselben Angaben (Roll, Stand, Basis/ausgerüstet) führen und Schwellen je Entfernung bewusst wählen; dieses Doc liefert Beispiele für Struktur und Fallstricke, **keine Startwerte**. Quellen mit anderem Spiel, Zeitstand oder Modus nicht mischen.
Übergabe an das abnehmende Repo per Briefkasten, nicht hier.

## 7. Offen und nicht messbar

- **Aktuelle Destiny-Schäden** je PvE/PvP: im Manifest nicht belegt; die Modelldaten sind von 2025 und veraltet (13 von 48 Kadenzen weichen ab).
- **Aktuelle Ziehen-/Wegstecken-/ADS-/Nachladezeiten** und Falloff-Meter: aus Stats allein nicht ableitbar; Handling-Sekunden der Menükarten nicht gemessen.
- **Wirkung des Aim-Assist-Stats:** weder Prozent noch allgemeiner Kegel (0.28: nur ein historisches Hand-Cannon-Beispiel von 2021 nennt 2,5° bis 3°); Quellenaussagen in [zielhilfe.md](zielhilfe.md).
- **30 nicht zugeordnete Destiny-Gruppen** und Projektil-, Pellet- und Sonderwaffen: kein Modell, Schadensfelder `null`.
- **Gesamtzeit bis zur Tötung** (Eingabe, Ziehen, ADS, Flug, Zielerfassung): nicht gerechnet; die Zustände überlagern sich.
- **Halo 2026:** nur historische Stände 2023/2024; die TTK 2024 nimmt gleiche Trefferzahlen wie 2023 an. **Apex Kopf, CoD Schaden und Kopffaktor:** `null` wegen Quellkonflikten. Destiny 1, Marathon: keine Zahlen.
- **Spielerstimmen:** Kommentarverläufe aller sechs Threads nicht gelesen; Zustimmungszahlen und Gegenstimmen nicht übernommen. **Quellen nicht erneut aufgerufen:** Manifest und Oracle-Quelltext live (Prüfung gegen die Kopie der Zuarbeit); B2-Datum (13.10.2023) steht auf der Seite nur als „vor 3 Jahren“, B1-Datum aus Season 22 abgeleitet.
- **Ghost-Magazin 15 (Beta) gegen 13 (API 2026):** Ursache nicht geprüft; die Valorant-API trägt kein Versionsdatum.
- **Nicht wieder versuchen:** Rangliste über Spiele hinweg; Menü-Balken in Sekunden umrechnen; Modell 2025 mit Stats 2026 mischen; aus Rohgruppen „Rahmen-Mittelwerte“ bilden.

## 8. Prüfung und Zählung

- **Zuarbeit:** 125 Einträge (113 Rohgruppen, 12 bewertete Beispiele; 2 Destiny-Menükarten [M]/[S], 1 Valorant-Karte [O]/[S], 9 Text-/API-Beispiele), 5 Spiele, 3 Videos, 23 Quellen (7 Daten, 7 Entwickler, 6 Spieler, 3 Videos).
  **Übernommen 122, korrigiert 3** (Valorant Guardian: unbelegte Deutung „Fehlertoleranz 0,19 s“ gestrichen; Halo 2023 und 2024: Status **B + Rechnung** statt B), **verworfen 0 Einträge**. Verworfen als Aussagen: die je Eintrag kopierten Bewertungsfelder, „wiederkehrend in zwei Quellen“ (C1/C2),
  „alle Threads vollständig geöffnet“, die in der JSON-Fassung der Zuarbeit zusätzlich vorhandenen, im Bericht und Quellenregister fehlenden Threads C7–C9 (ihr Inhalt ist nicht belegt). Von den 12 Beispielen sind **7 neu, 4 ergänzen Bestandszeilen, 1 (Apex) trennt Zeitstände**; neu sind außerdem 113 Gruppen und das Modell 2025.
- **Quellen:** 3 von 3 Videos per yt-dlp bestätigt; Zeitstempel 3 von 3 innerhalb der Länge; Webquellen 10 von 14 aufgerufen und bestätigt, 0 widerlegt, 4 nicht aufgerufen (Manifest, Oracle ×3: Quelltext und Formeldatei nicht live geladen, Inhalt gegen die Kopie der Zuarbeit geprüft; nur die Commit-Historie der Formeldatei per GitHub-API abgefragt); B1 und B4 nur per Wayback; Reddit 6 von 6 als Beiträge bestätigt.
- **Zahlen:** Manifest 113 von 113 Gruppen identisch zur Kopie (Hash, Kadenz, Magazin, Stats; außer den acht bewusst genullten Werten, siehe 2.3); Modelltabelle 43 von 43 Zeilen und Vergleichstabelle 9 von 9 Zeilen nachgerechnet (0 Abweichungen > 0,01 s); Formel, Handling- und Reloadkennlinie an 8 Familien gegen den Quellcode (Kopie der Zuarbeit) bestätigt; Formeldatei zuletzt 07.05.2025 laut Commit-Historie (GitHub-API).
- **Bild:** Handling-Balken 2 Zahlen (36,9 und 29,6 %) von Prüfer und Koordinator je nachgemessen = **4 Nachmessungen an 2 Zahlen** (Zuarbeit 36/29 ±3 pp: bestätigt); Karten-Zahlen: **12 verschiedene** (720/57, 540/36 und acht Ghost-Zahlen), alle von Prüfer A gelesen, **10 vom Koordinator** (nicht 540/36); Prüfer B sah die beiden Menükarten ebenfalls.
  **Nicht am Bild nachgemessen:** alle Text-/API-Beispiele (keine Bilder), Manifestzahlen.
- **Bewertung:** Abschnitt E der Zuarbeit nur nach der Quellenprüfung übernommen und je Spiel neu geschrieben; „wiederkehrend“ steht nirgends.

Schlusszeile: 5 Spiele · 12 Beispiele + 113 Rohgruppen (122 übernommen, 3 korrigiert, 0 verworfen) · 3 Videos (3 von 3 bestätigt), 7 Daten- (3 von 7 aufgerufen und bestätigt, 4 gegen die Kopie geprüft), 7 Entwickler- (7 von 7 bestätigt) und 6 Spielerquellen (Reddit 6 von 6 als Beiträge) · 2 Einzelbilder gemessen (Bild 60 je Menükarte), 4 Nachmessungen an 2 Balkenzahlen, 12 Kartenzahlen gelesen (10 vom Koordinator).

## Anhang A: Manifest-Basiswerte (113 Gruppen)

Quelle: Bungie-Manifest (Build 245114.26.10.13.2000-1-bnet.66137, Abruf 25.10.2026) [S]; `R/H/L/S/Z/AA` = Range / Handling / Reload / Stability / Zoom / Aim Assist (Stat-Zahlen, keine Einheiten); `—` = unbekannt oder nicht anwendbar.
„Modell 2025“ = es gibt eine historische Formelzuordnung ([2.4](#w-modell-2025)). Item- und Intrinsic-Hash je Gruppe in `data/waffenwerte.json`.

| ID | Typ · Munition | Rahmen | Beispielwaffe | RPM | Mag. | R/H/L/S/Z/AA | Modell 2025 |
|---|---|---|---|---:|---:|---|---|
| D2-001 | Auto Rifle · primary | Adaptive Frame | The Summoner | 600 | 41 | 40/70/56/41/16/62 | ja |
| D2-002 | Auto Rifle · primary | Balanced Heat Weapon | Zealous Ideal | 450 | — | 59/47/64/50/16/45 | nein |
| D2-003 | Auto Rifle · primary | High-Impact Frame | Age-Old Bond | 400 | 31 | 82/38/34/30/16/61 | ja |
| D2-004 | Auto Rifle · primary | Lightweight Frame | The Riposte | 720 | 52 | 34/50/51/52/17/76 | ja |
| D2-005 | Auto Rifle · primary | Precision Frame | Ammit AR2 | 450 | 33 | 61/46/38/45/15/44 | ja |
| D2-006 | Auto Rifle · primary | Rapid-Fire Frame | Chroma Rush | 720 | 51 | 25/35/47/56/16/80 | ja |
| D2-007 | Auto Rifle · primary | Support Frame | Chrysura Melo | 600 | 47 | 45/65/57/44/16/63 | nein |
| D2-008 | Auto Rifle · primary | Support Frame | Cusp Sempiternal | 600 | 47 | 45/73/68/50/16/74 | nein |
| D2-009 | Auto Rifle · primary | Support Frame | No Hesitation | 600 | 44 | 45/82/68/48/16/68 | ja |
| D2-010 | Auto Rifle · primary | Support Frame | DECATUR 02 | 600 | 44 | 42/63/60/45/16/62 | nein |
| D2-011 | Auto Rifle · primary | Support Frame | Adamantite | 600 | 44 | 39/70/66/49/16/64 | ja |
| D2-012 | Combat Bow · primary | High-Impact Longbow | Convened Recurve | — | — | —/39/30/34/18/43 | nein |
| D2-013 | Combat Bow · primary | Lightweight Frame | Whispering Slab | — | — | —/65/60/53/18/75 | ja |
| D2-014 | Combat Bow · primary | Precision Frame | Raconteur | — | — | —/56/40/48/18/64 | ja |
| D2-015 | Combat Bow · heavy | High-Impact Frame | A Good Shout | — | — | —/37/59/—/19/82 | nein |
| D2-016 | Fusion Rifle · special | Adaptive Frame | VS Gravitic Arrest | — | 6 | 34/30/31/48/15/50 | ja |
| D2-017 | Fusion Rifle · special | Aggressive Frame | Coriolis Force | — | 6 | 33/26/34/37/15/45 | ja |
| D2-018 | Fusion Rifle · special | High-Impact Frame | The Wizened Rebuke | — | 5 | 51/22/20/28/15/62 | ja |
| D2-019 | Fusion Rifle · special | Precision Frame | Main Ingredient | — | 5 | 59/31/24/35/15/45 | ja |
| D2-020 | Fusion Rifle · special | Rapid-Fire Frame | Cartesian Coordinate | — | 7 | 21/50/46/26/15/60 | ja |
| D2-021 | Glaive · special | Adaptive Glaive | The Enigma | 55 | 6 | 55/35/40/—/—/61 | ja |
| D2-022 | Glaive · special | Aggressive Glaive | The Heron | 45 | 5 | 61/46/27/—/—/76 | ja |
| D2-023 | Glaive · special | Rapid-Fire Glaive | Backfang | 80 | 6 | 43/71/70/—/—/61 | ja |
| D2-024 | Grenade Launcher · special | Area Denial Frame | Lost Signal | 72 | 1 | —/66/65/21/13/69 | nein |
| D2-025 | Grenade Launcher · special | Double Fire | Wilderflight | 100 | 1 | —/43/32/20/13/67 | ja |
| D2-026 | Grenade Launcher · special | Lightweight Frame | The Militia's Birthright | 90 | 1 | —/69/63/23/13/75 | ja |
| D2-027 | Grenade Launcher · special | Micro-Missile Frame | The Mountaintop | 90 | 1 | —/69/63/23/13/75 | ja |
| D2-028 | Grenade Launcher · special | Wave Frame | Forbearance | 72 | 1 | —/70/71/27/13/79 | ja |
| D2-029 | Grenade Launcher · heavy | Adaptive Frame | Play of the Game | 120 | 6 | —/33/46/35/13/65 | ja |
| D2-030 | Grenade Launcher · heavy | Compressed Wave Frame | Hullabaloo | 120 | 5 | —/41/39/38/13/61 | ja |
| D2-031 | Grenade Launcher · heavy | Precision Frame | Bushwhacker | 100 | 6 | —/66/54/58/13/61 | ja |
| D2-032 | Grenade Launcher · heavy | Rapid-Fire Frame | Terran Wind | 150 | 4 | —/26/25/25/13/30 | ja |
| D2-033 | Hand Cannon · primary | Adaptive Frame | Annual Skate | 140 | 10 | 40/47/38/49/14/75 | ja |
| D2-034 | Hand Cannon · primary | Adaptive Frame | Rose | 140 | 11 | 38/68/55/40/14/85 | ja |
| D2-035 | Hand Cannon · primary | Aggressive Frame | Igneous Hammer | 120 | 8 | 65/34/30/32/14/66 | ja |
| D2-036 | Hand Cannon · primary | Dynamic Heat Weapon | Modified B-7 Pistol | 180 | — | 32/35/70/59/14/70 | nein |
| D2-037 | Hand Cannon · primary | Heavy Burst | Warden's Law | 257 | 16 | 56/24/27/29/14/68 | ja |
| D2-038 | Hand Cannon · primary | Lightweight Frame | Rose | 140 | 11 | 43/60/55/45/14/85 | ja |
| D2-039 | Hand Cannon · primary | Precision Frame | Service Revolver | 180 | 12 | 32/31/30/52/14/67 | ja |
| D2-040 | Hand Cannon · primary | Spread Shot | Sarpedon-D | 100 | 8 | 31/25/27/27/12/63 | nein |
| D2-041 | Hand Cannon · special | Dynamic Heat Weapon | Uncivil Discourse | 180 | — | 75/79/80/77/20/63 | nein |
| D2-042 | Linear Fusion Rifle · heavy | Adaptive Burst | Stormchaser | — | 5 | 37/30/25/52/25/62 | ja |
| D2-043 | Linear Fusion Rifle · heavy | Precision Frame | Taipan-4fr | — | 5 | 48/36/29/43/25/64 | ja |
| D2-044 | Machine Gun · heavy | Adaptive Frame | Commemoration | 450 | 57 | 58/57/55/55/16/64 | ja |
| D2-045 | Machine Gun · heavy | Aggressive Frame | Pro Memoria | 600 | 64 | 45/45/47/50/17/46 | ja |
| D2-046 | Machine Gun · heavy | Balanced Heat Weapon | Bitter End | 900 | — | 33/23/59/83/16/51 | nein |
| D2-047 | Machine Gun · heavy | High-Impact Frame | THE SWARM | 360 | 47 | 69/35/38/33/16/39 | ja |
| D2-048 | Machine Gun · heavy | Rapid-Fire Frame | Eleatic Principle | 900 | 75 | 26/50/64/34/16/67 | ja |
| D2-049 | Pulse Rifle · primary | Adaptive Frame | Jorum's Claw | 390 | 38 | 49/44/43/50/17/60 | ja |
| D2-050 | Pulse Rifle · primary | Aggressive Burst | Insidious | 450 | 36 | 74/27/34/60/18/44 | ja |
| D2-051 | Pulse Rifle · primary | Balanced Heat Weapon | High Tyrant | 540 | — | 37/23/42/49/17/79 | nein |
| D2-052 | Pulse Rifle · primary | Dynamic Heat Weapon | All or Nothing | 540 | — | 33/22/55/41/17/77 | nein |
| D2-053 | Pulse Rifle · primary | Heavy Burst | Joxer's Longsword | 324 | 18 | 74/36/33/33/18/43 | ja |
| D2-054 | Pulse Rifle · primary | High-Impact Frame | The Messenger | 340 | 31 | 66/31/38/54/18/37 | ja |
| D2-055 | Pulse Rifle · primary | Legacy PR-55 Frame | BxR-55 Battler | 450 | 35 | 50/71/63/59/20/85 | ja |
| D2-056 | Pulse Rifle · primary | Lightweight Frame | The Martlet | 450 | 33 | 37/68/61/54/17/69 | ja |
| D2-057 | Pulse Rifle · primary | Rapid-Fire Frame | Gridskipper | 540 | 35 | 33/27/35/47/18/80 | ja |
| D2-058 | Pulse Rifle · special | Micro-Missile Frame | Mint Retrograde | 200 | 5 | —/20/25/42/20/74 | nein |
| D2-059 | Rocket Launcher · heavy | Adaptive Frame | Apex Predator | 20 | 1 | —/44/44/43/20/68 | ja |
| D2-060 | Rocket Launcher · heavy | Aggressive Frame | Curtain Call | 25 | 1 | —/18/60/23/20/27 | ja |
| D2-061 | Rocket Launcher · heavy | High-Impact Frame | Roar of the Bear | 15 | 1 | —/65/34/57/20/71 | ja |
| D2-062 | Rocket Launcher · heavy | Precision Frame | Micromort | 15 | 1 | —/43/34/42/20/61 | ja |
| D2-063 | Rocket Launcher · heavy | Precision Frame | Subzero Salvo | 15 | 1 | —/41/23/39/20/61 | ja |
| D2-064 | Scout Rifle · primary | Aggressive Frame | Long Arm | 120 | 14 | 55/53/45/25/18/52 | ja |
| D2-065 | Scout Rifle · primary | Balanced Heat Weapon | Voltaic Shade | 260 | — | 35/31/57/47/20/70 | nein |
| D2-066 | Scout Rifle · primary | High-Impact Frame | Frontier Justice | 150 | 13 | 72/24/31/18/21/35 | ja |
| D2-067 | Scout Rifle · primary | Lightweight Frame | Vouchsafe | 200 | 15 | 33/63/55/32/20/73 | ja |
| D2-068 | Scout Rifle · primary | Precision Frame | Hung Jury SR4 | 180 | 16 | 49/50/46/55/22/67 | ja |
| D2-069 | Scout Rifle · primary | Rapid-Fire Frame | Black Scorpion-4sr | 260 | 18 | 20/27/28/49/20/56 | ja |
| D2-070 | Scout Rifle · primary | Rapid-Fire Frame | Trustee | 260 | 17 | 35/30/31/43/19/67 | ja |
| D2-071 | Shotgun · special | Aggressive Frame | Baligant | 55 | 5 | 20/22/30/21/12/28 | ja |
| D2-072 | Shotgun · special | Aggressive Frame | Imperial Decree | 55 | 4 | 29/31/34/29/12/35 | ja |
| D2-073 | Shotgun · special | Heavy Burst | Arcane Embrace | 62 | 12 | 62/63/69/39/12/40 | ja |
| D2-074 | Shotgun · special | Lightweight Frame | Riiswalker | 80 | 6 | 45/71/62/43/12/52 | ja |
| D2-075 | Shotgun · special | MIDA Synergy | MIDA Macro-Tool | 65 | 5 | 59/36/42/42/12/71 | nein |
| D2-076 | Shotgun · special | Pinpoint Slug Frame | First In, Last Out | 65 | 6 | 58/60/45/40/12/27 | ja |
| D2-077 | Shotgun · special | Precision Frame | Fractethyst | 65 | 5 | 62/41/50/45/12/72 | ja |
| D2-078 | Shotgun · special | Precision Frame | Compass Rose | 65 | 5 | 62/35/48/41/12/73 | ja |
| D2-079 | Shotgun · special | Rapid Fire Slug | Trachinus | 87 | 7 | 40/40/67/50/12/72 | nein |
| D2-080 | Shotgun · special | Rapid-Fire Frame | IKELOS_SG_v1.0.3 | 140 | 7 | 34/44/61/32/12/72 | ja |
| D2-081 | Shotgun · special | Shot Package | Felwinter's Lie | 55 | 4 | 25/34/34/25/12/33 | ja |
| D2-082 | Sidearm · primary | Adaptive Burst | Senuna SI6 | 491 | 30 | 30/49/29/82/12/67 | ja |
| D2-083 | Sidearm · primary | Adaptive Burst | Peacebond | 491 | 30 | 33/50/29/79/12/69 | ja |
| D2-084 | Sidearm · primary | Adaptive Frame | Controlling Vision | 300 | 16 | 30/48/33/60/12/75 | ja |
| D2-085 | Sidearm · primary | Dynamic Heat Weapon | Compact Defender | 360 | — | 22/65/51/47/12/69 | nein |
| D2-086 | Sidearm · primary | Heavy Burst | Brass Attacks | 325 | 24 | 41/36/27/38/13/89 | ja |
| D2-087 | Sidearm · primary | Lightweight Frame | Eleventh Hour | 360 | 14 | 22/63/55/37/12/67 | ja |
| D2-088 | Sidearm · primary | Precision Frame | Insurmountable | 260 | 12 | 50/38/21/43/12/86 | ja |
| D2-089 | Sidearm · primary | Rapid-Fire Frame | The Fool's Remedy | 450 | 16 | 27/59/38/60/12/58 | ja |
| D2-090 | Sidearm · primary | Together Forever | Drang (Baroque) | 300 | 18 | 35/71/30/60/13/70 | ja |
| D2-091 | Sidearm · special | Micro-Missile Frame | Indebted Kindness | 100 | 9 | —/45/28/48/18/80 | ja |
| D2-092 | Sidearm · special | Together Forever | Unfall | 100 | 9 | —/41/38/36/18/67 | nein |
| D2-093 | Sniper Rifle · special | Adaptive Frame | Beloved | 90 | 4 | 50/47/38/46/40/68 | ja |
| D2-094 | Sniper Rifle · special | Aggressive Frame | Succession | 72 | 3 | 76/30/35/23/50/48 | ja |
| D2-095 | Sniper Rifle · special | Dynamic Heat Weapon | Conspiracy Honed | 140 | — | 37/70/77/36/40/78 | nein |
| D2-096 | Sniper Rifle · special | High-Impact Frame | The Helmsman | 72 | 8 | 59/41/19/27/25/59 | nein |
| D2-097 | Sniper Rifle · special | Rapid-Fire Frame | Omniscient Eye | 140 | 6 | 37/70/57/36/40/72 | ja |
| D2-098 | Sniper Rifle · heavy | Disruption Weapon [Shield-Piercing] | Refurbished A499 | 72 | 1 | 71/25/11/27/22/14 | nein |
| D2-099 | Submachine Gun · primary | Adaptive Frame | Qua Nilus II | 900 | 37 | 43/55/54/54/14/47 | ja |
| D2-100 | Submachine Gun · primary | Aggressive Burst | Whatchamacallit | 600 | 56 | 42/46/24/31/15/29 | nein |
| D2-101 | Submachine Gun · primary | Aggressive Frame | The Title | 720 | 32 | 40/48/23/20/15/32 | ja |
| D2-102 | Submachine Gun · primary | Aggressive Frame | The Immortal | 720 | 32 | 40/58/30/25/14/39 | ja |
| D2-103 | Submachine Gun · primary | Balanced Heat Weapon | Vikala SMG4 | 900 | — | 16/73/33/31/13/53 | nein |
| D2-104 | Submachine Gun · primary | Lightweight Frame | Gunburn | 900 | 38 | 25/66/28/37/14/53 | ja |
| D2-105 | Submachine Gun · primary | MIDA Synergy | CALUS Mini-Tool | 900 | 42 | 30/65/31/49/13/49 | ja |
| D2-106 | Submachine Gun · primary | Precision Frame | Unending Tempest | 600 | 30 | 53/23/19/41/14/58 | ja |
| D2-107 | Sword · heavy | Adaptive Frame | Double-Edged Answer | — | — | 60/—/—/—/0/— | nein |
| D2-108 | Sword · heavy | Aggressive Frame | Crown-Splitter | — | — | 60/—/—/—/0/— | nein |
| D2-109 | Sword · heavy | Caster Frame | Temptation's Hook | — | — | 40/—/—/0/0/— | nein |
| D2-110 | Sword · heavy | Lightweight Frame | Quickfang | — | — | 20/—/—/—/0/— | nein |
| D2-111 | Sword · heavy | Vortex Frame | Falling Guillotine | — | — | 40/—/—/0/0/— | nein |
| D2-112 | Sword · heavy | Wave Sword Frame | Abyssal Edge | — | — | —/—/—/0/0/— | nein |
| D2-113 | Trace Rifle · special | Adaptive Frame | Retraced Path | 1000 | 94 | 64/46/45/75/16/100 | ja |
