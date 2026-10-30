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
lange genug quer zur Kamera ([7](#7-offen-und-nicht-messbar)). Destiny 2 zeigt die eigene Figur beim Schießen mit Primär-, Spezial- und schwerer Waffe nie von außen – nur im sozialen
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
| **Atmen, schwer (Warframe Rhino, Noble-Set)** [M, vorläufig] <a id="a-wf-atmen"></a> | W-RH, 0–8,3 s (f0 → f500) | Feste Arsenalkamera (Boden 0,4 px Gesamtbewegung). Brust-Hochpunkte f97, f214, f329, f452 → **Periode ≈ 118 Bilder (1,97 s)**, Hub **≤ ≈ 0,01 KH** (≈ 5 px, unter der Längenauflösung ±8 px – kein Messwert, nur Obergrenze); seitliches Pendeln 6–8 px mit etwa halber Frequenz (≈ 230 Bilder). NCC nur 0,64–0,84 (Glanzlichter) → Größenordnung |
| **Leerlauf, leicht (Titanfall-Pilot, Lobby)** [M] <a id="a-tf-leerlauf"></a> | T1, n 200–2520 (3,3–42,0 s) | Leerlauf ist eine **Schleife von 1080 Bildern = 18,00 s** (feste Helmvorlage, Bestwert bei Verschiebung 1080, zwei volle Durchläufe); Kopf vertikal **≈ 7 px ≈ 0,008 KH** – Atmen kaum sichtbar, Leben kommt aus Kopfdrehungen und Gewichtsverlagerung. Haltung: tiefe Bereitschaft, Gewehr quer vor dem Körper |
| **Titanfall-Abwurf und Aufsatz (schwer)** [M] <a id="a-tf-landung"></a> | T2, n 1136–1149 (18,952–19,169 s) | Titan im Bild ab n 1136, **Fall 8 Bilder** (Arme gespreizt, Beine gestreckt), **Aufsatz in kompakter Hocke n 1144 ±1**, Kuppelschild ab n 1146 (+2 Bilder), Staub ab n 1149; Aufrichten verdeckt. Normaltempo über die HUD-Uhr belegt |
| **Einstieg Pilot → Titan, dritte Person (schwer)** [M] <a id="a-tf-einstieg"></a> | T2, n 1196–1404 (19,953–23,423 s) | Ego-Griff n 1196, Überblendung n 1201–1205, **dritte Person 182 Bilder (3,04 s)**: Pilot springt an den knienden Titan (n 1206–1236), Luke schließt bis ≈ n 1284, Titan richtet sich auf und dreht ≈ 180° (n 1290–1380), Schwarz n 1386; Griff bis Schwarz **3,17 s** ±2 Bilder |
| **Stand mit Gesten, BT-7274 (schwer)** [M]/[O] | T3, n 0–144, Bezugsbild n 102 | Untersicht: KH 640 px mit Antenne (59 % H). BT geht in diesem Fenster **nicht**; Gewichtsverlagerung, Arme pendeln, hebt die Waffe einhändig quer (n 27–36) [O] |
| **Richtungswechsel 180° mit Anschlag (Division 2)** [M] <a id="a-dv-wende"></a> | V-DZ, f926 → f938 (15,43 → 15,63 s) | Fremder Agent: Sprint nach links mit tiefer Waffe → frontal (f929) → **Waffe waagrecht nach rechts angelegt f935: 9 Bilder (0,15 s)**; Silhouette steht **f930–f933 (4 Bilder)**; Beine im Laufschritt nach rechts f938: **12 Bilder (0,20 s)** ±1 (Zuarbeit; Koordinator am Bogen jedes 3. Bilds ±3 nachgeprüft) |
| **Sprint mit Waffe, seitlich (Division 2)** [M] | V-DZ, f886–f926 | Gewehr **tief vor dem Bauch, Mündung 30–45° unter der Waagrechten**, Oberkörper vorgeneigt; Figur läuft schräg auf die Kamera zu (21 → 28 % H) → keine Schrittlänge, Kopfvorlage NCC 0,31–0,69 → **keine Frequenz** |
| **Ducken in Deckung (Gears 5)** [M Lage] | G-GL, f510 (8,50 s) | Kopfoberkante **52 % H** hinter der Deckungskante (≈ 50 % H), Figur 35–50 % B. Roadie Run 0,5–2,3 s: Bewegungsunschärfe, Füße unter dem Rand → keine Frequenz [O] |
| **Start Gehen, Turm (Destiny 2)** [O] | D-SW1, 45,4–46,0 s | Warlock mit schwerer Waffe dreht und läuft an; Clip endet nach **0,6 s** → keine Phase, keine Frequenz |
| **Batterie tragen (Destiny 2)** [O] | D-MA1, vier Abschnitte 47,5–56,75 s | Außenansicht der eigenen Figur nur beim Tragen (Batterie vor der Brust, beide Arme); Laufabschnitte ≤ 1,5 s (≤ 2 Zyklen) |
| **Laufen mit Schwert (Destiny 2)** [O] | D-EH, 33,0–36,2 s | Warlock läuft vom Betrachter weg, Figur 15–20 % H, **Robe verdeckt die Beine** → keine Fußaufsätze |

**Muster Ziel 1 (Beobachtung):** Leicht gegen schwer ist in dieser Auswahl nur am **Ereignis**, nicht am Gang belegt: der Titan wirkt schwer
über Aufsatz in tiefer Hocke (8 Bilder Fall, Schild 2 Bilder danach) und eine 3-s-Einstiegssequenz mit Aufrichten und Drehen; beim Atmen
bewegen sich leichte wie schwere Figuren kaum (≤ ≈ 0,01 KH, an der Auflösungsgrenze). Der Warframe-Gang (1,7 Schritte/s) liegt deutlich unter dem Destiny-Sprint-Wippen
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
| **Holster im Emote: Waffe auf dem Rücken, Destiny 2** [M] <a id="a-d2-ruecken"></a> | D-TW, 0,3 / 3,0 / 9,0 / 14,5 s | Arme über dem Kopf, Spezialwaffe **diagonal auf dem Rücken** von rechter Schulter (53,5 / 52) zur linken Hüfte (36,5 / 88), **≈ 40° gegen die Senkrechte**, in allen vier Bildern gleich (±1 pp, kein Pendeln). In keinem Clip sind zwei Waffen gleichzeitig am Körper [O]; Spieler kritisieren genau das („nur eine Waffe sichtbar“) und fast waagrechte Rückenlagen (Q1, Q2, Q4) |
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
Gewehr quer bzw. schräg tief vor dem Körper); andere Destiny-Hüter im Turm halten nichts in der Hand. (2) **Nicht gehaltene Waffen:** Division
und Warframe zeigen Langwaffen am Rücken (senkrecht, Mündung oben, teils über den Kopf hinaus), Destiny zeigt nur die zuletzt geführte – sie wandert im Emote diagonal auf den Rücken bzw. liegt schwer auf der Schulter. (3) **Schulterkameras** setzen die Figur links der Mitte
mit dem Kopf knapp unter der Bildmitte (Destiny-Schwert, Division) oder näher heran (Gears beim Zielen); das Zielkreuz bleibt rechts neben
dem Kopf frei. (4) **Lesbarkeit:** bei 9,5 % H (ein Beispiel, Division) ist „Langwaffe“ noch lesbar, die Klasse nicht – keine Schwelle; Destiny-Hüter ohne gehaltene Waffe sind auch bei
26–38 % H waffenlos.

## 4. Muster je Spiel

- **Destiny 2:** Außenansicht nur in sozialen Räumen, Emote, Super, Schwert, Tragen von Gegenständen und Missionsende. Schwere Waffe auf der
  Schulter (24°), Spezialwaffe im Emote auf dem Rücken (40°), nur eine Waffe sichtbar; Hand 0,068 KH. Bewegung von außen nicht
  messbar (keine Fenster ≥ 4 Zyklen; Kandidaten mit Third-Person-Glitch nur auf YouTube).
- **Titanfall 2:** Pilot ruht in tiefer Bereitschaft, Leerlauf 18-s-Schleife; Titan als schwere Figur über Abwurf (8 Bilder Fall, Hocke),
  Einstieg 3,0 s in dritter Person, Legion mit Kanone auf Hüfthöhe. Dauer-Fortbewegung des Titanen von außen nur in Mod-Videos (YouTube).
- **Warframe:** dauerhafte dritte Person; Gehtakt 1,7 Schritte/s; Animationssets (Noble/Agile) als Menüposten; Primär senkrecht oder diagonal
  am Rücken; schwerer Rahmen (Rhino) atmet mit ≈ 2-s-Periode (vorläufig) und Hub ≤ ≈ 0,01 KH; Necramech hält die Waffe erhoben.
- **The Division 2:** Gewehr tief vor dem Körper, Langwaffen senkrecht am Rucksack (Kopf überragt), Pistole am Oberschenkel; Wende mit
  Anschlag 9 Bilder; Zielen im Laufen ohne Gierversatz in diesem Clip.
- **Gears 5:** Zielkamera sehr nah (Kopf/Schulter füllen ein Drittel der Breite), Ducken in Deckung; Roadie Run nicht messbar.

## 5. Bewertung: gut, nicht so gut, für wen

Spielerquellen: 41 (Ziel 1: 27, Ziel 2: 15, eine für beide; drei nur Suchauszug), Fachquellen: 22 (Ziel 1: 15, Ziel 2: 9, davon W6/W7 dieselben Quellen wie B1/B11). Reddit lädt per curl
nicht (403); die Fäden sind über das Archiv Arctic Shift geprüft – **Punktzahlen sind Archivstand**, nicht heute. Kurzzeichen der Quellen
in [5.1](#51-quellen-der-bewertung); die Spalte „Belege“ aus Standard › 6 E steckt in den Kurzzeichen der Spalten „Gut“/„Nicht so gut“. Eigene Einschätzungen sind als solche markiert.

| Spiel | Gegenstand | Gut (warum) | Nicht so gut (warum) | Für wen | Spielerstimmen | Entwickler/Fach |
|---|---|---|---|---|---|---|
| **Destiny 2** <a id="a-e-d2-koerper"></a> | Körper von außen (Turm, Emote, Schwert) | Dritte Person in Sozialräumen gefällt, Wunsch nach mehr (P7, 446 P.) | Emotes und Ganzkörper steifer als in Destiny 1 (P5, P6); starres Stehen im Turm (P11, Suchauszug); Gehtempo (P8) | PvE-Sozialräume, Mode-Spieler (P10) | wiederkehrend „steif“ (2 Fäden); Gegenstimme: Mocap ist nicht steif (P5-Kommentare) | Bungie-Animationssystem (B5 GDC, B6 SIGGRAPH); Kotaku zu Ego (B15) |
| Destiny 2 <a id="a-e-d2-waffe"></a> | Waffe am Körper | Schwert-Rahmen mit eigener Halte-/Laufanimation geschätzt (Q9); Rückenwinkel laut Spielerbeobachtung still korrigiert (Q2, [C], nicht von Bungie bestätigt) | Rückenholster: Waffe fast waagrecht, Arme durchdringen, nur eine Waffe sichtbar (Q1, Q2, Q4); dritte Person im PvP verschafft Sichtvorteil („3-Peeking“, Q6, 1276 P.) | PvP (Fairness), Kosmetikspieler | wiederkehrend Holster (3 Fäden); Gegenstimme: Clipping-Grenze akzeptiert (Q4) | Hand folgt Waffe / Waffe folgt Hand (W3, GDC 2015); Bungie zu 3-Peeking (W4) |
| **Titanfall 2** <a id="a-e-tf"></a> | leicht gegen schwer | Kontrast schneller Pilot / träger Titan als Absicht wahrgenommen (P4); Titankampf über Entscheidungen statt „mushy“ (B3) | Titanen wirken leichter als in Titanfall 1, weniger Masse (P1 2855 P., P2); im Tech-Test zu langsam – Respawn beschleunigte Dash und Ion/Scorch (B8–B10) | Mech-Fans (Gewicht), PvP-Profis (Tempo) | wiederkehrend „TF1 schwerer“ (4 Quellen); Gegenstimme: TF1 „clunky“ (P3) | B3 (GDC 2017), B8–B10 (geändert nach Kritik) |
| **Warframe** <a id="a-e-wf"></a> | Körper von außen | Laufanimation transportiert Tempo (P16 4141 P., P17); Set-Idles beliebt (P12, 448 P.) | Animationssets wirken nur im Stand, in Bewegung „schnappt“ die Figur in den Standardlauf (P12–P15, B14); Necramech mit Zwangspausen und langsamem Dash (P19, P20, B13) | Fashion-Spieler; Mech-Spieler | wiederkehrend (5 Quellen); Gegenstimme: Aufwand je Rahmen | B13, B14 (Wiki mit Update-Historie) |
| Warframe | Waffe am Körper | Holster-Stile als Kosmetik (W5), kreative Lagen gewünscht (Q11) | zu wenige Lagen für sperrige Primärwaffen (Q11, Q12) | Fashion-Spieler | wiederkehrend (3) | W5 (Update 32) |
| **The Division 2** <a id="a-e-dv"></a> | Körper von außen | Deckungswechsel-Animation beliebt (P23, 1967 P.); schnelleres Laufen gefällt (P24) | E3-Sprint „unnatürlich“ (P21), Beta „clunky“ (P22) | Deckungsshooter, PvE | wiederkehrend; Gegenstimme: Gewicht der Ausrüstung | keine Massive-Quelle gefunden |
| The Division 2 | Waffe am Körper | Einschätzung: Rucksackwaffen machen die Ausrüstung von außen lesbar ([3.2](#a-dv-holster)) | Pistole schwebt neben dem Holster (Q13); Rucksackwaffe überragt den Kopf [M] | Kosmetikspieler | Einzelstimme | – |
| **Gears 5 / E-Day** <a id="a-e-gears"></a> | Körper von außen | Gewicht über Impuls statt Sofortstopp (B11); impulserhaltende Übergänge per Inertialization (B4) | geduckter Roadie Run wirkt im Mehrspieler unsinnig (P25, P27); Wallbouncing gegen „schwere“ Figuren (P26) | PvP-Profis, Kampagnenspieler | wiederkehrend, gespalten | B4 (GDC 2018), B11, B12 (2007, Roadie Run geändert) |
| **Fortnite** | Lesbarkeit der Waffe | – | Waffenklasse am Modell nicht erkennbar (Q14) | alle, besonders kleine Bildschirme | wiederkehrend im großen Faden | A01 per ID ([design-ausruestung](design-ausruestung.md#2-quellen)) |
| allgemein | Ego gegen außen (F5) | getrennte Modelle/Animatoren für Ego und außen, Ego-Waffe gestreckt und vergrößert (W2 Overwatch, GDC 2017) | keine Quelle nennt eine Zahl für Hand außen gegen Ego | Art-Direktion | – | W2, W8 (Valve-Wiki, Suchauszug), W9 (Suchauszug) |

### E2 – Lehren für Critic (Vorschlag, dort entscheiden)

- **Übernehmen:** Gewicht über **Ereignisse und Übergänge** statt über langsames Grundtempo – Titan-Aufsatz in tiefer Hocke (8 Bilder Fall,
  [Landung](#a-tf-landung)), Impuls beim Stopp (B11), Inertialization (B4); Titanfall beschleunigte nach Kritik (B8–B10).
- **Übernehmen:** Ruhe als **lange Schleife mit sehr kleinem Atemhub** (≈ 0,01 KH; Titanfall 18 s, Warframe-Rhino ≈ 2 s Atemperiode, vorläufig) und
  Leben über Kopf- und Gewichtswechsel ([Leerlauf](#a-tf-leerlauf), [Atmen](#a-wf-atmen)).
- **Übernehmen:** Schrittlänge an die zurückgelegte Strecke koppeln (B2 GDC 2014: Fuß rutscht nie), damit Füße bei der Isometrie-Kamera nicht gleiten.
- **Vermeiden:** einen Ruhestil, den die Bewegung nicht fortsetzt (Warframe-„Zurückschnappen“, P12–P15); feste Zwangspausen schwerer Figuren
  ohne Abbruch (Necramech, P19, B13).
- **Testen:** Gangtakt leicht ≈ 1,7 Schritte/s ([Warframe](#a-wf-gehen), vorläufig) als Startwert, schwer langsamer – Zahl für schwer fehlt
  ([7](#7-offen-und-nicht-messbar)); Wende mit Anschlag ≈ 9–12 Bilder ([Division](#a-dv-wende)).

### E2 – Lehren für BALLON (Vorschlag, dort entscheiden)

- **Übernehmen:** Ruhehaltung **tiefe Bereitschaft** (Waffe quer/schräg tief vor dem Körper, beide Hände) wie Titanfall-Pilot, Warframe und
  Division ([3.2](#32-tragehaltung-holster-zielen)); schwere Waffe auf der Schulter mit ≈ 24° gegen die Senkrechte ([Destiny](#a-d2-schulter)).
- **Übernehmen:** Rückensockel **diagonal** (Destiny ≈ 40°, [Emote](#a-d2-ruecken)) statt waagrecht – die Destiny-Kritik richtet sich gegen
  fast waagrechte Lagen und Arme, die durch die Waffe gehen (Q1, Q2).
- **Vermeiden:** Rucksackwaffen, die den Kopf überragen (Division ≥ 15 pp H, [Holster](#a-dv-holster)) – Einschätzung: verdirbt die
  Robotersilhouette und kollidiert mit dem Rückenmodul (F9 A).
- **Testen:** Handgröße außen 0,06–0,10 KH bzw. 0,4–0,6 Kopfhöhen ([3.3](#33-handgröße-außen-gegen-ego-frage-f5)) gegen den Ego-Arm v3 im
  Modell (orthografisch) prüfen – F5 A bleibt tragfähig; Waffenklasse auf Distanz über eine eigene Silhouette je Klasse (Q14, A01), weil im
  einzigen Beispiel bei 9,5 % H nur „Langwaffe“ lesbar war.

### 5.1 Quellen der Bewertung

**Spieler (Ziel 1):** P1 [r/titanfall 1kpf4ts](https://www.reddit.com/r/titanfall/comments/1kpf4ts/tf2_vs_tf1_titans/) · P2
[7447yf](https://www.reddit.com/r/titanfall/comments/7447yf/) · P3 [nbm1w7](https://www.reddit.com/r/titanfall/comments/nbm1w7/) · P4
[Well Played](https://www.well-played.com.au/titanfall-2-falling-short/) · P5 [r/DestinyTheGame a7ecvt](https://www.reddit.com/r/DestinyTheGame/comments/a7ecvt/)
· P6 [3qdgh5](https://www.reddit.com/r/DestinyTheGame/comments/3qdgh5/) (Destiny 1) · P7 [rdvjd1](https://www.reddit.com/r/DestinyTheGame/comments/rdvjd1/)
· P8 [87yjx7](https://www.reddit.com/r/DestinyTheGame/comments/87yjx7/) · P10 [Steam 3rd person view](https://steamcommunity.com/app/1085660/discussions/0/4299320215882183471)
· P11 [bungie.net 165680825](https://www.bungie.net/PL/Forums/Post/165680825?page=4) (Suchauszug) · P12 [r/Warframe 7wfha3](https://www.reddit.com/r/Warframe/comments/7wfha3/)
· P13 [set56m](https://www.reddit.com/r/Warframe/comments/set56m/) · P14 [8h8ezu](https://www.reddit.com/r/Warframe/comments/8h8ezu/) · P15
[Steam Warframe](https://steamcommunity.com/app/230410/discussions/0/1651045226219383516) · P16 [mxsjji](https://www.reddit.com/r/Warframe/comments/mxsjji/)
· P17 [10y20xs](https://www.reddit.com/r/Warframe/comments/10y20xs/) · P19 [1adlj74](https://www.reddit.com/r/Warframe/comments/1adlj74/) · P20
[Warframe-Forum 1241282](https://forums.warframe.com/topic/1241282-necramech-movement-improvement-ideas/) (403, Suchauszug) · P21
[MeinMMO](https://mein-mmo.de/the-division-2-spieler-amuesieren-sich-ueber-seltsame-lauf-animationen/) · P22 [Overclockers](https://forums.overclockers.co.uk/posts/32492627/)
· P23 [r/thedivision by6dut](https://www.reddit.com/r/thedivision/comments/by6dut/) · P24 [1j06rtb](https://www.reddit.com/r/thedivision/comments/1j06rtb/)
· P25 [r/GearsOfWar 1u073t7](https://www.reddit.com/r/GearsOfWar/comments/1u073t7/) · P26 [1lbzgdt](https://www.reddit.com/r/GearsOfWar/comments/1lbzgdt/)
· P27 [1037tfp](https://www.reddit.com/r/GearsOfWar/comments/1037tfp/).
**Spieler (Ziel 2):** Q1 [779ohp](https://www.reddit.com/r/DestinyTheGame/comments/779ohp/) · Q2 [73dcpz](https://www.reddit.com/r/DestinyTheGame/comments/73dcpz/)
· Q4 [9ly2cs](https://www.reddit.com/r/DestinyTheGame/comments/9ly2cs/) · Q5 [hc8xhi](https://www.reddit.com/r/DestinyTheGame/comments/hc8xhi/) · Q6
[gtaazh](https://www.reddit.com/r/DestinyTheGame/comments/gtaazh/) · Q9 [1wnazlv](https://www.reddit.com/r/DestinyTheGame/comments/1wnazlv/) · Q11
[r/Warframe uxdf44](https://www.reddit.com/r/Warframe/comments/uxdf44/) · Q12 [1o2ksgt](https://www.reddit.com/r/Warframe/comments/1o2ksgt/) · Q13
[r/thedivision 1lk53hi](https://www.reddit.com/r/thedivision/comments/1lk53hi/) · Q14 [r/FortNiteBR 18xi1xf](https://www.reddit.com/r/FortNiteBR/comments/18xi1xf/).
**Fach/Entwickler:** B1 [Zadziuk, GDC 2016 Motion Matching (For Honor)](https://www.youtube.com/watch?v=KSTn3ePDt50) · B2 [Rosen, GDC 2014
(Overgrowth)](https://www.youtube.com/watch?v=LNidsMesxSE) · B3 [Pineda, GDC 2017 (Titanfall 2)](https://www.youtube.com/watch?v=5kFqrI11xTc) · B4
[Bollo, GDC 2018 Inertialization (Gears)](https://www.youtube.com/watch?v=BYyv4KTegJI) · B5 [GDC, Destiny-Animation](https://www.youtube.com/watch?v=RmeEAFuE_2Q)
· B6 [SIGGRAPH „Destiny Character-Animation System“](https://history.siggraph.org/?p=59754) · B8 [Game Informer 24.08.2016](https://gameinformer.com/b/news/archive/2016/08/24/respawn-is-making-changes-to-titanfall-2-based-on-player-concerns)
· B9 [Windows Central](https://www.windowscentral.com/respawn-entertainment-addresses-feedback-titanfall-2s-recent-tech-test) · B10 [EA/Respawn
Tech Test and Feedback](https://www.ea.com/games/titanfall/titanfall-2/news/tech-test-and-feedback) (leitet um, Suchauszug) · B11 [gearsofwar.com
E-Day Gameplay Updates](https://www.gearsofwar.com/en-au/news/e-day-gameplay-updates/) · B12 [Engadget 2007](https://www.engadget.com/2007/04/15/epic-talks-post-update-roadie-run/)
· B13 [Warframe-Wiki Necramech](https://wiki.warframe.com/w/Necramech) · B14 [Animation Set](https://wiki.warframe.com/w/Animation_Set) · B15
[Kotaku](https://kotaku.com/what-destiny-2-and-overwatch-animations-tell-us-about-t-1819716453) · W1 [Epic: Aim Offset](https://dev.epicgames.com/documentation/en-us/unreal-engine/aim-offset-in-unreal-engine)
· W2 [Boehm, GDC 2017 (Overwatch)](https://www.youtube.com/watch?v=7t0hLZd_8Z4) · W3 [Hunt/Söderlind, GDC 2015 (Bungie)](https://www.youtube.com/watch?v=U_4u0kbf-JE)
· W4 [MeinMMO zu 3-Peeking](https://mein-mmo.de/destiny-2-three-peeking-deutet-neue-3-person-waffen-an/) · W5 [Warframe-Wiki Holster](https://wiki.warframe.com/w/Holster)
· W8 [Valve Viewmodel](https://developer.valvesoftware.com/wiki/Viewmodel) (Suchauszug) · W9 [Unknown Worlds](https://unknownworlds.com/futureperfect/?p=317) (Suchauszug).
Vollständige Liste mit Datum, Sprecher, Zustimmung und Gegenstimmen in `data/aussenansicht.json` › `player_voices`, `dev_sources`.

## 6. Entscheidungsvorlage (für den Nutzer, über Sightline)

<a id="frage-s1"></a>**Frage S1 – Wie wird Ziel 1 (Gang, Sprint, Sprung von außen) belegt?** (Abnehmer Critic; Aufwand S–M)
- **A (Empfehlung):** Folgesitzung **am Mac** mit YouTube (1080p60/720p60): zuerst Warframe `Zb_IHDN-YJs` (Ultraclocked, Movement Comparison),
  `VpoyL3nZcGA` (Necramech), Titanfall `IcXGMpYi1ps` / `9l4O0VvfsQk` (dritte Person, BT neben dem Piloten), Destiny `7N1WL8eu38I` /
  `HCI6oocEksk` (Third-Person-Glitch) – je Vorgang ≥ 4 Zyklen, Retail gegen Mod/Glitch kennzeichnen. Liefert Hz, KH-Schrittlänge, Hub, leicht/schwer.
- **B:** Critic setzt Startwerte aus Fachquellen und eigener Einschätzung, Motiongen misst später nach.
- **C:** Eigene Mitschnitte (Warframe frei spielbar) mit fester Seitenkamera – sauberste Messung, aber Aufnahmeaufwand beim Nutzer.
- Antwort (Nutzer im Sitzungschat, 30.10.2026): „Alle wie empfohlen“ → **A** (Empfehlung)

<a id="frage-s2"></a>**Frage S2 – Welche Waffen trägt der Roboter sichtbar am Körper?** (Abnehmer BALLON/Critic/Cube Escape; Stil, S)
- **A (Empfehlung):** nur die geführte Waffe sichtbar (Destiny-Ansatz); im Leerlauf/Emote wandert sie auf Rücken (≈ 40°) bzw. die schwere
  auf die Schulter (≈ 24°). Ein Sockel am Rücken genügt; die Silhouette des Roboters bleibt frei (F-R5/F9 Rückenmodul).
- **B:** alle ausgerüsteten Waffen sichtbar (Warframe/Division): Langwaffe senkrecht am Rücken, Handwaffe am Oberschenkel – mehr Lesbarkeit
  der Ausrüstung, aber „Antenne“ über dem Kopf und Kollision mit dem Rückenmodul (F9 A).
- **C:** später in Cube Escape entscheiden, wenn die Isometrie-Kamera steht.
- Antwort (Nutzer im Sitzungschat, 30.10.2026): „Alle wie empfohlen“ → **A** (Empfehlung)

<a id="frage-s3"></a>**Frage S3 – Ruhehaltung mit Waffe außen?** (Abnehmer Critic; Stil, S)
- **A (Empfehlung):** tiefe Bereitschaft – Waffe quer bzw. schräg tief vor dem Körper, beide Hände an der Waffe (Titanfall-Pilot,
  Warframe, Division); Atemhub sehr klein (≈ 0,01 KH), Leben über Kopf- und Gewichtswechsel in langer Schleife (Titanfall 18 s).
- **B:** Waffe hängt an einer Hand, Arme locker (andere Destiny-Hüter im Turm halten nichts) – entspannter, liest sich aber nicht als bewaffnet.
- Antwort (Nutzer im Sitzungschat, 30.10.2026): „Alle wie empfohlen“ → **A** (Empfehlung)

## 7. Offen und nicht messbar

- **Schrittfrequenz nach 4-Zyklen-Regel, Schrittlänge in KH, Hub und Pendeln im Gehen/Laufen/Sprint, Start/Stopp, Drehen auf der Stelle,
  Sprung, Landung zu Fuß, Fallen:** in keinem Spiel belegt. Gründe: YouTube ab ≈ 12:20–12:35 gesperrt (Bot-Prüfung/403); Twitch-Clips zeigen
  Figuren laufend fast nur von hinten oder schräg (keine Seitenansicht, kein Weltmaßstab), Overlays verdecken Füße (Warframe-Devstreams),
  Destiny zeigt die eigene Figur beim Schießen mit Primär-, Spezial- und schwerer Waffe nie von außen (nur Super, Schwert, Emote, Sozialraum, Tragen), Gears-Roadie-Run ist bewegungsunscharf. Nicht erneut aus denselben Twitch-Kanälen
  versuchen (Suchweg in [1](#1-quellen-und-methode) und in den Arbeitsordnern).
- **Leicht gegen schwer im Gang** (Pilot/Titan, Warframe/Necramech): nur am Ereignis belegt (Abwurf, Einstieg, Atmen). Kandidaten: Titanfall
  `IcXGMpYi1ps`, `9l4O0VvfsQk`, `g-ONoIEX48M`; Warframe `VpoyL3nZcGA`, `CybLkZ5jhi4`, `Zb_IHDN-YJs`; Twitch-Kampagnen-VODs 2913345452,
  2912894989 („Blood and Rust“, „The Beacon“).
- **Aim-Offset als Gierwinkel** (Beine quer, Oberkörper zum Ziel): in keinem Clip vorgekommen; Division-Beispiel zeigt nur Neigung.
  Kandidaten: Destiny `gABu34ErU88` (Snowball-Glitch), Division `Pi1-s4NYdOk`, `W4bsMcsp_P0`.
- **Feuern mit sichtbarem Rückstoß, Nachladen und Waffenwechsel von außen:** nicht belegt. Kandidaten: Titanfall `wmo_Fd9O-ps` (alle
  Nachladeanimationen in dritter Person), Division `vHMvNFzeC0g`, `NOeeQJrEbDk`, Gears `LoG8BimP61E`, `-KCBlBbeSO4`, `I7pTinIl0vg`.
- **Ego-Gegenwert der Hand an derselben Waffe (F5):** in Ego läuft die Waffe über den Bildrand – mit Rasterbildern nicht messbar; nur mit
  Modell-/Manifestmaßen (orthografische Waffe + Ego-Arm v3) lösbar, nicht aus Clips.
- **Erkennbarkeitsschwelle der Waffenklasse** (ab wie viel % H): nur zwei Punkte (Division 9,5 % H: „Langwaffe“ ja, Klasse nein; Destiny
  26–38 % H ohne gehaltene Waffe). Braucht eine Figur, die dieselbe Waffe in mehreren Abständen hält.
- **Warframe-Animationssets (Noble/Agile) im Vergleich, Necramech-Gang:** nicht gemessen (YouTube).
- **Weitere YouTube-Kandidaten Destiny 2** (Metadaten geprüft, 60/s): `9lKym3DMboc`, `Sg1lY2epEFc`, `Lpmv5cEQDQE`, `a5QXxK9r1_A` (Mod-Client
  prüfen), `cGCwARvHGX0` („Weird Walking Animation“), `RMLZqmCW4q4`, `SbdFtaovF98`; nur 30/s (Form): `3aTFDd8regs`, `LK06ySvC4os`,
  `9pxr9Ys5NGI`, `5Mrnz-hC4wM`, `tyaeI_vF-Ww`; Destiny 1, ausschließen: `fFRqOJsNYx4`. Titanfall (weitere): `nemPqWMIMK4`, `B8TtmPF2nDk`
  (vor Release), `pBbcRhDCbcM`; nur 30/s: `Db8b4EmYiVw`, `RBxR-JD1a9g`, `JgAplNlSH9w`.

## 8. Prüfung und Zählung

- **Unteragenten:** fünf (Destiny 2, Titanfall 2, Warframe, Division 2/Gears 5 messen, einer für Stimmen und Fachquellen), je eigener
  Arbeitsordner unter `~/Library/Caches/CubeEscape/reference/aussenansicht/` im Cloud-Container; keiner schrieb ins Repo.
- **Nachmessung durch den Koordinator: 12 Zahlen, 11 bestätigt, 1 teilweise** – Warframe-Gang (Spitzen f409/478/547/618 gegen
  f408/478/547/617; f694 nicht als Spitze gefunden → 3 sichere Zyklen, Zeile „vorläufig“), Rhino-KH 713 px (% gelten fürs Streambild),
  Rhino-Hand 0,10 KH; Titanfall-Leerlaufschleife 1080 Bilder (Gesamtbild-Differenz, Minimum bei 1080), Aufsatz n 1144, Helmoberkante 14,5 % H,
  Faust/Kopf ±10 px; Division-KH ≈ 700 gegen 690 px, Wende f935 (Bogen jedes 3. Bild, ±3); Destiny schwere Waffe (41/46) → (33/80), Hüter 40/29/18 gegen 38/26/18 % H;
  **teilweise:** Destiny-Scheitel der eigenen Figur verdeckt → KH als Spanne 41–46,5 % H übernommen.
- **Quellen:** 22 Twitch-Clips (14 gemessen und in `clips.json`, 8 nur gesichtet; 60/s, T2 59,94/s) mit yt-dlp-Metadaten (Kanal, Ersteller, Datum) in [1](#1-quellen-und-methode);
  6 von 6 Fach-/Presse-URLs per curl (HTTP 200), 3 von 3 Reddit-Fäden über das Archiv (Titel und Punktzahl wie im Bericht).
- **Übernommen / nicht übernommen:** übernommen 37 Mess- und Sichtzeilen der Zuarbeiten (21 [M], 16 [O]; Destiny 12, Titanfall 7, Warframe 9, Division/Gears 9; im JSON zusammengefasst zu 34 Einträgen in `body_motion`/`weapon_body` und 5 in `hand_size`); **korrigiert 3** (Warframe-Gang 4 → 3 sichere
  Zyklen und „vorläufig“; Destiny-KH als Spanne; Destiny-Holster: „nie am Körper“ → nur die geführte Waffe, Q1/Q2/Q4); nicht übernommen:
  Zeitangaben aus 10/s-Bögen (Titan-Exekution 3,9 s, nur [O]) und alle Bewertungstexte ohne Quelle.
- **Zählung:** 5 Spiele (Destiny 2, Titanfall 2, Warframe, The Division 2, Gears 5; Fortnite nur Stimme), 22 Clips (14 gemessen, 8 gesichtet), 41 Spieler- und
  22 Fachquellen (Ziel 2: 9, davon W6/W7 = B1/B11), ≈ 30 vermessene Einzelbilder; 36 YouTube-Kandidaten für die Folgesitzung.
