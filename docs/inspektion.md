# Inspektionsanimationen – Ego-Inspect, Menüinspektion, Abläufe und Dauern

Referenzanalyse REF 0.20 „Lookover“ (25.10.2026) für die Waffenreihe **BASIC** (Projekt `cubeescape-ballon`) und Cube Escape:
wie Spiele dem Spieler die Waffe zeigen – Ablauf, Phasen, Dauer, gezeigte Seiten, Hände und Rückkehr in die Hüfte.
Gesichtet und gemessen hat eine Codex-Mac-Sitzung (`gpt-6.1-sol` high, 24.10.2026). Diese Version hat die Ergebnisse eingepflegt,
alle Quellen per yt-dlp geprüft und fünf Werte an eigenen Downloads nachgemessen ([8](#8-nachmessung-und-zählung)). Hier stehen nur
Beobachtungen und Messwerte. Schlüsse und Startwerte entstehen in BASIC bzw. Cube Escape. Getrennte Themen mit eigenen Versionen und Docs:
[Visiere](visiere.md) (0.14), [Waffenproportionen](proportionen.md) (0.15), [Rückstoßmuster](rueckstoss.md) (0.16),
[Zielbewegung](zielbewegung.md) (0.17), [Oberflächenmuster](oberflaechen.md) (0.18), [Mündungsfeuer und Hülsenauswurf](muendung.md) (0.19).
Maschinenlesbare Fassung: [`data/inspektion.json`](../data/inspektion.json).

Destiny 2 hat Vorrang. Dort ist **kein Ego-Inspect** belegt, nur die Menüinspektion ([3](#3-destiny-2--menüinspektion-statt-ego-inspect)).
Die vier Destiny-Messzeilen stehen nach Repo-Regel auch in der Messtabelle
[destiny2.md › 2](destiny2.md#2-messungen-an-60-fps-aufnahmen-ab-16-oktober-2026--m) (Anker `z-insp-…`).

**Status:** **[M]** gemessen (Hüllrechteck-Fläche oder native Medienmarker); **[O]** Sichtbefund ohne belastbare Zahl. **Jede Zahl ist
das Beispiel einer Waffe** in einer Aufnahme mit unbekanntem FOV, Skin und Spielstand, kein Klassenmittel.

## 1. Methode und Genauigkeit

- **Zeitbasis: Quellmedienzeit.** Alle Dauern sind Zeiten in der Videodatei, gezählt in nativen Bildern. Sie sind **keine
  nachgewiesenen Spielechtzeiten**, denn keine Quelle hat einen positiven Normaltempoanker (keine Zeitlupenbeschriftung, aber
  auch kein Beleg für Normaltempo). `inspect_total_s` bleibt deshalb in allen 41 Einträgen `null`. Dauern nur aus 60/s- bzw. 59,94/s-Dateien.
  Apex (29,97/s) und der Battlefield-Showcase von Destroyerfield51 (29,97/s geladen) liefern nur Form, Fläche und Reihenfolge.
- **Marker (Codex):** Start = erste sichtbare Inspect-Bewegung, Ende = Hüftlage wieder erreicht; weiche Bewegungsgrenzen ±1–2 Bilder
  je Marker, Differenzen ±2–4 Bilder. Innere Phasengrenzen sind gröber abgelesen. „Hüftlage erreicht“ heißt nicht Stillstand und nicht
  Schussfreigabe. **Ruhe-zu-Ruhe** (erste Bewegung aus der ruhigen Hüfte bis zur Ruhe nach dem Nachschwingen) ist bei CS2 und Valorant
  0,2–0,4 s länger als das Codex-Fenster ([8](#8-nachmessung-und-zählung)); wer eine Gesamtdauer übernimmt, muss die Definition mitnennen.
- **Bildfläche** `max_area_pct`: größtes **gesichtetes Hüllrechteck** des sichtbaren Waffenkörpers ohne Hände in Prozent der gesamten
  Bildfläche, Ursprung oben links. Keine Silhouettenfläche, kein garantiertes Maximum über alle Bilder, Bildränder schneiden teils ab.
  Kanten am 10-%-Raster ±3 pp, daraus Fläche **±6–10 Flächenpunkte**. FOV unbekannt: keine Klassenmittel und keine spielfesten Größen.
- **Richtung:** Seiten beziehen sich auf das Bild. Winkel („grob 40–60° Kippen“) sind Schätzungen der projizierten Lage, keine
  kalibrierten 3D-Winkel. „Visier sichtbar“ ist kein Blick durch die Optik; eine Visier-Großaufnahme kommt in **keinem** Beispiel vor.
- **Zeitstempel:** Codex hat die Bögen mit direkten Einzelbild-Seeks bzw. nativen Bildindizes gebaut, nicht mit dem fehlerhaften
  Low-fps-Filter von `reference_frames.py sheet` ([LESSONS](LESSONS.md)); 46 Direktzeitpunkte weichen höchstens 0,013 s ab, die zwölf
  MW2019-/BO6-Endpunkte stimmen mit den ffprobe-PTS überein.
- **Jahrgang:** Die Quellen stammen von 2019–2025 (Halo-, CS2- und Valorant-Betastände eingeschlossen) und belegen ihren Aufnahmezustand,
  keinen Stand 2026. Destiny-Menübilder 2021 und die Rotationsvorschau 2023 sind unterschiedliche Funktionsstände.

## 2. Quellen

Alle 16 Videos am 25.10.2026 per yt-dlp geprüft: Kanal, Hochladedatum und Titel stimmen mit der Codex-Liste überein.
15 liefern die 41 Waffeneinträge, Deapog (Halo) ist nur Sichtung.

| Spiel | Video (Kanal, Datum) | Rate | Nutzung |
|---|---|---|---|
| Destiny 2 | [Destiny 2 (offiziell), kWUViHovz1E](https://www.youtube.com/watch?v=kWUViHovz1E), 17.05.2023 | 60/s | Menürotation (Gear Inspection Updates), Conditional Finality |
| Destiny 2 | [Ultraclocked, Y5OLr0nbgSg](https://www.youtube.com/watch?v=Y5OLr0nbgSg), 15.02.2021 | 60/s | statisches Menübild Extraordinary Rendition |
| Destiny 2 | [Ultraclocked, RXgRxHESqHQ](https://www.youtube.com/watch?v=RXgRxHESqHQ), 18.02.2021 | 60/s | statisches Menübild Far Future |
| Destiny 2 | [Ultraclocked, uoTaCBMXcFk](https://www.youtube.com/watch?v=uoTaCBMXcFk), 20.02.2021 | 60/s | statisches Menübild Threaded Needle |
| Apex Legends | [AlexTheRed, iNizXu2hl_0](https://www.youtube.com/watch?v=iNizXu2hl_0), 02.07.2021 | 29,97/s | Form, Fläche, Reihenfolge; keine Dauer |
| Halo Infinite | [Hectorlo, TnblT7JnMPI](https://www.youtube.com/watch?v=TnblT7JnMPI), 17.11.2021 | 60/s | Multiplayer-Beta 2021, automatische Idle-Gesten |
| Halo Infinite | [Deapog, 7hhc4qju5JM](https://www.youtube.com/watch?v=7hhc4qju5JM), 13.04.2026 | 30/s geladen | nur Sichtung: stark beschnitten, Modellnamen unklar |
| CoD MW2019 | [M4sked, VAdaNrfQcvw](https://www.youtube.com/watch?v=VAdaNrfQcvw), 05.08.2020 | 60/s | sechs Pistolen/Varianten, drei native Fenster |
| CoD BO6 | [EXILAS, HfgUhmc8p00](https://www.youtube.com/watch?v=HfgUhmc8p00), 11.11.2025 | 60/s | vier Pistolen, drei native Fenster |
| Battlefield 6 | [YourSixGaming, woNLxv-5Hkg](https://www.youtube.com/watch?v=woNLxv-5Hkg), 17.10.2025 | 60/s | freie Benutzerdrehung, eine unbenannte MP |
| Battlefield 6 | [Destroyerfield51, NAR8MrinKQ0](https://www.youtube.com/watch?v=NAR8MrinKQ0), 20.10.2025 | 29,97/s geladen | drei Kapitelmodelle, nur Form/Seiten |
| Valorant | [PC Gaming Videos, LF9pPIi5ops](https://www.youtube.com/watch?v=LF9pPIi5ops), 13.05.2020 | 59,94/s | Altstand 2020, fünf Waffen, drei vollständige Fenster |
| CS2 | [PC Gaming Videos, y1NSHUq7WOI](https://www.youtube.com/watch?v=y1NSHUq7WOI), 01.04.2023 | 59,94/s | Beta 2023, drei Pistolen |
| Borderlands 3 | [MorninAfterKill, Ugq35ExayfI](https://www.youtube.com/watch?v=Ugq35ExayfI), 26.09.2019 | 59,94/s | Item-/Parts-Menü, Hellfire |
| Borderlands 3 | [Agent Lomax, 3T2UZUYPzEc](https://www.youtube.com/watch?v=3T2UZUYPzEc), 15.03.2020 | 60/s | Parts-Menü, Hyperion-Scharfschütze (Mogul-Lauf) |
| Borderlands 3 | [Agent Lomax, Nwp4VJWUujY](https://www.youtube.com/watch?v=Nwp4VJWUujY), 02.10.2019 | 60/s | Parts-Menü, Vladof-AR Bezoomy |

Primärtexte zur Destiny-Menüfunktion: [Bungie, Season 21 Weapon Changes Preview](https://www.bungie.net/7/en/News/article/season_21_weapon_preview)
(17.05.2023) und [Update 7.1.0](https://www.bungie.net/7/en/News/Article/season-deep-update-7-1-0) (23.05.2023): Rotation, Ambient-Effekte und
entfernte Tiefenunschärfe in Inventar- und Eververse-Vorschau (7.1.0 › UI/UX am 25.10.2026 nachgelesen: Waffen und Ornamente drehbar
im Inspection Screen, Ambient-VFX sichtbar, Tiefenunschärfe entfernt). Eingebettete Einzelvideos eines Entwicklerbeitrags (ArtStation, 12.06.2023)
lieferten 404/403 und zählen nicht.

## 3. Destiny 2 – Menüinspektion statt Ego-Inspect

**Ego-Inspect: nicht gefunden.** Das ist kein Beweis, dass es ihn nicht gibt. Suchwege in [7](#7-nicht-gefunden-und-nicht-messbar).
Destiny zeigt die Waffe stattdessen **im Inventar-/Vorschaumenü ohne Hände**: seit Season of the Deep (Update 7.1.0, Mai 2023) frei
drehbar mit Ambient-Effekten am Modell, davor als statisches Schrägprofil.

| Waffe (Klasse) | Quelle, Zeit | Ablauf | Fläche | Status |
|---|---|---|---|---|
| Conditional Finality (Schrot, Exotic) | Destiny 2, 17.05.2023, 0:00–0:10 | Menü, benutzergesteuerte Drehung: beide Breitseiten, verkürzte Vorder-/Hinteransicht, Hochkant-Ansicht (f330–390); Eis-/Solar-Effekte bleiben am Modell, kein Schuss; keine feste Animationszeit | ≈ 50 % (Nachmessung 43 %) | [M] Fläche, [O] Ablauf |
| Extraordinary Rendition (MP) | Ultraclocked, 15.02.2021, 0:01 | statisches Menübild: schräge Breitseite, Mündung links, Schaft rechts, Magazin unten | ≈ 48 % | [M] |
| Far Future (Scharfschütze) | Ultraclocked, 18.02.2021, 0:01 | statisches Menübild: langes Laufstück, langes Zielfernrohr oben; kein Blick durch die Optik | ≈ 43 % | [M] |
| Threaded Needle (lineare Fusion) | Ultraclocked, 20.02.2021, 0:01 | statisches Menübild: Emitter zwischen länglichen Spitzen, offene Visiergabel oben | ≈ 40 % | [M] |

Beobachtet: Menübilder zeigen die **ganze Kontur** (Mündung, Visier/Emitter, Magazin, Schaft) groß und ohne Verdeckung durch Hände.
Die drei Modelle von 2021 haben verlängerte Vorderteile und eigenständige Visier-/Emitterformen. Kein Ornamentwechsel und kein
gepaarter Basis-/Ornamentvergleich im gewählten Fenster. Ego-Abläufe (Start → Hüfte, Finger, Kamerabewegung) sind für Destiny unbekannt.

## 4. Vergleich: Abläufe je Spiel

Fläche = Hüllrechteck-Stichprobe ([1](#1-methode-und-genauigkeit)); Zeiten in [5](#5-dauern-und-phasen). Vollständige Notizen je
Waffe in `data/inspektion.json`.

**Apex Legends** (AlexTheRed, 29,97/s, keine Dauer) – Muster: heben und seitlich aufrichten → um die Laufachse zur Gegenflanke rollen →
zurück → Hüfte; beide Flanken werden gezeigt, kein Magazinentnehmen.

| Waffe (Klasse) | Zeit | Beobachtung | Fläche |
|---|---|---|---|
| P2020 (Pistole) | 0:00–0:11 | schmale Seitenform, türkises Detail am Griffende | ≈ 7 % |
| Peacekeeper (Schrot) | 0:29–0:40 | langer gelochter Laufmantel und Gehäuse dominieren | ≈ 31 % |
| EVA-8 Auto (Schrot) | 0:41–0:51 | Trommelmagazin als großer Kreis an der Flanke | ≈ 35 % |
| Mozambique (Schrotpistole) | 1:04–1:15 | kurze hohe Dreilaufform, einhändige Hauptpose | ≈ 15 % |
| Volt (Energie-MP) | 1:28–1:38 | große Seitenfläche mit leuchtender Längslinie und Ziffern; erreicht Bildränder | ≈ 56 % (beschnitten) |
| Flatline (Sturmgewehr) | 2:15–2:26 | Gitter-/Rippengeometrie, Magazin und Griff lesbar; unten beschnitten | ≈ 50 % |

**Halo Infinite** (Hectorlo, Multiplayer-Beta 2021) – **automatische Idle-/Fidget-Gesten**, im Clip keine Inspect-Eingabe belegt.
Muster: Flanke zeigen → Stützhand greift um oder öffnet sich → Gegenrolle zur Oberseite → Rückkehr.

| Waffe (Klasse) | Zeit | Beobachtung | Fläche |
|---|---|---|---|
| MK50 Sidekick (Pistole) | 0:01–0:06 | linke Hand an Griff/Unterseite, Schlittenoberseite sichtbar | ≈ 16 % |
| CQS48 Bulldog (Schrot) | 0:07–0:11 | Stützhand öffnet sich am Vorderschaft; Trommel und Schiene | ≈ 29 % |
| MA40 (Sturmgewehr) | 0:12–0:16 | Flanke flach, dann Oberseite; digitaler Zähler sichtbar | ≈ 32 % |
| VK78 Commando | 0:17–0:21 | Reflexrahmen im Profil, keine Durchsicht | ≈ 33 % |
| BR75 (Salvengewehr) | 0:22–0:27 | breite Flankenpose gehalten; Zielfernrohr als schlankes Modul über der Tragebrücke | ≈ 40 % |
| S7 (Scharfschütze) | 0:28–0:33 | Hand am langen Gehäuse; langes Zielfernrohr prominent | ≈ 39 % |

**CoD MW2019** (M4sked, 60/s) – Muster bei allen sechs Pistolen: heben zur ersten Flanke → Handgelenkrolle zur Oberseite/Gegenflanke →
Hüfte; kurze Zweiflanken-Präsentation ohne Magazinwechsel. Weltanker (Leitungen, Mast) bleibt fest: die Hände bewegen die Waffe, nicht die Kamera.

| Waffe | Zeit | Beobachtung | Fläche |
|---|---|---|---|
| X16 | 0:02,533–0:06,467 | kantiger kurzer Schlitten | ≈ 18 % |
| 1911 | 0:11,917–0:15,850 | langer schmaler Schlitten | ≈ 18 % |
| M19 | 0:16,517–0:20,450 | heller kantiger Schlitten | ≈ 18 % |
| Renetti | 0:21–0:30 | zwei Varianten, zweite mit ausgeklappter Stütze; keine Dauer | ≈ 22 % |
| .357 (Revolver) | 0:30–0:44 | Trommel im Seitenprofil, zwei Finishvarianten; keine Dauer | ≈ 25 % |
| .50 GS | 0:44–0:49 | breiter hochkantiger Schlitten; keine Dauer | ≈ 25 % |

**CoD BO6** (EXILAS, 60/s) – zwei Muster: **Magazinprüfung** (9mm PM, GS .45, Stryder .22: Magazin heraus, oberste Patrone zur
Kamera, gleiches Magazin wieder ein, dann Ober-/Rückseite) und **Zweiseiten-Rolle** (Grekhova). Kein HUD-Anstieg, Titel und gleiches
Magazin stützen „Inspect, kein Nachladen“. Akimbo-Folgen haben eigene beidhändige Rollen (nicht als Waffe gezählt).

| Waffe | Zeit | Beobachtung | Fläche |
|---|---|---|---|
| 9mm PM | 0:01,033–0:06,917 | Magazinprüfung, Patronenlippen zur Kamera | ≈ 22 % |
| Grekhova | 0:17,600–0:22,633 | Flanke mit rotem Griff, zweite Hand rollt zur Gegen-/Oberseite; kein Magazin | ≈ 18 % |
| GS .45 | 0:38,650–0:44,700 | Magazinprüfung, oberste Patrone deutlich gezeigt | ≈ 23 % |
| Stryder .22 | 0:58–1:05 | langes Magazin heraus und wieder ein; langer Lauf/Dämpfer; keine Dauer | ≈ 33 % |

**Battlefield 6** – **freie Benutzerdrehung** (YourSixGaming-Anleitung): Waffe in eine Inspect-Haltung heben, dann per Maus/Stick
Flanke, Unterseite, Gegenflanke, Oberseite; zurück nach Loslassen. Seite und Haltezeit bestimmt der Spieler, keine feste Dauer.

| Waffe (Klasse) | Quelle, Zeit | Beobachtung | Fläche |
|---|---|---|---|
| unbenannte goldene MP (MP5-artig, Tutorialwaffe) | YourSixGaming, 0:22–0:44 | beide Flanken, Magazin, seitliche Schrauben, Ober-/Unterseite lesbar; Schienenoptik nur im Profil | ≈ 45 % (beschnitten) |
| M433 (Sturmgewehr) | Destroyerfield51, 0:32 / 0:36 | angehobene rechte Flanke → Rolle zur Gegen-/Oberseite; Magazin bleibt eingesetzt, Zeigefinger außen | [O] |
| B36A4 (Sturmgewehr) | Destroyerfield51, 1:16 / 1:20 | nahe Seitenpose → leichtes Umrollen; Handschuh entlang der Flanke | [O] |
| SOR-556 Mk2 (Sturmgewehr) | Destroyerfield51, 1:28 / 1:32 / 2:04 / 2:06 | helle Seitenpose → Gegen-/Oberseite; Finger außen am Gehäuse | [O] |

**Valorant** (PC Gaming Videos, Altstand 2020, 59,94/s) – Muster: erste Seite → Handgelenk rollt zur Unterseite/Gegenflanke → Hüfte;
keine Magazin- oder Verschlussbedienung, HUD-Munition bleibt gleich. Kamera-Weltanker nahezu fest.

| Waffe (Klasse) | Zeit | Beobachtung | Fläche |
|---|---|---|---|
| Classic (Pistole) | 0:00,717–0:03,554 | Zeigefinger und Daumen abgespreizt | ≈ 10 % |
| Ghost (gedämpfte Pistole) | 0:30,097–0:32,933 | langer Dämpfer, Schlitten kippt zur Kamera | ≈ 12 % |
| Sheriff (Revolver) | 0:45,145–0:48,081 | Trommelseite, keine Trommel geöffnet | ≈ 10 % |
| Frenzy (Automatikpistole) | 0:19,002–0:21,505 | beginnt bereits angehoben (Kapitelschnitt), keine Dauer | ≈ 10 % |
| Bucky (Pump-Schrot) | 1:13,257–1:16,760 | zwei Präsentationen, Kapitelschnitt; am linken Rand beschnitten | [O] |

**CS2** (PC Gaming Videos, Beta 2023, 59,94/s) – Muster: heben/erste Flanke → umrollen → **zweite Flanke lange halten** → absenken;
die linke Hand verlässt den Griff. Die Desert Eagle hat ab ≈ 6 s zusätzlich eine Drehvariante (Eingabe und Seltenheit unbekannt).

| Waffe (Klasse) | Zeit | Beobachtung | Längste Seite | Fläche |
|---|---|---|---|---|
| Desert Eagle (Pistole) | 0:00,400–0:05,572 | erste Seite mit Lauf steil nach oben, grob 40–60° gekippt; Schlitten, Auswurffenster, Griffseiten | zweite, zur Kamera gerollte Breitseite | ≈ 22 % |
| R8 Revolver | 0:14,965–0:20,554 | Trommel breit zur Kamera, dann Achsenansicht entlang des Laufs; keine Trommelöffnung | Trommelseite | ≈ 16 % |
| USP-S (Pistole mit Dämpfer) | 0:42,276–0:48,799 | Dämpfer verlängert die Silhouette; erste Seite ≈ 3,2 s | erste Seitenansicht mit Dämpfer | ≈ 20 % |

**Borderlands 3** – **Menüinspektion** im Item-/Parts-Menü, kein handgeführter Ego-Inspect: Waffe im Seitenprofil, Teile (Body,
Barrel, Accessoires) werden einzeln blau markiert, ihr Attribut steht links. Keine Hände, keine feste Dauer.

| Waffe | Quelle, Zeit | Beobachtung | Fläche |
|---|---|---|---|
| Hellfire (Dahl-MP, Präfix unsicher) | MorninAfterKill, 1:35–1:55 | Item View → Parts; Skin „Default“, kein Skinvergleich | ≈ 35 % (Karte verdeckt den Lauf) |
| Hyperion-Scharfschütze mit Mogul-Lauf (Itemname unbekannt) | Agent Lomax, 3:40 / 3:50 | gelochter zweistöckiger Vorderschaft, hohes Zielfernrohr | [O] (beschnitten) |
| Bezoomy (Vladof-AR, Präfix unsicher) | Agent Lomax, 0:45 / 0:50 / 0:55 | Holzschaft, kurzes Zielfernrohr, mehrteiliger Lauf | [O] (verdeckt) |

## 5. Dauern und Phasen

Zwölf vollständige native Fenster (Codex-Marker „erste sichtbare Inspect-Bewegung → Hüftlage erreicht“, Quellmedienzeit). Die
**Ruhe-zu-Ruhe**-Spalte gilt nur für die nachgemessenen Fenster ([8](#8-nachmessung-und-zählung)).

| Spiel | Waffe | Bilder (Rate) | Medienzeit | Ruhe-zu-Ruhe (0.20) |
|---|---|---|---|---|
| CoD MW2019 | X16 | f152 → f388 = 236 (60/s) | 3,93 s | 4,10 s |
| CoD MW2019 | 1911 | f715 → f951 = 236 (60/s) | 3,93 s | – |
| CoD MW2019 | M19 | f991 → f1227 = 236 (60/s) | 3,93 s | – |
| CoD BO6 | 9mm PM | f62 → f415 = 353 (60/s) | 5,88 s | 5,97 s |
| CoD BO6 | Grekhova | f1056 → f1358 = 302 (60/s) | 5,03 s | – |
| CoD BO6 | GS .45 | f2319 → f2682 = 363 (60/s) | 6,05 s | – |
| Valorant | Classic | f43 → f213 = 170 (59,94/s) | 2,84 s | 3,02 s |
| Valorant | Ghost | f1804 → f1974 = 170 (59,94/s) | 2,84 s | – |
| Valorant | Sheriff | f2706 → f2882 = 176 (59,94/s) | 2,94 s | – |
| CS2 | Desert Eagle | f24 → f334 = 310 (59,94/s) | 5,17 s | 5,54 s |
| CS2 | R8 Revolver | f897 → f1232 = 335 (59,94/s) | 5,59 s | – |
| CS2 | USP-S | f2534 → f2925 = 391 (59,94/s) | 6,52 s | – |

**Phasen** (Medienzeit, grob):

- **MW2019, X16 / 1911 / M19** – drei Pistolen mit **identischem Ablauf** von 236 Bildern: heben ≈ 0,5 s → erste Flanke ≈ 1,5 s →
  rollen ≈ 0,4–0,5 s → zweite Flanke ≈ 1,1–1,3 s → Rückkehr ≈ 0,25 s.
- **BO6, 9mm PM** – heben/Flanke 1,03–2,0 · Hand zum Magazin 2,0–2,9 · Magazinprüfung 2,9–4,2 · einsetzen 4,2–4,8 · Oberseite 4,8–6,6 ·
  Rückkehr 6,6–6,92 s. **GS .45** – heben/Flanke 38,65–40,0 · Hand zum Magazin 40,0–40,8 · Patrone/Magazin 40,8–41,7 · einsetzen
  41,7–42,5 · zweite Seite 42,5–44,2 · Rückkehr 44,2–44,70 s. **Grekhova** (ohne Magazin) – heben 17,60–18,0 · erste Flanke 18,0–19,3 ·
  Gegen-/Oberseite 19,3–22,0 · Rückkehr 22,0–22,63 s.
- **CS2, Desert Eagle** – heben/erste Flanke 0,40–2,00 · umrollen 2,00–2,75 · **zweite Flanke halten 2,75–4,76** · absenken/Rückkehr
  4,76–5,57 s. **R8** – anheben/Trommelseite 14,97–18,25 · umrollen/Oberseite 18,25–19,50 · Rückkehr 19,50–20,55 s. **USP-S** –
  heben/erste Seite 42,28–45,51 · Gegenflanke/Oberseite 45,51–47,51 · Rückkehr 47,51–48,80 s.
- **Valorant** – eine Rolle ohne Haltephase: erste Seite → Unterseite/Gegenflanke → Hüfte in ≈ 2,8–2,9 s Medienzeit.

## 6. Muster

Beobachtungen aus den Beispielen, keine Regeln; was davon BASIC übernimmt, entscheidet `cubeescape-ballon`.

1. **Drei Darstellungsarten:** Menüinspektion ohne Hände (Destiny 2, Borderlands 3), automatische Idle-Geste (Halo Infinite 2021) und
   Ego-Inspect auf Tastendruck (Apex, CoD, Valorant, CS2) – bei Battlefield 6 frei vom Spieler gedreht.
2. **Grundablauf Ego-Inspect:** heben → erste Breitseite → Rolle um die Laufachse zur Gegen-/Oberseite → Hüfte. Fast alle Beispiele
   zeigen **beide Flanken**; die Kamera bleibt stehen, die Hände bewegen die Waffe.
3. **Dauer folgt dem Inhalt:** reine Rolle ≈ 2,8–2,9 s (Valorant), Zweiflanken mit Halt ≈ 3,9 s (MW2019), mit Magazinprüfung oder langer
   Haltephase 5–6,5 s (BO6, CS2) – jeweils Medienzeit einzelner Aufnahmen.
4. **Ein Ablauf je Familie:** MW2019 nutzt für X16, 1911 und M19 denselben 236-Bilder-Ablauf; die Unterschiede liegen in der Form, nicht im Timing.
5. **Mechanik zeigen:** BO6 nimmt das Magazin heraus und dreht die oberste Patrone zur Kamera, ohne nachzuladen; CS2/Valorant öffnen weder
   Trommel noch Magazin.
6. **Fläche:** Pistolen füllen im Ego-Inspect ≈ 7–33 % des Bildes, Langwaffen in Apex/Halo ≈ 29–56 % (teils am Bildrand beschnitten);
   Destiny-Menübilder 40–50 %.
7. **Kein Visier-Großbild:** In keinem Beispiel wird durch die Optik geblickt; Visiere erscheinen nur im Profil als Teil der Oberkontur.
8. **Menüinspektion erklärt Aufbau:** Borderlands markiert Teile und nennt ihre Wirkung, Destiny zeigt die ganze Kontur drehbar mit
   Effekten – beides ohne Hände, die etwas verdecken.

## 7. Nicht gefunden und nicht messbar

**Destiny 2, Ego-Inspect: nicht gefunden.** Suchwege (nicht wiederholen, nur ergänzen):
- 63 Clip-Übersichten des PvE-Nachtrags vom 18.10.2026 ohne Fund ([destiny2.md › Sichtungsprotokoll](destiny2.md#sichtungsprotokoll-des-pve-nachtrags-18102026)).
- Websuchen 24.10.2026: `Destiny 2 weapon inspection menu rotate weapon inspect first person`, `Destiny 2 ornament preview weapon rotation`,
  `site.bungie.net "first person" "inspect" weapon` – Treffer führten nur zur offiziellen Menüvorschau. Alte Community-Wünsche sind
  kein Funktionsnachweis.
- Offen: Ornament-/Skinvergleich in der Menüvorschau, Drehgrenzen und -tempo der Rotation (frei bedient, keine feste Zeit).

**Titanfall 2, Vanilla-Inspect: nicht gefunden.** YouTube-Suche `Titanfall 2 inspect weapon animation vanilla`:
[OUCIHsQ4Vio](https://www.youtube.com/watch?v=OUCIHsQ4Vio) (Hectorlo, 16.08.2020) ist eine Reload-Sammlung,
[TZY3MK8BYrQ](https://www.youtube.com/watch?v=TZY3MK8BYrQ) (hyper, 01.12.2023) eine Flatline-Animationsdemo ungeklärter Herkunft,
[XkfeClIww2M](https://www.youtube.com/watch?v=XkfeClIww2M) betrifft Titanfall 1; [4sDwTD9U8bw](https://www.youtube.com/watch?v=4sDwTD9U8bw)
(Weapons From Games) bleibt Schuss-/Reloadquelle. Inspect-Animationen gibt es nur als Funktion von Northstar-Mods
([Mythic R301](https://thunderstore.io/c/northstar/p/CNS144/Mythic_R301_apex_R201/), [MW2022 M200](https://old.thunderstore.io/c/northstar/p/HK560/MW2022_M200/)).
Kein Waffeneintrag in der JSON.

**Weitere Grenzen:**
- **Spielechtzeit:** keine unabhängige Tempo-Referenz und keine Eingabeaufzeichnung; Abbruch durch Schuss und Schussfreigabe nach der
  Rückkehr sind unbekannt. Ein gleichbleibender Munitionszähler schließt Nachladen allein nicht aus.
- **Apex, BF6-Showcase:** 29,97/s – keine Dauern. Ein zusammengeschnittener Showcase belegt keine feste Inspect-Dauer.
- **Valorant Frenzy und Bucky:** Kapitelschnitt bzw. nicht trennbare Wiederholung – keine Gesamtdauer.
- **Skins/Ornamente:** keine systematisch gepaarten Basis-/Premium-Vergleiche; Unterschiede je Skin bleiben offen.
- **Auswahl:** MW2019/BO6/CS2/Valorant sind überwiegend Pistolen; keine Klassenmittel über Langwaffen.
- **Borderlands 3, Battlefield 6:** Der frühere BF6-Treffer `2xSSWPPChVM` ist nicht verfügbar. Für Borderlands 3 ist kein handgeführter
  Ego-Inspect belegt; die Zusatzsuche (u. a. [yCSs1tU4NZg](https://www.youtube.com/watch?v=yCSs1tU4NZg), Whoozaa) brachte keinen,
  [Td1dW-moo4o](https://www.youtube.com/watch?v=Td1dW-moo4o) (Ultraclocked) ist eine Reload-Sammlung.

## 8. Nachmessung und Zählung

**Quellenprüfung (25.10.2026):** alle 16 Videos und die sechs Such-/Ausschlussquellen per yt-dlp: Kanal, Datum und Titel stimmen;
`2xSSWPPChVM` ist wie von Codex vermerkt nicht verfügbar.

**Nachmessung** an eigenen yt-dlp-Downloads (1080p, native Rate), Einzelbilder sequenziell dekodiert, Bewegung gegen ein Hüftbild der
Ruhelage und Sichtprüfung der Markerbilder:

| Wert | Codex | Nachmessung 0.20 | Urteil |
|---|---|---|---|
| MW2019 X16 | f152 → f388, 3,93 s | linke Hand erscheint f151, Hüfte f388 (3,95 s); Nachschwingen bis f397 (4,10 s) | bestätigt |
| BO6 9mm PM | f62 → f415, 5,88 s | erste Drehung f57–59, Hand löst sich f412–413, Hüfte f413–416 (≈ 5,95 s) | bestätigt (Start +4 Bilder früher) |
| CS2 Desert Eagle | f24 → f334, 5,17 s | Anlauf ab f16, linke Hand f24; Waffe auf Hüfthöhe f334 (ab Anlauf 5,31 s), linke Hand zurück und Ruhe f348 (5,54 s) | Marker bestätigt; Ruhe-zu-Ruhe +0,37 s |
| Valorant Classic | f43 → f213, 2,84 s | erste Bewegung f40, Hüftlage f213 (ab erster Bewegung 2,89 s), Ruhe f221 (3,02 s) | Marker bestätigt; Ruhe-zu-Ruhe +0,18 s |
| Destiny 2 Conditional Finality, Fläche | ≈ 50 % | Hüllrechteck am 5-%-Raster ≈ 43 % (f540: x 0,26–0,975, y 0,355–0,955; f150 ≈ 39 %) | innerhalb ±6–10, Codex-Wert eher obere Grenze |

**Zählung (Codex):** 41 Waffenmodelle aus 9 Spielen bzw. Fassungen (MW2019 und BO6 getrennt), 16 Videos (15 mit Waffeneinträgen),
1433 einmalig gesichtete Quellbilder, davon 714 Mess-/Markerbilder (14 Form-/Flächenbilder, 700 native Medienmarker) – keine 714
bildgenauen Spielechtzeitmessungen. Arbeitsdaten im Cache (`~/Library/Caches/CubeEscape/reference/visiere/codex2/`, Nachmessung
`…/reference/inspektion-0.20/`), nicht im Repo.
