# cubeescape-reference – Regeln für KI-Agenten

Zentraler Repo-Einstieg: [Nexogen](https://github.com/ffunkfabian-hash/cubeescape-nexogen) – Repo-Links, Zuständigkeiten, Abhängigkeiten und Live-Status über die Status-CLI im Nexogen-Repo. Globale Regeln dort, Fachwissen und Prüfbelege hier.

**Werkzeuge:** `./ce check` · `./ce search query "Begriff"` · `./ce session topics` · `./ce codex quota|judge` · `./ce evidence clip|sheet|still|diff` · `./ce lock unity|blender|gpu -- <Befehl>` · `./ce report --since 7d`.

Gilt für alle Agenten (Claude Code, Codex, …). Globale Regeln: Repo `ffunkfabian-hash/cubeescape-rules` (`CLAUDE.md` dort).

## Projekt

Referenzmessungen für das Ego-Spielgefühl von Cube Escape (Vorbilder: Destiny 2, später Portal 2, Half-Life 2, Metroid Prime …) und der
Vergleich mit dem Spiel. **Hier stehen Beobachtungen und Zahlen; Schlüsse, Entscheidungen und Startwerte stehen in Cube Escape**
(`Docs/FIRST_PERSON_EQUIPMENT.md`), Hände/Clips in Toolgen, Konzeptblätter im Design-Repo. Öffentliches Repo: keine Zugangsdaten,
keine privaten Daten, keine Bild- oder Videodateien aus fremden Aufnahmen (nur Verweise, Zeitstempel und Zahlen).

- **Sprache:** Antworten, Doku und Commit-Messages auf Deutsch; Code, Bezeichner, Kommentare und Testnamen auf Englisch.
- **Version:** `.ce-repo.json` und `CHANGELOG.md`; jeder neue Auftrag Minor +1 mit englischem Namen; Bericht je Hauptversion in `docs/versions/<Haupt>.md`.

## Messregeln (Erfahrungen)

- Eine Messung = eine Zeile in der Messtabelle des Spiels (`docs/<spiel>.md` › 2) **und** ein Eintrag in `data/clips.json`
  (Messung, Clip-URL, Quelle mit Kanal/Datum, Zeitstempel). Zahlen eines Clips sind Beispiele einer Waffe, keine Archetyp-Mittelwerte;
  Perks/Stats sind unbekannt – auffällig kurze Zeiten so einordnen.
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
Hinweis an das abnehmende Repo (Cube Escape/Toolgen) per Briefkasten oder Übergabe, nie dort selbst schreiben.

Werkzeug-Erfahrungen: [docs/LESSONS.md](docs/LESSONS.md); die verlinkte Systemdokumentation bleibt die Langform.

## Plugins und Hooks

Der gemeinsame Wächter (Agent Tools 0.12) wird über Nexogen für Codex nach `/hooks`-Vertrauen und für Antigravity auf den gemessenen Oberflächen installiert; das reversible Git-Netz ergänzt ihn für alle Clients. Die begrenzte Commit-Vorabprüfung, Einbau und Grenzen stehen zentral in [Werkzeuge und Durchsetzung](https://github.com/ffunkfabian-hash/cubeescape-nexogen/blob/main/templates/regeln-details.md#werkzeuge-und-durchsetzung). Postfach (ce-shared 0.15.1, nur Claude Code mit installiertem Plugin): Für eine reservierte Sitzung (`./ce session reserve|patch`) startet ein Stop-Hook den Wächter selbst und weckt sie bei Nachrichten; läuft keiner, hält ein zweiter Stop-Hook das Ende einmal an (höchstens alle 2 h).
