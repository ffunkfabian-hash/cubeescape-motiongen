# Changelog

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
- [Versionsbericht](docs/versions/0.md#030-fieldwork--unveröffentlicht).

## 0.2.0 „Frame Ledger“ – 2026-10-18

- `measure` ergänzt Bildzeiten bei nativer Rate und einen Entwurf für einen Messungseintrag; Ausgaben bleiben im Scratch.
- Die Verweisprüfung meldet fehlende oder leere Pflichtfelder in `data/clips.json`; Werkzeugtests decken Messausgabe und Validierung ab.
- Kontaktbögen sind in der Cloud nicht bildlich geprüft; der Versionsbericht in `docs/versions/0.md` wird von Sightline ergänzt.

## 0.1.0 „Baseline“ – 2026-10-18

- Umzug der Destiny-2-Referenz aus Cube Escape (`Docs/FIRST_PERSON_EQUIPMENT.md` › 1.2a/1.2b): Messtabelle (53 Zeilen), Steckbriefe für
  elf Waffentypen, Bewegungsblock, Methode; Werkzeug `tools/reference_frames.py` mit Tests; `data/clips.json` (30 Clip-Verweise).
- [Versionsbericht](docs/versions/0.md#010-baseline--2026-10-18).
