# Repertoire – Posen, Bewegungsarten und Waffenaktionen von außen

Referenzanalyse REF 0.43 „Repertoire“ (27.11.2026). Abnehmer sind **Critic** (Roboter-Ganzkörper), **BALLON** (Waffe am Körper) und **Cube Escape**
(die Isometrie-Kamera zeigt den eigenen Roboter). Die Fragen kamen vom Nutzer: alle Posen, Animationen und Bewegungen, die Destiny 2 und The Division 2 zeigen –
Ducken, Rutschen, geduckt Gehen, Springen und mehr, möglichst von außen. Dazu kamen die Nachladeanimationen je Waffentyp und die Haltung der Waffe
in verschiedenen Posen. Daraus ergeben sich zwei Hauptziele:

- **(1) Bewegung und Posen:** ein Katalog der Zustände mit Zahlen, wo die Quelle sie trägt.
- **(2) Waffenaktionen:** Nachladen je Typ und Haltung der Waffe je Körperpose.

Hier stehen Beobachtungen und Zahlen; entschieden wird in Critic, BALLON und Cube Escape. Maschinenlesbar: [`data/repertoire.json`](../data/repertoire.json).
Bestand, auf dem diese Version aufbaut und den sie nicht wiederholt:
- [aussenansicht.md](aussenansicht.md): REF 0.32–0.42 – Gang, Rutschen, Landungen, Rückenwaffe, Nachladen von außen
- [nachladen.md](nachladen.md): Ego-Nachladezeiten Destiny 2
- [wechsel.md](wechsel.md)
- [nahkampf.md › 4](nahkampf.md#4-destiny-schwert-in-der-schulteransicht): Schwert in der Schulteransicht

**Status:** **[M]** am eigenen Einzelbild gemessen (echte 60/s je Messfenster geprüft); **[O]** Sichtung ohne belastbare Zahl; **[C]** Spielerstimme;
**[S]** Fachquelle; **[B]** Entwickler. **Jede Zahl ist das Beispiel einer Figur oder Waffe in einer Aufnahme** – kein Klassenmittel; Perks, Talente und
Reload-Wert sind unbekannt. Höhen in **Körperhöhen (KH)** der stehenden Figur am selben Bildausschnitt, Lagen in % B/H, Winkel zur Waagrechten
(+ = Mündung oben), ±5°.

**Kurzbefund**

- **Destiny 2 zeigt die eigene Figur von außen nur in Sonderlagen:** Super, gezogenes Schwert, Sparrow, Angeln, Emote, Finisher, Bug- und Glitch-Kameras.
  Den vollständigen Katalog mit dem Stand „von außen belegt / nur Ego / nicht gefunden“ zeigt [2.1](#21-katalog-was-es-gibt-und-was-von-außen-belegt-ist).
- **Neu gemessen (Destiny 2):**
  - [Super-Aktivierung](#r-super): meist **35–37 Bilder (≈ 0,6 s)** vom Kamerawechsel bis zum Blitz; über alle 12 Supers 12–55 Bilder.
  - [Ausholhocke Sentinel Shield](#r-sentinel): **≤ 0,68 KH** (Bezug ist ein Ausfallschritt, die volle Standhöhe liegt eher höher).
  - [Jäger-Sprung mit Schwert](#r-schwertsprung): 65 Bilder Luft, danach 8 Bilder Kniebeuge.
  - [Sparrow](#r-sparrow): Aufsteigen ≈ 10–12 Bilder, Absteigen 22.
- **Destiny 2, nicht belegt:**
  - echtes Ducken und geduckt Gehen von außen;
  - Sprungarten je Klasse ohne Schwert;
  - Hochziehen an Kanten.
- **The Division 2 kennt kein freies Ducken** – in allen neun Quellen nicht zu sehen; eine Hocke gibt es nur in und zwischen Deckungen ([O], als Spielregel unbelegt).
  - **Deckungshöhen:** [hoch 1,0 KH, seitlich am Pfeiler 0,92, beim Losgehen geduckt 0,83, niedrig **0,64**](#r-dv-deckung).
  - **Deckung zu Deckung:** [78 Bilder](#r-dv-c2c).
  - **Rolle:** [18–28 Bilder bis Boden, 28–48 bis Hocke](#r-dv-rolle), je nach Start.
  - **Mauersprung:** [66 Bilder ab der Krone](#r-dv-mauer), danach Hocke (+18) oder Abrollen (+48).
  - **Akrobatik:** Rolle, Sprung und Fall laufen mit freien Händen, die Waffen bleiben am Rucksack.
- **Nachladen Destiny 2 je Typ (Ego, 63 Abschnitte, 59 mit Dauer, Normaltempo vierfach belegt)** – Dauer bis ruhig ([3.1](#31-destiny-2--nachladen-je-waffentyp-ego)):

  | Typ | Dauer bis ruhig |
  |---|---|
  | Pistolen | 2,07–3,10 s |
  | Gewehre/MP | 1,77–3,35 s |
  | Scharfschütze | 2,12–3,55 s |
  | Fusion/Linear | 2,80–3,63 s |
  | Werfer | 2,85–3,72 s |
  | MG | 4,23–5,47 s |

  Die Typen überlappen stark: Die **Bauform** (Revolver, Kastenmagazin, Trommel, Deckel) trennt die Abläufe mehr als der Typ. Von außen ist das
  Nachladen je Typ in Destiny weiter nicht lesbar.
- **Nachladen The Division 2 je Klasse (dritte Person)** ([3.3](#33-the-division-2--nachladen-je-waffenklasse-dritte-person)):
  - **Magazinwaffen:** eine Grundform – Waffe steil bis senkrecht (60–85°) vor der rechten Schulter, linke Hand am Schacht. Die Klasse ändert nur die
    Dauer bis HUD: MP 72/83, Sturmgewehr 90, Gewehr 113, Magazin-LMG 117 Bilder.
  - **Gurt-MG:** waagrecht in Hüfthöhe, 186 Bilder.
  - **Einzelpatronen:** Pumpflinte ≈ 31 Bilder je Patrone, Repetierer ≈ 41.
  - **Repetieren:** verlässt das Zielfernrohr für 66–67 Bilder.
- **Waffenhaltung je Pose** ([3.4](#34-waffenhaltung-je-körperpose)):
  - **Division:** In Ruhe zeigt die Mündung nach unten (Tragen −20 bis −45°, Deckung −35 bis −45°, geduckter Lauf −50°, seitlich am Pfeiler senkrecht),
    in Bereitschaft nach oben (+70°, ein Beispiel; Vault +90° [O]).
  - **Destiny-Schwert:** bleibt beim Rutschen senkrecht in der Hand. Sprung und Landung messen nur die Klingenstellung im Jäger-Luftangriff mit Schwert:
    −11° beim Absprung, +7° bei der Landung.
  - **Sprint, Rutschen und Sprung mit Feuerwaffe:** sind von außen in keinem der beiden Spiele gemessen.

- **Nachtrag 28.11.2026** (nach Ende der YouTube-Sperre, zwei weitere Messagenten, 10 Ladungen: 7 Videos, davon eines Bestand H-CC, und 3 Abschnitte):
  - **Division, Schrot und Präzision:** Magazin-Schrot [ACS-12 93, SASG-12 113–128 Bilder bis HUD](#r-dv-sasg), steil 75–85°.
    [Röhrenflinte Super 90](#r-dv-super90): 29 Bilder je Patrone, lädt **tief vor der Hüfte (+20 bis +30°)**, flacher als die Pumpflinte.
    Das Präzisionsgewehr SR-1 braucht 136 Bilder bis HUD.
  - **Division, Seitenwaffen:** nur 24–28 echte Bilder/s, daher [O]. Ziehen der Pistole [≈ 18–20 Bilder](#r-dv-ziehen), Revolver steil neben dem Kopf.
  - **Destiny 2, Nachladen von außen am HUD:** Langwaffe [60–61 Bilder vom letzten Schuss bis voll](#r-d2-nachladen-aussen), Waffe steil links neben dem
    Kopf; Handkanone 92 Bilder. Ducken von außen gibt es weiter nur [ohne Maß](#r-d2-gegner-hocke).

## 1. Quellen und Methode

- **Arbeitsweise:** Fünf Unteragenten mit je eigenem Ordner unter `~/Library/Caches/CubeEscape/reference/aussenansicht/repertoire/`:
  - vier Messagenten, Opus, Denkaufwand high: Destiny Bewegung `md/`, Division Bewegung `mv/`, Destiny Nachladen `wd/`, Division Nachladen `wv/`;
  - ein Rechercheagent, Sonnet, Denkaufwand medium: Spielerstimmen und Fachquellen `st/`.

  Ein gemeinsamer Auftrag (`AUFTRAG.md`) mit Nachtrag „Waffenhaltung je Pose“. **Ein Lader** lud alle Videos nacheinander aus einer Warteschlange
  (Lehre 0.41): 43 Video-IDs eingereiht, 42 geladen, eine scheiterte an der YouTube-Sperre (`hiIqzpBSMvk`). Keiner der Agenten schrieb ins Repo.
- **Bildrate:** Die echte Rate ist je Messfenster über den Anteil wiederholter Bilder geprüft. Zeiten stammen nur aus Fenstern mit ≈ 60 echten Bildern/s (Schwelle ≥ 55/s, Marker dann ±2),
  30/s-Quellen nur für Form. Bildindex n = Containerbild (Zeit × Containerrate). Bei Abschnitts-Clips (`<id>_<a>-<b>`) zählt n ab dem Abschnittsbeginn,
  Videozeit = a + n/60. Marker ±1–3 Bilder je nach Zeile.
- **Nachtrag (28.11.2026):** Alle YouTube-Abrufe liefen über einen Lader mit Pausen (Suche, Metadaten, Download). Zwei Messagenten (Opus, high):
  Division Schrot/Präzision/Seitenwaffen `wv2/`, Destiny außen `md2/`. Der Koordinator prüfte 8 Stellen am Einzelbild: 6 bestätigt, 2 verworfen.
  - **Verworfen 1:** Der Destiny-Agent las die Rückenwaffe in H-CC als neue „Tragehaltung −42°“. Der Bestand ([aussenansicht › Rücken](aussenansicht.md#a-h-ruecken))
    hat genau diese Lage schon als verstaute Waffe gemessen (54° / 47°), die Hände sind leer.
  - **Verworfen 2:** Seine Falldauer von ≈ 50 Bildern widerspricht dem Bestand (Aufsatz n 3487). Am Bild ist die Figur bei n 3468–3482 noch in der Luft.
- **YouTube-Sperre:** Ab ≈ 23:25 verlangte YouTube für jeden yt-dlp-Abruf eine Bot-Prüfung, auch für Metadaten. Kanal, Datum und Titel prüften die
  Agenten vorher mit yt-dlp. Die Koordinator-Gegenprobe von Kanal und Titel lief danach über die oEmbed-Schnittstelle (ohne Datum).

**Videoquellen, gemessen oder ausgewertet** (Kanal | Datum | Titel aus yt-dlp; echte Rate im Messfenster)

| Kürzel | ID | Kanal \| Datum \| Titel (gekürzt) | Rate | Art / Sicht | hier |
|---|---|---|---|---|---|
| <a id="q-ab"></a>**MD-AB** | [`RMLZqmCW4q4`](https://www.youtube.com/watch?v=RMLZqmCW4q4) | Ultraclocked \| 04.06.2026 \| Destiny 2 vs Warframe - Abilities | 60 | showcase / außen (Super) | Super-Aktivierung, Sentinel-Hocke |
| **MD-SW** | [`tTjwM26ilgo`](https://www.youtube.com/watch?v=tTjwM26ilgo) | Ultraclocked \| 21.04.2026 \| Destiny 2 vs Warframe - Sword Animations | 60 | showcase / außen (Schwert) | Schwertsprung, Landung, Slam |
| **MD-SP** | [`leq_6q7wcZs`](https://www.youtube.com/watch?v=leq_6q7wcZs) | Ultraclocked \| 07.11.2026 \| Destiny 2 Sparrow vs Warframe Atomicycle | 54–57 | showcase / außen | Sparrow auf-/absteigen |
| **MD-TB** | [`MX6PRar-Iyw`](https://www.youtube.com/watch?v=MX6PRar-Iyw) | elitebeat DURNT \| 28.12.2021 \| how to D2 teabag faster | 59,94 | retail (Gambit) / außen (Arc Staff) | Ducken-Spam, Stabhaltung |
| **MD-SF** | [`r29lliwIu_s`](https://www.youtube.com/watch?v=r29lliwIu_s) | JB3 \| 13.02.2022 \| Third Person Selfie Glitch | 60 | glitch (Titan, Schwert) / außen von vorn | Rutschen von vorn |
| MD-FI, MD-EM, MD-SK, MD-FL, MD-LA | `kr9Urtv9H9M`, `jwPRB86SfGY`, `3JghPtGYdUI`, `EmNirZEBzuk`, `79Bn2_BdXQA` | Ultraclocked (Angeln), GameSpot (Emotes 2017), Aoterra, FLTR, glitchtutorial (Schwert-Skaten/-Fliegen) | 24–59 | showcase/retail | nur Form [O] |
| MD2-AN, MD2-MT (Nachtrag) | [`eFXF-P8dtPQ`](https://www.youtube.com/watch?v=eFXF-P8dtPQ), [`noqzBxvSqy4`](https://www.youtube.com/watch?v=noqzBxvSqy4) | ANDI \| 12.02.2025 \| Destiny 2 3rd person all weapons glitch??; Mtashed \| 19.09.2019 \| Making Some Destiny 2 T-Baggers Cry: | 60 | bug / außen (Titan, klein); retail PvP, Todeskamera | Handkanone am HUD; Gegnerhocke |
| H-CC (Bestand, Nachtrag erneut) | [`vzcGQI-O_qc`](https://www.youtube.com/watch?v=vzcGQI-O_qc) | Canoecarver \| 06.02.2025 \| Destiny 2 in 3rd person. (bug) | 59,94 (in den Messfenstern 0–1 Doppelbilder) | bug / außen (Titan, Schulterkamera) | Nachladen am HUD und Körper; ganz durchgesehen: kein Ducken, Rutschen, Ausweichen, Gleiten, Hochziehen |
| MD-AJ, MD-AG, MD-FN, MD-FS | `2V_jR5JdK8I`, `q8WndXSY6f8`, `zWxsBjXG_g8`, `CP_YvP_TTM8` | AJ (Bug 2024), Mr. Dweebs (Bug 2023), CantWant und AditRaidaa (Finisher) | 30–60 | bug/showcase | nur Form [O] |
| H-KW (Bestand) | [`3fClbInDPHo`](https://www.youtube.com/watch?v=3fClbInDPHo) 880–1440 s | Kawffee \| 10.01.2021 \| Destiny 2: Third-Person | 60 | glitch | erstmals durchgesehen: kein Rutschen, Ducken, keine Kante |
| <a id="q-nis"></a>**WD-NIS** | [`nis07-5BXuo`](https://www.youtube.com/watch?v=nis07-5BXuo) | Ultraclocked \| 13.09.2026 \| Destiny 2 - All Weapon Reload Animations in 3 minutes 33 seconds (FINAL) | 60 (≈ 0,1 % Doppelbilder) | showcase / Ego, ohne HUD | 63 Nachlade-Abschnitte (64 Schnitte) |
| **WD-XBI** | [`xBiUSxDcd2g`](https://www.youtube.com/watch?v=xBiUSxDcd2g) | Ultraclocked \| 22.10.2026 \| Destiny 2 vs Warframe - Weapon Reload Animations | 60 | Destiny Ego (dieselben Aufnahmen, Kapitel je Typ), Warframe außen | Typzuordnung, Warframe-Vergleich |
| WD-K12, WD-8UW | [`kal12oig1oU`](https://www.youtube.com/watch?v=kal12oig1oU), [`8uW8m_W8akk`](https://www.youtube.com/watch?v=8uW8m_W8akk) | Ultraclocked \| 16.07.2026 \| All Exotic Weapon Reloads in 37 seconds \| Year 8/9; Ultraclocked \| 12.07.2025 \| … in 41 seconds \| Year 7 | 60 (0–2 Doppelbilder je Vorgang) | Ego, Normaltempo im Bestand belegt | Tempoprüfung WD-NIS |
| WD-EV | [`F7WYbe19p-U`](https://www.youtube.com/watch?v=F7WYbe19p-U) | Evelyn-8 \| 09.02.2025 \| All Destiny 2 reload animations (Revenant) | ≈ 59 | Ego | Zweitaufnahme (Tempo) |
| WD-JB, WD-MA | `n7s9zSdDpyo`, `6YVvs3x76rY` | Just-B-You \| 13.04.2024; Mackenzie Adalaide \| 03.04.2024 (3rd-Person-Bugs) | 54–60 | bug / außen | Schwerthaltung Titan; Nachladen von Effekten verdeckt |
| <a id="q-tm"></a>**MV-TM** | [`VzjtHWEFrNw`](https://www.youtube.com/watch?v=VzjtHWEFrNw) | TerraMantis \| 19.03.2019 \| 10 Advanced Tips for The Division 2 | 57–60 nur in 89–97 und 105–125 s (97–105 s: 30–40) | retail / außen (teils geteiltes Bild) | Deckungshöhen, Deckung zu Deckung |
| **MV-AB** | [`g0iFqDZC_Qw`](https://www.youtube.com/watch?v=g0iFqDZC_Qw) | aBL1NDnoob \| 29.04.2022 \| Tips on HOW TO MOVE Efficiently in The Division 2 | 59–60 nur in 17–56, 87–99, 106–113, 150–164 s | retail / außen | Rolle, Mauersprung, Takt |
| MV-SH, MV-LG, MV-DV | `jqb7H3HV7gY` (240–840 s), `yIjip7WxhS8`, `X89yYnSbFR8` | Shirrako \| 12.03.2019 (Prolog); LugovoisesGames \| 24.01.2026 (ohne HUD); Dark Veil \| 24.03.2019 („Crouch“) | 52–60 abschnittsweise | retail / außen | Joggen, Vault, Einrasten, Gehen |
| MV-SB, MV-AC, MV-RH, MV-NB | `JR8nS448aq8`, `FDYTVF-xP1M`, `mpTVp8KgQk8`, `bft3kqhKh-c` | ScereBro PSNU (Emotes), Acez (Schulterwechsel), Rachel H (Wiederbeleben, Bug), NothingButSkillz (Menü) | ≤ 35 bzw. Menü | retail/bug | nur Form [O] |
| <a id="q-oc"></a>**V-OC1–3** | [`-CqNxaKFcD8`](https://www.youtube.com/watch?v=-CqNxaKFcD8), [`mk3V564-iHs`](https://www.youtube.com/watch?v=mk3V564-iHs), [`rb3hM7o6gxA`](https://www.youtube.com/watch?v=rb3hM7o6gxA) | OrcCorp \| 05.05.2019 (übrige Reihe ≈ Mai 2019) \| The Division 2 All Basic Assault Rifles & SMGs / LMGs & Shotguns / Marksman Rifles & Rifles (Showcase) | 60 (0–6 Wiederholungen je Fenster) | showcase (Schießstand) / außen | Nachladen je Klasse |
| V-SW | `GjYMr8s8wjQ` | Sweitz \| 18.04.2020 \| That Reload Speed. | 50 | retail, Nachladetalente | nur Form: Nachladen kniend in Deckung |
| V-TB (Nachtrag) | [`hiIqzpBSMvk`](https://www.youtube.com/watch?v=hiIqzpBSMvk) 161–240, 513–589 s | TuxedoBandido \| 01.08.2026 \| I Ranked All 13 Must-Have Sidearms in Division 2 | Container 60, **echt 24–28** | retail + Schießstand / außen | Seitenwaffen, Ziehen – nur [O] |
| V-OC2/3 (Nachtrag) | `mk3V564-iHs` 376–649 s (Schrot-Kapitel), `rb3hM7o6gxA` 74–99 s (neu) | OrcCorp (wie oben) | 55–60 in den Messfenstern (Super 90 ab n 10712 47, Marine Super 90 46 – dort nur [O]) | showcase / außen | Magazin- und Röhrenschrot, SR-1 |

**Verworfen:**
- `y1qCBaVKiQc`: Rainbow Six Siege, kein Destiny.
- `DTLIrhw5UsQ`: Destiny 1, 30/s.
- `p0SbjaEtyLA`: Battlefield 1, kein Division.
- `6z9BfWiVIEQ`: fast nur Ego.
- `0iClaH6VxhE`: 20–39/s.
- `VZZtKZjewzY`: andere, ältere Aufnahmen; nur zur Typzuordnung versucht.
- Nachtrag: `zOuaFLYJlCQ` (echt ≈ 30/s), `0wUsEQk5J2M` (nur Ego, ≈ 27/s), `d1gWKPQFZ18` (48/s, zu dunkel), `l7CkRni4ga8` (31.05.2017, Destiny 1, 30/s), `BaLjswEh_jA` (JB3, Kameramodus blendet die Figur aus), Division-Leiterclips
  `OBp-9D77Ips`, `KcJdUXUDXEE`, `pRWOUUYrO4A` (30/s, nichts Neues gegenüber 0.43).

**Nicht ladbar:**
- `cdTDQpC6bh4`, `w4pH16hxehM`: Zeitlupe und Rückwärtsfassung von WD-NIS, nur für Kanalmitglieder.
- `hiIqzpBSMvk`: Seitenwaffen Division – am 28.11. nachgeladen (Nachtrag), aber nur 24–28 echte Bilder/s.

**Kandidaten für eine Folgesitzung** (Metadaten geprüft, nicht geladen):
- **Division 60/s:** `bq3zuO7ZN1A`, `npHOc_HehsI`, `wKi980DRHe8`, `oLfOl6bNMfc`, `Ve_d57J6ZbY`, `EoBZ9IcAO2A`, `jH5yrWsAYZg`.
- **Division-Kapitel:** im Nachtrag erledigt – das Schrot-Kapitel lag schon im Abschnitt 376–649 s (in 0.43 fälschlich „nicht geladen“), 74–99 s nachgeladen.
- **Destiny:** `JjU2L3fBKNQ` Metadaten im Nachtrag geprüft (Ultraclocked \| 29.07.2023, 60/s, Schwertornament); `1ITfE8_Ux6I`, `dnw6p9nT8dQ` (Ultraclocked-Schwertornamente) ungeprüft.

## 2. Ziel 1 – Bewegung und Posen

### 2.1 Katalog: was es gibt und was von außen belegt ist

„außen [M]“ = gemessen in dritter Person, „außen [O]“ = gesichtet, „Ego“ = nur aus der Ich-Sicht bekannt, „–“ = gibt es nicht oder nicht gefunden
(Grund in [5](#5-offen-und-nicht-messbar)). Bestand = frühere Version, hier nur zitiert.

| Zustand | Destiny 2 | The Division 2 |
|---|---|---|
| Stand / Leerlauf | außen [O] (Turm, Menü; Bestand aussenansicht › 2.2) | außen [M] Menü/Gehen, Emote-Neutralstand [O] |
| Gehen | außen [O] (Turm, Oberkörper; Bestand) | außen [M Lage] Gewehr −45° |
| Laufen | außen [M vorl.] Titan 3,41 / Warlock 3,2–3,3 Schritte/s (Bestand) | außen [M vorl.] ≈ 3,3 Schritte/s; Joggen im Prolog ≈ 42 Bilder je Zyklus |
| Sprint | nicht trennbar vom Lauf (keine Eingabeanzeige) | Bestand: Gewehr tief vor dem Bauch −30 bis −45°; von Lauf nicht trennbar |
| **Ducken (Stand)** | **von außen nicht gemessen** – nur Ducken-Spam im Super ([Hub 0,07 KH](#r-teabag)), Ausholhocke ([≤ 0,68 KH](#r-sentinel)) und eine Gegnerhocke in der Todeskamera ohne Maß ([O, Nachtrag](#r-d2-gegner-hocke)) | **kein freies Ducken** [O]; Hocke nur in Deckung ([0,64 KH](#r-dv-deckung)) |
| **Geduckt gehen** | **von außen nicht gefunden** | nur als geduckter Lauf zwischen Deckungen ([Rumpf ≈ 45° vor](#r-dv-geduckt), 0,83 KH beim Losgehen) |
| **Rutschen** | außen [M] Bestand H-NC ≈ 33 Bilder; [von vorn mit Schwert](#r-rutschen-vorn) [O] | – (gibt es nicht als freie Bewegung; „Rutschen über die Motorhaube“ als Vault in Stimmen) |
| **Sprung** | außen [M] nur [Jäger mit Schwert und Luftangriff](#r-schwertsprung); Klassen-Sprünge (Lift, Gleiten, Dreifach) nur Bestand/Glitch [O] | kein freier Sprung; Sprung nur an Kanten ([Mauer](#r-dv-mauer), Geländer) |
| Fall / Landung | außen [M] Bestand Titan ohne Abfanghocke 4–7 Bilder; [nach Luftangriff Hocke 8 Bilder](#r-schwertsprung) | außen [M] [Hocke +18 oder Abrollen +48](#r-dv-mauer); aus großer Höhe tiefe Hocke und Rolle [O, 30/s] |
| Hochziehen / Klettern | Mantle im Spiel vorhanden, **von außen nicht gefunden** | Hochziehen an Mauerkrone [O, 30/s]; Vault mit senkrechter Waffe [O] |
| Ausweichen / Rolle | Jäger-Ausweichen nur Ego | außen [M] [Hechtrolle](#r-dv-rolle) |
| Deckung | – (kein Deckungssystem) | außen [M] hoch / seitlich / niedrig, [Deckung zu Deckung 78 Bilder](#r-dv-c2c), Einrasten 22 Bilder (vorl.) |
| Leiter / Abseilen / Kriechen | – | nur 30/s-Clips gefunden (nicht geladen) |
| Super / Fähigkeit | außen [M] [12 Supers](#r-super), Wirkposen [O] | Granate/Skill von außen nicht bildgenau gefunden |
| Schwert | außen [M] (Bestand nahkampf › 4; hier Sprung, Landung, Rutschen) | – |
| Reiten | außen [M] [Sparrow auf/ab](#r-sparrow) | – |
| Angeln | außen [O] Wurf (24–34/s) | – |
| Emote | Vorschau [O], 40 Emotes ohne Waffe (2017), Taunt-Hocke ≈ 0,7–0,8 | [O] ≤ 30/s, Waffen bleiben am Rucksack |
| Finisher | außen [O] (Zusammenschnitte 30/s) | – |
| Am Boden / Wiederbeleben | Geist statt Animation (nicht untersucht) | [O] 30/s: Helfer kniet auf einem Knie |
| Schulterwechsel | – | [O] ≤ 35/s, Kamera springt, Figur dreht nicht |

### 2.2 Destiny 2 – Messzeilen

| Vorgang | Quelle, Zeit (Bilder) | Messung |
|---|---|---|
| **Super-Aktivierung: Kamera Ego → dritte Person bis Blitz** [M] <a id="r-super"></a> | MD-AB, je Super ein Kapitel (Bilder in `data/repertoire.json`) | **Jäger:** Arc Staff 37, Spectral Blades 28. **Titan:** Fists of Havoc 31, Thundercrash 36 (startet in der Luft), Sentinel Shield 36, Bladefury 35. **Warlock:** Stormtrance 24, Daybreak 35, Well of Radiance 47, Song of Flame 37, Nova Warp 12, Winter's Wrath 55 Bilder (±2). Häufung **35–37 Bilder (0,58–0,62 s)**; kürzer, wo die Figur schwebt oder verschwindet; länger bei Bodenkreisen. Der Wechsel ist ein harter Schnitt; danach weicht die Kamera zurück (Figur ≈ 60 → 18 % H in ≈ 15 Bildern beim Well). Normaltempo nicht über eine Uhr belegt, kein Zeitlupenhinweis |
| **Ausholhocke Sentinel Shield (Titan)** [M] <a id="r-sentinel"></a> | MD-AB n 18874 gegen n 18912 (≈ 0,6 s später) | Figur in der Hocke 27 pp H, stehend mit Schild 40 pp H, Sohle gleich tief → **0,68 KH** (±0,06); Koordinator 0,66–0,69. Die stehende Vergleichspose ist ein Ausfallschritt – die volle Standhöhe liegt eher höher. Einziger KH-Wert einer Hocke bei 60/s, **aber kein freies Ducken** |
| Wirkposen Stormtrance, Well, Fists [O] | MD-AB n 25890–25914, 33931–33976, 12960–13030 | Stormtrance: Arme vor der Brust gekreuzt, steigt auf, krümmt sich nach vorn, schwebt danach mit hängenden Beinen. Well: steigt mit Schwert auf, sticht in den Boden. Fists: vorgebeugter Lauf mit geballten Fäusten |
| **Sprung mit Schwert und Luftangriff (Jäger)** [M] <a id="r-schwertsprung"></a> | MD-SW, Absprung n 7524 → Aufsatz n 7589 → aufrecht n ≈ 7596 | **Luft ≈ 65 Bilder (1,08 s, ±2)** einschließlich Angriff in der Luft – keine reine Sprungdauer. **Landung in tiefer Kniebeuge, 8 Bilder bis aufrecht** (±2). Klinge: Absprung −11° rechts-hinten, Landung +7° waagrecht rechts, Stand −14°. Sprunghöhe in KH nicht messbar (Figur läuft von der Kamera weg). Koordinator: Absprung, Aufsatz mit Staub und aufrecht am Einzelbild bestätigt |
| **Sparrow rufen/aufsteigen, absteigen** [M] <a id="r-sparrow"></a> | MD-SP n 38 → 48; n 8758 → 8780 → 8794 | Aufsteigen **≈ 10–12 Bilder** vom Kamerawechsel bis Sitzen (seitlicher Sprung); Absteigen **22 Bilder** bis Fuß am Boden, 36 bis zum Schnitt in Ego (±2, Fenster 54–57/s). Koordinator: Sitzen n 8758 und Figur neben dem Fahrzeug n 8780 bestätigt; ob der Fuß bei n 8780 schon aufsetzt, ist am Bild nicht sicher |
| **Ducken-Spam („Teabag“) im Arc Staff** [M, vorläufig] <a id="r-teabag"></a> | MD-TB n 2557 → 2644 | Hochpunkte über die rote Rüstung: **10 Zyklen in 87 Bildern = 8,7 Bilder je Zyklus**, Hub nur **≈ 0,07 KH** – bei diesem Takt erreicht die Figur die volle Hocke nicht. Vorläufig: Super-Haltung, Eingabe unbekannt (Makro wahrscheinlich) |
| Haltung Arc Staff im Stand [M Lage] | MD-TB n 2520 | Stab beidhändig quer, links oben (22 / 57 %) nach rechts unten (52 / 82 %), **≈ 25°**, Jäger leicht gebückt |
| **Rutschen von vorn mit Schwert (Titan)** [O]/[M Lage] <a id="r-rutschen-vorn"></a> | MD-SF n 186 → 192–200 → 240 | ein Bein gestreckt vorn, das andere angewinkelt, Rumpf aufrecht; **Schwert bleibt senkrecht in der rechten Hand** wie im Stand. Kamera fährt zurück → keine KH. Selfie-Glitch, keine Retail-Kamera. Koordinator: n 194 am Bild gesehen (Figur klein) |
| Schwert-Slam, Schwert-Skaten, Sword-Fly [O] | MD-SW n 11040–11127; MD-SK; MD-FL | Fall mit Klinge nach unten, Staub, Aufrichten; Gleiten in hockeähnlicher Lage mit Rückenwaffe neben dem Schwert; Fliegen über Sprung-Angriff-Folgen (Figur 10–20 % H) |
| Angeln, Emote-Vorschau, Finisher [O] | MD-FI n 1250–1320; MD-EM; MD-FN, MD-FS | Angeln: Rute beidhändig über die rechte Schulter zurück, Wurf, Rute ≈ 80° steil. Emotes (2017): keines mit Waffe; Taunt Dance in breiter Hocke ≈ 0,7–0,8 der Standhöhe (30/s, Kamera je Emote evtl. verschieden). Finisher mit Kamerafahrt, nur Form |
| Lauf mit Langwaffe an der Schulter (Warlock, Bug 2024) [O] | MD-AJ n 120–2040 | weiße Langwaffe diagonal vorn an der rechten Schulter – bestätigt Bestand H-KW n 29060 |
| Aufsteigen auf eine Stufe ohne Hände (Titan, Nachtrag) [O] | H-CC n 3290–3310 | Knie hoch, keine Hände, Waffe bleibt in Rückenlage; ≈ 14 Bilder (±3). Kein Hochziehen |
| **Hocke eines Gegners aus Sicht eines zweiten Spielers (Jäger, Nachtrag)** [O] <a id="r-d2-gegner-hocke"></a> | MD2-MT (`noqzBxvSqy4`) n 23366–23412, echte 60/s | Todeskamera folgt dem Gegner: n 23380–23396 **geduckt, breitbeinig, Rumpf vorgebeugt** (Umriss 24–27 pp H), ab n 23400 aufrecht, n 23406 laufend (44 pp H). Die Kamera rückt nach – **keine KH, keine Übergangsdauer**. Erste Hocke ohne Super von außen |

### 2.3 The Division 2 – Messzeilen

| Vorgang | Quelle, Zeit (Bilder) | Messung |
|---|---|---|
| **Kein freies Ducken** [O] | MV-DV n 0–790 („Crouch“), alle neun Quellen | Das Video mit dem Titel „Crouch“ zeigt nur aufrechtes Gehen. In allen neun Quellen kommt eine Hocke nur **in Deckung** und **zwischen Deckungen** vor. Als Spielregel nicht durch eine Fach- oder Entwicklerquelle belegt |
| **Deckungshöhen** [M] <a id="r-dv-deckung"></a> | MV-TM linkes Teilbild: hoch n 5494, niedrig n 5650; seitlich n 6456/6500; Losgehen n 5520 | Hoch an der Barrikade: Kappe 37 / Sohle 96 % H = Bezug **1,0 KH (59 pp)**. **Niedrig (Hocke): 38 pp = 0,64 KH** (±0,05). Seitlich angelehnt am Pfeiler **0,92 KH**. Beim Losgehen in den geduckten Lauf **0,83 KH**. Koordinator: n 5494 und n 5650 am Bild bestätigt (eigene Lesung 0,63) |
| **Deckung zu Deckung (geduckter Lauf)** [M] <a id="r-dv-c2c"></a> | MV-TM n 5548 → 5626 | hohe Deckung verlassen → ruhige Hocke in niedriger Deckung **78 Bilder (1,30 s)**, ±2; Strecke unbekannt (Lauf von der Kamera weg) |
| **Geduckter Lauf seitlich** [M Lage] <a id="r-dv-geduckt"></a> | MV-TM n 6404 | Rumpf **≈ 45° vorgeneigt**, Kopf vor den Hüften, Knie tief; Gewehr tief zweihändig ≈ −50° |
| Einrasten in niedrige Deckung (Auto) [M, vorläufig] | MV-LG n 25748 → 25770 | Abbremsen → ruhige Hocke **22 Bilder (0,37 s)**, ±3; Figur ≈ 25 % H, Kamera dreht mit |
| **Ausweichrolle** [M] <a id="r-dv-rolle"></a> | MV-AB aus der Deckung n 3117 → 3145 → 3165; aus dem Lauf n 3335 → 3353 → 3363 | Aus der Hocke: Hände/Schulter am Boden **+28**, Hocke **+48 Bilder (0,80 s)**, aufrecht +54. Aus dem Lauf: Boden **+18**, Hocke **+28**. Waagrechter Hechtsprung, Überschlag, Waffe bleibt am Rucksack. Bestand V-DS 22 / 38 liegt dazwischen – die Dauer hängt vom Start ab. Koordinator: Marker n 3117/3145/3165 am Bild bestätigt |
| **Über Mauer springen, zwei Landungen** [M] <a id="r-dv-mauer"></a> | MV-AB geteiltes Bild n 6487 → 6604 | Hände auf der Mauer n 6487–6490, oben n 6499–6505, Luftphase mit seitlich ausgestreckten Armen und laufenden Beinen, **Landung n ≈ 6556 (≈ 66 Bilder ab Krone)**; links Hocke, aufrecht **+18**; rechts Abrollen, aufrecht **+48**. Die Lesart weich/hart ist ohne Sprechertext nicht gesichert |
| Hinabspringen über Geländer [M, vorläufig] | MV-AB n 5354 → 5386 | Hand aufs Geländer, Beine darüber, Fall mit hängenden Beinen, Landung aufrecht ≈ 32 Bilder (±3) |
| Laufen von hinten, Takt [M, vorläufig] | MV-AB n 5186–5330 | Autokorrelation Beine 36 / 71 / 107, Rucksack 38 / 73 / 111 → **Zyklus ≈ 36–37 Bilder ≈ 3,3 Schritte/s**; nur 3 Zyklen (4-Zyklen-Regel nicht erfüllt) |
| Waffen am Rucksack beim Laufen [M Lage] | MV-AB n 5250 | zwei Langwaffen senkrecht links und rechts der Rucksackmitte; die linke überragt den Kopf um ≈ 5 pp H (Bestand V-KR mit Schalldämpfer ≥ 15 pp) |
| Hochziehen, Fall aus großer Höhe, Vault [O] | MV-AB n 6024–6048 und 6058–6230 (30/s); MV-SH n 8876–8892 | Hochziehen: beide Hände auf der Krone, ein Knie hoch. Große Höhe: Landung in tiefer Hocke, dann Rolle/Bauchlage. Vault: Gewehr senkrecht in der rechten Hand, Mündung oben |
| Schulterwechsel, Wiederbeleben, am Boden, Emotes [O] | MV-AC, MV-RH, MV-SB (≤ 35/s) | Schulterwechsel: Kamera springt, Figur dreht nicht. Wiederbeleben: Helfer kniet auf einem Knie. Emotes: Waffen bleiben am Rucksack, Neutralstand mit hängenden Armen |

### 2.4 Muster (Beobachtung)

1. **Destiny zeigt Bewegung von außen nur dort, wo das Spiel die Kamera wechselt.** Super, Schwert, Sparrow, Emote und Finisher sind gemessen oder
   gesichtet; die Grundbewegungen Ducken, geduckt Gehen, Klassensprünge und Hochziehen sind Ego-Zustände und von außen nur über seltene
   Bug-/Glitch-Aufnahmen zugänglich – in den durchgesehenen nicht gefunden. Der Kamerawechsel beim Super ist ein harter Schnitt mit ≈ 0,6 s Ansage.
2. **Division bindet die Hocke an die Deckung.** Statt eines freien Duckens gibt es drei Deckungshöhen (1,0 / 0,92 / 0,64 KH) und den geduckten Lauf
   zwischen Deckungen (0,83 KH, Rumpf ≈ 45° vor). Sprung gibt es nur an Kanten (Vault, Mauer, Geländer).
3. **Gewicht über Übergänge:** Landungen nach Angriff (Destiny) oder hohem Sprung (Division) gehen in eine Hocke mit 8–18 Bildern bis aufrecht oder in eine
   Rolle (+48); Landungen aus dem Lauf ohne Angriff kommen ohne Abfanghocke aus (Bestand 4–7 Bilder). Die Rolle dauert je nach Start 18–28 Bilder bis zum Boden.
4. **Zwei Hocken-Werte nahe beieinander:** Destiny-Ausholhocke ≤ 0,68 KH (Bezug Ausfallschritt), Division-Deckungshocke 0,64 KH – zwei Spiele, zwei Vorgänge, keine Klassenwerte.

## 3. Ziel 2 – Waffenaktionen und Waffenhaltung

### 3.1 Destiny 2 – Nachladen je Waffentyp (Ego)

Hauptquelle [WD-NIS](#q-nis): 64 Schnitte, davon 63 Nachlade-Abschnitte (einer ohne Bewegung), 59 mit Dauer (ohne: Abschnitte 0, 54, 55, 63).
- **Typ je Abschnitt** über die Kapitel von WD-XBI (dieselben Aufnahmen, 63 von 63 per Bildvergleich wiedergefunden). Untertypen (Automatik/Impuls/Scout/MP,
  Handkanone/Seitenwaffe) sind **nicht** belegt: keine Waffennamen im Video.
- **Normaltempo vierfach belegt:**
  1. legendärer Raketenwerfer 171 Bilder gegen Bestand 2,58–3,03 s;
  2. Zweitaufnahme WD-EV (201 gegen 203 bzw. 254 gegen 263 Bilder);
  3. sechs Abschnitte gleich den Exotic-Reihen WD-K12/WD-8UW mit belegtem Normaltempo (≤ 3 %; Startmarker gegen Bestand ±1);
  4. eigene Zeitlupenfassung des Kanals (`cdTDQpC6bh4`, 405 s ≈ 1,9 × 213 s) – das Hauptvideo ist die Normalfassung.

  Hinweis: Dass in der Bewegung kaum Doppelbilder vorkommen, schließt nur eine Verdopplung aus, keine Zeitlupe aus einer Hochraten-Aufnahme.
- **Marker:** „Beginn“ = erste Bewegung, „ruhig“ = 6 Bilder ohne Bewegung, ±3 Bilder.
- **Schrotflinten:** Die Abschnitte zeigen nur 2–3 Hülsen – keine Volladung.

| Typ (Kapitel) | Abschnitte | Beginn → ruhig | Bestand zum Vergleich ([nachladen.md](nachladen.md#2-messtabelle); Raketenwerfer [destiny2 › z-bb-rl-nachladen](destiny2.md#z-bb-rl-nachladen), Glefe [z-glefe-vexcalibur](destiny2.md#z-glefe-vexcalibur), [z-nk-glefe-lubrae](destiny2.md#z-nk-glefe-lubrae), übrige aus der Bestandsmatrix in destiny2.md) |
|---|---|---|---|
| Pistolen (Handkanone, Seitenwaffe) | 6 | 2,07–3,10 s (Median 2,41) | Seitenwaffe 1,1–1,75 s |
| MP und Gewehre | 18 | 1,77–3,35 s (Median 2,39) | MP 2,55 s bis Hüfte, Impuls 1,65, Scout 1,7–1,85 |
| Schrotflinte (Teilladung) | 3 | 3,22–3,48 s | Hawthorne 7 Hülsen 5,88, Baligant 5,77 |
| Scharfschütze | 5 | 2,12–3,55 s (Median 2,98) | Far Future 2,18 / 2,23 |
| Fusion / Linear / Spur | 2 | 2,80–3,63 s | Threaded Needle 3,30 |
| Werfer (Granat, Rakete) | 6 | 2,85–3,72 s (Median 3,33) | Raketenwerfer legendär 2,58–3,03, Prospector 4,48–4,62 |
| Maschinengewehr | 2 | 4,23–5,47 s | Shattered Cipher 4,87 |
| Bogen (Nachziehen) | 1 | 2,63 s (ein Showcase-Zyklus) | – |

**Abgleich mit dem Bestand:** Die Spannen überlappen mit dem Bestand. Außerhalb liegen Seitenwaffe (1,1–1,75 s), Impuls und Scout (1,65–1,85 s),
Raketenwerfer legendär (ab 2,58 s), Prospector (4,48–4,62 s), die Glefe des Bestands (2,28–3,07 s) und das MG mit Deckel (5,47 s, 0,6 s über Shattered Cipher) –
andere Modelle bzw. andere Endpunkte (z. B. MP „bis Hüfte“), kein Widerspruch.

**Abläufe je Bauform** (Phasen aus Bögen, ±4 Bilder)

| Bauform | Quelle | Ablauf | Beginn → Ende groß / ruhig |
|---|---|---|---|
| **Revolver-Handkanone** [M]/[O] <a id="r-revolver"></a> | WD-NIS n 622 → 757 / 770 | einhändig. Ablauf: (1) Mündung kippt hoch, (2) **Trommel schwenkt nach links aus** (≈ n 652), (3) Waffe steht senkrecht, Hülsen fallen, (4) Waffe quer vor die Brust, (5) linke Hand bringt den Schnelllader von links, (6) **Trommel schließt per Aufwärtsschwung**. Koordinator: Ruhe, Trommel offen, Rückkehr am Bild bestätigt | 2,25 / 2,47 s (zwei weitere 2,07–2,90 s) |
| Klapprahmen-Pistole | WD-NIS n 168 → 273 | Rahmen kippt auf, linke Hand lädt von vorn oben | 1,50 / 1,75 s (schnellster Pistolenablauf) |
| Seitenwaffe mit Kastenmagazin | WD-NIS n 1202 → 1388 | senkrecht, großes Magazin unten links (vermutlich Raketen-Seitenwaffe) | 2,67 / 3,10 s |
| **Gewehr, Kastenmagazin von unten** (Grundform) | WD-NIS n 7145 → 7285; gleiche Form in fünf weiteren | Mündung steil hoch nach rechts, altes Magazin fällt, linke Hand bringt neues von unten | 2,18 / 2,33 s (Spanne 1,77–2,50) |
| Gewehr, Rundtrommel | WD-NIS n 5755 → 5956; WD-EV | Trommel unten heraus, neue von links, Waffe steil | 3,08 / 3,35 s (Zweitaufnahme 3,39) |
| Gewehr, Batterie im Seitenschacht | WD-NIS n 3946 → 4122 | senkrecht, linke Hand seitlich am Gehäuse, Ladegriff oben | 2,50 / 2,93 s |
| Pumpflinte, Einzelhülsen | WD-NIS n 2580 → 2773 | Mündung ≈ 60° hoch, Hülsen **von unten**, **Pumpen am Ende** bei steiler Waffe | Teilladung |
| Scharfschütze, Magazin unten | WD-NIS n 9176 → 9323 | Magazin unten heraus, Waffe senkrecht, neues Magazin, Kammer | 2,27 / 2,45 s |
| **MG mit Deckel und Gurt** | WD-NIS n 10268 → 10596 | Deckel klappt senkrecht hoch, Gurt eingelegt, Deckel zu, Schlag – Waffe **flach quer** | 5,20 / 5,47 s; MG mit Seitenkasten 3,88 / 4,23 |
| Fusion / Linear | WD-NIS Abschnitt 51, 52 | Mündung steil hoch, Batterie seitlich, Schlag | 2,80 / 3,63 s bis ruhig |
| Granatwerfer: Kipplauf, Revolvertrommel, Wechseltrommel, Kasten | WD-NIS n 11069 → 11257 u. a. | Kipplauf: Hülse fällt, Hand setzt von unten ein. **Schwerer Werfer mit Revolvertrommel** (6 Kammern seitlich heraus, Waffe senkrecht) – im Bestand gab es bisher nur Prospector | 2,75 / 3,13 s (Revolvertrommel); übrige 3,03–3,47 s |
| **Raketenwerfer** <a id="r-rakete"></a> | WD-NIS n 11998 → 12169 | quer, Rakete von oben (wie Bestand); zweite Form steil hoch. Koordinator: Bewegung ab n 11998/11999, ruhig ab n 12169 per Bilddifferenz bestätigt | **171 Bilder (2,85 s)**; zweite Form 3,72 s |
| Bogen | WD-NIS Abschnitt 44, 45 | kein Magazin: Bogen dreht, neuer Pfeil von rechts | 2,62 / 2,63 s |
| Glefe (Sonderform) | WD-NIS n 8066 → 8291 | Schaft hochgeworfen und gedreht, Klingenteil getauscht | 3,63 / 3,75 s (Bestand 2,28–3,07) |

**Sonderformen der Exotics** zerlegen die Waffe, werfen Teile hoch oder tauschen ganze Trommeln. Einige liegen am unteren Rand ihres Typs (1,83 und 1,92 s, unter dem Gewehr-Median 2,39) – ihre
Zeiten nicht als Typ lesen.

### 3.2 Destiny 2 – Waffenaktionen von außen

| Vorgang | Quelle, Zeit | Messung |
|---|---|---|
| **Nachladen Langwaffe von außen, Titan (Nachtrag)** [M HUD]/[O Körper] <a id="r-d2-nachladen-aussen"></a> | Bestand H-CC (`vzcGQI-O_qc`): n 218 → 279 und n 5093 → 5153 | Automatik o. ä. (Magazin 33, Kadenz am Zähler 10 Bilder je Schuss [O]): **letzter Schuss → Zähler voll 60–61 Bilder (1,0 s), zweimal** (±1; Koordinator am Zähler bestätigt). Körper [O]: Waffe **steil ≈ 65–70° links neben dem Kopf** bei n 5106–5126, also vor dem Zählersprung; die Figur läuft dabei weiter. Bestand H-CT: 72 Bilder bis voll, ≈ 78 am Körper. Teilnachladen n 838–878 [O]: Waffe zweimal steil (≈ 66° / 64°), dazwischen in Rückenlage. Perks unbekannt |
| **Nachladen Handkanone von außen, Titan (Nachtrag)** [M HUD] | MD2-AN (`eFXF-P8dtPQ`) n 587 → 679 | HUD-Symbol Trommelrevolver, Magazin 24: **letzter Schuss → voll 92 Bilder (1,53 s)**, Pause vor der Eingabe möglich; Körper klein bzw. verdeckt, nicht lesbar |
| Nachladen von außen je Typ, sonst | WD-JB, WD-MA, WD-AJ, Bestand H-CT/H-KW | **weiter nicht lesbar**. Im Bug-Video WD-MA springt der Zähler 0 → 59 in 96 Bildern, die Figur ist dabei von Fähigkeitseffekten verdeckt; bei WD-JB fällt der Zähler ohne Nachladen. Am Körper: Bestand – Langwaffe senkrecht neben dem Kopf, ≈ 78 Bilder ([aussenansicht › 3.5](aussenansicht.md#a-h-nachladen)) – und Nachtrag H-CC [O] ([steil 65–70°](#r-d2-nachladen-aussen)) |
| **Schwert von außen (Titan, Lament)** [M Winkel] <a id="r-schwert-titan"></a> | WD-JB n 2220 (gleiche Form n 1620, 1920, 2520); n 2820 | Klinge **schräg vor dem Körper ≈ 58°**, Griff rechts unten auf Bauchhöhe, Klinge über die linke Schulter; beim Laufen quer auf Hüfthöhe nach rechts |
| Primärwaffe feuern (Titan, Bug) [O] | WD-JB n 3720 | an der rechten Schulter, Oberkörper verdreht – bestätigt Bestand |
| **Vergleich Warframe: Nachladen von außen** [M] | WD-XBI n 18322 → 18442 / 18491 | Schulterkamera hinten links; Gewehr aus der Vorhalte **≈ 52–55° nach rechts oben** gekippt, Rumpf und Schultern stehen, der Kopf neigt sich zur Waffe; 2,00 / 2,82 s (Warframe-Tempo nicht unabhängig belegt) |

### 3.3 The Division 2 – Nachladen je Waffenklasse (dritte Person)

Quelle: [OrcCorp-Showcases](#q-oc), Schießstand, Basiswaffen Stufe 30, Talente unbekannt.
- **Start:** Kamera und Figur verlassen den Anschlag (±2).
- **HUD:** Reserve- oder Magazinzähler springt (±1).
- **Ende der Körperanimation:** in keinem Fall sichtbar, weil die Figur danach abdreht, weggeht oder wieder anlegt. Deshalb „bis HUD“; in Titanfall und Gears lag
  HUD 0,2–0,3 s vor „ruhig“ ([aussenansicht › 3.4](aussenansicht.md#34-feuern-nachladen-und-wechsel-von-außen--ref-033)).

| Klasse, Waffe | Quelle, Bilder | Ablauf und Haltung | bis HUD |
|---|---|---|---|
| **MP, Converted SMG-9** [M] | V-OC1 `_408-500` n 880 → 952 | MP aufrecht vor der rechten Schulter, linke Hand am Magazin; Figur dreht danach ab | **72 Bilder (1,20 s)** |
| MP, MP5-N [M] | V-OC1 `_589-683` n 932 → 1015 | schräg ≈ 60°, dann aufrecht neben dem Kopf | **83 Bilder (1,38 s)** |
| **Sturmgewehr, FAMAS 2010** [M] <a id="r-dv-famas"></a> | V-OC1 `_131-204` n 881 → 971 | Waffe steil vor der rechten Schulter, Mündung oben; Nachladen läuft beim Weggehen weiter. Koordinator: Start n 881 und Reserve 714 → 678 bei n 971 am HUD bestätigt | **90 Bilder (1,50 s)** |
| Gewehr, SOCOM M1A [M] | V-OC3 `_404-542` n 2728 → 2841 | fast senkrecht ≈ 80°, linke Hand unten am Schacht | **113 Bilder (1,88 s)** |
| **LMG mit Magazin, Classic RPK-74** [M] <a id="r-dv-rpk"></a> | V-OC2 `_0-80` n 1890 → 2007 | **senkrecht ≈ 85° rechts neben dem Kopf**, linke Hand am Schacht, zurück in den Anschlag +137. Koordinator: senkrechte Waffe n 1997 am Bild bestätigt | **117 Bilder (1,95 s)** |
| **LMG mit Gurt, Classic M60** [M] | V-OC2 `_237-305` n 1749 → 1935 | Figur dreht seitlich, **Waffe waagrecht in Hüfthöhe**, beide Hände oben am Gehäuse | **186 Bilder (3,10 s)** |
| Pumpflinte M870, Einzelpatronen [M] | V-OC2 `_376-649` n 1134–1228 | Flinte steil vor der rechten Schulter, **projiziert ≈ 45°** (n 1200, Blick von links hinten; Nachtrag: Koordinator und Richter lesen 40–45°, die 0.43-Angabe 60–70° hatte kein weiteres Bild), linke Hand lädt von unten | **28 / 36 / 29–30 Bilder je Patrone (≈ 0,5 s)** |
| **Magazin-Schrotflinte, ACS-12** (20 Schuss) [M] <a id="r-dv-acs"></a> | V-OC2 `_376-649` n 5508 → 5605 | Start ohne Pause nach dem letzten Schuss (n 5512 ±3), Waffe **steil ≈ 75°** rechts neben dem Kopf, Hände verdeckt; Fenster 55/s, Marker ±2 | **93 Bilder (1,55 s)** |
| **Magazin-Schrotflinte, Tactical SASG-12 K** (7 Schuss) [M] <a id="r-dv-sasg"></a> | V-OC2 `_376-649` n 7990 → 8112, bereit n 8137 | Lauf **fast senkrecht ≈ 85°** vor der rechten Schulter, Mündung oben; Kamera zurück im Anschlag ≈ +140. Koordinator: Reserve 74 → 67 zwischen n 8111 und 8114 bestätigt; der Kopf senkt sich deutlich erst ab ≈ n 7999 – Start daher n 7990–7999 | **113–122 Bilder (1,9–2,0 s)**, bereit 147 |
| Magazin-Schrotflinte, Black Market SASG-12 S [M] | V-OC2 `_376-649` n 9108 → 9236, bereit n 9261 | gleiche Form ≈ 85° (n 9170); Fenster 59/s | **128 Bilder (2,13 s)**, bereit 153 |
| **Röhrenflinte Super 90, Einzelpatronen** [M] <a id="r-dv-super90"></a> | V-OC2 `_376-649` n 10590–10770 | **Flinte tief vor der Hüfte, ≈ +20 bis +30°** (n 10700; Koordinator ≈ 21°, Agent 27–29°), rechte Hand am Griff. Am selben Blickwinkel steht die M870 steiler (≈ 45°) – die Röhrenflinte lädt also flacher als die Pumpflinte. Koordinator: Reserve 98 → 97 bei n 10626 bestätigt. Marine Super 90 (leer, 46/s) [O]: 8 Patronen in 215 Bildern, Mittel 28,7 | **29 / 29 / 29 / 28 Bilder je Patrone (0,48 s)** im 57/s-Fenster [M]; zwei weitere Abstände 29 / 29 im 47/s-Teil [O]; 7 Patronen ab Start 180 |
| **Präzisionsgewehr mit Magazin, SR-1** [M] | V-OC3 `_74-99` n 1310 → 1446 | Fernrohr verlassen = Start (n 1310 ±1), Gewehr **fast senkrecht ≈ 84°** vor der rechten Schulter; die SR-1 verlässt auch zwischen den Schüssen das Fernrohr – ein Repetierer mit Magazin, kein Halbautomat [O] | **136 Bilder (2,27 s)** |
| Halbautomat Paratrooper SVD [O] | V-OC3 `_13-74` n 1990–3640 | alle Schüsse im Fernrohr, nach dem letzten Schuss geht die Figur ohne Nachladen weg – **kein Nachladen von außen** in dieser Quelle | – |
| Revolver Regulus [O] | V-TB `_161-240` n 1975 → 2067; Teilnachladen n ≈ 2596–2630 | rechte Hand hebt den Revolver **steil neben den Kopf (≈ 80–90°)** – dieselbe Kippform wie die Langwaffen; 28/s | ≤ 92 Bilder ab letztem Schuss |
| Pistole Rapid 50 [O] | V-TB `_513-589` n 696 → 763 | Figur im Gegenlicht hinter Deckung, Hände nicht sichtbar; 28/s | 67 Bilder ab letztem Schuss bis voll |
| **Ziehen: Langwaffe → Pistole (TDI Kard)** [O] <a id="r-dv-ziehen"></a> | V-TB `_513-589` n 4104–4140 | Gewehr über die rechte Schulter zum Rucksack (n 4112–4114) → rechte Hand an die rechte Hüfte → **Pistole in der Hand n 4130–4132**, dann einhändig tief vor der Hüfte. Bestand V-DS ≥ 18 Bilder passt; 24–28/s | ≈ 18–20 Bilder ab Gewehr weg |
| Repetierer Model 700, Einzelpatronen [M] | V-OC3 `_13-74` n 1745–1916 | steil ≈ 70° | **43 / 43 / 37 Bilder je Patrone (0,62–0,72 s)** |
| **Repetieren mit Ausstieg aus dem Zielfernrohr** [M] <a id="r-dv-bolt"></a> | V-OC3: Model 700 n 1183–1268; M44 n 744–828, 863–946 | Schuss → Fernrohr verlassen +11 → Hand am Kammerstängel, Waffe bleibt an der Schulter → Rückkehr ins Fernrohr beginnt **+66–67 Bilder** nach dem Verlassen; drei Zyklen, zwei Waffen gleich | 66–67 Bilder (1,1 s) |
| Nachladen in niedriger Deckung [O] | V-SW n 1316–1416 (50/s, Talente) | Figur kniet hinter Sandsäcken, Waffe **tief, ≈ 30° unter der Waagrechten** – andere Form als im Stand; nur ein Beispiel | – |
| Sturmgewehr AK-M, MP P90 [O] | V-OC1 | HUD verdeckt bzw. Figur verlässt den Stand vor dem Zählersprung (P90 ≥ 74 Bilder ohne Abschluss) | – |

### 3.4 Waffenhaltung je Körperpose

**Destiny 2** (Ego aus dem Bestand, außen wo belegt; „–“ = nicht gefunden):

| Typ | Sprint (Ego, Bestand) | Rutschen / Sprung | Nachladen (Ego, neu) | Außen (Halten, Feuern, Nachladen) |
|---|---|---|---|---|
| Handkanone | Waffe senkrecht, Lauf am oberen Rand | Rutschen: ≈ 10 % nach unten rechts, geneigt (Bestand) | einhändig, Trommel links, 2,1–2,9 s | – (Bestand H-CF2, 30/s: beidhändig); Nachladen nur am HUD 92 Bilder (Nachtrag) |
| Seitenwaffe | senkrecht, ≈ 13° | – | senkrecht, Magazin unten links, 3,1 s | – |
| Automatik/Impuls/Scout/MP | Gewehr quer unten Mitte, Lauf nach links unten; Impuls fast aus dem Bild | – | Mündung steil hoch rechts, linke Hand unten, 1,8–3,4 s | Feuern und Lauf vorn an der rechten Schulter (Bestand H-CT, H-KW ≈ 32°), Nachladen senkrecht neben dem Kopf (Bestand), Tragen diagonal am Rücken |
| Schrotflinte | fast aus dem Bild | – | ≈ 60° hoch, Hülsen von unten, Pumpen am Ende | – |
| Scharfschütze | höher und mittiger, ≈ 30° links oben | Bestand unsicher | Magazin unten, senkrecht | Glitch: über dem Rücken (Bestand) |
| MG | – | – | flach quer, Deckel/Seitenkasten, 4,2–5,5 s | Lauf mit MG an der rechten Schulter; am Rücken (Bestand) |
| **Schwert** | (Stimmen: nur Quickfang mit „Ninja“-Haltung hinter dem Rücken) | **Rutschen: senkrecht rechts, unverändert** ([vorn](#r-rutschen-vorn)); **Sprung −11°, Landung +7°** ([Jäger](#r-schwertsprung)) | kein Nachladen | Stand senkrecht bzw. tief vorn-rechts (Bestand); Titan Lament ≈ 58° schräg vor dem Körper ([WD-JB](#r-schwert-titan)) |
| Super-Waffe (Arc Staff) | – | Ducken-Spam: Stab bleibt quer | – | quer ≈ 25°, links hoch |

**The Division 2** (Sturmgewehr/Gewehr, wo nicht anders genannt; Winkel zur Waagrechten, − = Mündung unten):

| Pose | Haltung | Winkel | Hände | Quelle |
|---|---|---|---|---|
| Menü / Inventar | diagonal vor der Brust | ≈ −20° | beidhändig | V-OC1 n 60, 1100 |
| Gehen (Tragen) | tief, Schaft an der Hüfte bzw. Brust | **−22 bis −45°** | rechte am Griff, linke am Handschutz | V-OC1 n 654, V-OC2 n 708, MV-DV n 60 |
| Sprint | tief vor dem Bauch | −30 bis −45° | beidhändig | Bestand V-DZ |
| Geduckter Lauf | tief zweihändig | ≈ −50° | beidhändig | [MV-TM n 6404](#r-dv-geduckt) |
| Deckung hoch (Barrikade) | schräg vor der Hüfte | −45° | rechte am Griff, linke am Handschutz | MV-TM n 5494 |
| Deckung hoch, seitlich am Pfeiler | senkrecht dicht am Körper | ≈ −90° | beidhändig | MV-TM n 6500 |
| Deckung niedrig | vor dem Oberschenkel | **≈ −35°** (Richter, Linienfit; Verlauf n 5630–5670 −25 bis −38°; Agent las −54°) | beidhändig | MV-TM n 5650 |
| Deckung niedrig, Bereitschaft (Präzisionsgewehr) | steil vor Brust und Gesicht | **≈ +70°** | beidhändig | MV-AB n 9120 |
| Vault | senkrecht in der rechten Hand | +90° [O] | rechte Hand | MV-SH n 8876 |
| Nachladen (Magazinwaffen) | steil bis senkrecht vor der rechten Schulter | **+60 bis +85°** | rechte am Griff, linke am Schacht | 3.3 |
| Nachladen Gurt-MG | waagrecht in Hüfthöhe | ≈ 0° | beide oben am Gehäuse | 3.3 |
| Nachladen Magazin-Schrot, Präzisionsgewehr mit Magazin | steil vor der rechten Schulter | **+75 bis +85°** | verdeckt | [3.3](#r-dv-sasg) |
| Nachladen Röhrenflinte (Super 90) | tief vor der Hüfte | **≈ +20 bis +30°** | rechte am Griff | [3.3](#r-dv-super90) |
| Nachladen Revolver | steil neben dem Kopf, einhändig | ≈ +80 bis +90° [O] | rechte Hand | 3.3 |
| Pistole mit Ballistikschild | gestreckter rechter Arm auf Augenhöhe | ≈ 0° [O] | einhändig (Schild links) | V-TB n 1440 |
| Gehen mit gezogenem Revolver | hängend an der rechten Hüfte | ≈ −90° [O] | rechte Hand | V-TB n 1200 |
| Nachladen in niedriger Deckung | tief, kniend | ≈ −30° [O] | – | V-SW |
| Zielen im Laufen | angelegt | −15 bis −20° | beidhändig | Bestand V-DZ |
| Rolle, Sprung, Fall, Hochziehen | **keine Waffe in der Hand**, Waffen am Rucksack | – | Hände stützen, Arme seitlich | MV-AB |
| Emote | Waffen am Rucksack | – | frei | MV-SB |
| Pistole im Menü | senkrecht hängend rechts | −90° | rechte Hand an der Hüfte | MV-NB n 30960 |

Je Klasse fehlen die meisten Posen (LMG, Schrot, MP, Pistole in Deckung, Lauf oder Vault): Die Schießstand-Showcases zeigen nur den Stand, die
Bewegungsquellen meist ein Gewehr.

### 3.5 Muster (Beobachtung)

1. **Nachladen von außen ist in beiden Spielen ein Arm- und Waffenvorgang mit großer Kippbewegung.** In Division steht die Magazinwaffe steil bis senkrecht
   vor der rechten Schulter – bei MP, Sturmgewehr, Gewehr und Magazin-LMG dieselbe Form. Bei Destiny (Bestand) steht die Langwaffe senkrecht neben dem
   Kopf; Warframe kippt ≈ 52–55° nach außen-oben, der Rumpf bleibt stehen.
2. **Division unterscheidet die Klasse über die Dauer, Destiny über die Bauform.** In Division: MP 72–83 < Sturmgewehr 90 < Gewehr 113 < Magazin-LMG 117 <
   Gurt-LMG 186 Bilder bis HUD; Magazin-Schrot 93–128, SR-1 136 (Nachtrag). Destiny zeigt im Ego je Bauform einen eigenen Ablauf (Revolver, Trommel, Deckel, von oben), die Dauern überlappen stark.
   Ausnahmen in beiden Spielen: Gurt-MG flach statt steil und am längsten; in Division lädt auch die Röhrenflinte Super 90 tief (+20 bis +30°).
3. **Ruhe unten, Bereitschaft oben (Division).** Die Mündung zeigt in Ruhe, Deckung und geduckt nach unten (Tragen −20 bis −45°, Deckung −35 bis −45°,
   geduckter Lauf −50°, seitlich am Pfeiler senkrecht), in Bereitschaft nach oben (+70°, ein Beispiel; Vault +90° [O]). Akrobatik geschieht mit freien Händen; die Waffen bleiben am Rucksack sichtbar.
4. **Destiny-Schwert bleibt in der Hand.** Beim Rutschen steht es unverändert senkrecht, beim Sprung tief rechts-hinten, bei der Landung waagrecht. Mit
   Feuerwaffen sind Sprint, Rutschen und Sprung von außen nicht belegt – in Bug-Aufnahmen ist die aktive Waffe beim Laufen oft nicht zu sehen (Bestand 0.42).

## 4. Bewertung: gut, nicht so gut, für wen

**Quellen:**
- **Spielerstimmen:** 37 Reddit-Beiträge, je mit Datum, Punktzahl, Zustimmungsanteil und Top-Kommentaren über das Archiv Arctic Shift geprüft. Punktzahlen
  sind Archivstand. Reddit selbst lud per curl nicht (403).
- **Fach- und Entwicklerquellen:** 9; zwei davon nur Suchauszug.
- **Kürzel:** sind die Reddit-IDs, Liste in [4.1](#41-quellen-der-bewertung).
- **Nicht wiederholt:** die Quellen P/Q/B/W aus [aussenansicht › 5.1](aussenansicht.md#51-quellen-der-bewertung). Eigene Einschätzungen sind als solche markiert.

| Spiel | Gegenstand | Gut (warum) | Nicht so gut (warum) | Für wen | Spielerstimmen | Entwickler/Fach |
|---|---|---|---|---|---|---|
| **Destiny 2** | Figur von außen (Turm, Menü) | Animationen „so gut wie in Ego“ (10awbks, 209 P.); Fähigkeiten in dritter Person als Wunsch (zsx06x, 548 P.) | Umhang klebt an den Schulterblättern, Roben durchdringen den Boden (10awbks); Warlock-Menüstand „schwebt“, D1-Stand gewünscht (jqibag, 255 P.); Haltung wählbar gewünscht (oi1chw, 1058 P.) | Mode-Spieler, Warlock-Spieler (geteilt) | wiederkehrend; Gegenstimme „Schwebestand einzigartig“ | K1 (nur Ego) |
| Destiny 2 | Super- und Fähigkeitsanimationen | [Einschätzung] klare, kurze Ansage (≈ 0,6 s, Kamera weicht zurück) | Rift-/Barrikaden-Wirkanimation „unerträglich langsam“ (ka3wqt, 291 P.); Super sperrt Momentum (cetman, klein) | PvE, PvP | wiederkehrend; Gegenstimme Balance | – |
| Destiny 2 | Emote „Power Rising“ | – | soll in der Ladehaltung schleifen (i8aljs, 2244 P., 97 %) | Käufer | Einzel, hoch bewertet | K2: Community-Antwort „keine Versprechen“; Änderung nicht gefunden |
| Destiny 2 | Schwerthaltung im Sprint | Quickfang-„Ninja“-Haltung beliebt (75j3e2) | Ergo Sum ohne die Leichtrahmen-Haltung (1dc7yeo, 102 P.; 1d8rsqv) | Schwertspieler | wiederkehrend | Änderung nicht gefunden |
| Destiny 2 | Nachladeanimationen | Exotics mit eigener Animation beliebt (13v34pk, 483 P.; qeluma; ac5qm9) | wenige Rigs für Legendaries, Schrot immer Einzelpatrone (gu5age, 112 P.; zfv8zm, 214 P., 81 %; 8tzlt5, 406 P.) | Waffenliebhaber | wiederkehrend 2018 → 2022 | K4 (TWAB 21.05.2020: Reload-Stat setzt die Animationsgeschwindigkeit je Archetyp) |
| Destiny 2 | Nachladen in dritter Person | – | Quicksilver Storm zeigte in dritter Person die Sonder-Nachladeanimation auch beim normalen Nachladen | – | Einzel (Bug) | **K5: behoben 28.11.2023** – belegt, dass Destiny eigene Nachladeanimationen für die Außenansicht hat |
| **The Division 2** | Sprint und Laufen von außen | „schwer und realistisch“ (9z5180, Kommentar); „beste Charakteranimationen“, Rutschen über die Motorhaube in Deckung gelobt (15q4nv4, 69 P.) | „Windel-Watscheln“ (9z5180, 93 P.; cv91pu, 164 P.; apgcxl), 45°-Neigung (aom0ce, 0 P.); seit 2023 Sprint → Stopp ohne Überblenden (11s4686, 42 P.), 2024 nach Spielerangabe unverändert (1bzstxx) | Realismus-Spieler (gespalten) | wiederkehrend seit der Vorabversion 2018 | – (kein Entwicklerzitat gefunden) |
| The Division 2 | Deckung, Klettern, Wiederbeleben | [Einschätzung] Höhenstufen klar lesbar (1,0 / 0,64 KH); Deckungs-Tipps gelobt (15tbpwv, 114 P.) | Animationssperre nach dem Klettern (1twefo9, 37 P., 2026); Hänger beim Wiederbeleben | Alle | wiederkehrend | K7 (TU4: Bewegung um runde Deckung), K8 (TU7: Wiederbeleben-Hänger behoben) |
| The Division 2 | Nachladen | Nachladeanimation „außerordentlich schön“ (15q4nv4, Kommentar); [Einschätzung] Klasse an der Dauer lesbar | Nachladen blockiert Aufheben und Wiederbeleben (b3x5y4); RPK mit fremder Nachladeanimation (gz8w2v); Verzögerung mit Schild (j70h8n) | PvP, Waffenkenner | wiederkehrend | **K6 (TU6, 16.09.2019): M60 durchdrang die Figur beim Nachladen, behoben**; K7 (Schild-Nachladen mit falscher Animation, behoben) |
| The Division 2 | Waffenhaltung im Sprint | „Himmelwärts“-Haltung mit Mündung oben beliebt (1c6fwcc, Kommentar) | SMG-Sprint: drei Haltungen „ohne Logik“, SMG-9 wie Pistole (1c6fwcc); Zwei-Hand-Wunsch schon in Division 1 (7ky957, D1) | MP-Spieler | wiederkehrend D1 2017 → D2 2024 | – |

**E2 – Lehren für Critic, BALLON und Cube Escape (Vorschlag, dort entscheiden)**

- **Übernehmen:**
  - **Eine** steile Nachladeform für alle Magazinwaffen (Waffe senkrecht neben dem Kopf). Die Klasse zeigt sich über die Dauer (Division 72–186 Bilder) und
    eine Ausnahme für Gurtwaffen. Einschätzung: von oben in der Isometrie lesbar ([3.3](#33-the-division-2--nachladen-je-waffenklasse-dritte-person)).
  - Waffe in Ruhe mit der Mündung nach unten (Division −20 bis −50°), in Bereitschaft nach oben ([3.4](#34-waffenhaltung-je-körperpose)).
  - Fähigkeiten mit kurzer Ansage von ≈ 0,6 s ([Super](#r-super)).
- **Übernehmen oder testen:** Hocke als Höhenstufe von ≈ 0,64 KH ([Division](#r-dv-deckung)) bzw. ≤ 0,68 KH ([Destiny](#r-sentinel), Bezug Ausfallschritt). Ob der Roboter frei ducken darf oder
  nur an Deckung (Division), entscheidet Cube Escape.
- **Testen:**
  - Akrobatik (Rolle, Sprung, Klettern) mit freien Händen und der Waffe am Rücken (Division) gegen Waffe in der Hand (Destiny-Schwert).
  - Rolle 18–28 Bilder bis zum Boden und Landung mit Hocke +18 bzw. Rolle +48 als Startwerte.
- **Vermeiden:**
  - Stopp ohne Überblenden: Division-Spieler kritisieren ihn seit 2023.
  - Waffenhaltungen ohne erkennbare Regel je Waffe, z. B. SMG-Sprint in Division.
  - Gurtwaffen, die beim Nachladen den Körper durchdringen (Division TU6).

### 4.1 Quellen der Bewertung

**Spieler** (alle `https://www.reddit.com/r/<Sub>/comments/<id>/`, geprüft über Arctic Shift am 27.11.2026; Datum in UTC)

| Spiel und Thema | Beiträge (Datum) |
|---|---|
| Destiny 2, Bewegung und Posen | [10awbks](https://www.reddit.com/r/DestinyTheGame/comments/10awbks/) (13.01.2023) · [zsx06x](https://www.reddit.com/r/DestinyTheGame/comments/zsx06x/) (22.12.2022) · [oi1chw](https://www.reddit.com/r/DestinyTheGame/comments/oi1chw/) (11.07.2021) · [jqibag](https://www.reddit.com/r/DestinyTheGame/comments/jqibag/) (08.11.2020) · [i8aljs](https://www.reddit.com/r/DestinyTheGame/comments/i8aljs/) (12.08.2020) · [9br2ip](https://www.reddit.com/r/DestinyTheGame/comments/9br2ip/) (31.08.2018) · [cetman](https://www.reddit.com/r/DestinyTheGame/comments/cetman/) (18.07.2019) · [ka3wqt](https://www.reddit.com/r/DestinyTheGame/comments/ka3wqt/) (09.12.2020) · [1dc7yeo](https://www.reddit.com/r/DestinyTheGame/comments/1dc7yeo/) (09.06.2024) · [1d8rsqv](https://www.reddit.com/r/DestinyTheGame/comments/1d8rsqv/) (05.06.2024) · [75j3e2](https://www.reddit.com/r/DestinyTheGame/comments/75j3e2/) (10.10.2017) |
| Destiny 2, Nachladen | [13v34pk](https://www.reddit.com/r/DestinyTheGame/comments/13v34pk/) (29.05.2023) · [qeluma](https://www.reddit.com/r/DestinyTheGame/comments/qeluma/) (24.10.2021) · [gu5age](https://www.reddit.com/r/DestinyTheGame/comments/gu5age/) (31.05.2020) · [ac5qm9](https://www.reddit.com/r/DestinyTheGame/comments/ac5qm9/) (03.01.2019) · [zfv8zm](https://www.reddit.com/r/DestinyTheGame/comments/zfv8zm/) (08.12.2022) · [15ye6g5](https://www.reddit.com/r/DestinyTheGame/comments/15ye6g5/) (22.08.2023) · [dovdjy](https://www.reddit.com/r/DestinyTheGame/comments/dovdjy/) (29.10.2019) · [8tzlt5](https://www.reddit.com/r/DestinyTheGame/comments/8tzlt5/) (26.06.2018) · [a3wqw7](https://www.reddit.com/r/DestinyTheGame/comments/a3wqw7/) (07.12.2018) |
| The Division 2, Bewegung | [9z5180](https://www.reddit.com/r/thedivision/comments/9z5180/) (21.11.2018) · [15q4nv4](https://www.reddit.com/r/thedivision/comments/15q4nv4/) (13.08.2023) · [cv91pu](https://www.reddit.com/r/thedivision/comments/cv91pu/) (25.08.2019) · [apgcxl](https://www.reddit.com/r/thedivision/comments/apgcxl/) (11.02.2019) · [aom0ce](https://www.reddit.com/r/thedivision/comments/aom0ce/) (08.02.2019) · [11s4686](https://www.reddit.com/r/thedivision/comments/11s4686/) (15.03.2023) · [1bzstxx](https://www.reddit.com/r/thedivision/comments/1bzstxx/) (09.04.2024) · [1twefo9](https://www.reddit.com/r/thedivision/comments/1twefo9/) (04.06.2026) · [15tbpwv](https://www.reddit.com/r/thedivision/comments/15tbpwv/) (17.08.2023) |
| The Division 2, Nachladen und Haltung | [b3x5y4](https://www.reddit.com/r/thedivision/comments/b3x5y4/) (21.03.2019) · [b6ymr8](https://www.reddit.com/r/thedivision/comments/b6ymr8/) (29.03.2019) · [b7sr8n](https://www.reddit.com/r/thedivision/comments/b7sr8n/) (31.03.2019) · [j70h8n](https://www.reddit.com/r/thedivision/comments/j70h8n/) (07.10.2020) · [gz8w2v](https://www.reddit.com/r/thedivision/comments/gz8w2v/) (08.06.2020) · [lhq3a4](https://www.reddit.com/r/thedivision/comments/lhq3a4/) (11.02.2021) · [1c6fwcc](https://www.reddit.com/r/thedivision/comments/1c6fwcc/) (17.04.2024) · [7ky957](https://www.reddit.com/r/thedivision/comments/7ky957/) (20.12.2017, **Division 1**) |

**Fach und Entwickler**

| Kürzel | Quelle | Inhalt |
|---|---|---|
| K1 | [GDC 2015, Helsby (Bungie): The Art of First Person Animation for Destiny](https://www.gdcvault.com/play/1022297/The-Art-of-First-Person) | nur Ego |
| K2 | [Community-Antwort zu Power Rising](https://devtrackers.gg/destiny2/p/45fcdace-bungie-please-change-the-power-rising-super-saiyan-emote-to-loop-in-its-charge-up-stance-until-user-input-cancels) | Zuordnung zu Bungie nur über PCGamesN (Bestand W10) |
| K3 | TheGamer zu 3-Peeking | 404, Suchauszug; Inhalt im Bestand W4/W10 |
| K4 | [This Week At Bungie 21.05.2020](https://devtrackers.gg/destiny2/p/6806283e-this-week-at-bungie-5-21-2020) | Reload-Stat und Animationsgeschwindigkeit je Archetyp |
| K5 | [Update 7.3.0, 28.11.2023 (ComicBook)](https://comicbook.com/gaming/news/destiny-2-season-of-the-wish-d2-update-patch-notes/) | Quicksilver-Storm-Fix in dritter Person |
| K6 | [Division 2 TU6, 16.09.2019 (MP1st)](https://mp1st.com/news/division-2-title-update-6-patch-notes-revealed-ahead-release) | M60 durchdrang die Figur beim Nachladen; falsche Animation beim Zielen an der Wand |
| K7 | [Division 2 TU4 (Newsweek)](https://www.newsweek.com/division-2-update-109-title-4-gunner-gunslinger-patch-notes-exotic-1444454) | Schild-Nachladen mit falscher Animation; Bewegung um runde Deckung |
| K8 | [Division 2 TU7](https://devtrackers.gg/the-division/p/96a85f97-title-update-7-episode-3-patch-notes) | Hänger beim Wiederbeleben |
| K9 | Division 2 TU 18.2 (dsogaming) | 403, Suchauszug |

Die vollständige Liste mit Punkten, Zustimmung und Gegenstimmen steht in `data/repertoire.json` › `player_voices`, `dev_sources`.

## 5. Offen und nicht messbar

Mit Grund – nicht mit denselben Quellen wiederholen:

- **Destiny 2, Grundbewegungen von außen:**
  - **Was fehlt:** echtes Ducken, geduckt Gehen, Übergang Stand ↔ Hocke, Sprungarten je Klasse ohne Schwert (Lift, Gleiten, Dreifachsprung),
    Hochziehen an Kanten, Jäger-Ausweichen und Sprinthaltung.
  - **Warum:** In 21 geprüften Quellen und in H-KW 880–1440 s findet sich keine Aufnahme bei echten 60/s mit stehender Vergleichsfigur. Nachtrag: H-CC ganz durchgesehen
    (keiner dieser Zustände), MD2-AN grob; die einzige Hocke von außen ist ein Gegner in der Todeskamera ohne festen Maßstab.
  - **Weg:** Sicht eines zweiten Spielers (Crucible-Clips mit Ducken von vorn, Twitch), Beta-Vergleiche nur für Form (`wXqpcJXcK_k`, `5JTOhdfcC_c`, 30/s)
    oder eigener Mitschnitt.
- **Destiny 2, Nachladen von außen je Typ:** Schrot, Scharfschütze und Raketenwerfer sind von außen nicht gefunden; die Handkanone nur am HUD (92 Bilder, Nachtrag), der Körper nicht lesbar. Die Bug-Videos zeigen den Vorgang
  verdeckt oder zu klein, Suchen nach „both viewpoints“ treffen Destiny 1 oder 30/s. Dass es eigene Außenanimationen gibt, belegt K5.
- **Destiny 2, Untertypen im Nachladekatalog** (Automatik/Impuls/Scout/MP, Handkanone/Seitenwaffe): Das Video blendet keine Namen ein. Weg: Ultraclocked-Einzelshowcases
  mit Menübild.
- **Destiny 2, Waffenhaltung im Rutschen und Sprung je Typ (Ego):** Showcases bewegen sich nicht.
- **The Division 2, Pistole/Revolver:** Der Nachtrag lud `hiIqzpBSMvk`, doch die Quelle hat nur 24–28 echte Bilder/s – Nachladen, Ziehen (≈ 18–20 Bilder) und
  Revolverhaltung sind nur [O]; Wegstecken der Pistole nicht sichtbar. Weg: Seitenwaffen-Showcase mit echten 60/s.
- **The Division 2, Ende der Körperanimation beim Nachladen:** in allen Showcases verdeckt. Halbautomatisches Präzisionsgewehr: die SVD wird im Showcase
  nicht nachgeladen, die SR-1 ist ein Repetierer – ein Halbautomat von außen fehlt weiter.
- **The Division 2, Nachladen in hoher Deckung, links/rechts, im Laufen, Sprint, Vault oder Rolle je Klasse:** nicht gefunden (Schießstand). Ob sich der Ablauf in Deckung
  ändert, zeigt nur ein Beispiel mit Talenten (V-SW, 50/s).
- **The Division 2, weitere Bewegungen:**
  - **Nur 30/s-Clips:** Leiter, Abseilen, Kriechen, Dauer des Wiederbelebens.
  - **Nicht bildgenau gefunden:** Granate/Fähigkeit, Blindfeuer, Hervorkommen zum Zielen.
  - **Nur ≤ 35/s:** Schulterwechsel, Emotes.
  - **Nicht trennbar:** Sprint gegen Laufen (keine Eingabeanzeige).
  - **Kein Weltmaßstab:** Strecken in KH (Rolle, Deckung zu Deckung).
- **Normaltempo:** belegt für WD-NIS. Für MD-AB, MD-SW, die Division-Showcases und Warframe ist es nicht über eine Uhr belegt; kein Zeitlupenhinweis.
- **Freies Ducken in Division als Spielregel:** nur beobachtet, keine Entwickler- oder Wikiquelle.

## 6. Prüfung und Zählung

- **Unteragenten:** fünf, wie in [1](#1-quellen-und-methode); keiner schrieb ins Repo oder lud selbst.
- **Nachmessung durch den Koordinator: 11 Stellen, 10 bestätigt, 1 teilweise** (eigene Einzelbilder bzw. Bilddifferenz):
  - Sentinel-Hocke 0,66–0,69 gegen 0,68 KH;
  - Super-Wechsel Sentinel n 18856/18892;
  - Jäger-Schwertsprung n 7520/7524/7589/7597;
  - Rutschen von vorn n 194;
  - Revolver n 622/652/757/770;
  - Raketenwerfer 171 Bilder per Bilddifferenz;
  - FAMAS Start n 881 und Reserve 714 → 678 bei n 971;
  - RPK senkrecht n 1997;
  - Division-Deckungshöhen n 5494/5650 (eigene Lesung 0,63);
  - Rolle n 3117/3145/3165;
  - **teilweise:** Sparrow-Absteigen – Fuß am Boden bei n 8780 nicht sicher.
- **Quellen:**
  - Die Agenten prüften Kanal, Datum und Titel aller Videos per yt-dlp vor der Sperre.
  - Der Koordinator prüfte 5 IDs (`nis07-5BXuo`, `VzjtHWEFrNw`, `-CqNxaKFcD8`, `RMLZqmCW4q4`, `g0iFqDZC_Qw`) per oEmbed: Kanal und Titel passen.
  - Fach- und Spielerquellen selbst nachgeladen: K5 mit Fix-Text, K6 mit M60-Text; **alle 37 Reddit-IDs** über Arctic Shift (Sub, Titel, Datum,
    Punkte) – drei Daten um einen Tag auf UTC korrigiert.
- **Übernommen und nicht übernommen:**
  - **Übernommen:** die Mess- und Sichtzeilen der vier Messagenten (MD 33, MV 26, WD 63 Katalogabschnitte, 17 Phasen- und 7 Außenzeilen, WV 22) und
    37 Spieler- sowie 9 Fachquellen.
  - **Korrigiert:**
    - Die Kürzel R1–R39 des Rechercheagenten waren zwischen Tabelle und Liste verschoben; hier stehen die Reddit-IDs.
    - Die Sentinel-Vergleichspose ist ein Ausfallschritt; die Hocke steht als ≤ 0,68 KH.
    - Nach dem Richter (Runde 1): Gewehrwinkel in niedriger Deckung −54° → ≈ −35° (Linienfit am Einzelbild), Ruhe-Spanne neu gefasst; 63 statt 64 Abschnitte,
      59 statt 57 mit Dauer; Normaltempo vierfach statt fünffach; Abgleich mit dem Bestand und Sonderformen umformuliert; Zählung der Stellen; Exotic-Reihen in › 1; Eintrag für V-OC3 in `clips.json`.
  - **Nicht übernommen:**
    - Zeiten aus Quellen unter ≈ 50 echten Bildern/s, nur als Form geführt.
    - Die Warframe-Mediane aus der automatischen Segmentierung, nur [O] im JSON.
    - Die Deutung „weiche gegen harte Landung“ beim Mauersprung, nur als Beobachtung geführt.
- **Zählung:**
  - 2 Spiele, Warframe als Vergleich.
  - 43 Video-IDs eingereiht (42 geladen, 1 gescheitert), dazu weitere nur per Metadaten geprüft. Gemessen bzw. ausgewertet je Agent:
    MD 9, MV 6, WD 8, WV 4 (einzelne Videos bei zwei Agenten).
  - `data/repertoire.json` › `examples`: 149 Einträge = 63 Katalogabschnitte des Nachladevideos, 8 Phasenzeilen zu Katalogabschnitten derselben Aufnahme
    (Feld `same_segment`), 57 weitere Mess- und Sichtzeilen und 21 aus dem Nachtrag (Feld `agent` „wv2/md2 (Nachtrag 28.11.2026)“).
  - 37 Spieler- und 9 Fachquellen.
  - ≈ 20 eigene Prüfbilder des Koordinators.
- **Nachtrag 28.11.2026:**
  - **Nachmessung des Koordinators: 8 Stellen, 6 bestätigt, 2 verworfen.**
  - **Bestätigt:**
    - Tactical SASG-12 K: Reserve 74 → 67 zwischen n 8111 und 8114. Der Start ist unscharf (n 7990–7999), daher steht 113–122.
    - Super 90: Reserve 98 → 97 bei n 10626.
    - Haltung M870 gegen Super 90 am selben Blickwinkel: ≈ 45° gegen ≈ 21°.
    - Destiny-Zähler 1 → 0 → 33 bei n 218/279 und 5093/5153: 60–61 statt 61–62 Bilder.
    - Steile Waffe neben dem Kopf bei n 5116.
    - Kapitel-Übersicht des Schrot-Abschnitts: 8 Bilder.
  - **Verworfen:**
    - „Tragehaltung −42°“: Das ist die Rückenwaffe des Bestands.
    - Fall ≈ 50 Bilder: Bei n 3468–3482 ist die Figur noch in der Luft.
  - **Klasse:** In H-CC laut Bestand Titan, nicht Warlock.
  - **Nicht übernommen:** Lauf-Takt (2 Zyklen, Bestand hat 4), Lanzensprung (unklar) und Feuerhaltung +32 bis +38° (bestätigt nur den Bestand H-KW ≈ 32°).
  - **Quellen:** 10 Ladungen (7 Videos, davon `vzcGQI-O_qc` Bestand H-CC, und 3 Abschnitte), 26 IDs per Metadaten geprüft. Die Kanäle stammen aus `info:` des Laders, also yt-dlp nach der Sperre.
