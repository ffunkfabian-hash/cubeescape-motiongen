# Waffenproportionen und Silhouetten – Verhältnisse je Klasse, was schlank macht

Referenzanalyse REF 0.15 „Sideview“ (25.10.2026) für die Waffenreihe **BASIC** (Projekt `cubeescape-ballon`). Nur Videospiele, keine
echten Waffen. Schwerpunkt Destiny 2 als Stilvorbild höchster Priorität – **nicht kopieren**, sondern Verhältnisse und Formhierarchie
verstehen. Hier stehen Beobachtungen und Zahlen; der Abschnitt [BASIC-Abweichungen](#5-basic-abweichungen) stellt Abweichungen
fest; Schlüsse und Startwerte setzt BASIC. Maschinenlesbare Fassung: [`data/proportionen.json`](../data/proportionen.json). Anschluss an REF 0.14
„Eyebox“ ([Visiere](visiere.md)), die fand, dass
„klobig“ vor allem von großen, hohen Gehäusen und Block-Sockeln kommt.

**Status:** **[C]** Zuarbeit einer Antigravity-Sitzung (24.10.2026) – Quelle in dieser Version per yt-dlp bzw. Seitenabruf bestätigt,
die Zahl selbst nicht nachgemessen; **[M]** am eigenen Bild nachgemessen (Abschnitt [6](#6-nachmessung-m)); **[S]** Bild außerhalb des Spiels
(Wiki, Händlerseite, Künstlerseite); **[O]** Sichtung ohne belastbare Zahl. Ohne Angabe gilt [C]. **Jede Zahl ist das Beispiel einer Waffe in einer
bestimmten Ansicht**, kein Klassenmittel und keine Generatorgrenze.

## 1. Quellen und Methode

**Umfang:** 6 Spiele, 52 Referenzwaffen – Destiny 2: 26 (22 vollständig normiert, davon ein Künstler-Render, dazu eine getrennte
Highpoly-Glefe und drei beschnittene Waffen nur gesichtet [O]), Destiny 1, Marathon (2026, Season 1), Halo Infinite und Apex Legends je 5,
Borderlands 3: 6. Dazu 17 BASIC-Konturen aus dem älteren Seitenbogen (vier mit Bauteilmaßen) und der Scout-Visierring im Zielen.
Grundlage: 17 YouTube-Videos und 12 Bildseiten; Videos und Bilder liegen nur im Cache
(`~/Library/Caches/CubeEscape/reference/visiere/gemini/proportions/`), nie im Repo.

**Quellenprüfung (REF 0.15):** Weil Antigravity in REF 0.14 bei sechs Spielen falsche Video-IDs, Kanäle und Titel nannte, ist hier jede
Quelle einzeln geprüft: alle **17 Videos** per yt-dlp (Kanal, Titel, Hochladedatum stimmen; der Titel nennt die Waffe bzw. die
Waffenreihe), alle **12 Bildseiten** per Seitenabruf (Titel nennt die Waffe; Lootlemon-Seitendaten bestätigt). **Keine Quelle
musste weggelassen werden.** Nicht verwendet (von Antigravity selbst ausgeschlossen): `X_ADv1HMwkg` (zeigt Halo 3), `E1_CBO6lX40` und
Apex `iNizXu2hl_0` (First-Person-Kontur ungeeignet), D1 `VNprDRKZxt8`/`MjugMsHa_0o` (Enden abgeschnitten), Marathon `K_cdXt075Dc`
(Season 2, kein Messgewinn).

| Quelle | Kanal / Urheber | Hochgeladen | Inhalt | Waffen hier |
|---|---|---|---|---|
| [`IG-GZ72Vbi0`](https://www.youtube.com/watch?v=IG-GZ72Vbi0) <a id="p-q-titan"></a> | Ultraclocked | 14.02.2020 | D2 Titan-Legendaries (SUROS), 1440p60 | Annual Skate, Solemn Hymn, Swift Ride, Tone Patrol, A Single Clap, First In Last Out, Nox Echo III, Dead Man Walking |
| [`73lGCT7yOtk`](https://www.youtube.com/watch?v=73lGCT7yOtk) | Ultraclocked | 25.01.2020 | D2 EDZ-Legendaries (Häkke), 1440p60 | Bad News, Eystein-D, Flash and Thunder, Minimum Distance |
| [`42zdQOVBAD0`](https://www.youtube.com/watch?v=42zdQOVBAD0) | Ultraclocked | 30.01.2020 | D2 Nessus-Legendaries (Omolon), 1440p60 | Seven-Six-Five, The Mornin' Comes, Uriel's Gift |
| Einzelvideos Ultraclocked | Ultraclocked | 2020–2023 | je eine Waffe, 2160p60 | Threaded Needle `uoTaCBMXcFk`, Extraordinary Rendition `Y5OLr0nbgSg`, Far Future `RXgRxHESqHQ`, Imperial Needle `dKNTDzi__Qo`, Eriana's Vow `KtfF9at8onE`, Shattered Cipher `DEM-8xg66R8`, Trinity Ghoul/Three Glowing Dawns `nr69dmj6_pA`, Eyes of Tomorrow `3gX1miw4ykY` |
| [`9GYXfRgzrlM`](https://www.youtube.com/watch?v=9GYXfRgzrlM) | Teez Monkey | 08.03.2022 | D2 Lubrae's Ruin (Glefe) | Lubrae's Ruin [O] |
| [`1ERmScNiOk4`](https://www.youtube.com/watch?v=1ERmScNiOk4) | DFP | 09.02.2023 | D2 Saint's Scout | Scout-Ring im Zielen (8:40) |
| [`MkkQa1OIpDk`](https://www.youtube.com/watch?v=MkkQa1OIpDk) | Jumping Puzzle | 05.03.2015 | Destiny 1 Scout-Vergleich, 720p30 | Another NITC, Válka SR3, Cryptic Dragon, Jigoku SR3, MIDA Multi-Tool |
| [`QxZAflLtJRQ`](https://www.youtube.com/watch?v=QxZAflLtJRQ) | soda | 04.06.2026 | Marathon (2026) Season 1, alle Waffen | ARES RG, V00 Zeus RG, Overrun AR, V22 Volt Thrower, Magnum MC |
| [`ernPc3eEBdQ`](https://www.youtube.com/watch?v=ernPc3eEBdQ) | Bolt Gaming | 05.10.2021 | Halo Infinite Weapon Bench, 1080p30 | MA40, MK50, BR75, VK78, S7 |
| [`Nwp4VJWUujY`](https://www.youtube.com/watch?v=Nwp4VJWUujY) | Agent Lomax | 02.10.2019 | Borderlands 3 Vladof-AR-Teile | Dobby Nozh Maslo |
| Matt Lichy (ArtStation) [S] | Modellierer der Waffen | unbekannt | [Gjallarhorn](https://mlichy911.artstation.com/projects/9BmKNy) (Künstler-Render), [Forthcoming Deviance](https://mlichy911.artstation.com/projects/0an5V4) (Highpoly, nicht Spielmodell) | 2 |
| Apex Legends Wiki [S] | wiki.gg | unbekannt | freigestellte Seitenbilder | P2020, RE-45 Auto, Wingman, Mozambique, Alternator |
| Lootlemon [S] | lootlemon.com | Seiten 21.09.2019, geändert 2024 | freigestellte Seitenbilder des gezeigten Exemplars | The Butcher, Faisor, Hellshock, Bitch, ASMD |

Zeitstempel je Waffe: `data/proportionen.json` › `weapons[].timestamp` (Menübilder meist bei 0,7 s nach Waffenstart; alle D2-Bilder
von Antigravity zeitgenau mit `ffmpeg -ss` nachgegriffen, nicht aus Bögen niedriger Rate).

**Messgrößen** (alle als Anteil von L): **L = 1** ist die sichtbare Ausdehnung entlang der projizierten Hauptachse (Gewehre: Laufachse,
Glefe/Schwert: Stange/Klinge), **H** quer dazu. **Bogen-Sonderfall:** L = Wurfarmspanne, H einschließlich Pfeil – nicht mit Gewehr-H/L
vergleichen. *Gehäuse* = Hauptgehäuse ohne Magazin, Griffe, Optik; *freier Lauf* = vor Gehäuse/Handschutz frei liegend (0 = keiner
sichtbar); *Magazin* = sichtbar herausragender Teil; *Visierhöhe* = Gehäuseoberkante bis Optikoberkante mit Sockel; *Visierlänge* =
zusammenhängende Optikbaugruppe. Winkel gegen die Achsennormale, nach hinten positiv. `null` = unbekannt oder verdeckt, **kein Nullmaß**.
`blocks` zählt große Formmassen von Hand (subjektiv); Farbanteile sind nicht segmentiert.

**Genauigkeit und Grenzen:** BASIC-Kontur ±0,01 L, Bauteile ±0,02 L; D1/D2/Halo ±0,02–0,03 L; Marathon und Teile von BL3
±0,03–0,05 L; Winkel ±5–10°. Die D2-Menüs sind **3/4-Projektionen** mit zusätzlicher, unkalibrierter Verzerrung von grob 10–25 %
(Flash and Thunder > 40 %). Ein schräges Bild wird durch Drehen der Bildebene nicht zur Seitenansicht; ohne Kamera-Kalibrierung gibt es
keine 3D-Rückrechnung. Die BASIC-Werte stammen aus einer **orthografischen** Seitenansicht – mit D2-Menüwerten vergleichbar nur als
Größenordnung, nicht auf die zweite Stelle.

## 2. Verhältnisse je Klasse – Destiny 2

Beobachtete Spannweiten der konkreten Ansichten, keine typischen Klassenwerte (je Klasse 1–3 Waffen). Keine Mittel über Pistolen,
Gewehre, Bögen und Stangenwaffen bilden.

| D2-Klasse | vermessen / gesichtet | Gehäuse | freier Lauf | Visierhöhe | Visierlänge | H/L | Grenze |
|---|---:|---:|---:|---:|---:|---:|---|
| **Automatikgewehr** <a id="p-d2-auto"></a> | 2/2 | 0,18–0,24 | 0,00–0,07 | 0,04–0,12 | 0,06–0,16 | 0,32–0,49 | Solemn Hymn, Uriel's Gift |
| **Impulsgewehr** <a id="p-d2-impuls"></a> | 2/2 | 0,24–0,25 | 0,23–0,26 | 0,07–0,08 | 0,07–0,11 | 0,43–0,48 | Eystein-D, Swift Ride |
| **Scoutgewehr** <a id="p-d2-scout"></a> | 2/2 | 0,16–0,22 | 0,00–0,39 | 0,02–0,04 | 0,10–0,16 | 0,32–0,51 | Tone Patrol (Visierhöhe [M]), Seven-Six-Five |
| **Handfeuerwaffe** <a id="p-d2-hc"></a> | 3/3 | 0,21–0,27 | 0,00 | 0,13 | 0,37 | 0,52–0,61 | Visierwerte nur Eriana's Vow (Exot mit Zielfernrohr) |
| **Sidearm** <a id="p-d2-sidearm"></a> | 2/2 | 0,33 | 0,00 | 0,03 | 0,08 | 0,74–0,83 | Dead Man Walking, Minimum Distance |
| **Maschinenpistole** <a id="p-d2-mp"></a> | 1/1 | 0,14 | 0,00 | 0,06 | 0,05 | 0,50 [M] | Extraordinary Rendition, Magazin 0,30 [M] |
| **Schrotflinte** <a id="p-d2-schrot"></a> | 1/1 | 0,16 | 0,00 | 0,02 | 0,08 | 0,29 | First In, Last Out |
| **Scharfschützengewehr** <a id="p-d2-sniper"></a> | 3/3 | 0,07–0,13 | 0,00–0,48 | 0,05–0,11 | 0,17–0,22 | 0,17–0,32 | Far Future 0,17 [C], nachgemessen 0,18 [M]; A Single Clap, The Mornin' Comes |
| **Fusionsgewehr** <a id="p-d2-fusion"></a> | 1/1 | 0,19 | 0,00 | 0,03 | 0,18 | 0,49 | Nox Echo III, Magazin geöffnet |
| **Lineares Fusionsgewehr** <a id="p-d2-lfr"></a> | 1/1 | 0,17 | 0,00 | 0,11 | 0,16 | 0,43 | Threaded Needle |
| **Bogen** <a id="p-d2-bogen"></a> | 1/2 | – | – | – | – | 0,73 | Wurfarm-L; Trinity Ghoul mit Ornament, Imperial Needle beschnitten [O] |
| **Granatwerfer** <a id="p-d2-gl"></a> | 1/1 | 0,21 | 0,36 | 0,25 | 0,09 | 0,72 | Flash and Thunder, stark frontal – kein Formmaß |
| **Raketenwerfer** <a id="p-d2-rl"></a> | 1/2 | 0,36 | – | – | – | 0,60 | Gjallarhorn (Künstler-Render [S]); Eyes of Tomorrow beschnitten [O] |
| **Maschinengewehr** <a id="p-d2-mg"></a> | 1/1 | 0,13 | 0,10 | 0,06 | 0,09 | 0,30 | Shattered Cipher, H enthält Zweibein |
| **Glefe** <a id="p-d2-glefe"></a> | 0/2 | – | – | – | – | (0,12) | Lubrae's Ruin beschnitten [O]; 0,12 nur Highpoly Forthcoming Deviance [S], nicht Spielmodell; **neun Glefen und acht Schwerter an Manifestbildern 0.29: [nahkampf.md › 2–3](nahkampf.md#3-form-destiny-glefen-manifestbilder)** (H/L 0,09–0,12) |

**Vergleichsanker außerhalb Destiny 2** (je ein Beispiel; ganze Liste in `data/proportionen.json`):

| Spiel / Waffe | Gehäuse | freier Lauf | Visierhöhe | H/L | Grenze |
|---|---:|---:|---:|---:|---|
| **Destiny 1 · MIDA Multi-Tool** <a id="p-d1-mida"></a> | 0,20 | 0,00 | 0,14 | 0,65 | kurzer Bullpup, 3/4; D1-Reihe nur Scouts ([4:45](https://www.youtube.com/watch?v=MkkQa1OIpDk&t=285s)) |
| **Marathon · Overrun AR** <a id="p-marathon-overrun"></a> | 0,12 | 0,00 | 0,05 | 0,28 | kleine Inventarprojektion ([2:42](https://www.youtube.com/watch?v=QxZAflLtJRQ&t=162s)) |
| **Halo Infinite · S7 Sniper** <a id="p-halo-s7"></a> | 0,07 | 0,48 | 0,09 | 0,22 [M] | fast reine Seitenansicht ([2:40](https://www.youtube.com/watch?v=ernPc3eEBdQ&t=160s)) |
| **Apex · P2020** <a id="p-apex-p2020"></a> | 0,24 | 0,00 | 0,01 | 0,74 | Wiki-Bild [S] ([Seite](https://apexlegends.wiki.gg/wiki/P2020)) |
| **Borderlands 3 · Hellshock** <a id="p-bl3-hellshock"></a> | 0,36 | 0,00 | 0,08 | 0,58 | Lootlemon-Bild [S], gezeigter Teilestand ([Seite](https://www.lootlemon.com/weapon/hellshock-bl3)) |

## 3. Was schlank macht – was klobig macht

Gestalterische Ableitungen aus den genannten Bildern, keine kontrollierte Wahrnehmungsstudie. Getrennt wird messbare Kontur von Wirkung.

1. **Längsstaffelung statt gleich hoher Front** <a id="p-schlank-staffelung"></a> – Far Future: Gehäuse 0,07, freier Lauf 0,46–0,48 [M],
   H/L 0,18 [M]; S7 zeigt denselben Wechsel dünn–breit–dünn. Nicht jede Verkleidung muss weg: A Single Clap bleibt mit 0,13 freiem Lauf
   bei H/L 0,23. ([Far Future](https://www.youtube.com/watch?v=RXgRxHESqHQ) 0:00,7, [S7](https://www.youtube.com/watch?v=ernPc3eEBdQ&t=160s), [A Single Clap](https://www.youtube.com/watch?v=IG-GZ72Vbi0) 0:00,7)
2. **Gehäusehöhe und Gesamthöhe getrennt behandeln** <a id="p-schlank-magazin"></a> – Extraordinary Rendition: Gehäuse nur 0,14, aber
   Magazin 0,29–0,32 [M] und H/L 0,50 [M]. Ein langes Magazin macht die Silhouette hoch, ohne den Gehäuseblock zu verdicken.
   ([Video](https://www.youtube.com/watch?v=Y5OLr0nbgSg) 0:00,7)
3. **Optikoberkante niedrig, Teil der oberen Linie** <a id="p-schlank-optik"></a> – Tone Patrol trägt den Visierblock nur 0,013–0,019 [M]
   über dem Gehäuse, Eystein-D 0,07, Swift Ride 0,08. Wegen verschiedener Perspektiven keine allgemeine Schwelle.
   ([Tone Patrol](https://www.youtube.com/watch?v=IG-GZ72Vbi0&t=375s) 6:15,7, [Eystein-D](https://www.youtube.com/watch?v=73lGCT7yOtk&t=220s) 3:40,7, [Swift Ride](https://www.youtube.com/watch?v=IG-GZ72Vbi0&t=350s) 5:50,7)
4. **Große Öffnung mit schmalem Außenrand** <a id="p-schlank-ring"></a> – Scout-Ring im Zielen: Destiny außen/Öffnung 1,28 (REF 0.14
   unabhängig 1,30 [M]), BASIC 1,76–1,91 [M]. Der breite Rand ist hier der stärkere konkrete Klobigkeitsbeleg als die Waffenlänge
   (Abschnitt [5.2](#52-scout-visierring-im-zielen)). ([DFP](https://www.youtube.com/watch?v=1ERmScNiOk4&t=520s) 8:40)
5. **Negativräume als echte Unterbrechung der Masse** <a id="p-schlank-negativ"></a> – Seven-Six-Five mit offenem hinterem Schaft, Far
   Future mit Skelettschaft, Halo VK78 mit großer Schaftöffnung: eine große äußere Box mit wenig geschlossener Fläche.
   ([Seven-Six-Five](https://www.youtube.com/watch?v=42zdQOVBAD0&t=222s) 3:42,7, [VK78](https://www.youtube.com/watch?v=ernPc3eEBdQ&t=110s) 1:50)
6. **Große Farbflächen ordnen, Detail in Zonen** <a id="p-schlank-zonen"></a> – Solemn Hymn und Tone Patrol: breite zusammenhängende
   helle Schalen über dunkler Unterseite; Eystein-D bündelt Kleinteile an Fensterband und Unterseite. Wenige lesbare Massen statt
   gleichmäßig verteilter Rillen. ([Solemn Hymn](https://www.youtube.com/watch?v=IG-GZ72Vbi0&t=315s) 5:15,7)
7. **Erst die große Kontur, dann Fasen und Rundungen** – Dead Man Walking und Minimum Distance sind trotz runder Oberflächen mit
   Gehäuse 0,33 kompakte Pistolen: Rundung macht nicht automatisch schlank, Kante nicht automatisch klobig.
   ([Dead Man Walking](https://www.youtube.com/watch?v=IG-GZ72Vbi0&t=95s) 1:35,7, [Minimum Distance](https://www.youtube.com/watch?v=73lGCT7yOtk&t=408s) 6:48,7)
8. **Zusatzarme und Unterbauten getrennt prüfen** – Uriel's Gift: Gehäuse 0,18, aber H/L 0,49; Solemn Hymn: Gehäuse höher (0,24),
   Gesamtprojektion niedriger (0,32). Die Frontarme erklären einen Teil davon (keine kausale Kontrollmessung).
   ([Uriel's Gift](https://www.youtube.com/watch?v=42zdQOVBAD0&t=432s) 7:12,7)
9. **Klasse und Ausrüstung bestimmen den Maßstab** – Apex P2020 und RE-45 haben je Gehäuse ≈ 0,24, RE-45 mit Reflexvisier und langem
   Magazin aber H/L 0,84 statt 0,74. Pistolen- und MP-Höhen nicht an Langwaffen-H/L messen. ([P2020](https://apexlegends.wiki.gg/wiki/P2020), [RE-45](https://apexlegends.wiki.gg/wiki/RE-45_Auto) [S])
10. **Bewusste Masse braucht eine klare Hauptform** <a id="p-schlank-masse"></a> – Hellshock (Frontblock 0,36) und Gjallarhorn (großes
    Startrohr, hoher Aufbau) sind massive Gegenbeispiele. „Mehr Destiny“ heißt nicht pauschal „alles dünner“, sondern eine erkennbare
    Formhierarchie der gewählten Familie. ([Hellshock](https://www.lootlemon.com/weapon/hellshock-bl3), [Gjallarhorn](https://mlichy911.artstation.com/projects/9BmKNy) [S])

## 4. Formbefund BASIC (Bildstand 24.10.2026)

Im älteren Seitenbogen (cubeescape-ballon, `contact_side_scaled.png`, 1992 × 3050 px, 24.10.2026 12:47, Maßstab 400 px/m, SHA-256
`1952bbcc…`) wiederholen sich helle, annähernd gleich hohe Gehäuse mit dunklen Rechteckpaneelen; freiliegende Verbindungen und Läufe
staffeln die Silhouette. Die hellen Dreiecksschäfte dort sind vollflächig, keine Skelettschäfte. Der spätere Scout in
`sight_options.png` (24.10.2026 19:51, SHA-256 `adfad4db…`) zeigt dagegen einen offenen Schaftrahmen – die beiden Bildstände sind nicht
dieselbe Geometrie. **Beide Stände sind älter als der aktuelle BASIC-Generator**; die Zahlen unten sind Bildwerte, keine Generatorparameter.
Jede Waffe ist auf ihre eigene Länge normiert (Kontur ±1–3 px).

| BASIC | Klasse | L (px) | H/L | Gehäuse | freier Lauf | Visierhöhe | Visierlänge |
|---|---|---:|---:|---:|---:|---:|---:|
| **BASIC-01** <a id="p-basic-01"></a> | Auto | 363 | 0,300 | 0,116 | 0,193 | 0,055 | 0,063 |
| **BASIC-02** <a id="p-basic-02"></a> | Impuls | 320 | 0,319 | 0,128 | 0,119 | 0,066 | 0,066 |
| **BASIC-03** <a id="p-basic-03"></a> | Scout | 396 | 0,260 (0,263–0,265 [M]) | 0,098 | 0,205 | 0,063 | 0,164 |
| BASIC-04 | Handfeuerwaffe | 118 | 0,568 | – | – | – | – |
| BASIC-05 | Sidearm | 89 | 0,697 | – | – | – | – |
| **BASIC-06** <a id="p-basic-06"></a> | MP | 223 | 0,525 | 0,135 | 0,112 | 0,085 | 0,094 |
| BASIC-07 | Bogen | 414 | 0,669 | – | – | – | – |
| BASIC-08 | Schrot | 353 | 0,280 | – | – | – | – |
| BASIC-09 | Scharfschütze | 458 | 0,240 | – | – | – | – |
| BASIC-10 | Fusion | 322 | 0,320 | – | – | – | – |
| BASIC-11 | Lineare Fusion | 488 | 0,234 | – | – | – | – |
| BASIC-12 | Spur | 350 | 0,289 | – | – | – | – |
| BASIC-13 | Granatwerfer | 258 | 0,403 | – | – | – | – |
| BASIC-14 | Raketenwerfer | 379 | 0,314 | – | – | – | – |
| BASIC-15 | MG | 431 | 0,267 | – | – | – | – |
| BASIC-16 | Schwert | 477 | 0,067 | – | – | – | – |
| BASIC-17 | Glefe | 570 | 0,111 | – | – | – | – |

Bauteile der vier näher vermessenen Waffen (Anteil von L; Winkel ±5°): BASIC-01 Magazin 0,121/−10°, Griff 0,118/20°, Schaft 0,187
(Höhe 0,129); BASIC-02 Magazin 0,109/0°, Griff 0,134/20°, Schaft 0,237 (0,138); BASIC-03 Magazin 0,063/−5°, Griff 0,111/19°, Schaft
0,184 (0,106); BASIC-06 Magazin 0,117/8°, Griff 0,193/8°, Schaft 0,224 (0,211). Bogen BASIC-07 mit derselben Sonderachse wie Trinity
Ghoul (Wurfarmspanne 414 px, H mit Pfeil 277 px); entlang der Schussachse wäre H/L 1,495 – nicht mit dem D2-Bogenwert vergleichen.

## 5. BASIC-Abweichungen

### 5.1 Ganze Waffen gegen Destiny 2

| Vergleich | BASIC (orthografisch) | D2 (3/4-Menü) | Einordnung |
|---|---|---|---|
| Auto-Gehäuse | BASIC-01 0,116 | [Uriel's Gift / Solemn Hymn](#p-d2-auto) 0,18–0,24 | kein Beleg für einen pauschal zu hohen BASIC-Körper |
| Impuls-Gehäuse | BASIC-02 0,128 | [Eystein-D / Swift Ride](#p-d2-impuls) 0,24–0,25 | BASIC ist eher ein flacher, langer Mittelblock |
| Scout-Gehäuse | BASIC-03 0,098 | [Tone Patrol / Seven-Six-Five](#p-d2-scout) 0,16–0,22 | Unterschied liegt in Gliederung und Optik, nicht in der Dicke |
| **Scout-Visier über Gehäuse** | BASIC-03 **0,063**, Länge 0,164 | D2-Scouts **0,02–0,04** (Tone Patrol 0,013–0,019 [M]), Länge 0,10–0,16 | Aufbau ist höher; Länge am oberen Ende |
| MP-Kontur | BASIC-06 H/L 0,525, Gehäuse 0,135 | [Extraordinary Rendition](#p-d2-mp) 0,50 [M], 0,14 | ähnliche Quotienten, kein Massefehler |
| Sniper / LFR | BASIC-09 0,240, BASIC-11 0,234 | [D2-Sniper](#p-d2-sniper) 0,17–0,32, [Threaded Needle](#p-d2-lfr) 0,43 | Käfig insgesamt flach; ein großer Optikring kann trotzdem einzeln klobig wirken |
| Glefe | BASIC-17 0,111 | (Highpoly 0,12) | Gleichklang beweist keine Formgleichheit im Spiel |

**Befund:** Die BASIC-Seitenbilder belegen **kein generell zu hohes Gewehrgehäuse** – die Körper sind sogar flacher als die
D2-Beispiele (Vorbehalt Projektion). Konkret abweichend sind der **Visieraufbau** (Scout 0,063 gegen 0,02–0,04) und vor allem der
**Visierring im Zielen** (5.2). Das deckt sich mit REF 0.14: „klobig“ kommt von Größe und Höhe von Visiergehäuse und Sockel.

### 5.2 Scout-Visierring im Zielen

Quelle `sight_options.png` (s. o.), BASIC-Kachel x 655 / y 54, Destiny-Kachel x 1300 / y 0 (DFP 8:40), je 640 × 360 px, gemessen an der
waagerechten Öffnungsmitte (±4 px).

| Maß | BASIC Scout | Destiny-Referenz |
|---|---:|---:|
| Außenbreite Ringgehäuse | 328 px = 51,3 % B (326,5 px [M]) | 169 px = 26,4 % B |
| Lichte Öffnung | 181 px = 28,3 % B (171–186 px [M], je nach Innenfase) | 132 px = 20,6 % B |
| **Außen / Öffnung** <a id="p-ring-verhaeltnis"></a> | **1,81** (1,76–1,91 [M]) | **1,28** ([REF 0.14](visiere.md#v-d2-scout) bei 4:04,5: 1,30 [M]) |
| Randbreite waagerecht | ≈ 73,5 px | ≈ 18,5 px |
| Ringflächenanteil (Kreis genähert) | ≈ 69,5 % | ≈ 39 % |

Bei gleicher BASIC-Öffnung (181 px) ergäbe das Destiny-Verhältnis außen ≈ 232 px statt 328 px – **rund 29 % weniger Außenbreite**;
umgekehrt ist der BASIC-Ring bei gleicher Öffnung rund 42 % größer (verschiedene Bezugsgrößen). Wegen anderer Optik, Perspektive und
unbekanntem FOV ist das ein Entwurfsvergleich, keine 3D-Skalierungsanweisung. Die Kreisflächenrechnung ist nur ein Anschauungswert, nicht
die verdeckte Bildfläche. Heller breiter Ring und dunkle Innenfase verstärken den Eindruck zusätzlich (nicht isoliert geprüft).

**Augenabstand ist ein anderer Hebel:** Die Beschriftungen in `sight_examples.png` nennen für 70/90/110 mm Öffnungen von 29/22/18 % B
(BASIC-01), 32/25/20 % (BASIC-02), 40/31/26 % (Scout) – Werte der lokalen Darstellung, nicht nachgeprüft. Mehr Augenabstand verkleinert
das ganze Visier im Bild, ändert aber nicht das Verhältnis außen/Öffnung. Kompakte Prisma-/Flachkasten-Varianten zeigten im Zielen
starke Tunnelansichten: kompakte Außenform garantiert keinen guten Durchblick (eigener Geometrie-/Kameraauftrag).

### 5.3 Abweichungen in Kürze

Nur Befunde aus 5.1 und 5.2; Schlüsse und Startwerte setzt BASIC (`cubeescape-ballon`), die Übergabe läuft über den Briefkasten.

| Merkmal | BASIC | Destiny-Beispiele | Befund |
|---|---|---|---|
| **Scout-Ring außen/Öffnung** <a id="p-abw-ring"></a> | 1,76–1,91 [M] | 1,28–1,30 [M] | Abweichung; Destiny-Verhältnis bei gleicher Öffnung ≈ 29 % weniger Außenbreite |
| **Scout-Visier über Gehäuse** <a id="p-abw-visier"></a> | 0,063 | 0,02–0,04 (Tone Patrol 0,013–0,019 [M]) | Abweichung (Vorbehalt Projektion) |
| **Gewehrgehäuse** <a id="p-abw-gehaeuse"></a> | 0,10–0,13 | 0,16–0,25 | keine Abweichung nach oben; BASIC flacher |
| **Formgliederung** <a id="p-abw-form"></a> | gleich hohe helle Gehäuse mit dunklen Rechteckpaneelen, Vollschäfte (älterer Bogen) | Längsstaffelung, Negativräume, Detail in Zonen, eine Hauptform je Familie ([3](#3-was-schlank-macht--was-klobig-macht)) | Unterschied in der Gliederung, nicht in der Dicke |
| **Kurzwaffen, MP, Bogen** | H/L 0,57–0,70, MP 0,525, Bogen 0,669 | 0,52–0,83, MP 0,50, Bogen 0,73 | keine Abweichung; nur innerhalb der Klasse vergleichen |

## 6. Nachmessung [M]

Sechs Werte am eigenen Einzelbild mit Pixelraster nachgemessen (25.10.2026; `ffmpeg -ss` am Originalvideo bzw. an der Originaldatei,
Achse und Kanten selbst gesetzt, nicht aus den Antigravity-Markierungen übernommen). Alle innerhalb der angegebenen Toleranz.

| Wert | Antigravity [C] | eigene Messung [M] | Bild / Bemerkung |
|---|---:|---:|---|
| **Far Future H/L, freier Lauf** <a id="p-m-farfuture"></a> | 0,17 / 0,48 | 0,18 (0,176–0,185) / 0,46–0,47 | [`RXgRxHESqHQ`](https://www.youtube.com/watch?v=RXgRxHESqHQ) 0,7 s, 1080p; Laufachse −8,9°; Magazin-/Griffunterkante teils vom Menü verdeckt |
| **Tone Patrol Visierhöhe** <a id="p-m-tonepatrol"></a> | 0,02 | 0,013–0,019 | [`IG-GZ72Vbi0`](https://www.youtube.com/watch?v=IG-GZ72Vbi0&t=375s) 375,7 s, 720p; Gehäusekante neben dem Visierblock ±3 px |
| **Extraordinary Rendition Magazin, H/L** <a id="p-m-extrarend"></a> | 0,30 / 0,50 | 0,29–0,32 / 0,50 | [`Y5OLr0nbgSg`](https://www.youtube.com/watch?v=Y5OLr0nbgSg) 0,7 s, 1080p; Achse obere Schiene −12,8°; Magazin je nach Gehäusekante am Schacht |
| **Halo S7 H/L** <a id="p-m-s7"></a> | 0,23 | 0,22 (0,218 ohne, 0,227 mit Drahtbügel) | [`ernPc3eEBdQ`](https://www.youtube.com/watch?v=ernPc3eEBdQ&t=160s) 160 s, eigener 1080p-Abruf (Antigravity: 360p) |
| **BASIC-Scout-Ring außen/Öffnung** <a id="p-m-ring"></a> | 1,81 | 1,76–1,91 (außen 326,5 px, Öffnung 171–186 px) | `sight_options.png`, Helligkeitsprofil der Zeilen 178/185; Spanne = Innenkante mit/ohne dunkle Innenfase |
| **BASIC-03 H/L** <a id="p-m-basic03"></a> | 0,260 | 0,263–0,265 (397–399 × 105 px) | `contact_side_scaled.png`, Rahmen gegen Hintergrund (Trim 8–15 %) |

## 7. Offen und nicht messbar

- **Glefe:** Lubrae's Ruin ohne L (Stangenende abgeschnitten), Forthcoming Deviance nur als Highpoly; für einen Spielwert fehlt eine
  vollständige Seitenansicht (0.29: Manifestbilder in 3/4-Ansicht schließen die Lücke als Größenordnung, [nahkampf.md](nahkampf.md#3-form-destiny-glefen-manifestbilder)). Ebenso beschnitten: Imperial Needle (oben), Eyes of Tomorrow (hinten).
- **Stichprobe:** D1 nur Scouts (drei SR3-Verwandte), Apex nur kurze Waffen, Marathon nur Season 1, Halo nur die frühe Waffenbank
  (05.10.2021) – keine Reihe ist für ihr Spiel repräsentativ.
- **Farb- und Detailmaße:** Akzentanteile nicht segmentiert (überall `null`); Schrauben, Rillen, Leuchtteile, Paneele und `blocks`
  sind Sichtbefunde. BL3-Cyan ist Auswahlhervorhebung, kein Material.
- **Besondere Zustände:** Nox Echo III mit geöffnetem Magazin, Shattered Cipher mit Zweibein in H, BL3-Bajonette verlängern L – nicht
  ungefiltert in Grenzen übernehmen.
- **Keine 3D-Rückrechnung, kein Weltzoom/FOV:** Ansichten ohne Kalibrierung liefern Bildproportionen; der Ringvergleich normiert nur die
  sichtbare Öffnung. Eine echte Seiten-Orthoansicht der D2-Modelle (z. B. Inspektion mit fester Kamera) würde die 3/4-Verzerrung beseitigen.
