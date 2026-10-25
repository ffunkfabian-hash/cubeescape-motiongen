# cubeescape-reference

Zentraler Repo-Einstieg: [Nexogen](https://github.com/ffunkfabian-hash/cubeescape-nexogen) – Repo-Links, Zuständigkeiten, Abhängigkeiten und Live-Status über die Status-CLI im Nexogen-Repo. Globale Regeln dort, Fachwissen und Prüfbelege hier.

Referenzmessungen für das Ego-Spielgefühl von **Cube Escape**: wie Vorbilder (zuerst Destiny 2) Waffen und Werkzeuge halten, zielen,
wechseln, nachladen und bewegen – gemessen an 60-fps-Aufnahmen, als Zahlen mit Zeitstempeln und Steckbriefen je Typ. Cube Escape,
Toolgen und das Design-Repo lesen hier; entschieden und umgesetzt wird dort.

| Pfad | Inhalt |
|---|---|
| `docs/destiny2.md` | Messungen (Tabelle mit Clip und Zeitstempeln) und Steckbriefe je Waffentyp |
| `docs/apex.md`, `docs/titanfall2.md` | Bewegungs-Vorbilder: Sprint, Rutschen, Sprung/Landung, Wandlauf, tiefe Hüfte (je ein Steckbrief) |
| [docs/standard.md](docs/standard.md) | **Analyse-Standard:** verbindliche Regeln für Analysen und Zuarbeiten (Themen getrennt, Messen, Quellen, Bewertung, Unteragenten, Ergebnisaufbau); Vorlage für Aufträge in `docs/vorlagen/` |
| [docs/visiere.md](docs/visiere.md) | Visiere in Videospielen: Darstellungsarten, Zahlen im Zielen, Form, Sitz, Absehen, Glas, Spielerstimmen, Empfehlungen für BASIC (`data/visiere.json`) |
| [docs/proportionen.md](docs/proportionen.md) | Waffenproportionen und Silhouetten: Verhältnisse je Klasse (Destiny 2 und fünf Vergleichsspiele), was schlank macht, BASIC-Abweichungen (`data/proportionen.json`) |
| [docs/rueckstoss.md](docs/rueckstoss.md) | Rückstoßmuster in Videospielen: Nettobahnen, Takt, Rücklauf, Systemfassungen, Musterkatalog je Klasse, Gestaltungsregeln für BASIC (`data/rueckstoss.json`) |
| [docs/zielbewegung.md](docs/zielbewegung.md) | Zielbewegung im Zielen: Rückstoß im ADS gegen Weltanker, Halten, Punkt im Glas, Hüfte → Zielen; Destiny 2 mit Battlefield 2042, Apex und Halo im Vergleich (`data/zielbewegung.json`) |
| [docs/oberflaechen.md](docs/oberflaechen.md) | Oberflächenmuster von Waffen: Farbfelder, Akzentanteil, Helligkeitsabstand, Muster, Verschleiß und Shaderlogik in Destiny 2, Prüfung der Antigravity-Regeln, BASIC-Materialrollen als Vorschlag (`data/oberflaechen.json`) |
| [docs/muendung.md](docs/muendung.md) | Mündungsfeuer und Hülsenauswurf: Blitzdauer und -größe, Überdeckung des Visiers, Hülsen, Mündungsform; Destiny 2 mit Destiny 1, Halo, Titanfall 2, Apex, CoD, Borderlands 3 und Battlefield 6 (`data/muendung.json`) |
| [docs/inspektion.md](docs/inspektion.md) | Inspektionsanimationen: Menüinspektion (Destiny 2, Borderlands 3), Idle-Gesten (Halo), Ego-Inspect (Apex, CoD, Valorant, CS2, Battlefield 6) – Ablauf, gezeigte Seiten, Fläche, Medienzeiten (`data/inspektion.json`) |
| [docs/auswertung.md](docs/auswertung.md) | Gesamtauswertung: Vergleich der Vorgänge, belegte Muster, Widersprüche und offene Fragen |
| `docs/cube-escape.md` | Cube Escape selbst, mit denselben Messgrößen vermessen (eigene 60-fps-Aufnahmen aus der Testkopie): Messungen, Steckbriefe je Gerät, Vergleich mit den Vorbildern |
| `data/clips.json` | Clip-Verzeichnis: Messung, Clip-URL, Quelle, Zeitstempel |
| `tools/reference_frames.py` | Werkzeug: Clips finden/laden, Kontaktbögen (2/s, 10/s, native Rate), Mittenkreuz |
| `tests/` | Werkzeugtests (`./check`) |
| `ce` | Einstieg in die gemeinsamen Werkzeuge (Lader aus ce-agent-tools, Stand in `.ce-repo.json` › `tools_version`; keine eingebettete Kopie) |
| `docs/versions/0.md` | Versionsberichte |

Prüfen: `./check`. Messen: `python3 tools/reference_frames.py --help` (Ablauf in `docs/destiny2.md` › 2 › Methode).
Clips und Kontaktbögen bleiben außerhalb des Repos (Urheberrecht, Größe); hier liegen nur Zahlen, Beschreibungen und Verweise.
