# Changelog

## 0.3.0 „Fieldwork“ – unveröffentlicht

- Destiny 2, PvE-Kanäle (mactics, datto, saltagreppo; 54 Clips gesichtet, 5 vermessen, 9 neue Messzeilen): Scharfschützengewehr (Ziehen, Zielfernrohr ein/aus mit
  Reihenfolge Modell/Linse, Sprint-Haltung, Rutschen), Gewehr (tiefe Sprint-Haltung, Austritt), Granatwerfer (Kipplauf-Nachladen), Bogen (Hüfte von rechts, Spannen ohne ADS, Lösen), Sidearm (Hüfte, Nachladen) und Raketen-Sidearm (ADS, Rückstoß).
- Steckbriefe Sidearm, Langes Gewehr und Bogen ergänzt; Bewegung: Rutschen und Zielfernrohr-Reihenfolge; zwei Maschinenpistolen-Clips für den Codex-Teil vorgemerkt.
- Codex-Teil (PR #1, 63 Clips gesichtet, 8 Messungen): Maschinenpistole (Hüfte, Arme, Fadenkreuz, Wechsel), vollständiges Automatikgewehr-Nachladen mit HUD-Marker,
  Raketenwerfer-ADS und -Schuss, Sichtungsprotokoll je Clip, Fadenkreuz-Katalog (Stand), yt-dlp-Fallback als Python-Modul im Werkzeug.
- Aktionen und Lücken (Sightline, zweiter Teil): Maschinenpistole Sprint/ADS/Dauerfeuer (PvP, 60/s), Duality-Nachladen, Nahkampf bei 60/s, Wechsel-Übersicht je Klasse;
  Befund: Fadenkreuz-Aufblühen ist aus Stream-Clips nicht messbar; zwei Titel-Treffer waren ein anderes Spiel bzw. unklar (Methode).
- [Versionsbericht](docs/versions/0.md#030-fieldwork--unveröffentlicht).

## 0.2.0 „Frame Ledger“ – 2026-10-18

- `measure` ergänzt Bildzeiten bei nativer Rate und einen Entwurf für einen Messungseintrag; Ausgaben bleiben im Scratch.
- Die Verweisprüfung meldet fehlende oder leere Pflichtfelder in `data/clips.json`; Werkzeugtests decken Messausgabe und Validierung ab.
- Kontaktbögen sind in der Cloud nicht bildlich geprüft; der Versionsbericht in `docs/versions/0.md` wird von Sightline ergänzt.

## 0.1.0 „Baseline“ – 2026-10-18

- Umzug der Destiny-2-Referenz aus Cube Escape (`Docs/FIRST_PERSON_EQUIPMENT.md` › 1.2a/1.2b): Messtabelle (53 Zeilen), Steckbriefe für
  elf Waffentypen, Bewegungsblock, Methode; Werkzeug `tools/reference_frames.py` mit Tests; `data/clips.json` (30 Clip-Verweise).
- [Versionsbericht](docs/versions/0.md#010-baseline--2026-10-18).
