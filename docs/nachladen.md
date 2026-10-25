# Nachladen – Phasen, Munitionsübernahme und Rückkehr

Referenzanalyse REF 0.25 „Reload“ (25.10.2026) für die Waffenreihe **BASIC** (Projekt `cubeescape-ballon`) und Cube Escape: wann beim
Nachladen Magazin oder Hülse sichtbar wechseln, wann die Munitionsanzeige springt und wann die Waffe in die Hüfte und zur Ruhe zurückkehrt –
bei Destiny 2 (Einzelhülsen, Batterie, Scharfschütze, Maschinengewehr, Trommelgranatwerfer) und im Vergleich bei Marathon, Apex Legends und
Titanfall 2. Gemessen hat eine Codex-Mac-Sitzung (Auftrag „Ego-Bewegung“, Thema 3, 25.10.2026). Diese Version hat die Zuarbeit nach dem
[Analyse-Standard](standard.md) geprüft, gegen den Bestand abgeglichen und nur Neues oder Präzisierendes übernommen ([8](#8-prüfung-und-zählung)).
Hier stehen Beobachtungen und Messwerte; Schlüsse und Startwerte entstehen in BASIC bzw. Cube Escape. Maschinenlesbare Fassung:
[`data/nachladen.json`](../data/nachladen.json). Getrennte Nachbarthemen: [Hüftlage](huefte.md) (0.22), [Inspektion](inspektion.md) (0.20),
[Mündungsfeuer](muendung.md) (0.19); Waffenwechsel (Ziehen/Wegstecken) ist ein eigenes Thema und **nicht** hier enthalten.

**Status:** **[M]** am Einzelbild bei nativen 60/s gemessen; **[O]** Sichtung ohne belastbare Zahl; **[C]** Spielerstimme oder Zuarbeit, nicht vollständig
nachgeprüft; **[S]** Sekundär- oder Fachquelle; **[B]** Entwickler. **Jede Zahl ist das Beispiel einer Waffe** in einer Aufnahme mit unbekanntem FOV, Handling, Perks und Spielstand – kein Klassenmittel.
Die Zeiten sind Quellmedienzeit **sichtbarer Posen**: keine Eingabezeit, keine Feuerfreigabe, keine Sperrzeit.

## 1. Quellen und Methode

- **Videos:** 13 YouTube-Videos aus vier Spielen bzw. Fassungen, alle am 25.10.2026 per yt-dlp geprüft (Kanal, Datum, Titel, Länge; alle
  Zeitstempel innerhalb der Länge). Destiny 2: acht Ultraclocked-Showcases (2020/21), GrizzlyOne95 (13.03.2022, Häkke-Schrotflinte mit HUD) und
  Hynra Can Fly (29.06.2022, Scharfschütze mit HUD). Vergleich: Marathon (Aculite, 01.03.2026), Apex Legends (Cacek47, 06.02.2019), Titanfall 2
  (Weapons From Games, 14.03.2019). Liste mit Titeln in `data/nachladen.json`. Die IDs der Einträge (`d2-…`, `R-H01…`, `RQ01`, `MV`, `AV`, `TV`) stammen aus den Teilzuarbeiten und bleiben unverändert. Ein vierzehntes Video (PauseResetPlay, `Pxvo2aU7g1k`, 15.06.2018,
  Schrotflinte mit HUD 0→8) ist gültig, aber **für Zeiten verworfen**: 59,94/s im Container, nur ≈ 30 echte Bilder/s.
- **Zeit:** absolute Quellzeit bei nativen 60/1 (Versatz 0), **±1 Bild (16,7 ms)** je Marker, Differenzen ±2 Bilder; weiche Endlagen tragen Bereiche.
  Die Messbilder liegen im Cache der Zuarbeit, nicht im Repo.
- **Endpunkte nicht austauschbar:** „Hüfte“ = die Waffe erreicht die hüftähnliche Lage; „ruhig“ = Ende der großen gerichteten Rückkehrbewegung
  (langsamer Idle bleibt erlaubt). In den 15 Einträgen mit beiden Markern liegen sie 0,03–0,45 s auseinander (Differenz der Marker `t_s`):
  Destiny-Magazin-/Trommel-/Gurtaufnahmen (Far Future ×2, Threaded Needle, Prospector ×2, Cipher) 0,12–0,45 s (Far Future 0,12 / 0,17,
  Threaded Needle 0,22, Prospector 0,20 / 0,15, Cipher 0,45); Titanfall 2 und Apex (soweit ein ruhig-Marker existiert) 0,07–0,20 s (P2016 0,20 / 0,17,
  CAR 0,18 / 0,07, P2020 0,10); Hawthorne 0,10 s, Cartesian 0,18 s, Baligant 0,03 s, Shock and Awe 0,05 s. Baligant 2 Bilder, Shock and Awe 3 Bilder
  (mit dem Hüftbereich 2) – an der Grenze der ±2-Bilder-Differenz, dort nicht als getrennte Endpunkte belegt. Gesamtzeiten nur mit ihrer Definition vergleichen.
- **HUD:** Zeitpunkt, an dem sich die Munitionsanzeige im Bild ändert (`hud_ammo_shown_s`). Die orange Anzeige am Modell der Cartesian Coordinate ist
  **kein** HUD-Zähler. Ohne HUD wird kein Leer-/Taktisch-Zustand aus der Handanimation erschlossen.
- **Normaltempo:** Hynra-Clip: HUD-Uhr 6:21 → 6:11 zwischen 10 und 20 s Videozeit (laut Zuarbeit), eigene Stichprobe 6:17 → 6:16 zwischen 14,25 und
  14,68 s. Marathon: laut Zuarbeit HUD-Uhr 19:12 → 19:09 in 3,000 s – bei der Abnahme **im Bild nicht lesbar**, daher nicht bestätigt. Apex und
  Titanfall ohne eigenen Tempoanker; die Apex-Zuarbeit nennt ein exakt doppeltes Bild als Quellunregelmäßigkeit, keine 30-in-60-Struktur.
- **Feldnamen:** In `data/nachladen.json` heißen Dauern `visible_*` und die Abbruchangabe `cancel_observed` (in keinem Fall beobachtet), damit sie nicht
  als Spielmechanik gelesen werden.
- **Nicht übernommen:** die je Eintrag **kopierten Bewertungsfelder** der Zuarbeit (`good`, `bad`, `audience`, `player_opinion`, `dev_reference`) –
  alle 23 Einträge trugen denselben Text je Spiel (Maschinengewehr-Text bei Schrotflinte, Apex-Threads bei Destiny); die Bewertung steht je Spiel in
  [5](#5-bewertung-gut-nicht-so-gut-für-wen). Außerdem verworfen: das Video `Pxvo2aU7g1k` (siehe oben) und drei Apex-Inspektionsfolgen, die Codex
  selbst als Inspektion erkannt hat.

## 2. Messtabelle

Spalten: Fenster = Beginn bis Ende der Messung (Quellzeit in s); Marker = nur die gesetzten Marker (ohne Wert = nicht belegt, siehe `data/nachladen.json`
› `phases`). Jede Zeile hat einen Anker `rl-…`.

### Destiny 2

| Waffe (Klasse) | Quelle | Fenster (s) | Marker (Quellzeit, s) | Dauer (sichtbare Posen) | Munition / HUD | Bestand | Hinweis; Bildprüfung |
|---|---|---|---|---|---|---|---|
| **Hawthorne's Field-Forged Shotgun** (Schrotflinte) <a id="rl-d2-hawthorne-native"></a> | Ultraclocked, [73lGCT7yOtk](https://www.youtube.com/watch?v=73lGCT7yOtk), 25.01.2020 | 322,283–328,267 s | Waffe verlässt die Hüftlage / Nachladebeginn 322,283 · Ladeöffnung dreht zur Kamera 322,400 · Hülse 1 322,883 · Hülse 2 323,517 · Hülse 3 324,133 · Hülse 4 324,750 · Hülse 5 325,383 · Hülse 6 326,000 · Hülse 7 326,617 · abschließende Repetierbewegung 327,667 · zurück hüftähnlich 328,067 · ruhige Hüftlage, weiches Ende 328,167 | bis ruhig (weiches Beruhigen): **5,88 s** (5,83–5,98); bis Hüfte: 5,77–5,82 s | kein HUD | ergänzt Zeile Hawthorne (0.6.0) | 7 Einzelhülsen, Takt 37–38 Bilder; Repetieren erst nach der siebten Hülse; kein HUD – Hülsenspitzen sind keine Munitionsübernahme; Bild: Prüfer: Start f19337, Hülse 1 f19373, Hülse 7 f19597, Repetieren/Hüfte f19660/f19684 ok |
| **Baligant** (Schrotflinte) <a id="rl-d2-baligant-native"></a> | Ultraclocked, [afs_dhFDhQU](https://www.youtube.com/watch?v=afs_dhFDhQU), 09.02.2020 | 15,550–21,350 s | Waffe verlässt die Hüftlage / Nachladebeginn 15,550 · Hülse 1 16,117 · Hülse 2 16,983 · Hülse 3 17,833 · Hülse 4 18,700 · Hülse 5 19,567 · abschließende Repetierbewegung 20,733 · zurück hüftähnlich 21,283 · ruhige Hüftlage, weiches Ende 21,317 | bis ruhig (weiches Beruhigen): **5,77 s** (5,75–5,80); bis Hüfte: 5,70–5,75 s | kein HUD | ergänzt Zeile Baligant (0.6.0) | 5 Einzelhülsen, Takt 51–52 Bilder; bestätigt die Bestandszahlen 0,85–0,87 s je Hülse; Bild: Prüfer: Start f933, ruhig f1279 ok |
| **Cartesian Coordinate** (kurzes Fusionsgewehr) <a id="rl-d2-cartesian-native"></a> | Ultraclocked, [73lGCT7yOtk](https://www.youtube.com/watch?v=73lGCT7yOtk), 25.01.2020 | 161,317–163,300 s | Waffe verlässt die Hüftlage / Nachladebeginn 161,317 · Batterie sichtbar vom Schacht getrennt 161,633 · neue Batterie vor dem Schacht 162,267 · Batterie sitzt / orange Modellanzeige beginnt 162,317 · Hand löst sich vom Schacht 162,500 · Handballenschlag gegen die Seite 162,733 · zurück hüftähnlich 163,050 · ruhige Hüftlage, weiches Ende 163,233 | bis ruhig (weiches Beruhigen): **1,92 s** (1,88–1,98); bis Hüfte: 1,72–1,77 s | kein HUD | ergänzt Zeile Cartesian Coordinate (0.6.0) | Batterie seitlich; orange Anzeige gehört zum Modell, **kein HUD**; Hüfte und ruhig getrennt; Bild: Prüfer: Start Soll f9679 / Ist f9678 (−1 Bild), Anzeige f9738 ok |
| **Shock and Awe** (kurzes Fusionsgewehr) <a id="rl-d2-shock-awe-native"></a> | Ultraclocked, [42zdQOVBAD0](https://www.youtube.com/watch?v=42zdQOVBAD0), 30.01.2020 | 358,850–361,833 s | Waffe verlässt die Hüftlage / Nachladebeginn 358,850 · Batterie löst sich sichtbar seitlich 359,400 · neue Batterie von unten links sichtbar 360,233 · Einsetzen beendet, Hand löst sich 360,433 · Handballenschlag gegen die Seite 361,133 · zurück hüftähnlich 361,667 · ruhige Hüftlage, weiches Ende 361,717 | bis ruhig (weiches Beruhigen): **2,87 s** (2,85–2,98); bis Hüfte: 2,78–2,83 s | kein HUD | ergänzt Zeile Shock and Awe (0.6.0) | Batterie teils verdeckt: Marker nennt sichtbares Ablösen; Handballenschlag getrennt; Bild: Prüfer: Start f21531, Hüfte f21700, ruhig f21703 ok |
| **Häkke-Schrotflinte, Name nicht eingeblendet** (Schrotflinte) <a id="rl-d2-shotgun-three-round-hud"></a> | GrizzlyOne95, [lZcqE1LWRDA](https://www.youtube.com/watch?v=lZcqE1LWRDA), 13.03.2022 | 11,700–13,967 s | Nachlade-Rollen nach Waffenwechsel, weicher Beginn 11,750 · erste sichtbare rote Hülse 12,250 · HUD 0→3 / Reserve 6→3 12,350 · HUD 3→6 / Reserve 3→0 12,750 · abschließende Repetier-/Schließbewegung sichtbar 13,333 · zurück hüftähnlich 13,900 | bis Hüfte: 2,05–2,25 s | HUD 0→3 bei 12,350 s, 3→6 bei 12,750 s (24 Bilder = 0,400 s); Reserve 6→3→0; leer; letzte Zunahme → hüftähnlich 1,08–1,22 s | neu | Name und Kapazität nicht eingeblendet; Titel nennt Enhanced Dual Loader + Frenzy – das +3 je Zuführbewegung ist nur für diesen Perk-Fall belegt; Beginn direkt nach Waffenwechsel, Ruhe nicht isoliert; Zähler 6 am Anfang beweist keine Maximalkapazität; Bild: Prüfer und eigene Nachmessung: HUD 0→3 bei f741, 3→6 bei f765 (24 Bilder), Reserve 6→3→0 ok |
| **Imperial Needle** (Bogen) <a id="rl-d2-bow-reload-na"></a> | Ultraclocked, [dKNTDzi__Qo](https://www.youtube.com/watch?v=dKNTDzi__Qo), 19.02.2021 | ≈ 4–6 s (nur Sichtung) | – | keine Gesamtdauer (Start oder Ende nicht isoliert) | – | ergänzt Bogen-Zyklus (s-matrix-bogen), nur Abgrenzung | [O]: neuer Pfeil von rechts gehört zum Schusszyklus, kein Magazin-Nachladen; keine neue Zeit, keine Aussage über alle Bögen; Bild: keine Zahl, nicht nachgemessen |
| **Far Future** (Scharfschützengewehr) <a id="rl-r-h01"></a> | Ultraclocked, [RXgRxHESqHQ](https://www.youtube.com/watch?v=RXgRxHESqHQ), 18.02.2021 | 15,867–18,050 s | Beginn 15,867 · Magazin heraus 16,150 · Magazin ein 16,567 · Kammerstängel-Griff 17,067 · Hüfte 17,933 · ruhig 18,050 | bis ruhig (Ende der großen Rückkehrbewegung): **2,18 s** (2,12–2,25) | kein HUD | ergänzt Zeile Far Future (0.6.0) | aus der Hüfte; „Magazin heraus“ = Luftspalt 16,150 s (Bestand 15,94–16,09 s: andere Definition); Bild: nur Rechnung und Bestandsvergleich |
| **Far Future** (Scharfschützengewehr) <a id="rl-r-h02"></a> | Ultraclocked, [RXgRxHESqHQ](https://www.youtube.com/watch?v=RXgRxHESqHQ), 18.02.2021 | 44,000–46,233 s | Beginn 44,000 · verlässt Zielachse 44,100 · Magazin ein 44,750 · Kammerstängel-Griff 45,183 · Hüfte 46,067 · ruhig 46,233 | bis ruhig (Ende der großen Rückkehrbewegung): **2,23 s** (2,17–2,30) | kein HUD | ergänzt Zeile Far Future (0.6.0) | aus dem Zielfernrohr; Gesamtdauer enthält das sichtbare Verlassen der Zielachse; Magazin-Aus verdeckt; Bild: nur Rechnung und Bestandsvergleich |
| **Shattered Cipher** (Maschinengewehr) <a id="rl-r-h03"></a> | Ultraclocked, [DEM-8xg66R8](https://www.youtube.com/watch?v=DEM-8xg66R8), 14.05.2021 | 11,800–16,667 s | Beginn 11,800 · Deckel öffnet 12,433 · Trommel hoch 13,117 · Gurt 13,500 · Deckel geschlossen 14,583 · seitliche Hand 15,367 · Hüfte 16,217 · ruhig 16,667 | bis ruhig (Ende der großen Rückkehrbewegung): **4,87 s** (4,80–4,93) | kein HUD | ergänzt Zeile Shattered Cipher (0.7.0) | Deckel, Trommel, Gurt, Seitenhand; Quelle Mai 2021 – belegt keine heutigen MG-Regeln; lokale Datei 1280 × 720 (Bestand nennt 1920 × 1080; Bilder/60 bleibt gültig); Bild: nur Rechnung und Bestandsvergleich |
| **Threaded Needle** (Lineares Fusionsgewehr) <a id="rl-r-h04"></a> | Ultraclocked, [uoTaCBMXcFk](https://www.youtube.com/watch?v=uoTaCBMXcFk), 20.02.2021 | 16,033–19,333 s | Beginn 16,033 · Magazin ein 17,567 · tiefer Halt 18,400 · Hüfte 19,117 · ruhig 19,333 | bis ruhig (Ende der großen Rückkehrbewegung): **3,30 s** (3,22–3,37) | kein HUD | ergänzt Zeile Threaded Needle (0.7.0); Hüfte-Marker weicht ab | Bestand: Hüfte 19,3 · ruhig ≈ 19,35 · „ruhig +3,3 s“; Zuarbeit: Hüfte 19,117 s (3,08 s), ruhig 19,333 s (3,30 s) – die **Ruhe** stimmt, der **Hüftmarker** liegt ≈ 11 Bilder früher; am Bild nicht entschieden; Bild: nur Rechnung und Bestandsvergleich |
| **The Prospector** (Schwerer Trommelgranatwerfer (Exotic)) <a id="rl-r-h05"></a> | Ultraclocked, [L3UXaiGBtVc](https://www.youtube.com/watch?v=L3UXaiGBtVc), 12.03.2021 | 14,267–18,883 s | Beginn 14,267 · Trommel offen 14,500 · Magazin heraus 15,050 · Magazin ein 16,233 · Hüfte 18,683 · ruhig 18,883 | bis ruhig (Ende der großen Rückkehrbewegung): **4,62 s** (4,53–4,70) | kein HUD | neu (Bestand: „nicht vermessen“) | Exotic-Trommelwechsel, Schussrücklauf davor, Effektblitze ab f863 eigene Ereignisse; Start überlappt den Rücklauf; Bild: Prüfer: Trommel offen f870, Magazin ein f974, Hüfte f1121 per Sichtprüfung |
| **The Prospector** (Schwerer Trommelgranatwerfer (Exotic)) <a id="rl-r-h06"></a> | Ultraclocked, [L3UXaiGBtVc](https://www.youtube.com/watch?v=L3UXaiGBtVc), 12.03.2021 | 22,900–27,383 s | Beginn 22,900 · Trommel offen 23,100 · Magazin heraus 23,650 · Magazin ein 24,800 · Hüfte 27,233 · ruhig 27,383 | bis ruhig (Ende der großen Rückkehrbewegung): **4,48 s** (4,40–4,57) | kein HUD | neu | zweiter Wechsel im selben Upload; Slow-Motion-Überblendung nach dem Ende; Bild: nur Rechnung |
| **Blau/violettes Scharfschützengewehr mit kleiner Rundoptik (Name unbestätigt)** (Scharfschützengewehr) <a id="rl-rq01"></a> | Hynra Can Fly, [ZpuJ2yw_U3c](https://www.youtube.com/watch?v=ZpuJ2yw_U3c), 29.06.2022 | 14,133–15,667 s | linke Hand am Magazin 14,133 · Magazin aus dem Schacht 14,317 · neues Magazin sichtbar 14,633 · Magazin sitzt 14,650 · HUD 0→1 (Reserve 1→0) 14,667 · hüftähnliche Rückkehr 15,483 | keine Gesamtdauer (Start oder Ende nicht isoliert) | HUD 0 / Reserve 1 → 1 / 0 bei 14,667 s; Kapazität unbekannt; HUD → Hüftbild 0,82 s (49 Bilder, 47–52) | neu | Name unbestätigt; Beginn mit Ziehen überlagert; Zähler 0 / Reserve 1 → 1 / 0 – Kapazität unbekannt, nicht „voll“; Bild: Prüfer und eigene Nachmessung: HUD 0→1 bei f880 (f879 zeigt 0), hüftähnlich f929 ok |

### Marathon (2026)

| Waffe (Klasse) | Quelle | Fenster (s) | Marker (Quellzeit, s) | Dauer (sichtbare Posen) | Munition / HUD | Bestand | Hinweis; Bildprüfung |
|---|---|---|---|---|---|---|---|
| **Gewehr A, schwarz/rot mit gelbem Oberteil (Modell unbestätigt)** (Gewehr) <a id="rl-mv01"></a> | Aculite, [FEW1ZkadfM8](https://www.youtube.com/watch?v=FEW1ZkadfM8), 01.03.2026 | 199,083–201,367 s | Beginn 199,167 · verlässt Mitte 199,200 · Magazin heraus 199,683 · Magazin ein 200,000 · HUD 200,817 · Hüfte 201,267 | bis Hüfte: **2,10 s** | taktisch: 15 → 27; HUD 200,817 s; HUD → Hüfte 0,45 s | neu (kein Marathon-Doc) | Modell unbestätigt; Start = erste Reload-Handbewegung nach ADS-aus; keine isolierte Ruhe (Gehen); Bild: Prüfer: HUD 15→27 bei 200,8167 s exakt (Summe 15+238 = 27+226) |
| **Gewehr A, schwarz/rot mit gelbem Oberteil (Modell unbestätigt)** (Gewehr) <a id="rl-mv02"></a> | Aculite, [FEW1ZkadfM8](https://www.youtube.com/watch?v=FEW1ZkadfM8), 01.03.2026 | 272,633–274,917 s | HUD 274,350 · Hüfte 274,783 | keine Gesamtdauer (Start oder Ende nicht isoliert) | taktisch: 6 → 27; HUD 274,350 s; HUD → Hüfte 0,43 s | neu | Start durch Ziehen überlagert → Gesamtdauer null; Gehen und Transparenzeffekt verhindern Ruhe; Bild: nicht einzeln am Bild geprüft |
| **Thermal-Scharfschützengewehr mit HUD-Kapazität 5 (Modell unbestätigt)** (Scharfschützengewehr) <a id="rl-mv03"></a> | Aculite, [FEW1ZkadfM8](https://www.youtube.com/watch?v=FEW1ZkadfM8), 01.03.2026 | 149,900–152,467 s | HUD 151,733 · Hüfte 152,333 | keine Gesamtdauer (Start oder Ende nicht isoliert) | taktisch: 4 → 5; HUD 151,733 s; HUD → Hüfte 0,60 s | neu | Thermal-Scharfschütze, Kapazität 5; Start durch ADS-aus überlagert; Ladeweg verdeckt; Bild: Prüfer: HUD 4→5 Soll 151,7333 / Ist 151,7167 s (−1 Bild) |

### Apex Legends (2019)

| Waffe (Klasse) | Quelle | Fenster (s) | Marker (Quellzeit, s) | Dauer (sichtbare Posen) | Munition / HUD | Bestand | Hinweis; Bildprüfung |
|---|---|---|---|---|---|---|---|
| **RE-45 Auto** (Pistole) <a id="rl-av01"></a> | Cacek47, [R-BGChzYGpo](https://www.youtube.com/watch?v=R-BGChzYGpo), 06.02.2019 | 17,717–19,900 s | Beginn 17,750 · verlässt Mitte 17,767 · Magazin ein 18,733 · Verschluss 18,883 · HUD 19,333 · Hüfte 19,600–19,850 | bis Hüfte: 1,85–2,10 s | leer: 0 → 15; HUD 19,333 s; HUD → Hüfte 0,27–0,52 s | ergänzt apex.md (Nachladen, Beginn) und auswertung.md V12 | **korrigiert:** Hüftlage nicht 19,15 s, sondern ≈ 19,6–19,85 s (Zuarbeit: total 1,40 s → jetzt Start→Hüfte 1,85–2,10 s); Kameradrehung verhindert Ruhe; Bild: Prüfer und eigene Nachmessung: bei 19,15 s noch beide Hände am Verschluss, HUD 0→15 bei 19,333 s ok |
| **P2020** (Pistole) <a id="rl-av02"></a> | Cacek47, [R-BGChzYGpo](https://www.youtube.com/watch?v=R-BGChzYGpo), 06.02.2019 | 29,017–30,217 s | Beginn 29,067 · verlässt Mitte 29,100 · Magazin ein 29,783 · HUD 29,917 · Hüfte 30,067 · ruhig 30,167 | bis ruhig: **1,10 s** | leer: 0 → 10; HUD 29,917 s; HUD → Hüfte 0,15 s | ergänzt apex.md und auswertung.md V12 | kein sicherer Verschlussgriff; Hüfte 0,150 s, ruhig 0,250 s nach HUD; Bild: Prüfer: HUD 0→10 bei 29,9167 s exakt |
| **R-301 Carbine** (Automatikgewehr) <a id="rl-av03"></a> | Cacek47, [R-BGChzYGpo](https://www.youtube.com/watch?v=R-BGChzYGpo), 06.02.2019 | 46,283–48,783 s | Beginn 46,350 · verlässt Mitte 46,383 · Magazin ein 47,800 · Verschluss 48,233 · HUD 48,250 · Hüfte 48,733 | bis Hüfte: **2,38 s** | leer: 0 → 18; HUD 48,250 s; HUD → Hüfte 0,48 s | ergänzt apex.md und auswertung.md V12 | Hand am Ladegriff nach Magazinsitz; danach ADS, daher keine Ruhe; Inspektionsfolge 40–42,8 s von Codex verworfen; Bild: Prüfer: HUD 0→18 bei 48,25 s exakt |

### Titanfall 2

| Waffe (Klasse) | Quelle | Fenster (s) | Marker (Quellzeit, s) | Dauer (sichtbare Posen) | Munition / HUD | Bestand | Hinweis; Bildprüfung |
|---|---|---|---|---|---|---|---|
| **Hammond P2016** (Pistole) <a id="rl-tv01"></a> | Weapons From Games, [4sDwTD9U8bw](https://www.youtube.com/watch?v=4sDwTD9U8bw), 14.03.2019 | 5,417–6,783 s | Beginn 5,483 · verlässt Mitte 5,533 · Magazin ein 6,267 · HUD 6,267 · Hüfte 6,517 · ruhig 6,717 | bis ruhig: **1,23 s** | taktisch: 5 → 16; HUD 6,267 s; HUD → Hüfte 0,25 s | ergänzt titanfall2.md (Nachladen) und auswertung.md V12 | Paar mit TV02 (taktisch 5 → 16); Bild: Prüfer: HUD 5→16 bei 6,2667 s exakt |
| **Hammond P2016** (Pistole) <a id="rl-tv02"></a> | Weapons From Games, [4sDwTD9U8bw](https://www.youtube.com/watch?v=4sDwTD9U8bw), 14.03.2019 | 15,517–16,817 s | Beginn 15,583 · verlässt Mitte 15,617 · Magazin ein 16,300 · HUD 16,300 · Hüfte 16,583 · ruhig 16,750 | bis ruhig: **1,17 s** | leer: 0 → 16; HUD 16,300 s; HUD → Hüfte 0,28 s | ergänzt titanfall2.md und auswertung.md V12 | Paar mit TV01 (leer 0 → 16); kein belastbarer Zusatzgriff; Bild: Prüfer: HUD 0→16 bei 16,30 s exakt |
| **CAR** (Maschinenpistole) <a id="rl-tv03"></a> | Weapons From Games, [4sDwTD9U8bw](https://www.youtube.com/watch?v=4sDwTD9U8bw), 14.03.2019 | 94,100–96,200 s | Beginn 94,267 · verlässt Mitte 94,400 · Magazin heraus 94,667 · HUD 95,500 · Magazin ein 95,517 · Hüfte 95,933 · ruhig 96,117 | bis ruhig: **1,85 s** | taktisch: 1 → 36; HUD 95,500 s; HUD → Hüfte 0,43 s | ergänzt titanfall2.md und auswertung.md V12 | Paar mit TV04; eine Restpatrone; Zeitfeld korrigiert (überspannte TV04); Bild: Prüfer: Start 94,2667 s, HUD 1→36 bei 95,50 s ok |
| **CAR** (Maschinenpistole) <a id="rl-tv04"></a> | Weapons From Games, [4sDwTD9U8bw](https://www.youtube.com/watch?v=4sDwTD9U8bw), 14.03.2019 | 101,633–104,100 s | Beginn 101,733 · verlässt Mitte 101,767 · Magazin heraus 102,217 · Magazin ein 103,100 · Verschluss 103,400 · HUD 103,400 · Hüfte 103,933 · ruhig 104,000 | bis ruhig: **2,27 s** | leer: 0 → 36; HUD 103,400 s; HUD → Hüfte 0,53 s | ergänzt titanfall2.md und auswertung.md V12 | Paar mit TV03; zusätzlicher Griff auf der Oberseite nach Magazinsitz; Zeitfeld korrigiert; Bild: HUD 0→36 bei 103,4 s nicht einzeln nachgeprüft |

## 3. Abgleich mit dem Bestand

| Eintrag | Bestand | Zuarbeit | Entscheidung |
|---|---|---|---|
| Hawthorne, Baligant (Einzelhülsen) | [destiny2.md › 2](destiny2.md#2-messungen-an-60-fps-aufnahmen-ab-16-oktober-2026--m) (0.6.0): 7 bzw. 5 Hülsen, Baligant 5,77 s und 0,85–0,87 s je Hülse | native Marker, Takt 37–38 bzw. 51–52 Bilder, Hawthorne Repetieren 327,5–327,8 s (Bestand 327,45–327,60 s: anderer Markerumfang) | **ergänzt**, Bestandszahlen bestätigt; keine Doppelzeile |
| Cartesian Coordinate, Shock and Awe (Batterie) | Hüfte ≈ 163,05 s bzw. ≈ 361,65 s, Cartesian 1,73 s (104 Bilder) | Hüfte 163,033–163,083 s bzw. 361,633–361,683 s; zusätzlich ruhig 163,2–163,3 s bzw. 361,70–361,83 s | **ergänzt** (Ruhe als eigener Endpunkt), bestätigt |
| Far Future | Magazin heraus ≈ 15,94–16,09 s, Hüfte 17,917 s | Magazin heraus 16,150 s (Luftspalt), Hüfte 17,933 s | **ergänzt**, kein Widerspruch (andere Definition, 1 Bild) |
| Shattered Cipher | Zeile nennt 1920 × 1080 | lokale Datei 1280 × 720 | **ergänzt**; Bilder/60 bleibt gültig, Auflösung nur zur Kenntnis |
| Threaded Needle | [Zeile 0.7.0](destiny2.md#2-messungen-an-60-fps-aufnahmen-ab-16-oktober-2026--m): Hüfte 19,3 · ruhig ≈ 19,35 · „ruhig +3,3 s“; Matrix „3,3 s (Hüfte, Normaltempo)“ | Hüfte 19,117 s (3,08 s), ruhig 19,333 s (3,30 s) | **ergänzt:** die Ruhe (≈ 19,35 / 19,333 s) und die 3,3 s stimmen überein; der Hüftmarker weicht ≈ 11 Bilder ab (19,3 gegen 19,117 s) und ist **am Bild nicht entschieden**; Bestand bleibt stehen |
| Imperial Needle (Bogen) | Zyklus und `s-matrix-bogen` | Pfeil anlegen ≠ Magazin-Nachladen | **ergänzt als [O]** ohne Zeit |
| The Prospector | „Nicht vermessen (0.7.0)“; Matrix „Granatwerfer schwer: Ablauf nicht eindeutig“ | zwei Trommelwechsel 4,62 s und 4,48 s | **neu**, schließt die Lücke für den Exotic; legendärer Trommel-GL bleibt offen |
| Häkke-Schrotflinte (HUD), Hynra-Scharfschütze (HUD) | kein HUD-Beleg beim Nachladen | HUD in Dreierschritten; HUD 0→1 bei Reserve 1 | **neu** |
| Apex RE-45, P2020, R-301 | [apex.md](apex.md): Nachladen nur Beginn, von Loot-Animation überlagert (anderer Clip, R-99-Zeile); [auswertung.md](auswertung.md) V12 | vollständige leere Nachladungen mit HUD | **ergänzt**, kein Widerspruch; RE-45-Hüfte **korrigiert** (siehe 2) |
| Titanfall 2 P2016, CAR | [titanfall2.md](titanfall2.md): Nachladen „nur Ansätze hinter Effekten“; V12 | zwei echte Leer-/Taktisch-Paare | **ergänzt**, kein Widerspruch |
| Marathon | kein eigenes Doc (nur Erwähnungen) | drei taktische Fälle | **neu**, wie Marathon in [huefte.md](huefte.md) ohne eigenes Doc |

## 4. Muster

- **Einzelhülsen (Destiny 2; zwei Waffen, kein Klassenwert):** Hawthorne 7 Hülsen im Takt 0,617–0,633 s, Baligant 5 Hülsen im Takt 0,850–0,867 s; erste Hülse 0,60 s bzw. 0,57 s nach dem
  Beginn, ein einziges Repetieren erst nach der letzten Hülse; bis ruhig 5,88 s bzw. 5,77 s. Der Häkke-Fall mit HUD zeigt dagegen **+3 je Zuführbewegung**
  (24 Bilder = 0,400 s zwischen den Schritten) – nur für diese Perk-Kombination belegt, kein Standard für Einzelhülsen.
- **Batterie (kurze Fusion):** gleiche Figur bei Cartesian Coordinate (bis Hüfte 1,72–1,77 s, bis ruhig 1,92 s) und Shock and Awe (2,78–2,83 s, 2,87 s):
  Batterie seitlich ablösen, neue einsetzen, Handballenschlag, Rückkehr.
- **Magazin, Trommel, Gurt:** Far Future 2,18 s aus der Hüfte und 2,23 s aus dem Zielfernrohr (enthält das sichtbare Verlassen der Zielachse),
  Threaded Needle 3,30 s, Prospector 4,62 s und 4,48 s (zwei Wechsel, Schussrücklauf überlappt den ersten Beginn), Shattered Cipher 4,87 s mit
  Deckel, Trommel und Gurt als getrennte Abschnitte. Hüfte und ruhig liegen bei diesen sechs Destiny-Aufnahmen 0,12–0,45 s auseinander (Cipher 0,45 s); über die 15 Einträge mit beiden Markern
  0,03–0,45 s (Titanfall 2/Apex 0,07–0,20 s; Einzelwerte in 1).
- **HUD vor Hüfte:** In **allen 12 Fällen mit HUD-Zahl und Hüftmarker** wechselt die Munitionsanzeige **vor** der sichtbaren Rückkehr in die Hüfte, nie
  deckungsgleich: Apex 0,15 / 0,27–0,52 / 0,48 s, Titanfall 2 0,25 / 0,28 / 0,43 / 0,53 s, Marathon 0,43 / 0,45 / 0,60 s, Destiny 2 (Häkke-Schrot, Hynra-
  Scharfschütze) 1,08–1,22 s und 0,82 s. Beschreibt die Anzeige, nicht die Feuerfreigabe.
- **Leer gegen taktisch (Titanfall 2):** CAR 2,27 s leer gegen 1,85 s taktisch bis ruhig (Δ 0,42 s, zusätzlicher Griff auf der Oberseite); P2016 1,17 s
  leer gegen 1,23 s taktisch – kein Unterschied. Ein Paar je Waffe, **kein Klassenfaktor**.
- **Apex leer:** P2020 1,10 s (bis ruhig), R-301 2,38 s und RE-45 ≈ 1,85–2,10 s (bis Hüfte).
- **Marathon:** nur taktische Fälle; die Gesamtdauer ist nur bei MV01 belegt (2,10 s bis Hüfte), bei MV02/MV03 überlagern Ziehen und ADS-aus den Beginn.

## 5. Bewertung: gut, nicht so gut, für wen

Eigene Einschätzungen aus den Messzeilen, keine Spielerprobung. Die fünf Spielerthreads [C] sind per Pullpush-Archiv als Beiträge bestätigt (Subreddit,
Titel, Datum, Autor); der Kommentarverlauf wurde nicht nachgelesen. Liste in `data/nachladen.json` › `player_sources` und `dev_sources`.

| Spiel | Gegenstand | Gut (warum) | Nicht so gut (warum) | Für wen | Belege | Spielerstimmen | Entwickler / Fach |
|---|---|---|---|---|---|---|---|
| Destiny 2 | Phasenlesbarkeit und Statusübernahme (Schrot, Fusion, Scharfschütze, MG, Granatwerfer) | Lange Abläufe gliedern sich in erkennbare Abschnitte (Cipher: Deckel öffnen, Gurt, Deckel schließen; Far Future trennt Magazinsitz und Kammergriff); die Häkke-Schrotflinte zeigt die Munitionszunahme sichtbar in Dreierschritten. | Sichtbares Einsetzen oder eine Zunahme der Anzeige belegt keine Feuerfreigabe; Handverdeckung und lange Zwischenposen erschweren die Zuordnung; der reservebegrenzte Scharfschütze (Reserve 0 danach) darf nicht als voll gelten; Einzelhülsen dauern 5,77 s (Baligant) und 5,88 s (Hawthorne). | PvE: Gewichtsgefühl und Statusverständnis; PvP und Einsteiger: eindeutiger Bereitschaftshinweis und klare Abbruchregeln. | [M] Shattered Cipher 11,800–16,667 s (DEM-8xg66R8), Far Future 15,867–18,050 s (RXgRxHESqHQ), Häkke-Schrotflinte HUD 0→3→6 (lZcqE1LWRDA). | [C] Reddit r/DestinyTheGame: P1 Quicksilver Storm (17.03.2023, **Einzelstimme**: Reload-Cue ≈ 0,1 s zu früh laut Titel, nicht übernommen); P2 Riskrunner (07.12.2020) und P3 Scharfschütze (09.10.2019) – laut Zuarbeit zwei unabhängige Threads über volle Munition nach Animationsabbruch bei weiter bestehender Schusssperre. **Antworten, Gegenstimmen und Wertungen in den Threads wurden nicht nachgelesen** (nur Zuarbeit). Beiträge per Pullpush bestätigt (Subreddit, Titel, Datum, Autor); ob das Problem verbreitet ist, ist offen. | [B] Bungie Update 9.0.0.1 (MG-Nachlade-Checkpoints, laut Zuarbeit 15.07.2025): bei der Abnahme nicht abrufbar, **nicht geprüft**; die Cipher-Messung von 2021 kann die Regel ohnehin nicht belegen. |
| Apex Legends | Reihenfolge von HUD-Zunahme, Hüftlage und Leer-/Taktisch-Rückmeldung (RE-45, P2020, R-301) | Die Zunahme der Munitionsanzeige kommt in allen drei Fällen **vor** der sichtbaren Rückkehr in die Hüfte (0,15–0,52 s); Einschätzung: die Rückmeldung ist früh, wer aufs HUD schaut, weiß es vor der Pose. | Eine Regel „Hüftpose = geladen“ oder „HUD voll = feuerbereit“ trägt die Stichprobe nicht; alle drei Fälle sind leer, ein taktischer Zeitgewinn ist hier nicht belegt; Apex-Clip von 2019, Threads von 2020 und 2025. | Schnelle Nahkämpfe (PvP), Einsteiger und Spieler mit seltenem Blick aufs HUD. | [M] AV02 P2020 29,0667–30,1667 s, AV03 R-301 46,35–48,7333 s, AV01 RE-45 17,75 → ≈ 19,6–19,85 s (R-BGChzYGpo). | [C] r/apexlegends: P4 „tactical reload trick“ (20.06.2020) und P5 „TIL this“ (21.11.2025) – laut Zuarbeit zwei unabhängige Threads über Nutzen und Bekanntheit des taktischen Nachladens (Zählen unter Feuer schwierig; späte Entdeckung der zusätzlichen Kammerphase). **Inhalte der Antworten nicht nachgelesen**; kein Beleg für Verbreitung. Beiträge per Pullpush bestätigt (Scores weichen leicht ab: P4 5 statt 4, P5 54 statt 60). | keine |
| Titanfall 2 | Leer-/Taktisch-Paare derselben Waffe (P2016, CAR) | Zwei echte Paare im selben Upload machen die Zusatzarbeit des leeren Ablaufs prüfbar: CAR 2,27 s leer gegen 1,85 s taktisch bis ruhig. | Keine universelle Leer-Strafe: die P2016 braucht taktisch 1,23 s und leer 1,17 s; Marker, Poseende und Tempo-Restunsicherheit bleiben; HUD voll ist kein Feuerfreigabetest. | Spieler, die Leer-/Taktisch-Risiko lernen; Animations- und Balancingprüfung. | [M] TV01/TV02 P2016 (5,48–6,72 s, 15,58–16,75 s), TV03/TV04 CAR (94,27–96,12 s, 101,73–104,0 s) in 4sDwTD9U8bw. | keine (für Titanfall 2 wurden keine Threads ergänzt; weder Zufriedenheit noch Beschwerden behauptet) | keine |
| Marathon (2026) | Munitionsübernahme vor sichtbarer Rückkehr (drei taktische Fälle) | Die Anzeige wechselt 0,43–0,60 s vor der Hüftpassage – ein vom Pose-Ende getrennter Informationsschritt. | Gehen, transparente Effekte und überlagerte Startposen verhindern Ruhe und teils die Gesamtdauer; Modelle unbestätigt; ohne Feuerfreigabetest kein Urteil über zu frühes oder spätes Freigeben. | Einsteiger und schnelle Entscheidungen unter Bewegung; Anzeigen- und Animationstest. | [M] MV01 199,17–201,27 s, MV02/MV03 nur Hüft- und HUD-Marker (FEW1ZkadfM8). | keine | [B/S] Autodesk-Blog 20.10.2026 (Brendan Russert, Riot/Valorant): Magazin heraus, Munitionsübernahme und erneut schussfähiger Zustand als Beats, die auch bei Skins lesbar bleiben müssen; ein früher Drachen-Reload hatte einen unklaren Bereitschaftsmoment. Seite abgerufen und stützend – ein **spielübergreifendes Entwurfsziel** (Valorant), weder Marathon-spezifisch noch Bestätigung der hier gemessenen Zeiten. |

### E2 – Lehren für BASIC und Cube Escape (Vorschlag, dort entscheiden)

- **übernehmen:** Magazin-/Munitionsübernahme und den Moment, in dem die Waffe wieder bereit wirkt, als getrennte Beats entwerfen und mit demselben Spieler
  gemeinsam testen (Basis: Destiny 2, Apex, Marathon; Entwurfsziel nach [B] Riot/Autodesk). Keine festgelegte BASIC-Zeit.
- **vermeiden:** aus der Hüftpose, dem Ende der großen Rückkehrbewegung oder der Anzeige „voll“ allein auf Feuerfreigabe schließen; bei Reserveende eine
  Teilfüllung als voll darstellen (Hynra-Scharfschütze, Häkke-Schrot).
- **testen:** je Waffe einmal leer und einmal mit Restmunition aufnehmen – gleiche Start-/Enddefinition, HUD, Modell und tatsächlicher Folgeschuss
  zugleich protokolliert; Abbruch vor Übernahme, nach Übernahme und nach Bereitschaft getrennt prüfen; beim Fortsetzen festlegen, ob Neustart oder
  Checkpoint gelten soll (in P2/P3 beschreiben Spieler laut Zuarbeit/Titel Schusssperre trotz voller Anzeige – Inhalte nicht nachgelesen; ob das verbreitet ist, ist offen – den Hinweis testen). Destiny-Zahlen nicht als Startwerte kopieren.

## 6. Für Cube Escape

Cube Escape vergleicht seine Nachladeabläufe am besten gegen die Marker dieser Tabelle mit derselben Definition (Beginn, Magazin ein, HUD,
Hüfte, ruhig) bei 60/s ([cube-escape.md](cube-escape.md) hält die eigenen Bildmarker). Werte gelten mit unbekanntem FOV und unbekannten Perks; ein Vergleich
braucht eine eigene Aufnahme mit bekanntem FOV (Messplan BASIC). Keine Startwerte hier.

## 7. Offen und nicht messbar

- **Abbruch** durch Sprint oder Waffenwechsel vor der Munitionsübernahme: in keinem Fall belegt; die negativen Suchwege aus den Methoden 14 und 15 in
  [destiny2.md](destiny2.md) wurden nicht wiederholt.
- **Frühestmögliche Feuerfreigabe**, Eingabebeginn und Sperrzeiten: aus Bildern nicht ableitbar.
- **Leer-/Taktisch-Paar derselben Destiny-Waffe** fehlt; die vier Showcases haben keinen Zähler, der Häkke-Fall belegt nur „leer“. HUD +1 bei echter 60/s-Inhaltsrate
  bleibt offen (PauseResetPlay hat nur ≈ 30 Inhaltsbilder/s).
- **Kapazität** der Häkke-Schrotflinte und des Hynra-Scharfschützen unbekannt; „voll“ wird nirgends behauptet. Waffenname des Häkke-Falls nicht eingeblendet.
- **Marathon:** Waffenmodelle unbestätigt; das Normaltempo (HUD-Uhr) bei der Abnahme nicht lesbar; MV02/MV03 ohne Gesamtdauer.
- **Quellen nicht nachgeprüft:** Bungie Update 9.0.0.1 (Seite nicht abrufbar); Kommentarverläufe der fünf Reddit-Threads nicht gelesen.
- **Lücken:** legendärer Trommel-Granatwerfer; Halo, Destiny 1, CoD, Battlefield, Valorant, The Finals (30 echte Bilder/s oder zu schwache Quellen).
- **Nicht wieder versuchen:** MG-Checkpoint-Regeln aus 2021er Showcases; Apex-Inspektionsfolgen (RE-45 ≈ 5–8 s, P2020 ≈ 24 s, R-301 ≈ 40–42,8 s – Inspektion, kein
  Nachladen; Cache ab ≈ 63 s beschädigt); `ZfNuA5r-470` (Halo, 30 Inhaltsbilder in 60er-Container), `GSzouZZwDgg` (Titanfall 2, variable Duplikate),
  `WFGX_ADv1HMwkg` (ist Halo 3), `gCQHKNsIU9w` (ist R5 Reloaded).

## 8. Prüfung und Zählung

- **Zuarbeit:** 23 Einträge (22 [M], 1 [O]), 4 Spiele bzw. Spielstände, 13 Videos, laut Zuarbeit 1894 eindeutige native Messbilder (nicht nachgezählt).
  **Übernommen 20, korrigiert 3** (RE-45-Hüfte widerlegt; zwei Zeitfelder von TV03/TV04), **verworfen 0** Einträge. Von den 23 Einträgen sind **7 neu** und
  **16 ergänzen** Bestandszeilen. Verworfen wurden die kopierten Bewertungsfelder aller 23 Einträge und ein Zusatzvideo.
- **Quellen:** 13 von 13 Videos per yt-dlp bestätigt (zwei Prüfer, Sonnet 5.5), 23 von 23 Zeitstempeln innerhalb der Videolänge; Nachrechnung von Gesamtdauern,
  Frame/60 und Phasenabständen 23 von 23 ohne Abweichung. Spielerthreads 5 von 5 als Beiträge bestätigt; Fachquellen 1 von 2 bestätigt (Autodesk), Bungie nicht prüfbar.
- **Bild:** 22 Zahlen von den Prüfern nachgemessen: **21 bestätigt** (zwei mit −1 Bild: Cartesian-Start, Marathon-HUD 4→5), **1 widerlegt** (RE-45-Hüfte), dazu 1 nicht
  prüfbar (Marathon-Uhr). Eigene Nachmessung des Koordinators: Häkke-HUD 0→3 und 3→6, Hynra-HUD 0→1, Hynra-Magazin aus dem Schacht (14,317 s) und die RE-45-Hüfte (bestätigt die
  Widerlegung: Bilder bei 19,15 / 19,35 / 19,60 / 19,85 s) – 5 Zahlen, die vier HUD-/Magazinwerte innerhalb ±1 Bild; vier davon (Häkke 0→3 und 3→6, Hynra 0→1, RE-45-Hüfte) hatten auch die Prüfer
  gemessen, neu ist nur das Hynra-Magazin aus dem Schacht. Zusammen **27 Nachmessungen an 23 verschiedenen Zahlen (4 doppelt)**. Nicht am Bild nachgemessen: Far-Future-Zeilen, Cipher, Threaded Needle, Prospector Nr. 2, Marathon MV02, Titanfall TV04 (nur Rechnung und Bestand).
- **Bewertung:** Abschnitt E der Zuarbeit nur nach der Quellenprüfung übernommen; „wiederkehrend“ steht nur dort, wo zwei unabhängige Threads belegt sind (je zwei bei
  Destiny und Apex), die Einzelstimme P1 ist als solche markiert.

Schlusszeile: 4 Spiele · 23 Beispiele (20 übernommen, 3 korrigiert) · 13 Videos · 5 Spieler- und 2 Fachquellen (6 bestätigt) · 27 Nachmessungen an 23 verschiedenen Zahlen (4 doppelt).
