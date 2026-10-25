# Zielbewegung im Zielen – Sway, Rückstoß im ADS, Punkt im Glas, Hüfte → Zielen

Referenzanalyse REF 0.17 „Steadyhand“ (25.10.2026) für die Waffenreihe **BASIC** (Projekt `cubeescape-ballon`) und Cube Escape.
Gemessen hat eine Codex-Mac-Sitzung (`gpt-6.1-sol` high, 24.10.2026) an 60/s-Aufnahmen. Diese Version hat die Ergebnisse
eingepflegt, die Quellen per yt-dlp geprüft und fünf Werte selbst nachgemessen ([8](#8-nachmessung-und-zählung)). Hier stehen nur
Beobachtungen und Messwerte. Schlüsse und Startwerte entstehen in BASIC bzw. Cube Escape. Getrennte Themen mit eigenen Versionen und Docs:
[Visiere](visiere.md) (0.14); Rückstoßmuster und weitere Themen folgen in eigenen Versionen. Maschinenlesbare Fassung:
[`data/zielbewegung.json`](../data/zielbewegung.json).

Die **Destiny-2-Messzeilen** stehen nach Repo-Regel in der Messtabelle [destiny2.md › 2](destiny2.md#2-messungen-an-60-fps-aufnahmen-ab-16-oktober-2026--m)
(Anker `z-zb-…`). Dieses Doc fasst sie in [3](#3-destiny-2--übersicht) zusammen und enthält den Vergleich mit Battlefield 2042, Apex
Legends und Halo Infinite, die Muster und die Grenzen.

**Status:** **[M]** gemessen (Vorlagenverfolgung oder Bildmaßstab); **[O]** Sichtbefund ohne belastbare Zahl; **[M/O]** gemessen, Teile nur
gesichtet. **Jede Zahl ist das Beispiel einer Waffe** in einer Aufnahme mit unbekanntem FOV, Handling, Stabilität und Perks, kein Klassenmittel.

## 1. Methode und Genauigkeit

- **Verschiebungen** in **Prozentpunkten (pp) der gesamten Bildbreite B bzw. Bildhöhe H**, Ursprung oben links, rechts/unten positiv.
  Lage ±3 pp; die Differenz zweier getrennt gefundener Marker (Punkt gegen Rahmen) konservativ bis **±6 pp**. Feinere Rohwerte stehen nur
  zur Nachvollziehbarkeit da.
- **Zeiten** in nativen Videobildern ab dem genannten Marker, ±1 Bild, Abstände bis ±2 Bilder. Bei Einzelschüssen zählt der Blitz, bei
  Stößen und Salven der **letzte Schuss**. Native Taktrate aus ffprobe (`r_frame_rate`): Destiny 60/1, Battlefield 60000/1001, Apex und Halo
  60/1, ClawZ (R-301) 7479/250 ≈ 29,9/s, dort nur Form und Lage. OpenCV-Mittelwerte fragmentierter Dateien sind kein Takt.
- **Verfolgung:** `cv2.matchTemplate` (normierte Kreuzkorrelation, NCC) mit festen Vorlagen aus dem ersten Bild: starre Architektur
  (**Weltanker**), Visier-/Modellrand, Zielpunkt. Verdeckte oder verformte Vorlagen (NCC deutlich unter ≈ 0,85, Formwechsel, Overlay
  im Ausschnitt) liefern **keine** Spur. Ein Weltanker zeigt die **projizierte Sichtbewegung**: Welt nach unten heißt, der Blick geht nach
  oben. Das ist kein Kamerawinkel und kein Beweis für reinen Spielrückstoß, denn unbekannte Eingaben und Gegenzug bleiben enthalten.
  Showcase-Kameras (Ultraclocked) stehen fest, sind aber nicht nachweislich unbewegt.
- **Zielpunkt:** Chroma Rush und Gridskipper zielen auf ≈ 50/50, die übrigen sechs Destiny-Beispiele auf ≈ 50/57,4 (Showcases 2020/21).
  Bezug ist jeweils die sichtbare Ruhelage.
- **Normaltempo** je Video geprüft ([destiny2.md › Methode 10](destiny2.md#2-messungen-an-60-fps-aufnahmen-ab-16-oktober-2026--m)): Schussabstände
  Chroma 5, Gridskipper 4 Bilder (Zeitlupe 8), Tone Patrol 20–21 Bilder (= 180/min), Annual Skate 27 Bilder (= 140/min); die übrigen
  Destiny-Videos mit markierten 0,5×-/0,25×-Abschnitten getrennt.
- **Übersichtskacheln liefern keine Zeitmarker:** `reference_frames.py sheet` zeigt bei niedriger Bildrate ein Bild eine halbe Abtastperiode
  nach seiner Beschriftung ([LESSONS](LESSONS.md)). Alle Zahlen stammen aus absoluten nativen Bildindizes.
- **Weltzoom** als **Bildmaßstab** einer Weltstruktur Hüfte → Zielen (Mehrskalen-NCC auf 480 × 270, gegengeprüft mit SIFT + RANSAC oder
  einer zweiten Welt-ROI), wie in [visiere.md › 1](visiere.md#1-quellen-und-methode). Rundung ±0,05–0,1×, kein Winkelzoom.

## 2. Quellen

Alle Zeiten in diesem Doc und in destiny2.md beziehen sich auf das **Originalvideo**. Kanal, Datum und Titel am 25.10.2026 per yt-dlp bestätigt.

| Kürzel | Kanal · Hochladedatum · Video | Waffe(n) | Bildrate / Hinweis |
|---|---|---|---|
| D-A | Ultraclocked · 15.05.2021 · [QxSa4m3wIEA](https://www.youtube.com/watch?v=QxSa4m3wIEA) | Chroma Rush (Automatik, Holo) | 1920 × 1080, 60/s |
| D-I | Ultraclocked · 13.05.2021 · [DFn14wAPluA](https://www.youtube.com/watch?v=DFn14wAPluA) | Gridskipper (Impuls, Holo) | 1920 × 1080, 60/s |
| D-SH | Ultraclocked · 14.02.2020 · [IG-GZ72Vbi0](https://www.youtube.com/watch?v=IG-GZ72Vbi0) | Tone Patrol (Scout), Annual Skate (Handfeuerwaffe) | 1920 × 1080, 60/s, SUROS-Sammelvideo |
| D-N | Ultraclocked · 18.02.2021 · [RXgRxHESqHQ](https://www.youtube.com/watch?v=RXgRxHESqHQ) | Far Future (Scharfschütze, Rundscope) | 1920 × 1080, 60/s |
| D-L | Ultraclocked · 20.02.2021 · [uoTaCBMXcFk](https://www.youtube.com/watch?v=uoTaCBMXcFk) | Threaded Needle (lineare Fusion, offene Gabel) | 1920 × 1080, 60/s |
| D-M | Ultraclocked · 15.02.2021 · [Y5OLr0nbgSg](https://www.youtube.com/watch?v=Y5OLr0nbgSg) | Extraordinary Rendition (MP, Reflex) | 1920 × 1080, 60/s |
| D-B | Ultraclocked · 19.02.2021 · [dKNTDzi__Qo](https://www.youtube.com/watch?v=dKNTDzi__Qo) | Imperial Needle (Bogen, Ring) | 1920 × 1080, 60/s |
| B-R | SammyBoiii: FPS · 17.02.2022 · [enyEjb4dXU8](https://www.youtube.com/watch?v=enyEjb4dXU8) | rotes Gewehr mit Reflex (Modell offen) | 1920 × 1080, 59,94/s |
| B-P | Flexaur · 06.10.2021 · [EbV5pVp92AU](https://www.youtube.com/watch?v=EbV5pVp92AU) | G57, M44 | **Beta 2021**, 1280 × 720, 59,94/s; G57-Schnittstart = Originalbild 4856 (81,014 s), M44 ≈ 300 s + lokal |
| A-E | Cacek47 · 06.02.2019 · [R-BGChzYGpo](https://www.youtube.com/watch?v=R-BGChzYGpo) | RE-45 | früher Retailstand, nur 0–55 s, 1280 × 720, 60/s |
| A-R | ClawZ · 25.11.2020 · [UetKaZiF9uA](https://www.youtube.com/watch?v=UetKaZiF9uA) | R-301 | 1150 × 720, ≈ 29,9/s – nur Form und Lage |
| A-P | tZveig · 11.04.2019 · [_ZttaEjdcQU](https://www.youtube.com/watch?v=_ZttaEjdcQU) | P2020 | nur 0–30 s, 1920 × 1080, 60/s; Normaltempo plausibel, nicht unabhängig kalibriert |
| H | Abyssopelagic · 30.07.2021 · [ZfNuA5r-470](https://www.youtube.com/watch?v=ZfNuA5r-470) | BR75, VK78 Commando, S7 | **erste Technical Preview**, 1280 × 720, 60/s |

## 3. Destiny 2 – Übersicht

Volle Zeilen mit Zeitstempeln und Grenzen: Spalte „Zeile“ (destiny2.md › 2). Welt = Weltanker nach unten (Blick nach oben); Modell = Visier-/Modellrand.

| Waffe (Klasse, Visier) | Vorgang | Welt | Modell/Visier | Spitze | Rückkehr | Zeile |
|---|---|---|---|---|---|---|
| Chroma Rush (Auto, Holo) | ADS-Viererstoß | ≈ 4 pp H | < 1 pp | 2 Bilder nach letztem Schuss | nahe 22, Basis 36 Bilder; kein Unterschwingen | [z-zb-chroma-stoss](destiny2.md#z-zb-chroma-stoss) |
| Gridskipper (Impuls, Holo) | ADS-Dreiersalve | ≈ 5 pp H | < 1 pp | 2–3 Bilder nach drittem Schuss | nahe 25, Basis 42 Bilder | [z-zb-gridskipper-salve](destiny2.md#z-zb-gridskipper-salve) |
| Tone Patrol (Scout, Glas) | ADS-Folge, 5 Schüsse | ≈ 6 pp H | – | Plateau 6–8 Bilder nach letztem Schuss | nahe 53, Basis 75 Bilder | [z-zb-tone-patrol-folge](destiny2.md#z-zb-tone-patrol-folge) |
| Tone Patrol | Punkt gegen Glasrand | – | relativ < 1 pp H | Blitz verdeckt | – | [z-zb-tone-patrol-punkt](destiny2.md#z-zb-tone-patrol-punkt) |
| Annual Skate (Handfeuerwaffe, Kimme) | isolierter ADS-Schuss | ≈ 6 pp H | dreht hoch [O], keine Zahl | 7–8 Bilder nach Blitz | nahe 47, Basis 68 Bilder | [z-zb-annual-skate-schuss](destiny2.md#z-zb-annual-skate-schuss) |
| Far Future (Scharfschütze, Rundscope) | ADS-Schuss im Scope | ≈ 18 pp H | Scope-Zeichen < 3 pp | 4 Bilder nach Blitz | bleibt ≈ 12 pp H versetzt | [z-zb-far-future-schuss](destiny2.md#z-zb-far-future-schuss) |
| Far Future | Halten 1,8 s | < 3 pp | < 3 pp | keine Periode | – | [z-zb-far-future-halt](destiny2.md#z-zb-far-future-halt) |
| Threaded Needle (lineare Fusion, Gabel) | ADS-Schuss | ≈ 13 pp H | ≈ 8 pp H **nach oben** | Modell 3, Welt 8 Bilder nach Blitz | Modell ≈ 20 Bilder; Welt bleibt 6–7 pp H versetzt | [z-zb-threaded-needle-schuss](destiny2.md#z-zb-threaded-needle-schuss) |
| Threaded Needle | Punkt minus Gabelrand [O] | – | Punkt ≈ 7 pp H tiefer (±6) | nach dem Blitz | – | [z-zb-threaded-needle-punkt](destiny2.md#z-zb-threaded-needle-punkt) |
| Threaded Needle | Halten 0,8 s | < 3 pp | < 3 pp | keine Periode | – | [z-zb-threaded-needle-halt](destiny2.md#z-zb-threaded-needle-halt) |
| Extraordinary Rendition (MP, Reflex) | ADS-Feuerfolge | roh 2,6 pp H | roh 1,3 pp H | an/unter Genauigkeit | überlagert | [z-zb-rendition-folge](destiny2.md#z-zb-rendition-folge) |
| Imperial Needle (Bogen, Ring) | gespannt halten 0,75 s | < 3 pp | < 3 pp | keine Periode | – | [z-zb-imperial-needle-halt](destiny2.md#z-zb-imperial-needle-halt) |
| Imperial Needle | Lösen = ADS-Ausstieg | Maßstabwechsel | Ring ≈ 30 pp H nach unten | 1. Lösungsbild | keine | [z-zb-imperial-needle-loesen](destiny2.md#z-zb-imperial-needle-loesen) |
| Imperial Needle | Endmaßstab Hüfte → ADS | **≈ 2,2×** | – | – | – | [z-zb-imperial-needle-zoom](destiny2.md#z-zb-imperial-needle-zoom) |
| Extraordinary Rendition | Endmaßstab Hüfte → ADS | **≈ 1,7×** | – | – | – | [z-zb-rendition-zoom](destiny2.md#z-zb-rendition-zoom) |

## 4. Vergleich: Battlefield 2042, Apex Legends, Halo Infinite

Historische Aufnahmefassungen (BF-Beta 2021 bzw. Aufnahme 2022, Apex 2019/2020, Halo-Technical-Preview 2021). Das sind beobachtete Gestaltungsprinzipien,
kein kontrollierter Vergleich gleicher FOV-, Eingabe- und Versionsbedingungen. Reaktionsintervalle sind Videozeit, keine Eingabe- oder Freigabelatenz.

| Vorgang | Clip (Kanal, Datum, Video) | Originalzeit / native Bilder | Messung und Grenze |
|---|---|---|---|
| **BF2042, rotes Gewehr (Reflex): Beginn eines ADS-Feuerstoßes** [M] <a id="z-zb-bf-reflex-stoss"></a> | SammyBoiii: FPS, 17.02.2022, [enyEjb4dXU8](https://www.youtube.com/watch?v=enyEjb4dXU8) | 41,408–42,092; f2482–2523 | Welt **≈ 4 pp H nach unten**, NCC ≥ 0,931; Rahmen roh < 1 pp H. Weltspur steigt am Fensterende noch: **kein vollständiger Peak/Return**. Mit anderer Welt-ROI bestätigt. Modell offen, keine M5A3-Zuschreibung. |
| **BF2042, rotes Gewehr: ruhiger ADS-Halt** [M/O] <a id="z-zb-bf-reflex-halt"></a> | dieselbe Quelle | 40,407–41,408; f2422–2482 | Welt, Rahmen und Punkt innerhalb ±3 pp. ≈ 1 s trägt keine Atemperiode, keine Null-Sway-Aussage. |
| **BF2042 (Beta), G57: ADS-Schussfolge, Kimme/Korn** [M/O] <a id="z-zb-bf-g57"></a> | Flexaur, 06.10.2021, [EbV5pVp92AU](https://www.youtube.com/watch?v=EbV5pVp92AU) | 89,706–90,307; Original f5377–5413 (lokal f521–557) | Zähler 15 → 14 und Schuss im nativen Bogen bestätigt. Welt roh innerhalb ±0,83 pp H, Modell bis ≈ 1 pp H: **unter Lagegenauigkeit**. Modellspur im Blitz lückenhaft. |
| **BF2042 (Beta), M44: Teil-Rücklauf, Kimme/Korn** [M/O] <a id="z-zb-bf-m44"></a> | dieselbe Quelle | ≈ 308,392–309,443; lokal f503–566 | Revolver beginnt schon hochgekippt (5 Patronen), **kein Schuss im Fenster**. Welt ändert sich im Rücklauf ≈ 3 pp H (NCC ≥ 0,935), Modell rotiert stark. Keine Kick-Amplitude, Peak- oder Rückkehrzeit. |
| **Apex, RE-45: ADS-Schüsse, Kimme/Korn** [M/O] <a id="z-zb-apex-re45"></a> | Cacek47, 06.02.2019, [R-BGChzYGpo](https://www.youtube.com/watch?v=R-BGChzYGpo) | 14,450–14,983; f867–899 | Achse mittig, Zähler 15 → 14 → 13. Rahmen roh −0,14…+0,42 pp H, Welt ≈ ±0,56 pp H: **unter ±3 pp**. Blitz verdeckt die Rahmenvorlage; keine Peak-/Rückkehrkurve. Ein Nachbarbild ist exakt doppelt. |
| **Apex, R-301: ADS-Zweischussfolge, offene Kimme** [M/O] <a id="z-zb-apex-r301"></a> | ClawZ, 25.11.2020, [UetKaZiF9uA](https://www.youtube.com/watch?v=UetKaZiF9uA) | ≈ 31,49–31,89; Quellindizes 942–954 bei ≈ 30/s | Zähler 16 → 15 → 14, Hülsen, Kimme/Korn mittig. Welt roh 2,22 pp H, Modell 0,56 pp H (NCC ≥ 0,968/0,882): beides unter ±3 pp. **Keine Zeiten** (≈ 30/s), keine Linsenparallaxe bei offener Kimme. |
| **Apex, P2020: ADS-Schuss, Schlitten und Kimme** [M/O] <a id="z-zb-apex-p2020"></a> | tZveig, 11.04.2019, [_ZttaEjdcQU](https://www.youtube.com/watch?v=_ZttaEjdcQU) | 21,100–22,300; f1266–1338; Blitz und Zähler 10 → 9 bei f1297 = 21,617 | Schlitten zieht sichtbar zurück, Kimme verschiebt sich gegen das Korn; Form wieder nominal ≈ f1308 = 21,800: **11 Bilder / 0,183 s Videozeit** (Endmarker ±2), keine kalibrierte Spielzeit. Modellvorlage verformt sich (NCC 0,54), kein freigegebener Rohpeak. **Weltkanal offen** (nur Wolken). |
| **Halo Infinite, BR75: Schussabschnitt im Smartlink** [M/O] <a id="z-zb-halo-br75"></a> | Abyssopelagic, 30.07.2021, [ZfNuA5r-470](https://www.youtube.com/watch?v=ZfNuA5r-470) | 58,150–58,750; f3489–3525 | Waffenmodell im Zoom ausgeblendet. Welt **≈ 4 pp H nach unten** (roh 3,61), NCC ≥ 0,964; kurze Salvenfolge, Gegenzug unbekannt; keine isolierte Rückkehr. Punktspur folgt Gegnerglühen, keine gültige Absehensspur. |
| **Halo Infinite, VK78 Commando: Schüsse im digitalen Zoom** [M/O] <a id="z-zb-halo-commando-feuer"></a> | dieselbe Quelle | 128,300–128,950; f7698–7737 | Welt roh 0,14 pp H, unter ±3 pp. Die „Visier“-ROI mischt Welt und Overlay und ist **keine** Modell- oder Parallaxespur; Gegner verdeckt den Punkt. HUD „3×“ ist eine Spielanzeige, kein gemessener Bildmaßstab. |
| **Halo Infinite, S7: Schuss im digitalen Scope** [O] <a id="z-zb-halo-s7-schuss"></a> | dieselbe Quelle | 332,600–333,200; f19956–19992; Schuss ab f19967 = 332,783 | Weltvorlage verliert am starken Hub die Zuordnung (NCC bis 0,617): **keine Peak-Amplitude, -zeit oder Rückkehr**. Overlaystrich ist kein Waffenmodell. |
| **Halo Infinite, VK78 Commando: Modell weg, digitaler Zoom wächst** [M/O] <a id="z-zb-halo-commando-zoom"></a> | dieselbe Quelle | Modell zuletzt f7660 = 127,667; Overlay zuerst f7661 = 127,683; Rest bis ≈ f7666 = 127,767 | Modell zwischen zwei Bildern ausgeblendet; der Weltmaßstab wächst danach noch **≈ 5 Videointervalle**. Kein Modellweg davor, kein Endzoom aus dieser Folge. |
| **Halo Infinite, S7: Scope erscheint, Restzoom folgt** [M/O] <a id="z-zb-halo-s7-zoom"></a> | dieselbe Quelle | Modell zuletzt f19897 = 331,617; Scope zuerst f19898 = 331,633; Rest bis ≈ f19905 = 331,750 | Großer Maßstabsprung im ersten Scopebild, Rest **≈ 7 Videointervalle**; Kameradrehung überlagert. Keine Eingabe → ADS-Latenz. |

## 5. Hüfte → Zielen: Endmaßstäbe und vorhandene Verläufe

Neu freigegeben: **Imperial Needle ≈ 2,2×** und **Extraordinary Rendition ≈ 1,7×** (Zeilen in [3](#3-destiny-2--übersicht)). **Threaded Needle**
(33,100 → 34,300) bleibt offen: Kandidat ≈ 3,0× mit NCC 0,913, aber SIFT nur 2 Inlier und eine zweite ROI findet eine falsche Wandkante.

Schon in destiny2.md belegte Übergänge (nicht neu gemessen, hier nur zur Einordnung): Chroma Rush Holo – Modell 11 Bilder zur Achse,
letzte deutliche Änderung nach 18 Bildern, Zoom beginnt 1–2 Bilder nach dem Modell und endet 2 Bilder vor dessen Ruhe, 1,84×
([Zeile](destiny2.md#z-chroma-rush)); Gridskipper Holo – Modell 11 Bilder, gesamt 18, 2,10–2,11× ([Zeile](destiny2.md#z-gridskipper-salve));
Far Future Rundscope – Modell 4 Bilder, Glasreflex 1–2, Linsenbild mit Zeichen 3–4 Bilder, dann harter Wechsel zum Vollbild-Overlay,
gesamt ≈ 0,15–0,17 s; Tone Patrol ≈ 22 Bilder, Imperial Needle ≈ 15 Bilder Drehung, Threaded Needle ≈ 0,30–0,32 s ADS ein.
Halo zeigt einen anderen Aufbau: das Modell verschwindet im Umschaltbild, der digitale Zoom wächst danach noch 5–7 Bilder ([4](#4-vergleich-battlefield-2042-apex-legends-halo-infinite)).

## 6. Muster je Messgröße

- **(a) Sway/Atmen:** Kein Destiny-Halt (0,75 / 0,8 / 1,8 s) zeigt eine messbare Periode; auch der BF-Halt (≈ 1 s) nicht. „Innerhalb ±3 pp“
  ist die Auflösungsgrenze, keine Spielfunktion. Eine Periode darf weder aus einem Rückstoß-Rücklauf noch aus unbekannter Mausnachführung
  gewonnen werden.
- **(b) Sichtbarer Rückstoß im ADS:** In Destiny wandert im ADS vor allem die **Welt**, das Visier bleibt fast stehen: Chroma Rush 4, Gridskipper 5,
  Tone Patrol und Annual Skate je 6, Threaded Needle 13, Far Future 18 pp H Welt bei Visierhub unter 1 pp (Holo) bzw. Scope-Zeichen unter 3 pp.
  Threaded Needle trennt Modell und Welt zeitlich (Gabel nach 3, Welt nach 8 Bildern). Scharfschütze und lineare Fusion kehren im Fenster nicht
  ganz zurück (12 bzw. 6–7 pp H Rest), Stöße und Salven schon (36–75 Bilder ab letztem Schuss, kein Unterschwingen über der Genauigkeit).
  BF2042 (Reflex-Gewehr) und Halo (BR75) zeigen im Feuer ebenfalls ≈ 4 pp H Weltaufbau bei kleinem Rahmenhub; die Pistolen und das R-301 in
  Apex sowie G57 in BF bleiben unter ±3 pp. Das sind getrennte Kanäle je Waffe, keine gemeinsame Amplitude einer Waffenklasse.
- **(c) Punkt im Glas:** Nur Threaded Needle liefert einen groben Versatz (Punkt ≈ 7 pp H tiefer gegen den angehobenen Gabelrand, ±6 pp);
  Tone Patrol bleibt relativ unter 1 pp, aber die Blitzbilder sind verdeckt. Offene Kimmen haben keine Glasöffnung, Halo-Rahmen sind digitale
  Overlays. Ein ruhiger Punkt im Bild belegt keine Parallaxefreiheit, und aus einem Punkt-/Rahmenversatz folgt kein bestimmter Kamera- oder
  Linsenaufbau.
- **(d) Hüfte → Zielen:** Destiny-Holos bewegen Modell und Weltzoom mit verschiedenen Start- und Endmarkern; das Rundscope wechselt nach kurzer
  Linsenphase hart zum Overlay; Halo blendet das Modell aus und zoomt digital weiter. Endmaßstäbe 2,2× (Bogen-Ring) und 1,7× (MP-Reflex) sind
  Bildverhältnisse. Es gibt keine universelle ADS-Kurve je Waffentyp.

## 7. Nicht messbar / offen

Damit keine Sitzung dieselben Wege erneut versucht:

- **Atemperiode:** keine mehrzyklischen Halte in diesen Clips; für Tone Patrol fehlt ein langer isolierter Halt. Keine Frequenz und keine Null-Amplitude ansetzen.
- **Reiner Kamerarückstoß ohne Eingabenachführung**, FOV in Grad, Winkel, Meter, Geschwindigkeiten: aus Weltankern nicht ableitbar.
- **Einzelschusswerte aus Mehrfachfeuer:** Auto-, Impuls-, Scout- und MP-Folgen überlagern die Rückstellung; Maxima gelten für Stoß/Salve.
- **Unterschwingen:** nur nennen, wenn ein Kanal die Basis jenseits der Lagegenauigkeit unterschreitet; Modellrückkehr bei bleibender Weltlage ist keins.
- **Parallaxe-Spitzen unter Blitz oder Verdeckung:** ungültige Punktspuren werden weder als großer Ausschlag noch als Null berichtet.
- **Bogen-Lösen:** gleichzeitig ADS-Ausstieg und Maßstabwechsel, kein isolierter ADS-Rückstoß.
- **Threaded-Needle-Endzoom:** Kandidat 3,0× nicht freigegeben ([5](#5-hüfte--zielen-endmaßstäbe-und-vorhandene-verläufe)).
- **Weitere Destiny-Übergangssplits:** über den Bestand hinaus nicht isoliert; Geh-, Landungs-, Abbruch- und Projektilsuche aus
  [Methode 14](destiny2.md#methode-14)–[16](destiny2.md#methode-16) nicht wiederholt.
- **Ausgeschlossene Quellen:** Skeptation `gCQHKNsIU9w` (08.11.2021) zeigt „Modded Apex – Unofficial – R5Reloaded“ mit veränderter Waffe –
  28 verfolgte Bilder verworfen. Cacek47 29,800–30,450 (Ende Nachladen) und 26,400–26,850 (Hüftfeuer) sind keine P2020-ADS-Belege.
  Wolken sind kein starrer Weltanker. Beta- und Technical-Preview-Zahlen (Flexaur, Abyssopelagic) gelten nicht für spätere Fassungen.
- **Vorrang für eine Folgesitzung:** lange kontrollierte ADS-Halte (Scout, Scharfschütze, lineare Fusion), isolierte Schüsse ohne ADS-Ausstieg,
  unverdeckte Punkt-/Rahmenverläufe – nicht dieselben Clips und Phasen.

## 8. Nachmessung und Zählung

**Nachmessung REF 0.17 (25.10.2026, Mac):** eigener Tracker und eigene ROIs (nicht die Vorlagen der Codex-Sitzung), dieselben Originalvideos, absolute
Bildindizes. Alle fünf Werte liegen innerhalb der Genauigkeit:

| Wert | Codex | Nachmessung | Weg |
|---|---|---|---|
| Chroma Rush, Welt im Viererstoß | ≈ 4 pp H, Spitze +2 | 3,7–3,8 pp H, Plateau +2 bis +6 Bilder (f1406–1410), NCC ≥ 0,95; Rest ≤ 0,1 pp ab +30 | zwei Wand-ROIs links/rechts |
| Far Future, Welt nach dem Schuss | ≈ 18 pp H bei +4, Rest ≈ 12 | 17,5 pp H bei +4 (f2012), NCC 0,933; Rest 12,0 pp H bei 34,483 | Wand-ROI ohne Scope-Balken (die ROI mit Balken fällt auf NCC 0,6) |
| Threaded Needle, Gabel und Welt | −8 bei +3; 13 bei +8 | Gabel −7,8 pp H bei +3 (NCC 0,77, Gabel wächst); Welt 12,8 pp H ab +7, Rest 6,7 | Gabelspitze, zwei Wand-ROIs |
| Imperial Needle, Endmaßstab | ≈ 2,2× | 2,24× mit zwei ROIs (NCC 0,912 / 0,855), aus den Fundorten 2,23× | Mehrskalen-NCC, ADS-Ausschnitt verkleinert |
| Extraordinary Rendition, Endmaßstab | ≈ 1,7× | 1,709× (32 Inlier) | ORB + RANSAC (Ähnlichkeit) |

Skripte und Ausgaben im Cache (`~/Library/Caches/CubeEscape/reference/visiere/codex/nachmessung-ref017/`), nicht im Repo.

**Zählung der Codex-Sitzung:** **17 Waffenbeispiele** (Destiny 8, Battlefield 3, Apex 3, Halo 3) aus **13 Videos**, **1392 eindeutige native
Quellbildindizes** (1342 für Verfolgung und Zoom, 50 zusätzliche Übergangsmarker; 13 davon bei ≈ 29,9/s). Quellindizes sind keine Zahl verschiedener
Simulationsposen (ein RE-45-Nachbarbild ist doppelt). Arbeitsdaten (Skripte, ROI-Konfigurationen, CSV, Manifeste) im Cache unter
`~/Library/Caches/CubeEscape/reference/visiere/codex/`.
