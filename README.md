# cubeescape-reference

Zentraler Repo-Einstieg: [Nexogen](https://github.com/ffunkfabian-hash/cubeescape-nexogen) – Repo-Links, Zuständigkeiten, Abhängigkeiten und Live-Status über die Status-CLI im Nexogen-Repo. Globale Regeln dort, Fachwissen und Prüfbelege hier.

Referenzmessungen für das Ego-Spielgefühl von **Cube Escape**: wie Vorbilder (zuerst Destiny 2) Waffen und Werkzeuge halten, zielen,
wechseln, nachladen und bewegen – gemessen an 60-fps-Aufnahmen, als Zahlen mit Zeitstempeln und Steckbriefen je Typ. Cube Escape,
Toolgen und das Design-Repo lesen hier; entschieden und umgesetzt wird dort.

| Pfad | Inhalt |
|---|---|
| `docs/destiny2.md` | Messungen (Tabelle mit Clip und Zeitstempeln) und Steckbriefe je Waffentyp |
| `docs/apex.md`, `docs/titanfall2.md` | Bewegungs-Vorbilder: Sprint, Rutschen, Sprung/Landung, Wandlauf, tiefe Hüfte (je ein Steckbrief) |
| [docs/visiere.md](docs/visiere.md) | Visiere in Videospielen: Darstellungsarten, Zahlen im Zielen, Form, Sitz, Absehen, Glas, Spielerstimmen, Empfehlungen für BASIC (`data/visiere.json`) |
| [docs/proportionen.md](docs/proportionen.md) | Waffenproportionen und Silhouetten: Verhältnisse je Klasse (Destiny 2 und fünf Vergleichsspiele), was schlank macht, BASIC-Abweichungen (`data/proportionen.json`) |
| [docs/rueckstoss.md](docs/rueckstoss.md) | Rückstoßmuster in Videospielen: Nettobahnen, Takt, Rücklauf, Systemfassungen, Musterkatalog je Klasse, Gestaltungsregeln für BASIC (`data/rueckstoss.json`) |
| [docs/zielbewegung.md](docs/zielbewegung.md) | Zielbewegung im Zielen: Rückstoß im ADS gegen Weltanker, Halten, Punkt im Glas, Hüfte → Zielen; Destiny 2 mit Battlefield 2042, Apex und Halo im Vergleich (`data/zielbewegung.json`) |
| [docs/auswertung.md](docs/auswertung.md) | Gesamtauswertung: Vergleich der Vorgänge, belegte Muster, Widersprüche und offene Fragen |
| `docs/cube-escape.md` | Cube Escape selbst, mit denselben Messgrößen vermessen (eigene 60-fps-Aufnahmen aus der Testkopie): Messungen, Steckbriefe je Gerät, Vergleich mit den Vorbildern |
| `data/clips.json` | Clip-Verzeichnis: Messung, Clip-URL, Quelle, Zeitstempel |
| `tools/reference_frames.py` | Werkzeug: Clips finden/laden, Kontaktbögen (2/s, 10/s, native Rate), Mittenkreuz |
| `tests/` | Werkzeugtests (`./check`) |
| `ce` | Einstieg in die gemeinsamen Werkzeuge (Lader aus ce-agent-tools, Stand in `.ce-repo.json` › `tools_version`; keine eingebettete Kopie) |
| `docs/versions/0.md` | Versionsberichte |

Prüfen: `./check`. Messen: `python3 tools/reference_frames.py --help` (Ablauf in `docs/destiny2.md` › 2 › Methode).
Clips und Kontaktbögen bleiben außerhalb des Repos (Urheberrecht, Größe); hier liegen nur Zahlen, Beschreibungen und Verweise.
