# Changelog

## 0.29.0 „Bladework“ – 2026-10-28

- Neue Referenzanalyse [Schwert und Glefe](docs/nahkampf.md) mit `data/nahkampf.json` für BALLON Paket 7: Form an 17 Destiny-Manifestbildern (8 Schwerter: Klinge 0,64–0,76 L, H/L 0,07–0,10 schlank bzw. 0,21–0,33 breit; 9 Glefen mit gemeinsamem Gerüst: Kragen 0,30 L, Kopf ab 0,52–0,55 L, H/L 0,09–0,12), Destiny-Schulteransicht (Einstieg 9 + 20 Bilder, Ausstieg 6 Bilder, Figur 42 % H links der Mitte, Angriffe 14–58 Bilder, Block ≤ 9 Bilder), Ego-Schwerter in Dark Messiah, Chivalry 2, Halo Infinite und Ghostrunner (Ruhe rechts/unten, Mitte 1–4 Bilder verdeckt) und die Glefe in Ego (Hüfte, Schuss mit Projektil an der Bildmitte, Kadenz 51–63 Bilder, Schlag 8 + 10 Bilder, Schild ein 10–11 Bilder, Nachladen 3,07–3,50 s, kein ADS). Fünf Messzeilen (`z-nk-…`) und Methode 27 in destiny2.md, fünf Einträge in `data/clips.json`, Datentest.
- Befund (Beobachtung, entschieden wird in BALLON): Bungie begründet die Schulteransicht der Schwerter mit Schlägen außerhalb des Ego-Sichtfelds und hält die Glefe bewusst in Ego (Developer Insights, 14.02.2022); Entscheidungsvorlage A/B/C mit Empfehlung **B** (Schwert in Ego nach Vorbildern).
- Abnahme: drei Unteragenten (zwei Opus, ein Sonnet; Nutzerwunsch über Sightline), 8/8 nachgemessene Zahlen bestätigt, 3/3 Stimmen-URLs, Vexcalibur-Bestand bestätigt; offen u. a. Skyrim ohne Mods, Winkel-FOV der Schulterkamera, Glefen-Fadenkreuzlage. [Bericht](docs/versions/0.md#0290-bladework--2026-10-28).

## 0.28.0 „Pullzone“ – 2026-10-25

- Neue Referenzanalyse [Zielhilfe und Eingabe](docs/zielhilfe.md) mit `data/zielhilfe.json`: 35 Beispiele aus fünf Spielen (Destiny 2 14, Halo Infinite 6, Apex Legends 7, Call of Duty 5, VALORANT 3; sechs Video- und 29 Dokumentarbefunde) aus fünf Videos und 21 Entwicklerquellen (Codex-Mac, Ego-Bewegung R2, Thema Zielhilfe). Eine Messzeile in `docs/destiny2.md` › 2 (Anker `z-zh-drewsky`), Methode 26, fünf Einträge in `data/clips.json`, Querverweis in waffenwerte.md.
- Befund (Beobachtung, Schlüsse in BASIC/Cube Escape): Schusskorrektur und Kamerahilfe sind getrennte Mechaniken; es gibt **keine gemessene Zielhilfe-Stärke** (die drei [M]-Zeilen zeigen nur Bildlagen), ein AA-Stat hat keine Formel im Manifest, Entwicklerzahlen sind historisch oder relativ; CoD BO7 koppelt die volle Rotational-AA an aktive Verfolgung (Launch-Abzug 35 %, später 25 %).
- Abnahme: 5/5 Videos per yt-dlp, 21/21 Entwicklerquellen (7 nur per Archiv), 5/7 Spielerbeiträge, 11 Nachmessungen an 8 Zahlenpaaren; übernommen 29, **korrigiert 6** (Halo H01: zweiter Bildwert widerlegt, (95,50) gegen (51,51)), kopierte Bewertungsfelder und „alle Threads gelesen“ verworfen. [Bericht](docs/versions/0.md#0280-pullzone--2026-10-25).

## 0.27.0 „Statline“ – 2026-10-25

- Neue Referenzanalyse [Waffenwerte](docs/waffenwerte.md) mit `data/waffenwerte.json`: 113 Destiny-2-Manifestgruppen (Kadenz, Magazin, sechs Stats) als unbewertete Rohdaten, das historische Schadens- und Handlingmodell von Patch 8.2.6 (43 Rahmen, 16 Kennlinien, veraltet) und zwölf Beispiele aus fünf Spielen (Destiny 2, Halo Infinite, Apex Legends, Valorant, Warzone; drei Video-, neun Text-/API-Beispiele; Codex-Mac, Ego-Bewegung R2, Thema Waffenwerte). Eine Messzeile in `docs/destiny2.md` › 2 (Anker `z-ww-karte`), Methode 25, drei Einträge in `data/clips.json`, Notiz in apex.md.
- Befund (Beobachtung, Schlüsse in BASIC/Cube Escape): Menükarte (ausgerüstet, 2021) und Manifest-Basis (2026) liegen bei Chroma Rush und Gridskipper 1–25 Stat-Punkte auseinander; Stat-Zahlen sind keine Einheiten; Schwellen hängen am Entfernungsband (Phantom > 20 m, Sheriff > 30 m); ideale TTK ist eine Rechnung ab dem ersten Treffer; die Valorant-Ghost-Karte nannte 2020 Magazin 15 (API 2026: 13).
- Abnahme: 3/3 Videos per yt-dlp, 113/113 Manifestgruppen, 43/43 Modellzeilen und 9/9 Vergleichszeilen nachgerechnet, 4 Nachmessungen an 2 Balkenzahlen; übernommen 122, **korrigiert 3** (Guardian-Deutung gestrichen, Halo-Status B + Rechnung), kopierte Bewertungsfelder und „wiederkehrend“ (C1/C2) verworfen. [Bericht](docs/versions/0.md#0270-statline--2026-10-25).

## 0.26.0 „Swapline“ – 2026-10-25

- Neue Referenzanalyse [Ziehen, Wegstecken und Waffenwechsel](docs/wechsel.md) mit `data/wechsel.json`: 29 Beispiele aus Destiny 2 (14), Marathon (4), Apex (3, Erstaufheben), Valorant (3), Halo (2, nur Form) und Titanfall 2 (3, nur Form) aus 14 Videos (Codex-Mac, Ego-Bewegung Thema 2) – Wegstecken, leere Sicht, Ziehen bis zur ersten hüftähnlichen Passage und Ruhe in Bildern. Fünf Messzeilen in `docs/destiny2.md` › 2 (Anker `z-sw-…`), Methode 24, 14 Einträge in `data/clips.json`, Notizen in apex.md, titanfall2.md und auswertung.md.
- Befund (Beobachtung, Schlüsse in BASIC/Cube Escape): Destiny-Wechsel zeigen Wegstecken 5–16 Bilder (vier Fälle) und leere Sicht 4–18 Bilder (0,07–0,30 s); Ziehen nach Menüschnitt (7–24 Bilder) ist kein Wechsel; die erste hüftähnliche Passage ist kein Endpunkt (in drei gemessenen Fällen Überschwingen 8–10 pp); Apex-Erstaufheben ≠ Slotwechsel.
- Abnahme: 14/14 Videos per yt-dlp, 57 Zahlen von Prüfern und 4 vom Koordinator am Bild nachgemessen; übernommen 24, **korrigiert 5** (Raketenwerfer-Marker f73/f86 → f77/f88–89 widerlegt, Leerphase und Hüftmarker als Bereiche, Halo-Zeiten gestrichen), kopierte Bewertungsfelder verworfen; **Bestandskorrektur:** „Waffe ganz weg“ 2,334 s → 2,284 s. [Bericht](docs/versions/0.md#0260-swapline--2026-10-25).

## 0.25.0 „Reload“ – 2026-10-25

- Neue Referenzanalyse [Nachladen](docs/nachladen.md) mit `data/nachladen.json`: 23 Beispiele aus Destiny 2 (13), Marathon (3), Apex (3) und Titanfall 2 (4) aus 13 Videos (Codex-Mac, Ego-Bewegung Thema 3) – Marker von Beginn bis Hüfte und Ruhe, Munitionsanzeige (HUD) gegen sichtbare Rückkehr, Leer-/Taktisch-Paare. Vier Messzeilen in `docs/destiny2.md` › 2 (Anker `z-rl-…`), Methode 23, 13 Einträge in `data/clips.json`, Notizen in apex.md, titanfall2.md und auswertung.md (V12).
- Befund (Beobachtung, Schlüsse in BASIC/Cube Escape): die Munitionsanzeige wechselt in allen 12 Fällen mit HUD **vor** dem Hüftmarker (0,15–1,22 s), nie deckungsgleich; Hüfte und ruhig liegen in den 15 Einträgen mit beiden Markern 0,03–0,45 s auseinander (Destiny-Magazin-/Trommel-/Gurtaufnahmen 0,12–0,45 s, Titanfall 2/Apex 0,07–0,20 s; Baligant 2 und Shock and Awe 3 Bilder, an der Grenze der ±2-Bilder-Differenz); Titanfall CAR leer 2,27 s gegen taktisch 1,85 s, P2016 ohne Unterschied.
- Abnahme: 13/13 Videos per yt-dlp, 27 Nachmessungen am Bild an 23 verschiedenen Zahlen (22 Prüfer, 5 Koordinator, 4 doppelt); übernommen 20, **korrigiert 3** (Apex-RE-45-Hüfte widerlegt: ≈ 19,6–19,85 s statt 19,15 s; zwei Zeitfelder), die je Eintrag kopierten Bewertungsfelder verworfen. [Bericht](docs/versions/0.md#0250-reload--2026-10-25).

## 0.24.0 „Glidepath“ – 2026-10-25

- **Visier-Anflug, Fadenkreuz und Sprint je Waffentyp in Destiny 2** für den BALLON-Prototyp (17 BASIC-Standardtypen): Tabellen je Typ in [destiny2.md › 3](docs/destiny2.md#s-glidepath), 35 Messzeilen (`z-gp-…`), Methode „Glidepath“, Vergleich in [auswertung.md](docs/auswertung.md#ballon-visier), Einträge in `data/clips.json`.
- Befund: **kein Überschwingen in 11 gemessenen Typen** (Bogen, Scharfschütze, kurze Fusion nur ±3–4 pp, Scout übertragen); in verfolgten Fällen monoton mit Abbremsen über 3–9 Bilder, Dauer 6–20 Bilder; Weltzoom endet meist mit dem Modell (drei Ausnahmen). Hüft-Fadenkreuz an 8 Typen gemessen, beim ADS-Beginn in einem Bild weg (Automatik, MP); Trefferanzeige rotes X 3,0–3,6 % H. Sprintfrequenz in keinem eigenen Clip mit 4 Zyklen belegt. Acht Widersprüche zum Bestand gelistet, nicht entschieden. [Bericht](docs/versions/0.md#0240-glidepath--2026-10-25).

## 0.23.0 „Stride“ – 2026-10-25

- **Sprint-Wippen in Destiny 2 gemessen** ([Methode 21](docs/destiny2.md#methode-21), Tabelle [Sprint-Wippen je Typ](docs/destiny2.md#s-sprint-wippen)): Automatikgewehr (Datto, Last Wish, 15.09.2018) und Handfeuerwaffe (Crystic, 24.08.2022) wippen vertikal mit **0,317 s (3,16 Hz)** über 4 bzw. 9 (5 + 4) Zyklen, seitlich mit **≈ 0,63 s (≈ 1,6 Hz, je 2 Zyklen, vorläufig)**; Hochpunkte an den Seitenumkehren (U-Bogen); Hub ≈ 10–11 % H / 13 % B (Automatik, Visier) und ≈ 13 % H / 4 % B (Handfeuerwaffe, Griff); Rollen ≈ 7° (Automatik); kein Kamerawippen nachweisbar. Ersetzt die unbestätigte 30/s-Lesung 2,5–3 Hz; PandaPaxxy an der 60/s-Datei nur Teilbeleg (2 Zyklen).
- Zwei Messzeilen (`z-st-…`), PandaPaxxy-Zeile nachgemessen, Steckbriefe Automatik/Handfeuerwaffe, Bewegungsabsatz, Vergleich mit dem BALLON-Prototyp in [auswertung.md](docs/auswertung.md#ballon-sprint), drei Einträge in `data/clips.json`, eine Lehre. Ein-/Austritt nicht isoliert; übrige Typen in REF 0.24 „Glidepath“. [Bericht](docs/versions/0.md#0230-stride--2026-10-25).

## 0.22.0 „Hipline“ – 2026-10-25

- Neue Referenzanalyse [Hüftlage](docs/huefte.md) mit `data/huefte.json`: 57 Waffen aus 10 Spielen bzw. Fassungen aus 17 Videos (Zuarbeit: 19) (Codex-Mac, Ego-Bewegung Thema 1) – Mündung, hintere Visieröffnung, Griffhand, Hüllrechteck und projizierte Neigung im Ruhebild; Destiny 2 mit 28 neuen Waffen aus 16 Klassen. Acht Messzeilen in `docs/destiny2.md` › 2 (Anker `z-hl-…`), Methode 20, 17 Einträge in `data/clips.json`.
- Abnahme: 19/19 Videos per yt-dlp, zehn Bildstichproben; übernommen 57, verworfen 7 (fünf Doppelungen zum Bestand, zwei Schwerter), offen 1. Codex-Mündung von Prometheus Lens widerlegt (Bestand gilt); Steckbrief Granatwerfer präzisiert (57 / 54 gilt für Ignition Code, Flash and Thunder ≈ 58 / 67); Titanfall-2-Showcase neben die tiefe Spielclip-Hüfte gestellt. [Bericht](docs/versions/0.md#0220-hipline--2026-10-25).

## 0.21.0 „Playbook“ – 2026-10-25

- Neuer [Analyse-Standard](docs/standard.md), verbindlich für alle Analysen und Zuarbeiten (Claude, Codex, Antigravity, Unteragenten): Themen getrennt, Messregeln (Bildmaßstab statt Winkelzoom, Körperhöhen, FOV-Bezug, Kachelfehler), Quellenpflicht per yt-dlp und Statusstufen [M]/[S]/[B]/[C]/[O], Bewertung „gut / nicht so gut / für wen“ mit Spielerstimmen, Gegenstimmen und Entwickler-Referenzen (Mindestmaß 5 + 2 Quellen), Unteragenten je Thema bei großen Analysen, Prüfung jeder Zuarbeit, Aufbau A–F der Ergebnisdateien, Einpflegen und Aufräumen.
- Vorlage für Aufträge `docs/vorlagen/auftrag-analyse.md`; Verweis in `AGENTS.md` › Messregeln, README, eine Lehre. Keine Messwerte geändert. [Bericht](docs/versions/0.md#0210-playbook--2026-10-25).

## 0.20.0 „Lookover“ – 2026-10-25

- Neue Referenzanalyse [Inspektionsanimationen](docs/inspektion.md) mit maschinenlesbarer Fassung `data/inspektion.json`: 41 Waffen aus 9 Spielen bzw. Fassungen (Destiny 2 zuerst, Apex, Halo Infinite, CoD MW2019 und BO6, Battlefield 6, Valorant, CS2, Borderlands 3) aus 16 Videos, gemessen von Codex-Mac am 24.10.2026: Darstellungsart (Menü, Idle-Geste, Ego-Inspect, freie Drehung), Ablauf und gezeigte Seiten, Hüllrechteck-Fläche, zwölf native Medienfenster mit Phasen. Vier Destiny-Messzeilen in `docs/destiny2.md` › 2 (Anker `z-insp-…`), Methode und Steckbrief-Hinweis, 23 Einträge in `data/clips.json`.
- Befund: **Destiny 2 hat keinen belegten Ego-Inspect**, nur die Menüinspektion (seit Update 7.1.0 drehbar mit Ambient-VFX); Titanfall 2 ohne Vanilla-Inspect. Ego-Inspects dauern 2,8–6,5 s Quellmedienzeit (Valorant-Rolle bis CS2 USP-S mit langer Haltephase; BO6-Magazinprüfung 5,9–6,1 s), Ruhe-zu-Ruhe 0,2–0,4 s länger als die Codex-Marker. Alle 16 Quellen per yt-dlp geprüft, fünf Werte nachgemessen. [Bericht](docs/versions/0.md#0200-lookover--2026-10-25).

## 0.19.0 „Flashpan“ – 2026-10-25

- Neue Referenzanalyse [Mündungsfeuer und Hülsenauswurf](docs/muendung.md) mit maschinenlesbarer Fassung `data/muendung.json`: Blitzdauer, Blitzgröße (Hüllrechteck), Überdeckung der Visieröffnung, Hülsen (erste Sichtbarkeit, Richtung) und Mündungsform für 35 Waffenmodelle aus acht Spielen (Destiny 2: 12, Destiny 1: 5, Halo Infinite, Titanfall 2, Apex, CoD MW 2019, Borderlands 3, Battlefield 6 je 3), gemessen von Codex-Mac am 24.10.2026. Zwölf Destiny-Messzeilen in `docs/destiny2.md` › 2 (Anker `z-mf-…`), Methode 18, elf Steckbriefe ergänzt, 35 Einträge in `data/clips.json`.
- Alle 20 Quellen per yt-dlp bestätigt, New-Malpais-Entwicklerquelle über ArtStation geprüft; fünf Werte nachgemessen, Gridskipper-Blitzhöhe korrigiert (Seitenzungen 13–16 statt 25 % H). Befund: wo Zeiten belegt sind, 1–2 Bilder Blitz; ADS-Überdeckung 5 % bis ≈ 100 %; goldene Hülsen im ersten oder zweiten Blitzbild. [Bericht](docs/versions/0.md#0190-flashpan--2026-10-25).

## 0.18.0 „Livery“ – 2026-10-25

- Neue Referenzanalyse [Oberflächenmuster von Waffen](docs/oberflaechen.md) mit `data/oberflaechen.json`: Farbfelder, bunter Anteil, Helligkeitsabstand Schale–Rahmen, Muster, Verschleiß und Shaderlogik in Destiny 2 (42 Hersteller-Grundlacke gesichtet, acht gemessen, zwei Shaderreihen), die zehn Antigravity-„Regeln“ als Behauptung mit Befund, BASIC-Materialrollen als Vorschlag. Acht Messeinträge in `data/clips.json`.
- Antigravity-Zuarbeit (9 Spiele, 86 Beispiele, 34 Videos) größtenteils nicht übernommen: alle IDs echt, aber 24 Videos mit falschem Kanal/Datum, 56 Beispiele nicht bestätigt (u. a. Halo 3 statt Infinite, Teileleitfäden statt Hersteller, 14 Zeitstempel hinter dem Videoende), Beschreibungen bei mindestens 8 bestätigten D2-Waffen falsch. Befund: bunte Pixel der Grundlacke 1,7–9,9 % (C* > 25) bei 7 von 8, Farbtonfläche der Akzente 5,6–11,7 % (Antigravity 18–20 %), ΔL* ≥ 40 nur bei hellen Schalen, Muster queren Paneele, Visiergehäuse folgen bei mehreren Waffen der Lackierung. [Bericht](docs/versions/0.md#0180-livery--2026-10-25).

## 0.17.0 „Steadyhand“ – 2026-10-25

- Neue Referenzanalyse [Zielbewegung im Zielen](docs/zielbewegung.md) mit maschinenlesbarer Fassung `data/zielbewegung.json`: Rückstoß im ADS gegen einen starren Weltanker getrennt vom Visier, ruhiges Halten, Punkt im Glas und Hüfte → Zielen für 17 Waffenbeispiele aus vier Spielen (Destiny 2, Battlefield 2042, Apex, Halo Infinite), gemessen von Codex-Mac am 24.10.2026, eingepflegt und an fünf Werten nachgemessen. 15 Destiny-Messzeilen in `docs/destiny2.md` › 2 (Anker `z-zb-…`), Methode 17, acht Steckbriefe ergänzt, 27 Einträge in `data/clips.json`.
- Befund: Im ADS wandert in den Destiny-Showcases vor allem die Welt (4–18 pp Bildhöhe), das Visier bleibt nahe der Ruhelage; Scharfschütze und lineare Fusion kehren nicht ganz zurück; Halte von 0,75–1,8 s zeigen keine Atemperiode. Neue Endmaßstäbe Imperial Needle 2,2× und Extraordinary Rendition 1,7×. [Bericht](docs/versions/0.md#0170-steadyhand--2026-10-25).
## 0.16.0 „Kickback“ – 2026-10-25

- Neue Referenzanalyse [Rückstoßmuster in Videospielen](docs/rueckstoss.md) mit maschinenlesbarer Fassung `data/rueckstoss.json`: 9 Spiele, 36 Waffen, 44 Serienfenster (Codex-Zuarbeit), Destiny 2 zuerst; Nettobahnen gegen Weltanker, Takt, Rücklauf ins ±3-pp-Band, Systemfassungen (Destiny 2023/2025, Valorant hybrid, Apex, CS2, CoD, Battlefield), Musterkatalog je Klasse und zehn Gestaltungsregeln als Vorschlag für BASIC (cubeescape-ballon). 27 Messeinträge in `data/clips.json` (einer je Messzeile).
- Stand „nicht fertig im strengen Kontrollmessziel“: außer Bungies Abyss-Defiant-Test keine Bahn ohne Spielereingabe, kein Zufallsanteil, keine Erstschuss-Streuung. 19 Quellen per yt-dlp geprüft, sechs Stichproben nachgemessen; Titanfall-2-R-201 korrigiert (Fehltreffer des Turmankers, Spitze ≈ 9 statt 18,9 pp H). [Bericht](docs/versions/0.md#0160-kickback--2026-10-25).

## 0.15.0 „Sideview“ – 2026-10-25

- Neue Referenzanalyse [Waffenproportionen und Silhouetten](docs/proportionen.md) mit `data/proportionen.json`: 52 Waffen aus 6 Spielen (Destiny 2: 26, Destiny 1, Marathon, Halo Infinite, Apex je 5, Borderlands 3: 6), Verhältnisse je D2-Klasse (Gehäuse, freier Lauf, Visierhöhe/-länge, H/L), zehn Beobachtungen „was schlank macht“, 17 BASIC-Konturen und der Scout-Visierring im Zielen als BASIC-Abweichungen (Schlüsse in cubeescape-ballon).
- Zuarbeit einer Antigravity-Sitzung [C]: alle 17 Videos per yt-dlp und alle 12 Bildseiten per Abruf bestätigt (keine weggelassen), sechs Werte am eigenen Bild nachgemessen [M], alle innerhalb der Toleranz; vier Kernmessungen in `data/clips.json`.
- Befund: BASIC-Gehäuse sind nicht zu hoch (0,10–0,13 L gegen D2 0,16–0,25 in 3/4-Ansicht); abweichend sind der Scout-Visieraufbau (0,063 L gegen 0,02–0,04) und der Visierring im Zielen (außen/Öffnung 1,76–1,91 gegen Destiny 1,28–1,30). [Bericht](docs/versions/0.md#0150-sideview--2026-10-25).

## 0.14.0 „Eyebox“ – 2026-10-24

- Neue Referenzanalyse [Visiere in Videospielen](docs/visiere.md) mit maschinenlesbarer Fassung `data/visiere.json`: fünf Darstellungsarten (Vollbild, HUD, 3D mit einer Kamera, 3D mit Linsenbild, kein Zielen), Visiertyp je Klasse, Zahlen im Zielen (Öffnung, Gehäuse, Rahmen/Öffnung, Weltzoom als Bildmaßstab, ADS-Zeit) für 31 Spiele, Scharfschützen-Katalog über 100 Spiele, Sitz-Faustregeln, Absehen, Glas, Spielerstimmen und Empfehlungen für BASIC (cubeescape-ballon). 33 Kernmessungen in `data/clips.json`.
- Befund: „klobig“ entsteht durch große, hohe Gehäuse und Block-Sockel, nicht durch die Rahmenstärke (Destiny-Ring 0,15 × Öffnung); Weltzoom ist als Bildmaßstab zu messen, nicht als Winkelzoom; Titanfall skaliert das Visier mit dem FOV. Werkzeugbefund: `sheet` beschriftet Kacheln bei niedriger Bildrate zu früh (eigener Patch folgt). [Bericht](docs/versions/0.md#0140-eyebox--2026-10-24).

## 0.13.1 – 2026-10-24

- Werkzeug-Pin auf ce-agent-tools 0.22.0 „Tollgate“ (`9f1ed12`, vorher 0.20.0 `c7d03f4`): `./ce session say/mail` mit Courier-Verbesserungen (Modellzeile, Kopie an Sightline bei PR/Merge, `ce-freigabe`-Erkennung, `--follow`), Merge-Sperre im Plugin; `.ce-repo.json`, `./ce`, PR-Check-Schritt. Kein Verhalten des Generators geändert.

## 0.13.0 „Lightfoot“ – 2026-10-23

- Eingebettete Werkzeugkopie `tools/ce_tools` (34 Dateien) entfernt (Entscheidung des Nutzers 23.10.2026, Nexogen › Werkzeugstopp und Sync nach Bedarf). `./ce` ist jetzt der Lader aus Agent Tools 0.20 „Lodestar“ und führt genau den Stand aus `.ce-repo.json` › `tools_version` aus (installiertes Plugin mit diesem Commit, Cache `~/.cache/ce-agent-tools`, sonst Download aus dem öffentlichen ce-agent-tools).
- `.mcp.json` startet `ce-search` über `python3 ce search serve`; der PR-Check holt die Werkzeuge mit dem Schritt `ce-tools` am selben Commit. Kein `tidy`-Eintrag: Motiongen schreibt Clips und Bögen nur in Scratch-Ordner. Fachdaten unverändert. [Bericht](docs/versions/0.md#0130-lightfoot--2026-10-23).

## tools-0.16 „Tidemark“ – 2026-10-22

- Gemeinsame Werkzeuge über `ce_sync.py` aus Agent Tools 0.16 (ce-agent-tools#15): `./ce plugins check|fix` hält die Claude-Code-Installationen von ce-shared auf einer Version (je Worktree ein Eintrag, Update erreicht sie nicht sicher); der SessionStart-Hook des Plugins warnt bei älterem ce-shared.
- Hinweis in `AGENTS.md` › Plugins und Hooks; fachliche Versionen und Ausgaben unverändert.

## tools-0.15.1 „Wakeline“ – 2026-10-22

- Gemeinsame Werkzeuge über `ce_sync.py` aus Agent Tools 0.15.1 (ce-agent-tools#13, #14): `./ce session mail` braucht keinen Namen mehr und teilt den Stand mit dem neuen Stop-Hook des Plugins, der den Postfach-Wächter für reservierte Sitzungen selbst startet (am Mac live geprüft); `say` nimmt den Absender aus der Reservierung des Worktrees.
- Hook-Beschreibung in `AGENTS.md` › Plugins und Hooks ergänzt; fachliche Versionen und Ausgaben unverändert.

## tools-0.14.0 „Crosstalk“ – 2026-10-22

- Gemeinsame Werkzeuge über `ce_sync.py` aus Agent Tools 0.14 synchronisiert: `--reserve`/`./ce session patch` melden die Sitzung im Postfach (cubeescape-nexogen#16) an, `./ce session say|who` schreiben Sitzungen einander bzw. listen die angemeldeten.
- Eigenständiger Werkzeugpaket-Stand; fachliche Versionen und Ausgaben unverändert.
- Abnahme über [Tools #12](https://github.com/ffunkfabian-hash/ce-agent-tools/pull/12) (401 Tests, Opus-Richter), `ce_sync --check` und Repo-Quick.

## tools-0.13.0 „Glasshouse“ – 2026-10-22

- Gemeinsame Werkzeuge über `ce_sync.py` aus dem geprüften Agent-Tools-Quellstand 0.13 synchronisiert: Dashboard, Belegvergleich, Vorprüfung, Durchlaufmessung und strengere Cloud-/Vertragsprüfungen.
- Eigenständiger Werkzeugpaket-Stand; fachliche Versionen und Ausgaben unverändert, bestehende Gatehouse-Hooks werden nicht neu installiert.
- Abnahme über [Tools #11](https://github.com/ffunkfabian-hash/ce-agent-tools/pull/11), Quellhash-Abgleich, Repo-Quick und Doku-Prüfung.

## tools-0.12.0 „Gatehouse“ – 2026-10-22

- Gemeinsame Werkzeuge über `ce_sync.py` aus der freigegebenen Quelle Agent Tools 0.12 synchronisiert, einschließlich der Korrektur für ältere Toolgen-Prüfschnittstellen aus 0.11.1.
- Hook-Beschreibung ergänzt: gemeinsame Client-Vorabprüfung und unabhängiges Git-Netz werden über Nexogen installiert; Einbau und Grenzen bleiben zentral dokumentiert.
- Eigenständiger Werkzeugpaket-Stand; Abnahme durch Quellfreigabe [Tools #10](https://github.com/ffunkfabian-hash/ce-agent-tools/pull/10), Hash-Abgleich, Repo-Quick und Doku-Prüfung.

## 0.12.0 „Relaywake“ – 2026-10-22

- Eingebettete gemeinsame Werkzeuge von der geprüften Quelle Agent Tools 0.11 „Wayfinder“ synchronisiert: FTS-Korrektur, öffentliche Such-Aliase, risikobasierter Richter und budgetierter API-Einstieg.
- Nur Werkzeug-Rollout auf Basis 0.11.20; fachliche Daten, Generator-Ausgabe und Verträge unverändert. Hash-Abgleich und repo-eigener Quick sind die Abnahme.
- [Versionsbericht](docs/versions/0.12.md).

## 0.11.20 „Trajectory“ – 2026-10-19

- Ergebnisse des Messauftrags „REF 0.11.17 Ballista“ (Codex-Mac, Briefkasten rules#1) eingetragen: neun Messzeilen in `docs/destiny2.md` § 2 und `data/clips.json` (Imperial Needle, Ignition Code, Eyes of Tomorrow, Cartesian Coordinate, Shock and Awe, Prometheus Lens, Chroma Rush, Baligant, Blue Shift; Anker `z-ballista-…`). Befund: **in keinem Beispiel eine aufgelöste reine Flugzeit**; sichtbare Geschosse mit Spur nur bei Ignition Code (6 Bilder) und Eyes of Tomorrow (Flugköpfe, Suchbahnen); Mündungsblitz-, Kern- und Strahldauer in Bildern, Prometheus Lens 113 Bilder (1,883 s).
- Neue Methode 16: Negativregister Projektile (Pfeilfall, Granaten-Abprall und -Zünder, kurze Raketenflugzeit, Einzelbolzen/Streuung, Pelletmuster, HUD-X bleiben offen). Zwei neue Anker (`s-schrotflinte`, `ce-huefte-muendung-schrot`) für die Schrot-Verweise der Auswertung. Keine Vergleichswerte für Cube Escape abgeleitet. [Versionsbericht](docs/versions/0.md#01120-trajectory--2026-10-19).

## 0.11.19 „Afterline“ – 2026-10-19

- `docs/auswertung.md` an REF 0.11.18 angepasst: Schrot-Mündungsversatz nur für Hawthorne’s Field-Forged Shotgun (+8 / +16 Prozentpunkte) mit CE verglichen; unbenannte PvP-Sichtung −10 / +2 bleibt ungesichert und ohne Differenz. Sprint-Bob-Frequenz als zurückgezogen/nicht bestätigt gekennzeichnet; kein isolierter Destiny-Luftwert.
- Cartesian-ADS ein und aus jeweils mit 0,083 s bis Achse/Hüfte und 0,117 s bis Ruhe sowie benanntem Quellanker angegeben. Keine neue Messung, kein CE-Startwert. Für die Hawthorne-Steckbrief- und CE-Schrot-Zeile fehlen eigene Quellanker; Abschnittsverweise bleiben gültig und der Quellenbesitzer erhält den Hinweis. [Versionsbericht](docs/versions/0.md#01119-afterline--2026-10-19).

## 0.11.18 „Plumb Line“ – 2026-10-19

- Quellenbefunde der Astra-Prüfung (Delta Ledger, Briefkasten rules#1) behoben – nur Zusammenfassungen und Labels, keine Messwerte: `destiny2.md` § 3 nennt Sprint-Frequenz und Luftwert jetzt als zurückgezogen (S1), das CE-Feld des Automatikgewehrs „rechts unterhalb der Mitte“ statt „10 % links oben“ (S1), das CE-Feld des Scharfschützen ohne „nicht konvergierend“ (S5), das Cartesian-ADS-Label nach den Zeitmarken 0,083 / 0,117 s (S4, auch `clips.json`).
- Zeilen „Sprung mit Scharfschützengewehr“ und „Sprint-Haltung“ nennen ihren Clip explizit (ZkMushroom 11.04.2021) statt „derselbe Clip“ und haben `clips.json`-Einträge (S3); neue Anker `z-sprung-scharfschuetze`, `z-sprint-haltung-scharfschuetze`, `z-cartesian-ads`. `cube-escape.md` § 4: Schrot-Zeile mit Hawthorne-Showcase (+8 / +16) und der PvP-Sichtung −10 / +2 als ungesichert (S2-Anteil; `auswertung.md` zieht Delta Ledger nach). [Versionsbericht](docs/versions/0.md#01118-plumb-line--2026-10-19).

## 0.11.16 „Anchorage“ – 2026-10-19

- Zeilenanker (`destiny2.md#L123`) in `docs/auswertung.md` durch benannte Anker ersetzt (`<a id="z-…"></a>` am Ende des ersten Feldes der Zeile, Methoden 14/15, Steckbriefe, vier Zeilen in `cube-escape.md`): die alten Nummern waren nach den Einschüben von 0.11.11–0.11.14 großteils verrutscht (z. B. „Chroma“ → Schrotflinte, „Flash and Thunder“ → Gridskipper).
- `tools/check_links.py` prüft jetzt jeden Anker (benannte `id`, Überschrift-Slug, auch Verweise innerhalb einer Datei) und lehnt Zeilenanker ab; fünf Tests. Dabei zwei tote Überschriftanker gefunden und behoben (`cube-escape.md` 2.2 → `ce-mp-uebergaenge`, CHANGELOG-Verweis auf 0.3.0). Keine Messwerte geändert. [Versionsbericht](docs/versions/0.md#01116-anchorage--2026-10-19).

## 0.11.15 „Delta Ledger“ – 2026-10-19

- `docs/auswertung.md`: Ham-Wechsel mit gemessener Leerphase getrennt von Waffe A ergänzt; Bagels als Kamera-/Modell-Teilbeleg ohne Rückkehr eingeordnet; Methode 15 und Status der zwölf Fragen verlinkt. Keine neuen Messungen oder Startwerte.

## 0.11.14 „Cold Case“ – 2026-10-19

- Ergebnisse des Messauftrags „REF 0.11.13 Dragnet“ (Codex-Mac, Briefkasten rules#1) eingetragen: zwei Messzeilen in `docs/destiny2.md` § 2 und `data/clips.json` – Teilbeleg Kamera-/Modell-Kick (Bagels 22.08.2019: Blitz → Maximum 8 Bilder = 0,133 s, Weltanker +10,56 % Bildhöhe, ohne Rückkehrzeit, kein unbeeinflusstes Profil) und Waffenwechsel mit Eingabe-Overlay (Ham 02.12.2025: Overlay → neues Modell 0,300 s, hüftähnlich 0,433–0,450 s, Bild ohne Waffe 0,150 s).
- Neue Methode 15: Negativregister mit 57 Einträgen (30 am Bild gesichtet, 19 nur Metadaten, 7 ausgeschlossen) – Nachladen-Abbruch, Gehen/Stopp und isolierte Landung bleiben aus freien Destiny-Clips unbelegt; dazu der Bungie-Hinweis auf MG-Reload-Checkpoints (03.07.2025, ohne Clipzeit). `docs/cube-escape.md` § 4: Ham-Wert in der Zeile „Wechsel: leere Sicht“. Keine Zahl für Cube Escape abgeleitet. [Versionsbericht](docs/versions/0.md#01114-cold-case--2026-10-19).

## 0.11.12 „Switch Ledger“ – 2026-10-19

- `docs/auswertung.md`: V13 und die Differenztabelle um den Waffenwechsel nach vollem Nachladen (Waffe A, HUD „Suros Synergy“) aus REF 0.11.11 ergänzt; Wegsenken, neues Modell und hüftähnliche Pose bleiben getrennte Marker. Kein geprüfter Leerbild-Wert und kein Nachlade-Abbruch.
- Methode 14 in den offenen Befunden berücksichtigt: Abbruch vor HUD-voll, kontrolliertes Gehen/Strafe/Stopp und isolierte Landung bleiben unbelegt; getrennter Kamera-Kick ohne freigegebenes Fenster. Keine neue Suche, Messung oder Startwerte. [Versionsbericht](docs/versions/0.md#01112-switch-ledger--2026-10-19).

## 0.11.11 – 2026-10-19

- Messauftrag „REF 0.11.10 Afterimage“ (Codex-Mac, 7 Clips, native Bilder; Briefkasten rules#1) eingetragen: eine neue Messzeile (Waffenwechsel nach vollem Nachladen, Waffe A, mell0wtonin 18.07.2022: Wegsenken 0,550 s nach „voll“, vom Wegsenken bis zum neuen Modell 0,283–0,300 s; ob dazwischen ein Bild ganz ohne Waffe liegt, nicht geprüft) und die Negativbefunde als neue Methode 14: Nachladen-Abbruch vor „voll“, Gehen/Strafe/Stopp, isolierte Landung und der getrennte Kamera-Kick sind aus den geprüften freien Destiny-Clips nicht belegt.
- Keine Zahl für Cube Escape abgeleitet; die Differenztabelle in `docs/auswertung.md` zieht die Auswertungssitzung nach. [Versionsbericht](docs/versions/0.md#01111--2026-10-19).

## 0.11.9 – 2026-10-19

- Hinweis der Auswertungssitzung zu REF 0.11.8, an der Messzeile bestätigt: Der Impuls-Salvenabstand (Gridskipper) steht in `destiny2.md` (Steckbrief, Bestandsmatrix) und `cube-escape.md` › 4 nicht mehr als „≥ 0,383 s“, sondern als beobachtet 0,383–0,433 s (kleinster gesehener Wert 0,383 s, kein Grenzwert), wie die Messzeile. Sidearm (Brass Attacks, „min. 0,383 s“) unverändert.
- [Versionsbericht](docs/versions/0.md#0119--2026-10-19).

## 0.11.8 – 2026-10-19

- `docs/auswertung.md` an REF 0.11.7 / Frame Audit angepasst: Automatikgewehr PvP und Chroma Rush getrennt, zurückgezogene Luft-Absenkung aus der Rangfolge entfernt, MP-Übergangsnullpunkte und ADS-aus-Endmarker getrennt, Impuls-Salvenabstand als beobachteten Bereich mit korrekter Differenz ausgewiesen und Sprint-Bob nicht gerankt.
- Keine neuen Messungen, keine Startwerte und keine Änderungen an Sightline-Quelltabellen. [Versionsbericht](docs/versions/0.md#0118-table-repair--2026-10-19).

## 0.11.7 – 2026-10-19

- Quellkorrekturen aus der Bildprüfung „Frame Audit“ (Codex-Mac, 12 Clips, native Bilder; Briefkasten rules#1); F01 zusätzlich von Sightline am Twitch-Clip (GernaderJake 0,750 s) nachgeprüft: Gewehr-Hüftmündung des PvP-Beispiels liegt bei ≈ 65 / 57 (rechts unterhalb der Mitte), die Angabe „40 / 40“ ist zurückgezogen (`destiny2.md`, `cube-escape.md` › 4: Differenz zum Sturmgewehr jetzt gegen Chroma Rush +7 / +9 und Jake ≈ +15 / +7).
- Zurückgezogen: die Luft-Absenkung „45 % in 0,35 s“ (kein isolierter Luftwert); Sprint-Bob-Frequenz 2,5–3 Hz nicht bestätigt (Hub 8–10 % plausibel). Präzisiert: MP-Fall 19 Bilder ab gewähltem Zwischenmarker (9 Bilder sicherer Einwärtszug), „ruhig 10–11 Bilder“ in 10 (ruhige Pose) und ≈ 11 (weiches Ausfedern unter Feuer) getrennt, Cartesian-Zeitlupe bei ≈ 164,5–165,0 s. Neu Methode 13: Destiny-Waffen sind nicht gleich. Namenskorrektur: das Schwert im Io-Showcase heißt „Unspoken Promise“, nicht „Broken Promise“ (Hinweis Codex-Mac, „Arsenal Atlas“).
- Die zugehörigen Korrekturen der Differenztabelle (F01–F07) in `docs/auswertung.md` folgen durch die Auswertungssitzung. [Versionsbericht](docs/versions/0.md#0117--2026-10-19).

## 0.11.6 – 2026-10-19

- Korrektur aus der Differenztabelle 0.11.5 (Codex-Cloud, Briefkasten rules#1), an der Quellzeile nachgeprüft: In `docs/cube-escape.md` › 4 war der Destiny-Wert „−2 / −4“ für die Handfeuerwaffen-Hüfte der ADS-Schuss (48/46, CW10); die Hüfte liegt im selben Clip grob bei 60/49, also ≈ +10 / −1. Die Differenz zur Pistole ist damit −0,2 / +12,1 statt +11,8 / +15,1 Prozentpunkte.
- [Versionsbericht](docs/versions/0.md#0116--2026-10-19).

## 0.11.5 „Delta Ledger“ – 2026-10-19

- `docs/auswertung.md` ergänzt eine nach Themen gruppierte Differenztabelle Destiny 2 ↔ Cube Escape mit Quellen, absoluten/relativen Abständen, Belegstärke, gemeinsamem Zeitnullpunkt und Vorbehalten; nicht tragfähige Vergleiche sind separat ausgewiesen.
- Eine Rangfolge stellt große, besser belegte Abstände voran. Keine Empfehlung und keine Startwerte in den Referenzunterlagen; keine Clips geladen oder neu vermessen.
- [Versionsbericht](docs/versions/0.md#0115-delta-ledger--2026-10-19).

## 0.11.4 „Afterglow“ – 2026-10-19

- `docs/auswertung.md` auf Referenz 0.11.3 (main `cc39153`) nachgezogen: CE-Tracefall-MP-Marker und Zeitnullpunkte ergänzt; die Befunde F01–F09, B01–B03 und U01–U08 eingearbeitet, darunter Ehroar-Waffenzuordnung, Vexcalibur-Reload, Flash-and-Thunder-Tempo, Chroma-/Cartesian-Bildmarker und Ikelos-Quotient.
- W1–W8 und die Fragen an Cube Escape aktualisiert; Zeitwerte ab Tastendruck und ab erster sichtbarer Bewegung getrennt. Keine neuen Messungen; keine anderen Referenz- oder Spieldateien geändert.
- [Versionsbericht](docs/versions/0.md#0114-afterglow--2026-10-19).

## 0.11.3 – 2026-10-19

- Rest der Codex-Gegenprüfung (Briefkasten rules#1, Befunde „ungenau“), jeder Punkt an der Quellzeile nachgeprüft; keine Messzahl geändert. **U01** `data/clips.json`: 33 Einträge der Referenzen 0.5–0.10 um die in der Messzeile belegten Ruhe-/Hüft-/Teilmarker ergänzt (z. B. Far Future ruhig ≈ 18,05, Hüftschuss ruhig ≈ 15,83). **U02** Entlüften ≈ 2,0 s mit Differenzunsicherheit (15,9 → 18,0 = 2,1 s rechnerisch, ± 0,1). **U05** Fusion-Wiederholung 160,483 → 160,717 = 14 Intervalle, 15 Bilder einschließlich Endpunkten.
- **U07** Tempo-/Menüfreigaben: Methode 10 nennt, welche YouTube-Zeilen am Bild geprüft sind (0.11.2); für alle anderen gilt „nicht unabhängig belegt“. Zwei veraltete Flash-and-Thunder-Stellen (› 4) an 0.11.2 angeglichen.
- **U08** `docs/cube-escape.md` › 4: Differenz-Spannen aus den Messzeilen nachgerechnet (Breite, ADS aus, Linse, Rückstoß Hüfte/ADS, Wippen, Absprung, Ziehen, Nachladen mit benannten Endmarkern); der unbelegte AR-Wert „+13 B.“ beim ADS-Rückstoß und „D ±0 bis +5 B.“ beim Ziehen entfallen. Magnetgreifer: „Greifen ohne Kick“ ist ein Klick ins Leere.
- [Versionsbericht](docs/versions/0.md#0113--2026-10-19).

## 0.11.2 – 2026-10-19

- Bildprüfung der YouTube-Zeilen 0.5–0.10 am Mac (Codex-Mac, native Bilder, Briefkasten rules#1) übernommen: **B01** die Ehroar-Nachladezeile ist eine andere Waffe, nicht Ikelos (HUD „34“ ist kein Perk/Mod); **B02** Vexcalibur ist ein Nachladevorgang von 2,283 s, keine drei Nahkampfschläge; **B03** Flash and Thunder: Schuss 270,117, Tempo belegt (1×, Wiederholung 0,5×).
- Präzisierungen: Chroma 18/19 Bilder, Cartesian ADS ein/aus 5/7 Bilder, Ikelos-Tempo-Quotient 1,984. Die Befunde stammen aus Codex' Bildprüfung und sind aus der Cloud nicht erneut prüfbar (YouTube gesperrt).
- [Versionsbericht](docs/versions/0.md#0112--2026-10-19).

## 0.11.1 – 2026-10-19

- Korrekturen aus Codex' Gegenprüfung der Referenzen 0.5–0.10 (Briefkasten rules#1), alle neun „falsch“-Befunde am Text nachgeprüft und bestätigt (F01–F09): MP-Folgeschuss ist seit 0.7.0 belegt, Bogen-Zyklus und Draw Time getrennt, Bogen-ADS nicht pauschal „fehlt“, Waffe-gegen-Kamera nur als „Modellverschiebung gesichtet, Kameraanteil nicht isoliert“, Flash and Thunder und Vexcalibur als Medienzeit, Reload-Balken beim Scharfschützen-Paar nicht tragend, Impuls-Salve als Schussabstand 0,067 s (erster → dritter 0,133 s), Rückstoß-Spitze −1…0 B. (schwere +2).
- Offen aus der Prüfung: die „ungenau“-Punkte U01–U08 (Markerlisten, Differenz-Spannen) und die Bildprüfung der YouTube-Zeilen am Mac.
- [Versionsbericht](docs/versions/0.md#0111--2026-10-19).

## 0.11.0 „Twin Reel“ – 2026-10-19

- `docs/cube-escape.md` › 2.2 neu: MP-Übergänge aus Cube Escape 0.95 „Tracefall“ (Codex-Mac, 14 Fälle × 3, alle Bilder erhalten, 60/s) – ADS ein/aus, Sprint → ADS, Nachladen mit Spielereignissen und Bildmarkern, **ab erster sichtbarer Bewegung** wie die Vorbilder.
- Vergleich (› 4): MP-Zeilen ADS ein/aus, neue Zeile Sprint → ADS (CE 0,60 s gegen Destiny 0,32 s, Vorbehalt Endpunkt), Nachlade-Marker mit Ereignis- und Bildwerten getrennt; beide CE-Aufnahmen (Plumbline, Tracefall) stimmen auf 1–2 Bilder überein.
- [Versionsbericht](docs/versions/0.md#0110-twin-reel--2026-10-19).

## 0.10.1 – 2026-10-19

- Korrekturen aus „Confluence“ (Hinweise „Für Sightline“), an den Messzeilen nachgeprüft: Scharfschütze A Single Clap 2,80 s **bis ruhig** (nicht bis Hüfte), Far Future 2,05 s Hüfte / 2,18 s ruhig; in `docs/cube-escape.md` › 4 der Destiny-Kamera-Kick als nicht isoliert belegt und der Pistolen-Hüftrückstoß ohne Beleg (der Wert war ein ADS-Schuss).
- [Versionsbericht](docs/versions/0.md#0101--2026-10-19).

## 0.10.0 „Confluence“ – 2026-10-19

- `docs/auswertung.md` auf die Referenzstände 0.5.0–0.9.0 fortgeschrieben: MP-Nachladen/ADS-aus, Impuls- und Automatik-Showcases, kurze Fusion, Schrot-Einzelhülsen, Sniper-Reload/Scope sowie Wechselmarker mit getrennten Endpunkten.
- Zurückgezogene Destiny-Belege sind als „kein Beleg“ gekennzeichnet; W1–W8 und die offenen Cube-Escape-Fragen sind mit aktuellem Status, vorhandenen Zahlen und Quellenlinks versehen. Zeitnullpunkt CE ab Tastendruck und Vorbilder ab erster Bewegung bleiben getrennt.
- Keine neuen Messungen; [Versionsbericht](docs/versions/0.md#0100-confluence--2026-10-19).

## 0.9.0 „Looking Glass“ – 2026-10-19

- Neues Doc `docs/cube-escape.md`: Cube Escape 0.94 „Plumbline“ mit denselben Messgrößen vermessen wie Destiny 2, Apex und Titanfall – zwölf Ego-Geräte (neun Waffen,
  Portalwerfer, Magnetgreifer, Taschenlampe), eigene Aufnahmen 1920 × 1080 bei 60/s aus der Testkopie, Lage pixelgenau aus den projizierten Ankern, Profilwerte daneben.
- 20 Messzeilen, 12 Zeilen Messwerte je Gerät, 12 Steckbriefe, Vergleich mit den Vorbildern (nur Zahlen, Schlüsse in Cube Escape › 18); Vergleich auf den Referenzstand 0.8.0 nachgezogen.
- Begonnen als 0.4.0 auf alter Basis (Selbstvermessung, Mac); Integration und Nummer 0.9.0 durch `Sightline · Cloud`.
- [Versionsbericht](docs/versions/0.md#090-looking-glass--2026-10-19).

## 0.8.0 „Crosswind“ – 2026-10-18

- Codex' Destiny-Bewegungsprüfung (16 Befunde) am Bild abgenommen und in `docs/destiny2.md` › 2/3 eingearbeitet: alte Werte ersetzt oder eingeschränkt, keine Zusatzzeilen daneben.
- Zurückgezogen: Geh-/Bob-Beleg (Destiny 1), durchgehende Scharfschützen-Leere, Automatik-„Landung“ (Waffenwechsel 87 → 1 Patrone), MP-Sprint-Ein/Aus (Wippen), Schrotflinten-Folgeschuss/Pump, Aztecross-Reload-Ende, 1,2-s-Gewehrbereitschaft, Hüft-Zuordnung des CammyCakes-Schusses (ADS).
- Neu: Wechselmarker (Scharfschütze → Handfeuerwaffe, Handfeuerwaffe → Schrotflinte, Granatwerfer → Bogen), Bogen-ADS-Verlassen mit Vollzug, Spann-Reset, MP-Absenkung nach ADS aus; MP-Hüfthalt aus 0.5.1 endet bei ≈ 16,70. Methode 12 (Quellenprüfung). `clips.json` 145 → 149 (6 neu, 2 entfernt).
- [Versionsbericht](docs/versions/0.md#080-crosswind--2026-10-18).
## 0.7.0 „Armory“ – 2026-10-18

- **Waffentyp-Katalog** nach dem offiziellen Bungie-Manifest (Version 244213.26.06.29, abgerufen 18.10.2026): 17 Untertypen je Munitionsart mit Rahmen; neu gegenüber der Ausgangsliste u. a. Hitzewaffen (Entlüften statt Nachladen), Mikro-Raketen-Rahmen, Spread Shot, Slug-Schrot, schwere Bogen/Scharfschützen/Schrot/Fusion/Spur, Primär-Granatwerfer. Bestandsmatrix je Typ in `docs/destiny2.md` › 4.
- Destiny 2, Mac/YouTube, nativ 60/s: **Automatik- und Impulsgewehr** weitgehend (Kadenz, Salvenabstände, Modellrückstoß, ADS mit Zoomverlauf, leeres Nachladen), dazu legendäres Scout-Gewehr, Sidearm-Salve, Bogen, Spezial-Granatwerfer (2×), Maschinengewehr, lineare Fusion mit offener Kimme, Spurgewehr- und Raketenwerfer-Nachladen (Exotic), Hitzewaffe, MP-Folgeschuss nach dem Nachladen (HUD voll → erster Schuss 0,72 s, ein Fall); **Schwert wechselt in die Schulteransicht, Glefe bleibt Ego**.
- Methode 11 (Modellrückstoß per Bildausschnitt-Verfolgung, Zoom als Bildmaßstab); Übergänge, Fortbewegung und Kamera-Kick misst eine eigene Codex-Sitzung (Matrix-Spalte „bei Codex“); Klärungsvorschlag zu W7 (Impuls-Nachladen) und W3 (Showcase-Kadenzen) an Codex übergeben (Auswertung schreibt Codex). › 2 +18 Messzeilen, +14 Sichtungen, › 3 +13 Steckbriefe; `clips.json` +18.
- Offen: Einzelschuss eines Automatikgewehrs, Inspect, legendärer schwerer Granatwerfer und Raketenwerfer-Nachladen, Slug-Schrot, Spread Shot, schwere Sonderformen; [Versionsbericht](docs/versions/0.md#070-armory--2026-10-18).

## 0.6.0 „Chargeline“ – 2026-10-18

- Destiny 2, Mac/YouTube, nativ 60/s, je Klasse zwei Legendary-Waffen aus Ultraclocked-Showcases: **kurzes Fusionsgewehr** (Ladehaltung, Laden bis Strahl = Charge-Time-Wert 0,517/0,867 s, Salve 0,25 s mit Modellrückstoß, ADS ein/aus, Nachladen 1,73–2,9 s), **klassische Schrotflinte** (Pumpen, Einzelhülsen 0,62–0,87 s je Hülse, Repetieren am Ende, voll 5,8–5,9 s), **Scharfschützengewehr** (Nachladen 2,05–2,80 s, Zielfernrohr-Phasen an zwei Optikformen).
- W5 (Scope) und W6 (Sniper-Sprung, Schrot-Reload) geklärt; Methode 10: Normaltempo ohne „0.5x“-Marke über Wiederholungen belegen. `docs/destiny2.md` › 2 neun Messzeilen, sieben Sichtungen, › 3 drei Steckbriefe; `clips.json` +9.
- Offen: HUD-Marker und Folgeschuss nach dem Nachladen (Showcases ohne HUD), Inspect; Lückenliste für 0.7.0 im [Versionsbericht](docs/versions/0.md#060-chargeline--2026-10-18).

## 0.5.2 – 2026-10-18

- MP-Nachtrag (Mac, YouTube, 60/s, Normaltempo): **ADS aus → ruhige Hüfte** isoliert am Exotic Huckleberry (Hüfte 0,067 s, ruhig 0,167 s) und an Ikelos mit HUD (Ehroar, 0,10 / ≈ 0,18 s, Kamera führt nach) – passt zum PvP-Fall aus 0.5.1 (≈ 0,17 s bis Hüfthaltung).
- **HUD „Zähler voll“** 0,73 s nach Beginn des Nachladens aus dem ADS (Ehroar); Huckleberry-Nachladen mit Magazin-Auswurf (MagOut 0,10, MagIn 0,97, Hüfte 2,12 s); Hüftmündung der Showcases ≈ 56–58 / 62–68 % (Raster).
- Werkzeug: `fetch` lädt von YouTube (60-fps-Video bis 1080p, Twitch unverändert); Kontaktbögen ohne `drawtext` über ImageMagick, Schrift wird gesucht – `./check` jetzt auch auf dem Mac grün.
- Offen: erster Folgeschuss nach dem Nachladen (an die Katalog-Sitzung 0.7.0 übergeben).
- [Versionsbericht](docs/versions/0.md#052--2026-10-18).

## 0.5.1 – 2026-10-18

- MP **ADS aus → Hüfthaltung** isoliert belegt (PvP-Clip, nativ 60/s): erste Bewegung bis Hüfthaltung ≈ 10 Bilder (0,17 s), Zeitnullpunkt die erste sichtbare Bewegung; Einzelfall, ± 2 Bilder. Zeile in `docs/destiny2.md` › 2, `clips.json` +1.
- [Versionsbericht](docs/versions/0.md#051--2026-10-18).

## 0.5.0 „Magwell“ – 2026-10-18

- Destiny-2-MP vermessen (Mac, YouTube, 60/s, Normaltempo): **vollständiges Nachladen** an zwei Legendary-MPs (Ultraclocked: Ikelos_SMG, Extraordinary Rendition) mit getrennten Markern – erste Bewegung, MagOut 0,32–0,35 s, MagIn 1,03–1,07 s, Ladehebel, Hüfte 2,55 s, ruhig 2,82–2,87 s; Zähler nicht messbar (kein HUD).
- **ADS aus bis ruhige Hüfte bleibt offen:** alle vier ADS-Ausstiege der Showcases gehen in 3–5 Bildern direkt ins Nachladen (nicht isoliert); Aztecross-Review verworfen.
- Methode 9: YouTube-Weg auf dem Mac, Ultraclocked-Showcases (kein HUD, Zeitlupe gekennzeichnet), ffmpeg ohne `drawtext`.
- [Versionsbericht](docs/versions/0.md#050-magwell--2026-10-18).

## 0.4.2 – 2026-10-18

- Bildraten geklärt (Codex): Toolgen-Clips 24/s, Reel-Ausgabe 30/s, Simulation 60 Schritte/s; Methode 8 und Auswertung angepasst.
- Sichtung für Codex' Messplan: sieben weitere Clips (138 gesamt) auf MP-Nachladen und ADS aus durchsucht – kein Beleg; Sichtungstabelle in `docs/destiny2.md` ergänzt, Lücke bleibt offen.
- [Versionsbericht](docs/versions/0.md#042--2026-10-18).

## 0.4.1 – 2026-10-18

- Befund Bildrate (Codex): Cube-Escape-Reels speichern 30 Bilder/s bei 60 Simulationsschritten/s; ±1 Bild bei 60/s braucht vollständige Einzelbilder. Eingetragen in `docs/destiny2.md` › 2 › Methode 8 und `docs/auswertung.md` › 3.
- [Versionsbericht](docs/versions/0.md#041--2026-10-18).

## 0.4.0 „Crosscheck“ – 2026-10-18

- Werkzeug-Vorbilder (Codex, PR #2): `docs/portal2.md`, `docs/halflife2.md`, `docs/metroidprime.md`, `docs/taschenlampe.md` mit Messungen, Quellen und Steckbriefen; `measure` bindet Kontaktbögen an Quellbild und Zeitstempel.
- Gesamtauswertung (Codex, PR #3): `docs/auswertung.md` – 18 gemeinsame Vorgänge über sieben Vorbilder, Spannen und Muster mit Gegenbeispielen, acht eigene Widersprüche (W1–W8), zwölf Fragen an Cube Escape, 44 Quellenanker; dazu `docs/pdf/Referenzanalyse.pdf` (22 Seiten, Lesefassung).
- Korrekturen der Auswertung (Sightline): Apex-Mündungsrichtung und -kadenz, Titanfall-ADS-Zeit und gestrichene Kadenz (W1, W3 behoben); Fieldwork 0.3.0 mit diesem Stand veröffentlicht.
- [Versionsbericht](docs/versions/0.md#040-crosscheck--2026-10-18).

## 0.3.0 „Fieldwork“ – 2026-10-18

- Destiny 2, PvE-Kanäle (mactics, datto, saltagreppo; 54 Clips gesichtet, 5 vermessen, 9 neue Messzeilen): Scharfschützengewehr (Ziehen, Zielfernrohr ein/aus mit
  Reihenfolge Modell/Linse, Sprint-Haltung, Rutschen), Gewehr (tiefe Sprint-Haltung, Austritt), Granatwerfer (Kipplauf-Nachladen), Bogen (Hüfte von rechts, Spannen ohne ADS, Lösen), Sidearm (Hüfte, Nachladen) und Raketen-Sidearm (ADS, Rückstoß).
- Steckbriefe Sidearm, Langes Gewehr und Bogen ergänzt; Bewegung: Rutschen und Zielfernrohr-Reihenfolge; zwei Maschinenpistolen-Clips für den Codex-Teil vorgemerkt.
- Codex-Teil (PR #1, 63 Clips gesichtet, 8 Messungen): Maschinenpistole (Hüfte, Arme, Fadenkreuz, Wechsel), vollständiges Automatikgewehr-Nachladen mit HUD-Marker,
  Raketenwerfer-ADS und -Schuss, Sichtungsprotokoll je Clip, Fadenkreuz-Katalog (Stand), yt-dlp-Fallback als Python-Modul im Werkzeug.
- Aktionen und Lücken (Sightline, zweiter Teil): Maschinenpistole Sprint/ADS/Dauerfeuer (PvP, 60/s), Duality-Nachladen, Nahkampf bei 60/s, Wechsel-Übersicht je Klasse;
  Befund: Fadenkreuz-Aufblühen ist aus Stream-Clips nicht messbar; zwei Titel-Treffer waren ein anderes Spiel bzw. unklar (Methode).
- Teil 3 (Sightline): Nachladen von Handfeuerwaffe (Hüfte 1,0 s, ADS 0,67 s), linearer Fusion (0,85 s) und Handfeuerwaffen-Rückstoß im ADS bei 60/s, Bogen-Zyklus (0,60 s
  nachspannen), Scout-Zielfernrohr aus (0,17 s, Linse zuerst), Strand-Nahkampf mit Rückkehr (1,5 s); Nachlade-Übersicht je Klasse mit Muster.
- Neue Vorbilder `docs/apex.md` (R-99: Hüfte fast auf der Achse, Sprint hoch-mittig, ADS ↔ Sprint 0,45 s, Landung mit Dip, Rutschen gekippt im Bild) und
  `docs/titanfall2.md` (tiefe kleine Hüfte, Waffe im Flug ausgeblendet, Wandlauf mit 10–15° Kamerarolle, Scope ≤ 0,1 s) – 30 Clips gesichtet, 4 vermessen.
- Zweite Runde Apex/Titanfall (34 Clips): Apex-Wechsel 0,40 s ohne leere Sicht, Sentinel-Scope ≤ 0,1 s, Rutschkamera rollt nicht; Titanfall ADS ein 0,12 s / aus 0,12 s bei 60/s (Kadenz nicht bestimmbar, Korrektur in 0.4.0).
- [Versionsbericht](docs/versions/0.md#030-fieldwork--2026-10-18).

## 0.2.0 „Frame Ledger“ – 2026-10-18

- `measure` ergänzt Bildzeiten bei nativer Rate und einen Entwurf für einen Messungseintrag; Ausgaben bleiben im Scratch.
- Die Verweisprüfung meldet fehlende oder leere Pflichtfelder in `data/clips.json`; Werkzeugtests decken Messausgabe und Validierung ab.
- Kontaktbögen sind in der Cloud nicht bildlich geprüft; der Versionsbericht in `docs/versions/0.md` wird von Sightline ergänzt.

## 0.1.0 „Baseline“ – 2026-10-18

- Umzug der Destiny-2-Referenz aus Cube Escape (`Docs/FIRST_PERSON_EQUIPMENT.md` › 1.2a/1.2b): Messtabelle (53 Zeilen), Steckbriefe für
  elf Waffentypen, Bewegungsblock, Methode; Werkzeug `tools/reference_frames.py` mit Tests; `data/clips.json` (30 Clip-Verweise).
- [Versionsbericht](docs/versions/0.md#010-baseline--2026-10-18).
