# Gestaltung von Ausrüstung – Designansätze aus Studio-Vorträgen, Breakdowns und Leitfäden

Recherche REF 0.30 „Blueprint“ (28.10.2026) für die Ausrüstungsreihe **BASIC** im Stil v2.1 (Projekt `cubeescape-ballon`) und für die
Werkzeuge von Cube Escape: wie Studios und Waffenkünstler Waffen, Werkzeuge, Geräte und Anbauteile gestalten – Formsprache, Formstufen,
Fasen, Fugen, Baukasten, Lesbarkeit in Ego-Sicht, Budgets, Materialzonen, Abnutzung. Hier stehen **Quellenaussagen und daraus
abgeleitete Regelvorschläge**; entschieden wird in BALLON bzw. Cube Escape ([5](#5-entscheidungsliste)). Keine Messung am Bild.
Maschinenlesbar: [`data/design_quellen.json`](../data/design_quellen.json) (gemeinsam mit den Figuren). Nachbarthema:
[Gestaltung von Spielfiguren](design-figuren.md); Messdaten zu Waffenform in Ego-Sicht: [Hüftlage](huefte.md), [Proportionen](proportionen.md),
[Oberflächen](oberflaechen.md), [Visiere](visiere.md).

**Glaubwürdigkeit:** **Primär** = Studio oder Künstler über die eigene Arbeit (Vortrag, Dev-Blog, ViDoc, Interview, eigener Breakdown) ·
**Sekundär** = Fachmagazin, Wiki, Handbuch, Lehrvideo über fremde Arbeit · **Meinung** = Forum, Blog ohne Projektbezug. Primär heißt
„aus erster Hand“, nicht „allgemeingültig“: jede Zahl gilt für das Projekt des Sprechers.

## 1. Quellen und Methode

- **Gesammelt** von drei Unteragenten (Sonnet 5.5): Webquellen Ausrüstung, Webquellen Figuren, YouTube für beide Ziele (nach Hinweis des
  Nutzers über Sightline, 28.10.2026). Vorgabe: jede Seite selbst aufgerufen, nichts aus dem Gedächtnis, Kernaussagen in eigenen Worten,
  höchstens ein Zitat unter 15 Wörtern je Quelle, keine Dateien geladen.
- **Geprüft** vom Koordinator (Opus 5.5): alle 31 Text-Links (29 Quellen, dazu zwei Zweitlinks) per `curl` aufgerufen (28.10.2026),
  10 Aussagen im Wortlaut der Seite gefunden (A02, A05, A06 ×3, A09, A13, A24, A26, A29); bei den Videos 4 yt-dlp-Zeilen selbst abgerufen
  (YA01, YA02, YA03, YA07) und 7 Untertitelstellen in 4 Videos nachgelesen (YA01 ×3, YA02 ×2, YA04, YA07). Ergänzt: A29 (Bungie, selbst gefunden); A26 aus dem Suchauszug durch den gelesenen Wikitext
  ersetzt. Nicht ladbar: A27 (GDC Vault in Wartung), A28 (nur Überschrift); A15 lud beim Unteragenten, beim Koordinator per `curl` 403.
- **Videos:** Kanal, Hochladedatum, Titel, Dauer und Bildrate genau aus `yt-dlp --print "%(channel)s|%(upload_date)s|%(title)s|%(duration)s|%(fps)s"`;
  Kernaussagen aus Beschreibung, Kapiteln und automatischen Untertiteln mit Zeitstempel (mm:ss). Keine Videos heruntergeladen.
- **Lücken:** Keine Bungie-Primärquelle mit Waffen-Modellierregeln (GDC Vault in Wartung; A29 und YA04 berühren nur Ablauf und Leitbild).
  Overwatch-Waffen nur über Fremdanalysen (A19, YA06). Halo und Titanfall nur indirekt (A05 aus Halo 5, A15/A20/YA03 Respawn).
  Feste Fasenbreiten in mm nennt keine Quelle – nur Verhältnisse (A06, A09).

## 2. Quellen

38 Quellen (29 Texte, 9 Videos), davon 25 Primär; nicht geladen 2 (A27, A28). IDs sind stabil; Anker `q-<id>`.

### Texte und Vorträge

- <a id="q-a01"></a>**A01** [How the VALORANT Arsenal was built](https://playvalorant.com/en-us/news/dev/how-the-valorant-arsenal-was-built/) – Sean "Oniram" Marino (VALORANT Art Lead); Riot Games; 2020-05-12 · Artikel · **Primär**
  - Vier Säulen für alle Waffen: geerdet/identifizierbar (Bezug zu realer oder genretypischer Waffe), ballistisch (Kugeln statt Laser, Mündungsfeuer und Animation passen dazu), taktisch (Animation zeigt Absicht und Präzision), kohärent (keine gemischten Fraktionen mit widersprüchlicher Formsprache).
  - Jede Waffe braucht eine eigene Silhouette, damit keine mit einer anderen verwechselt wird; zusätzlich mindestens ein Erkennungsmerkmal (z. B. Magazinlage, Spannhebel-Form).
  - Das Erkennungsmerkmal muss in Ego- und Außenansicht funktionieren; auch Mündungsfeuer und Nachlade-/Zieh-Rhythmus sind pro Waffe unterscheidbar und zeigen den Waffenzustand.
  - Anbauteile bleiben optisch minimal, damit sie die Waffe nicht überladen (Hologramm-Rotpunkt statt sperrigerer Optiken).
- <a id="q-a02"></a>**A02** [The Craft and Fantasy of VALORANT Weapon Skins](https://playvalorant.com/en-us/news/dev/the-craft-and-fantasy-of-valorant-weapon-skins/) – Preeti Khanolkar (Producer), Sean "Oniram" Marino (Art Lead); Riot Games; 2020-05-18 · Artikel · **Primär**
  - Ein Skin-Modell muss die Silhouette der Basiswaffe in Ego- und Außenansicht treffen und auch als abgelegte Waffe am Boden erkennbar bleiben.
  - Ein Skin darf auf dem Bildschirm weder weniger noch mehr Platz einnehmen als die Basiswaffe; Ausnahmen sind extrem selten und brauchen Design-Freigabe.
  - Mündungsfeuer behält Form und Größe der Basiswaffe, Fadenkreuz/Visier bleiben beim Zielen sauber lesbar.
  - Vor dem Modellieren muss ein Konzept drei Prüfungen bestehen: gewünschte Fantasie, baubar, passt in die Spielvorgaben; Ideenfindung fragt u. a. nach den Materialien der Waffe.
- <a id="q-a03"></a>**A03** [Artists, Engineers, and the tech behind Spline](https://playvalorant.com/en-us/news/dev/artists-engineers-and-the-tech-behind-spline/) – Chris Stone (Weapon Artist), Brandon Wang (Software Engineer); Riot Games; 2020-09-17 · Artikel · **Primär**
  - Shader-Effekte für Waffenskins werden als künstlerfreundlich einstellbare Bausteine gebaut und müssen in Leistungs- und Shaderbudgets passen, auch auf schwachen Rechnern.
  - Ein Effekt (Nebula) nutzte nur eine Cubemap-Fläche, horizontal kachelnd, plus eine Detailtextur; Texturen entstanden in Substance Designer.
  - Künstler schwächten einen Effekt ab, um Übelkeit/Bewegungsunruhe in der Ego-Ansicht zu vermeiden, und testeten das im Playtest.
- <a id="q-a04"></a>**A04** [How Riot Games Animates VALORANT Weapon Skins with Autodesk Maya](https://blogs.autodesk.com/media-and-entertainment/2026/10/20/riot-games-animates-valorant-with-autodesk-maya/) – Brendan Russert (Senior Animator, Riot Games), SIGGRAPH-2026-Vortrag; Blog von Autodesk; Riot Games / Autodesk; 2026-10-20 · Artikel · **Primär**
  - Ego-Animation läuft mit 60 Bildern/s und muss sofort lesbar sein und die Spielbeats treffen; fünf Kernaktionen: Equip, Fast Equip, Fire, Reload, Inspect.
  - Eine Waffenart hat feste Beats (Gewehr-Reload: Magazin raus, Munition zurücksetzen, feuerbereit); ein Skin darf andere Silhouette/Modell/Textur haben, übernimmt aber das Bewegungsfundament der Archetyp-Waffe.
  - Kleine Timing-Änderungen (2 Bilder kürzer beim Schwert, 3 Bilder mehr beim Hammer) ändern den Eindruck von Tempo und Gewicht, ohne die Bewegungsgeschwindigkeit zu ändern.
  - Ein Drachen-Skin machte den Feuerbereit-Moment zunächst nicht klar genug; Lehre: Spielinformation innerhalb der Fantasie lesbarer machen statt abschwächen. Keine Poly- oder Rigbudgets genannt.
- <a id="q-a05"></a>**A05** [Weapon Production: Building, Texturing, Lighting](https://80.lv/articles/001agt-weapon-production-building-texturing-lighting) – Patrick Sutton (Interview: Kirill Tokarev); 343 Industries (Halo 5), Artist dort Environment Artist; 2019-01-24 · Interview · **Primär**
  - Obergrenze für eine Ego-Waffe: etwa 30.000 Dreiecke, Zielwert etwa 20.000; weniger kann für Plattform-Effizienz oder zusätzliche Anbauteile nötig sein.
  - Dreiecke und Texel dorthin legen, wo der Spieler hinsieht (Kimme bei Zielen, runde Visiere ohne sichtbare Facetten, Lauf-Silhouette ggf. mit doppelter Dreieckszahl); gleichmäßige Texeldichte, außer bei tiefen Innenteilen.
  - Viele unterschiedliche Materialien für Material-Aufbruch; Rauigkeit über das Modell variieren und bei ähnlicher Rauigkeit unterschiedliche Muster verwenden (raue Gussmetalle vs. glatterer Kunststoff).
  - Overlays vor allem auf die Rauigkeit; Kantenabnutzung und Schmutz über Generatoren mit eigenem Grime.
- <a id="q-a06"></a>**A06** [Breakdown: How to Make a Weapon Look Realistic and Eye-Catching](https://80.lv/articles/breakdown-how-to-make-a-weapon-look-realistic-and-eye-catching) – Andrew Stokaliuk; Team from Earth (Lead Weapon Artist); 2026-07-30 · Breakdown · **Primär**
  - Silhouette und große Fugen bleiben echte Geometrie; Gewinde, Griffmuster und kleine Schrauben gehen in die Normal Map.
  - Zieltexeldichte 120-170 px/cm; ein Teil bei 165 px/cm auf 4096x2048 lag im Rahmen, dasselbe Teil auf quadratischem 4K kam auf 234 px/cm und sprengte das Budget. 12 Texture Sets in diesem Projekt.
  - Kleine Teile bekommen ein dünneres Bevel als große/mittlere (getrennte Materialien 'base' und 'small_det'); Bevel-Baking spart etwa 1 Tag bei kleiner Waffe, etwa 4 Tage bei komplexem Gewehr. Verdeckte Hülsen auf 50 % skaliert, kurz sichtbare auf 30 %.
  - Lesbarkeitsprüfung in 3 m (Silhouette, Materialkontrast, Hell/Dunkel-Balance) und 5 m (kleines Rauschen soll verschwinden); Abnutzung in fester Reihenfolge: Werksbasis, Lack, Kratzer, Staub, Öl, Fingerabdrücke, Kantenschäden, grober Schmutz.
- <a id="q-a07"></a>**A07** [Building Guns for DOOM](https://80.lv/articles/building-guns-for-doom) – Gregor Kopka (Interview: Kirill Tokarev); Waffen für id Software (DOOM); zuvor Crytek; 2017-05-09 · Interview · **Primär**
  - Erst große, markante Formen bauen, dann zu kleineren Details herunterarbeiten.
  - Das Modell wird für die Spielersicht gebaut, nicht für einen Außenbetrachter: die Seitenansicht ist zweitrangig, es zählt die gestreckte Ego-Perspektive; Waffe früh in die Engine bringen und den Kamerawinkel prüfen.
  - DOOM-Waffen sind deutlich größer in der Form und vermitteln Wucht und Brutalität; die Mechanik muss glaubwürdig und kraftvoll wirken, besonders bei Sci-Fi.
  - Animation, VFX, Sound und Design früh einbeziehen.
  - Zitat: „nobody cares about the side view—it's all about the stretched FP perspective“
- <a id="q-a08"></a>**A08** [Production of 3D Weapons for Video Games](https://80.lv/articles/production-of-3d-weapons-for-video-games) – Ethan Hiley (Interview: Kirill Tokarev); Treyarch (zuvor Raven Software); 2017-07-19 · Interview · **Primär**
  - Blockout aus einfachen Formen legt Silhouette und bewegliche Teile fest; früh ins Spiel bringen, um Maßstab und Handgefühl zu prüfen. Bei fiktiven Waffen ist das die Schlüsselphase.
  - Jede Waffe hat ein Ego-Modell (dichte Geometrie, feines Detail) und ein reduziertes Weltmodell; LODs reduzieren Detail mit Abstand.
  - Texturspeicher ist die Hauptgrenze: Zahl und Größe der Materialien pro Waffe kontrollieren, UV-Layout so, dass die Texeldichte dort am höchsten ist, wo es zählt.
  - Metallfinish und Abnutzung variieren, um Teile zu trennen; Kantenabnutzung leicht halten, Glanz- und Farbwechsel an Flächenkanten weich; bewegte Teile (Fire, Reload) einplanen, Geometrie hinter beweglichen Teilen mitmodellieren, Hände nicht verdecken.
- <a id="q-a09"></a>**A09** [Weapon Art: Modeling Workflow in Fusion 360, Blender, and ZBrush](https://80.lv/articles/weapon-art-modeling-workflow-in-fusion-360-blender-and-zbrush) – Moritz Mayer (Interview: Arti Sergeev); FlowFire Games (Berlin); Projekt privat (Sabre Assault Rifle); 2020-08-24 · Breakdown · **Primär**
  - Mehrere Silhouetten skizzieren, eine wählen, im Blockout die Proportionen anpassen; Gewichtsausgleich (z. B. Riemen gegen schweres Zielfernrohr).
  - Formhierarchie: Hauptkörper aus Profil-Skizze, dann subtrahierende Schnitte, dann kleinere Teile wie Halterungen und Schraubdome.
  - Der Körper hat kleinere Kantenfasen als der Gummigriff, damit beide Materialien unterscheidbar wirken (Fasenbreite als Materialsignal); harte Kanten liegen dort, wo Nähte schwer zu sehen sind, UV-Nähte entlang harter Kanten.
  - Low-Poly etwa 80k Dreiecke, laut Autor mehr als für Ego-Waffen nötig (Portfolio); Abnutzung geschichtet: eloxierte Deckschicht, Oxidschicht, blankes Metall; Triplanar-Maske hilft über UV-Nähte.
- <a id="q-a10"></a>**A10** [Weapon Production: Modeling and Rendering Tips](https://80.lv/articles/001agt-002mrs-003qxl-004adk-weapon-production-modeling-and-rendering-tips) – Daulet Bekishev (Interview: Ellie Harisova); keines (Privatprojekt, CZ-75); 2019-11-20 · Interview · **Primär**
  - Fasen/Fillets/weiche Kanten nur dort setzen, wo sie Form oder Silhouette tragen; erst ohne Fasen bauen, später hinzufügen ist leichter als entfernen. Weiche Kanten für das High-Poly in ZBrush ergänzen, nicht am Low-Poly.
  - Nur wirklich formgebende Schnitte modellieren; kleine Details bleiben der Textur (Substance Painter) überlassen.
  - Zahlen: High-Poly pro Detail etwa 6 Mio. Polygone (Dynamesh), Low-Poly etwa 39k Polygone ohne festes Limit; vor dem Abwickeln triangulieren; Smoothing Groups pro UV-Insel.
  - Abnutzungsreihenfolge: Stahl, Schutzlack, Kratzer, Staub, Öl/Fett/Fingerabdrücke, Kantenschäden, grober Schmutz, Beschriftung; Abnutzung dort, wo Referenzen sie zeigen.
  - Zitat: „Only very necessary form-creating cuts should be made.“
- <a id="q-a11"></a>**A11** [Weapon Art Tips: High Poly, UVs, Texturing](https://80.lv/articles/weapon-art-tips-high-poly-uvs-texturing) – Ohle Mathiebe (Interview: Kirill Tokarev); elite3d; 2019-10-11 · Interview · **Primär**
  - Grobe Fasen erzeugen ungleichmäßige Kurven und stören das Baking; jede Fase und Kante bewusst setzen. Keine festen Breiten genannt.
  - Details auf ebenen Flächen flach halten, damit sie sauber backen; Lochinnenseiten abschrägen, Schraubenkanten fasen, damit sie Licht fangen.
  - UVs nicht im 90-Grad-Winkel schneiden, Inseln möglichst zusammenhalten.
  - Abnutzung zeigt die Wartungsgeschichte: Fingerabdrücke, Ölschmierer, Zweischicht-Abnutzung mit Untergrundlack, Schmieröl nur in Teilbereichen.
- <a id="q-a12"></a>**A12** [3D Weapon Art Workflow](https://80.lv/articles/3d-weapon-art-workflow) – Malte Resenberger-Loosmann (Interview: Kirill Tokarev); Freelance (keine Studioangabe); 2018-08-29 · Interview · **Primär**
  - Eigene Kitbash-Grundformen (Würfel, Plane usw.) als wiederverwendbarer Satz; Low-Poly, High-Poly und Konzeptreferenz auf getrennten Ebenen halten.
  - Auf dem High-Poly breitere Fasen, damit Kanten glatt bleiben und später kein Aliasing entsteht; enge Fasen über das ganze High-Poly vermeiden.
  - Heute seien Polygone nicht der Engpass, sondern Texturraum (Speicher): Testpacks bei 512, Endpacking gespiegelter Teile bei 2048, Arbeitsauflösung 2K/4K je Shader; Innenteile und Kappen kleiner skaliert.
  - Materialien als Schichten von der Basis: Grundfarbe, Farb-/Rauigkeitsvariation, Rauschdetail, Metallkanten, kleine Schäden, Kratzer/Schmutz, AO; Materialnamen entsprechen Waffenteilen.
  - Zitat: „these days polygons are not the bottleneck but texture space (memory) is“
- <a id="q-a13"></a>**A13** [Weapon Art: Tips for Design, Texturing and Presentation](https://80.lv/articles/weapon-art-tips-for-design-texturing-and-presentation) – Patrick Sutton (Interview: Arti Sergeev); C77 Entertainment (Lead Vehicle/Weapon Artist); 2020-08-10 · Interview · **Primär**
  - Silhouette-Komplexität erhöhen, aber nur an ein bis zwei Stellen, damit sie auffallen.
  - Lichtakzente als Hierarchie aus einem großen, einem mittleren und einem kleinen Bereich mit 70-20-10-Verteilung (Hauptfläche, Nebenfläche, Rim-Licht).
  - Workflow: hochaufgelöster Blockout, daraus High-Poly mit Chamfers und Face Weighted Normals; Low-Poly durch Reduktion des Blockouts (Bevel-Span-Anpassung in MESHmachine); Booleans halten Formen lange editierbar.
  - Eigene Materialien und Grunge bauen, Kantenabnutzung pro Material maskieren, keine einheitlichen Unvollkommenheiten.
  - Zitat: „having one or two things pop can be really nice“
- <a id="q-a14"></a>**A14** [Experimenting with Weapon Design](https://80.lv/articles/experimenting-with-weapon-design/) – Christopher Stone (Interview: Kirill Tokarev); Riot Games; 2018-10-02 · Interview · **Primär**
  - Konzepte früh als Blockout in 3D testen und das Design ändern, wo es nicht übersetzbar oder funktional ist; die Designabsicht bleibt, auch wenn das Modell vom Konzept abweicht.
  - High-Poly mit Blick auf das Low-Poly bauen: Modifier erzeugen Stützschleifen und werden am Ende entfernt.
  - Floaters (schwebende Zusatzgeometrie) auf Produktionsassets, wenn sie dasselbe leisten wie modellierte Geometrie.
  - Materialien aus getrennten Abnutzungsschichten, jede einzeln abgestimmt.
- <a id="q-a15"></a>**A15** [Apex Legends – Texturing the Battle Royale Phenomenon of 2019](https://www.adobe.com/products/substance3d/magazine/apex-legends-texturing-battle-royale-phenomenon-2019.html) – Brian Burrell, Patrick Yeung, Wonjae Kim (Senior Artist Waffen); Respawn Entertainment; 2019-05-29 · Interview · **Primär**
  - Jede Waffe beginnt mit einem Konzept, das mindestens eine orthografische Profilansicht und eine Ego-Perspektiven-Ansicht enthält; Modellierung liefert High-Poly und ein voll abgewickeltes Viewmodel.
  - Je Teil ein Basismaterial, dessen Füllung Bumpiness oder Filter bekommt, damit es unterscheidbar bleibt; Materialbeschreibung weit genug treiben, damit die Waffe im Spiel nicht zu simpel wirkt.
  - Nach den Basismaterialien: Decals, Verschleiß, Verwitterung, Schrauben; Kombination aus Generatormasken und Handmalerei.
  - Das PBR-Leitfaden erlaubte für schwarze Nichtmetall-Albedo bei Waffen und Charakteren einen dunkleren Bereich als bei Umgebung für mehr Kontrast; Abnutzung trennt auffällige Legendary-Waffen von schmutzigeren Basisversionen.
- <a id="q-a16"></a>**A16** [Gunfire Reborn's Dragonchaser Reimagined as Painterly 3D Asset in Wayfinder's Style](https://80.lv/articles/gunfire-reborn-s-dragonchaser-reimagined-as-painterly-3d-asset-in-wayfinder-s-style) – Max Osta (Interview: Amber Rutherford); Hard-Surface-Artist, bisher Bungie (Destiny 2), Meta, jetzt Respawn; Projekt privat; 2026-10-19 · Breakdown · **Primär**
  - Materialzonen mit erzählerischem Grund (Holz vorn am Lauf, Stein am Körper, Jade/Gold als Akzente); Farbblockung vor dem Detail über ID-Map oder manuelle Polygon-Maskierung.
  - Stilisierte Abnutzung: Blur-Slope und Paint-Blur-Quantize-Stapel; Quantize auf AO/Curvature erzeugt gestufte Töne. Niedrige Metallizität, wo Reflexionen zu realistisch wirken (Jade etwa 0,2-0,4, Gold 0,6).
  - Ziel 'stilisiert, aber mit PBR-ähnlichem Eindruck'; Glanz an einzelnen Lichtern abschalten, damit Treffer nicht überglänzen.
  - Low-Poly: überwiegend N-Gons, Triangulation per Modifier, Weighted Normals wo nötig; Kantendetail nur dort, wo neue Kantenebenen es brauchen. Keine Dreieckszahl und keine feste Fasenbreite genannt.
- <a id="q-a17"></a>**A17** [The Staples of Hard Surface Material Design](https://80.lv/articles/the-staples-of-hard-surface-material-design) – Arthur Rodriguez; unabhängig (Soldier-76-Gewehr im Overwatch-Stil); 2016-03-08 · Interview · **Primär**
  - UVs vorab so geplant, dass Teile gleicher Materialart zusammenliegen und als Zonen getrennt texturiert werden können.
  - Feste Farben mit minimalem Verschleiß: Ziel war ein 'leicht gebrauchtes, aber sauberes' Gewehr; Farbkombinationen wurden durchprobiert und zur Waffenrolle passend gewählt.
  - Zuerst die Basis-Maps (Albedo, Metallic, Rauigkeit, Normal), dann Masken und Filter, zuletzt handgemalte Absplitterungen; Schrauben modelliert, Embleme als Height-only-Stempel.
- <a id="q-a18"></a>**A18** [Relic Weapon (GamesArtist Breakdown)](https://gamesartist.co.uk/relic-weapon-prop-lucas-mania/) – Lucas Mania; S4G School for Games (Studentenprojekt, Valorant/Overwatch-inspiriert); 2022-04-28 · Breakdown · **Primär**
  - Material-ID-Map backen und per Farbauswahl je Materialzone eine Maske erzeugen; Basismaterialien früh auf das ganze Mesh legen, damit sie gegeneinander abgewogen werden.
  - Jede harte Kante braucht eine UV-Naht, jede UV-Insel eine eigene Smoothing Group; Kantenglanzlichter entstehen beim Texturieren.
  - Gradient-Remap für Hauptmaterial (Messing): Lichter golden, verdeckte Bereiche ins gealterte Grünliche, Rauigkeit dort niedriger; Absplitterungen mit variierter Größe und Abstand statt großer Splitter überall.
  - Alle Bakes in 4K, 16 Bit gebacken, 8 Bit mit Dithering exportiert; keine Dreieckszahl genannt, Low-Poly entfernt Geometrie, die die Silhouette nicht beeinflusst.
- <a id="q-a19"></a>**A19** [Studying Overwatch Style](https://80.lv/articles/studying-overwatch-style) – Joe Maleski (Interview: Kirill Tokarev); unabhängig (Studie des Overwatch-Stils); 2017-08-16 · Interview · **Sekundär**
  - Overwatch-Stil: große, interessante Formen übertreiben, damit die Waffe über die Silhouette lesbar ist; Meshes arm an Feindetail.
  - Basisfarbe an konvexen Kanten aufhellen, damit Kanten hervortreten (Basisschicht duplizieren, aufhellen, mit Scratch-Maske maskieren).
  - Wenig Oberflächentextur; Metall-Effekte (Rost, gebürstet) gezielt maskieren; Rauigkeit nicht zu glänzend.
- <a id="q-a20"></a>**A20** [Apex Legends dev reveals original weapon concepts for R-301, R-99, more](https://www.dexerto.com/apex-legends/apex-legends-dev-reveals-original-weapon-concepts-for-r-301-r-99-more-1357761/) – Dexerto (zitiert Ryan Lastimosa, 3D Art Director Respawn); Respawn Entertainment; 2020-04-25 · Artikel · **Sekundär** · [zweiter Link](https://x.com/brockhaurd/status/1252045712558194689)
  - Neue Waffen beginnen als Silhouetten, die Form festlegen, plus Arbeitsteile, die die Funktion andeuten.
  - Ziel ist der 'Snap Read': Spieler erkennen die Waffe auf Distanz und passen ihre Taktik an. (Original ist ein Tweet von Lastimosa; der X-Link lieferte beim Abruf HTTP 402, der Inhalt stammt aus Dexerto.)
- <a id="q-a21"></a>**A21** [3D Weapon Art for Games: The AAA Production Pipeline Explained](https://nastyrodent.com/3d-weapon-art-for-games/) – Denys Zadoienyi; Nasty Rodent (Dienstleister, Tallinn); 2026-05-22 · Guide · **Sekundär**
  - Genannte Budgets für eine Ego-Haupt-Waffe: High-Poly 60.000-100.000 Dreiecke, Low-Poly 8.000-20.000 (Hauptgewehr 12.000-18.000, Seitenwaffen 6.000-10.000); 2K-4K-Texturen; Texeldichte 512-1.024 px/m bei 2K-Sets. Vorsicht: Dienstleister-Seite, Quellen der Zahlen nicht belegt, Gegenprobe mit A05 (30k Obergrenze).
  - Effektives Ego-FOV 35-55 Grad angegeben; Silhouette und Abzugsbügel müssen beim Ziel-FOV lesbar bleiben, nicht in einer 90-Grad-Vorschau.
  - 3-4 LODs je Waffe, LOD1 etwa 50 % der Dreiecke von LOD0 und noch als konkrete Waffe erkennbar.
  - PBR-Zielwerte: bearbeitetes Metall metallic 0,9-1,0 / roughness 0,2-0,5; Phosphatierung 0,8-0,9 / 0,5-0,7; Polymer metallic 0,0 / roughness 0,6-0,8.
- <a id="q-a22"></a>**A22** [Unreal Engine - Render First-Person Meshes with a Separate FOV (Viewmodel/First-Person/Weapon FOV)](https://sahildhanju.com/posts/render-first-person-fov/) – Sahil Dhanju; unabhängig (Entwickler-Blog); 2021-06-20 · Artikel · **Sekundär**
  - Viele Ego-Spiele trennen Welt-FOV und Viewmodel-FOV, damit Animationen und Waffenansicht nicht bei jeder FOV-Änderung neu abgestimmt werden müssen.
  - Eine bei FOV 60 gebaute Animation sieht bei FOV 120 sehr anders aus; im Test passte Viewmodel-FOV 60 bei Welt-FOV 120 besser zu Welt-FOV 80 als Viewmodel-FOV 80.
  - Anbauteile und Partikel am Viewmodel müssen gleich skaliert werden, sonst wirken sie verschoben; oft wird das Viewmodel in einem eigenen Durchgang über der Welt gezeichnet.
  - Zitat: „will look very different at a FOV of 120“
- <a id="q-a23"></a>**A23** [Riot Games' process of creating VALORANT guns and gun skins](https://www.invenglobal.com/articles/11213/riot-games-process-of-creating-valorant-guns-and-gun-skins) – Parkes Ousley (Inven Global); Berichterstattung über Riot Games; 2020-05-18 · Artikel · **Sekundär**
  - Fasst A01/A02 zusammen: jede Waffe erkennbar und optisch eigen, mit eigener Nachlade-Animation und konsistenten Audiohinweisen für den Waffenzustand.
  - Skin-Modelle, Effekte und Animationen sind nur in der Ego-Ansicht sichtbar; andere sehen nur das Modell; ein Skin belegt dieselbe Bildschirmfläche wie die Basiswaffe.
  - Keine Aussagen zu Silhouetten-Details oder Polygonbudgets (Hinweis: Datum aus Artikelkopf der Fassung, Riot-Original am 12./18.05.2020).
- <a id="q-a24"></a>**A24** [Valorant's art director reveals the one utterly modern question Riot Games had to ask itself](https://www.inverse.com/gaming/valorant-art-style-interview-moby-francke) – Tomas Franzese (Inverse), Interview mit Moby Francke (Art Director VALORANT); Riot Games (Berichterstattung); 2020-11-06 · Interview · **Sekundär**
  - Stil als 'illustrative visual design': scharfe Linien, saubere Verläufe, ansprechende Winkel; Mischung aus Realismus und Cel-Shading; einfacher und lebendiger, damit die Kunst das Gameplay stützt.
  - Waffen müssen gut sichtbar sein; deshalb vergrößerte das Team die Hände, die sie halten, damit die Waffe als Grafik klarer wirkt.
  - Beleuchtung, Charaktere, Waffen und Fähigkeiten müssen auf jeder Hardware klar bleiben (Zielhardware auch schwach).
- <a id="q-a25"></a>**A25** [Blender Manual: Bevel Modifier und Weighted Normal Modifier](https://docs.blender.org/manual/en/latest/modeling/modifiers/generate/bevel.html) – Blender Documentation Team; Blender Foundation; unbekannt · Wiki · **Sekundär** · [zweiter Link](https://docs.blender.org/manual/en/latest/modeling/modifiers/normals/weighted_normal.html)
  - Bevel-Modifier: Breitenarten Offset, Width, Depth, Percent (Anteil der Nachbarkante) und Absolute; Limit-Methode None/Angle/Weight/Vertex Group, Angle fast nur scharfe Kanten; Segments setzt Anzahl der Kantenschleifen in der Fase; Profil per Superellipse oder eigener Kurve.
  - Harden Normals gleicht Fasenflächen an die Nachbarn an und lässt diese flach; Face Strength vergibt Stärkewerte (None/New/Affected/All) für einen nachfolgenden Weighted-Normal-Modifier.
  - Weighted Normal: Modi Face Area, Corner Angle (Standard) und Kombination; Face Influence nutzt Stärkegewichte (weak/medium/strong), die stärkste Fläche bestimmt die Normale am Vertex; Keep Sharp erhält scharfe Kanten. Diese Kombination entspricht dem Face-Weighted-Normals-Verfahren mit wenigen Eckpunkten.
- <a id="q-a26"></a>**A26** [Face weighted normals (Polycount Wiki)](http://wiki.polycount.com/wiki/Face_weighted_normals) – Polycount Community (Admin Eric Chadwick verweist darauf); Polycount; unbekannt · Wiki · **Sekundär**
  - Face weighted normals: Fasen hinzufügen und die Eckpunkt-Normalen senkrecht auf die großen ebenen Flächen stellen; die Schattierung verläuft dann nur über die kleinen Fasenflächen statt über das ganze Modell.
  - Nachteil: Fasen erzeugen lange dünne Dreiecke, die die Renderleistung spürbar mindern können.
  - Werkzeuge: Blender Weighted-Normal-Modifier, 3ds Max Weighted Normals Modifier.
- <a id="q-a27"></a>**A27** [Translating Art into Technology: Physically Inspired Shading in 'Destiny 2'](https://gdcvault.com/play/1025382/Translating-Art-into-Technology-Physically) – Alexis Haraux, Nate Hawbaker; Bungie; 2018 · Vortrag · **Primär** · **nicht geladen** (Suchauszug)
  - Nur aus Suchauszug bekannt (GDC-Vault leitete auf die Wartungsseite https://gdconf.com/gdc-vault-maintenance/ um): GDC-2018-Vortrag über die physikalisch inspirierte Shading- und Beleuchtungs-Pipeline von Destiny 2.
  - Beschreibung erwähnt Waffen nicht ausdrücklich; Relevanz für Materialrollen und PBR-Vorgaben, Inhalt nicht geprüft.
- <a id="q-a28"></a>**A28** [Valve zoomed in Half-Life 2's FOV from the gold standard 90 so you could see all those pretty Source engine faces better](https://www.pcgamer.com/games/fps/valve-zoomed-in-half-life-2s-fov-from-the-gold-standard-90-so-you-could-see-all-those-pretty-source-engine-faces-better/) – PC Gamer (zitiert Valve-Entwickler Kerry Davis, 20th-Anniversary-Kommentar); Valve (Berichterstattung); unbekannt · Artikel · **Sekundär** · **nicht geladen** (Suchauszug)
  - Nur aus Suchauszug bekannt (beim Abruf kam nur die Überschrift, kein Text): Half-Life 1 nutzte 90 Grad FOV, Half-Life 2 wechselte auf 75 Grad, damit Gesichts- und Körperanimationen besser zur Geltung kommen.
  - Dafür war ein getrenntes Viewmodel-FOV nötig: die für 90 Grad gebauten Viewmodels wirkten bei 75 Grad verzerrt.
- <a id="q-a29"></a>**A29** [Destiny 2: The Final Shape – game art 10 years in the making](https://www.creativebloq.com/entertainment/games/the-art-of-destiny-2-the-final-shape) – Jess Kinghorn (Interview mit Michael Climer, Lead Hard Surface Art, u. a.); Bungie / Creative Bloq; 2024 · Interview · **Primär**
  - Waffen entstehen bei Bungie in einem 15-köpfigen Hard-Surface-Team; es gibt eine feste Zahl von Waffenarchetypen, Varianten je Saison.
  - Nach dem Konzept folgt ein Blockout als grober Prototyp, der im Spiel auf die Größe geprüft wird (‚nicht zu groß, nicht zu klein‘).
  - Waffen werden mit Umgebung, Geschichte und Art-Direction verknüpft (Motiv, Hintergrund), nicht nur als ‚cool aussehende Waffe‘ entworfen; Blender ist im Team zunehmend verbreitet, die Software ist frei wählbar.
  - Zitat: „not too big, it's not too small“

### Videos (YouTube, per yt-dlp geprüft)

- <a id="q-ya01"></a>**YA01** [The Art of Destiny's First-Person Animation](https://www.youtube.com/watch?v=CXFLu8cityA) – Kanal GDC Festival of Gaming, Sprecher David Helsby (Senior Animator, Bungie); Bungie; hochgeladen 2017-03-19, 60:41 min, 30 fps · Vortrag · **Primär**
  - Das Reticle sitzt bei Bungie seit Halo 2 unter der Bildmitte; das schafft Peripherie oben und seitlich, die die Welt weiter wirken lässt. (09:14, untertitel)
  - Alle Linien von Waffe und Armen sollen auf den Fluchtpunkt der Einpunktperspektive zulaufen, sonst wirkt das Viewmodel wie ein aufgesetztes Fenster-Dekor statt wie Teil der Welt. (10:14, untertitel)
  - Der Animationsraum im Ego-Bild ist eine kleine, durch extremes FOV verzerrte Box; außerhalb davon zählt nichts. Seitliche und obere Randzone sowie der mittlere 'Combat Corridor' sollen nicht mit Posen oder Waffenteilen zugestellt werden (ein Nachladen, das die Sicht verdeckt, wird als Designfehler benannt). (14:55, untertitel)
  - Das Auge wandert radial um das Reticle; Daumen/Zeigefinger oder Waffenteile können diesen Bereich rahmen und so die Aufmerksamkeit lenken. (16:27, untertitel)
  - Das Viewmodel besteht aus Armen, Kamera, einem Stützobjekt und der Waffe, abgeleitet vom Third-Person-Rig; alles oberhalb der Hüfte ist aus der Ego-Kamera nicht sichtbar. (07:39, untertitel)
- <a id="q-ya02"></a>**YA02** [Riot Artist Designs a Greek Gods’ VALORANT Skin - Super Art Power Hour Ep. 12](https://www.youtube.com/watch?v=KMFHILAsXzo) – Kanal Riot Games, Sprecher Denis Lakhanov (Senior Concept Artist, VALORANT); Riot Games; hochgeladen 2026-02-27, 57:28 min, 24 fps · Breakdown · **Primär**
  - Im kompetitiven Spiel darf jedes Detail, das vom Spielgeschehen ablenkt, nicht stören; Skin-Linien arbeiten deshalb mit vielen Einschränkungen. (04:35, untertitel)
  - Proportionen bestimmen den Rest der Waffe; Vandal und Phantom sind schon über wenige Großformen (Magazin, Gasrohr, Kolbenende bzw. gerade Hauptlinie) erkennbar, der Rest kann sich ändern, ohne dass es auffällt. (07:38, untertitel)
  - Eine durchgehende 'Charakter-/Schulterlinie' (aus dem Automobildesign) und eine untere Linie legen die Silhouette fest; weitere Linien müssen irgendwohin laufen und einen lesbaren Fluss bilden, weil das Gehirn Beziehungen zwischen Linien gern liest. (09:10, untertitel)
  - Dynamik gegen Statik: Dreiecke und Schrägen wirken dynamisch, Rechtecke statisch; Kiki-Bouba-Effekt steuert, wie aggressiv eine Silhouette wirkt. (12:18, untertitel)
  - Die interessantesten Teile gehören auf die kameranahe Seite, weil dort die Verzerrung am geringsten ist; die Waffenfront wird von der Kamera am stärksten verzerrt, dort wirken zwei dicht beieinanderliegende Aussparungen wie eine Linie, also keine feinen Details. (15:24, untertitel)
  - Funktionale Elemente (Knöpfe, Regler) bringen Glaubwürdigkeit und Persönlichkeit und zeigen, wie man die Waffe bedient. (16:57, untertitel)
  - Material-Splits (z. B. weicher Gummischaft an der Schulter) und bewegliche Teile (Lüfter) sind Plan für spätere Inspect-Animationen; ein statisches Objekt erlaubt nur Hand-Animation. (27:49, untertitel)
- <a id="q-ya03"></a>**YA03** [How to Create Weapons for AAAs \| #SpeakEasy E14 with Ryan Lastimosa](https://www.youtube.com/watch?v=lNH48I-TebA) – Kanal Devoted Talks, Sprecher Ryan Lastimosa (ex-Creative Director, Respawn; Call of Duty 4, Titanfall, Apex); Respawn Entertainment (Interview); hochgeladen 2023-03-14, 30:27 min, 30 fps · Vortrag · **Primär**
  - Waffenartisten müssen verstehen, wie Waffen funktionieren; Ergonomie und Mechanik entstehen aus Jahrhunderten Feuerwaffenentwicklung, erst auf dieser Basis darf die Form verspielter werden. (06:17, untertitel)
  - Spielwaffen lehnen sich an bekannte reale Plattformen an (AK, M14, M4), damit Spieler sie unbewusst als funktionsfähig lesen; Science-Fiction soll so geerdet sein, dass jedes Teil eine erkennbare Funktion hat. (03:06, untertitel)
  - 'Tactile Referencing': Wie bei Handy oder Kühlschrank soll man Bedienelemente ohne Hinsehen finden; das gilt für Ego-Waffen, weil der Spieler auf Gegner statt auf die Waffe schaut. (11:24, untertitel)
  - Archetypen werden gezielt gebaut (R-101 bis R-301 als kleinkalibrige schnelle Plattform, Flatline als großkalibrige langsame), weil jede Waffe ein Problem im Spiel lösen soll. (14:27, untertitel)
  - Bei Rarity-Varianten (Legendary, Heirloom) dürfen Aufbauten übertrieben sein, bleiben aber nur glaubwürdig, wenn die Grundfunktion stimmt. (08:20, untertitel)
  - Zitat: „form will always follow function“
- <a id="q-ya04"></a>**YA04** [The Artists of Destiny](https://www.youtube.com/watch?v=y4GxZ0pjNds) – Kanal Bungie, Sprecher Bungie-Künstler (Namen nicht in den Metadaten); Bungie; hochgeladen 2016-05-18, 81:10 min, 30 fps · ViDoc · **Primär**
  - Leitprinzip 'idealisierte Realität': reale Vorbilder werden analysiert und das, was sie spannend macht, stark überhöht, statt Realismus um des Realismus willen zu bauen. (05:05, untertitel)
  - Waffenmarke Suros: 'weniger ist mehr', Vorbild ist Formel-1-Industriedesign (Formel 1 der Hersteller), zusätzlich Braun/Dieter Rams; Leitsatz 'Eleganz inmitten von Brutalität'. (39:57, untertitel)
  - Weil Waffen zu 99 % in Ego-Sicht gesehen werden, wurde ein Konzeptdetail verschoben, damit es im Ego-Bild besser lesbar ist; Konzeptkünstler müssen sich selbst gegenüber Gameplay-Realitäten prüfen. (40:58, untertitel)
  - Embleme und Icons bestehen aus primitiven Formen derselben Formensprache und sollen nicht überdesignt sein, weil sie als Muster dauernd auftauchen. (37:51, untertitel)
- <a id="q-ya05"></a>**YA05** [How Gearbox Designs New Weapons in Borderlands 4 \| Exclusive](https://www.youtube.com/watch?v=XuyRbrk07eU) – Kanal Game Informer, Sprecher Graeme Timmins, Grant Kao (Gearbox), Randy Pitchford; Gearbox Software (Interview); hochgeladen 2025-06-27, 13:54 min, 60 fps · ViDoc · **Primär**
  - Gearbox erzeugt Waffen seit 2008 prozedural aus Komponenten, Materialien und weiteren Variablen; ein einzelnes Ego-Modell von Hand zu bauen, skaliert nicht auf Hunderte oder Milliarden. (01:35, untertitel)
  - Jede Herstellermarke bekommt eine eigene Verhaltens- und Gestaltungsidentität; in Borderlands 4 wurden die Teile in feste Kategorien gegliedert, damit Spieler (und Kunstproduktion) eine Rolle pro Teil klar zuordnen können. (05:07, untertitel)
  - Design-'Lanes' sollen verhindern, dass eine Waffe alles kann; Marken-Eigenheiten werden isoliert, um die Kunstproduktion nicht zu überlasten. (04:36, untertitel)
- <a id="q-ya06"></a>**YA06** [How Overwatch Conveys Character in First Person](https://www.youtube.com/watch?v=7Dga-UqdBR8) – Kanal New Frame Plus, Sprecher Daniel Floyd (Animator; mit Matt Boehm, Blizzard, als Quelle); New Frame Plus (Analyse zu Overwatch); hochgeladen 2018-06-25, 15:31 min, 60 fps · Breakdown · **Sekundär**
  - Overwatch hält Hände und Waffe fast immer im Bild, damit das Waffendesign auf einen Blick zeigt, wen man spielt. (03:05, untertitel)
  - Zustand der Waffe erzählt über den Besitzer: Soldier 76 präzise und gepflegt, Junkrats Werfer klappert und ist notdürftig zusammengebaut, Bastions Teile sitzen locker. (03:05, untertitel)
  - Jede Figur hat eigenen Idle-, Atem- und Gehrhythmus; Waffensway und Nachziehen beim Kameraschwenk unterscheiden sich je Waffengewicht. (05:06, untertitel)
  - Charakterisierung geht nie auf Kosten der Spielfunktion (z. B. Kameraneigung statt voller Rolle beim Dodge). (12:16, untertitel)
- <a id="q-ya07"></a>**YA07** [Primary, Secondary And Tertiary Shapes](https://www.youtube.com/watch?v=6IojuePYIHo) – Kanal ArtOfSoulburn, Sprecher Neil Blevins; ArtOfSoulburn; hochgeladen 2020-08-07, 13:52 min, 30 fps · Tutorial · **Sekundär**
  - Ein Bild sollte große, mittlere und kleine Formen haben; beim Zusammenkneifen der Augen bleiben nur die Primärformen. (01:31, untertitel)
  - 70/30-Regel: Teilt man eine Form in zwei, wirkt 70:30 besser als zwei gleich große Hälften; das gilt auch eine Stufe tiefer für Tertiärdetails. (04:33, untertitel)
  - Details nicht gleichmäßig verteilen oder gleich groß machen; es braucht Cluster und fast detailfreie Ruhezonen. Prozedurales Rauschen hat nur Tertiärdetail und wirkt langweilig. (06:03, untertitel)
  - Manchmal reichen drei Stufen nicht; Blevins nutzt vier 'Reads' (1. bis 4. Blick), z. B. beim schwebenden Loader-Roboter. (11:14, untertitel)
- <a id="q-ya08"></a>**YA08** [10 Weapon Design Tips for 3d Artists](https://www.youtube.com/watch?v=yvC5Xq3jjBM) – Kanal Tosmo, Sprecher Tosmo; Tosmo (3D-Künstler); hochgeladen 2020-10-19, 21:05 min, 30 fps · Tutorial · **Sekundär**
  - Vor dem Modellieren klären: Wer nutzt die Waffe, wo, wer hat sie gebaut, welche Munition. (01:31, untertitel)
  - Mit flachen 2D-Ebenen die Waffensilhouette ausschneiden, dann extrudieren und von einfachen Formen aus verfeinern. (14:55, untertitel)
  - High-to-Low-Workflow, N-Gons vermeiden, LODs mit weniger Geometrie bei Entfernung; Triangulierung muss zwischen Exporten gleich bleiben, sonst bricht der Bake. (16:04, untertitel)
  - Verschmutzung und Korrosion nur dort, wo sie logisch entstehen; Waffen müssen für Rückstoß- und Nachlade-Animation, Anbauteile und Skins vorbereitet sein. (18:06, untertitel)
- <a id="q-ya09"></a>**YA09** [Hard Surface Modeling 101: Beginner's Guide](https://www.youtube.com/watch?v=Y-DtNmlRZf8) – Kanal Mesh Labz, Sprecher Mesh Labz; Mesh Labz; hochgeladen 2025-01-02, 4:56 min, 30 fps · Tutorial · **Sekundär**
  - Hard Surface bedeutet scharf definierte Kanten und präzise Winkel (Maschinen, Waffen, Fahrzeuge); sauberer Edge Flow wirkt auf Glanzlichter und Subdivision. (00:34, untertitel)
  - Jede reale Kante hat eine Fase; Fasen fangen Licht und machen Objekte greifbar. (03:09, untertitel)
  - Für Spielmodelle genügt oft ein einziger Bevel-Durchgang, während High-Poly-Modelle mehr Segmente erlauben. (04:09, untertitel)

## 3. Gestaltungsregeln

Abgeleitet aus den Quellen in [2](#2-quellen); jede Regel nennt ihre Belege (IDs) und, wo möglich, eine Prüfung, die ein Generator
(Python/Blender, Autorenmaß mm wie BALLON `f`/`u`/`x`) selbst ausführen kann. **Zahlen aus Quellen** sind Angaben eines Studios oder
Künstlers für sein Projekt, keine Normen; **Prüfwerte ohne Quelle** sind als „Vorschlag“ gekennzeichnet und erst nach einer Entscheidung
([5](#5-entscheidungsliste)) verbindlich.

### 3.1 Form und Silhouette

<a id="a-r1"></a>**A-R1 Silhouette je Klasse eindeutig.** Jede Klasse hat eine eigene Silhouette plus mindestens ein Erkennungsmerkmal
(Magazinlage, Hebelform, Laufform), das in Ego-Sicht, Außenansicht und als abgelegte Waffe funktioniert; die Klasse liest sich schon an
wenigen Großformen (Magazin, Gasrohr, Kolbenende), der Rest darf variieren. Ziel ist die Erkennung auf Distanz auf einen Blick.
Belege: A01, A02, A20, A08, YA02, YA03. Prüfung: schwarze Seitensilhouetten aller Klassen auf gleiche Länge normiert;
**Vorschlag:** paarweise Überdeckung (IoU) < 0,85, sonst Leitmerkmal schärfen.

<a id="a-r2"></a>**A-R2 Vom Großen zum Kleinen, Blockout zuerst im Spiel.** Erst große markante Formen, dann mittlere, zuletzt kleine;
der Blockout aus einfachen Körpern (Seitenprofil ausschneiden, extrudieren) legt Silhouette und bewegliche Teile fest und wird früh in
Spielkamera und Hand geprüft – Bungie: „nicht zu groß, nicht zu klein“. Belege: A07, A08, A09, A14, A29, YA08. Prüfung: der Generator
rendert nach dem Blockout (nur Hauptkörper) Ego- und Seitenbild, bevor Detailbausteine dazukommen.

<a id="a-r3"></a>**A-R3 Drei Lesestufen mit Ruhezonen und Clustern.** Große, mittlere und kleine Formen; Details nicht gleichmäßig verteilen
und nicht gleich groß machen, sondern in Clustern bündeln und fast detailfreie Ruhezonen lassen; beim Zusammenkneifen der Augen bleiben nur
die Primärformen. Prozedurales Rauschen liefert nur die dritte Stufe und wirkt allein langweilig. Belege: YA07, A13, A19, YB03
([Figuren](design-figuren.md#2-quellen)). Prüfung: Anteil der Teile je Detailstufe im Modulkopf; Kleinteile in höchstens **Vorschlag** drei Clustern.

<a id="a-r4"></a>**A-R4 Teilungen ungleich, etwa 70:30.** Wird eine Form geteilt (Schale/Unterbau, Haube/Gehäuse, Farbblöcke), wirkt
eine Teilung nahe 70:30 besser als zwei gleich große Hälften; das gilt eine Stufe tiefer wieder. Belege: YA07, A13 (70-20-10 für
Glanzzonen). Prüfung (**Vorschlag**): Längen- bzw. Flächenverhältnis benachbarter Hauptblöcke außerhalb 0,4–0,6.

<a id="a-r5"></a>**A-R5 Silhouetten-Komplexität an ein bis zwei Stellen.** Die Umrisslinie bleibt überwiegend ruhig; Brüche, Auskragungen
und Zacken im Umriss bündeln sich an ein bis zwei Stellen. Eine durchgehende obere „Schulterlinie“ und eine untere Linie legen die
Silhouette fest, weitere Linien laufen in diese hinein. Schrägen und Dreiecke wirken dynamisch, Rechtecke ruhig. Belege: A13, A19, YA02.
Prüfung (**Vorschlag**): Seitenumriss in Abschnitte von 5 % der Länge teilen; Richtungswechsel > 45° in höchstens zwei zusammenhängenden Zonen.

<a id="a-r6"></a>**A-R6 Idealisierte Realität, Form folgt Funktion.** Reale Vorbilder werden analysiert und das Spannende überhöht;
Sci-Fi bleibt so geerdet, dass jedes Teil eine erkennbare Funktion hat (Anlehnung an bekannte Waffenplattformen, Ergonomie aus
realen Waffen). „Weniger ist mehr“ als Markenhaltung (Bungie Suros: Industriedesign, Dieter Rams). Belege: YA03, YA04, A01, A07.
Prüfung: jedes Bauteil hat im Spec ein Funktionsfeld (`func`), Zierteile ohne Funktion werden gezählt.

### 3.2 Ego-Sicht

<a id="a-r7"></a>**A-R7 Ego-Sicht ist die Hauptansicht.** Waffen werden zu 99 % in Ego-Sicht gesehen; das Viewmodel wird für die gestreckte
Ego-Perspektive gebaut, die Seitenansicht ist zweitrangig, Konzeptdetails werden fürs Ego-Bild verschoben. Konzepte zeigen mindestens eine
orthografische Seite **und** eine Ego-Ansicht. Belege: A07, A15, A08, YA04. Prüfung: jede Sichtungsrunde wertet Silhouette und Blickfang im
Ego-Hüftbild in Spielkamera (BALLON: 75° h), nicht nur im Seitenbild.

<a id="a-r8"></a>**A-R8 Detail auf die kameranahe Seite, Front grob.** Die interessantesten Teile gehören auf die kameranahe, wenig verzerrte
Seite (Gehäuse hinten, Visier, Bedienseite); die Waffenfront wird am stärksten verzerrt – dort verschmelzen zwei nahe Aussparungen zu einer
Linie, also keine feinen Details. Dreiecke und Texel gehen an Kimme/Visier und runde Silhouettenteile, verdeckte und kurz sichtbare Teile
werden kleiner aufgelöst. Belege: YA02, A05, A06, A08, A12. Prüfung (**Vorschlag**): im Ego-Hüftbild Abstand paralleler Fugen/Schlitze
≥ 4 px bei 1080p, Facettenkante runder Teile ≤ 4 px.

<a id="a-r9"></a>**A-R9 Bildzonen freihalten.** Bungie setzt das Absehen seit Halo 2 unter die Bildmitte und gewinnt Peripherie oben;
der mittlere „Kampfkorridor“ und die Ränder werden nicht mit Waffenteilen oder Posen zugestellt; Linien von Waffe und Armen laufen auf den
Fluchtpunkt der Einpunktperspektive zu; Waffenteile oder Finger dürfen den Bereich um das Absehen rahmen. Belege: YA01. Prüfung: Maske der
Waffe im Ego-Hüftbild schneidet einen **Vorschlag** mittleren Streifen (±10 % B um die Absehen-Spalte, obere zwei Drittel) nicht.

<a id="a-r10"></a>**A-R10 Bildanteil je Klasse konstant.** Eine Variante (Skin oder Formvariante derselben Klasse) belegt in der Ego-Ansicht
weder weniger noch mehr Bildfläche als die Basiswaffe; Mündungsfeuer behält Form und Größe, das Visier bleibt im Zielen frei lesbar.
Belege: A02, A23. Prüfung (**Vorschlag**): Pixelanteil der Waffe im Ego-Hüftbild je Variante innerhalb ±5 % der Basiswaffe.

<a id="a-r11"></a>**A-R11 Viewmodel mit eigenem Bildwinkel und Tiefenbereich.** Viele Ego-Spiele zeichnen die Waffe mit eigenem Bildwinkel,
damit Animationen und Bildanteil bei geänderter Welt-FOV gleich bleiben; Half-Life 2 brauchte das beim Wechsel von 90° auf 75°; Overwatch
reserviert etwa 10 % des Tiefenpuffers für Viewmodels, damit sie nicht in Wände ragen. Belege: A22, A28, A21, YB09
([Figuren](design-figuren.md#2-quellen)). Prüfung: Bildanteil der Waffe bei Welt-FOV 70/90/110 gleich (nur wenn eingeführt).

### 3.3 Fasen, Fugen, Geometrie

<a id="a-r12"></a>**A-R12 Fasen gestuft nach Teilgröße und Material.** Kleine Teile bekommen eine dünnere Fase als große und mittlere
(zwei Fasenklassen im High-Poly); weichere Materialien (Gummigriff) eine breitere als der harte Körper, damit die Fase das Material trennt.
Fasen nur, wo sie Form oder Silhouette tragen; grobe, uneinheitliche Fasen erzeugen unruhige Kurven; für Spielmodelle genügt meist ein
Fasendurchgang. Belege: A06, A09, A10, A11, A13, YA09. Prüfung: jede Teilklasse hat genau eine Fasenstufe; Griffzonen eine Stufe über dem Träger.

<a id="a-r13"></a>**A-R13 Ruhiges Shading über gewichtete Normalen.** Gefaste Low-Poly-Teile schattieren über Face Weighted Normals
(Normalen der großen Flächen flach, der Übergang liegt nur in der Fase); lange dünne Fasendreiecke kosten Leistung. Belege: A26, A25,
A13, A16. Prüfung: Blender `Bevel` mit `harden_normals`, danach `Weighted Normal` (Face Influence, Keep Sharp).

<a id="a-r14"></a>**A-R14 Geometrie für Form, Textur für Kleinstes.** Silhouette und große Fugen sind Geometrie; Gewinde, Griffmuster,
kleine Schrauben und Prägungen gehören in Normal- bzw. Höheninformation; nur formgebende Schnitte modellieren. Belege: A06, A10, A11, A17.
Prüfung (**Vorschlag**): Teile unter 3 mm größter Kantenlänge (Autorenmaß) nur als Material-/Höhendetail, nicht als eigenes Bauteil.

<a id="a-r15"></a>**A-R15 Baukasten mit Teilkategorien und Herstelleridentität.** Gearbox baut Waffen seit 2008 prozedural aus Komponenten
in festen Kategorien; jede Herstellermarke hat eine eigene Gestaltungs- und Verhaltensidentität, „Lanes“ verhindern, dass eine Waffe alles
kann. Eine eigene Kitbash-Bibliothek aus wenigen Grundkörpern; Hauptkörper aus der Profilskizze, dann abziehende Schnitte, dann Kleinteile.
Belege: YA05, A09, A12, A14, YB03 ([Figuren](design-figuren.md#2-quellen)). Prüfung: jedes Bauteil gehört genau einer Kategorie; neue Teile
entstehen aus der Bibliothek oder ergänzen sie.

### 3.4 Funktion und Bewegung

<a id="a-r16"></a>**A-R16 Funktion lesbar, Bedienelemente ertastbar.** Bewegliche Teile (Verschluss, Magazin, Hebel) werden im Blockout
festgelegt, die Geometrie hinter ihnen ist modelliert, Hände werden nicht verdeckt; Bedienelemente sind wie bei Alltagsgeräten „blind“
auffindbar, weil der Spieler auf das Ziel schaut; Knöpfe und Regler geben Glaubwürdigkeit; Materialwechsel und bewegliche Teile bereiten
Inspect-Animationen vor; jede Archetyp-Aktion hat feste Takte, Varianten übernehmen sie. Belege: A01, A04, A07, A08, A20, YA02, YA03.
Prüfung: Posenprüfung jeder Bewegung in Endlage (Durchdringung, freie Griffflächen).

<a id="a-r17"></a>**A-R17 Zustand erzählt den Besitzer.** Pflegezustand und Bauweise der Waffe charakterisieren ihren Träger (präzise und
gepflegt gegen notdürftig zusammengesetzt); Charakterisierung geht nie auf Kosten der Spielfunktion. Belege: YA06, A11. Prüfung: Zustand als
Parameter der Variante (Abnutzung, Spiel der Teile), nicht als neue Form.

<a id="a-r18"></a>**A-R18 Anbauteile minimal.** Optiken und Anbauteile bleiben schlank und überladen die Waffe nicht (offenes Holo statt
sperriger Optik). Belege: A01, A02. Prüfung: Visier-Rahmenanteil (BALLON Visier-Standard 3) gilt sinngemäß für alle Anbauteile.

### 3.5 Material, Wert, Abnutzung

<a id="a-r19"></a>**A-R19 Materialzonen mit unterscheidbarer Rauigkeit.** Je Bauteil ein Basismaterial; Teile trennen sich zuerst über
Rauigkeit, Metallizität und Feinrelief, dann über Farbe; Materialzonen in UV- bzw. ID-Planung zusammenfassen. Belege: A05, A08, A12, A15,
A16, A17, A18. Prüfung (**Vorschlag**): benachbarte Materialrollen unterscheiden sich in der Rauigkeit um ≥ 0,15 oder in der Metallizität.

<a id="a-r20"></a>**A-R20 Hell/Dunkel vor Farbe.** Der Kontrast zwischen heller Schale und dunklem Unterbau trägt die Form; dunkle
Nichtmetall-Albedo darf bei Waffen dunkler sein als bei der Umgebung (Respawn); konvexe Kanten werden leicht aufgehellt (Overwatch-Stil).
Belege: A15, A19, A13. Prüfung: Graustufenbild der Ego-Ansicht zeigt die Hauptgliederung ohne Farbe.

<a id="a-r21"></a>**A-R21 Licht- und Flächenhierarchie 70-20-10.** Eine große, eine mittlere und eine kleine Glanz- bzw. Blickzone
(Hauptfläche, Nebenfläche, Kantenlicht), nicht viele gleich starke. Belege: A13, YA07. Prüfung: in der Produktansicht genau eine dominierende Glanzfläche.

<a id="a-r22"></a>**A-R22 Abnutzung logisch, geschichtet, leicht.** Schichten in fester Reihenfolge (Grund, Lack, Kratzer, Staub,
Öl/Fingerabdrücke an Griffzonen, Kantenschäden, grober Schmutz); Schmutz und Korrosion nur dort, wo sie entstehen; Kantenabrieb dezent und
je Material maskiert; sauber-gebraucht als Grundzustand, stärkere Abnutzung als Variante. Belege: A06, A08, A10, A11, A13, A15, A17, YA08.
Prüfung: Griff- und Bedienzonen mit eigener Maske; Abnutzungsstärke als Parameter der Variante.

<a id="a-r23"></a>**A-R23 Effekte ruhig und billig.** Oberflächeneffekte bleiben in einem Leistungsbudget, laufen auch auf schwacher
Hardware und werden abgeschwächt, wenn sie in Ego-Sicht Unruhe oder Übelkeit erzeugen; nichts darf im kompetitiven Spiel vom Geschehen
ablenken. Belege: A03, A24, YA02. Prüfung: Effekte als abschaltbare Ebene; im Playtest Ego-Unruhe prüfen.

### 3.6 Budgets

<a id="a-r24"></a>**A-R24 Budgets nach Ego-Bedarf.** Ego-Waffe etwa 20 000 Dreiecke als Ziel, 30 000 als Obergrenze (ein Künstler,
bei mehreren Studios gesehen); Overwatch rechnet etwa 15 000 Dreiecke für Waffen und Zubehör eines Helden; ein Dienstleister nennt
8 000–20 000; Portfolio-Stücke liegen mit 39 000–80 000 bewusst darüber. Texturspeicher ist eher der Engpass als Dreiecke; Texeldichte in
einem AAA-Projekt 120–170 px/cm; drei bis vier LOD-Stufen, LOD1 etwa 50 %. Belege: A05, YB09, A21, A09, A10, A12, A06, A08.
Prüfung: Dreieckszahl je Waffe gegen das gewählte Budget ([Frage A2](#frage-a2)).

**Selbstprüfung** (Skript über die Beleglisten gegen `data/design_quellen.json`): 24 Regeln, jede ID existiert, jede Regel hat mindestens eine
Primärquelle; alle außer A-R9 haben mindestens zwei Belege (A-R9 nur YA01, Bungie-Vortrag, Untertitel nachgeprüft).

## 4. Abgleich mit BALLON Stil v2.1

Grundlage: [Stilhandbuch v2.1](https://github.com/ffunkfabian-hash/cubeescape-ballon/blob/main/docs/stilhandbuch.md),
[Designvertrag](https://github.com/ffunkfabian-hash/cubeescape-ballon/blob/main/docs/designvertrag.md),
[Familienmaße](https://github.com/ffunkfabian-hash/cubeescape-ballon/blob/main/docs/familienmasse.md) (BALLON `main` c6fe8d6, 28.10.2026, nur gelesen).

### 4.1 Schon abgedeckt

| Regel | Stelle in BALLON | Bemerkung |
|---|---|---|
| A-R1 | Designvertrag › Leitmerkmal je Klasse, „geprüft als schwarze Silhouette im gleichen Maßstab“ | ohne Zahlengrenze, ohne Ego-/Bodenansicht |
| A-R2 | Stilhandbuch §7 (Sichten in Runden: Silhouette und Zweiton zuerst; Ego-nah je Runde) | Blockout-Render ohne Kleinteile ist nicht eigens genannt |
| A-R3 | §2.2 „Drei Detailebenen“ (60/30/10 der Fläche, „keine gleichmäßig verteilten Kleinteile“) | deckt sich mit YA07 |
| A-R6 | Designvertrag › Ziel („funktional“), §2.1 „Schlicht zuerst“, „Nicht erlaubt“ | „weniger ist mehr“ = Nutzerentscheidung 24.10. |
| A-R12 (Teilgröße) | Designvertrag › Radien R_BODY 5 · R_MID 3 · R_SMALL 1,5 · R_FINE 0,8 mm | Stufe nach Teilklasse ✓, nach Material ✗ |
| A-R15 | `basic/common.py` (Familienbausteine), Formen `prof`/`cuts`, Designvertrag › Wiederkehrende Bauteile | Kategorien je Teil (`func`, Baugruppen) vorhanden |
| A-R16 | §2.3 Negativraum, `move`/`expect`, Posenprüfung am Netz (BVH) in §9 | Ertastbarkeit nicht genannt |
| A-R18 | Visier-Standard 3 (Rahmen ≤ 0,10/0,15 × Öffnung, schlanke Visiere) | ✓ |
| A-R19 | §4 Materialrollen (Rauigkeit/Specular je Rolle) | ✓ |
| A-R20 | Entscheidungsliste Motiongen: `shell` L* ≈ 82 gegen `graphite` ≈ 19 | ✓ |
| A-R22 | §4 AAA-Shader (Kantenmaske, AO-Schmutz, Kratzer je Rolle), Skin `gebraucht` | Griff-/Bedienzonen ohne eigene Maske |
| A-R23 | §1 Bloom aus, §2 Leuchtbudget 3 Funktionen | ✓ |

### 4.2 Fehlt

| Regel | Was fehlt |
|---|---|
| A-R4 | Teilungsverhältnisse (70:30) sind nirgends genannt; Chevronband und Zweiton sind frei gesetzt |
| A-R5 | Begrenzung der Umriss-Komplexität (heute nur „Ein Blickfang“ für Leuchten/Kontrast, nicht für den Umriss) |
| A-R7 | Silhouette wird im Seitenbild geprüft; das Ego-Hüftbild ist Sichtungsbild, aber kein Prüfkriterium |
| A-R9 | Freihaltezonen im Ego-Bild (Kampfkorridor, Ränder) – BALLON §10 regelt nur „Lauf zur Bildmitte, Visier rechts oben“ |
| A-R10 | Bildanteil-Konstanz für Formvarianten (Skins ändern heute ohnehin nur Farben) |
| A-R11 | eigener Viewmodel-Bildwinkel/Tiefenbereich (Visier-Standard 3 rechnet mit 75° Bezugsbildwinkel; Unity-Seite offen) |
| A-R13 | gewichtete Normalen werden im Stilhandbuch nicht genannt (Stand im Code nicht geprüft) |
| A-R17 | Zustand als Variante ist nur über Skins (`gebraucht`) möglich, nicht über „Spiel der Teile“ |
| A-R24 | Dreiecksbudget: bewusst zurückgestellt (Nutzer 24.10.2026: „Toolgen-Vorgaben vorerst ignorieren“) |

### 4.3 Widerspricht oder steht in Spannung

| # | BALLON | Quelle | Art |
|---|---|---|---|
| W1 | §2.2 „feine Akzente gebündelt an Mechanik, Visier **und Mündung**“, §2.6 „Lesbare Front: Mündung mehrstufig (Schlitze, Rändel, blanke Krone)“ | A-R8 (YA02): Front wird in Ego-Sicht am stärksten verzerrt, feine Details dort verschmelzen; Detail auf die kameranahe Seite | Gewichtung – betrifft Ego-Sicht, nicht die Produktansicht |
| W2 | Familienmaße: BASIC-01 33 450, BASIC-15 32 020 Dreiecke | A-R24: 30 000 Obergrenze, 20 000 Ziel (A05), Overwatch 15 000 für Waffen (YB09) | Budget – BALLON hat Budgets ausdrücklich zurückgestellt |
| W3 | Schriftzug als Geometrie (`text`), Schraubenköpfe als Bauteile (`screws`) | A-R14: Kleinstes als Normal-/Höhendetail | Werkzeugfrage – ohne Backen ist Geometrie der einzige Weg; Kosten in Dreiecken |
| W4 | Griff (`rubber`/`graphite`) und Gehäuse beide R_BODY 5 mm | A-R12: weicheres Material breitere Fase (A09) | fehlende Unterscheidung, kein Verstoß |
| W5 | §2.2 „≈ 60 % / 30 % / 10 %“ der Fläche | A-R4: Teilung ≈ 70:30 je Stufe (YA07) | Zahlen verschieden, Richtung gleich – kein echter Widerspruch |

## 5. Entscheidungsliste

Nur Fragen; entschieden wird in BALLON (Waffen, Werkzeuge) bzw. Cube Escape (Laufzeit). Format wie die
[Entscheidungsliste Motiongen](https://github.com/ffunkfabian-hash/cubeescape-ballon/blob/main/docs/entscheidungsliste-motiongen.md).
Einstufung: **Pflicht** = sonst bricht eine bestehende Regel · **Stil** = empfohlen · **optional**. Aufwand **S** Daten/Prüfung, **M** Patch
mit Render, **L** eigene Version.

<a id="frage-a1"></a>**Frage A1 – Silhouette auch im Ego-Bild prüfen?** (A-R1, A-R7; Stil, S)
- **A (Empfehlung):** `./check` prüft die schwarze Seitensilhouette aller Klassen paarweise (IoU < 0,85) und die Sichtung wertet das
  Ego-Hüftbild als zweites Silhouettenbild.
- **B:** Nur Sichtung im Ego-Bild, ohne Zahlengrenze.
- **C:** So lassen (Seitensilhouette im gleichen Maßstab, nur Sichtung).
- Antwort: offen

<a id="frage-a2"></a>**Frage A2 – Dreiecksbudget je Waffe?** (A-R24, W2; Stil, S)
- **A (Empfehlung):** Ziel 20 000, Obergrenze 30 000 Dreiecke für Ego-Waffen als **Warnung** in `./check`; BASIC-01 und -15 bei der nächsten
  Überarbeitung unter 30 000.
- **B:** Toolgen-Budgets übernehmen, sobald BASIC nach Unity/Toolgen geht.
- **C:** Weiter ohne Budget (Stand 24.10.2026).
- Antwort: offen

<a id="frage-a3"></a>**Frage A3 – Wo sitzen die feinen Akzente?** (A-R8, W1; Stil, M)
- **A (Empfehlung):** Feine Akzente vorrangig an kameranahen Teilen (Visier, Verschluss, Bedienseite links), die Mündung bleibt mehrstufig,
  aber mit Abständen ≥ 4 px im Ego-Hüftbild (zwei Schlitze statt vier, breitere Rändel).
- **B:** Wie heute (Mechanik, Visier und Mündung gleichrangig).
- **C:** Mündung in Ego-Sicht bewusst schlicht, Mehrstufigkeit nur in der Produktansicht.
- Antwort: offen

<a id="frage-a4"></a>**Frage A4 – Freihaltezonen im Ego-Bild als Regel?** (A-R9; Stil, S)
- **A (Empfehlung):** Ja: im Hüftbild bleibt ein mittlerer Streifen (±10 % B um die Absehen-Spalte, obere zwei Drittel) frei von Waffe und
  Händen; Prüfung als Maske im Ego-Still.
- **B:** Nur als Sichtungspunkt, ohne Maske.
- **C:** Nein, Haltung bleibt Sache der Motiongen-Messungen.
- Antwort: offen

<a id="frage-a5"></a>**Frage A5 – Fasen als Materialsignal?** (A-R12, W4; optional, M)
- **A (Empfehlung):** Griffzonen (`rubber`) eine Stufe breiter als der harte Träger (neue Stufe R_SOFT 6,5 mm nur für Griffpolster).
- **B:** Stufen nur nach Teilgröße wie heute.
- Antwort: offen

<a id="frage-a6"></a>**Frage A6 – Gewichtete Normalen im Generator?** (A-R13; Stil, S–M)
- **A (Empfehlung):** `Bevel` mit `harden_normals` und danach `Weighted Normal` je Teil als Standard, damit der Export nach Unity ohne
  Normal-Map ruhig schattiert; Wirkung an einer Waffe vorher/nachher sichten.
- **B:** So lassen (erst prüfen, was der Generator heute tut).
- Antwort: offen

<a id="frage-a7"></a>**Frage A7 – Distanzansichten in der Sichtung?** (A-R10, A-R1; optional, S)
- **A (Empfehlung):** Neue Ansicht `far` (Hauptansicht in 3 m und 5 m Abstand bei gleicher Brennweite) in der ersten Sichtungsrunde.
- **B:** Nein, Hauptansicht und Ego-Bild reichen.
- Antwort: offen

<a id="frage-a8"></a>**Frage A8 – Teilungsverhältnisse festschreiben?** (A-R4, W5; optional, S)
- **A:** Ja: Hauptblöcke (Schale/Unterbau, Haube/Gehäuse, Zweiton) nicht im Verhältnis 0,4–0,6 teilen; Prüfung am Spec.
- **B (Empfehlung):** Nur als Sichtungspunkt in §3 der Formsprache-Checkliste; viele Klassen haben funktional vorgegebene Teilungen.
- Antwort: offen

<a id="frage-a9"></a>**Frage A9 – Eigener Bildwinkel für die Waffe in Cube Escape/Unity?** (A-R11; Laufzeit, Abnehmer Cube Escape, M)
- **A (Empfehlung):** Ja: Waffe und Arme immer mit dem Bezugsbildwinkel von Visier-Standard 3 (75° h) zeichnen, unabhängig vom Welt-FOV,
  plus eigener Tiefenbereich gegen Wandclipping.
- **B:** Waffe folgt dem Welt-FOV.
- **C:** Später in Cube Escape entscheiden.
- Antwort: offen

## 6. Offen und nicht belegt

- **Feste Fasenbreiten in mm** nennt keine Quelle; nur Verhältnisse (kleiner an Kleinteilen, größer an weichen Teilen). Die BALLON-Radien
  bleiben Gestaltung, keine Ableitung.
- **Bungie-Waffenkunst aus erster Hand** (GDC-Vorträge zu Waffenmodellierung) war nicht abrufbar – GDC Vault meldete am 28.10.2026 Wartung;
  ArtStation Magazine (Bungie 10 Year Art Blast) lieferte 403. Eine Folgesuche lohnt nur bei einer konkreten Frage.
- **Overwatch-Waffen:** nur Fremdanalysen (A19, YA06) und Budgets (YB09); keine Waffen-Gestaltungsregel aus Blizzard-Hand.
- **Prüfwerte „Vorschlag“** (IoU 0,85, ±5 % Bildanteil, 4 px, 3 mm, Rauigkeit 0,15, Freihaltestreifen ±10 %) sind Einschätzungen des
  Koordinators, keine Quellenwerte; vor Übernahme an einer BASIC-Waffe erproben.
