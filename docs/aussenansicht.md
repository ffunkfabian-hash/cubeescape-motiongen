# Außenansicht – Körperbewegung und Waffe am Körper

Referenzanalyse REF 0.32 „Spectator“ (30.10.2026) für **Critic** (Roboter-Ganzkörper in three.js), **BALLON** (Waffe am Körper von außen) und
später **Cube Escape** (Isometrie-Kamera zeigt den eigenen Roboter). Zwei Hauptziele: **(1) Körperbewegung von außen** – Stand/Atmen, Gehen,
Laufen, Sprint, Start/Stopp, Drehen, Richtungswechsel, Ducken, Sprung/Landung, Fallen, leicht gegen schwer; **(2) Waffe am Körper von außen** –
Tragehaltung je Klasse, Hüfte gegen Zielen (Aim-Offset), Feuern, Nachladen, Wechsel, Holster, Lesbarkeit auf Distanz und die Handgröße außen
gegen Ego ([Frage F5](design-figuren.md#frage-f5)). Hier stehen Beobachtungen und Zahlen; entschieden wird in Critic, BALLON und Cube Escape.
Maschinenlesbar: [`data/aussenansicht.json`](../data/aussenansicht.json). Bestand, auf dem diese Version aufbaut: die Schwert-Schulteransicht
in [nahkampf.md › 4](nahkampf.md#4-destiny-schwert-in-der-schulteransicht) (bisher die einzige Messung in dritter Person, hier nicht
wiederholt), [design-figuren.md](design-figuren.md) (F-R9, F-R11, Frage F5) und [design-ausruestung.md](design-ausruestung.md#2-quellen).

**Status:** **[M]** am eigenen Einzelbild gemessen (60/s-Bild mit 5- oder 10-%-Raster, Vorlagensuche NCC); **[O]** Sichtung ohne belastbare
Zahl; **[C]** Spielerstimme oder Zuarbeit, nicht vollständig nachgeprüft; **[S]** Sekundär-/Fachquelle; **[B]** Entwickler. **Jede Zahl ist
das Beispiel einer Figur in einer Aufnahme** mit unbekanntem FOV, Perks und Eingabe – kein Klassenmittel. Strecken in **Körperhöhen (KH)**
der stehenden Figur am selben Bild; Bildlagen in % B/H (Ursprung oben links, 50/50 = Bildmitte).

**Kurzbefund.** Ziel 2 ist in vier Spielen belegt (Holster, Tragehaltung, Figurgröße in der Kamera, Handgröße außen), Ziel 1 nur
lückenhaft: Gehtakt (Warframe), Atmen und Leerlauf (Warframe, Titanfall 2), Titanfall-Aufsatz, Einstieg in den Titan und eine Wende mit
Anschlag (Division 2) sind gemessen; **Schrittfrequenz nach der 4-Zyklen-Regel, Schrittlänge, Hub im Gehen, Sprint, Sprung und Fallen sind
für kein Spiel belegt** – YouTube war in dieser Cloud-Sitzung nach 20 Minuten gesperrt, die Twitch-Clips zeigen Figuren fast nie
lange genug quer zur Kamera ([7](#7-offen-und-nicht-messbar)). Destiny 2 zeigt die eigene Figur im Kampf nicht von außen – nur im sozialen
Raum, im Emote, im Super, mit Schwert und beim Tragen von Gegenständen.

## 1. Quellen und Methode

- **Videos [M]:** Twitch-Clips (1080p/900p, echte 60/s – Doppelbilder per Bilddifferenz geprüft), ganz geladen; **Clipzeit = Originalzeit**,
  Bildindex f bzw. n = Zeit × 60 (59,94 bei T2). Jede Quelle per `yt-dlp --print "%(channel)s|%(upload_date)s|%(title)s"` am 30.10.2026
  geprüft; Kanal (Broadcaster) und Clip-Ersteller getrennt. Einzelbilder bildgenau (`select=eq(n,N)`), 5- oder 10-%-Raster mit Mittenkreuz;
  Bögen nur zum Finden. Marker ±1 Bild, Differenzen ±2 Bilder, Lagen ±3 pp, Längen in px ±8–15 px.
- **Körperhöhe KH** = Scheitel bis Sohle der stehenden Figur im selben Bild; wo die Sohle unter dem Bildrand liegt, ist KH eine Untergrenze.
  Längen von Waffen und Händen sind **projiziert** (3/4-Blick verkürzt) – Verhältnisse nur als Größenordnung.
- **Takt:** Gehen über einen festen Bildmarker der Figur (Farbmaske oder feste Vorlage, NCC ≥ 0,85); ein Arm- = ein Gangzyklus (zwei
  Schritte), Frequenz nur aus ≥ 4 aufeinanderfolgenden Zyklen ([Methode 21](destiny2.md#methode-21)), sonst „vorläufig“. Atmen/Leerlauf über
  eine feste Brust-/Helmvorlage bei fester Kamera (Bodenvorlage als Gegenprobe).
- **Normaltempo:** alle Quellen sind Live-Mitschnitte (Stream, Devstream, Lobby) ohne Zeitlupenhinweis; in T2 zusätzlich über die HUD-Spieluhr
  belegt (Sprung alle 60 Bilder). Keine Zeitlupe in diesem Doc; die Schwertzeiten aus [nahkampf.md › 4](nahkampf.md#4-destiny-schwert-in-der-schulteransicht)
  bleiben Medienzeit.
- **Streambilder mit verkleinertem Spielfenster** (Warframe-Devstreams: Spielfenster 19–97 % B × 6–83 % H): % H beziehen sich aufs Streambild,
  übernommen werden nur Verhältnisse in KH.
- **YouTube:** zu Sitzungsbeginn (12:14) luden Metadaten, Formate und ein Testausschnitt in diesem Cloud-Container (yt-dlp mit Node als
  JS-Laufzeit); ab etwa 12:20–12:35 meldete YouTube Bot-Prüfung bzw. HTTP 403 für alle Abrufe. Umgehungen (andere Player-Clients, Cookies)
  wurden nicht weiter verfolgt. 36 YouTube-Kandidaten mit geprüften Metadaten stehen in [7](#7-offen-und-nicht-messbar) für eine Folgesitzung.
- **Unteragenten:** vier Messagenten (Destiny 2, Titanfall 2, Warframe, Division 2/Gears 5) und ein Rechercheagent (Spielerstimmen,
  Fachquellen), je eigener Arbeitsordner; Koordinator-Stichprobe in [8](#8-prüfung-und-zählung).

| Kürzel | Quelle | Kanal (Clip-Ersteller) | Datum | Bild | hier |
|---|---|---|---|---|---|
| <a id="a-q-datto"></a>**D-DA** | [Twitch `SpookyCovertPoxJKanStyle`](https://www.twitch.tv/datto/clip/SpookyCovertPoxJKanStyle) „Datto's thoughts on Tower event“ | Datto (iamwat_) | 06.06.2020 | 1920 × 1080, 60/s | Turm: eigene Figur mit schwerer Waffe, andere Hüter in fünf Abständen |
| <a id="a-q-teawrex"></a>**D-TW** | [Twitch `AmusedJollyKuduHoneyBadger`](https://www.twitch.tv/teawrex/clip/AmusedJollyKuduHoneyBadger-sAmR78fXAZd_9zsr) | Teawrex (Basandra) | 01.12.2021 | 1920 × 1080, 60/s | Hangar: Emote mit Waffe auf dem Rücken, zwei Hüter |
| <a id="a-q-ehroar"></a>**D-EH** | [Twitch `InventiveCuriousLemurNerfBlueBlaster`](https://twitch.tv/ehroar/clip/InventiveCuriousLemurNerfBlueBlaster) „Pro Gamer Build“ | Ehroar (magicman457) | 06.02.2020 | 1600 × 900, 60/s | Charakterbild mit Scharfschützengewehr (Hand), Ego derselben Waffe, Schwert-Lauf |
| **D-SW** | [Twitch `ThankfulCourteousGazellePanicBasket`](https://www.twitch.tv/sweatcicle/clip/ThankfulCourteousGazellePanicBasket) | Sweatcicle (iamburgie24) | 12.12.2020 | 1920 × 1080, 60/s | anderer Hüter mit Langwaffe (Arena) |
| D-SW1, D-MA1 | [`WittyColdbloodedDootKeepo`](https://twitch.tv/sweatcicle/clip/WittyColdbloodedDootKeepo), [`NastyTolerantLettuceDoubleRainbow`](https://twitch.tv/mactics/clip/NastyTolerantLettuceDoubleRainbow-l5T5zCw4kfvBWORM) | Sweatcicle, Mactics | 20.11.2020, 20.04.2024 | 60/s | Start Gehen (0,6 s), Batterie tragen (≤ 1,5 s) – [O] |
| <a id="a-q-cdawg"></a>**T1** | [Twitch `DoubtfulMushyPlumHassanChop`](https://clips.twitch.tv/DoubtfulMushyPlumHassanChop-p1Qs91lrN9CV1HB5) | CDawg (rustin13) | 14.09.2025 | 1920 × 1080, 60/s | Lobby: Pilot mit Gewehr, Leerlauf, Hand |
| <a id="a-q-pato"></a>**T2** | [Twitch `FamousFaintChickpeaMVGame`](https://clips.twitch.tv/FamousFaintChickpeaMVGame-7MC1YQEz0gMmtZFc) „despliegue de titan“ | patofiestahd | 23.10.2026 | 1920 × 1080, 59,94/s | Titanfall-Abwurf, Einstieg in dritter Person, HUD-Uhr |
| **T3** | [Twitch `TacitSpoopyBaboonTF2John`](https://clips.twitch.tv/TacitSpoopyBaboonTF2John-i8CDQvlZx5Fo8R3Y) | LIRIK (MrChuckleTeeth) | 09.09.2023 | 1920 × 1080, 60/s | BT-7274 steht und gestikuliert (Kampagne) |
| T4, T5 | [`TrappedShinyPrariedogAllenHuhu`](https://clips.twitch.tv/TrappedShinyPrariedogAllenHuhu-BqCC13iVq5e17q0Z), [`SuaveEagerToadNomNom`](https://clips.twitch.tv/SuaveEagerToadNomNom-swZhQsGXVoTfFf2I) | WoolieVersus | 22.09.2023 | 60/s | Legion mit Kanone, Titan-Exekution – [O] |
| <a id="a-q-travission"></a>**W-TR** | [Twitch `EnthusiasticAgileBunnyBudStar`](https://clips.twitch.tv/EnthusiasticAgileBunnyBudStar) „Walking Animation“ | Warframe (Travission) | 01.03.2019 | 1920 × 1080, 60/s | Gehen (Armschwung als Takt) |
| <a id="a-q-rhino"></a>**W-RH** | [Twitch `DullFurtiveShrimpCoolCat`](https://clips.twitch.tv/DullFurtiveShrimpCoolCat-Ks2nqD6u4_Mms-Ay) „Rhino Heirloom“ | Warframe | 31.01.2025 | 1920 × 1080, 60/s | Rhino Prime (Noble-Animationsset) im Arsenal: Atmen, KH, Hand |
| **W-RN** | [Twitch `KawaiiCautiousGoshawkCharlietheUnicorn`](https://clips.twitch.tv/KawaiiCautiousGoshawkCharlietheUnicorn) „Runner Noble“ | Warframe (de_taylor) | 24.05.2019 | 1920 × 1080, 60/s | leichter Warframe von vorn, KH, Tragehaltung |
| W-YQ, W-CS, W-SL, W-KN | [`YummyQuaintCoffeeTriHard`](https://clips.twitch.tv/YummyQuaintCoffeeTriHard), [`CrackySpicyGoatAMPEnergyCherry`](https://clips.twitch.tv/CrackySpicyGoatAMPEnergyCherry), [`SolidLaconicKleeHoneyBadger`](https://clips.twitch.tv/SolidLaconicKleeHoneyBadger-jyx_2whFuKu837p8), [`KitschyNastyHippoNomNom`](https://clips.twitch.tv/KitschyNastyHippoNomNom-JreAN-R0_xF63ueS) | Warframe (de_taylor u. a.) | 2019–2024 | 60/s | Holster, Schulterkamera, Necramech – [O] |
| <a id="a-q-dz"></a>**V-DZ** | [Twitch `ProductiveDirtyFalconYouWHY`](https://clips.twitch.tv/ProductiveDirtyFalconYouWHY) | MarcoStyle (Craban) | 16.03.2019 | 1600 × 900, 60/s | The Division 2: Inventar frontal, Schulterkamera, Holster, Sprint, Wende, Zielen im Laufen |
| **V-CH** | [Twitch `HyperPeacefulClipsmomImGlitch`](https://clips.twitch.tv/HyperPeacefulClipsmomImGlitch) | Chappie (Karenius) | 11.03.2020 | 60/s | The Division 2: Präzisionsgewehr frontal, Handbreite |
| V-KR | [Twitch `AbnegateBlatantReindeerOMGScoots`](https://clips.twitch.tv/AbnegateBlatantReindeerOMGScoots) | 077602 (뉴비환불제조기) | 19.06.2019 | 60/s | The Division 2: Rucksackwaffe über dem Kopf |
| <a id="a-q-gears"></a>**G-GL** | [Twitch `FriendlyBillowingBillBrainSlug`](https://clips.twitch.tv/FriendlyBillowingBillBrainSlug) | Gears of War (lHybr1dl) | 16.07.2019 | 1280 × 720, 60/s | Gears 5: Roadie Run, Zielkamera, Deckung |

Gesichtet ohne Messung: Destiny 2 neun weitere Clips (Vorschaubild zeigte Außenansicht, der Clip nicht), Titanfall 2 26 Clips (Ego, 30/45/48/s),
Warframe 4, Division/Gears 13 (Liste in den Arbeitsordnern). **Suchweg Destiny (nicht wiederholen):** Top-100-Clips von 16 Destiny-Kanälen
(1475 Einträge, 868 Vorschaubilder als Kontaktbögen) – **Twitch-Vorschaubilder sind kein Filter für Außenansicht** (9 von 14 Treffern trogen).

## 2. Ziel 1 – Körperbewegung von außen

| Vorgang | Quelle, Zeit (Bilder) | Messung |
|---|---|---|
| **Gehen, leicht (Warframe)** [M, vorläufig] <a id="a-wf-gehen"></a> | W-TR, 6,80–11,57 s (f408 → f694) | Takt über das orange Leuchtteil der Sekundärwaffe in der rechten Hand (Farbmaske, feste Bildstelle 41–42 % B / 70–71 % H): Spitzen f408, f478, f547, f617 (f694 im beginnenden Kameraschwenk) → **69,7 Bilder je Zyklus (1,16 s) = 1,72 Schritte/s**; mit f694 71,5 Bilder = 1,68 Schritte/s. Halbphase: Hand vorn f478, hinten-außen f512 (34 Bilder). Annahme Armzyklus = Gangzyklus; Füße unter dem Stream-Overlay → **Fußaufsatz, Schrittlänge, Hub nicht messbar** |
| **Atmen, schwer (Warframe Rhino, Noble-Set)** [M, vorläufig] <a id="a-wf-atmen"></a> | W-RH, 0–8,3 s (f0 → f500) | Feste Arsenalkamera (Boden 0,4 px Gesamtbewegung). Brust-Hochpunkte f97, f214, f329, f452 → **Periode ≈ 118 Bilder (1,97 s)**, Hub **≈ 5 px ≈ 0,007 KH**; seitliches Pendeln 6–8 px mit etwa halber Frequenz (≈ 230 Bilder). NCC nur 0,64–0,84 (Glanzlichter) → Größenordnung |
| **Leerlauf, leicht (Titanfall-Pilot, Lobby)** [M] <a id="a-tf-leerlauf"></a> | T1, n 200–2520 (3,3–42,0 s) | Leerlauf ist eine **Schleife von 1080 Bildern = 18,00 s** (feste Helmvorlage, Bestwert bei Verschiebung 1080, zwei volle Durchläufe); Kopf vertikal **≈ 7 px ≈ 0,008 KH** – Atmen kaum sichtbar, Leben kommt aus Kopfdrehungen und Gewichtsverlagerung. Haltung: tiefe Bereitschaft, Gewehr quer vor dem Körper |
| **Titanfall-Abwurf und Aufsatz (schwer)** [M] <a id="a-tf-landung"></a> | T2, n 1136–1149 (18,952–19,169 s) | Titan im Bild ab n 1136, **Fall 8 Bilder** (Arme gespreizt, Beine gestreckt), **Aufsatz in kompakter Hocke n 1144 ±1**, Kuppelschild ab n 1146 (+2 Bilder), Staub ab n 1149; Aufrichten verdeckt. Normaltempo über die HUD-Uhr belegt |
| **Einstieg Pilot → Titan, dritte Person (schwer)** [M] <a id="a-tf-einstieg"></a> | T2, n 1196–1404 (19,953–23,423 s) | Ego-Griff n 1196, Überblendung n 1201–1205, **dritte Person 182 Bilder (3,04 s)**: Pilot springt an den knienden Titan (n 1206–1236), Luke schließt bis ≈ n 1284, Titan richtet sich auf und dreht ≈ 180° (n 1290–1380), Schwarz n 1386; Griff bis Schwarz **3,17 s** ±2 Bilder |
| **Stand mit Gesten, BT-7274 (schwer)** [M]/[O] | T3, n 0–144, Bezugsbild n 102 | Untersicht: KH 640 px mit Antenne (59 % H). BT geht in diesem Fenster **nicht**; Gewichtsverlagerung, Arme pendeln, hebt die Waffe einhändig quer (n 27–36) [O] |
| **Richtungswechsel 180° mit Anschlag (Division 2)** [M] <a id="a-dv-wende"></a> | V-DZ, f926 → f938 (15,43 → 15,63 s) | Fremder Agent: Sprint nach links mit tiefer Waffe → frontal (f929) → **Waffe waagrecht nach rechts angelegt f935: 9 Bilder (0,15 s)**; Silhouette steht **f930–f933 (4 Bilder)**; Beine im Laufschritt nach rechts f938: **12 Bilder (0,20 s)** ±1 |
| **Sprint mit Waffe, seitlich (Division 2)** [M] | V-DZ, f886–f926 | Gewehr **tief vor dem Bauch, Mündung 30–45° unter der Waagrechten**, Oberkörper vorgeneigt; Figur läuft schräg auf die Kamera zu (21 → 28 % H) → keine Schrittlänge, Kopfvorlage NCC 0,31–0,69 → **keine Frequenz** |
| **Ducken in Deckung (Gears 5)** [M Lage] | G-GL, f510 (8,50 s) | Kopfoberkante **52 % H** hinter der Deckungskante (≈ 50 % H), Figur 35–50 % B. Roadie Run 0,5–2,3 s: Bewegungsunschärfe, Füße unter dem Rand → keine Frequenz [O] |
| **Start Gehen, Turm (Destiny 2)** [O] | D-SW1, 45,4–46,0 s | Warlock mit schwerer Waffe dreht und läuft an; Clip endet nach **0,6 s** → keine Phase, keine Frequenz |
| **Batterie tragen (Destiny 2)** [O] | D-MA1, vier Abschnitte 47,5–56,75 s | Außenansicht der eigenen Figur nur beim Tragen (Batterie vor der Brust, beide Arme); Laufabschnitte ≤ 1,5 s (≤ 2 Zyklen) |
| **Laufen mit Schwert (Destiny 2)** [O] | D-EH, 33,0–36,2 s | Warlock läuft vom Betrachter weg, Figur 15–20 % H, **Robe verdeckt die Beine** → keine Fußaufsätze |

**Muster Ziel 1 (Beobachtung):** Leicht gegen schwer ist in dieser Auswahl nur am **Ereignis**, nicht am Gang belegt: der Titan wirkt schwer
über Aufsatz in tiefer Hocke (8 Bilder Fall, Schild 2 Bilder danach) und eine 3-s-Einstiegssequenz mit Aufrichten und Drehen; beim Atmen
bewegen sich leichte wie schwere Figuren kaum (0,007–0,008 KH). Der Warframe-Gang (1,7 Schritte/s) liegt deutlich unter dem Destiny-Sprint-Wippen
in Ego (3,16 Hz, [Methode 21](destiny2.md#methode-21)) – verschiedene Vorgänge (Gehen außen gegen Sprint in Ego), nicht vergleichen.

## 3. Ziel 2 – Waffe am Körper von außen

### 3.1 Figur in der Kamera und Lesbarkeit

| Vorgang | Quelle, Zeit | Messung |
|---|---|---|
| **Eigene Figur im Turm, Destiny 2** [M] <a id="a-d2-turm"></a> | D-DA, f60 (1,000 s) | Sohle 91,5 % H, Scheitel hinter Waffe/Schulterpanzer 45–50 % H → **KH 41–46,5 % H**, Körpermitte ≈ 38 % B (Kamera rechts hinter der Figur) |
| **Andere Hüter auf Distanz, Destiny 2** [M]/[O] <a id="a-d2-lesbar"></a> | D-DA, f60 | Figuren **38 / 26 / 18 / ≈ 5 / ≈ 2 % H**; bei 38 und 26 % H **keine gehaltene Waffe sicher erkennbar** (im Turm hängen die Hände leer), bei ≤ 5 % H nur Umriss [O] |
| **Eigene Figur, Schulterkamera Division 2** [M] | V-DZ, f1260 (21,00 s) | Kopfoberkante **49 % H**, Füße unter dem Bildrand, Körpermitte 38–48 % B (links der Mitte), Zielkreuz rechts neben Kopf/Schulter |
| **Anderer Agent auf Distanz, Division 2** [M]/[O] | V-DZ, f1260 | Figur **≈ 9,5 % H**: Langwaffe als schräge Linie noch als „Gewehr“ erkennbar, Klasse (Gewehr/Präzision/MG) nicht [O] |
| **Schulterkamera Warframe** [O] | W-SL, f90 / f230 | Figur links der Mitte, Kopfoberkante ≈ 35 % der Spielhöhe, Fadenkreuz rechts neben dem Kopf; beim Zoom rückt die Kamera über die rechte Schulter, Waffe füllt 36–49 % B |
| **Zielkamera Gears 5** [M Lage] | G-GL, f270 (4,50 s) | Kamera dicht über der rechten Schulter: **Kopf/Schulter füllen 0–33 % B, Kopfoberkante 22 % H**, Lancer 8–35 % B bei 55–75 % H, Zielkreuz frei rechts |
| Bestand: Schwert-Schulter Destiny 2 [M] | [nahkampf.md › 4](nahkampf.md#4-destiny-schwert-in-der-schulteransicht) | Figur 42–43 % H, links der Mitte, Kopf 3–5 pp unter der Bildmitte |

### 3.2 Tragehaltung, Holster, Zielen

| Vorgang | Quelle, Zeit | Messung |
|---|---|---|
| **Schwere Waffe auf der Schulter, Destiny 2** [M] <a id="a-d2-schulter"></a> | D-DA, f60 | Diagonal auf der linken Schulter von (41,5 / 46) bis (32,8 / 80,5): **≈ 0,8–0,9 KH** projiziert, **24° gegen die Senkrechte**; ebenso D-SW1 (Warlock, 43,8 s) [O] |
| **Holster im Emote: Waffe auf dem Rücken, Destiny 2** [M] <a id="a-d2-ruecken"></a> | D-TW, 0,3 / 3,0 / 9,0 / 14,5 s | Arme über dem Kopf, Spezialwaffe **diagonal auf dem Rücken** von rechter Schulter (53,5 / 52) zur linken Hüfte (36,5 / 88), **≈ 40° gegen die Senkrechte**, in allen vier Bildern gleich (±1 pp, kein Pendeln). Nicht ausgerüstete Waffen sind in keinem Destiny-Clip am Körper zu sehen [O] |
| **Kurze Waffe, anderer Hüter, Destiny 2** [O] | D-TW, 6,0 s | Figur 25,5 % H, kurze Waffe **mündungsoben an der rechten Schulter** – Haltung einer Handwaffe erkennbar, Klasse nicht |
| **Langwaffe, anderer Hüter gebückt, Destiny 2** [M]/[O] | D-SW, f900 (15,0 s) | Jäger gebückt 23 % H, Waffe ≈ 0,78 der gebückten Figurhöhe, Mündung 22° unter der Waagrechten; Klasse nicht sicher (Scharfschütze oder Glefe) |
| **Leerlauf mit Gewehr, Titanfall-Pilot** [M] | T1, n 900 | **Gewehr quer vor dem Körper** (tiefe Bereitschaft), Mündung links unten (≈ 34 / 53), projiziert ≈ 0,47 KH (3/4-Blick) |
| **Kanone auf Hüfthöhe, Legion (Titanfall 2)** [O] | T4, n 612 (10,20 s) | Seitenansicht, Ausfallschritt: Rotorkanone **auf Hüfthöhe waagrecht**, Rumpf nach vorn gekippt, Kanone ≈ 0,6–0,75 der Schritthöhe |
| **Tragehaltung Primär, Warframe** [O] | W-RN, f240 | Gewehr **quer vor dem Bauch**, beide Hände vor dem Becken, Ellbogen angewinkelt; Nahkampfwaffe an der rechten Hüfte schräg nach unten-vorn |
| **Holster Primär am Rücken, Warframe** [O] <a id="a-wf-holster"></a> | W-YQ f240; W-CS f600 | Laufen ohne Waffe in der Hand: Primär **senkrecht hinter der rechten Schulter, Mündung auf Kopfhöhe**, zweiter Stab links; Javlok **diagonal über dem Rücken** (Arsenal) |
| **Necramech im Arsenal** [O] | W-KN, f2420 | Waffe **erhoben in der rechten Hand** neben dem Körper, Mündung oben; Rumpf füllt 44–68 % B (größer als jeder Warframe im selben Menü) |
| **Tragehaltung Gewehr frontal, Division 2** [M] <a id="a-dv-trage"></a> | V-DZ, f180 (3,00 s) | KH **≈ 690 px (77 % H)**, Kopf 0,15 KH; Gewehr **tief vor dem Körper** (Schaft an der rechten Schulter, Mündung schräg unten-vorn), projiziert **0,58 KH** |
| **Präzisionsgewehr frontal, Division 2** [M] | V-CH, f60 (1,00 s) | KH ≈ 678 px; Waffe fast seitlich quer vor dem Körper, projiziert **≥ 0,82 KH** |
| **Holster am Rucksack, Division 2** [M Lage] <a id="a-dv-holster"></a> | V-DZ f1260; V-KR f180 | Zwei Langwaffen **senkrecht bis steil (60–80°), Mündung oben**, links und rechts der Rucksackmitte; bei V-KR überragt das Schalldämpfer-Gewehr den Kopf um **≥ 15 pp H** („Antenne“ der Silhouette, auch bei fremden Agenten); Pistole am Oberschenkel [O] |
| **Zielen im Laufen (Aim-Offset), Division 2** [M] <a id="a-dv-aim"></a> | V-DZ, f938–f947 | Beine laufen in Zielrichtung, Waffe angelegt **15–20° unter der Waagrechten** (Ziel am Boden): **Gierversatz Beine ↔ Waffe ≈ 0° (±10°)**; ein seitlicher Versatz (Beine quer, Brust zum Ziel) kommt in keinem gemessenen Clip vor |

### 3.3 Handgröße außen gegen Ego (Frage F5)

| Figur | Quelle | Hand (KH) | Hand ÷ Kopf | Hand ÷ Waffe | Kopf (KH) |
|---|---|---|---|---|---|
| Destiny-2-Warlock, Charakterbild [M] <a id="a-d2-hand"></a> | D-EH f210 | **0,068** (±0,013, Handlänge) | 0,54 (±0,1) | ≤ 0,10 (Lauf verdeckt) | ≈ 0,13 |
| Titanfall-Pilot, Lobby [M] <a id="a-tf-hand"></a> | T1 n 900 | **0,06–0,07** (Faust) | 0,41–0,45 | 0,13–0,14 (projiziert) | ≤ 0,15 |
| Warframe Rhino Prime, Arsenal [M, grob] | W-RH f60 | **0,10** (Handlänge) | ≈ 0,6 | – (keine Waffe) | ≈ 0,16 |
| Division-2-Agent, Präzisionsgewehr [M] | V-CH f60 | 0,084 (**Handbreite**) | 0,56 (Breite) | 0,10 (Breite) | 0,15 |
| BT-7274 (Titan), Untersicht [O] | T3 n 102 | 0,16–0,19 (Faust, perspektivisch vergrößert) | – | – | – |

**Ego-Gegenwert an derselben Waffe:** nicht messbar – in Ego läuft der Lauf über den Bildrand und ist stark verkürzt (D-EH 0,5 s; die
Ego-Hand nimmt ≈ 35 % H ein, außen 4,8 % H – nur Bildanteil). **Befund:** Die Außenhände der vier Spielfiguren liegen bei **0,06–0,10 KH
und 0,4–0,6 Kopfhöhen**; keine sichtbare Vergrößerung wie bei Valorant (A24, ohne Faktor). Nur der Titan hat übergroße Hände (Faust 2,5–3×
die Pilotenhand relativ zur KH, Einschätzung ohne Perspektivkorrektur). Das stützt die gewählte Antwort **A** zu F5 (ein Handmaß für beide
Ansichten), ist aber kein Ego-Vergleich.

**Muster Ziel 2 (Beobachtung):** (1) **Tiefe Bereitschaft** ist die Ruhehaltung in drei Spielen (Titanfall-Pilot, Warframe, Division:
Gewehr quer bzw. schräg tief vor dem Körper); Destiny-Hüter im Turm halten nichts in der Hand. (2) **Nicht gehaltene Waffen:** Division
und Warframe zeigen Langwaffen am Rücken (senkrecht, Mündung oben, teils über den Kopf hinaus), Destiny zeigt sie nie – nur die geführte
Waffe wandert im Emote diagonal auf den Rücken bzw. liegt schwer auf der Schulter. (3) **Schulterkameras** setzen die Figur links der Mitte
mit dem Kopf knapp unter der Bildmitte (Destiny-Schwert, Division) oder näher heran (Gears beim Zielen); das Zielkreuz bleibt rechts neben
dem Kopf frei. (4) **Lesbarkeit:** ab ≈ 10 % H ist „Langwaffe“ lesbar, die Klasse nicht; Destiny-Hüter ohne gehaltene Waffe sind auch bei
26–38 % H waffenlos.

## 4. Muster je Spiel

- **Destiny 2:** Außenansicht nur in sozialen Räumen, Emote, Super, Schwert, Tragen von Gegenständen und Missionsende. Schwere Waffe auf der
  Schulter (24°), Spezialwaffe im Emote auf dem Rücken (40°), nicht ausgerüstete Waffen unsichtbar; Hand 0,068 KH. Bewegung von außen nicht
  messbar (keine Fenster ≥ 4 Zyklen; Kandidaten mit Third-Person-Glitch nur auf YouTube).
- **Titanfall 2:** Pilot ruht in tiefer Bereitschaft, Leerlauf 18-s-Schleife; Titan als schwere Figur über Abwurf (8 Bilder Fall, Hocke),
  Einstieg 3,0 s in dritter Person, Legion mit Kanone auf Hüfthöhe. Dauer-Fortbewegung des Titanen von außen nur in Mod-Videos (YouTube).
- **Warframe:** dauerhafte dritte Person; Gehtakt 1,7 Schritte/s; Animationssets (Noble/Agile) als Menüposten; Primär senkrecht oder diagonal
  am Rücken; schwerer Rahmen (Rhino) atmet mit 2-s-Periode und 0,007 KH Hub; Necramech hält die Waffe erhoben.
- **The Division 2:** Gewehr tief vor dem Körper, Langwaffen senkrecht am Rucksack (Kopf überragt), Pistole am Oberschenkel; Wende mit
  Anschlag 9 Bilder; Zielen im Laufen ohne Gierversatz in diesem Clip.
- **Gears 5:** Zielkamera sehr nah (Kopf/Schulter füllen ein Drittel der Breite), Ducken in Deckung; Roadie Run nicht messbar.

## 5. Bewertung: gut, nicht so gut, für wen

<!-- BEWERTUNG -->

## 6. Entscheidungsvorlage (für den Nutzer, über Sightline)

<!-- ENTSCHEIDUNG -->

## 7. Offen und nicht messbar

<!-- OFFEN -->

## 8. Prüfung und Zählung

<!-- PRUEFUNG -->
