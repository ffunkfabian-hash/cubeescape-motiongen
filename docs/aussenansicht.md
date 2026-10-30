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

**Kurzbefund REF 0.33 „Gaitline“ (Mac, 30.10.2026; 19 YouTube-Quellen aus [7](#7-offen-und-nicht-messbar) und eine eigene Suche, [2.1](#21-gang-von-außen--ref-033),
[3.4](#34-feuern-nachladen-und-wechsel-von-außen--ref-033)).** Gangtakt nach der 4-Zyklen-Regel jetzt in zwei Spielen: **Warframe Laufen 3,81
Schritte/s** (leicht) und **Gears 5 Gehen 3,00 Schritte/s** (schwer gepanzerte Figur, 8 Zyklen); Sprint/Roadie Run 4,09 bzw. 4,17 Schritte/s
(vorläufig), Destiny-Warlock von hinten ≈ 3,2–3,3 (vorläufig, Glitch-Kamera). Der Takt kommt aus **Posengleichheit**, nicht aus Fußaufsätzen:
in keiner Quelle steht eine ganze Figur quer zur Kamera bei echten 60/s – **Fußaufsatz ±1 Bild, Schrittlänge und Hub in KH bleiben offen**,
ebenso **Pilot ↔ Titan und Warframe ↔ Necramech im Gang** (kein Titan-/Mech-Gang über ≥ 4 Zyklen). Neu für Ziel 2: Nachladen von außen
(Titanfall R-201 128 Bilder bis Ausgangslage, Gears Lancer 146 Bilder bis ruhig), Wechsel in Division 2 (≥ 18 Bilder bis Anschlag), Rückstoß von außen als
**Kamerakick** (Destiny-Glitch 2,4–3,5 pp, Gears Gnasher ≥ 7,6 pp) bei kleinem Körperausschlag (≈ 0,03 KH). Ein Gierversatz Beine ↔ Oberkörper
kommt in keinem der 20 Videos vor.

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

### 1.1 Quellen REF 0.33 (YouTube, Mac)

yt-dlp 2026.10.21 mit Deno und `yt-dlp-ejs`, **nacheinander** geladen (ein Lader, keine parallelen Abrufe aus Unteragenten; keine Bot-Prüfung
in ≈ 1,5 h), Format 299/303 (1080p60) bzw. 298 (720p60). Kanal, Datum und Titel je ID per `yt-dlp -J` am 30.10.2026; **echte Bildrate** je
Video über den Anteil wiederholter Bilder (mittlere Bilddifferenz < 0,5) an mehreren Stellen. `capture`: **retail** · **showcase** (Retail,
für ein Video geschnitten) · **glitch** (Destiny Third-Person-Glitch) · **mod** (Northstar-/Konsolenkamera) – Kamera und Animationszustände
weichen bei glitch/mod ab. Zeiten nur bei echten ≈ 60/s; Bildindex n = Zeit × Containerrate.

| Kürzel | ID | Kanal \| Datum \| Titel (gekürzt) | Bild, echte Rate | capture | hier |
|---|---|---|---|---|---|
| <a id="a-q-ultraclocked"></a>**W-UC** | [`Zb_IHDN-YJs`](https://www.youtube.com/watch?v=Zb_IHDN-YJs) | Ultraclocked \| 25.02.2026 \| Warframe vs Duet Night Abyss - Movement Comparison | 1080p, 60/s (Standbild 7,4–8,3 s), linke Hälfte = Warframe | showcase | Laufen, Sprint, Schleichen, Landung |
| W-DB | [`CybLkZ5jhi4`](https://www.youtube.com/watch?v=CybLkZ5jhi4) | Drunk Bear \| 22.07.2017 \| Warframe Animation Database: Default | 1080p, **6–18/s** | showcase | nur Form |
| W-NM, W-VR | [`VpoyL3nZcGA`](https://www.youtube.com/watch?v=VpoyL3nZcGA), [`GvseUKgOreM`](https://www.youtube.com/watch?v=GvseUKgOreM) | DizzyBones \| 21.09.2020 \| Necramech max movement speed; Mactics \| 11.09.2024 \| I FINALLY Got The VOIDRIG | 720p, 29/s; 720p, 52–53/s | retail | Necramech: unscharf bzw. nie zu Fuß |
| <a id="a-q-eyelessrook"></a>**T-ER** | [`wmo_Fd9O-ps`](https://www.youtube.com/watch?v=wmo_Fd9O-ps) | EyelessRook \| 04.10.2020 \| All Weapons Reload Animations In Third Person | 1080p, 60/s | retail (Ego eines zweiten Spielers auf den Piloten) | Nachladen von außen |
| T-FG1, T-FG2 | [`IcXGMpYi1ps`](https://www.youtube.com/watch?v=IcXGMpYi1ps), [`nemPqWMIMK4`](https://www.youtube.com/watch?v=nemPqWMIMK4) | Froggygun \| 08.01.2023 / 20.02.2023 \| 3rd person / thirdperson above | 720p, 60/s; 720p, **17–54/s** | mod (Northstar-Konsole im Bild) | Pilot/Titan nur [O] |
| T-TK | [`9l4O0VvfsQk`](https://www.youtube.com/watch?v=9l4O0VvfsQk) | Taskinoz \| 25.11.2017 \| 3rd Person % 2:12.10 | 144p-Scan; Abschnitte 720p **27–55/s** | mod (vermutet, Konsole nicht sichtbar) | Normaltempo per Timer, kein Gang |
| T-GO | [`g-ONoIEX48M`](https://www.youtube.com/watch?v=g-ONoIEX48M) | Game Over \| 14.01.2022 \| Chapter 2 - BT 7274 | 720p, 31–60/s | retail | BT nie gehend neben dem Piloten |
| <a id="a-q-jarv"></a>**D-JV** | [`7N1WL8eu38I`](https://www.youtube.com/watch?v=7N1WL8eu38I) | Jarv \| 31.12.2020 \| THIRD PERSON GLITCH! (Beyond Light, Season 12) | 1080p, 57,8/s | glitch | Lauf von hinten, Normaltempo |
| <a id="a-q-ign"></a>**D-IGN** | [`HCI6oocEksk`](https://www.youtube.com/watch?v=HCI6oocEksk) | IGN \| 24.12.2017 \| How to Play Destiny 2 in Third Person (Dawning 2017) | 1080p, 53,1/s | glitch | Rückstoß von außen |
| D-HD, D-ZS | [`gABu34ErU88`](https://www.youtube.com/watch?v=gABu34ErU88), [`cGCwARvHGX0`](https://www.youtube.com/watch?v=cGCwARvHGX0) | xHOUNDISHx \| 24.12.2017 \| THIRD PERSON GUN GLITCH; Zer0 SP \| 16.01.2021 \| Weird Walking Animation | 1080p, 59,2/s; 59,9/s | glitch; retail (Ego) | Dauerfeuer [O]; Fehlerbild [O] |
| <a id="a-q-shiro"></a>**G-ST** | [`I7pTinIl0vg`](https://www.youtube.com/watch?v=I7pTinIl0vg) | Shiro Tsuki \| 01.02.2020 \| Gears of War 4 vs Gears 5 - Movement comparison | 1080p, 59,659/s Container, echt 56–57/s | retail (geteiltes Bild) | Gehen, Roadie Run, Rolle |
| <a id="a-q-pcgv"></a>**G-PC** | [`LoG8BimP61E`](https://www.youtube.com/watch?v=LoG8BimP61E) | PC Gaming Videos \| 13.09.2019 \| GEARS 5 ALL Weapons & Reload Animations Showcase | 1080p, 56–58/s | showcase | Lancer-Nachladen |
| G-WG | [`-KCBlBbeSO4`](https://www.youtube.com/watch?v=-KCBlBbeSO4) | Weapons From Games \| 06.09.2019 \| GEARS 5 - All Weapons | 1080p, 51–55/s | showcase | Gnasher-Schuss |
| <a id="a-q-silverhound"></a>**V-DS** | [`NOeeQJrEbDk`](https://www.youtube.com/watch?v=NOeeQJrEbDk) | Dan Silverhound \| 26.06.2019 \| Gunslinger / Bullfighter Weapon Swap Fun | 1080p, 50–59/s | retail | Wechsel, Rolle |
| V-SL, V-DR, V-MB | [`Pi1-s4NYdOk`](https://www.youtube.com/watch?v=Pi1-s4NYdOk), [`W4bsMcsp_P0`](https://www.youtube.com/watch?v=W4bsMcsp_P0), [`vHMvNFzeC0g`](https://www.youtube.com/watch?v=vHMvNFzeC0g) | Slash2x \| 09.03.2019 (Open Beta); Dod-Regnbue \| 21.10.2023; Microwaved Banana Split \| 31.03.2019 | **10–26/s**; bis 14/s; 11–40/s | retail | nur Form bzw. nicht gemessen |

**Takt ohne Fußaufsatz:** Wo Füße unter dem Bildrand, unter Roben oder in Bewegungsunschärfe liegen, ist der Takt der Abstand **gleicher
Posen** (feste Figurvorlage bzw. Selbstähnlichkeit des Figurenausschnitts, ±1 Bild) mit einer zweiten Spur zur Gegenprobe (Farbmaske,
Kopf-Tiefpunkte); ein voller Zyklus wird von der halben Periode (Spiegelpose) über die Ähnlichkeitshöhe getrennt. **Abschnitte** wurden
per Bildvergleich gegen die 144p-Gesamtkopie verortet (Taskinoz +1088,000 / +655,000 s, ±0,033 s – kein Versatz wie in
[nahkampf.md › 10](nahkampf.md#10-offen-und-nicht-messbar)).

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

### 2.1 Gang von außen – REF 0.33

Quellen in [1.1](#11-quellen-ref-033-youtube-mac). Schritte/s = 2 ÷ Zyklusdauer; „Pose“ = Takt aus Posengleichheit, nicht aus Fußaufsätzen.

| Vorgang | Quelle, Zeit (Bilder) | Messung |
|---|---|---|
| **Laufen, leicht (Warframe, Standardset)** [M] <a id="a-g-wf-lauf"></a> | W-UC, 1,133–3,233 s (f68 → f194) | Pose gleich **f68, f100, f131, f162, f194** (Figurenausschnitt, NCC gegen f100) → **4 Zyklen, 31,5 Bilder je Zyklus (0,525 s) = 3,81 Schritte/s**; Spiegelpose dazwischen (f82/113/145/177). Von hinten, Füße unter dem Bildrand → keine Fußaufsätze; Rückenhub nur [O] ≈ 3,5–4 pp H, zwei je Zyklus (NCC 0,50). Normaltempo offen (Video geschnitten, Standbild 7,4–8,3 s) |
| Sprint, leicht (Warframe) [M, vorläufig] <a id="a-g-wf-sprint"></a> | W-UC, f260 → f348 | Pose gleich f260, 289, 319, 348 → **3 Zyklen, 29,3 Bilder = 4,09 Schritte/s**; zwischen zwei Überblendungen. Stärker vorgeneigt, Arme angewinkelt hinter dem Körper [O] |
| Schleichgang geduckt, leicht (Warframe) [M, vorläufig] | W-UC, f527 → f626 | Pose gleich f527, 560, 593, 626 → **3 Zyklen, 33,0 Bilder = 3,64 Schritte/s**; Füße sichtbar, Aufsatz bei mitlaufender Kamera nur grob (rechts ≈ f536, links ≈ f553) [O] |
| **Harte Landung nach langem Fall (Warframe)** [M] <a id="a-g-wf-landung"></a> | W-UC, f2024 → f2084 | **Aufsatz f2024 ±2** (Draufsicht), tiefe Hocke ab f2028 (+4), gehalten bis f2074, Aufrichten f2075–2083 (9 Bilder), ruhig ab f2084 → **Aufsatz bis Ruhe 60 Bilder (1,00 s)**; Landung mit Abrollen ≈ 0,7 s bis aufrecht [O] |
| **Gehen, schwer gepanzert (Gears 5, Kait)** [M] <a id="a-g-gears-gehen"></a> | G-ST, n 70–420 (Gears-5-Hälfte) | Kopf-Tiefpunkte n 82, 103, 122, …, 281 (10 Schritte in 199 Bildern) und Seitenmaxima der blauen Handschuhmarke n 78, 120, 160, …, 398 (**8 Zyklen, 40,0 Bilder = 0,670 s**) → **3,00 Schritte/s** (Container 59,659/s); Gears 4 dieselbe Figur **3,01 Schritte/s**. Amplitude verworfen (Kopfvorlage NCC-Median 0,79), Füße unter dem Bildrand. Normaltempo offen |
| Roadie Run (Gears 5) [M, vorläufig] <a id="a-g-gears-roadie"></a> | G-ST, n 740–1130 | Feste Vorlage auf dem Lancer am Rücken: Bildgleich-Maxima n 756 … 1128 → **13 Zyklen, 28,6 Bilder (0,480 s) = 4,17 Schritte/s**; Seitenmaxima bestätigen (28,8). Vorläufig, weil die NCC zwischen den Maxima auf 0,53–0,6 fällt; Füße unscharf |
| **Ausweichrolle bis Anschlag (Gears 5 / Division 2)** [M] <a id="a-g-rolle"></a> | G-ST n 2250–2320; V-DS n 2518–2556 | Gears: erste Bewegung n 2250 → **Schulter am Boden +21 Bilder** → Hocke mit Waffe im Anschlag **+46 Bilder (0,77 s)** → erster Schuss +70 (Spielereingabe). Division: **+22 Bilder** bis Boden, **+38 Bilder (0,63 s)** bis Hocke hinter der Kiste (ohne Anschlag) |
| Lauf von hinten, Warlock (Destiny 2, Glitch) [M, vorläufig] <a id="a-g-d2-lauf"></a> | D-JV, f12760–f12900 | Robe verdeckt die Beine → Takt über die Silhouettenhöhe: Hochpunkte f12763, 12784, 12805, 12821, 12839, 12857, 12873 → 18,3 Bilder je Schritt ≈ **3,3 Schritte/s**; seitliche Lage des Unterkörpers wiederholt sich alle 37 Bilder (r = 0,41) → **3,2 Schritte/s**; nur 3–3,8 Zyklen, Lauf/Sprint nicht trennbar. Figur 15–23 % H, läuft vom Betrachter weg. **Normaltempo belegt:** HUD-Countdown: Übergang auf 0:35 bei f11840, auf 0:18 bei f12842 → 17 Spielsekunden in 1002 Bildern (58,9 Bilder je Spielsekunde) |
| Gleiten (Destiny 2, Warlock, Glitch) [O] | D-JV, f12576–12636, f12905–12946 | Figur schwebt mit hängenden Beinen, Silhouette sinkt langsam; Absprung und Landung nicht getrennt |
| Pilot und Titan (Titanfall 2) [O] <a id="a-g-tf"></a> | T-FG1 13–15,5 s, 97–101 s, 1126–1133 s; T-FG2; T-TK 655–715 s, 1088–1148 s; T-GO | **Keine Gangzahl:** Pilot nur von hinten auf dunklem Gitterrost (Kopfvorlage NCC meist < 0,85), Titan mit Füßen unter dem Bildrand oder unter Rauch/HUD; T-FG2 nur 17–54/s; Taskinoz-Abschnitte 27–55/s, BT steht 5–34 s und kämpft danach, Pilot springt nach 2,4 s in Parkour; T-GO zeigt BT nur in Nahsicht. Normaltempo der Taskinoz-Abschnitte per Speedrun-Timer belegt (50,000 s Timer in 50,000 s Video) |
| Necramech (Warframe) [O] | W-NM 0–18,5 s; W-VR ganz | 29/s und bewegungsunscharf, kein Takt; Voidrig-Video: Mech nie zu Fuß (nur Arsenal ≈ 786 s), 182 Schnitte |

**Muster 2.1 (Beobachtung):** (1) Der Takt steigt mit dem Tempo **wenig**: Warframe Schleichen 3,64 → Laufen 3,81 → Sprint 4,09 Schritte/s,
Gears Gehen 3,00 → Roadie Run 4,17 – Tempo kommt vor allem über die Schrittlänge (nicht gemessen) und die Haltung (Vorlage, Arme hinten).
(2) Die schwer gepanzerte Gears-Figur geht mit 3,0 Schritten/s – nicht langsam im Takt; das Gewicht liegt in Haltung, Rolle (Boden nach 21 Bildern,
Anschlag nach 46) und Landung, wie in 0.32 beim Titan. (3) Der Warframe-Gehtakt aus 0.32 (1,72 Schritte/s, [Gehen](#a-wf-gehen)) ist ein
anderer Vorgang (Gehen im Devstream) und bleibt vorläufig; Laufen außen (3,81) liegt nahe am Ego-Sprint-Wippen von Destiny (3,16 Hz vertikal
= ein Ausschlag je Schritt) – verschiedene Spiele und Vorgänge, nicht gleichsetzen.

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

### 3.4 Feuern, Nachladen und Wechsel von außen – REF 0.33

Marker wie in [nachladen.md](nachladen.md#2-messtabelle): erste Bewegung → Waffe wieder in der Ausgangslage („Anschlag“) → ruhig; HUD-Ereignisse
getrennt genannt. Quellen in [1.1](#11-quellen-ref-033-youtube-mac).

| Vorgang | Quelle, Zeit (Bilder) | Messung |
|---|---|---|
| **Nachladen R-201 von außen (Titanfall 2)** [M] <a id="a-r-tf-r201"></a> | T-ER, n 370 → 505 (6,167–8,417 s), 60/s | Waffe kippt ab **n 370** (davor ruhig), wieder in Ausgangslage **n 498 ±2 → 128 Bilder (2,13 s)**, ruhig n 505 ±3 (135 Bilder). Ablauf [O]: Mündung kippt nach außen-oben, linke Hand zweimal zur Hüfte (n ≈ 414–423, 474–490), Rumpf und Beine stehen. Figur ≈ 49 % H. Normaltempo nicht belegt |
| **Nachladen Lancer von außen (Gears 5)** [M] <a id="a-r-gears-lancer"></a> | G-PC, n 7414 → 7560 (123,69–126,13 s) | erste Bewegung **n 7414 ±2** → ruhig in Hüftbereitschaft **n 7560 ±2: 146 Bilder (2,44 s)**; Ablauf: Waffe steil vor die Schulter, linke Hand hinter den Rücken (n 7428–7456), Waffe senkrecht, flach gedreht, zurück. **HUD:** Active-Reload-Leiste n 7411–7532, Magazinbalken voll zwischen n 7541 und 7548 – **0,2–0,3 s vor „ruhig“** (wie in [LESSONS](LESSONS.md): HUD vor Körper). Feuerrate am Zähler 7,2 Schuss/s (Prüfgröße, Sollwert offen) |
| **Wechsel Gewehr → Revolver (Division 2)** [M, Untergrenze] <a id="a-r-dv-wechsel"></a> | V-DS, n 2925 → 2947 (48,80–49,17 s), echt 53/s | Langwaffe schwingt ab **n 2925** ab, Revolver in der Hand n 2937 (12 Bilder), **Arm im Anschlag n 2943 (18 Bilder, 0,30 s)**, ruhig n 2947 (22 Bilder); Hüftschuss dazwischen n 2941. Anfang beim Verlassen der Deckung evtl. verdeckt → Untergrenze, ±2 Bilder |
| **Schuss Gnasher (Gears 5, JD): Kamera und Waffe** [M] <a id="a-r-gears-gnasher"></a> | G-WG, n 10630 → 10686 (177,17–178,10 s), echt ≈ 51/s | Zwei Weltanker (Kran, Geländer): Welt springt **≥ 7,6 pp H nach unten** (Kamera nickt hoch; n 10631–10641 verworfen, NCC < 0,85), Rücklauf monoton ohne Überschwingen, **ruhig ab n 10680 (50 Bilder)**, Endlage = Ausgangslage (Δ 0,04 pp). Waffe wechselt beim Pumpen die Form (NCC 0,2–0,4) → Ausschlag nicht messbar; **Waffe zurück in Ausgangspose n 10685 (55 Bilder)**. Zeiten Medienzeit (Wiederholbilder) |
| **Rückstoß von außen, Einzelschüsse (Destiny 2, Glitch)** [M] Lage, [O] Zeiten <a id="a-r-d2-kick"></a> | D-IGN, Schüsse f3618, 3762, 3872, 3957, 4056 | Warlock mit dem Rücken zur Kamera (KH ≈ 39 % H), Waffe in Glitch-Haltung senkrecht auf der Schulter. **Kamerakick:** Welt springt je Schuss **2,4–3,5 pp H** nach unten (Spind 2,4–2,6, Deckenpaneel 3,5 – Orbit-Kamera mit Parallaxe, daher Spanne), **Spitze +6–7 Bilder**, zurück nach **28–39 Bildern**. **Figur gegen Welt:** Rücken steigt 1,27–1,34 pp H nach oben (≈ 0,033 KH) und rückt 0,6–0,85 pp B nach rechts, Spitze +5–7, Ruhe nach 28–34 Bildern (drei Schüsse mit NCC ≥ 0,85). Waffe/Hand verworfen (Mündungsblitz, NCC 0,35–0,8). Echte Rate 53/s, Normaltempo nicht belegt |
| Dauerfeuer von außen (Destiny 2, Glitch) [O] | D-HD f6600–6647; D-IGN f4113–4133 | Leuchtspuren alle 5–7 Bilder (≈ 9–10 Schuss/s), Waffe hoch vor der rechten Schulter; Normaltempo in D-HD per HUD belegt (12 s in 716 Bildern). D-IGN: Magazin 39 → 34 in 5 Containerbildern je Schuss |
| Zielen und Haltung (Gears 5, Warframe, Division Open Beta) [O]/[M Lage] | G-PC f7313, f250; W-DB f719; V-SL f3960 | Gears-Schulterkamera: Figur 22–48 % B, Kopfoberkante 53–55 % H, zweite Langwaffe senkrecht am Rücken; Warframe Primär waagrecht in Schulterhöhe (Arsenal); Division-Agent frontal, Gewehr senkrecht vor der Brust beim Nachladen |

**Muster 3.4 (Beobachtung):** (1) **Nachladen von außen ist ein Arm- und Waffenvorgang:** Rumpf und Beine bleiben stehen (R-201, Lancer);
R-201 128 Bilder (2,13 s) bis zur Ausgangslage (135 bis ruhig), Lancer 146 Bilder (2,44 s) bis ruhig in Hüftbereitschaft –
zwei Sturmgewehre, Endmarker verschieden. (2) **Rückstoß liest sich von außen vor allem als Kamerakick**, der Körper bewegt
sich wenig (Destiny ≈ 0,03 KH); Gnasher (Schrot) kickt die Kamera mindestens doppelt so weit wie die Destiny-Kinetikwaffe (≥ 7,6 gegen 2,4–3,5 pp) – zwei Beispiele,
keine Klassenwerte. (3) **Aim-Offset als Gierwinkel** (Beine quer, Oberkörper zum Ziel) kommt in keinem der 20 Videos vor; die gemessenen
Figuren schießen mit Beinen und Brust in Schussrichtung oder in Glitch-Haltung ([7](#7-offen-und-nicht-messbar)).

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

**Ergänzt in 0.33 ([2.1](#21-gang-von-außen--ref-033), [3.4](#34-feuern-nachladen-und-wechsel-von-außen--ref-033)):**
- **Destiny 2:** Glitch-Kamera zeigt den Warlock von hinten mit ≈ 3,2–3,3 Schritten/s (vorläufig) und die Primärwaffe **auf der Schulter wie eine
  schwere** – Glitch-Haltung, nicht als Retail übernehmen; Rückstoß von außen = Kamerakick 2,4–3,5 pp, Körper ≈ 0,03 KH. Die Klasse ist in allen
  Glitch-Quellen Warlock (der Glitch setzt ihn voraus), die Rasse bleibt unter dem Helm unbestimmt – ein Exo ist nicht belegt.
- **Titanfall 2:** Nachladen von außen 128 Bilder (R-201); Third-Person-Videos sind Northstar-Mods; Pilot- und Titan-Gang nicht messbar.
- **Warframe:** Laufen 3,81, Sprint 4,09 (vorläufig), Schleichen 3,64 Schritte/s; harte Landung 1,00 s bis Ruhe; Necramech-Gang ohne 60/s-Quelle.
- **The Division 2:** Wechsel Gewehr → Revolver ≥ 18 Bilder bis Anschlag; Ausweichrolle 22 Bilder bis Boden, 38 bis Hocke.
- **Gears 5:** Gehen 3,00 Schritte/s (8 Zyklen), Roadie Run 4,17 (vorläufig), Rolle 21/46 Bilder, Lancer-Nachladen 146 Bilder, Gnasher-Kamerakick ≥ 7,6 pp.

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

**Neue Belege 0.33 zu dieser Tabelle** (keine neuen Spielerstimmen – die neuen Zahlen ändern keine Bewertung, sie belegen sie):
Warframe „Laufanimation transportiert Tempo“ (P16) – gemessen steigt der Takt vom Laufen zum Sprint nur um 7 % (3,81 → 4,09, [Sprint](#a-g-wf-sprint)),
das Tempo kommt also über Haltung und Schrittlänge [M]/Einschätzung. Gears „Gewicht über Impuls“ (B11) – die Rolle braucht 46 Bilder bis zum
Anschlag gegen 38 Bilder ohne Anschlag in Division ([Rolle](#a-g-rolle)) [M]. Destiny „nur eine Waffe sichtbar“ (Q1, Q2, Q4) – die
Glitch-Ansicht legt auch die Primärwaffe beim Laufen auf die Schulter ([Lauf](#a-g-d2-lauf)); das ist ein Kamerafehler, kein Retail-Beleg.

### E2 – Lehren für Critic (Vorschlag, dort entscheiden)

- **Übernehmen:** Gewicht über **Ereignisse und Übergänge** statt über langsames Grundtempo – Titan-Aufsatz in tiefer Hocke (8 Bilder Fall,
  [Landung](#a-tf-landung)), Impuls beim Stopp (B11), Inertialization (B4); Titanfall beschleunigte nach Kritik (B8–B10).
- **Übernehmen:** Ruhe als **lange Schleife mit sehr kleinem Atemhub** (≈ 0,01 KH; Titanfall 18 s, Warframe-Rhino ≈ 2 s Atemperiode, vorläufig) und
  Leben über Kopf- und Gewichtswechsel ([Leerlauf](#a-tf-leerlauf), [Atmen](#a-wf-atmen)).
- **Übernehmen:** Schrittlänge an die zurückgelegte Strecke koppeln (B2 GDC 2014: Fuß rutscht nie), damit Füße bei der Isometrie-Kamera nicht gleiten.
- **Vermeiden:** einen Ruhestil, den die Bewegung nicht fortsetzt (Warframe-„Zurückschnappen“, P12–P15); feste Zwangspausen schwerer Figuren
  ohne Abbruch (Necramech, P19, B13).
- **Testen (Stand 0.32, durch den Punkt „Testen (0.33)“ ersetzt):** Gangtakt leicht ≈ 1,7 Schritte/s ([Warframe](#a-wf-gehen), vorläufig) als Startwert, schwer langsamer – Zahl für schwer fehlte
  ([7](#7-offen-und-nicht-messbar)); Wende mit Anschlag ≈ 9–12 Bilder ([Division](#a-dv-wende)).
- **Testen (0.33):** Laufen ≈ 3,8 Schritte/s, Sprint ≈ 4,1 (vorläufig) als Startwerte für eine leichte Figur ([Warframe](#a-g-wf-lauf)); für eine
  schwere Figur **nicht** langsamer takten, sondern Gehen ≈ 3,0 Schritte/s wie die schwer gepanzerte Gears-Figur ([Gears](#a-g-gears-gehen)) und
  Gewicht über Rolle/Landung zeigen (Rolle bis Anschlag 46 Bilder, harte Landung 1,0 s bis Ruhe, [Rolle](#a-g-rolle), [Landung](#a-g-wf-landung)).
  Schrittlänge und Hub fehlen weiter – an der eigenen Isometrie-Kamera aus der Strecke ableiten (B2).

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
- **Testen (0.33):** Nachladen von außen als reiner Arm-/Waffenvorgang (Rumpf und Beine stehen) mit R-201 2,13 s bis zur Ausgangslage bzw. Lancer 2,44 s bis ruhig an je einem
  Sturmgewehr ([R-201](#a-r-tf-r201), [Lancer](#a-r-gears-lancer)); Wechsel ≥ 18 Bilder bis Anschlag ([Division](#a-r-dv-wechsel)). Rückstoß von
  außen zeigt sich vor allem in der Kamera – am Körper reicht ein kleiner Ausschlag (≈ 0,03 KH, [Kick](#a-r-d2-kick)).

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

**Stand nach REF 0.33 „Gaitline“** (die Punkte darunter sind der Stand 0.32 und bleiben als Begründung stehen):
- **Erledigt:** Schrittfrequenz nach der 4-Zyklen-Regel für Warframe (Laufen) und Gears 5 (Gehen) ([2.1](#21-gang-von-außen--ref-033));
  Nachladen, Wechsel und Feuern mit Rückstoß von außen je mit mindestens einem Beispiel ([3.4](#34-feuern-nachladen-und-wechsel-von-außen--ref-033)).
- **Teilweise:** Sprint/Roadie Run, Schleichen und Destiny-Lauf nur vorläufig bzw. mit verworfener Amplitude; Landung (Warframe) und Rolle
  (Gears, Division) gemessen, Sprung mit Absprung und Fallen zu Fuß nicht.
- **Weiter offen, mit Grund – nicht mit denselben Quellen wiederholen:**
  - **Fußaufsatz ±1 Bild, Schrittlänge und Hub/Pendeln in KH, Start/Stopp, Drehen auf der Stelle:** keine der 20 Quellen zeigt eine ganze
    Figur quer zur Kamera bei echten 60/s (Füße unter dem Bildrand: W-UC, G-ST; Robe: D-JV; Gitterrost/Rauch: T-FG1; Schnitte: W-UC, W-VR).
    Kandidat: Gears „Wall cover walk“ (G-ST n ≈ 1200–1640, Seitschritt vor einer Wand als Weltanker) – nur Seitschritt, kein Vorwärtsgang.
  - **Pilot ↔ Titan, Warframe ↔ Necramech im Gang:** T-FG1/T-FG2/T-TK/T-GO und W-NM/W-VR geprüft, kein Titan- oder Mech-Gang über ≥ 4 Zyklen;
    T-TK-Abschnitte und T-FG2 haben nur 17–55 echte Bilder/s. Weg: eigener Mitschnitt mit fester Seitenkamera (Antwort C zu [S1](#frage-s1))
    oder eine Northstar-Seitenkamera bei echten 60/s.
  - **Aim-Offset als Gierwinkel:** in keinem der 20 Videos (Division-Kandidaten V-SL nur 10–26/s, V-DR Figur am Bildrand; Destiny-Glitch
    entkoppelt Waffe und Ziel).
  - **Erkennbarkeit der Waffenklasse in mehreren Abständen:** alle Showcases zeigen die Figur in fester Nahkamera.
  - **Normaltempo** für Warframe- und Gears-Showcases nicht belegt (keine Uhr, kein Ton im Videostream); belegt nur Destiny D-JV/D-HD (HUD)
    und Taskinoz (Speedrun-Timer).
  - Destiny-Hüter von außen nach **Klasse und Rasse**: Klasse in allen Glitch-Quellen Warlock (die Third-Person-Glitches setzen ihn voraus),
    Rasse unter dem Helm unbestimmt – Titan, Jäger und ein sicher erkennbarer Exo fehlen.

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

**Prüfung REF 0.33 „Gaitline“ (30.10.2026):**
- **Unteragenten:** vier Messagenten (Warframe, Titanfall 2, Destiny 2, Gears 5/Division 2; Opus, high), je eigener Ordner unter
  `~/Library/Caches/CubeEscape/reference/aussenansicht-gang/`; keiner schrieb ins Repo oder lud selbst – ein Lader für alle Downloads
  (nacheinander; ein kurzer Doppelabruf von etwa 2 min beim Neustart, danach getrennt), Abschnitte über eine Warteschlange.
- **Nachmessung durch den Koordinator: 8 Zahlen, 8 bestätigt** (eigene Spuren oder Bögen, nicht die CSV der Agenten): Warframe-Laufen
  (Selbstähnlichkeit: f68/100/131/162/193 → 3,84 gegen 3,81 Schritte/s), Warframe-Landung (Aufsatz f2024–2026, Ruhe ≈ f2084), Destiny-Countdown
  (0:35 ab **f11840** statt f11838 – übernommen 1002 statt 1004 Bilder, Normaltempo ±2 %), Destiny-Kamerakick (eigener Anker Deckenpaneel:
  Spitze +6, Ruhe ≈ 35 Bilder; Betrag 3,5 statt 2,4–2,6 pp → als Spanne übernommen), Gears-Gehen (eigene Handschuh-Farbmaske: 8 Zyklen,
  39,9 Bilder → 2,99 Schritte/s), Lancer-Nachladen (f7413–7414 → f7560–7562), Gears-Rolle (2250/2271/2296 im Rahmen ±3), R-201-Nachladen
  (n 370–371 → 495–498). **Korrigiert 2** (Destiny-Marker, Kick-Betrag als Spanne), **nicht übernommen:** Statusangaben „nicht messbar“ als
  Messwert (als [O] mit Grund geführt), Zeiten aus Quellen unter ≈ 50 echten Bildern/s (nur Form).
- **Quellen:** 19 Kandidaten-IDs plus eine eigene Suche (Necramech: `GvseUKgOreM`; `btEXSl9CcyY`, `2SpdpXuBd4o` nur 30/s, verworfen), alle per
  yt-dlp geprüft; Kanal, Datum, Titel in [1.1](#11-quellen-ref-033-youtube-mac). Keine neuen Spieler- oder Fachquellen (Standard › 4: nur zu neuen
  Bewertungsbefunden; die neuen Zahlen belegen bestehende).
- **Zählung:** 5 Spiele (plus Gears of War 4 als Vergleichsseite), 20 Videos geprüft, 10 davon gemessen; 35 neue JSON-Einträge (body_motion
  23: 11 [M], 12 [O]; weapon_body 12: 6 [M] bzw. [M/O], 6 [O]); Gangtakt nach 4-Zyklen-Regel in 2 Spielen, vorläufig in 3 weiteren Vorgängen.
