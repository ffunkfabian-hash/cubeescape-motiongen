# Analyse-Standard Motiongen

Verbindlich für alle Referenzanalysen in diesem Repo und für alle Zuarbeiten (Claude, Codex, Antigravity, Unteragenten). Gilt zusätzlich zu
den [Messregeln in AGENTS.md](../AGENTS.md#messregeln-erfahrungen) und den globalen Regeln in Nexogen (Modellwahl, Richter, Merge über
Sightline, Sperren, Belege) – die werden hier nicht wiederholt. Entstanden aus REF 0.14–0.20 (Visiere bis Inspektion); neue Erfahrung
ändert diesen Standard über eine eigene Version. Vorlage für Aufträge: [vorlagen/auftrag-analyse.md](vorlagen/auftrag-analyse.md).

## 1. Themen getrennt halten

- **Ein Thema = ein Arbeitsordner, eine Ergebnisdatei, eine Version, ein Doc** (`docs/<thema>.md`, maschinenlesbar `data/<thema>.json`).
  Nebenthemen, die bei einer Analyse auffallen, bekommen einen eigenen Auftrag; im laufenden Doc höchstens ein Querverweis.
- Ein Thema hat **höchstens zwei Hauptziele**. Teile eines Themas (z. B. Bewegung und Effekte desselben Vorgangs) dürfen verschiedene
  Zuarbeiter haben, aber getrennte Ergebnisdateien; zusammengeführt wird beim Einpflegen in **einer** Version mit getrennten Abschnitten.
- Arbeitsordner liegen im Cache, nie im Repo: `~/Library/Caches/CubeEscape/reference/<bereich>/<thema>/`.

## 2. Messen

- Einheiten und Genauigkeit wie in AGENTS.md (Prozent der Bildbreite **B** / Bildhöhe **H**, Ursprung oben links, Mitte 50/50 = Zielpunkt,
  ±3 Prozentpunkte; Zeiten nur aus 60/s-Aufnahmen, ±1 Bild = 16,7 ms; 30/s nur für Form und Lage).
- **Zahlen nur aus Einzelbildern** mit 10-%-Raster und Mittenkreuz oder aus Bögen mit `--fps native` bzw. ≥ 5/s. **Werkzeugbefund:**
  `reference_frames.py sheet` zeigt bei niedriger Bildrate jede Kachel etwa eine halbe Abtastperiode **später** als ihre Beschriftung –
  Übersichtsbögen nur zum Finden.
- **Bildmaßstab statt Winkelzoom:** Zoom und Vergrößerung als Bildmaßstab messen (Vorlagensuche, gültig ab Korrelation ≥ 0,85 und Fund
  nahe der Mitte; zweiter, anders aussehender Anker zur Gegenprobe); nennt ein Spiel einen Winkelzoom, beide Werte getrennt angeben.
- **Third-Person:** Strecken und Höhen in **Körperhöhen** der Figur (stehend = 1,0, am selben Bild gemessen); Gegnergröße in Spielerhöhen.
- **Bildanteile gelten nur mit FOV:** Spiele skalieren Waffe und Visier mit dem FOV (Titanfall: +23–28 % von FOV 70 auf 112); FOV des
  Aufnehmenden nennen oder als unbekannt kennzeichnen.
- **Eine Zahl ist das Beispiel einer Waffe, Optik oder Aktion**, kein Klassenmittel; Fremdaufnahmen zeigen Netto aus Spiel und Eingabe.
- Was nicht messbar ist, steht mit Grund im Doc („nicht messbar / offen“), damit niemand es erneut versucht.

## 3. Quellen

- **Status je Aussage:** **[M]** gemessen am Einzelbild oder per Bildvergleich · **[S]** Sekundärquelle (Wiki, Datenbank, API, Einblendung
  im Spiel, Fachanalyse) · **[B]** Entwickler (Patchnotes, Blog, Interview, GDC-Vortrag, ViDoc) · **[C]** Community oder Zuarbeit einer
  anderen Sitzung, nicht vollständig nachgeprüft · **[O]** Sichtung ohne belastbare Zahl. Mischangaben nennen alle zutreffenden Stufen.
- **Jede Videoquelle** wird mit `yt-dlp --print "%(channel)s|%(upload_date)s|%(title)s" <id>` geprüft; eingetragen wird genau diese Ausgabe
  (Kanal, ID, Hochladedatum) plus Bildrate und Zeitstempel. Kanal und Clip-Ersteller getrennt nennen. Spielstand prüfen (Destiny 1 oder 2,
  Patch, Season, Mod-Client).
