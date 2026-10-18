# Metroid Prime – Referenz für Armkanone und Visor

Bildbeobachtungen und Messungen vom 18. Oktober 2026; **Originalfamilie, Originalgrafik mit Randomizer und Remastered werden getrennt**.
[M] = am Bild gemessen, [O] = begrenzte Beobachtung. Keine Zahlen werden als Mittelwert über Editionen oder Waffenformen behandelt.
Die zugehörigen Quellen- und Zeitstempel-Einträge gehören in [data/clips.json](../data/clips.json).

## 1. Quellen

- **BashPrime / Originalfamilie:** [Kanal](https://twitch.tv/bashprime), unter anderem „What the f*** is a toad“ vom **26.10.2018**.
  Das Aufnahmedatum liegt vor Remastered; klassisches HUD und das eingebettete 4:3-Spielbild passen zur ursprünglichen Fassung.
  **GameCube-Version, Wii-Trilogy-Port, Emulator und konkrete Revision sind aus diesen Bildern nicht sicher unterscheidbar.**
  „Originalfamilie“ benennt diese Grenze ausdrücklich, nicht eine nachgewiesene Hardware.
- **BashPrime / Originalgrafik mit Randomizer:** Aufnahmen aus 2023 zeigen dasselbe klassische HUD und ein sichtbares
  Randomizer-/Inventaroverlay. Die beiden Ladebelege aus „bash "two missile refills" prime“ gehören nur zu diesem Aufnahmezustand;
  Einstellungen und mögliche Modifikationen der Spielparameter sind unbekannt. Der Beamname ist dort nicht lesbar;
  die Messungen benennen deshalb die gelbe Ladeform, ohne sie allein aus Farbe/Form sicher einem Beam zuzuordnen.
- **Vinesauce / Metroid Prime Remastered:** [Kanal](https://twitch.tv/vinesauce), Clips vom Februar/März 2023 mit
  Twitch-Kategorie „Metroid Prime Remastered“, vollständigem 16:9-Spielbild, detaillierter Kanone und dem entsprechenden Visor-HUD.
  Der Ice-Beam- beziehungsweise Wave-Beam-Name erscheint in den gemessenen Bildern. Ein Bildausschnitt mit bloß gleicher Kategorie
  genügt nicht: drei so kategorisierte Clips zeigen tatsächlich fremde Einspieler/Startbilder und bleiben reine Screening-Einträge.
- **Typbeleg:** Das geschlossene Rohr führt direkt in den rechten gepanzerten Arm; in der Originalfassung wird kein lesbarer
  Beamname behauptet. In Remastered zeigen die vermessenen Bilder explizit „Ice Beam“ beziehungsweise „Wave Beam“ im HUD.
- Quelle ist jeweils der **Broadcaster (`channel`/Kanal-URL)** aus den Clip-Metadaten, nicht der Clip-Ersteller (`uploader`).
  Datum ist `upload_date`. Die Links und Daten jeder tatsächlich gesichteten Aufnahme stehen im Screeninglog unten.

## 2. Methode und Messungen – [M]

Ablauf entsprechend [Destiny 2, Abschnitt 2](destiny2.md#2-messungen-an-60-fps-aufnahmen-ab-16-oktober-2026--m):
`tools/reference_frames.py list`, `fetch`, vollständige `overview` mit 2 Bildern/s, Suche mit `sheet --fps 10`,
danach native Originalbilder über `measure --fps native --cross`; Einzelbilder mit 10-%-Raster für Lageangaben.
**Alle 16 tatsächlich gesichteten Clips haben eine native Streamrate von 60 Bildern/s.** Die Messmarker haben ±1 Bild
(16,7 ms), Lageangaben ±3 Prozentpunkte. Angaben wie „Haltung erreicht“ beschreiben den sichtbaren Zustand, keine Spielbereitschaft.

Bei BashPrime belegt das Spiel nur einen Teil des Streambildes. Deshalb beziehen sich Lage und Mittenkreuz auf die ausgeschnittene
**Spielfläche**, nicht auf Facecam/Overlay: 2018er Layout `(x=418, y=10, Breite=852, Höhe=640)`, 2023er Layout
`(398, 8, 1130, 848)`. Die Crops behalten die Framezahl; die MP4-Zeitquantisierung weicht gegenüber den Original-PTS um weniger als
1 ms ab. Die Tabellenmarker wurden über den gleichen Frameindex auf die Original-PTS zurückgeführt und auf Millisekunden gerundet.
Vinesauce zeigt die Spielfläche vollständig bei 1920 × 1080. Ursprung oben links; Lage `x / y` in Prozent Breite/Höhe.

**Grenzen:** Kein sichtbares Eingabelog, also kein Tastendruckzeitpunkt und keine Inputlatenz. „Ladezeit“ meint ausschließlich
vom ersten sichtbaren Ladezeichen bis zur definierten vollen Ladehülle. Ein Beamwechsel kann ebenfalls eine orange Ringwelle erzeugen;
HUD-Name, folgende Waffenform und Schussfarbe werden zur Zuordnung mitgeprüft. Streamer-FOV und Maßstab sind unbekannt;
keine Weltmeter, Geschwindigkeiten in m/s oder Blickfeldgrade. Kamerarollen, Fortbewegung und Waffenanimation werden nicht ohne
separaten Beleg als Sway, Bob oder Landung aufgeteilt. Für **saubere Geh-/Sprint-Bob-Hz, eine eigene Sprinthaltung, isolierten Absprung
und Landungsrückkehr sowie einen räumlichen Lock-on-Fadenkreuzsprung** fehlt in dieser Auswahl ein eindeutiger Ablauf.
Das ist eine Lücke dieser Aufnahmen, kein Nachweis fehlender Spielmechaniken. 2-fps-Screening kann kurze Vorgänge übersehen.

Clips, Crops, Raster und native Kontaktbögen liegen ausschließlich außerhalb des Repos im Sitzungs-Scratch
`/tmp/ce-tool-references/metroidprime/`; die Pfadzuordnung steht dort in `evidence.json`, Bildlisten in den `*-pts.csv`, die Zuordnung zu Original-PTS
in `frame-map.json`. Medien werden nicht ins Repository übernommen.

| Vorgang | Clip (Twitch, Kanal, Datum) | Zeitstempel im Clip | Messung |
|---|---|---|---|
| **Armkanone: Hüftlage und Umsehen (Originalfamilie)** | `https://twitch.tv/bashprime/clip/ObedientImpartialDiscDuDudu` (BashPrime, 26.10.2018, Originalfamilie) | Lage 2,950 s; Umsehen 0,000–1,000 s | Armkanonenform mit weißem Überzug (Beamname im Originalbeleg nicht lesbar): Körper etwa **53–100 % Breite × 64–100 % Höhe**, Mündungsbereich etwa **61 / 66**. Die Waffe steigt von unten rechts schräg zur Mitte auf; der rechte Arm geht in das geschlossene Rohr über, eine separate Griffhand ist nicht sichtbar. Beim Umsehen bleibt sie rechts unten; kein großer seitlicher Ausschlag wie eine Verlagerung bis zur Bildmitte. Lage relativ zur ausgeschnittenen Spielfläche, ±3 Prozentpunkte. |
| **Combat Visor → Scan Visor (Originalfamilie)** | `https://twitch.tv/bashprime/clip/ObedientImpartialDiscDuDudu` (BashPrime, 26.10.2018, Originalfamilie) | Senken ab 1,100 s → Kanone weg 1,251 s → erste Scanrahmenlinien 1,317 s | **9 Bilder (0,15 s)** vom ersten Senken bis zur vollständig verdeckten Armkanone; **13 Bilder (0,22 s)** bis zu den ersten Scanrahmenlinien. Die Kanone fällt nach unten rechts; das Kampf-HUD verschwindet mit ihr. Danach erscheinen die rechteckigen Scan-Ecken in der freien Sicht. Dies sind sichtbare Animationsmarker, keine Eingabe- oder Scanbereitschaftszeit. |
| **Scan Visor → Combat Visor (Originalfamilie)** | `https://twitch.tv/bashprime/clip/ObedientImpartialDiscDuDudu` (BashPrime, 26.10.2018, Originalfamilie) | Scanrahmen blendet aus ab 2,417 s → Kanone erscheint 2,567 s → untere rechte Haltung 2,834 s | **9 Bilder (0,15 s)** bis zum Wiedererscheinen der Kanone; danach **16 Bilder (0,27 s)** bis zur wieder erreichten unteren rechten Haltung, insgesamt **25 Bilder (0,42 s)**. Das Kampf-HUD baut sich parallel auf. Die Kanone kommt von unten rechts; kein separates Vorhalten einer Hand in der Scanansicht. |
| **Armkanone: sichtbares Laden bis volle Ladehülle (Originalgrafik, Randomizer)** | `https://twitch.tv/bashprime/clip/AcceptableConsiderateCurryMrDestructoid-0qnhH00QAshA7yZr` (BashPrime, 30.08.2023, Originalgrafik, Randomizer) | erstes Aufleuchten 18,600 s → volle äußere Ladehülle 19,217 s → gehalten bis 20,267 s → Entladen 20,284 s | **37 Bilder (0,62 s)** vom ersten sichtbaren Aufleuchten der Kanonenlinien bis zur voll ausgebildeten äußeren Kugelhülle. Zuerst glühen die Längsstreifen und die Rohrkante; vor der Mündung wächst ein orangegelber Ring zu einer Kugelhülle mit kreisenden Partikeln. Der volle Zustand wird noch etwa **1,05 s** sichtbar gehalten. Beim Entladen verschwindet die Hülle in einem Bild; der gelbe Schuss läuft von rechts unten nach vorn. **Keine Gesamtladezeit ab Tastendruck**: ein eventuell vorausgehender unsichtbarer Anteil ist unbekannt. Der Randomizer-Zustand ist kein Beleg für unveränderte Spielparameter. |
| **Armkanone: linke Hand in der Ladehaltung (Originalgrafik, Randomizer)** | `https://twitch.tv/bashprime/clip/AcceptableConsiderateCurryMrDestructoid-0qnhH00QAshA7yZr` (BashPrime, 30.08.2023, Originalgrafik, Randomizer) | Hand erscheint 19,367 s → Haltepose 19,567 s; Rückzug 20,150–20,284 s | Nach Erreichen der Ladehülle kommt die **linke Hand von unten links**, Finger nach oben rechts zur Kanone; nach **12 Bildern (0,20 s)** liegt sie am oberen linken Teil des Rohres. Hand/Handgelenk etwa **48 / 87**, Fingerspitzen etwa **64 / 84** in der Haltepose. Sie stützt beziehungsweise umfasst das Rohr von links; die rechte Hand bleibt in der Armkanone verborgen. Vor dem Entladen zieht die linke Hand nach unten links zurück. Lage ±3 Prozentpunkte; kein behaupteter Eingabezeitpunkt. |
| **Ice Beam: Hüftlage (Remastered)** | `https://twitch.tv/vinesauce/clip/AverageConsideratePorpoiseMingLee-fPTgfwUkaSKAHo1E` (Vinesauce, 23.02.2023, Remastered) | 3,800 s | Körper ungefähr **54–100 % Breite × 62–96 % Höhe**, Mündungsbereich etwa **58 / 65**. Die gepanzerte Armkanone liegt rechts unten; drei gelbe Leuchtstreifen und eine helle schräge Kante führen zur Mündung. Die Waffe wird durch den unteren Visorrahmen angeschnitten. Keine sichtbare linke Stützhand in diesem Moment; kein ADS-Okular. Das kleine freie Zielzeichen liegt um **50 / 50**. Lage ±3 Prozentpunkte. |
| **Lock-on: Aufbau der Zielmarkierungen (Remastered)** | `https://twitch.tv/vinesauce/clip/ClumsyAnnoyingAntMikeHogu-9HFuYjU70tIotSP6` (Vinesauce, 22.02.2023, Remastered) | rote Zielmarkierungen ab 13,551 s → große cyanfarbene Klammern ab 13,617 s; Aufbau beobachtet bis 13,834 s | Die weißen Dreieckmarkierungen am Gegner werden rot; **4 Bilder (0,07 s)** danach beginnen größere cyanfarbene Klammern von außen in einen Ring um das Ziel einzufahren. Der Gegner liegt vor und während des Aufbaus bereits ungefähr bei **50 / 50**. **Ein räumlicher Fadenkreuzsprung ist hier nicht isolierbar**; die Aufnahme belegt den Markerwechsel und die Ringbewegung. Gleichzeitig öffnet sich die Ice-Beam-Mündung zum Schuss; daraus wird keine reine ADS- oder Kamera-Rückstoßzeit abgeleitet. |
| **Power Beam → Wave Beam: sichtbare Umformung (Remastered)** | `https://twitch.tv/vinesauce/clip/WittyCalmPancakeAllenHuhu-ZPrcvCj4z5ODMMNE` (Vinesauce, 17.02.2023, Remastered) | Ringwelle ab 9,234 s → Rohrkörper orange umzeichnet 9,417 s → Wave-Beam-HUD 9,834 s → violetter Schuss 9,917 s | **36 Bilder (0,60 s)** von der ersten sichtbaren Ringwelle bis zum neuen Beam-Namen im HUD. Die orangegelbe Welle läuft über den Rohrkörper, Leuchtlinien zeichnen dessen Form nach; anschließend erscheint die violette Wave-Beam-Kennung und ein violetter Schuss. **Beamwechsel, kein gemessenes Aufladen**: Die erste Welle allein wäre ohne den nachfolgenden HUD-/Schussbeleg mehrdeutig. Die Kanone bleibt rechts unten im Bild. |
| **Armkanone beim Unterwasser-Plattformwechsel (Remastered)** | `https://twitch.tv/vinesauce/clip/ClumsyAnnoyingAntMikeHogu-9HFuYjU70tIotSP6` (Vinesauce, 22.02.2023, Remastered) | 3,000–3,634 s | Während der Blick über den Zwischenraum zur nächsten Plattform schwenkt, bleibt die Ice-Beam-Kanone in der unteren rechten Bildregion sichtbar (Körper ungefähr **54–100 / 62–96 %**). Sie wird nicht in eine getrennte Tragepose gebracht. Blickrollen, räumliche Fortbewegung und Waffenbewegung überlagern sich; **Absprung-, Landungsmarker und Bob-Frequenz lassen sich in diesem Ausschnitt nicht trennen**. Dies ist ein Haltungsbeleg während des Plattformwechsels, keine Messung einer Sprung- oder Landedauer. |

### Screeninglog vom 18.10.2026

**16 Clips aus zwei Kanälen vollständig mit 2 Bildern/s gesichtet**: BashPrime 8, Vinesauce 8. Die Auswahl enthält auch
Ergebnisbilder, Morph Ball, Menüs und fremde Einspieler; diese zählen als Sichtungen, nicht als Ego-Messungen.
Insgesamt wurden 23 Clips geladen; 7 zusätzliche BashPrime-Clips bereits anhand ihrer Metadaten als Prime 2/Dread ausgeschlossen
und **nicht** in diese 16 Sichtungen eingerechnet. Leere Cliplisten bei `zeni`, `zoidy`, `paraxade`, `milessmb`, `clairoen`, `miles`;
`behemoth87` bot in der Liste überwiegend Super-Metroid-Titel. Diese Listen sind ebenfalls keine Sichtungen.
BashPrime wurde über seine Topliste gefunden. Vinesauce wurde über die öffentliche Twitch-Spielkategorie und danach den Broadcaster
gewählt; eine Kategorienzuweisung allein wird nicht als Bildbeleg übernommen.

| Kanal / Datum | Clip / Titel | Rate | Tatsächlich gesichtet / Ergebnis |
|---|---|---|---|
| BashPrime, 13.07.2018 | [How to get completely denied by Metroid Prime](https://twitch.tv/bashprime/clip/InventiveGracefulCroquetteBudStar) | 60 Bilder/s | Schwarzblende, Mission-Final-Ergebnisbild und Reaktion; kein Ego-Spiel. |
| BashPrime, 03.05.2017 | [Metroid Prime Any% attempts](https://twitch.tv/bashprime/clip/EnjoyableSuperMinkSSSsss) | 60 Bilder/s | Überwiegend Morph Ball und Transformationen, sehr kurze Egoansicht um 14 s; keine isolierte Zielaktion vermessen. |
| BashPrime, 26.10.2018 | [What the f*** is a toad](https://twitch.tv/bashprime/clip/ObedientImpartialDiscDuDudu) | 60 Bilder/s | Ego 0–4 s, Combat-/Scan-Visor hin und zurück; danach Morph Ball/Transformationen. Originalfamilie durch Datum vor Remastered belegt. |
| BashPrime, 30.08.2023 | [bash "two missile refills" prime](https://twitch.tv/bashprime/clip/AcceptableConsiderateCurryMrDestructoid-0qnhH00QAshA7yZr) | 60 Bilder/s | Originalgrafik mit Randomizer-Inventaroverlay; mehrere Ladehüllen und Schüsse, Morph Ball dazwischen, spätere Facecam. Lade- und Handhaltung vermessen. |
| BashPrime, 10.05.2023 | [I edge my chat](https://twitch.tv/bashprime/clip/SpeedyFriendlyBunnyBleedPurple-8_nvKEx7QV6EZWpr) | 60 Bilder/s | Originalgrafik mit Inventar-/Randomizerlayout, kurze Ego- und Menüphasen; kein isolierter Ladevorgang vermessen. |
| BashPrime, 08.09.2023 | [Birthday Skip](https://twitch.tv/bashprime/clip/HonorableShakingDillM4xHeh-BeWo8M8JMljjS0po) | 60 Bilder/s | Originalgrafik/Randomizer, Meta-Ridley-Kampf mit Plasmakanone, Karte und Inventar; später Nahkampfgegner. Nicht mit unveränderter Original-Spielkonfiguration gleichgesetzt. |
| BashPrime, 18.10.2018 | [Thardus softlock](https://twitch.tv/bashprime/clip/TentativeVenomousLegDBstyle) | 60 Bilder/s | Originalfamilie: Morph Ball am Anfang, Scan auf Thardus, danach Plasma-Kanone in Egoansicht; Softlock-Kontext, kein normaler Bewegungsablauf. |
| BashPrime, 11.08.2023 | [Moment of Truth](https://twitch.tv/bashprime/clip/CrackyCalmUdonDatBoi-GFXq_bJMWi-oDTjR) | 60 Bilder/s | Originalgrafik/Randomizer: Morph Ball, Scan, Ego-Umsehen vor Pfeiler und Bewegung zur Tür, Inventar. Kurzzeitige Kanonendips bei 8,2/10,3 s geprüft; keine sichere Sprung-/Bob-Zuordnung. |
| Vinesauce, 22.02.2023 | [vinny on jerma chatterz](https://twitch.tv/vinesauce/clip/ClumsyAnnoyingAntMikeHogu-9HFuYjU70tIotSP6) | 60 Bilder/s | Remastered-Ego, Unterwasser-Plattformwechsel, Ice-Beam-HUD, Gegner und Lock-on-Marker; Mündung öffnet sich beim Feuern. |
| Vinesauce, 23.02.2023 | [Worst Thing I Have Said In Years](https://twitch.tv/vinesauce/clip/AverageConsideratePorpoiseMingLee-fPTgfwUkaSKAHo1E) | 60 Bilder/s | Remastered-Ego, Ice-Beam-Feuern auf markierten Gegner, danach Umsehen/Gehen im dunklen Raum; Hüftlage mit Raster vermessen. |
| Vinesauce, 10.02.2023 | [Flash Fried Samus](https://twitch.tv/vinesauce/clip/FrozenLivelyMuleBleedPurple-bdg4L52kV_XnwkO1) | 60 Bilder/s | Remastered-Morph-Ball-Sequenz in Lavaraum; kein Ego-Spiel, keine Ego-Messung. |
| Vinesauce, 23.02.2023 | [im a cweep](https://twitch.tv/vinesauce/clip/TawdryBetterPancakePeanutButterJellyTime-P7pOxTde1T2XugVX) | 60 Bilder/s | Fremder Einspieler/Meme mit Albumgrafik, trotz Remastered-Kategorie; kein Ego-Spiel. |
| Vinesauce, 22.02.2023 | [Vinny's response to the Gorillaz movie getting canceled](https://twitch.tv/vinesauce/clip/PricklyCrunchyGoldfishLitty-baoXMfpNgewsNLyj) | 60 Bilder/s | Starting-Soon-Bild und Nintendo-Switch-Logo, trotz Remastered-Kategorie; kein Ego-Spiel. |
| Vinesauce, 03.03.2023 | ["I'll probably be fine"](https://twitch.tv/vinesauce/clip/WiseCaringFiddleheadsRiPepperonis-SO50Xo7AoTNzqqBW) | 60 Bilder/s | Remastered: zuerst Morph Ball um Säule, ab etwa 6,5 s Ego mit Plasmakanone; Umsehen und Bewegung zwischen blau leuchtenden Flächen. |
| Vinesauce, 02.05.2023 | [Laugh of Relief (Insanity)](https://twitch.tv/vinesauce/clip/DistinctHungryBobaPhilosoraptor-wCADouMiT2f31uXY) | 60 Bilder/s | Anderes Spiel (Pizza-Tower-artige 2D-Plattformeransicht), trotz Remastered-Kategorie; kein Metroid-Ego-Spiel. |
| Vinesauce, 17.02.2023 | [hoot wireman](https://twitch.tv/vinesauce/clip/WittyCalmPancakeAllenHuhu-ZPrcvCj4z5ODMMNE) | 60 Bilder/s | Remastered-Ego, Power-/Wave-Beamwechsel, Umsehen, Raumwechsel zur violetten Tür und violetter Schuss; Beamwechsel nativ vermessen. |

## 3. Steckbrief – Form, Bewegung und Aktionen

Die Zeilen bleiben nach Edition/Aufnahmezustand getrennt; „Hüfte“ bezeichnet die normale Egoansicht ohne Scan-Visor.
Nicht gemessene Felder bleiben offen. Das sichtbare Rohr ist Teil des rechten Arms, kein freier Gegenstand mit sichtbarer Griffhand.

| Typ | Hüfthaltung: Lage, Größe, Lauf | Zielen in der Hüfte (Mündung → Mitte) | Sprint / Tragen | ADS: Zeit, Visier, Nähe, Zoom | Feuern / Rückstoß | Aktionen (Ziehen, Nachladen, Pump, Laden) | Arme | Besonderheiten | Cube Escape (Felder, Toolgen) |
|---|---|---|---|---|---|---|---|---|---|
| **Armkanone mit weißem Überzug / Originalfamilie** (BashPrime, 26.10.2018) | Unten rechts, Körper etwa 53–100 / 64–100 %, weißer Überzug, Rohr schräg nach oben links | Mündungsbereich etwa 61 / 66, klar rechts unter der Mitte; kein Hüftschuss in diesem Beleg vermessen | Keine isolierte Sprint-/Tragepose; beim Umsehen bleibt sie rechts unten | Kein ADS-Okular im Beleg; Combat-/Scan-Visorwechsel getrennt unten | Nicht vermessen | Combat → Scan: Kanone in 0,15 s weg; Rückweg: erscheint nach 0,15 s und steht nach insgesamt 0,42 s wieder unten rechts | Rechter Arm im Rohr; keine separate Griffhand; linke Hand in diesen Momenten nicht sichtbar | Klassisches HUD; Plattform und Revision innerhalb der Originalfamilie offen | — |
| **Armkanone, gelbe Ladeform / Originalgrafik mit Randomizer** (BashPrime, 30.08.2023) | Beispiel bei 18,500 s: Körper etwa 54–100 / 65–100 %, Mündungsbereich etwa 58 / 67; keine Typ-Mittelwerte | Ladehülle sitzt vor der Mündung rechts unter der Mitte; beim Entladen läuft der Schuss nach vorn | Nicht isoliert | Kein ADS im vermessenen Ablauf | Volle Ladehülle verschwindet beim Entladen in einem Bild; reine Rückstoß-/Kamerazeit nicht isoliert | Sichtbares Leuchten → volle Hülle 37 Bilder / 0,62 s; voller Zustand wird gehalten; keine Tastendruck-Gesamtladezeit | Linke Hand kommt nach der vollen Hülle von unten links, umfasst den oberen Rohrteil in etwa 0,20 s und zieht vor dem Schuss zurück; rechte Hand im Rohr | Randomizer-Overlay sichtbar, Einstellungen/Parameter unbekannt | — |
| **Armkanone, Ice Beam / Remastered** (Vinesauce, 22./23.02.2023) | Körper etwa 54–100 / 62–96 %, Mündungsbereich etwa 58 / 65; drei gelbe Streifen, helle schräge Kante; unterer Visorrahmen davor | Freies Zielzeichen um 50 / 50; bei Lock-on rotes Ziel und einfahrende cyanfarbene Klammern; hier kein isolierbarer räumlicher Sprung | Bei Unterwasser-Plattformwechsel weiter rechts unten sichtbar; keine getrennte Tragepose belegt; Bob-Hz/Sprint offen | Keine klassische ADS-Pose im Beleg; Visor-HUD bleibt sichtbar; Zoom nicht bestimmt | Vordere Kanonenteile öffnen sich, helles Eis/Mündungslicht verdeckt Teile des Rohres; keine isolierte Rückstellzeit | Lock-on: rote Markierungen gehen den großen cyanfarbenen Klammern um 4 Bilder voraus | Rechter Arm im Rohr; linke Stützhand im Hüftlagebild nicht sichtbar | Unterwasser-Bewegung mit Blickrollen überlagert; keine verlässlichen Absprung-/Landungsmarker | — |
| **Armkanone, Power → Wave Beam / Remastered** (Vinesauce, 17.02.2023) | Bleibt beim Wechsel rechts unten; keine vollständige Wegsteckphase | Zielzeichen bleibt in der freien Sicht; nach Wechsel violetter Schuss | Nicht isoliert | Kein ADS im Wechselablauf | Violette Schussfarbe bestätigt Wave Beam; Rückstoß nicht vermessen | Ringwelle → neue Wave-Beam-Kennung 36 Bilder / 0,60 s; Körper wird vorübergehend orange umzeichnet | Keine separate Handaktion im vermessenen Wechsel | Ähnliche Ringfarbe wie Ladeeffekt; erst HUD/Schuss sichern die Zuordnung zum Wechsel | — |
| **Scan Visor / Originalfamilie** (BashPrime, 26.10.2018) | Armkanone vollständig außerhalb des Bildes | Rechteckige Scan-Ecken und Zielmarker in freier Sicht | Kein Trageobjekt neben dem Scannerrahmen sichtbar | Erste Scanrahmenlinien 13 Bilder / 0,22 s nach dem ersten Senken; kein gemessener optischer Zoom | Nicht anwendbar | Scanrahmen blendet separat von Kanonenbewegung ein/aus; sichtbarer Hin-/Rückweg unterschiedlich lang | Keine schwebende separate Scannerhand im Beleg | Scanansicht tauscht HUD und Werkzeugpräsenz; kein physisches Okular vor der Kamera | — |
