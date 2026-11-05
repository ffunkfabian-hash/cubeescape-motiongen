# Lehren

Nur wiederkehrende Dauer-Fallen. Alle Lehren im Wortlaut (auch Einzelfälle der Versionen): [LESSONS-lang.md](LESSONS-lang.md), per `rg -n` durchsuchen.

- Messwerte sind Beispiele eines Clips, keine Archetyp-Mittelwerte ([Regeln](../AGENTS.md)).
- Stabile benannte Anker verwenden; Zeilennummern verschieben sich ([Regeln](../AGENTS.md)).
- Keine fremden Videos oder privaten Daten ins öffentliche Repo übernehmen ([Regeln](../AGENTS.md)).
- Erkenntnisse in Messdaten halten; Schlussfolgerungen gehören ins Spielprojekt ([Regeln](../AGENTS.md)).
- Gemeinsame Werkzeuge nicht einbetten: `./ce` lädt den gepinnten Stand aus ce-agent-tools; Stand nur mit eigener Version wechseln ([0.13](versions/0.md#0130-lightfoot--2026-10-23)).
- `sheet` bei niedriger Bildrate: Kachel zeigt ein Bild eine halbe Abtastperiode nach ihrer Beschriftung – Zahlen nur aus Einzelbildern oder Bögen ≥ 5/s ([visiere](visiere.md#1-quellen-und-methode)).
- Zuarbeit anderer Agenten (Antigravity) vor Übernahme per yt-dlp gegen Kanal/Titel prüfen und eine Stichprobe am Bild nachmessen; erfundene Quellen kommen vor ([visiere](visiere.md#1-quellen-und-methode)).
- Weltanker auf sich wiederholender Struktur (Turmsegmente, Wolken, Paneele) springt mit hoher Korrelation auf den falschen Abschnitt; jede Bahn mit einem zweiten, anders aussehenden Anker prüfen ([rueckstoss](rueckstoss.md#7-offen-und-nicht-messbar)).
- Zuarbeit nicht nur an der Quelle prüfen, sondern jedes Beispiel zum Zeitstempel am Bild: echte Video-IDs trugen in 0.18 falsche Waffen und erfundene Farbbeschreibungen ([oberflaechen](oberflaechen.md#1-quellen-und-methode)).
- Regeln einmal festschreiben statt je Prompt kopieren: der [Analyse-Standard](standard.md) gilt für jede Zuarbeit, Aufträge entstehen aus der [Vorlage](vorlagen/auftrag-analyse.md) ([0.21](versions/0.md#0210-playbook--2026-10-25)).
- Wippfrequenz nur aus ≥ 4 Zyklen an einer **festen** Vorlage messen; nachgeführte Vorlagen springen auf Nachbarkanten und täuschen Doppelgipfel vor, Halbwellen und 30/s-Lesungen trugen keine Frequenz ([Methode 21](destiny2.md#methode-21)).
- Linkprüfung mit `curl`, nicht mit Python-`urllib` (ohne CA-Zertifikate meldet es jede HTTPS-Seite tot); Polycount-Wiki lädt nur per http, GDC Vault war am 28.10.2026 in Wartung – „nicht geladen“ eines Unteragenten selbst nachprüfen ([0.30](versions/0.md#0300-blueprint--2026-10-28)).
- Rückstoß nie mit nachgeführter Vorlage messen: beim Kippen springt sie auf andere Bauteile (Annual Skate: 12,6 statt ≈ 23 pp H); Beträge an einer festen Landmarke von Hand prüfen ([Methode 30](destiny2.md#methode-30)).
