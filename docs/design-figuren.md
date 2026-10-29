# Gestaltung von Spielfiguren – Roboter, Mechs und gepanzerte Figuren

Recherche REF 0.30 „Blueprint“ (28.10.2026) für die Roboter-Spielfigur von **BASIC** (Projekt `cubeescape-ballon`, Ego-Arme, Figur
`robot_figure.py`) und für Cube Escape (Roboter-Spielfigur, NPCs wie M-4): wie Studios Figuren aufbauen – Proportion, Silhouette,
Formsprache, Lesbarkeit auf Distanz und in Bewegung, modulare Panzerteile und Gelenke, Topologie und Rig, Farb- und Materialblockung,
Maßstab Figur zu Ausrüstung. Hier stehen **Quellenaussagen und daraus abgeleitete Regelvorschläge**; entschieden wird in BALLON bzw.
Cube Escape ([5](#5-entscheidungsliste)). Keine Messung am Bild. Maschinenlesbar: [`data/design_quellen.json`](../data/design_quellen.json)
(gemeinsam mit der Ausrüstung). Nachbarthema: [Gestaltung von Ausrüstung](design-ausruestung.md).

**Glaubwürdigkeit:** **Primär** = Studio oder Künstler über die eigene Arbeit (Vortrag, Dev-Blog, ViDoc, Interview, eigener Breakdown) ·
**Sekundär** = Fachmagazin, Wiki, Lehrmaterial über fremde Arbeit · **Meinung** = Forum, Blog ohne Projektbezug, SEO-Leitfaden. Jede Zahl
gilt für das Projekt des Sprechers.

## 1. Quellen und Methode

- **Gesammelt** von drei Unteragenten (Sonnet 5.5) wie in [design-ausruestung.md › 1](design-ausruestung.md#1-quellen-und-methode).
- **Geprüft** vom Koordinator (Opus 5.5): alle Text-URLs per `curl` aufgerufen (28.10.2026), 9 Aussagen im Wortlaut der Seite gefunden
  (F04, F06 ×2, F11, F22, F23 ×2, F24, F28) plus F33 (1–3 mm, Meinungsquelle); bei den Videos 3 yt-dlp-Zeilen selbst abgerufen (YB04, YB05,
  YB09) und 7 Untertitelstellen in 6 Videos nachgelesen (YB01, YB02, YB04, YB05, YB09 ×2, YB13). F24 aus dem Suchauszug durch den gelesenen
  Wikitext ersetzt (die Aussage zu Knie-Dreiecken gestrichen, weil die Unterseite nur Bilder zeigt). Nicht ladbar: F08 (GDC Vault in
  Wartung), F17 (Steam-Hilfe nur per JavaScript); F30 lud beim Unteragenten, beim Koordinator 403.
- **Lücken:** Maßstab Figur zu Ausrüstung (Hand, Griff, Schulter) belegen nur F11/YB06 (Titanfall) und A24 (Valorant: Hände vergrößert);
  eine Zahl für Hand ÷ Griff fand keine Quelle. Farbregel 60/30/10 nur als Meinung (F30). Gelenkfreiräume in mm nur Meinung (F33).

## 2. Quellen

47 Quellen (33 Texte, 14 Videos), davon 26 Primär; nicht geladen 2 (F08, F17). IDs sind stabil; Anker `q-<id>`.

### Texte und Vorträge

- <a id="q-f01"></a>**F01** [Illustrative Rendering in Team Fortress 2](https://www.yumpu.com/en/document/view/11265082/illustrative-rendering-in-team-fortress-2-pdf-valve) – Jason Mitchell, Moby Francke, Dhabih Eng; Valve; 2007 · Paper · **Primär** · [zweiter Link](https://steamcdn-a.akamaihd.net/apps/valve/2007/NPAR07_IllustrativeRenderingInTeamFortress2.pdf)
  - Stilvorbild waren Illustratoren des frühen 20. Jh. mit starken, unterscheidbaren Silhouetten; Kanten werden über Rim-Licht statt dunkler Umrisslinien betont.
  - Schattierung soll die Klassen unter wechselnden Lichtbedingungen lesbar halten; Luminanz- und Farbtonvariation vermittelt die Form schnell.
  - Rim-Licht (aus Irradiance-Volume) hält Figuren auch fern von lokalen Lichtern definiert - Kantenlicht ersetzt Outline.
  - Zitat: „strong, distinctive silhouettes“
- <a id="q-f02"></a>**F02** [Illustrative Rendering in Team Fortress 2 (Wiki-Seite mit Videotranskript)](https://wiki.teamfortress.com/wiki/Illustrative_Rendering_in_Team_Fortress_2) – Official TF2 Wiki; Valve (Wiki); unbekannt · Wiki · **Sekundär**
  - Charaktere sind so gebaut, dass sie auch ohne Lichthinweise an der Silhouette erkennbar sind; Proportionen, Waffen und Silhouettenlinien machen jede Klasse einzigartig.
  - Kleiderfalten im Schatten wiederholen die äußeren Silhouettenformen (Hierarchie: erst Umriss, dann Innenform).
  - Team-Paletten: gedämpfte Farben dominieren, kleine gesättigte Akzente; RED wirkt warm/kantig, BLU kühl/orthogonal.
  - Visuelles Rauschen der Welt wird minimiert (impressionistischer Look).
- <a id="q-f03"></a>**F03** [VALORANT Shaders and Gameplay Clarity](https://www.riotgames.com/en/news/valorant-shaders-and-gameplay-clarity) – Brandon 'mochi' Wang; Riot Games; 2020-06-30 · Artikel · **Primär**
  - Figuren müssen sich immer von der Umgebung abheben; mit Entfernung brechen Details weg, daher werden entfernte Figuren aufgehellt.
  - Zusätzliches Licht auf streifenden Winkeln (Fresnel) erzeugt einen Silhouetteneffekt, betont auf der Oberkörperseite (Licht von oben).
  - Team-Lesbarkeit per Fresnel-Farbe: Gegner rot, Verbündete neutral blau; bei Distanz werden Gegner-Fresnels größer, aber begrenzt (Clamping).
  - Glanz (Specular) ist für die Lesbarkeit entbehrlich und wird auf niedrigen Einstellungen entfernt.
  - Zitat: „characters need to always stand out from their environment“
- <a id="q-f04"></a>**F04** [Clarity in League](https://www.leagueoflegends.com/en-us/news/dev/clarity-in-league/) – bananaband1t; Riot Games; 2021-03-12 · Artikel · **Primär**
  - Silhouette wird in primäre, sekundäre und tertiäre Merkmale gegliedert; das primäre Merkmal (z. B. Waffe) darf auch in Skins nie entfernt oder stark verändert werden.
  - Die Größe der Silhouette signalisiert Spielstil: große, gepanzerte Figuren lesen sich als Tanks/Kämpfer, sehr kleine nicht.
  - Aus der Silhouette allein muss die Blickrichtung erkennbar sein (kommt sie auf mich zu oder geht sie weg).
  - Figuren, die vor allem über Animation erkannt werden, sind schwerer variierbar.
- <a id="q-f05"></a>**F05** [What's It Like to Art Direct a Major Video Game?](https://www.vice.com/en/article/heres-what-its-like-to-art-direct-overwatch/) – Giaco Furino (Interview mit Bill Petras); Blizzard Entertainment / Vice; 2016-06-21 · Interview · **Primär**
  - Overwatch-Art-Direktor Bill Petras nennt große, kräftige Silhouetten als Leitprinzip (Vergleich mit World of Warcraft).
  - Dynamische Proportionen und Formen stehen im Mittelpunkt des Charakterdesigns.
  - Gesamtziel: kräftige, bunte, optimistische Optik.
  - Zitat: „big, bold silhouettes on characters“
- <a id="q-f06"></a>**F06** [What it's like to work on Overwatch as a concept artist](https://overwatch.blizzard.com/en-gb/news/23537427/what-it-s-like-to-work-on-overwatch-as-a-concept-artist/) – Overwatch-Konzeptkünstler (u. a. Daryl Tan, Qiu Fang); Blizzard Entertainment; unbekannt · Artikel · **Primär**
  - Große Formen liegen oben an der Figur, damit sie aus der Ferne lesbar sind; feine Details erst aus der Nähe.
  - Quadrate lesen sich als stabil, Kreise als harmlos (keine scharfen Kanten) - Grundformen transportieren Charakter.
  - Die Bewegung von Pharah und Reinhardt folgt den mechanischen Gelenken ihrer Rüstung; ein Skin darf die Silhouette nicht radikal ändern.
  - Eine frühe Talon-Figur scheiterte im Playtest, weil ihre Silhouette nicht identifizierbar war.
  - Zitat: „big shapes tend to appear near the top of characters“
- <a id="q-f07"></a>**F07** [Designing Overwatch](https://www.cookandbecker.com/en/article/378/designing-overwatch.html) – Arjan Terpstra; Cook and Becker (über Blizzard-GDC-Vortrag 2017); 2022-10-24 · Artikel · **Sekundär**
  - Erste Säule: Vielfalt auch bei Körperproportionen und Designsprache; Reinhardt hat bewusst überlebensgroße Proportionen und große Schulterpanzer.
  - Lesbarkeit mitten im Kampf war laut Petras/Tsang der Kern; geprüft wurde, ob eine Silhouette einer vorhandenen zu ähnlich ist.
  - Jeder Held bekam eine eigene Farbpalette; helle Palette bewusst als Gegenpol zu düsteren Sci-Fi-Shootern.
- <a id="q-f08"></a>**F08** [The Art of 'Overwatch': Evolving a Legacy](https://www.gdcvault.com/play/1024268) – Bill Petras, Arnold Tsang; Blizzard Entertainment; 2017 · Vortrag · **Primär** · **nicht geladen** (Suchauszug)
  - Vortrag der Art Director/Assistant Art Director über frühe Art-Direction-Pfeiler (Vielfalt, hoffnungsvolle Zukunft, lebendige Welt) und das Design einzelner Helden/Karten.
  - Stoßrichtung laut Sekundärquellen: Heldenlesbarkeit im Kampf als Grundlage, Silhouettenabgleich gegen bestehende Figuren (siehe F07).
- <a id="q-f09"></a>**F09** [How Riot Games designs a new agent in Valorant](https://www.oneesports.gg/valorant/valorant-agent-design-neon-riot-games/) – Wanzi Koh (mit John Goscicki, Riot); ONE Esports / Riot Games; 2022-11-25 · Interview · **Sekundär**
  - Vorproduktion bis ca. 2 Monate mit einem Proxy-Modell: Farben und Formen werden früh vor einer Wand und an Deckungen auf Sichtbarkeit getestet.
  - Beispiel Neon: geprüft wurde, ob ihre Haarknoten über Kisten hinausragen (Sichtbarkeit über Deckung).
  - Gesamtdauer eines Agenten 10-14 Monate; Produktion 3-4 Monate.
- <a id="q-f10"></a>**F10** [How Valorant's Agent Characters Are Designed With Gameplay In Mind](https://screenrant.com/valorant-agents-character-design-gameplay-riot-games-interview/) – Camden Jones; Screen Rant / Riot Games; 2021-08-25 · Interview · **Sekundär**
  - Fairness im Wettbewerb prägt Kleiderfarbe und Körperform; Konzepte werden verworfen, wenn die Silhouette das Spiel unfair macht.
  - Alle Agenten müssen kampfglaubwürdig wirken (Taschen, Gurte) - Funktion vor Stil.
- <a id="q-f11"></a>**F11** [Q&A: Titanfall lead artist Joel Emslie](https://www.cgchannel.com/2014/04/qa-titanfall-lead-artist-joel-emslie/) – Joel Emslie (Interview); Respawn Entertainment / CG Channel; 2014-04-29 · Interview · **Primär**
  - Titan-Entwurf begann mit einer Kitbash-Maquette; neben einer Actionfigur gestellt las sie sich als ca. 6 m (20 ft) großer Mech - der Maßstab Pilot zu Titan wurde früh fixiert, weil die Welt darum gebaut wurde.
  - Maquetten (Ogre kitbash, Atlas Scratchbuild) auf Drahtarmatur im Maßstab 1:6 mit realen Teilen; Realteile erden das Design.
  - Entwürfe wurden überarbeitet, damit Animation und Design die Bewegung glaubwürdig umsetzen konnten.
  - Leitmotiv David gegen Goliath: Pilot gegen Titan.
- <a id="q-f12"></a>**F12** [Titanfall 2 interview: Talking single-player, eSports, and bonding with your titan](https://fenixbazaar.com/2016/08/23/titanfall-2-full-interview/) – Fenix Bazaar Staff (Joel Emslie); Respawn Entertainment / Fenix Bazaar; 2016-08-23 · Interview · **Primär**
  - Visuelle Sprache ist laut Art Director Säule neben der Spielsprache: jeder Titan soll einen 'Flash Read' der Kernfähigkeiten liefern.
  - Für Titanfall 2 kamen zwei neue Rigs (Skelette) hinzu: einer für einen flinken Titan mit langen, baumelnden Gliedern, einer für einen langen, stelzigen Körperbau - Proportion wird über das Skelett gesteuert.
  - Spieler sollen Rüstungstyp, Fähigkeiten und Persönlichkeit an der Form ablesen.
  - Zitat: „visual language is a huge pillar for me“
- <a id="q-f13"></a>**F13** [The making of Horizon Zero Dawn's machines, as told by Guerrilla Games](https://blog.playstation.com/archive/2017/02/24/the-making-of-horizon-zero-dawns-machines-as-told-by-guerrilla-games/) – Gillen McAllister; Guerrilla Games / PlayStation Blog; 2017-02-24 · Interview · **Primär**
  - Skorpion-artige Maschinen wurden verworfen, weil dünne Beine kaum Trefferfläche boten; große Flächen und sichtbare mechanische Teile erlauben mehrlagige Designs mit abschießbaren Komponenten.
  - Maschinen kombinieren Tiermerkmale statt ein Tier zu kopieren; frühe grobe Modelle und Mockups testen die Richtung.
  - Schwachstellen sind am Körper ablesbar (Augen, Panzerplatten) - Form kommuniziert Spielregeln.
- <a id="q-f14"></a>**F14** [Making Horizon Zero Dawn's Machines feel like living creatures](https://www.gamedeveloper.com/design/making-i-horizon-zero-dawn-i-s-machines-feel-like-living-creatures) – Game Developer Staff; Guerrilla Games / Game Developer; 2017-04-21 · Artikel · **Sekundär**
  - Maschinen als Exoskelett (Metallrahmen außen, weiches Inneres als Schwachstelle) statt innerem Skelett.
  - Unpolierte ZBrush-Modelle mit Skelett gingen früh ins Spiel; Thunderjaw: ca. 5 Modellierer über 8 Monate, 18 Monate von Skizze bis spielbar.
  - 'Christmas-Tree-Problem': zu viele Lichter/Farben stören die Lesbarkeit; Gewicht großer Maschinen entsteht durch langsames Drehen, Ton, Partikel, Kamerawackeln.
- <a id="q-f15"></a>**F15** [Building Customizable Characters - GDC Summary and Review (Destiny)](https://www.bungie.net/en/Forums/Post/64332998?page=0) – Datto (Forenbeitrag zum Vortrag von Scott Shepard, Bungie); Bungie (GDC 2013, Zusammenfassung); 2014-04-08 · Artikel · **Sekundär**
  - Klassen-Silhouetten: Titan schwer gepanzert (Ritterrüstung, Wappenrock), Hunter leicht und zusammengewürfelt, Warlock Gelehrter; Anteil Panzer/Stoff je Klasse verschieden.
  - Basisslots Kopf/Brust/Arm/Bein plus ein klassenspezifischer fünfter Slot (Hunter-Umhang, Titan-Abzeichen, Warlock-Armband).
  - Speicherbudget je Körperteil verteilt (Titan mehr für Arme/Brust, Warlock weniger Arme), gleiche Gesamtsumme je Klasse; Farbkanäle für Panzer, Stoff und Anzug.
  - 'Mash Up': wiederverwendbare Teile ('Lego'); Basisteil einmal gebaut, Korrektur wirkt auf alle Sets; Betrachter prüft Clipping zwischen Teilen.
- <a id="q-f16"></a>**F16** [Take a gander at how Valve designs the look and feel of Dota 2 heroes](https://www.gamedeveloper.com/design/take-a-gander-at-how-valve-designs-the-look-and-feel-of-i-dota-2-i-heroes) – Alissa McAloon; Valve / Game Developer; 2017-10-06 · Artikel · **Sekundär**
  - Valves Charakter-Leitfaden gliedert sich in Silhouette, Wertverlauf (Value Gradient), Wertmuster, Farbe/Sättigung, Farbschemata, Ruheflächen und Direktionalität.
  - Ziel: unverwechselbarer Look auf dem Schlachtfeld, der die Identität schnell vermittelt.
- <a id="q-f17"></a>**F17** [Dota 2 Workshop - Character Art Guide / Item Model Requirements](https://support.steampowered.com/kb/9334-YDXV-8590/dota-2-workshop-character-art-guide) – Valve; Valve; unbekannt · Guide · **Primär** · **nicht geladen** (Suchauszug) · [zweiter Link](https://support.steampowered.com/kb/9814-QSHK-8085/dota-2-workshop-item-model-requirements)
  - Aus Suchauszug (Seitentext lud nicht, nur Titel 'Steam Support :: Dota 2 Workshop - Character Art Guide'): Silhouette muss auf den ersten Blick identifizierbar sein; Value (Hell/Dunkel) zählt mehr als Farbe.
  - Detailreiche Bereiche sollen ein kleiner Anteil sein und dort konzentriert, wo sie zählen; Sättigung unten niedriger, oben höher.
  - Budgets in Dreiecken; Polygondichte als Gradient (niedrig an Füßen/Unterkörper, hoch an Kopf/Oberkörper); jedes Polygon soll Silhouette oder Verformung dienen. Konkrete Zahlen je Held auf dota2.com/workshop/requirements nicht auswertbar.
- <a id="q-f18"></a>**F18** [Gears of War: Judgment - Epic's Art Director Discusses The Look](https://gameinformer.com/games/gears_of_war_judgment/b/xbox360/archive/2012/06/18/chris-perna-interview.aspx) – Dan Ryckert (Interview mit Chris Perna); Epic Games / Game Informer; 2012-06-18 · Interview · **Primär**
  - Erkennbarkeit bei Neudesigns bleibt durch das kreisförmige Brustpanzer-Motiv erhalten - ein einzelnes Leitmotiv trägt die Marke.
  - 'Dinosaur chart': Gegner in klein/mittel/riesig gestaffelt für Variation der Größenklassen im Kampf.
  - Palette bewusst von entsättigt (Gears 1) zu kräftig (Gears 3) verschoben, passend zu besserer Beleuchtung.
- <a id="q-f19"></a>**F19** [What the armor says: Gear of War](https://www.destructoid.com/what-the-armor-says-gear-of-war/) – Brad BradNicholson (zitiert Cliff Bleszinski); Epic Games / Destructoid; 2009-08-10 · Artikel · **Sekundär**
  - Rüstung bewusst schwer und bauchig (rundes Brustteil, blau emissiv); Ziel: Figuren fühlen sich 'schwer' an, Deckung nehmen soll sich wie das Pressen eines Massekörpers anfühlen.
  - Design der Rüstung als Spielgefühl-Werkzeug: Volumen und Masse verstärken Feedback.
- <a id="q-f20"></a>**F20** [Researcher Robot: Learning Hard-Surface Techniques](https://80.lv/articles/researcher-robot-learning-hard-surface-techniques) – Evgeny Romanov (Interview: Arti Sergeev); 80.lv (Einzelkünstler); 2020-06-30 · Breakdown · **Primär**
  - Roboter mit funktionierender Mechanik (Rücken und Kopf bewegen sich zusammen); Silhouette per Anatomiereferenz mit S-Kurve angelegt.
  - Das Rigging durch einen Dritten enthüllte Modellierfehler; extreme Posen sind nötig, um zu sehen, wie Mechanismen zusammenarbeiten.
  - Aufteilung in 7 UV-Teile; Ngons/Dreiecke unkritisch, wenn das Shading stimmt.
  - Zitat: „put in quite extreme poses and watch how everything works“
- <a id="q-f21"></a>**F21** [How to Auto Rig Cyborgs with Character Creator AccuRIG - Part 2](https://magazine.reallusion.com/2023/04/10/how-to-auto-rig-cyborgs-with-character-creator-accurig-part-2/) – José Antonio Tijerín; Reallusion Magazine; 2023-04-10 · Guide · **Sekundär**
  - Starre Roboter ('rigid system') gelten als aufwendigste Rigart, da keine elastischen Verformungen nutzbar sind; das System beruht auf Kugeln als Gelenken.
  - Hydraulikrohre: untere Polygone an Hüfte, obere an Brust gebunden, dadurch scheinbar gleitend/sich dehnend.
  - Starre Teile besser als Teile des Modells belassen; bei vielen überlappenden Teilen drohen Durchdringungen.
- <a id="q-f22"></a>**F22** [How to Auto Rig Cyborgs With Character Creator AccuRIG](https://80.lv/articles/how-to-auto-rig-cyborgs-with-character-creator-accurig) – José Tijerín; 80.lv; 2023-05-05 · Guide · **Sekundär**
  - Starre Rüstungsteile (Beintaschen, Unterarmschienen) werden über Attach an Knochen gehängt; Helm mit mehreren Teilen besser als Prop mit eigenen Knochen.
  - Einteiliger Brustpanzer schränkt ein: obere Wirbelsäulenknochen nicht animieren, Arme nicht über 180 Grad heben.
  - Gemischte Struktur aus starren Teilen auf flexiblen Teilen spart Polygone; Überschneidungen sofort in der Geometrie beheben.
- <a id="q-f23"></a>**F23** [Elbow Topology Explained for Character Modeling](https://cgtyphoon.com/topology/elbow-topology-explained-for-character-modeling/) – CG Typhoon; CG Typhoon; unbekannt · Guide · **Sekundär**
  - Schleifenzahl am Ellbogen: Mobile 3-4, normale Spielfigur 4-6, Heldenfigur 6-8, Cinematic 8+.
  - Mehrere gleichmäßig verteilte Schleifen statt einer Scharnierschleife; Pole nicht auf die Biegelinie legen (Einschnüren, Shading-Fehler); bevorzugt Quads, Dreiecke nur abseits der Biegezone.
  - Testen bei ca. 45 Grad (frühes Einschnüren) und 90 Grad (Dicke bleibt) sowie am Extrem (gestreckte Seite, Silhouette).
- <a id="q-f24"></a>**F24** [Topology (inkl. Unterseite Limb Topology)](http://wiki.polycount.com/wiki/Topology) – Polycount-Community; Polycount; unbekannt · Wiki · **Sekundär**
  - Topologie zählt am meisten, wo am stärksten verformt wird: Hüfte/Gesäß, Schultern/Achseln, Mundwinkel, Knie, Ellbogen, Hände/Finger.
  - Für ein Low-Poly-Spielmodell sind Dreiecke erlaubt, aber jede Kante braucht einen Grund; Spielmodelle auf gute Silhouette, Kantenloops für Verformung, ruhige Vertex-Normalen und gute UV-Nähte optimieren.
- <a id="q-f25"></a>**F25** [Topology for Game and Game-Based Characters](https://80.lv/articles/topology-for-game-and-game-based-characters) – Ellie Harisova (Interviews mit Evgeny Pyrch, Massimiliano Bianchini); 80.lv; 2020-07-11 · Artikel · **Sekundär**
  - Kantenfluss entlang von Anatomie- bzw. Kleidungslinien anlegen; Gelenke brauchen besondere Aufmerksamkeit für Rig und Animation.
  - Technische Vorgaben und Polygonlimit einhalten; gute Topologie erlaubt mehr Detail mit weniger Polygonen.
  - Zitat: „The joints require extra attention to look good when it's getting rigged and animated.“
- <a id="q-f26"></a>**F26** [The Soul of Low Poly Characters](https://80.lv/articles/the-soul-of-low-poly-characters) – Danette Beatty (Interview: Kirill Tokarev); 80.lv (Einzelkünstlerin); 2016-11-23 · Interview · **Primär**
  - Proportionen aus einfachen Primitiven aufbauen; Form und Proportion zuerst, Details später.
  - Jedes Polygon muss relevant sein, aber es braucht genug Polygone für eine saubere Silhouette; Kantenfluss beim Retopologisieren darauf ausrichten.
  - Flache Farben per Vertex-Painting (keine UVs nötig).
  - Zitat: „Working with so few polygons means that each one needs to be relevant.“
- <a id="q-f27"></a>**F27** [Implementing Low Poly Style in Game Dev](https://80.lv/articles/implementing-low-poly-style-in-game-dev) – Maciej Szymaś (Interview: Kirill Tokarev); 80.lv (Einzelkünstler); 2019-04-15 · Interview · **Primär**
  - Vier Stufen: Grundform, optimiertes Modell, Stilisierung mit Detail, Oberflächendetail.
  - Proportion und richtige Form tragen das Modell; als Budget-Beispiel wird ein Limit von 1000 Dreiecken pro Modell genannt (Hinweis: Artikel behandelt Assets allgemein, nicht gezielt Charaktere).
  - Geglättete Normalen/Sharp-Marks geben Sculpt-Look ohne mehr Dreiecke.
- <a id="q-f28"></a>**F28** [Design Tips for In-Game Character Proportions](https://kongregatedev.ghost.io/design-tips-for-in-game-character-proportions/) – Kongregate Developers Blog; Kongregate; 2016-05-19 · Artikel · **Sekundär**
  - Reale Erwachsene ca. 7-8 Kopfhöhen; ab 8 Köpfen beginnt 'Superhelden-Gebiet'; Zeichentrick meist 2-6 Köpfe.
  - Bei 8 Köpfen nimmt der Körper mehr Bildfläche ein, Gesichtsdetails werden schwerer lesbar; ein breiterer Kopf überdeckt mehr Körper.
  - In Draufsicht verdeckt ein großer Kopf den Körper - Körper ggf. länger machen.
- <a id="q-f29"></a>**F29** [What Is Shape Language? A Guide for Character Designers](https://pixune.com/blog/shape-language-technique/) – Nazanin Shahbazi; Pixune; 2026-08-16 · Artikel · **Sekundär**
  - Kreis = freundlich/sicher, Quadrat = Stärke/Stabilität/Autorität (Helden, Beschützer), Dreieck = Gefahr/Tempo/Unberechenbarkeit (Schurken, Monster).
  - Beispiele: Baymax/Kirby rund, Superman/Captain America quadratisch, Scar/Maleficent dreieckig. Mischung der Grundformen ist üblich.
- <a id="q-f30"></a>**F30** [The Ultimate Guide to Creating Memorable Character Color Palettes](https://pixflow.net/blog/the-ultimate-guide-to-creating-memorable-character-color-palettes/) – unbekannt; Pixflow; 2026-03-12 · Guide · **Meinung**
  - 60-30-10 für Figuren: 60 % Grundfarbe (Identität), 30 % Zweitfarbe (Kontrast/Tiefe), 10 % Akzent.
  - Geringer Kontrast lässt Figuren im Hintergrund verschwinden; Palette gegen verschiedene Hintergründe testen.
- <a id="q-f31"></a>**F31** [Collections: The Problem with Sci-Fi Body Armor](https://acoup.blog/2024/11/29/collections-the-problem-with-sci-fi-body-armor/) – Bret Devereaux; A Collection of Unmitigated Pedantry; 2024-11-29 · Artikel · **Meinung**
  - Auf dem Oberarm sitzende Schulterpanzer und ein an Gurten hängendes Brustteil stoßen bei erhobenen Armen an den Hals; große Lücke zwischen Kragen und Schulter.
  - Historische Lösungen: segmentierte Schulterplatten für hebbare Arme, Brustpanzer endet an der natürlichen Taille, teleskopierende Lamellen am Hüftschutz.
  - Beispiel Mass Effect N7: Bauchplatten gleiten nicht übereinander, die Rüstung biegt sich nur.
- <a id="q-f32"></a>**F32** [Help with a pauldron rig](https://blenderartists.org/t/help-with-a-pauldron-rig/1546417) – grant.r.brown, digitvisions (Forum); Blender Artists Community; 2024-08-30 · Wiki · **Meinung**
  - Schulterpanzer müssen sich relativ zum Arm verschieben: Extra-Knochen mit Armature-Constraint statt direkter Elternschaft am Oberarm.
  - Constraint-Einfluss per Driver an die Armhöhe koppeln (ca. 0,195 Arm unten, ca. 0,595 Arm oben), Scharnierposition am Panzer nachjustieren.
- <a id="q-f33"></a>**F33** [Mecha armor rigging guide (Mecha-Pilot)](https://threedium.io/create/3d-models/character/anime/mecha-pilot) – Threedium; Threedium; unbekannt · Guide · **Meinung**
  - Doppeltes Skelett: organische Knochen für Wirbelsäule/Gliedmaßen plus separate mechanische Knochen für Rüstungsteile (Schulterpanzer, Brustplatten, Hüftschutz).
  - Gewichte für Mecha-Teile nur 0,0 oder 1,0 (starr); als Abstand zwischen Rüstungsplatten werden 1-3 mm genannt.
  - Pole-Vector-Constraints steuern Beugerichtung von Ellbogen und Knie.

### Videos (YouTube, per yt-dlp geprüft)

- <a id="q-yb01"></a>**YB01** [A No-Nonsense Approach to Designing Horizon Zero Dawn's Robot Dinosaurs](https://www.youtube.com/watch?v=iDqDPsjrz94) – Kanal GDC Festival of Gaming, Sprecher Jan-Bart van Beek (Art Director, Guerrilla); Guerrilla Games; hochgeladen 2020-10-29, 60:57 min, 30 fps · Vortrag · **Primär**
  - Die ersten Maschinenentwürfe nach dem Muster militärischer Industriedesigns (Kriegsmaschine, Killzone-Stil) verfehlten den emotionalen Kern (Jäger statt Soldat) und wirkten nicht wie Lebewesen; alles wurde verworfen. (35:18, untertitel)
  - Roboter-Dinosaurier funktionieren, weil bekannte Formen (T-Rex) sofort Gefahr signalisieren, ohne dass Animation oder Hintergrund es erklären müssen. (37:22, untertitel)
  - Biomimetik: Maschinen folgen den Lösungen der Natur (Exoskelett statt innerem Skelett, künstliche Muskeln, algorithmisch erzeugte Verstärkungen), beraten von Robotiker:innen der TU Delft. (41:03, untertitel)
  - Form folgt der ökologischen Nische und Funktion (Watcher als 'Alarmglocke'); die Gestalt darf stark variieren, entscheidend ist, dass das Verhalten stimmt, damit man sie als Lebewesen liest. (42:04, untertitel)
- <a id="q-yb02"></a>**YB02** [Building Machines for a Better Future in 'Horizon'](https://www.youtube.com/watch?v=dr17S0I_h78) – Kanal GDC Festival of Gaming, Sprecher Maxim Fleury, Lennart Franken (Guerrilla Games); Guerrilla Games; hochgeladen 2022-12-27, 60:42 min, 30 fps · Vortrag · **Primär**
  - Pipeline einer Maschine: Designdokument, 3D-Konzept (direkt in 3D per Kitbash), Rig, Detailmodell, Outsourcing für Spielmesh, Texturierung; ein Jahr pro Maschine ist der Ausgangswert, den Parallelisierung drücken muss. (05:43, untertitel)
  - Stilregeln: keine Kolben, Schrauben oder harten Kanten, nichts Menschengemachtes, keine 90-Grad-Winkel; Rahmen und Muskeln als organisches 3D-gedrucktes Gerüst mit Platten darüber. (11:52, untertitel)
  - Interaktive Teile (Platten, Antennen, Waffen) sind heller, der Körper dunkler, damit abschießbare Komponenten klar als getrennte Teile lesen. (12:23, untertitel)
  - Eine Bibliothek älterer Maschinenteile wird neu skulptiert wiederverwendet; subjektive Arbeit (Detail, Farbe) bleibt intern, objektive (UV, LOD, Bake) geht an Dienstleister, etwa 80/20. (19:06, untertitel)
- <a id="q-yb03"></a>**YB03** [Creating the Characters and Machines of Horizon Forbidden West -Guerrilla Games- 2023 ZBrush Summit](https://www.youtube.com/watch?v=MKkI8DWHwm4) – Kanal Maxon ZBrush, Sprecher Arno Schmitz, Lennart Franken (Guerrilla Games); Guerrilla Games; hochgeladen 2023-10-25, 93:17 min, 30 fps · Breakdown · **Primär**
  - Insert-Mesh- und Alpha-Pinsel-Bibliothek aus früheren Maschinen sichert einheitlichen Look; bewährte Platten werden verformt wiederverwendet, auch an Kostümen. (50:51, untertitel)
  - Silhouette wird mit Insets, Extrusionen und geschichteten Kantendetails aufgebrochen; Detailmaßstab über alle Maschinen gleich halten. (62:20, untertitel)
  - Jede Maschine besteht aus primären, sekundären und tertiären Formen; regelmäßige Verteilung wirkt künstlich, es braucht Ruhezonen und Gruppierung (Clumping). (68:07, untertitel)
- <a id="q-yb04"></a>**YB04** [Building Customizable Characters for Destiny](https://www.youtube.com/watch?v=WS-2-Q7RWLk) – Kanal GDC Festival of Gaming, Sprecher Scott Shepard (Bungie); Bungie; hochgeladen 2017-02-16, 55:35 min, 30 fps · Vortrag · **Primär**
  - Figuren werden in unabhängige Bausteine ('Bits': Schnallen, Schulterplatten, Visiere) zerlegt und per Assembler zu Arrangements zusammengesetzt; ein Fix am Bit wirkt auf alle Teile, die es verwenden. (12:48, untertitel)
  - Drei Materialfamilien über 'Dyes' (Armor, Cloth, Suit) steuern Farbe, Glanz und Detailkarten; Bits können je als in Ego-Sicht sichtbar oder unsichtbar markiert werden. (13:52, untertitel)
  - Klassen bekommen einfache Basissilhouetten für Lesbarkeit: Titan schwer (Metallplatten über Gummianzug, große Schulterpads), Hunter leicht (Hartschale über flexiblem Mittelteil), Warlock Mäntel/Roben. (04:08, untertitel)
  - Bits werden starr gebunden (Ein-Klick-Skinning) oder von Riggern individuell gewichtet; stark überlappende Teile wurden wegen technischen Aufwands vereinfacht. (16:24, untertitel)
  - Pro Spieler und Slot gibt es feste Budgets (Titan-Arm 1024x512 und ca. 170k Geometriespeicher, Warlock-Arm 512x512 und ca. 110k). (19:36, untertitel)
- <a id="q-yb05"></a>**YB05** [GDC 2008 - Stylization with a Purpose: The Illustrative World of Team Fortress 2](https://www.youtube.com/watch?v=SRFmHNzwbME) – Kanal iiboharz, Sprecher nicht in den Metadaten genannt (GDC-2008-Vortrag von Valve; Re-Upload mit Audio und Folien); Valve (Re-Upload durch Dritte); hochgeladen 2023-06-04, 51:12 min, 30 fps · Vortrag · **Primär**
  - Dreistufige Lesehierarchie: erst Farbe (Team), dann Silhouette (Klasse), zuletzt die Waffe. (05:34, untertitel)
  - Silhouetten unterscheiden sich über Körperproportionen, Hüte, Schuhe und Faltenwurf; sie sollen auch unter Drehung wirken. (07:06, untertitel)
  - Hohe Kontraste und Details liegen auf Brusthöhe (Abzeichen, Gurte, Westen), unten dunkel zu oben hell, damit der Blick zur Waffe geführt wird. (07:36, untertitel)
  - Prozess: Silhouette zuerst, dann Innenformen/Schattenformen, Modellblatt, Modell; Ambient Occlusion nur als Malhilfe. Rim-Highlights ersetzen dunkle Konturlinien. (14:45, untertitel)
- <a id="q-yb06"></a>**YB06** [Designing The Titans of Titanfall](https://www.youtube.com/watch?v=PWgByQiDhpE) – Kanal Game Informer, Sprecher Joel Emslie (Lead Artist, Respawn); Respawn Entertainment (Game Informer); hochgeladen 2013-06-28, 5:49 min, 30 fps · ViDoc · **Primär**
  - Titans entstehen als physische Kitbash-Maquette; man sieht sofort Schwerpunkt und Balance, und sie dient in Meetings als Action-Figur zur Spielprüfung. (01:03, untertitel)
  - Designziele: glaubwürdig, geerdet, militärisch, mit Platz für den Piloten; Mocap auf Titan-Rig skaliert, um organischere Bewegung zu bekommen. (02:05, untertitel)
  - Hände statt Kanonenarme ermöglichen Interaktionen wie Greifen und Werfen; Überdesign vermeiden, jedes Element soll auf den ersten Blick lesbar sein. (03:05, untertitel)
- <a id="q-yb07"></a>**YB07** [Titanfall 2 Inside Development: Pilot + Titan Design](https://www.youtube.com/watch?v=zs41dFUx0Po) – Kanal Titanfall Official, Sprecher Joel Emslie und Team (Respawn); Respawn Entertainment; hochgeladen 2016-12-16, 3:45 min, 30 fps · ViDoc · **Primär**
  - Praktische Maquetten halten das Design ehrlich, weil reale Teile nie perfekt sind (leicht schief, ungleiche Proportionen) und so Glaubwürdigkeit erzeugen. (00:05, untertitel)
  - Die erste Maquette (ein Tauchanzug) war Auslöser für die Titans: Ein kleiner Charakter im Anzug führte zur Idee der großen Roboter. (01:07, untertitel)
  - Zitat: „Real world objects are never perfect.“
- <a id="q-yb08"></a>**YB08** [3D Character Art & Skin Creation - Super Art Power Hour Ep 3](https://www.youtube.com/watch?v=AY-6Ny8VArA) – Kanal Riot Games, Sprecher Annie Kwon (Character Artist, Riot); Riot Games; hochgeladen 2022-08-15, 59:00 min, 24 fps · Breakdown · **Primär**
  - Der 'First Read' aus Entfernung (zusammengekniffene Augen) muss die Figur schon identifizieren; nicht zu früh an Gesicht oder Detail heranzoomen. (10:21, untertitel)
  - Konvexe und konkave Formschatten/AO werden bewusst überbetont, damit die 3D-Form auch ohne Drehung lesbar bleibt; Farbe wird neben der Spielkarte geprüft. (09:20, untertitel)
  - Low-Poly muss deformieren: Ellbogen müssen sauber falten, Rigger- und Pipeline-Bedürfnisse im Austausch klären. (12:56, untertitel)
- <a id="q-yb09"></a>**YB09** [SGC20: Walking trough the character creation process of Overwatch - The future of game tech](https://www.youtube.com/watch?v=0S8hi1wp4uc) – Kanal Sweden Game Arena, Sprecher Bruce Wilkie (Engine Programmer, Blizzard); Blizzard Entertainment; hochgeladen 2020-10-30, 75:11 min, 25 fps · Vortrag · **Primär**
  - Im Prototyp zählt zuerst die Silhouette: der Held muss im Kampf auffallen, das 2D-Konzept muss ins 3D übertragbar, riggbar und animierbar sein. (05:45, untertitel)
  - Budgets bei Overwatch: ca. 30.000 Dreiecke je Held, ca. 15.000 für Waffen und Zubehör, rund 30 MB Texturen nach Kompression. (11:53, untertitel)
  - Skelett: harte Obergrenze 1024 Bones, Ziel unter 500 Simulations-Bones; Cloth-Bones sind billig, physikalische Gelenke teuer. (15:59, untertitel)
  - Ego-Viewmodels bekommen rund 10 % des Tiefenpuffers, damit sie nicht in die Welt clippen. (16:59, untertitel)
- <a id="q-yb10"></a>**YB10** [Animation Bootcamp: Bringing Life to the Machines of Horizon Zero Dawn](https://www.youtube.com/watch?v=50mIKB-NACU) – Kanal GDC Festival of Gaming, Sprecher Richard Oud (Animator, Guerrilla Games); Guerrilla Games; hochgeladen 2019-11-27, 58:05 min, 30 fps · Vortrag · **Primär**
  - Mechanisch ruckelnde Bewegung ließ sich bei höherem Tempo nicht halten; die Animation wanderte zu realistischen Tierbewegungen mit gelegentlichem Jitter. (09:49, untertitel)
  - Roboterhafte Bewegung blieb nur der Ancient-Klasse (z. B. Deathbringer) vorbehalten, weil sie zum Design passt; ansonsten Tierreferenzen (Emu, Seelöwe, Roter Panda) für ein unterscheidendes Merkmal. (12:24, untertitel)
- <a id="q-yb11"></a>**YB11** [Overwatch: How A Hero is Mei'd](https://www.youtube.com/watch?v=lHevkQIZL2M) – Kanal GDC Festival of Gaming, Sprecher David Gibson (Animator, Blizzard); Blizzard Entertainment; hochgeladen 2016-06-06, 53:42 min, 30 fps · Vortrag · **Primär**
  - Neue Helden entstehen im Gespräch von Konzeptkünstlern, Art Director, Designern und Autor; der Animator holt zusätzlich informell Wünsche aller Disziplinen ein. (18:45, untertitel)
  - Gameplay-Einschränkungen ergeben sich aus dem Design: Der Schlauch von Mei's Waffe zum Rucksack hält eine Hand an der Waffe und begrenzt Bewegungen. (22:22, untertitel)
- <a id="q-yb12"></a>**YB12** [The Evolution of Destiny's Art](https://www.youtube.com/watch?v=XBCoq9yrBdk) – Kanal Game Informer, Sprecher Art Director von Destiny (laut Beschreibung, Name nicht genannt); Bungie (Game Informer); hochgeladen 2013-12-07, 6:06 min, 30 fps · ViDoc · **Primär**
  - Man definiert zuerst ein Ziel, das sofort cool wirkt, und füllt den Rest darum; bei Rüstung wiegt man Einheitlichkeit gegen Vielfalt ab, nicht perfekt passende Teile vermitteln den Eindruck gesammelter Beute. (04:06, untertitel)
- <a id="q-yb13"></a>**YB13** [Animating Mech tutorial part 2/3 - Skinning in MayaLT](https://www.youtube.com/watch?v=VmEhsielvLU) – Kanal Kubold, Sprecher Kubold; Kubold; hochgeladen 2016-11-22, 10:24 min, 30 fps · Tutorial · **Sekundär**
  - Bei einem Hard-Surface-Mech wird jedes Vertex auf genau einen Knochen begrenzt (Max Influences 1, statt 4 bei biegsamen Figuren). (03:07, untertitel)
  - Gewichte mit dem Solid-Pinsel auf Wert 1 malen und links auf rechts spiegeln; das Ergebnis mit Test-Keyframes prüfen. (04:11, untertitel)
- <a id="q-yb14"></a>**YB14** [Animating and Rigging Robots in Blender 3D](https://www.youtube.com/watch?v=ZkAk-GYpcvs) – Kanal SouthernShotty, Sprecher SouthernShotty; SouthernShotty; hochgeladen 2023-12-05, 16:09 min, 60 fps · Tutorial · **Sekundär**
  - Teile werden mit 'Empty Groups' statt Automatic Weights gebunden, weil automatische Gewichte den Mech weich und biegsam machen; Vertex-Gruppen mit Gewicht 1 weisen jedes Teil einem Knochen zu. (07:40, untertitel)
  - IK-Kette mit Zwischenknochen und separatem Fuß-Kontrollknochen, benannt .L/.R und per Symmetrize gespiegelt. (04:37, untertitel)

## 3. Gestaltungsregeln

Abgeleitet aus den Quellen in [2](#2-quellen); jede Regel nennt ihre Belege (IDs) und eine Prüfung, die ein Generator (Python/Blender,
Welt mm, Figur auf z = 0 wie BALLON `robot_figure.py`) selbst ausführen kann. **Zahlen aus Quellen** gelten für das genannte Projekt;
**Prüfwerte ohne Quelle** sind als „Vorschlag“ gekennzeichnet und erst nach einer Entscheidung ([5](#5-entscheidungsliste)) verbindlich.

### 3.1 Silhouette und Lesbarkeit

<a id="f-r1"></a>**F-R1 Silhouette erkennbar ohne Licht und Farbe.** Jede Figur (Spielerfigur, jeder NPC-Typ) ist als schwarze Fläche
eindeutig, auch gedreht; der „erste Blick“ aus der Distanz (Augen zusammenkneifen) identifiziert sie; neue Figuren werden gegen die
vorhandenen auf Verwechslung geprüft, und eine nicht erkennbare Silhouette scheitert vor der Produktion. Belege: F01, F02, F04, F06, F07,
F12, YB05, YB08, YB09. Prüfung: Silhouetten vorn, seitlich, 3/4 und hinten auf gleiche Höhe normiert; **Vorschlag:** paarweise IoU < 0,85 je Ansicht.

<a id="f-r2"></a>**F-R2 Lesereihenfolge festlegen.** Team Fortress 2 liest erst Farbe (Team), dann Silhouette (Klasse), zuletzt die
Ausrüstung; die Figur führt den Blick entsprechend. Belege: YB05, F02. Prüfung: im Modulkopf festhalten, was der erste, zweite und dritte
Blick zeigt (Spielerfigur: Silhouette → Medaillon/Visier → Ausrüstung).

<a id="f-r3"></a>**F-R3 Silhouette in Primär, Sekundär, Tertiär gliedern.** Das primäre Merkmal (Schulter-/Kopfform, Leitmotiv) bleibt in
jeder Variante erhalten; Varianten ändern Sekundäres und Tertiäres. Ein einzelnes wiederkehrendes Motiv kann eine ganze Marke tragen
(Gears-Brustkreis); bewusst nicht perfekt passende Teile wirken wie gesammelte Beute. Belege: F04, F06, F18, YB12. Prüfung: Varianten-IoU
zur Grundfigur **Vorschlag** ≥ 0,9.

<a id="f-r4"></a>**F-R4 Große Formen und Kontrast oben.** Die größten, kennzeichnenden Formen liegen im oberen Körperdrittel (Schultern,
Kopf, Brust); hoher Kontrast und Details sitzen auf Brusthöhe, unten dunkler, oben heller; Detaildichte, Sättigung und Polygondichte
steigen von den Füßen zum Kopf. Belege: F06, YB05, F17, F03. Prüfung: Anteil der Teile mit Fein-/Akzentdetail oberhalb der Hüfte
**Vorschlag** ≥ 70 %; mittlere Helligkeit Oberkörper > Beine.

<a id="f-r5"></a>**F-R5 Blickrichtung an der Silhouette ablesbar.** Vorn und hinten unterscheiden sich im Umriss, damit Spieler erkennen,
ob die Figur kommt oder geht. Belege: F04, YB05. Prüfung (**Vorschlag**): IoU der an der Körperachse gespiegelten Seitensilhouette < 0,9.

<a id="f-r6"></a>**F-R6 Figur hebt sich von der Umgebung ab.** Kantenlicht (Rim/Fresnel) statt dunkler Umrisslinie, betont auf der
Oberseite; entfernte Figuren werden leicht aufgehellt; Freund/Feind über Kantenfarbe; Formschatten und AO werden überbetont, damit die
Form ohne Drehung liest. Belege: F01, F03, YB05, YB08. Prüfung: Laufzeit (Cube Escape/Unity), nicht im Modell; im Blender-Hero mit Rim-Licht.

### 3.2 Form, Proportion, Größe

<a id="f-r7"></a>**F-R7 Formsprache nach Rolle.** Quadrat steht für Stabilität und Stärke, Kreis für Harmlosigkeit, Dreieck und Schräge
für Gefahr und Tempo (Kiki/Bouba); bekannte Formen signalisieren eine Rolle ohne Erklärung (Horizon: T-Rex-Form = Gefahr). Figuren mischen
die Grundformen, eine dominiert. Belege: F06, F29, YB01, YA02 ([Ausrüstung](design-ausruestung.md#2-quellen)). Prüfung: dominierende
Grundform je Figur im Modulkopf festhalten, am Silhouettenbild prüfen.

<a id="f-r8"></a>**F-R8 Proportion bewusst wählen und messen.** Reale Erwachsene messen 7–8 Kopfhöhen, ab 8 beginnt die Heldenproportion;
Overwatch nutzt bewusst vielfältige, übertriebene Proportionen (Reinhardt überlebensgroß); massige Rüstung macht Figuren schwer;
Körperbauten unterscheiden sich über eigene Skelette (lang und stelzig gegen gedrungen). Belege: F28, F05, F07, F19, F12. Prüfung:
Körperhöhe ÷ Kopfhöhe (Scheitel bis Kinnunterkante bzw. Helmunterkante) als Kennzahl im Spec.

<a id="f-r9"></a>**F-R9 Größenklassen staffeln.** Gegner und NPCs werden in klein/mittel/groß gestaffelt („Dinosaur chart“); die
Silhouettengröße signalisiert die Rolle (große, gepanzerte Figuren = Tank/Kämpfer); große Flächen statt dünner Beine bieten Trefferfläche.
Belege: F18, F04, F13. Prüfung: Höhe je NPC-Typ als Vielfaches der Spielerfigur im Spec.

<a id="f-r10"></a>**F-R10 Form zuerst aus Grundkörpern, Maquette prüft Balance.** Proportion aus einfachen Primitiven, dann Detail;
Titanfall baute physische Kitbash-Maquetten, an denen Schwerpunkt und Balance sofort sichtbar waren – reale Teile sind nie perfekt und
wirken dadurch glaubwürdig. Belege: F26, F27, F11, YB06, YB07, YB02. Prüfung: Proportionsblatt aus Grundkörpern und Schwerpunkt über der
Standfläche vor jeder Schale.

<a id="f-r11"></a>**F-R11 Maßstab früh festlegen.** Der Maßstab Figur zu Welt und zu Ausrüstung wird früh fixiert, weil Level und Ausrüstung
darauf aufbauen (Titanfall: Maquette neben einer Actionfigur ergab den 20-Fuß-Titan); Hände dürfen für die Lesbarkeit gehaltener Waffen
vergrößert werden (Valorant); Hände statt Waffenarme erlauben Greifen und Werfen. Belege: F11, YB06, A24 ([Ausrüstung](design-ausruestung.md#2-quellen)).
Prüfung: Handbreite, Griffumfang, Schulterbreite und Augenhöhe als Kennzahlen im Spec, Waffe an `Socket_Hand` ohne Durchdringung.

### 3.3 Farbe, Material, Spielregeln

<a id="f-r12"></a>**F-R12 Hell/Dunkel vor Farbe, Akzente sparsam.** Wertgruppen tragen die Lesbarkeit mehr als Farbton; gedämpfte
Hauptflächen, kleine gesättigte Akzente; zu viele Lichter und Farben ergeben das „Weihnachtsbaum“-Problem; drei Materialfamilien
(Panzer, Stoff, Anzug) steuern Farbe und Glanz (Destiny „Dyes“). Eine 60-30-10-Verteilung nennt nur eine Meinungsquelle. Belege: F02, F16,
F17, F14, YB04, F30. Prüfung: Graustufenbild zeigt Kopf, Rumpf, Gliedmaßen getrennt; Leuchtstellen gezählt.

<a id="f-r13"></a>**F-R13 Spielregeln an der Form.** Treffer- und Schwachstellen sind am Körper ablesbar; abschießbare oder interaktive
Teile sind heller als der dunklere Körper (Horizon Forbidden West); Maschinen nutzen ein Exoskelett mit weicher Zone als Schwachstelle.
Belege: F13, F14, YB02, YB01. Prüfung: Schwachstellen und abtrennbare Teile als eigene Teilklasse mit eigener Materialrolle und Wertstufe.

### 3.4 Baugruppen, Gelenke, Rig

<a id="f-r14"></a>**F-R14 Baukasten mit Slots und Budgets.** Figuren bestehen aus Bausteinen und Slots (Kopf, Brust, Arme, Beine plus ein
Klassenslot); ein Fix am Baustein wirkt auf alle Sätze; Bausteine sind einzeln als in Ego-Sicht sichtbar oder unsichtbar markiert; das
Budget wird je Slot verteilt (Destiny, PS3/360: Titan-Arm 1024 × 512 Textur und etwa 170 k Geometriespeicher, Warlock-Arm 512 × 512 und
etwa 110 k); Bibliotheken bewährter Teile sichern einen einheitlichen Look. Belege: F15, YB04, F17, YB02, YB03. Prüfung: Budget je
Baugruppe und Ego-Sichtbarkeit je Teil im Spec.

<a id="f-r15"></a>**F-R15 Gesamtbudget nach Rolle.** Overwatch rechnet etwa 30 000 Dreiecke je Held und 15 000 für Waffen und Zubehör,
rund 30 MB Texturen; Knochen hart bis 1024, Ziel unter 500 simulierte. Belege: YB09, F27. Prüfung: Dreiecke und Knochen je Figur im Spec gegen
das gewählte Budget ([Frage F6](#frage-f6)).

<a id="f-r16"></a>**F-R16 Panzerteile starr, je Teil ein Knochen.** Harte Schalen werden starr an genau einen Knochen gebunden (maximaler
Einfluss 1 statt 4 bei biegsamen Figuren); automatische Gewichte machen Mechs weich; weiche Verbinder (Unteranzug, Schläuche) verformen
sich oder werden an zwei Enden gebunden, damit sie gleiten; stark überlappende Teile wurden bei Destiny wegen des Aufwands vereinfacht.
Belege: YB13, YB14, YB04, F21, F22, F33. Prüfung: jedes Teil der Rolle Schale/Panzer hat genau einen Elternanker.

<a id="f-r17"></a>**F-R17 Gelenke für die Pose bauen.** Schulterpanzer bewegen sich relativ zum Arm (Hilfsknochen, Einfluss nach
Armhöhe), Brustpanzer enden an der Taille, segmentierte Schulter- und Hüftplatten lassen Heben und Beugen zu; ein einteiliger Brustpanzer
verbietet Armheben über 180° und Bewegung der oberen Wirbelsäule; zwischen Platten bleibt Luft; Ausrüstung kann Posen begrenzen (Meis
Schlauch hält eine Hand an der Waffe). Belege: F31, F32, F22, F33, YB11. Prüfung: **Posensatz** (Arm oben, Arm vor der Brust, tiefe Hocke,
Ausfallschritt, Rumpfdrehung ±45°) mit Durchdringungsprüfung je Teilpaar; **Vorschlag:** Abstand zwischen Platten ≥ 1 mm in Grundhaltung
(Meinungsquelle F33 nennt 1–3 mm).

<a id="f-r18"></a>**F-R18 Extremposen früh testen.** Erst das Rig in extremen Posen zeigt, ob Mechanik und Teile zusammenpassen; Clipping
zwischen Rüstungsteilen wird in einem Betrachter geprüft. Belege: F20, F15, YB04. Prüfung: Posensatz aus F-R17 in jeder Sichtungsrunde.

<a id="f-r19"></a>**F-R19 Topologie nur dort für Verformung.** Kantenschleifen braucht, was sich verformt (Schulter/Achsel, Ellbogen, Knie,
Hüfte, Hände); Richtwerte am Ellbogen: Spielfigur 4–6 Schleifen, Heldenfigur 6–8; Pole nicht auf die Biegelinie; Biegetest bei 45° und
90°; im Low-Poly sind Dreiecke erlaubt, jede Kante braucht einen Grund. Starre Roboterteile brauchen keine Verformungsschleifen.
Belege: F23, F24, F25, F26, YB08, F21. Prüfung: verformte Teile mit Schleifenzahl im Spec; Biegetest 45°/90°.

### 3.5 Funktion und Bewegung

<a id="f-r20"></a>**F-R20 Funktion glaubwürdig, Vorbild Natur oder Technik.** Gelenke, Hydraulik und Ausrüstung (Taschen, Gurte) sind
nachvollziehbar; die Bewegung folgt den mechanischen Gelenken; Maschinen kombinieren Merkmale statt ein Vorbild zu kopieren, Form folgt der
Rolle; Überdesign vermeiden, jedes Element liest sich auf den ersten Blick. Belege: F06, F10, F13, F20, YB01, YB06. Prüfung: jedes
sichtbare Gelenk hat Drehachse und Anschlag im Spec.

<a id="f-r21"></a>**F-R21 Bewegung organisch, Roboterruck nur als Stilmittel.** Mechanisch ruckelnde Bewegung trug bei Horizon bei höherem
Tempo nicht; die Maschinen bewegen sich nach Tiervorbildern mit gelegentlichem Ruck, roboterhafte Bewegung blieb einer Klasse vorbehalten;
Titanfall skalierte Bewegungsaufnahmen auf das Titan-Rig für organischere Bewegung. Belege: YB10, YB06. Prüfung: Laufzeit/Animation –
Ruckanteil als Parameter je Figurenklasse.

**Selbstprüfung** (Skript über die Beleglisten gegen `data/design_quellen.json`): 21 Regeln, jede ID existiert, jede Regel hat mindestens
zwei Belege und mindestens eine Primärquelle.

## 4. Abgleich mit BALLON Stil v2.1

BALLON hat **kein eigenes Figuren-Stilhandbuch**. Grundlage sind
[Stilhandbuch v2.1 › 10 Arme und Animation](https://github.com/ffunkfabian-hash/cubeescape-ballon/blob/main/docs/stilhandbuch.md) (Formregeln Arm v3),
die [Roboter-Übergabe](https://github.com/ffunkfabian-hash/cubeescape-ballon/blob/main/docs/uebergabe-roboter.md) (Heldensilhouette, Zielbild
des Nutzers) und `basic/arms/robot_figure.py` (Roboter v2, „keine Spielfigur“; Höhe 1860 mm, Kopfsegment 1470–1760 mm, Schultergelenke
±215 mm, Hüfte 960 mm) – BALLON `main` c6fe8d6, 28.10.2026, nur gelesen.

### 4.1 Schon abgedeckt

| Regel | Stelle in BALLON | Bemerkung |
|---|---|---|
| F-R3 | Arm v3: „Medaillon … das Wiedererkennungsmerkmal“; Roboter: Medaillons an Schultern, Ellbogen, Knien | Leitmotiv wie Gears-Brustkreis |
| F-R4 | Übergabe: „breite, runde Schultern, V-Rumpf mit schmaler Taille“ | große Formen oben ✓; Kontrast auf Brusthöhe: Zielbild „Brustplatte mit einzelnem rundem Sensor“ |
| F-R7 | Roboter v2: gerundete Querschnitte nach „viel zu kantig“, Medaillons (Kreis) auf kastigem Grundaufbau | Mischung Kreis + Quadrat vorhanden, nicht benannt |
| F-R12 | helle Platten über dunklem Unteranzug, „kein Leuchten außer der Augenlinie“, je Teil höchstens eine Akzentlinie | ✓ |
| F-R14 | Übergabe 0.5 „Teardown“: fünf Baugruppen Kopf, Arme, Ober-/Unterkörper, Beine mit `Socket_*`-Ankern | Slots ✓, Budgets je Slot ✗ |
| F-R16 | Arm v3 und Roboter: Teile je Segment (`segment-typ`), konvexe Hüllen | starr je Segment ✓ |
| F-R20 | Zielbild: „sichtbare Gelenke, kleine Hydraulik, nachvollziehbare Verbindungen“; Arm v3 Kardan-Handgelenk | ✓ |

### 4.2 Fehlt

| Regel | Was fehlt |
|---|---|
| F-R1, F-R5 | Silhouettenprüfung (Ansichten, Verwechslung mit NPCs), Vorn/Hinten-Unterscheidung im Umriss |
| F-R2 | festgelegte Lesereihenfolge |
| F-R6 | Kantenlicht/Fresnel als Laufzeitregel (Cube Escape); BALLON-Hero nutzt Rim-Licht nur im Render |
| F-R8 | Proportion als Kennzahl (Kopfhöhen) im Spec |
| F-R9, F-R13 | Größenklassen und Schwachstellen für NPCs/Gegner (Cube Escape) |
| F-R11 | Maßregel Hand ÷ Griff ÷ Schulter für die Außenansicht; der Roboter nutzt den Ego-Arm v3 unverändert |
| F-R15 | Dreiecks- und Knochenbudget der Figur |
| F-R17, F-R18 | Posensatz mit Durchdringungsprüfung (Übergabe 0.5 prüft nur „keine Lücke in der Grundhaltung“) |
| F-R19 | Topologie weicher Teile (Unteranzug in den Fugen) |
| F-R21 | Bewegungsstil der ganzen Figur (Arm-Animation hat Federn und Atmen, die Figur keine Regel) |

### 4.3 Widerspricht oder steht in Spannung

| # | BALLON | Quelle | Art |
|---|---|---|---|
| W1 | Übergabe-Vorschlag „Kopf etwa 10 % größer“; Roboter v2 misst 1860 mm bei 290 mm Kopfsegment ≈ 6,4 Segmentlängen (Segment, nicht gemessene Kopfhöhe) | F-R8: 7–8 Kopfhöhen real, ab 8 Held (F28); Zielbild des Nutzers „schlanker humanoider Körper, lange gepanzerte Beine“ | Proportion – ein größerer Kopf führt weg vom schlanken Zielbild ([Frage F1](#frage-f1)) |
| W2 | Roboterarme = Ego-Arm v3 unverändert (Vorschlag der Übergabe, Entscheidung offen) | F-R11: Hände für Waffenlesbarkeit vergrößern (A24); Außenansicht hat andere Bedürfnisse als Ego-Sicht | offene Abhängigkeit ([Frage F5](#frage-f5)) |
| W3 | Roboter v2: „keine Spielfigur“ | F-R15/F-R16/F-R19 setzen Rig, Budget und Topologie einer Spielfigur voraus | Status – Regeln greifen erst mit „BASIC GROSS“ als Spielfigur |

## 5. Entscheidungsliste

**Beantwortet am 29.10.2026** (Nutzer im Sightline-Chat, weitergegeben über das Postfach): „Alle wie empfohlen“ – F1–F9 A. Umsetzung in BALLON bzw. Cube Escape; dieses Doc hält nur die Antworten fest.

Nur Fragen; entschieden wird in BALLON (Roboter-Spielfigur, Ego-Arme) bzw. Cube Escape (Spielfigur, NPCs, Laufzeit). Format wie die
[Entscheidungsliste Motiongen](https://github.com/ffunkfabian-hash/cubeescape-ballon/blob/main/docs/entscheidungsliste-motiongen.md).
Einstufung und Aufwand wie in [design-ausruestung.md › 5](design-ausruestung.md#5-entscheidungsliste).

<a id="frage-f1"></a>**Frage F1 – Proportion der Roboter-Spielfigur?** (F-R8, W1; Stil, M)
- **A (Empfehlung):** Schlank nach dem Zielbild: etwa 7,5 Kopfhöhen (Helm gemessen), lange Beine, Kopf **nicht** vergrößern; Kennzahl im Spec.
- **B:** Heldenproportion 8 und mehr (breitere Schultern, längere Beine).
- **C:** Kompakt wie Roboter v2 (≈ 6,4 Segmentlängen) mit Kopf +10 % nach der Übergabe.
- Antwort (Nutzer im Sightline-Chat, 29.10.2026, Postfach cubeescape-nexogen#16 Kommentar 6489554081): „Alle wie empfohlen“ → **A** (Empfehlung)

<a id="frage-f2"></a>**Frage F2 – Formsprache je Rolle?** (F-R7; Stil, S)
- **A (Empfehlung):** Spielerfigur Quadrat mit Kreis-Akzenten (stabil, verlässlich; Medaillons), M-4 und freundliche NPCs kreisdominiert,
  Gegner mit Dreiecken und Schrägen; Grundform je Figur im Modulkopf.
- **B:** Eine Formfamilie für alle Figuren, Unterscheidung nur über Farbe und Größe.
- Antwort (Nutzer im Sightline-Chat, 29.10.2026, Postfach cubeescape-nexogen#16 Kommentar 6489554081): „Alle wie empfohlen“ → **A** (Empfehlung)

<a id="frage-f3"></a>**Frage F3 – Posensatz und Durchdringungsprüfung?** (F-R17, F-R18; Pflicht, sobald Spielfigur; M)
- **A (Empfehlung):** Fünf Posen (Arm oben, Arm vor der Brust, tiefe Hocke, Ausfallschritt, Rumpfdrehung ±45°) mit BVH-Prüfung je
  Teilpaar in `./check`, Plattenabstand ≥ 1 mm in Grundhaltung.
- **B:** Nur Grundhaltung ohne Lücke (Stand Übergabe 0.5).
- Antwort (Nutzer im Sightline-Chat, 29.10.2026, Postfach cubeescape-nexogen#16 Kommentar 6489554081): „Alle wie empfohlen“ → **A** (Empfehlung)

<a id="frage-f4"></a>**Frage F4 – Schulterpanzer und Brustpanzer?** (F-R16, F-R17; Stil, M)
- **A (Empfehlung):** Schale starr je Segment, Schulterpanzer an einem Hilfsknochen mit Einfluss nach Armhöhe, Brustpanzer endet an der
  Taille, Bauch zweigeteilt.
- **B:** Schulterpanzer fest am Oberarm, einteiliger Rumpf (einfacher, Arme nicht über Schulterhöhe).
- Antwort (Nutzer im Sightline-Chat, 29.10.2026, Postfach cubeescape-nexogen#16 Kommentar 6489554081): „Alle wie empfohlen“ → **A** (Empfehlung)

<a id="frage-f5"></a>**Frage F5 – Hände der Figur gegenüber der Ego-Hand?** (F-R11, W2; Stil, S–M)
- **A (Empfehlung):** Ein Handmaß für beide Ansichten (Ego-Arm v3), Änderungen am Ego-Arm wirken auf die Figur; Griffbreite 30 mm der
  Familie bleibt Bezug.
- **B:** Hand der Außenansicht 10–15 % größer (Valorant-Ansatz), Ego-Hand unverändert.
- **C:** Getrennt entscheiden, wenn die Figur Spielfigur wird.
- Antwort (Nutzer im Sightline-Chat, 29.10.2026, Postfach cubeescape-nexogen#16 Kommentar 6489554081): „Alle wie empfohlen“ → **A** (Empfehlung)

<a id="frage-f6"></a>**Frage F6 – Budget der Spielfigur?** (F-R15, W3; Stil, S)
- **A (Empfehlung):** Figur höchstens 30 000 Dreiecke, Ausrüstung getrennt gezählt, Knochen ≤ 100 (ohne Simulation); Warnung in `./check`.
- **B:** Ohne Budget, bis die Figur nach Unity geht.
- Antwort (Nutzer im Sightline-Chat, 29.10.2026, Postfach cubeescape-nexogen#16 Kommentar 6489554081): „Alle wie empfohlen“ → **A** (Empfehlung)

<a id="frage-f7"></a>**Frage F7 – Größenklassen für NPCs und Gegner in Cube Escape?** (F-R9, F-R13; Abnehmer Cube Escape, S)
- **A (Empfehlung):** Drei Klassen als Vielfaches der Spielerfigur (klein ≈ 0,6, mittel ≈ 1,0, groß ≥ 1,6), Schwachstellen hell auf dunklem Körper.
- **B:** Alle in Spielergröße, Unterscheidung über Form.
- **C:** In Cube Escape entscheiden.
- Antwort (Nutzer im Sightline-Chat, 29.10.2026, Postfach cubeescape-nexogen#16 Kommentar 6489554081): „Alle wie empfohlen“ → **A** (Empfehlung)

<a id="frage-f8"></a>**Frage F8 – Kantenlicht zur Lesbarkeit?** (F-R6; Laufzeit, Abnehmer Cube Escape, M)
- **A (Empfehlung):** Fresnel-Kantenlicht für Figuren in Unity, betont oben, Gegner farbig; keine Umrisslinie.
- **B:** Nur Szenenlicht.
- Antwort (Nutzer im Sightline-Chat, 29.10.2026, Postfach cubeescape-nexogen#16 Kommentar 6489554081): „Alle wie empfohlen“ → **A** (Empfehlung)

<a id="frage-f9"></a>**Frage F9 – Vorn/Hinten im Umriss?** (F-R5; Stil, S)
- **A (Empfehlung):** Rückenmodul (Kühl- oder Energieblock) gibt der Rückseite einen eigenen Umriss; vorn Visier und Brustsensor.
- **B:** Nur Visier vorn, Rücken glatt.
- Antwort (Nutzer im Sightline-Chat, 29.10.2026, Postfach cubeescape-nexogen#16 Kommentar 6489554081): „Alle wie empfohlen“ → **A** (Empfehlung)

## 6. Offen und nicht belegt

- **Hand ÷ Griff ÷ Schulter als Zahl:** keine Quelle; Valorant vergrößert Hände (A24) ohne Faktor, Titanfall nennt nur den Maßstab Pilot zu
  Titan. Eine Messung an Spielbildern wäre Motiongen-Arbeit, wenn [Frage F5](#frage-f5) eine Zahl braucht.
- **GDC „The Art of Overwatch“** (F08) und der Dota-2-Leitfaden (F17) waren nicht lesbar; Inhalte nur über Sekundärquellen (F07, F16).
- **Prüfwerte „Vorschlag“** (IoU 0,85/0,9, 70 % Detail oben, 1 mm Plattenabstand, Posensatz, Größenfaktoren, Knochen ≤ 100) sind
  Einschätzungen des Koordinators; vor Übernahme an der BASIC-Figur erproben.
