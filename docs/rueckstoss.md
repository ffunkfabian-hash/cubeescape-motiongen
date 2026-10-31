# Rückstoßmuster in Videospielen – Bahn, Takt, Rücklauf und Streuung

Referenzanalyse REF 0.16 „Kickback“ (25.10.2026) für die Waffenreihe **BASIC** (Projekt `cubeescape-ballon`). Nur Videospiele.
Hier stehen Beobachtungen und Messwerte. Der Abschnitt [Gestaltungsregeln für BASIC](#6-gestaltungsregeln-für-basic-vorschlag)
ist ein **Vorschlag**; entschieden wird in BASIC. Maschinenlesbare Fassung: [`data/rueckstoss.json`](../data/rueckstoss.json).
Getrennte Themen: Visiere in [visiere.md](visiere.md) (REF 0.14), Waffenproportionen in [proportionen.md](proportionen.md) (REF 0.15), Einzelschuss-Kick und Bloom einzelner Destiny-Waffen in
[destiny2.md](destiny2.md#2-messungen-an-60-fps-aufnahmen-ab-16-oktober-2026--m).

**Stand: nicht fertig im strengen Kontrollmessziel.** Bis auf Bungies eigenen Test (Abyss Defiant) ist bei keiner Aufnahme belegt, dass der
Spieler nicht gegensteuert. Alle übrigen Bahnen sind **Nettobahnen** (Rückstoß plus unbekannte Eingabe). Zufallsanteil,
Erstschuss-Streuung und isolierte Rückführzeit sind nirgends gemessen. Diese Lücken betreffen die Gültigkeit der Größen, nicht ihre
Nachkommastellen.

**Status:** **[M]** gemessen am Bild; **[M-Netto]** gemessene Weltankerbewegung bei unbekannter Eingabe; **[S]** Entwickler- oder
Sekundärquelle (Patchnotes, Datenbank); **[C]** Community-Test; **[O]** Sichtung ohne belastbare Zahl. Lage in Prozent der Bildbreite
**B** bzw. Bildhöhe **H**, Ursprung oben links, x nach rechts, y nach unten; **negatives dy = Blick wandert nach oben**. ±3 Prozentpunkte
(pp). Zeiten nur aus 60/s-Aufnahmen, Schussmarker ±1 Bild, Abstände ±2 Bilder. **Jede Zahl ist das Beispiel einer Waffe mit
unbekanntem FOV, Zoom und Ausbau**, kein Klassenmittel; Prozentwerte verschiedener Spiele und Optiken sind keine Rangliste.

## 1. Quellen und Methode

**Umfang:** 9 Spiele, 36 Waffen, 44 Serienfenster (35 gemessene oder gesichtete Fenster plus 9 qualitative MW2019-Wandserien), rund
6 400 bearbeitete Quellbilder. Gemessen hat eine Codex-Sitzung (24.10.2026, Arbeitsdaten im Cache
`~/Library/Caches/CubeEscape/reference/visiere/codex3/`, nicht im Repo); diese Sitzung hat die Quellen geprüft, Stichproben
nachgemessen, einen Wert korrigiert und die Ergebnisse eingepflegt.

**Messung:** Ein fester Weltausschnitt (Wand, Gebäudekante, Fels, kein Waffenmodell, kein HUD) wird per normierter Kreuzkorrelation
(`cv2.matchTemplate`, gültig ab corr ≥ 0,85) Bild für Bild gesucht; seine negierte Verschiebung ist die Bewegung der Bildmitte
(= Zielpunkt) gegen die Welt. Zwei räumlich getrennte Anker prüfen Mehrdeutigkeiten. Schusszeitpunkte kommen aus dem
Mündungsblitz (Destiny-Showcases) oder dem Munitionszähler (Battlefield 6, Halo, Titanfall, Apex). Die große Drehung bei Abyss Defiant
ist zusätzlich per Homographie (SIFT/RANSAC) gegengeprüft. **Nicht** gemessen: Winkel in Grad (FOV unbekannt), Kadenz aus
Lehrvideos mit Standbildern (Apex), Zeiten aus 24/30-/s-Dateien.

**Prüfung dieser Sitzung (25.10.2026):**

1. **Quellen:** alle 19 YouTube-Videos per yt-dlp gegen Kanal, Hochladedatum und Titel geprüft – alle stimmen
   (Liste in `data/rueckstoss.json` › `sources`). Zwei Primärtexte nachgelesen: Bungie Update 9.1.0 (Entfernung des
   deterministischen Rückstoßes) und Valorant-Patch 11.08 (geschützte Kugeln). Die übrigen Text- und Datenbankquellen sind Codex-Zuarbeit.
2. **Nachmessung** mit eigenem Tracker, eigenen Ankern und Rasterbild (10 %-Raster, Mittenkreuz):

| Stichprobe | Codex | Nachmessung | Urteil |
|---|---|---|---|
| Chroma Rush, 12er-Stoß | 720/min, Vor-Schuss −12,0 pp H, Spitze 12,8, seitlich 2,2, Band nach 24 Bildern | 12 Blitze im Abstand 5 Bilder, −12,3 / Spitze −13,2 / 2,1 / 24 Bilder | bestätigt |
| Threaded Needle, Rest vor Schuss 2/3/4 | 6,7 / 13,1 / 19,6 pp H | 6,6 / 13,2 / 19,6 (zwei Anker gleich) | bestätigt |
| BF6 B36A4, 18 Schüsse | −6,1 pp H, seitlich ≤ 1,8 | HUD 19 → 1 in 21,08–22,52 s, −5,6 pp H, seitlich ≤ 1,4 | bestätigt |
| Abyss Defiant, Zählung | 36 → 0 in 2,467–8,333 s | HUD 36 (2,40) · 35 (2,50) · 0 (8,30) | bestätigt (Amplitude nicht nachgemessen) |
| Titanfall 2 Hemlok | Ende −4,4 pp H | −4,4 … −5,4 (drei Anker) | bestätigt |
| **Titanfall 2 R-201** | dy bis −18,9, Ende −16,7 pp H | **Spitze ≈ −9, Ende ≈ −3 pp H** (Fels- und Turmanker) | **korrigiert**: Codex-Turmanker springt ab 174,9 s auf einen falschen Turmabschnitt |

**Systemfassungen:** Rückstoß ist eine Eigenschaft eines Spielstands, nicht eines Spiels.

| Spiel | Fassung | Aussage | Quelle |
|---|---|---|---|
| Destiny 2 | bis Season 21 (Showcases 2020/21) | vor der Einführung teilweise fester Folgen; das System dieser Fassung ist hier nicht eigens belegt | Aufnahmen [M-Netto] |
| Destiny 2 | Season 22, 21.09.2023 | geeignete Waffen mit teilweise wiederholbarer Folge: gemeinsamer Anfang, möglicher Musterwechsel in der ersten Magazinhälfte, Treffer weiter zufällig abweichend; höhere Recoil Direction = weniger seitlich, ohne Formel | [Bungie TWID](https://www.bungie.net/7/en/News/article/twid_09_21_2023) [S] |
| Destiny 2 | Update 9.1.0, 09.09.2025 | deterministischer Rückstoß bei allen Waffen außer Vigilance Wing wieder entfernt | [Bungie 9.1.0](https://www.bungie.net/7/en/News/Article/destiny_update_9_1_0) [S, geprüft] |
| Destiny 2 | Community 2019 | „Endziffer 5 eher senkrecht, Zehnerwerte links/rechts, 100 Sonderfall“ – eigene Versuche, keine Entwicklerformel; hier weder bestätigt noch widerlegt | [Reddit, Crystic](https://www.reddit.com/r/DestinyTheGame/comments/ae6r61/how_the_recoil_direction_stat_works_xpost_from/) [C] |
| Valorant | 2020 | **hybrid**: deterministischer Anfang, spätere Abweichung pseudozufällig, Geschossungenauigkeit getrennt – ein durchgehend festes Spray ist falsch | [Riot-Entwickler](https://old.reddit.com/r/VALORANT/comments/g7ft19/why_is_there_rifle_first_shot_deviation_and_rng/foj1bb5/) [S] |
| Valorant | Patch 11.08 | PC: Phantom 8 geschützte Kugeln, Seitenwechsel 0,6 s, Chance 10 %; Vandal 6 / 0,6 s / 10 %; Spectre 5 / 0,28 s – gilt nicht für die Aufnahmen von 2020 | [Patchnotes](https://playvalorant.com/en-gb/news/game-updates/valorant-patch-notes-11-08/) [S, geprüft] |
| Apex Legends | 2020 | handabgestimmte Punkte mit kleiner Varianz, die die Bahn verformt statt sie zu ersetzen | [Archiv Respawn](https://devtrackers.gg/apex-legends/p/028b5aa2-s4-updated-recoil-control-patterns-rotated) [S] |
| CS2 | 2026 | feste Grundbahn je Waffe, Trefferstreuung getrennt (Test mit abgeschalteter Streuung) | [Imbaboost](https://imbaboost.com/tools/cs2-recoil-patterns) [C] |
| CoD MW2019 | 2019 | erlernbare waffenspezifische Muster, Gegeneingabe beim Rücklauf berücksichtigt | [Activision](https://blog.activision.com/ja/call-of-duty/2019-08/Modern-Warfare-Multiplayer-First-Look-New-Gameplay-Mechanics) [S] |
| Battlefield 2042 | Update 2.1.1 | getrennte Multiplikatoren für Basisrückstoß und ersten Schuss (M16A3 0,44 → 0,36 bzw. 1,45 → 1,15) | [EA](https://www.ea.com/en-gb/games/battlefield/battlefield-2042/news/battlefield-2042-update-notes-2-1-1) [S] |
| Battlefield 6 | Update 1.0.1.0, 09.10.2025 | Rückstoß gegenüber der Vorveröffentlichung geändert – die Torbis-Aufnahme liegt davor | [EA](https://www.ea.com/games/battlefield/battlefield-6/news/battlefield-6-update-notes-1-0-1-0) [S] |
| CoD BO6 | 2024 | Gun Kick und Centering Speed als getrennte Werte | [Activision](https://www.callofduty.com/guides/blackops6/pre-game/call-of-duty-guides-black-ops-6-multiplayer-pre-game-weapons-and-loadouts) [S] |

**Quellen der Messungen** (Kanal, YouTube-ID, Hochladedatum, Bildrate der ausgewerteten Datei):

| Spiel | Waffen | Quelle | Bildrate | Eingabe |
|---|---|---|---|---|
| Destiny 2 | Chroma Rush | Ultraclocked, `QxSa4m3wIEA`, 15.05.2021 | 60 | unbekannt |
| Destiny 2 | Abyss Defiant | Destiny 2 (Bungie), `rw_6lS0pBf0`, 11.09.2023 | 30 | **ohne Gegensteuern** laut Bungie |
| Destiny 2 | Gridskipper | Ultraclocked, `DFn14wAPluA`, 13.05.2021 | 60 | unbekannt |
| Destiny 2 | Swift Ride, Tone Patrol, Annual Skate, Dead Man Walking, Foggy Notion | Ultraclocked, `IG-GZ72Vbi0`, 14.02.2020 („SUROS Weapons“) | 60, Normaltempo | unbekannt |
| Destiny 2 | Extraordinary Rendition | Ultraclocked, `Y5OLr0nbgSg`, 15.02.2021 | 60 | unbekannt |
| Destiny 2 | Shattered Cipher | Ultraclocked, `DEM-8xg66R8`, 14.05.2021 | 60 | unbekannt |
| Destiny 2 | Threaded Needle | Ultraclocked, `uoTaCBMXcFk`, 20.02.2021 | 60 | unbekannt |
| Destiny 2 | The Messenger (nur Sichtung) | Timothy Hsu, `mkwgPBa1fXI`, 27.04.2021 | 30 | unbekannt, Lauf gewechselt |
| CS2 | M4A1-S, M4A4, AK-47 | Moskri, `wSZA073GUw8`, 25.03.2023 | 60, Montage 1280 × 546 | unbekannt |
| Valorant | Phantom, Vandal, Spectre | SC Valorant Guides, `vaqlrCzy3PM`, 27.11.2020 | 30, Digitalzoom | Lehrvideo mit Kompensation |
| Apex Legends | R-301, Flatline, HAVOC | Do_ASAP, `8QQJAwUaRi0`, 28.01.2026 | 59,94, Standbilder im Feuer | unbekannt, 4x-Optik |
| Battlefield 6 | B36A4, AK4D, M433 | Torbis, `ROUP1z62caA`, 17.09.2025 | 60, Vorveröffentlichung | unbekannt |
| Battlefield 2042 | M5A3 / AK-24 / K30 | SammyBoiii: FPS, `enyEjb4dXU8` 17.02.2022 / `0Rq3rypcIQo` 21.03.2022 / `L6BiTz_3teo` 16.05.2022 | 60 / 30 / 30 | unbekannt |
| CoD MW2019 | Kilo 141, M4A1, AK-47 | Ghostjobs, `nBsmMfQfd_M`, 04.08.2020 | 24, Splitbild | unbekannt |
| Halo Infinite | MA40, BR75, Mk50 / VK78 | Abyssopelagic, `ZfNuA5r-470`, 30.07.2021 (Technical Preview) / AznSlickSlaya, `9TdIttKuOgE`, 04.10.2021 | 60 (Inhalt ≈ 30) / 60 | unbekannt |
| Titanfall 2 | C.A.R., R-201, Hemlok | Weapons From Games, `4sDwTD9U8bw`, 14.03.2019 | 60 | unbekannt |

Gesichtet und verworfen (freies Zielen, Optikmontagen, falsches Spiel oder gelöschtes Konto): Skovos `WH5xpA7tfY8`, AlexTheRed
`iNizXu2hl_0`, ClawZ `UetKaZiF9uA`, Skeptation `gCQHKNsIU9w`, Qwixzo `Xt591V15YKk`, DevDestini `q3JS3k_zjrY`, Hoodiewaffles
`qI_IWMuH_Zs`, Zagzogs `xygk-adR6pg`/`v0HWVURYPDM`, TheXclusiveAce `KOj-CAzkwTc`, gtnprn-Diagrammvideos, CWabbit `iARAFvWhDFg`
(Konto geschlossen), Kat `Ny7bw5dXwPo`; ein angebliches Halo-Infinite-Video war Halo 3.

## 2. Destiny 2 – Messungen

Recoil Direction (RD) laut Datenbank ist ein Basiswert ohne Beleg der Clipkonfiguration; im Clip belegt ist nur Abyss Defiant (RD 86,
Stabilität 25). Pfadwerte der Showcases: Bildmitte gegen Weltanker im Bild **vor** jedem Schuss, auf die erste Probe genullt; Abyss Defiant
und Battlefield 6 beziehen sich auf das Bild vor dem ersten Schuss und tasten am Munitionszähler ab (`path_basis` in den Daten).

| Vorgang | Quelle, Zeit | Messung | RD (Basis) |
|---|---|---|---|
| **Chroma Rush (Automatik): 12er-Hüftstoß** [M-Netto] <a id="r-d2-chroma"></a> | `QxSa4m3wIEA`, 5,55–7,20 s; Schüsse 5,667–6,583 | 12 Schüsse im Abstand 5 Bilder (720/min). Netto steigt gleichmäßig bis −12 pp H vor Schuss 12, Spitze −12,8 nach dem letzten; seitlich ≤ 2,2 pp B (unter Genauigkeit), leichte Rechts-dann-zurück-Biegung. Rücklauf ins ±3-pp-Band **24 Bilder** (0,40 s) nach dem letzten Schuss, Rest −0,6 pp H. Nachgemessen. | 45 |
| **Abyss Defiant (Automatik): drei Magazine ohne Gegensteuern** [M/S] <a id="r-d2-abyss"></a> | `rw_6lS0pBf0` (Bungie), 2,467–8,333 / 11,533–17,400 / 20,467–26,333 s | Je 36 → 0 (≈ 360/min). Lange aufwärts gerichtete Säule mit kleinen Links-/Rechtswechseln, **dreimal wiedererkennbar dieselbe Form**, kein enges festes S. Teilspitzen ≈ 58 / 63 / 60 pp H (projiziert, unterschiedlich weit gültig – keine Magazinstreuung). Seitlich ≤ 2,5 pp B. Fassung Season 22. | **86 im Clip** |
| **Gridskipper (Impuls): drei Dreiersalven** [M-Netto] <a id="r-d2-gridskipper"></a> | `DFn14wAPluA`, 29,70–32,30 s | In der Salve 4 Bilder Abstand (0,067 s), erste bis dritte Kugel 8 Bilder. Jede Salve steigt ≈ 4 pp H, zwischen den Salven baut sich das Netto weitgehend ab (Salvenanfänge 68 und 24 Bilder auseinander = Spielertakt). Spitze 5,7 pp H, Rücklauf ins Band 12 Bilder. | 55 |
| Swift Ride (Impuls) [O] | `IG-GZ72Vbi0`, 362,0–363,9 s | Drei Salven sichtbar, Anker widersprechen sich – Bahn verworfen. | 70 |
| **Tone Patrol (Scout, 180/min): fünf getaktete Schüsse** [M-Netto] <a id="r-d2-tone"></a> | `IG-GZ72Vbi0`, 388,50–391,40 s | Abstand 21/21/20/20 Bilder. Je Schuss Hochimpuls bis 5,7 pp H, **Rest vor dem Folgeschuss wächst** (−1,7 / −2,2 / −2,8 / −3,3 pp H). Seitlich 0,4 pp B. Rücklauf ins Band 23 Bilder. | 62 |
| **Annual Skate (Handfeuerwaffe, 140/min): fünf ADS-Schüsse** [M-Netto] <a id="r-d2-annual"></a> | `IG-GZ72Vbi0`, 83,50–87,50 s | Unregelmäßiger Takt (86/56/33/34 Bilder). Großer Hochimpuls je Schuss bis 7,6 pp H mit deutlichem Modellkippen, Netto-Rest vor dem nächsten Schuss nur 1,7 pp H – der Kick kommt im Bild fast ganz zurück (Eingabe unbekannt). | 88 |
| Dead Man Walking (Seitenwaffe) [M-Netto/O] | `IG-GZ72Vbi0`, 121,0–124,6 s | Weltanker bis 9,8 pp H, dann Rücklauf; Schusszahl ohne HUD nicht gesichert. | 98 |
| Foggy Notion (MP, 900/min) [M-Netto/O] | `IG-GZ72Vbi0`, 184,5–190,0 s | Hüftstöße, Spanne ≈ 9 pp H, seitlich unter 3 pp B; Fenster endet im Feuer. | 91 |
| Extraordinary Rendition (MP) [O] | `Y5OLr0nbgSg`, 43,20–44,55 s | Anker verlieren Güte – Bahn verworfen; Wandtreffer bilden einen schmalen Aufwärtsstreifen. | 97 |
| **Shattered Cipher (MG): Hüfte und ADS** [M-Netto] <a id="r-d2-cipher"></a> | `DEM-8xg66R8`, 7,00–8,70 und 30,30–36,90 s | Hüfte 2,8 pp H (an der Genauigkeitsgrenze), ADS bis 12,4 pp H über mehrere Stöße (zwei Anker ≤ 0,74 pp auseinander). Anderer Bildmaßstab: kein Hüfte/ADS-Quotient. | 45 |
| **Threaded Needle (lineare Fusion): vier geladene Schüsse** [M-Netto] <a id="r-d2-needle"></a> | `uoTaCBMXcFk`, 34,30–42,50 s; Schüsse ≈ 34,57 / 36,82 / 39,03 / 41,13 | Rest vor Schuss 2/3/4: **6,7 / 13,1 / 19,6 pp H** – jeder Schuss hebt den Blick ≈ 6,5 pp H, und netto kommt in 2,1–2,3 s Pause nichts zurück (Eingabe unbekannt). Seitlich ≤ 1,0 pp B. Nachgemessen. | 65 |

Zusatzsichtung The Messenger (`mkwgPBa1fXI`, „75 vs 100 recoil direction“): Wandgruppen zweier Läufe sichtbar, aber Lauftausch ändert
auch die Stabilität, Neuzielen zwischen Gruppen – kein Beleg für eine Stat→Winkel-Abbildung oder die Endziffer-Regel [O].

## 3. Vergleichsspiele – Messungen

| Vorgang | Quelle, Zeit | Messung |
|---|---|---|
| CS2 M4A1-S, laufende Serie [M-Netto] | `wSZA073GUw8`, 0–2,0 s | Serie läuft bei Videobeginn schon: dx −0,5 … +1,2 % B, dy −3,1 … +1,6 % H (Montage 1280 × 546). Treffer: schmaler Stamm, seitliche Kappe [O]. |
| CS2 M4A4 [M-Netto] | `wSZA073GUw8`, 5,70–8,35 s | dy bis −5,9 % H, dx −0,9 … +1,8 % B; nach dem Steigen seitliche Richtungswechsel [O]. |
| **CS2 AK-47** [M-Netto] <a id="r-cs2-ak"></a> | `wSZA073GUw8`, 12,60–16,00 s | dy bis −11,0 % H, dx −0,3 … +2,7 % B; Wandbild erst steiler Stamm, oben breiter [O]. |
| Valorant Phantom / Vandal / Spectre [M] | `vaqlrCzy3PM`, 110,5 / 231,7 / 349,5 s | Sichtbare Trefferhüllen im **kompensierten** Lehrbeispiel: 5,4 × 1,3 / 5,8 × 1,5 / 0,8 × 5,0 % B × H. Kein ungeführtes Spray, kein Stabilitätsranking. |
| Apex R-301 / Flatline [M] | `8QQJAwUaRi0`, 127,8–131,5 / 162,0–166,9 s | 31 bzw. 29 Schüsse (HUD). Endhülle 5,9 × 20,4 bzw. 10,9 × 23,1 % B × H (4x, unten vom Rahmen begrenzt). R-301: Stamm mit Haken nach rechts; Flatline: S-/Zickzack [O]. Gesamtbahnen verworfen (Anker < 0,85). |
| **Apex HAVOC** [M-Netto] <a id="r-apex-havoc"></a> | `8QQJAwUaRi0`, 200,0–204,5 s | 29 Schüsse; Weltanker 271/271 Bilder gültig: dy bis −51,5 % H, dx −6,4 … +5,2 % B (4x-Optik, Lehrvideo hält Bilder an – keine Zeiten). Erst steil, später Seitenschleife. Hülle 6,8 × 21,5 %. |
| **BF6 B36A4: 18 Schüsse** [M-Netto] <a id="r-bf6-b36"></a> | `ROUP1z62caA`, 21,100–22,517 s | Abstand 5 Bilder (720/min). Erste sieben Schüsse nur ≈ 1,3 pp H, dann gleichmäßiger Anstieg bis −6,1 pp H; seitlich ≤ 1,8 pp B. Nachgemessen (−5,6). |
| BF6 AK4D: 8 + 5 Schüsse [M-Netto] | `ROUP1z62caA`, 49,95–51,58 s | 6–8 Bilder Abstand (≈ 514/min). Erster Teilstoß bis ≈ 5 pp H, in 22 Bildern Pause ≈ 4 pp zurück, zweiter steigt wieder bis 3,7. |
| BF6 M433: 15 Schüsse [M-Netto] | `ROUP1z62caA`, 113,12–114,12 s | 4–5 Bilder Abstand (≈ 847/min). Senkrecht bis −4,4 pp H, seitlich ≤ 2,2 pp B. |
| **BF2042 M5A3 / AK-24 / K30** [M-Netto] <a id="r-bf2042"></a> | `enyEjb4dXU8` 41,0–43,3 s / `0Rq3rypcIQo` 154,1–156,8 s / `L6BiTz_3teo` 167,2–168,7 und 176,0–178,5 s | Netto ≈ 11 / 12 / 8–11 pp H aufwärts, seitlich ≤ 1,3 / 0,8 / 1,7 pp B – **fast rein senkrecht**. Einschussspalte im Hüftbild ≈ 8 / 10 / 11 % H hoch, ≈ 1,3–1,8 % B breit. |
| **CoD MW2019 Kilo 141 / M4A1 / AK-47** [O/C] <a id="r-mw2019"></a> | `nBsmMfQfd_M`, 10,5–28 / 62–79 / 113–126 s | Je **drei Wandserien mit gleicher Grundform**: Kilo aufwärts-links diagonal, M4A1 aufwärts mit Rechtsbogen oben, AK-47 lange Säule mit seitlichen Knicken; mit Aufsätzen kompakter. Keine Zahlen (24/s, Splitbild). |
| Halo Infinite MA40 / BR75 / Mk50 / VK78 [M-Netto] | `ZfNuA5r-470` 11,8 / 52,6 / 85,6 s; `9TdIttKuOgE` 7,5–13,3 s | MA40 17 Schüsse bis −5,7 pp H; BR75 sechs Dreiersalven (4 Bilder intern), lokal fast ruhig (≤ 0,7 pp); Mk50 9 Schüsse ≤ 0,7 pp; VK78 20 Wand-Taps −2,4 … +1,1 pp H. Alle unter Zielverfolgung. |
| **Titanfall 2 C.A.R. / R-201 / Hemlok** [M-Netto] <a id="r-tf2"></a> | `4sDwTD9U8bw` 96,6–101,5 / 171,3–175,4 / 207,3–212,8 s | C.A.R. 36 Schüsse bis −4,3 pp H mit seitlichen Wechseln; **R-201 29 Schüsse bis ≈ −9 pp H, Ende ≈ −3, seitlich −2,9 … +2,3 pp B** (korrigiert, siehe › 1); Hemlok sechs Dreiersalven bis −4,4 pp H. Dauerfeuer 4–5 Bilder je Schuss. |

## 4. Musterkatalog je Klasse – Destiny zuerst

Formen sind den genannten Clips zugeordnet; Prozentwerte unterschiedlicher Spiele werden nicht gemittelt.

| Klasse | Destiny | Vergleich | Form in den gemessenen Clips (Netto, Eingabe unbekannt) |
|---|---|---|---|
| Automatik | Chroma Rush: gleichmäßige Rampe, ≈ 1 pp H je Schuss, seitlich kaum; Abyss: lange Säule mit kleinen Seitenwechseln, dreimal gleiche Form | CS2: Stamm mit seitlicher Kappe; MW2019: Diagonale / Bogen / Säule je Waffe; Apex: Haken, S, Schleife; BF: fast senkrecht | in den Destiny-Clips senkrecht mit leichtem Wackeln, keine markante Figur; die markanten Figuren der CS2/MW2019/Apex-Clips liegen in der Seitenform |
| Impuls | Gridskipper: Stufe je Salve, Erholung zwischen den Salven | Halo BR75 fast ruhig; Hemlok steigt über die Salven | Gridskipper: jede Salve eine Stufe, in der Pause teilweise zurück |
| Scout | Tone Patrol: kräftiger Einzelimpuls, wachsender Rest vor den Folgeschüssen | VK78 (getaktete Taps) | im Tone-Patrol-Clip wächst die Netto-Restlage vor den Folgeschüssen (−1,7 → −3,3 pp H); nach dem letzten Schuss 23 Bilder bis ins ±3-pp-Band |
| Handfeuerwaffe | Annual Skate: großer Hochimpuls, deutliches Kippen des Modells, Rest klein | kein gleichwertiger Vergleich | in diesem Clip großer Einzelimpuls; das Modell kippt sichtbar stärker, als die Welt wandert |
| Seitenwaffe | Dead Man Walking: Hochimpulse bis ≈ 10 pp H | Halo Mk50 klein | – |
| MP | Foggy Notion: steigende Nettobahn ≈ 9 pp H, seitlich wenig | BF2042 K30 schmal senkrecht; C.A.R. mit Seitenwechseln | – |
| MG | Shattered Cipher: ADS-Fenster bis 12,4 pp H, Hüftfenster 2,8 pp H (anderer Bildmaßstab, kein Quotient) | kein Vergleich | – |
| Lineare Fusion | Threaded Needle: ≈ 6,5 pp H je Schuss, netto **kein Rücklauf** zwischen Schüssen | kein Vergleich | im Clip eine Stufe je Schuss, die bis zum nächsten Schuss stehen bleibt |

**Rücklauf:** gemessen nur als Netto der Quelle – Chroma Rush 24 Bilder (0,40 s) nach 12 Schüssen, Tone Patrol 23 Bilder, Gridskipper
12 Bilder. Threaded Needle bleibt oben. Ob der Rücklauf vom Spiel oder vom Spieler kommt, ist offen.

## 5. Muster und Unterschiede

1. **Fest, hybrid oder zufällig ist eine Entwurfsentscheidung, die Spiele wechseln:** CS2 und CoD MW2019 setzen auf lernbare Grundbahnen,
   Valorant auf einen festen Anfang mit zufälligen Seitenwechseln, Apex auf feste Punkte mit kleiner Varianz, Destiny 2023 kurz auf
   teilweise feste Folgen und 2025 wieder zurück (außer Vigilance Wing).
2. **Die beiden gemessenen Destiny-Automatikwaffen zeigen keine Signaturform:** Chroma Rush und Abyss Defiant steigen als Säule mit
   kleinem Seitenwackeln; ob das für alle Destiny-Waffen gilt, ist mit zwei Clips nicht belegt. Signaturformen (Diagonale, Bogen, S, Haken) zeigen CS2, MW2019 und Apex.
3. **Die Battlefield-Fenster sind fast senkrecht:** BF6 und BF2042 steigen in allen sechs gemessenen Fenstern mit ≤ 2,2 pp B seitlich
   (Netto, Eingabe unbekannt); BF6 B36A4 beginnt flach und
   steigt erst nach etwa sieben Schüssen.
4. **Kamera, Modell und Treffer bewegen sich verschieden:** Apex-Trefferhüllen sind kleiner als die gleichzeitige Kamerabahn,
   Annual Skate kippt das Modell stärker als die Welt wandert, Valorant/CS zeigen Treffer, Kamera und Modell getrennt.
5. **Takt und Rest hängen in den Clips zusammen:** bei Tone Patrol (Scout) und Threaded Needle (Fusion) wächst die Restlage vor jedem Folgeschuss, bei Salvenwaffen erholt sich die Bahn
   in der Salvenpause.

**Spielerstimme Nexxoss Gaming [C] (0.37 „Verdict“, Einzelstimme aus Auto-Untertiteln, nie gegen eine [M]-Messung; Abgleich je Klasse in [destiny2 › Verdict](destiny2.md#s-verdict)):** Fünf Klassenurteile passen zu den Formen in › 4: Automatik „sehr stabil“ ([MpYNiAGiyOI](https://www.youtube.com/watch?v=MpYNiAGiyOI) [02:12]), MP „die Waffe zieht“ ([uWSAd3wZ7Cs](https://www.youtube.com/watch?v=uWSAd3wZ7Cs) [03:39]), Seitenwaffe „zieht richtig hoch“, man müsse gegensteuern ([Gx86mSoVO98](https://www.youtube.com/watch?v=Gx86mSoVO98) [03:11]), Donnerlord (MG) „zieht zwar schon hoch“ ([9DjwEfcZptE](https://www.youtube.com/watch?v=9DjwEfcZptE) [02:15]), Impuls mit „Problem mit der Stabilität“ ([89v3B8Vpkvk](https://www.youtube.com/watch?v=89v3B8Vpkvk) [01:35]). Die Handfeuerwaffe „Die Ruhige Hand“ nennt er „ganz stabil“ ([GgcO_mG25i4](https://www.youtube.com/watch?v=GgcO_mG25i4) [03:03]), obwohl die Kamera im Zielen ≈ 22 pp H springt ([z-v37-hc-kick](destiny2.md#z-v37-hc-kick)) – die Messung gilt; ob das Urteil relativ zu anderen Handfeuerwaffen gemeint ist oder die Rückkehr meint, ist offen (Einschätzung).

## 6. Gestaltungsregeln für BASIC (Vorschlag)

Vorschlag aus den Beobachtungen oben, im Auftrag der BASIC-Sitzung formuliert und ihr per Briefkasten übergeben; Werte und Entscheidung
liegen in BASIC (`cubeescape-ballon`), nicht hier. Quellprozente sind Formreferenzen und müssen im eigenen FOV
kalibriert werden.

1. **Vier Kurven getrennt führen:** Grundbahn der Kugel, Kameraantwort, Modellkick und Streuung als eigene Parameter
   (Apex, Annual Skate, CS2 zeigen sie verschieden).
2. **Eine lesbare Form je Waffe:** senkrechter Beginn, Diagonale, Bogen oder spätes S. Mehr Hub allein schafft wenig Eigenart.
   Die beiden Destiny-Automatikclips zeigen eine steigende Säule mit kleinem Seitenwackeln; Signaturformen wie in CS2/MW2019/Apex
   wären eine eigene Entscheidung.
3. **Salven zweistufig:** Takt in der Salve und Erholung bis zur nächsten getrennt einstellen (Gridskipper, BR75, Hemlok).
4. **Lernbarkeit ausdrücklich festlegen:** fester Anfang plus begrenzter Zufall (Valorant) oder ganz feste Bahn (CS2) ist eine Entscheidung,
   kein Nebenprodukt.
5. **Zufall begrenzen und getrennt benennen:** Richtungsvariation der Bahn und Streuung um den Zielpunkt sind verschiedene Größen; eine
   Zufallsquote lässt sich aus diesen Einzelserien nicht ableiten.
6. **Rest unter schnellem Takt zulassen und testen:** Tone Patrol und Threaded Needle zeigen wachsenden Rest; ein vollständiger
   Rücklauf nach jedem Schuss ist keine Pflicht für alle Klassen.
7. **Rücklauf als eigener Serienparameter:** letzter Schuss, Eintritt ins Toleranzband (Destiny-Beispiele 0,2–0,4 s) und bleibender
   Versatz als getrennte Marker abnehmen.
8. **Ersten Schuss getrennt behandeln:** Erstschuss-Kick und Erstschuss-Streuung sind zwei Parameter (Battlefield 2042 führt eigene
   Multiplikatoren; BF6 B36A4 beginnt flach).
9. **Visierlesbarkeit im Dauerfeuer prüfen:** Modellkippen, Blitz und Optikrand dürfen keine Zielpunktwechsel vortäuschen; am eigenen
   Testclip mit Weltanker prüfen.
10. **Fassung speichern:** Muster ändern sich mit Patches (Destiny 2023 → 2025); im Standard festhalten, welche Fassung gilt und
    wie sie gemessen wurde.

## 7. Offen und nicht messbar

- **Nicht messbar aus diesen Aufnahmen** (nicht erneut versuchen): isolierter Rückstoß ohne Spielereingabe (außer Bungie-Test),
  Zufallsanteil, Erstschuss-Streuung, isolierte Rückführzeit, Winkel in Grad, Kadenz aus Lehrvideos mit Standbildern (Apex),
  Zeiten aus 24/30-/s-Dateien (MW2019, Valorant, Abyss, BF2042 AK-24/K30).
- **Was eine Kontrollaufnahme braucht:** gleiche Waffe, Perks, Stabilität, FOV und Standposition; feste Wand und Haltepunkt; mindestens
  zwei identische Serien plus mehrere isolierte erste Schüsse; sichtbarer Nachweis der Blick-Eingabe (Overlay); ungeschnittene 60/s bis
  zur Ruhe. Für Erstschuss-Statistik und Zufallsquote deutlich mehr Wiederholungen.
- **Werkzeugfalle:** Ein Weltanker auf sich wiederholender Struktur (Turmsegmente, Wolken, Wandpaneele) kann mit hoher Korrelation auf
  den falschen Abschnitt springen (R-201: 12 pp in 0,3 s). Jede Bahn mit einem zweiten, anders aussehenden Anker gegenprüfen.
- Waffenzuordnung im Sammelvideo `IG-GZ72Vbi0` folgt der Reihenfolge der Quelle; Waffennamen wurden nicht einzeln am Bild gelesen.
