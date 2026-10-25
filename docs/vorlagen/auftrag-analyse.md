# Vorlage: Analyse-Auftrag (Zuarbeit für Motiongen)

Kopieren, Platzhalter `<…>` ersetzen, nichts aus [docs/standard.md](../standard.md) weglassen. Der fertige Auftrag liegt **im Arbeitsordner**
(Cache) als `AUFTRAG.md`, damit jeder Client ihn lesen kann; eine Kopie im Notizordner der koordinierenden Sitzung. Die Startnachricht an
Codex/Antigravity nennt nur den Pfad, die Welle und – **je Auftrag entschieden** – ob Unteragenten freigegeben sind. Die Pfade unten
sind der Stand am Mac (Oktober 2026) und vor jedem Auftrag zu prüfen; alles in `<…>` ist Platzhalter.

---

```text
<Modell und Denkaufwand mit Grund – Codex: gpt-6.1-sol high für Bildmessung, gpt-6-luna medium für Recherche; Antigravity: „Modell und
Denkaufwand in der ersten Zeile nennen“.> Erste Zeile deiner Antwort: Modell, Denkaufwand, Grund. Antworte auf Deutsch.

# <Titel> – <n> getrennte Themen

## Ziel
<Wofür (BASIC / Cube Escape / Toolgen), welche Frage, warum jetzt.> Destiny 2 zuerst (Stilvorbild höchster Priorität, nicht kopieren),
dazu Destiny 1 und Marathon, dann <Vergleichsspiele>. Je Thema ausdrücklich: Was funktioniert gut, was nicht so gut, und was sagen
Spieler dazu? Jedes Thema ist getrennt – eigener Ordner, eigene Ergebnisdatei, später eigene Version.

## Welche Welle?
<Tabelle Welle → Themen mit Ordnernamen; „Bearbeite die Welle aus der Startnachricht, ohne Angabe Welle 1; jedes Thema mit ‚fertig‘
abschließen, bevor das nächste beginnt“.>

## Gemeinsame Regeln
- Verbindlich: Analyse-Standard Motiongen, im Repo `/Users/ffunk/Claude/cubeescape-reference` auf `origin/main` unter `docs/standard.md`
  (`git -C /Users/ffunk/Claude/cubeescape-reference show origin/main:docs/standard.md`) – vollständig lesen.
- Arbeitsordner: `~/Library/Caches/CubeEscape/reference/<bereich>/<thema>`; Werkzeuge und Messregeln: `…/<bereich>/tools/methode.md`.
- Ergebnisdateien: Notizordner `<pfad>` als `<präfix>-<thema>.md`; falls nicht beschreibbar `…/<bereich>/ergebnisse/`.
- Kein Repo-Auftrag: kein Branch, kein Commit, kein Push, in keinem Git-Repo etwas ändern; Repos nur lesen.
- Werkzeuge: `export PATH=~/Library/Caches/CubeEscapeBallon/venv-media/bin:$PATH; export SSL_CERT_FILE=~/Library/Caches/CubeEscapeBallon/venv-media/lib/python3.12/site-packages/certifi/cacert.pem`;
  Suche `yt-dlp --flat-playlist --print "%(id)s|%(title)s|%(duration)s|%(channel)s" "ytsearch10:<suche>"`; Laden
  `python3 /Users/ffunk/Claude/cubeescape-reference/tools/reference_frames.py fetch "<url>" --out <ordner>`; Rasterbild `…/tools/grid.sh`;
  Bildmaßstab `…/tools/tmatch.py` mit `~/Library/Caches/CubeEscape/reference/visiere/venv/bin/python`.
- Quellenpflicht, Bewertung (gut / nicht so gut / für wen / Spielerstimmen / Entwickler), Mindestmaß 5 Spieler- und 2 Fachquellen,
  Aufbau A–F mit Tabelle E und E2: wie `docs/standard.md` › 3, 4, 6.
- Werkzeugbefund: `sheet` beschriftet Kacheln bei niedriger Bildrate eine halbe Periode zu früh – Zahlen nur aus `--fps native`,
  Bögen ≥ 5/s oder `grid.sh`.
- Zuerst lesen, nichts wiederholen: <vorhandene Docs auf origin/main, die das Thema berühren>.
- Unteragenten: <freigegeben / ein Unteragent je Thema>; jeder schreibt nur in Ordner und Datei seines Themas.
- Umfang: gern gründlich; Zwischenstand alle 30–45 Minuten, je Thema Abschluss nach etwa 3 Stunden, Dateien über ~1,5 GB in 720p,
  Cache unter <Grenze> GB.

## Thema <Nr> – <Name> (`<ordner>/` → `<präfix>-<thema>.md`)
<Was untersucht wird, welche Spiele zuerst, welche Messgrößen.> JSON: `<feld>`, `<feld>`, …
```

---

**Startnachricht (Muster):**

```text
Auftrag: ~/Library/Caches/CubeEscape/reference/<bereich>/AUFTRAG.md – bitte vollständig lesen und genau befolgen, dazu docs/standard.md
im Repo cubeescape-reference (origin/main). Bearbeite Welle <n>. <Unteragenten sind freigegeben | Keine Unteragenten>. Nichts in Git-Repos ändern.
Erste Zeile: Modell, Denkaufwand, Grund. Antworte auf Deutsch.
```
