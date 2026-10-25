# Mündungsfeuer und Hülsenauswurf – Blitz, Überdeckung des Visiers, Hülsen, Mündungsform

Referenzanalyse REF 0.19 „Flashpan“ (25.10.2026) für die Waffenreihe **BASIC** (Projekt `cubeescape-ballon`) und Cube Escape.
Gemessen hat eine Codex-Mac-Sitzung am 24.10.2026 an nativen Einzelbildern. Diese Version hat die Ergebnisse eingepflegt, alle
Quellen per yt-dlp geprüft und fünf Werte selbst nachgemessen ([8](#8-nachmessung-und-zählung)); ein Wert ist korrigiert (Gridskipper-Höhe).
Hier stehen nur Beobachtungen und Messwerte, Schlüsse und Startwerte entstehen in BASIC bzw. Cube Escape. Getrennte Themen mit eigenen
Versionen und Docs: [Visiere](visiere.md) (0.14), [Waffenproportionen](proportionen.md) (0.15), [Rückstoßmuster](rueckstoss.md) (0.16),
[Zielbewegung](zielbewegung.md) (0.17), [Oberflächenmuster](oberflaechen.md) (0.18). Inspektionsanimationen sind ein eigenes Thema und stehen nicht hier. Maschinenlesbare Fassung:
[`data/muendung.json`](../data/muendung.json).

Die **Destiny-2-Messzeilen** stehen nach Repo-Regel in der Messtabelle [destiny2.md › 2](destiny2.md#2-messungen-an-60-fps-aufnahmen-ab-16-oktober-2026--m)
(Anker `z-mf-…`, [Methode 18](destiny2.md#methode-18)). Dieses Doc fasst sie in [3](#3-destiny-2--übersicht) zusammen und enthält
Destiny 1, den Vergleich mit Halo Infinite, Titanfall 2, Apex Legends, Call of Duty: Modern Warfare (2019), Borderlands 3 und
Battlefield 6, die Muster und die Grenzen. Schon vorhandene Mündungsmessungen aus REF 0.11.17 „Ballista“ ([Methode 16](destiny2.md#methode-16):
Chroma-Rush-Hüftschuss, Baligant, Blue Shift, Ignition Code, Cartesian Coordinate, Shock and Awe, Eyes of Tomorrow, Prometheus Lens,
Imperial-Needle-Fächer) sind nicht wiederholt.

**Status:** **[M]** gemessen am nativen Einzelbild; **[M/O]** gemessen, Teile nur gesichtet; **[O]** Sichtung ohne belastbare Zahl.
**Jede Zahl ist das Beispiel einer Waffe** in einer Aufnahme mit unbekanntem FOV und unbekannten Perks, kein Klassenmittel.

## 1. Methode und Genauigkeit

- **Größe und Lage** in Prozent der gesamten Bildbreite B bzw. Bildhöhe H, Ursprung oben links, Bildmitte 50/50; Kanten und Lagen ±3 pp,
  abgelesen an 960-px-Einzelbildern mit 10-%-Raster. **Blitzgröße** = Hüllrechteck des zusammenhängenden, waffennahen Feuerbereichs im
  Peakbild, keine segmentierte Flammenfläche. Abgesetzte Funken, Leuchtspuren, Wandtreffer und Dauerleuchten am Modell zählen nicht mit;
  diffuse oder vom Bildrand beschnittene Bereiche bleiben ohne Zahl.
- **Überdeckung** = überstrahlter Anteil der lichten Visieröffnung, nur bei Glas oder Holo mit begrenzter Öffnung, ±5–15 pp. Offene
  Kimmen und ausgeblendete Mündungen (Vollbild-Scope) bekommen **keinen** Prozentwert, auch nicht 0 %.
- **Zeiten** nur bei 60/s-Quellen mit belegtem Normaltempo ([destiny2.md › Methode 10](destiny2.md#2-messungen-an-60-fps-aufnahmen-ab-16-oktober-2026--m)),
  in nativen Bildern ab absoluten Bildindizes: Marker ±1 Bild, Abstände ±2 Bilder. 30/s-Quellen (D1, New Malpais) und 60/s-Container mit
  paarweise wiederholtem Inhalt (Halo, Apex) liefern nur Form und Größe. Übersichtskacheln von `reference_frames.py sheet` dienten nur der
  Navigation – sie zeigen bei niedriger Bildrate ein Bild eine halbe Abtastperiode nach ihrer Beschriftung ([LESSONS](LESSONS.md)).
- **Hülsen:** „Verzögerung 0“ heißt, die erste Hülse ist im ersten Blitzbild **sichtbar** (±2 Bilder) – kein Nachweis exakter
  Gleichzeitigkeit und nicht der verborgene mechanische Beginn im Auswurffenster. Hülsengrößen sind **Perspektivgrößen** beim nahen
  Vorbeiflug, keine Patronenmaße. In langen Stößen sind ältere Hülsen nicht beliebig dem neuesten Schuss zuzuordnen.
- **Null-Regel:** null = nicht messbar. Kein sichtbarer Blitz ist kein Nullblitz, keine sichtbare Hülse kein Beweis hülsenlosen Betriebs.
- **Mündungsform** aus Ego- und Menübild (Ultraclocked-Startmenüs zeigen die ruhende Außengeometrie, kein äußeres Schussbild); Anteile =
  Teil der sichtbaren Waffenlänge. Ports und Zacken belegen keine physikalische oder technische Ursache der Effektform.

## 2. Quellen

Alle 20 Modellquellen am 25.10.2026 per yt-dlp gegen Kanal, Hochladedatum und Titel geprüft – alle stimmen mit der Codex-Angabe überein.
Zeiten beziehen sich auf das **Originalvideo**, außer wo „lokal“ steht.

| Spiel | Kanal · Hochladedatum · Video | Waffe(n) | Bildrate / Hinweis |
|---|---|---|---|
| Destiny 2 | Ultraclocked · 15.02.2021 · [Y5OLr0nbgSg](https://www.youtube.com/watch?v=Y5OLr0nbgSg) | Extraordinary Rendition | 1920 × 1080, 60/s |
| Destiny 2 | Ultraclocked · 13.05.2021 · [DFn14wAPluA](https://www.youtube.com/watch?v=DFn14wAPluA) | Gridskipper | 1920 × 1080, 60/s |
| Destiny 2 | Ultraclocked · 15.05.2021 · [QxSa4m3wIEA](https://www.youtube.com/watch?v=QxSa4m3wIEA) | Chroma Rush | 1920 × 1080, 60/s |
| Destiny 2 | Ultraclocked · 18.02.2021 · [RXgRxHESqHQ](https://www.youtube.com/watch?v=RXgRxHESqHQ) | Far Future | 1920 × 1080, 60/s |
| Destiny 2 | Ultraclocked · 20.02.2021 · [uoTaCBMXcFk](https://www.youtube.com/watch?v=uoTaCBMXcFk) | Threaded Needle | 1920 × 1080, 60/s |
| Destiny 2 | Ultraclocked · 19.02.2021 · [dKNTDzi__Qo](https://www.youtube.com/watch?v=dKNTDzi__Qo) | Imperial Needle | 1920 × 1080, 60/s |
| Destiny 2 | Ultraclocked · 14.02.2020 · [IG-GZ72Vbi0](https://www.youtube.com/watch?v=IG-GZ72Vbi0) | Tone Patrol, Annual Skate, First In, Last Out | SUROS-Sammelvideo, 60/s; Ausschnittversätze +375,000 s / +53,000 s per Bildabgleich bestätigt |
| Destiny 2 | Ultraclocked · 25.01.2020 · [73lGCT7yOtk](https://www.youtube.com/watch?v=73lGCT7yOtk) | Minimum Distance | Häkke-Sammelvideo, Kapitel 408–450 s; Ausschnittversatz ungeprüft, Zeiten lokal |
| Destiny 2 | Ultraclocked · 14.05.2021 · [DEM-8xg66R8](https://www.youtube.com/watch?v=DEM-8xg66R8) | Shattered Cipher | 1280 × 720, 60/s |
| Destiny 2 | Amanda Golla · 18.01.2026 · [-i74Bk7Sz0c](https://www.youtube.com/watch?v=-i74Bk7Sz0c) | New Malpais | **Entwickler-VFX-Portfolio**, 1280 × 720, 30/s, Build unbekannt; [ArtStation-Projekt](https://amandanicole21.artstation.com/projects/AZJG1e) am 25.10.2026 gelesen |
| Destiny 1 | NOIZION · 05.09.2020 · [vzFORMU5J84](https://www.youtube.com/watch?v=vzFORMU5J84) | Hawkmoon, Thorn | 720p, 29,97/s, Kapitel 23 s / 53 s |
| Destiny 1 | Great Daemon · 23.11.2015 · [MjugMsHa_0o](https://www.youtube.com/watch?v=MjugMsHa_0o) | Doctrine of Passing | 30/s |
| Destiny 1 | Eris Jolley · 07.01.2016 · [VNprDRKZxt8](https://www.youtube.com/watch?v=VNprDRKZxt8) | Arminius-D (Menü) | 30/s |
| Destiny 1 | Jumping Puzzle · 05.03.2015 · [MkkQa1OIpDk](https://www.youtube.com/watch?v=MkkQa1OIpDk) | MIDA Multi-Tool (Menü) | 30/s |
| Halo Infinite | Abyssopelagic · 30.07.2021 · [ZfNuA5r-470](https://www.youtube.com/watch?v=ZfNuA5r-470) | MA40, BR75, MK50 Sidekick | **erste Technical Preview**, 60/s-Container mit Paarduplikaten |
| Titanfall 2 | Weapons From Games · 14.03.2019 · [4sDwTD9U8bw](https://www.youtube.com/watch?v=4sDwTD9U8bw) | Hammond P2016, B3 Wingman, Smart Pistol MK6 | 60/s |
| Apex Legends | Cacek47 · 06.02.2019 · [R-BGChzYGpo](https://www.youtube.com/watch?v=R-BGChzYGpo) | RE-45, P2020, R-301 | 60/s-Container mit Paarduplikaten; Datei nach ≈ 80 s defekt |
| CoD MW (2019) | Tigerfield · 26.10.2019 · [_KTdg4YM1fQ](https://www.youtube.com/watch?v=_KTdg4YM1fQ) | X16, 1911, .357 | 60/s, Ausschnitt 0–75 s |
| Borderlands 3 | Agent Lomax · 15.03.2020 · [3T2UZUYPzEc](https://www.youtube.com/watch?v=3T2UZUYPzEc) | Entrepreneur, Mogul, Broodmother (Hyperion) | 60/s, Schuss über HUD-Zähler |
| Battlefield 6 | Torbis · 17.09.2025 · [ROUP1z62caA](https://www.youtube.com/watch?v=ROUP1z62caA) | B36A4, AK4D, A-545 | 1920 × 1080, 60/s, im Bild als **„Recorded in pre-launch build“** gekennzeichnet |

**Nur Suche oder ausgeschlossen** (ebenfalls per yt-dlp bestätigt): Skeptation `gCQHKNsIU9w` (08.11.2021, Modded Apex/R5Reloaded – kein
Retailbeleg), Hoodiewaffles `qI_IWMuH_Zs` (18.08.2020, CoD-Optiken ohne Schuss in den Suchfenstern AUG 10–18 s, P90 75–83 s,
MK2 Carbine 102–110 s), Zagzogs `xygk-adR6pg` (06.11.2019, 30/s), Ultraclocked `Td1dW-moo4o` (07.06.2025, BL3-Nachladeschnitt),
Agent Lomax `Nwp4VJWUujY` (02.10.2019, Vladof-Fenster bei 25 s mit Mündungs-/Zielpartikeln überlagert).

**New Malpais:** Die Schöpferin nennt auf ArtStation ihre VFX-Arbeit an dieser Destiny-2-Waffe, darunter den grünen Strand-Effekt am
Lauf **beim Granatschuss** und eine zusätzliche Mündungsfeuer-Karte. Ob die gemessenen Außenschüsse Granat- oder Pulsschüsse sind, ist
nicht getrennt. Das Video trägt Bungie-/Destiny-2-Einblendungen, Build und Aufnahmezeit sind nicht ausgewiesen: **kein Nachweis des
aktuellen Spielstands**.

## 3. Destiny 2 – Übersicht

Volle Zeilen mit Zeitstempeln und Grenzen: Spalte „Zeile“ (destiny2.md › 2). Bilder = native Bilder bei 60/s; „–“ = nicht messbar.

| Waffe (Klasse) | Ansicht | Kern / gesamt | Blitz B × H, Mitte | Überdeckung | Hülse | Mündungsform | Zeile |
|---|---|---|---|---|---|---|---|
| Extraordinary Rendition (MP) | ADS, offene Kimme | 2 / 2 | 10 × 10 %, 50/75 | – (keine Öffnung) | im 1. Blitzbild, rechts nach unten | langes offenes Rohr, goldene Längsstreben (≈ 38 %) | [z-mf-rendition](destiny2.md#z-mf-rendition) |
| Gridskipper (Impuls) | ADS, Holo | 1 / 2 | 20 × 15 %, 50/77 (Seitenzungen) | ≈ 5 % | im 1. Blitzbild, rechts unten | kurzer offener Kopf mit Seitenfenster (10–15 %) | [z-mf-gridskipper](destiny2.md#z-mf-gridskipper) |
| Chroma Rush (Auto) | ADS, Holo | 2 / 2 | 20 × 40 %, 50/65 | ≈ 20 % | 1 Bild nach Blitz, rechts | lange geschlitzte Vorderhülle (40–45 %) | [z-mf-chroma-rush-ads](destiny2.md#z-mf-chroma-rush-ads) |
| Far Future (Scharfschütze) | Hüfte; Scope | 2 / 2 | 14 × 35 %, 55/63 | – (Mündung im Scope ausgeblendet) | – | langer schlanker Lauf, goldener Schlitzabschnitt (≈ 25 %) | [z-mf-far-future](destiny2.md#z-mf-far-future) |
| Threaded Needle (lineare Fusion) | ADS, Gabel | – | – (beschnitten, diffus) | – | – im Fenster | zwei Spitzen um dunklen Emitter (≈ 27 %) | [z-mf-threaded-needle](destiny2.md#z-mf-threaded-needle) |
| Imperial Needle (Bogen) | ADS | – | kein Gas-Mündungsfeuer | – | n. z. | kein Lauf, Pfeilauflage am Griff | [z-mf-imperial-needle](destiny2.md#z-mf-imperial-needle) |
| Tone Patrol (Scout) | ADS, Glas | – (Tempo des Fensters offen) | 55 × 45 % | ≈ 50 % | – | schmaler Lauf vor perforiertem Mantel (≈ 40 %) | [z-mf-tone-patrol](destiny2.md#z-mf-tone-patrol) |
| Annual Skate (Handfeuerwaffe) | Hüfte | – | 28 × 42 %, 60/35 | – | – (Trommel später = Nachladen) | runde obere Bohrung im Rechteckgehäuse | [z-mf-annual-skate](destiny2.md#z-mf-annual-skate) |
| Minimum Distance (Sidearm) | Hüfte und ADS | – | 14 × 20 %, ADS 50/55 | – (offene Kimme, Korn kurz verdeckt) | – | kleine Bohrung bündig in der Schlittenstirn | [z-mf-minimum-distance](destiny2.md#z-mf-minimum-distance) |
| Shattered Cipher (MG) | ADS, Holo | 2 / 2 | 25 × 35 %, 50/65 | ≈ 40 % | im 1. Blitzbild, ≈ 85/90 | kurzes offenes Endstück (≈ 6 %) vor geschlitztem Mantel | [z-mf-shattered-cipher](destiny2.md#z-mf-shattered-cipher) |
| First In, Last Out (Schrot) | ADS, Holo | – | 30 × 45 % | ≈ 100 % am Peak | – | kleiner Lauf bündig in glatter Vorderhülle | [z-mf-filo](destiny2.md#z-mf-filo) |
| New Malpais (Impuls) | **außen**, Seitenprofil | – (30/s) | – (links beschnitten) | – | – | dunkler kurzer Laufkopf | [z-mf-new-malpais](destiny2.md#z-mf-new-malpais) |

Ergänzend aus Ballista (nicht neu gemessen): Chroma Rush **Hüfte** – Kern 2 Bilder ≈ 7 %, erste Hülse 2 Intervalle nach dem Blitz
([z-ballista-chroma-rush](destiny2.md#z-ballista-chroma-rush)); Baligant Hüfte – Kern 3 Bilder ≈ 20 %, Flammenkranz 7 Bilder ≈ 30 %
([z-ballista-baligant](destiny2.md#z-ballista-baligant)); Imperial Needle – blauer Entladefächer 2 Bilder ≈ 22 %
([z-ballista-imperial-needle](destiny2.md#z-ballista-imperial-needle)).

## 4. Destiny 1

Alle Quellen 30/s: Form und Größe, **keine Zeiten**. Aufnahmejahrgang nicht als heutiger Stand übertragen.

| Vorgang | Clip (Kanal, Datum, Video) | Zeit / Bild | Messung und Grenze |
|---|---|---|---|
| **Hawkmoon (Handfeuerwaffe): ADS und Hüfte** [M/O] <a id="z-mf-d1-hawkmoon"></a> | NOIZION, 05.09.2020, [vzFORMU5J84](https://www.youtube.com/watch?v=vzFORMU5J84) | ADS 31,431 (f942); Hüfte 43,610 / 44,044 | ADS: Hüllrechteck **≈ 30 × 40 %** um 57/56, unregelmäßiger gelbweißer Stern mit seitlichen Lappen, orange/roter Saum; nach oben abgesetzte Funken nicht addiert. Korn und Zielachse überstrahlt, keine Glasöffnung. Hüftpeak oben beschnitten. Kurzer Lauf in hoher kantiger Laufhülle, Korn oben, keine eigenständige Bremse abgrenzbar. Keine Schuss-Hülse im Fenster. Nachmessung 0.19: ≈ 32 × 37 % um 58/54 (HUD 12 → 11) |
| **Thorn (Handfeuerwaffe): ADS und Hüfte** [M/O] <a id="z-mf-d1-thorn"></a> | dieselbe Quelle | ADS 63,630 (f1907); Hüfte 71,672 (f2148) | ADS: **≈ 55 × 45 %** um 54/47, heller runder Kern, waagerechte Flügel weit über den Lauf, grünlicher Nebelsaum (weißgrün); ständig grüne Flecken am Gehäuse nicht gezählt. Hüftpeak beschnitten. Kurze zentrale Laufgruppe zwischen gezackten Hüllenteilen – keine Gasführung durch die Zacken belegt |
| **Doctrine of Passing (Auto): ADS** [M] <a id="z-mf-d1-doctrine"></a> | Great Daemon, 23.11.2015, [MjugMsHa_0o](https://www.youtube.com/watch?v=MjugMsHa_0o) | 8,000 | **≈ 45 × 40 %**, zweiflügeliger seitlicher Fächer, heller Kern über dem Lauf, roter Halo; die Flammen flankieren die Kimme, der Kern erhellt den unteren offenen Visierbereich (kein Prozentwert). Kurze zylindrische Mündungsgruppe |
| **Arminius-D (Auto): Menü** [O] <a id="z-mf-d1-arminius"></a> | Eris Jolley, 07.01.2016, [VNprDRKZxt8](https://www.youtube.com/watch?v=VNprDRKZxt8) | 58,000 | Nur Geometrie: kurzer leicht aufgeweiteter schwarzer Laufabschluss vor freiliegendem schlankem Lauf. Kein Schuss, kein Nullblitz |
| **MIDA Multi-Tool (Scout): Menü** [O] <a id="z-mf-d1-mida"></a> | Jumping Puzzle, 05.03.2015, [MkkQa1OIpDk](https://www.youtube.com/watch?v=MkkQa1OIpDk) | 285,000 | Nur Geometrie: kurze rechteckige Mündungsöffnung bündig am bullpupartigen Gehäuse, kein langer freier Lauf |

## 5. Vergleich: Halo Infinite, Titanfall 2, Apex Legends, Call of Duty, Borderlands 3, Battlefield 6

Historische Aufnahmefassungen (Halo-Technical-Preview 2021, Apex 2019, BF6-Vorabbuild 2025). Beobachtete Gestaltungsprinzipien, kein
kontrollierter Vergleich gleicher FOV-, Licht- und Versionsbedingungen. Halo und Apex: 60/s-Container mit paarweise wiederholten
Spielbildern, deshalb **keine Dauer**; Titanfall, CoD, Borderlands und BF6: Blitzkern meist nicht getrennt, Dauer und Hülsendelay null.

| Vorgang | Clip (Kanal, Datum, Video) | Zeit (s) | Messung und Grenze |
|---|---|---|---|
| **Halo Infinite, MA40 (Auto): Hüfte** [M] <a id="z-mf-halo-ma40"></a> | Abyssopelagic, 30.07.2021, [ZfNuA5r-470](https://www.youtube.com/watch?v=ZfNuA5r-470) | 8,683 (Containerbilder 521–536) | **≈ 14 × 35 %** um 61/67, asymmetrischer drei- bis vierzackiger Stern, weißgelb/orange; kurzer Laufabschluss unter hohem Gehäuse |
| **Halo Infinite, BR75 (Impuls): Hüfte** [M] <a id="z-mf-halo-br75"></a> | dieselbe Quelle | 65,000 | **≈ 20 × 38 %**, seitlich aufgefächerter Stern rechts unter der Bildmitte; Blick außerhalb des Blitzes überwiegend frei. Kurzer Lauf vor Bullpup-Gehäuse |
| **Halo Infinite, MK50 Sidekick (Pistole): Hüfte** [M] <a id="z-mf-halo-mk50"></a> | dieselbe Quelle | 86,067 | **≈ 10 × 16 %**, kleiner runder/fransiger Kegel am hochspringenden Lauf um 62/48, oberhalb des Ausgangsvisiers |
| **Titanfall 2, Hammond P2016 (Pistole): ADS** [O] <a id="z-mf-tf2-p2016"></a> | Weapons From Games, 14.03.2019, [4sDwTD9U8bw](https://www.youtube.com/watch?v=4sDwTD9U8bw) | 12,250 | Schuss, Rückstoß und erste Hülse bei 12,250; das Visier verdeckt die Kernzone. Hülse ≈ 1–2 % B, fliegt rechts, dann rechts unten und wächst |
| **Titanfall 2, B3 Wingman (Revolver): ADS** [O] <a id="z-mf-tf2-wingman"></a> | dieselbe Quelle | 33,633 | Zähler 6 → 5, Rückstoß ab 33,683; nur blasser Rauch-/Lichthalo über dem Lauf, keine freie Flammenkontur; kein Hülsenauswurf beim Schuss (38,0–38,5 ist Nachladen) |
| **Titanfall 2, Smart Pistol MK6: Hüfte** [M] <a id="z-mf-tf2-smart"></a> | dieselbe Quelle | 75,417 | **≈ 4 × 7 %**, kleiner runder Lichtpuls, Zähler 12 → 11; Hülse danach rechts, Delay null (Kernbeginn an verdeckter Laufkante unklar) |
| **Apex, RE-45 (Automatikpistole): Hüfte** [M] <a id="z-mf-apex-re45"></a> | Cacek47, 06.02.2019, [R-BGChzYGpo](https://www.youtube.com/watch?v=R-BGChzYGpo) | 10,000 | **≈ 8 × 10 %**, kleiner fransiger gelboranger Kegel direkt vor dem Lauf; große rotierende Messinghülse ≈ 2–3 % B nach rechts oben |
| **Apex, P2020 (Pistole): Hüfte** [O] <a id="z-mf-apex-p2020"></a> | dieselbe Quelle | 25,383 | Einzelschuss, Rückstoß und Hülse (rechts oben, dann zurückfallend), Blitzkern nicht getrennt |
| **Apex, R-301 (Auto): ADS, offene Kimme** [M] <a id="z-mf-apex-r301"></a> | dieselbe Quelle | 50,017 | **≈ 28 × 25 %**, zwei seitliche orange Flammen am Visierfuß; die Öffnungsmitte bleibt sichtbar, die Flammen flankieren statt zu füllen (nicht segmentiert). Hülse rechts oben, ≈ 2–3 % B |
| **CoD MW (2019), X16 (Pistole): Hüfte** [O] <a id="z-mf-cod-x16"></a> | Tigerfield, 26.10.2019, [_KTdg4YM1fQ](https://www.youtube.com/watch?v=_KTdg4YM1fQ) | 5,867 | Schüsse, Schlittenhub, Hülsen (rechts oben, ≈ 2 % B) und heller Rauch; kein isolierter Kern in der Tageslichtansicht |
| **CoD MW (2019), 1911 (Pistole): Hüfte** [O] <a id="z-mf-cod-1911"></a> | dieselbe Quelle | 33,250 | Schuss und Rückstoß, Kern unaufgelöst; Geometrie- und Ablaufbeleg, kein belegtes fehlendes Mündungsfeuer |
| **CoD MW (2019), .357 (Revolver): Hüfte** [O] <a id="z-mf-cod-357"></a> | dieselbe Quelle | 51,017 | Heller diffuser Rauchpuff vor dem langen Lauf, Kern nicht getrennt; kein Hülsenauswurf beim Schuss (53,8–54,3 ist Öffnen/Nachladen) |
| **Borderlands 3, Entrepreneur (Hyperion, Scharfschütze)** [O] <a id="z-mf-bl3-entrepreneur"></a> | Agent Lomax, 15.03.2020, [3T2UZUYPzEc](https://www.youtube.com/watch?v=3T2UZUYPzEc) | 180,567 | Zähler 7 → 6; orange Aufhellung um Lauf und Vordergehäuse, keine freie Kernkontur, kein Hülsendelay |
| **Borderlands 3, Mogul (Hyperion)** [O] <a id="z-mf-bl3-mogul"></a> | dieselbe Quelle | 210,033 | Waffe und Vordergehäuse leuchten weiß auf; Flammenkontur nicht von Material-/Umgebungslicht getrennt |
| **Borderlands 3, Broodmother (Hyperion)** [O] <a id="z-mf-bl3-broodmother"></a> | dieselbe Quelle | 270,000 | Violetter Ring/heller Energiekern laufnah, ab 270,300 große gelbe Nahzielüberlagerung; Projektil, Mündungslicht und Partikel nicht getrennt, Größe und Dauer null |
| **Battlefield 6, B36A4 (Sturmgewehr): Hüfte** [M/O] <a id="z-mf-bf6-b36a4"></a> | Torbis, 17.09.2025, [ROUP1z62caA](https://www.youtube.com/watch?v=ROUP1z62caA) | 19,000–20,200; Raster 19,650; Form 36,000 | Mündung ≈ 54/58, kurzer rosaroter Lichtansatz; roter Strich Richtung 50/50 ist Leuchtspur. Hülse bei 19,650 ≈ 75/51, ≈ 1–2 × 1–2 %, rechts leicht hoch. Im Nachladen rechteckiges Auswurffenster rechts am Gehäuse |
| **Battlefield 6, AK4D: Hüfte** [M/O] <a id="z-mf-bf6-ak4d"></a> | dieselbe Quelle | 43,000–44,200; Raster 43,733; Form 56,000 | Mündung ≈ 54/55, HUD 19 → 9; Kern nicht von Hintergrund/Leuchtspur getrennt (nicht als 0 Bilder werten). Goldene Hülse bei 43,733 ≈ 70/50, ≈ 3 × 2 %, diagonal rechts/leicht hoch |
| **Battlefield 6, A-545 (Sturmgewehr): ADS, offene Kimme** [M/O] <a id="z-mf-bf6-a545"></a> | dieselbe Quelle | 67,000–68,200; Raster 67,033; Form 79,000 | Mündung hinter/unter der Visierachse, keine freie Kontur (keine 0-%-Überdeckung). Hülse bei 67,033 ≈ 90/53, ≈ 6 × 2 % (Perspektivgröße), helles Messing mit dunkler Öffnung |

## 6. Muster

Beobachtungen über die Beispiele hinweg, keine Gestaltungsregeln: was BASIC daraus macht, entscheidet `cubeescape-ballon`.

- **Kurzer Kern, breite Seitenflammen:** In Destiny steht ein kleiner heller Kern (MP-Halbkreis 10 × 10 %, Impulskegel wenige % B) neben
  deutlich breiteren Seitenflammen (Scout 55 % B, Schrot 30 × 45 %, MG 25 × 35 %). Wo 60/s und Normaltempo belegt sind, dauert der Blitz
  **1–2 Bilder** (Rendition, Gridskipper, Chroma Rush, Far Future, Shattered Cipher). Große Feuerflächen sitzen dabei an schmalen
  Laufenden (MG: offenes Endstück ≈ 6 % der sichtbaren Länge, 25 × 35 % Feuer).
- **Visier bleibt meist lesbar, aber nicht immer:** Die Destiny-ADS-Beispiele überstrahlen 5 % (Gridskipper), 20 % (Chroma), 40 % (MG),
  50 % (Scout) bis praktisch 100 % am Peak (Schrot) der lichten Öffnung – keine universelle Destiny-Regel. Apex R-301 und D1 Doctrine
  lassen Flammen die Kimme **flankieren**; Minimum Distance verdeckt das Korn kurz.
- **Goldene Hülsen neben Energieeffekten:** Rendition, Gridskipper und Shattered Cipher zeigen die erste Hülse schon im ersten
  Blitzbild, Chroma Rush ein Bild später (Hüfte, Ballista: zwei). Effektfarbe und Hülsenlosigkeit sind nicht gleichzusetzen; bei
  Threaded Needle, Tone Patrol, Annual Skate, Minimum Distance und First In, Last Out ist im Fenster keine Hülse sicher sichtbar.
- **Farbe trägt Identität:** D1 Hawkmoon (warmer Stern) und Thorn (weißgrüne Flügel) unterscheiden sich bei gleicher Klasse stark;
  Dauerleuchten am Modell ist ein getrennter Effekt. New Malpais zeigt außen einen grünweißen Fächer mit Ringresten.
- **Halo und Apex:** gut lesbare Sternformen; die Apex-Hülsen fliegen rechts oben (für Halo ist keine Hülsenrichtung erfasst).
  Inhaltsduplikate begrenzen die zeitliche Auflösung.
- **CoD und BF6:** in den gewählten Fenstern eher Gehäusebewegung, Rauch und Hülsen als ein isolierbarer heller Kern; BF6 zeigt im
  Nachladen getrennte rechteckige Auswurffenster.
- **Form:** offene zylindrische Endstücke (MG ≈ 6 %, Impuls 10–15 % der sichtbaren Länge) vor geschlitzten Mänteln; Energiewaffen mit
  Emitter statt Laufmund (Threaded Needle); Bohrungen bündig in Schlitten- oder Gehäusestirn (Minimum Distance, Annual Skate, First In,
  Last Out, MIDA). Ein separates Auswurffenster ist in den Ego-Bildern nur bei BF6 im Nachladen klar zu sehen.

## 7. Nicht messbar / offen

Damit keine Sitzung dieselben Wege erneut versucht:

- **Außenfeuer im Retailspiel:** nur der Entwickler-Außenbeleg New Malpais (30/s, links beschnitten, Build unbekannt). Startmenüs zeigen
  die ruhende Geometrie, kein Schussbild. Vollständige Paare außen/Hüfte/ADS je Waffe fehlen.
- **Dauer** bei 30/s (D1, New Malpais) und in Containern mit Inhaltsduplikaten (Halo, Apex); **Normaltempo** der Fenster Tone Patrol,
  Annual Skate, Minimum Distance, Threaded Needle und First In, Last Out nicht neu geprüft – Zeitfelder null. Minimum Distance: Ausschnittversatz offen.
- **Threaded Needle:** diffuse Ring-/Aufhellungsphase ohne isolierten Kern; **Imperial Needle:** kein Gasblitz (Bogen), Hülse nicht zutreffend.
- **Hülsen:** 3D-Flugbahn, Rückwärtskomponente, mechanischer Auswurfbeginn und Ladehebelbewegung aus einer Kamera nicht ableitbar;
  in langen Stößen keine Zuordnung zur einzelnen Patrone (BF6 B36A4).
- **Rauch-Endmarker**, physische Mündungslänge/-dicke in mm, Geschossgeschwindigkeit, Engine-Emitterdaten: nicht aus Bildproportionen.
- **Weitere D2-Klassen:** kurze Fusion, Granat-/Raketenwerfer, Spurgewehr, Glefe/Schwert hier nicht neu gemessen (teils in
  [Methode 16](destiny2.md#methode-16)); normale gegen energetische Varianten und Ornamentpaare wären eigene Ergänzungen.
- **Gesichtet ohne Beleg:** CoD-Optikvideos (Hoodiewaffles, Zagzogs) ohne Schuss, BL3 Vladof (Partikel), Apex-Datei nach ≈ 80 s defekt,
  Skeptation Modded Apex – siehe [2](#2-quellen).

## 8. Nachmessung und Zählung

**Nachmessung REF 0.19 (25.10.2026, Mac):** eigene Dekodierung ab Dateianfang mit absoluten Bildindizes (kein Suchsprung), eigene
960-px-Rasterbilder mit 10-%-Raster, dazu Hellwert-Differenz gegen das Bild drei Bilder vor dem Schuss. Vier Werte bestätigt, einer korrigiert:

| Wert | Codex | Nachmessung | Ergebnis |
|---|---|---|---|
| Shattered Cipher, ADS-Puls (f1838) | 2 Bilder; 25 × 35 % um 50/65; Hülse im 1. Blitzbild ≈ 85/90; Pulsabstand 4 | 2 Bilder (f1838–1839, f1840 nur violette Spuren); ≈ 26 × 34 % um 50/69; Hülse im 1. Blitzbild ≈ 84/91; nächster Puls f1842 | bestätigt |
| Extraordinary Rendition, ADS (f2403) | 2 Bilder; 10 × 10 % um 50/75; Hülse im 1. Blitzbild | 2 Bilder (f2403–2404); ≈ 9 × 10 % um 50/77; Hülse im 1. Blitzbild am rechten Rand | bestätigt |
| Gridskipper, ADS-Puls (f1627) | Kern 1, gesamt 2; 20 × 25 % um 50/68 | Kern 1, Seitenzungen auch in f1628; Seitenzungen ≈ 20 × 13–16 % um 50/77, mit dem getrennten Glaskegel ≈ 38 % H; Hülse im 1. Blitzbild | **korrigiert:** Höhe 15 % (Seitenzungen), Kegel getrennt genannt |
| Chroma Rush, ADS-Puls (f1389) | 2 Bilder; 20 × 40 % um 50/65; Hülse +1 | 2 Bilder (Restschimmer in f1391 an der ±1-Grenze); ≈ 15 × 36 % (erster Puls nur links seitlich); Hülse in f1390 | bestätigt, Breite am Toleranzrand |
| D1 Hawkmoon, ADS (f942 bei 29,97/s) | 30 × 40 % um 57/56 | ≈ 32 × 37 % um 58/54; HUD 12 → 11 | bestätigt |

Skript und Rasterbilder im Scratch dieser Sitzung, nicht im Repo; Codex-Arbeitsdaten (Bögen, Rasterbilder, `seqsheet.py`,
`match_offsets.py`, Sidecars) im Cache unter `~/Library/Caches/CubeEscape/reference/visiere/codex2/`.

**Zählung der Codex-Sitzung:** **8 Spiele, 35 Waffenmodelle, 20 Modellquellen-Videos**; mindestens **1779 native Mess-, Form- und
Abgrenzungsbilder** plus 62 Übersichtsbilder (1841 gezählte Quellbildindizes): Destiny 2 792 native Bilder (738 bei 60/s, 54 bei 30/s),
Vergleichsteil 648 Containerbildindizes, BF6 219, D1-Ergänzung 120 native Formbilder. Negativfenster zählen als Abgrenzungsprüfung, nicht als
zusätzliche Blitzmessungen; Quellbildindizes sind keine Zahl verschiedener Spielzustände.