- Wiki- und Datenbankwerte mit URL und Abrufdatum; Entwickleraussagen mit URL, Datum und Sprecher.
- **Ergiebige Videoquellen (Stand 31.10.2026):** Ultraclocked (Showcases ohne HUD, 1080p60, feste Kamera – Zeiten, Weltzoom, Formen; kein Sprint);
  **Nexxoss Gaming** (https://www.youtube.com/@nexxossgaming, Destiny-Reviews und „Waffentest“, überwiegend deutsch, 2017–2025, Eisenbanner-Reihe
  Okt. 2017 mit einer Waffe je Klasse; Spielszenen mit HUD in PvE und PvP, ab 2018 nur 21–30 echte Bilder/s – ergiebig für Spielerurteile [C] aus den
  deutschen Auto-Untertiteln, Haltungen beim Laufen und im Sprint, Weltzoom vor Wänden, Einschlagbilder; nicht für Zeiten unter ± 33 ms, Sprinttakt
  und Raketenwerfer-Urteile, [destiny2 › 1](destiny2.md#1-quellen)); Twitch-Clips der Kanäle in [destiny2 › 2](destiny2.md#2-messungen-an-60-fps-aufnahmen-ab-16-oktober-2026--m).
  Auto-Untertitel mit `yt-dlp --write-auto-subs --sub-langs de-orig` laden; Zitate wörtlich mit Zeitstempel, Hörfehler nicht „verbessern“, Lesart getrennt.
- **Urheberrecht:** keine fremden Bilder, Videos, Tonschnipsel, Texturen, Logos oder Filmstills im Repo – nur Beobachtungen, Zahlen,
  Zeitstempel, Links. Bei Filmen nur offizielle Trailer und Clips; Zitate höchstens eines unter 15 Wörtern je Quelle.

## 4. Bewerten: gut, nicht so gut, Spielerstimmen

Bewertung ist Pflicht, nicht Beiwerk. Je Spiel und untersuchtem Gegenstand:

- **Was funktioniert gut – warum?** und **was funktioniert nicht so gut – warum?** (Lesbarkeit, Reaktionszeit, Wucht, Fairness, Klarheit,
  Stil, Leistung, Übelkeit, Bugs) sowie **für wen** (Einsteiger/Profis, PvE/PvP, Controller/Maus, Barrierefreiheit).
- **Jede Aussage mit Beleg**: Zeitstempel [M]/[O] oder URL [C]/[B]/[S]. Eigene Einschätzungen sind als „Einschätzung“ gekennzeichnet und
  stehen getrennt von Spieler- und Entwicklermeinungen.
- **Spielermeinungen** gezielt suchen (Reddit, Steam, offizielle Foren, ResetEra, Presse mit Spielerzitaten; YouTube-Kommentare nur mit
  sichtbarer Zustimmung). Je Meinung: **Einzelstimme oder wiederkehrend** (in wie vielen unabhängigen Quellen), Zustimmung wo sichtbar,
  **Gegenstimmen**, Datum und Patch-Stand (vor/nach Update). Nicht ladbare Seiten nur als „Suchauszug“ kennzeichnen, nie Inhalte erfinden.
- **Referenzen:** Entwickleraussagen und Fachquellen (Game Maker's Toolkit, Digital Foundry, Accessibility Guidelines); gezielt suchen,
  **was nach Kritik geändert wurde** – das belegt, was nicht gut funktionierte.
- **Mindestmaß je Thema:** 5 Spielerquellen und 2 Entwickler- oder Fachquellen mit URL; wo nicht auffindbar, begründen.
- Schlüsse für BASIC und Cube Escape sind **Vorschläge**; entschieden wird dort (AGENTS.md › Projekt).

## 5. Unteragenten und Zuarbeit

- **Große Analysen** (mehrere Spiele oder Themen, mehr als etwa zehn Videos) laufen mit **einem Unteragenten je Thema oder Spiel**;
  kleine Aufgaben erledigt die Sitzung selbst (globale Regel „gezielt einsetzen“). Jeder Unteragent schreibt nur in Ordner und
  Ergebnisdatei seines Themas und bekommt diesen Standard mit.
- **Zuarbeit von außen** (Codex, Antigravity): liefert nur in Cache und Notizordner, ändert kein Repo. Eingepflegt wird in einer eigenen
  Claude-Sitzung je Thema mit Versionsnummer.
- **Prüfung durch den Koordinator** vor „fertig“ bzw. vor dem Einpflegen: 3 Quellen per yt-dlp nachprüfen, 2–8 Zahlen am eigenen Rasterbild
  nachmessen, jedes übernommene Beispiel am Zeitstempel ansehen, 3 Spieler-URLs aufrufen, Aufbau nach [6](#6-aufbau-einer-ergebnisdatei)
  vollständig; Zeitstempel gegen die Videolänge prüfen. Was die Prüfung nicht besteht, wird nicht übernommen und im Bericht **gezählt**
  („bestätigt n von m, nicht übernommen k mit Grund“). **Fremde Zuarbeit ist Rohstoff, keine Quelle:** 0.14 fand Video-IDs anderer Titel,
  0.18 bestätigte 30 von 86 Beispielen (24 von 34 Videos mit falschem Kanal/Datum, 14 Zeitstempel hinter dem Videoende, Farbangaben bei
  mindestens 8 Waffen falsch) – siehe [LESSONS](LESSONS.md).
- **Leitplanken (weich):** Zwischenstand alle 30–45 Minuten mit „fertig/nicht fertig“ in der ersten Zeile; je Thema Abschluss nach etwa
  3 Stunden, Offenes für eine Folgesitzung notieren; Dateien über ~1,5 GB in 720p; Cache je Auftrag in einer vorher genannten Grenze.
- **Aufräumen** nach dem Merge: eigene Downloads und Zwischendateien; Belege der aktuellen und der vorigen Version bleiben.

## 6. Aufbau einer Ergebnisdatei

Gilt für Zuarbeiten und als Gliederung des späteren Docs:

- erste Zeile „fertig/nicht fertig“ mit Zählung
- **A** Quellenliste (Videos, Wikis/API, Entwickler, Community getrennt)
- **B** Mess- und Sichtzeilen `| **Vorgang** | Quelle (Kanal, ID, Datum) | Zeitstempel | Messung |`
- **C** JSON-Liste (unbekannt = `null`; immer `game`, `subject`, `status`, `source_url`, `timestamp`, `notes`; dazu `good`, `bad`,
  `audience`, `player_opinion {summary, recurrence, sources, counter}`, `dev_reference {summary, url, date}`)
- **D** Muster je Spiel und Klasse (Destiny zuerst)
- **E** „Was funktioniert gut / was nicht so gut“ als Tabelle: Spiel · Gegenstand · Gut (warum) · Nicht so gut (warum) · Für wen · Belege ·
  Spielerstimmen (wiederkehrend/Einzel/Gegenstimmen) · Entwickler/Fachquelle; danach **E2** „Lehren für BASIC/Cube Escape“ (übernehmen /
  vermeiden / testen, als Vorschlag)
- **F** Nicht messbar / offen (mit Grund)
- Schlusszeile: Spiele, Beispiele, Videos, Quellen, gemessene Einzelbilder

## 7. Einpflegen ins Repo

- Doc `docs/<thema>.md` mit Status-Legende, Quellen und Methode, Messtabelle, Mustern, Bewertung (Abschnitt E), Vorschlägen und „offen“;
  `data/<thema>.json`; Kernmessungen in `data/clips.json`; benannte Anker für zitierte Zeilen; Lehre in `docs/LESSONS.md`; CHANGELOG und
  Versionsbericht.
- Prüfung: `./check`, `git diff --check`, Codex-Richter bis Freigabe; Merge nur durch Sightline nach Ja des Nutzers.
- **Parallele Sitzungen im selben Repo:** eigene Dateien (`docs/<thema>.md`, `data/<thema>.json`) parallel bearbeiten; die gemeinsamen
  Dateien (`CHANGELOG.md`, `.ce-repo.json`, `docs/versions/0.md`, `docs/LESSONS.md`, `README.md`, `data/clips.json`, `docs/destiny2.md`)
  erst kurz vor dem PR nach `git merge origin/main` ändern – am besten per idempotentem Skript, das nach jedem Einholen erneut läuft.
  Sightline mergt in Versionsreihenfolge; so liefen 0.14–0.20 ohne Konflikt.
- Übergabe an das abnehmende Repo (BASIC, Cube Escape, Toolgen) per Briefkasten; dort nie selbst schreiben.
