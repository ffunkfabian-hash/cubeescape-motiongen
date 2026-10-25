# Oberflächenmuster von Waffen – Farbfelder, Akzent, Muster, Verschleiß, Shader

Referenzanalyse REF 0.18 „Livery“ (25.10.2026) für die Waffenreihe **BASIC** (Projekt `cubeescape-ballon`). Nur Videospiele.
Destiny 2 ist das Stilvorbild höchster Priorität – **nicht kopieren**: keine Muster, Logos, Texturen oder Bilder übernehmen, nur
verstehen, wie Farbfelder, Akzente, Muster und Abnutzung verteilt sind. Hier stehen Beobachtungen und Messwerte; der Abschnitt
[BASIC-Materialrollen](#7-basic-materialrollen-vorschlag) ist ein **Vorschlag**, entschieden wird in BASIC. Maschinenlesbare Fassung:
[`data/oberflaechen.json`](../data/oberflaechen.json). Getrennte Themen: Visiere in [visiere.md](visiere.md) (REF 0.14), Proportionen in
[proportionen.md](proportionen.md) (REF 0.15), Rückstoß in [rueckstoss.md](rueckstoss.md) (REF 0.16), Zielbewegung in
[zielbewegung.md](zielbewegung.md) (REF 0.17).

**Stand: Zuarbeit größtenteils nicht übernommen.** Grundlage war eine Antigravity-Analyse (24.10.2026: 9 Spiele, 86 Beispiele,
34 Videos). Von 86 Beispielen sind **30 bestätigt** (21 wie angegeben, 9 mit korrigierter Quelle oder Zeit), **56 weggelassen**. Ihre
Beschreibungsfelder (Zonen, Farbwerte, Flächenanteile, Verschleißwerte) sind nicht übernommen, weil sie bei mindestens 8 der 24
bestätigten Destiny-2-Waffen dem Bild widersprechen. Was hier steht, ist eigene Sichtung und Messung.

**Status:** **[M]** am eigenen 1080p-Bild gemessen (Abschnitt [4](#4-nachmessung-m)); **[O]** eigene Sichtung am Menübild ohne Zahl;
**[A]** Antigravity-Angabe, nur zum Vergleich. Farbwerte sind **gerenderte Pixel** im Inspektionsmenü (warmes Licht von oben
rechts, Schatten, Glanz), keine Albedo und keine Materialwerte. **Jede Zahl ist das Beispiel einer Waffe in einem Bild**, kein
Herstellermittel und keine Generatorgrenze.

## 1. Quellen und Methode

**Quellenprüfung:** Weil Antigravity schon in REF 0.14 falsche Video-IDs, Kanäle und Titel nannte, ist jede Quelle per yt-dlp geprüft
(Kanal, Titel, Hochladedatum, Länge) und jedes Beispiel am Bild zum angegebenen Zeitpunkt angesehen. Alle 34 Video-IDs existieren,
aber bei **24** stimmen Kanal oder Datum nicht (z. B. `TnblT7JnMPI` ist von Hectorlo 2021, nicht „Halo Inspect“ 2022; `QxZAflLtJRQ` ist
von 2026, nicht 2024). 14 Zeitstempel liegen hinter dem Ende ihres Videos. Häufig passt das Video nicht zur Waffe: `X_ADv1HMwkg` zeigt
Halo 3, `Qh7gYQpSq0Y` nur Widowmaker, `Nwp4VJWUujY` und `3T2UZUYPzEc` sind Teileleitfäden zu Vladof-Sturmgewehren und
Hyperion-Scharfschützengewehren, die beiden Nb90-Shadervideos zeigen je nur eine Waffe. Gründe je Beispiel:
`data/oberflaechen.json` › `examples[].reason`.

| Spiel | Antigravity | bestätigt | korrigiert | weggelassen |
|---|---|---|---|---|
| Destiny 2 | 30 | 15 | 9 | 6 (Liminal Vigil, The Last Word, The Huckleberry, Telesto, Midnight Coup, Blast Furnace) |
| Destiny 1 | 7 | – | – | 7 (Videos sind Visiervergleiche, vier Zeitstempel hinter dem Ende) |
| Marathon, Halo Infinite, Apex, Valorant, CoD, Overwatch 2 | 42 | je 1 | – | 36 |
| Borderlands 3 | 7 | – | – | 7 |

Die sechs bestätigten Vergleichsbeispiele (CE Tactical Sidearm, MA40, R-301 mit Trophy-Collector-Skin, Classic, 9mm PM, Widow's Kiss)
sind nur als Waffe bestätigt; die Skinnamen stimmen bis auf den R-301 nicht oder sind nicht zu sehen, die Bilder sind Spielszenen ohne
belastbaren Musterbefund. **Der Vergleich mit anderen Spielen fehlt damit in dieser Version** (Abschnitt [8](#8-offen-und-nicht-messbar)).

**Verwendete Quellen** (alle per yt-dlp bestätigt; Videos nur im Cache `~/Library/Caches/CubeEscape/reference/`, nie im Repo):

| Quelle | Kanal | Hochgeladen | Inhalt | hier verwendet |
|---|---|---|---|---|
| [`IG-GZ72Vbi0`](https://www.youtube.com/watch?v=IG-GZ72Vbi0) <a id="o-q-suros"></a> | Ultraclocked | 14.02.2020 | D2 Titan-Legendaries (SUROS), 1080p60 | 10 Menüs, 4 Beispiele, 2 [M] |
| [`73lGCT7yOtk`](https://www.youtube.com/watch?v=73lGCT7yOtk) <a id="o-q-hakke"></a> | Ultraclocked | 25.01.2020 | D2 EDZ-Legendaries (Häkke) | 13 Menüs, 5 Beispiele, 2 [M] |
| [`42zdQOVBAD0`](https://www.youtube.com/watch?v=42zdQOVBAD0) <a id="o-q-omolon"></a> | Ultraclocked | 30.01.2020 | D2 Nessus-Legendaries (Omolon) | 10 Menüs, 4 Beispiele, 2 [M] |
| [`afs_dhFDhQU`](https://www.youtube.com/watch?v=afs_dhFDhQU) <a id="o-q-veist"></a> | Ultraclocked | 09.02.2020 | D2 Io-Legendaries (VEIST) | 9 Menüs, 4 Beispiele, 2 [M] |
| Einzelvideos | Ultraclocked | 15.–20.02.2021 | Extraordinary Rendition `Y5OLr0nbgSg`, Far Future `RXgRxHESqHQ`, Imperial Needle `dKNTDzi__Qo`, Threaded Needle `uoTaCBMXcFk` | 4 Beispiele |
| [`kWUViHovz1E`](https://www.youtube.com/watch?v=kWUViHovz1E) | Destiny 2 | 17.05.2023 | Bungie, Inspektionsmenü Season of the Deep | Conditional Finality |
| [`RdbQEge8ziM`](https://www.youtube.com/watch?v=RdbQEge8ziM) <a id="o-q-rosarago"></a> | Nb90 | 28.09.2024 | Shaderreihe auf Ros Arago IV (Cassoid) | Shaderlogik |
| [`pazFJ51axhE`](https://www.youtube.com/watch?v=pazFJ51axhE) <a id="o-q-elsie"></a> | Nb90 | 23.09.2024 | Shaderreihe auf Elsie's Rifle (BRAVE) | Shaderlogik, 1 Beispiel |
| Vergleich | QxZAflLtJRQ soda · TnblT7JnMPI Hectorlo · UetKaZiF9uA ClawZ · LF9pPIi5ops PC Gaming Videos · HfgUhmc8p00 EXILAS · Qh7gYQpSq0Y iFaiiLed | 2020–2026 | Marathon, Halo Infinite, Apex, Valorant, BO6, Overwatch 2 | nur Waffe bestätigt |

**Menüabschnitte:** In den vier Hersteller-Videos zeigt Ultraclocked jede Waffe zuerst im Inspektionsmenü, dann herangezoomt ohne
Bedienleiste. Die Abschnitte sind per Vorlagenvergleich der Menüleiste („APPEARANCE“) bei 1/s gefunden (42 Menüs); Zeitangaben hier
sind der Beginn des Menüs in Sekunden. Gemessen wird im Bild aus der Mitte des Abschnitts (Waffe groß, keine Bedienleiste).

**Messung [M]:** Der Menühintergrund ist in allen vier Videos gleich. Er ist als maskierter Median über die 42 Menübilder geschätzt
(960 × 540, zwei Runden ohne Pixel, die mehr als 30 Stufen vom Median abweichen); die Fläche, in der die meisten Waffen liegen, ist
bilinear aus ihrem Rand gefüllt. Waffe = Summe der RGB-Abweichung vom Hintergrund > 36, danach Schließen und Öffnen, eingeschlossene
Löcher gefüllt (Abzugsbügel-Öffnungen zählen dadurch mit, < 1 %), Herstellerbanner, Wasserzeichen und Bedienleiste ausgenommen.
Je Waffenpixel CIELAB (sRGB, D65): **bunter Anteil** = Anteil mit Buntheit C* über 15, 25 und 35; bei C* ≤ 25 Helligkeitsklassen hell
(L* > 65), mittel, dunkel (L* < 35). **Proben** sind 12 × 12-px-Mittel im 1080p-Bild an Stellen, die im Kontrollbild markiert und
angesehen sind (Lage in `data/oberflaechen.json` › `measurements[].probes`). Genauigkeit: Maskenrand ±2 px (Anteile ±1–2 Punkte),
Proben ±3 L*. Skripte und Kontrollbögen: `~/Library/Caches/CubeEscape/reference/oberflaechen-0.18/work/`.

## 2. Destiny 2 – Hersteller-Grundlacke und Sonderwaffen

Sichtung [O] am Menübild, bei acht Waffen gemessen [M]. Die Y1-Waffen (Ultraclocked 2020) tragen ihre Grundlackierung; welcher Shader
aktiv ist, zeigt das Video nicht. Korrigierte Zeiten nennen Antigravitys Angabe.

| Waffe | Quelle, Menü ab | Befund |
|---|---|---|
| **Annual Skate** <a id="o-d2-annual-skate"></a> [M] | [SUROS](#o-q-suros) 53 s | mintweiße Schale, zwei rote Diagonalbänder mit weißen Abplatzern, SUROS-Schriftzug, dunkler Rahmen und Griff, blanker Lauf |
| **Solemn Hymn** <a id="o-d2-solemn-hymn"></a> [M] | SUROS 315 s | weiße Oberschale, breites rotes Band entlang der Schalenunterkante mit weißen Sprenkeln, dunkelgraues Untergehäuse, graues Magazin |
| **Swift Ride** | SUROS 350 s | weiße Schale mit gesprenkelten roten Diagonalbändern, dunkler Rahmen, gelochter Stahl-Laufmantel |
| **Tone Patrol** | SUROS 375 s | weiß-rote Schale mit SUROS-Schriftzug, dunkles Untergehäuse, gelochter Stahl-Laufmantel |
| **A Single Clap** | SUROS 0 s (Antigravity: Omolon-Video 1:20) | weiße Schale mit rotem Band, dunkler Schaft, dunkles Zielfernrohr |
| **Eystein-D** <a id="o-d2-eystein-d"></a> [M] | [Häkke](#o-q-hakke) 220 s | Grün-Tarnung nur auf der oberen Handschutzschale, ockerfarbenes Feld mit rotem HÄKKE-Schriftzug, schwarzes geripptes Untergehäuse, blanke Mündungsbremse |
| **Bad News** <a id="o-d2-bad-news"></a> [M] | Häkke 0 s | stark abgeriebene helle Stahl-/Weißschale, orangefarbener Block hinten oben, brauner Griff |
| **Minimum Distance** | Häkke 408 s (6:45) | creme-oranger Schlitten mit HÄKKE-Schriftzug, brauner Griff |
| **Show of Force** | Häkke 541 s (8:58) | abgeriebene hellgraue Fleckentarnung, orange Markierung hinten, Stahllauf |
| **Cartesian Coordinate** | Häkke 141 s (Antigravity: Nb90-Video) | rosarot-graue abgeriebene Tarnung, dunkle Teile |
| **Uriel's Gift** <a id="o-d2-uriels-gift"></a> [M] | [Omolon](#o-q-omolon) 432 s | blaugraue Fleckentarnung über Ober-, Unterschale und Zielfernrohr, türkiser Streifen, türkise Flüssigkeitskapsel, abgeriebene Kanten |
| **The Mornin' Comes** <a id="o-d2-mornin-comes"></a> [M] | Omolon 386 s | rot über Körper und Zielfernrohr, dunkles Magazin, blaue Linse |
| **Last Hope** | Omolon 45 s (5:00) | blaugraue Tarnung, türkise Kapseln im Griff, OMOLON-Schriftzug |
| **Seven-Six-Five** | Omolon 223 s | blaugraue Tarnung mit türkisen Teilen |
| **Valakadyn** <a id="o-d2-valakadyn"></a> [M] | [VEIST](#o-q-veist) 317 s (1:10) | dunkles Olivgrau mit hellgrünem Lochfeld seitlich, blanker Schalldämpfer |
| **Death Adder** <a id="o-d2-death-adder"></a> [M] | VEIST 116 s (2:45) | cremefarbene Schale, gelbe Zelle oben, schwarzer Griff mit weißen Streifen, orange leuchtende Anzeige |
| **Widow's Bite** | VEIST 354 s (4:15) | dunkelgrau mit violettem Schimmer, grünes Visierelement |
| **The Rattler** | VEIST 248 s (5:30) | dunkles Oliv mit violettem Schimmer, kleine grüne Akzente, weiße Griffstreifen |
| **Extraordinary Rendition** | `Y5OLr0nbgSg` 1 s | abgeriebenes Gold über dunklem Petrol (gerippter Laufmantel), schwarzer Rahmen und Griff |
| **Far Future** | `RXgRxHESqHQ` 1 s | abgeriebenes Gold über Petrol, gerippter Laufmantel und Schaftrohr, orange Ringe am Zielfernrohr |
| **Threaded Needle** | `uoTaCBMXcFk` 1 s | abgeriebenes Gold über Schwarz, petrolfarbene gerippte Teile, goldenes Visier |
| **Imperial Needle** | `dKNTDzi__Qo` 1 s | schwarz-goldener Bogen, Gold an den Kanten der Wurfarme, petrolfarbener Griff |
| **Conditional Finality** | `kWUViHovz1E` 1 s | zwei Hälften rosa/rot und blau mit leuchtenden Kanten, Flammen- und Eiseffekt am Lauf (Exotic) |
| **Elsie's Rifle** | [Nb90](#o-q-elsie) 430 s | wechselnde Shader, siehe Abschnitt 3; Antigravitys Shadername nicht bestätigt |

**Herstellerbild in den 42 Menüs [O]:** SUROS durchweg weiße bis mintweiße Schale mit Rot, dunkler Rahmen, blanke gelochte
Laufmäntel; Häkke Weiß/Stahl, Grün-, Grau- oder Rosatarnung mit Orange oder Ocker, braune oder schwarze Griffe; Omolon blaugraue Tarnung mit
Türkis, einzelne Waffen ganz rot oder oliv; VEIST dunkles Oliv, Grau oder Blaugrau mit violettem Schimmer und kleinen Grünflächen, eine Waffe
creme mit Gelb. Fast jede Waffe trägt den Herstellerschriftzug. Innerhalb eines Herstellers wiederholen sich Farbwelt und Musterart, die
Verteilung auf die Teile wechselt von Waffe zu Waffe. Die Cabal-/Chosen-Waffen (2021) teilen ein eigenes Bild: Gold über Petrol und
Schwarz, flächig abgerieben.

## 3. Shaderlogik – was ein Shader ändert und was bleibt

Zwei Nb90-Videos zeigen je eine Waffe mit allen Shadern ihres Kontos; Bögen alle 10 bzw. 15 s und sechs bis zehn Einzelbilder je Video [O].

| | Ros Arago IV (Cassoid, [`RdbQEge8ziM`](#o-q-rosarago)) | Elsie's Rifle (BRAVE, [`pazFJ51axhE`](#o-q-elsie)) |
|---|---|---|
| geändert | Farbe **und** Oberflächenstruktur der ganzen Waffe: Schale, Rahmen, Griff, Magazin, Schaft (Arctic Pearl bei 115 s färbt auch Griff und Magazin weiß); je Shader zwei bis drei Farb-/Materialfelder (605 s: schwarze Schalenteile, rotbraunes Gehäuse, Stahl) | Farben der Bänder und der Grundfläche, teils Metall statt Lack (900 s: Stahl mit hellgrünem Feld) |
| Muster | kommt aus dem Shader: Digitaltarnung (Vanguard Unity, 105 s), Bruchstruktur, Schuppen, Marmor, Rost; läuft über alle Paneele | festes Bandlayout der Waffe: Lage und Form der Diagonalbänder bleiben bei jedem Shader gleich, der Shader färbt sie nur; die Bänder queren Paneelgrenzen schräg |
| fest | Form, Prägungen und Kleinsymbole behalten Lage, nehmen aber die Shaderfarbe an | goldenes Emblem hinten, kleine blaue Leuchtanzeige oben, helle Magazinfenster |

**Folgerung als Beobachtung:** Ein Destiny-Shader belegt erkennbar wenige Farb-/Materialfelder und kann die ganze Waffe umfärben;
Leuchtteile und Embleme sind ausgenommen. Ob ein Muster vom Shader oder von der Waffe kommt, unterscheidet sich je Waffe. Antigravitys
„4-Kanal-System nach den Quadranten des Shader-Symbols“ mit festen Flächenanteilen (35–50 / 15–25 / 25–35 / 5–12 %) ist aus den Videos
weder bestätigt noch widerlegt und hier nicht übernommen.

## 4. Nachmessung [M]

Acht Grundlacke aus den vier Hersteller-Videos, Bild aus der Mitte des Menüabschnitts. Bunter Anteil = Anteil der Waffenfläche mit
C* über der Schwelle; ΔL* = beleuchtete Schalenprobe minus dunkle Rahmen-/Griffprobe.

| Waffe | Bild | C* > 15 | C* > 25 | C* > 35 | Schale (Probe) | Rahmen/Griff | ΔL* | Antigravity [A] |
|---|---|---|---|---|---|---|---|---|
| Annual Skate <a id="o-m-annual-skate"></a> | 54,5 s | 8,0 % | 6,7 % | 5,0 % | `#C7DAD9` L* 85,7 | `#2E2E2E` 18,9 | 67 | Akzent 20 %, `#9C5769` |
| Solemn Hymn <a id="o-m-solemn-hymn"></a> | 317 s | 11,0 % | 9,9 % | 8,5 % | `#C5D2D0` 83,2 | `#2E2E2E` 18,9 | 64 | Akzent 18 %, `#C41E3A` |
| Bad News <a id="o-m-bad-news"></a> | 2 s | 4,5 % | 2,7 % | 1,0 % | `#C8D0D0` 82,9 | `#191009` 5,4 | 78 | „Schwarzstahl 55 %“ – falsch |
| Eystein-D <a id="o-m-eystein-d"></a> | 222 s | 12,8 % | 5,4 % | 0,2 % | Tarnung `#475734` 34,8 | `#25201D` 12,7 | 22 | Herstellerband 8 % |
| Uriel's Gift <a id="o-m-uriels-gift"></a> | 434 s | 27,6 % | 1,7 % | 0,1 % | Tarnung `#83A2B3`/`#63899C` 55–65 | Unterschale `#3B586A` 35,9 | 19–29 | ähnlich (Petrol/Indigo) |
| Death Adder <a id="o-m-death-adder"></a> | 117,5 s | 15,7 % | 3,3 % | 2,8 % | `#ACAF98` 70,7 | `#141614` 7,0 | 64 | „mattschwarz 60 %, giftgrün“ – falsch |
| The Mornin' Comes <a id="o-m-mornin-comes"></a> | 387,5 s | 45,9 % | 28,1 % | 10,1 % | rot `#321211`–`#471A17` 10–16 | Magazin `#101416` 6,0 | 4–10 | „kobaltblau 55 %“ – falsch |
| Valakadyn <a id="o-m-valakadyn"></a> | 318,5 s | 3,1 % | 2,8 % | 2,3 % | `#646E6D` 45,6 | dunkle Klasse L* 11,6 | ≈ 34 | „giftgrüne Haube 30 %“ – zu hoch |

Weitere Proben: Akzentflächen Annual Skate `#CD697C`/`#97323E` (C* 42–46), Solemn Hymn `#B3686A` (32), Bad News Orange `#EDB393` (30),
Eystein-D Ockerfeld `#7F6C35` (33), Uriel's Gift Türkis `#39828C` (23), Death Adder Gelb `#D8D170` (50), Valakadyn Grün `#3D5512` (40);
blanke Läufe und Mündungen L* 40–74 bei C* ≤ 3. Mit Schatten und Glanz verteilt sich die Helligkeit breit (L*-Spanne 10.–90.
Perzentil der Waffenfläche: helle Schalen 69–75, Tarnung und dunkle Lacke 46–52, Mornin' 37).

**Befund:** Der bunte Anteil der Grundlacke liegt bei 7 von 8 Waffen unter 10 % (C* > 25); Antigravitys Akzentanteile sind etwa doppelt
so hoch. Er hängt stark an der Schwelle (Uriel's Gift 1,7 % oder 27,6 %), weil gedämpfte Tarnfarben zwischen 15 und 25 liegen. Der
Helligkeitsabstand Schale–Rahmen ist bei hellen Schalen groß (64–78), bei Tarnung und Farblack klein (4–34).

## 5. Die Antigravity-Regeln am Bild

Antigravity formulierte zehn „harte Gestaltungsregeln“. Hier sind sie als Behauptung mit Befund geführt, nicht als Gesetz.

| # | Behauptung [A] | Befund | Urteil |
|---|---|---|---|
| 1 | 3–4 Farbzonen, keine überzeugende Waffe hat mehr | Die 42 Grundlacke zeigen meist drei bis vier Felder (Schale, dunkler Rahmen, Metall, ein Akzent; Tarnung = ein Feld mit zwei bis drei Tönen); Shader zwei bis drei Felder plus Metall [O] | Beobachtung passt, Wertung unbelegt |
| 2 | Akzent 5–12 %, mehr wirkt wie Spielzeug | 1,7–9,9 % bei 7 von 8 (C* > 25), Belege zu hoch (Annual Skate 6,7 statt 20 %, Solemn Hymn 9,9 statt 18 %); Mornin' ist rot als Grundfarbe [M] | Größenordnung „unter etwa 10 %“ passt für Grundlacke; Wirkung unbelegt |
| 3 | Muster enden an Fugen und Kanten | Eystein-D: ja; Annual Skate, Swift Ride, Elsie's Rifle, Ros-Arago-Shader: Muster queren Paneele [O] | als Regel widerlegt |
| 4 | Musterelement 2–6 % der Länge (10–35 mm) | nicht gemessen; Millimeter haben keinen Maßstab im Bild | offen |
| 5 | Schale/Rahmen ΔL* ≥ 40 | helle Schalen 64–78, Tarnung und Farblack 4–34; Antigravitys eigener Omolon-Beleg ergibt 27 [M] | als allgemeine Regel widerlegt |
| 6 | Visiere bleiben in 85 % neutral | Visiergehäuse folgen oft der Lackierung (Uriel's Gift, Mornin', Cabal/Chosen); neutral bleibt die Linse; 85 % ungezählt [O] | für Gehäuse widerlegt |
| 7 | Funktionsteile bleiben unlackiert | Läufe und Mündungen meist blank; Shader färben aber auch Griff, Magazin, Schaft; fest bleiben Emblem, Leuchtanzeige, Magazinfenster (Elsie's) [O] | teilweise |
| 8 | Verschleiß zu 80 % an Kanten, nie flächig | Kantenabrieb kommt vor (Uriel's Gift), ebenso flächige gemalte Abnutzung: Sprenkel im Rotband (SUROS), ganze Schale (Bad News), Gold über Dunkel (Cabal/Chosen) [O] | Absolutform widerlegt |
| 9 | Material- statt Farbkontrast (Beleg Superblack) | Beleg nicht im genannten Video; Gold neben Petrol und Stahl neben Lack sichtbar; Rauheit aus Video nicht messbar | offen |
| 10 | Herstellerschrift als Maßstabsanker (1–3 %) | Schriftzug auf fast allen Y1-Grundlacken; Größe nicht gemessen [O] | bestätigt, Größe offen |

## 6. Was „hochwertig statt laut“ wirken lässt – Beobachtungen

Nur aus den bestätigten Destiny-Bildern; keine Wirkungsmessung.

- **Wenige Felder, eine Signalfarbe:** Die Grundlacke tragen eine bunte Farbe auf wenigen Prozent der Fläche (Band, Block, Schriftfeld);
  Ausnahme sind ganz farbige Waffen wie The Mornin' Comes, deren Farbe dann gedämpft und dunkel gerendert ist (L* 10–16).
- **Hell/Dunkel trägt die Form bei hellen Schalen,** bei Tarnungen tun es Tonwechsel innerhalb einer Farbfamilie und blanke Metallteile.
- **Abnutzung ist gemalt und flächig verteilt** (Sprenkel, abgeriebene Flächen), nicht nur Kantenaufhellung.
- **Muster haben eine Richtung:** Diagonalbänder (SUROS, Elsie's Rifle) und großflächige Flecken (Omolon, Häkke) statt feinem Rauschen.
- **Familie über Farbwelt:** Hersteller erkennt man an Farbwelt, Musterart und Schriftzug, nicht an gleicher Verteilung auf den Teilen.

## 7. BASIC-Materialrollen (Vorschlag)

Abbildung der Beobachtungen auf die Rollen in `basic/kit.py` (cubeescape-ballon, Branch `claude/ballon-0.7-truecolor`, gelesen
25.10.2026: `shell`, `graphite`, `anodized`, `trim`, `accent`, `energy`, `decal`, Skins mit `roles`, `pattern`, `wear`). **Nur Vorschlag;
entschieden wird in BASIC.** BASIC-Farben sind Albedo, die Destiny-Werte gerenderte Pixel – nur als Größenordnung vergleichbar.

| Rolle | Beobachtung in Destiny 2 | Vorschlag |
|---|---|---|
| `shell` | Hauptträger von Farbe und Muster; Grundlacke hell (L* 71–86) oder Tarnung/Farblack (L* 10–65) | Skin färbt `shell` immer; Muster liegt hier |
| `graphite` | dunkler Rahmen, Griff, Untergehäuse (Proben L* 5–19); Shader färben auch ihn um (Arctic Pearl) | darf je Skin umgefärbt werden, Standard dunkel; Kontrast zu `shell` je Skin festlegen statt pauschal ΔL* ≥ 40 |
| `anodized` | Visiergehäuse folgen oft der Lackierung | Visiergehäuse wahlweise `shell` folgen lassen, Klemmen und Schiene `anodized` |
| `trim` | blanke Läufe, Mündungen, Kanten (L* 40–74, C* ≤ 3) | skinfest als Metall; Abnutzung legt `trim` frei |
| `accent` | bunter Anteil 2–10 % (C* > 25) als Band, Block oder Schriftfeld | eine Akzentfarbe je Skin; Anteil als messbare Größe (C* > 25) im Bildtest |
| `energy` | Leuchtanzeigen, Kapseln und Linsen bleiben unter Shadern | skinfest |
| `decal` | Herstellerschrift auf fast allen Grundlacken, Emblem bei Elsie's Rifle skinfest | eigene Schrift/Marke als `decal`, Lage skinfest |
| Muster | aus dem Shader (Ros Arago IV) oder festes Bandlayout der Waffe, vom Shader nur gefärbt (Elsie's Rifle) | Musterlayout je Waffe als Maske, Farben aus dem Skin; Muster dürfen Paneele queren |

Zum Vergleich BASIC-Standard (Albedo): `shell` `#D8CCB4` (L* ≈ 82) gegen `graphite` `#2C2E33` (L* ≈ 19) entspricht der hellen-Schale-Gruppe
oben; `accent` `#E0651E` ist eine Signalfarbe wie die SUROS- und Häkke-Akzente.

## 8. Offen und nicht messbar

- **Vergleichsspiele fehlen:** Von 56 Vergleichsbeispielen ist keines mit Musterbefund bestätigt. Eine neue Sammlung braucht
  Inspektions- oder Skinvideos, in denen Waffe und Skinname am Bild stehen (Einblendung oder Menü).
- **Musterskala** (Fleckgröße relativ zur Waffenlänge) und **Schriftgröße** sind nicht gemessen.
- **Rauheit, Metallanteil, Albedo** sind aus Videobildern nicht messbar (Menülicht, Tonwertkurve, Kompression); Farbwerte hier sind
  Pixel im Inspektionsmenü.
- **Flächenanteile je Bauteil** (Schale/Rahmen/Metall in %) sind nicht segmentiert; die Helligkeitsklassen mischen Material und Schatten.
- **Shaderkanäle:** Wie viele Kanäle ein Destiny-Shader technisch hat, zeigt kein Video; nur die sichtbare Wirkung ist belegt.
