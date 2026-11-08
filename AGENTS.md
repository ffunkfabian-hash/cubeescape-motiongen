# cubeescape-reference – Regeln für KI-Agenten

Zentraler Repo-Einstieg: [Nexogen](https://github.com/ffunkfabian-hash/cubeescape-nexogen) – Repo-Links, Zuständigkeiten, Abhängigkeiten und Live-Status über die Status-CLI im Nexogen-Repo. Globale Regeln dort, Fachwissen und Prüfbelege hier.

## Harter Kern

Quelle: Nexogen `templates/kern.md`, nur dort ändern; gilt auch in Cloud-Sitzungen.

1. Kein Commit direkt auf `main`.
2. Kein Force-Push, keine überschriebenen Branches oder Tags.
3. Nichts Fremdes anfassen oder löschen: andere Sitzungen, Worktrees, Stash, Haupt-Checkout.
4. Merge nach `main` nur mit Ja des Nutzers, außer Patch bis 100 Zeilen ohne Format, Vertrag, Kernpfad bei grünem `merge-check`; Tag, Release, Repo öffentlich machen immer nur mit Ja.
5. Tests nie löschen oder abschwächen, um grün zu werden.
6. Keine Zugangsdaten, kein fremdes Material, keine großen Binärdaten nach außen (öffentliche Repos, fremde APIs).
7. Formate, Verträge und IDs nur mit Migration; IDs sind ewig.
8. Nichts als fertig melden, was nicht geprüft ist.

## Projekt

Referenzmessungen für das Ego-Spielgefühl von Cube Escape (Vorbilder: Destiny 2, später Portal 2, Half-Life 2, Metroid Prime …) und der
Vergleich mit dem Spiel. **Hier stehen Beobachtungen und Zahlen; Schlüsse, Entscheidungen und Startwerte stehen in Cube Escape**
(`Docs/FIRST_PERSON_EQUIPMENT.md`), Hände/Clips in Toolgen, Konzeptblätter im Design-Repo. Öffentliches Repo: keine Zugangsdaten,
keine privaten Daten, keine Bild- oder Videodateien aus fremden Aufnahmen (nur Verweise, Zeitstempel und Zahlen).

- **Version:** `.ce-repo.json` und `CHANGELOG.md`; Bericht je Hauptversion in `docs/versions/<Haupt>.md`. Patch und Version nach der globalen Regel (Patch: 1–3 Zeilen Changelog, kein neuer Minor).

## Messregeln (Erfahrungen)

- **Analysen und Zuarbeiten folgen dem [Analyse-Standard](docs/standard.md):** Themen getrennt (ein Thema = Ordner, Ergebnisdatei, Version, Doc),
  Quellenpflicht per yt-dlp, Bewertung „gut / nicht so gut / für wen“ mit Spielerstimmen und Entwickler-Referenzen, Unteragenten je Thema bei
  großen Analysen, Prüfung jeder Zuarbeit vor dem Einpflegen. Aufträge an Codex/Antigravity aus [docs/vorlagen/auftrag-analyse.md](docs/vorlagen/auftrag-analyse.md).
- Eine Messung = eine Zeile in der Messtabelle des Spiels (`docs/<spiel>.md` › 2) **und** ein Eintrag in `data/clips.json`
  (Liste `clips`: Messung, Clip-URL, Quelle mit Kanal/Datum, Zeitstempel). Zahlen eines Clips sind Beispiele einer Waffe, keine Archetyp-Mittelwerte;
  Perks/Stats sind unbekannt – auffällig kurze Zeiten so einordnen.
- Jede `data/*.json` ist ein Objekt mit `schema_version` (ganze Zahl, erster Schlüssel) = Version des **Dateiformats**; `version` ist die
  REF-Version des **Inhalts**. Formänderung (Feld umbenannt/entfernt, Typ, Wurzel) → `schema_version` + 1, Migration aller Dateien und Leser im
  selben PR (Regel 7, als Version mit Richter); neue Felder dazu brauchen keine neue Nummer. `tests/test_schema_version.py` prüft das.
- Verweise auf Messzeilen, Methoden und Steckbriefe nur über benannte Anker (`<a id="z-…"></a>` am Ende des ersten Feldes der Zeile), nie über Zeilennummern (`#L123`):
  Einschübe verschieben sie, ohne dass ein Test es merkt. `./check` (`tools/check_links.py`) lehnt `#L…` ab und prüft, dass jeder `#anker` im Zielsatz existiert.
- Genauigkeit: ±1 Bild bei nativer Rate (60/s = 16,7 ms), ±0,05 s bei 10/s; Lage im Bild in Prozent (Breite / Höhe, Ursprung oben links,
  Mitte = Zielpunkt), ±3 %. Immer mit `--cross` messen, wenn es um Zielpunkt, Mündung oder Visier geht.
- Steckbriefe (› 3) halten die **Form** fest (wo etwas liegt, was sich wie bewegt); Spalten: Hüfthaltung, Zielen, Sprint/Tragen, ADS, Feuern/
  Rückstoß, Aktionen, Arme, Besonderheiten, Cube-Escape-Felder. Neue Erkenntnis ersetzt alte Zeile; Korrekturen nennen Datum und Grund.
- Was aus Clips nicht messbar ist (Tempo in m/s, Welt-FOV in Grad, Betrachten, seltene Aktionen), steht im Spiel-Doc unter „Methode“,
  damit keine Sitzung es erneut versucht. Cloud-Sitzungen: YouTube gesperrt, Twitch-Clips laden; der Picker braucht keine Anmeldung.
- Werkzeugänderungen (`tools/`) brauchen Tests in `tests/` und `./check` grün; das Werkzeug schreibt nie ins Repo (Clips/Bögen in den Scratch).

## Befehle

`./check` – Werkzeugtests und Doku-Verweise. `python3 tools/reference_frames.py list|fetch|overview|sheet …` – Messen (Ablauf: `docs/destiny2.md` › 2).

## Definition of Done

Messzeile + `clips.json`-Eintrag + Steckbrief aktualisiert; `./check` grün; Abschlussbericht auf Deutsch mit Clip-Zahl, Neuem, Offenem;
Hinweis an das abnehmende Repo (Cube Escape/Toolgen) per Postfach (Nexogen-Issue #16) oder Übergabe, nie dort selbst schreiben.

## Hooks und Werkzeuge (nur Repo-Eigenes)

`./ce` lädt den in `.ce-repo.json` › `tools_version` gepinnten Stand aus ce-agent-tools; keine Kopie im Repo. Pin wechseln: `./ce tools pin <commit>` und denselben Commit in `.github/workflows/check.yml` eintragen. Hier gibt es keine hookify-Dateien; Tests und `./check` sind das Netz.
