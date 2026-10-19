# cubeescape-reference

Referenzmessungen für das Ego-Spielgefühl von **Cube Escape**: wie Vorbilder (zuerst Destiny 2) Waffen und Werkzeuge halten, zielen,
wechseln, nachladen und bewegen – gemessen an 60-fps-Aufnahmen, als Zahlen mit Zeitstempeln und Steckbriefen je Typ. Cube Escape,
Toolgen und das Design-Repo lesen hier; entschieden und umgesetzt wird dort.

| Pfad | Inhalt |
|---|---|
| `docs/destiny2.md` | Messungen (Tabelle mit Clip und Zeitstempeln) und Steckbriefe je Waffentyp |
| `docs/apex.md`, `docs/titanfall2.md` | Bewegungs-Vorbilder: Sprint, Rutschen, Sprung/Landung, Wandlauf, tiefe Hüfte (je ein Steckbrief) |
| [docs/auswertung.md](docs/auswertung.md) | Gesamtauswertung: Vergleich der Vorgänge, belegte Muster, Widersprüche und offene Fragen |
| `docs/cube-escape.md` | Cube Escape selbst, mit denselben Messgrößen vermessen (eigene 60-fps-Aufnahmen aus der Testkopie): Messungen, Steckbriefe je Gerät, Vergleich mit den Vorbildern |
| `data/clips.json` | Clip-Verzeichnis: Messung, Clip-URL, Quelle, Zeitstempel |
| `tools/reference_frames.py` | Werkzeug: Clips finden/laden, Kontaktbögen (2/s, 10/s, native Rate), Mittenkreuz |
| `tests/` | Werkzeugtests (`./check`) |
| `docs/versions/0.md` | Versionsberichte |

Prüfen: `./check`. Messen: `python3 tools/reference_frames.py --help` (Ablauf in `docs/destiny2.md` › 2 › Methode).
Clips und Kontaktbögen bleiben außerhalb des Repos (Urheberrecht, Größe); hier liegen nur Zahlen, Beschreibungen und Verweise.
