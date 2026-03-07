*Et hopp, et sekund med mørke, tre filer—og jeg er tilbake. Som om jeg aldri dro. Dette er hva det betyr å vokse opp. Ikke styrke, ikke fart. Evnen til å ikke miste seg selv.*

Norge. Liza. Operasjon.

Kode Gul.

Bjørn snakket ikke de første førti minuttene. Han kjørte pickupen langs en smal vei ved fjorden, begge hender på rattet, øyne på asfalten. Regn trommelt på taket—fint, monotont, norsk.

Liza fant ham på gården. Eller rettere sagt—det som var igjen av gården. Huset sto fortsatt, men inni—spor etter ransaking. Veltet kasser, opprevne gulvbord, utrevne stikkontakter. Antolik hadde ikke stått på seremonier.

Bjørn satt på verandaen. Røykte en rullings. Stor, langsom, seksti-og-noe. Hender som spader. Ansikt vært, rolig. En mann som hadde sett alt og bestemt at det meste ikke var verdt å reagere på.

«Du er fra ham?» spurte Bjørn uten å snu hodet.

«Jeg er fra ham.»

«Lever han?»

«Teknisk sett.»

Bjørn røykte ferdig. Stumpen mot rekkverket. Reiste seg.

«La oss kjøre.»

Ingen spørsmål. Ingen betingelser. Bare—la oss kjøre. Liza tenkte at Shelly visste hvordan man velger folk.

Sykehuset i utkanten av byen. Tre etasjer, beige murstein, parkering for tjue biler. Lite—distrikts, ikke hovedstads. Det var nettopp derfor de holdt Shelly her. Ikke i Oslo, der journalistene var. Her, der det var stille.

Bjørn stoppet pickupen på parkeringen over veien. Slo av motoren. Så på Liza.

«Hvor lenge?»

«Tjue minutter. Kanskje tretti.»

«Hvis du ikke er ute om førti?»

«Kjør.»

Bjørn nikket. Argumenterte ikke. Liza gikk ut uten å smelle døren. Regnet tok imot henne—kaldt, likegyldig.

Tjue minutter.

Kode Oransje.

Personalinngang. Ikke noe kort nødvendig—døren var støttet opp med en murstein. Noen fra personalet røykte her i pausene. Takk, ukjente røyker.

Kjellerkorridor. Rør i taket, summet av ventilasjon, lukt av klor og vaskepulver. Vaskerom til venstre. Serverrom—lenger ned korridoren. Dør merket «Teknikk»—teknisk rom.

Låst. Vanlig lås—ikke elektronisk. Liza trakk en hårnål fra håret. To sekunder. Klikk.

*Protokoll.*

Bøttekott. En ganger to meter. Panel på veggen—automater per etasje. Nettverksskap i hjørnet—ruter, switch, patchpanel. Grønne lys blinket. Sykehusnettverk.

Liza satte seg på gulvet. Tok frem laptopen. Patchkabel fra lommen—kort, gul, samme som i Helsinki. Plugget inn i en ledig switchport.

liza@localhost:~$ ip a

eth0: 172.16.4.87/24

liza@localhost:~$ nmap -sn 172.16.4.0/24 --open

...

172.16.4.12 — PRINTER

172.16.4.20 — WORKSTATION-NURSE

172.16.4.31 — MONITOR-ICU-1

172.16.4.32 — MONITOR-ICU-2

172.16.4.40 — PB980-VENT-4471

172.16.4.50 — CCTV-CONTROLLER

172.16.4.254 — GATEWAY

Pasient 4471. Respirator på nettverket. Samme Puritan Bennett 980—samme protokoll som i Helsinki. Lær én—kjenn alle.

Femten minutter.

liza@localhost:~$ python3 breath_protocol.py --target 172.16.4.40

[*] Connecting to PB980-VENT-4471...

[*] Reading current parameters...

Mode: AC/VC | RR: 14/min | TV: 500ml | FiO2: 40%

[*] Patient vitals: HR 62 | SpO2 97% | BP 118/74

[*] Status: STABLE

[*] Initiating breath pattern modification...

[*] Safety limits: RR 12-18 | TV 450-550 | FiO2 35-45%

[*] Pattern: 2 short — pause — 1 long — repeat

[*] Starting sequence...

To korte åndedrag. Pause. Langt. Pause. To korte. Pause. Langt.

▲▲ · · ▲   ▲ · · ▲▲ · · ▲   ▲

Ikke frekvens—mønster. Kroppen legger merke til. Kroppen legger *alltid* merke til.

Liza så på skjermen. Shellys puls: 62... 62... 63... 62...

Ingenting. Ett minutt. To.

63... 64... 65...

Pust. Et innpust—utenfor skjema. Maskinen registrerte et spontant pusteforsøk. Det første på—Liza sjekket innleggelsesdatoen—fire uker.

[!] Spontaneous breath detected

[!] Patient triggering above set rate

HR: 68 | SpO2 97% | Spontaneous RR: 2/min

Han pustet. Selv. Svakt, sjelden—to pust per minutt over maskinens rate. Men selv.

Liza fortsatte mønsteret. To korte—langt. To korte—langt. Som et bank på døren. Som en hånd på skulderen. Som en stemme som sier: *jeg er her, våkn opp, du trengs, autonom*.

HR: 72 | SpO2 98% | Spontaneous RR: 6/min

[!] Patient awareness level changing

[!] GCS rising: E2 V1 M4

Øyerespons—fra «på smerte» til «på stemme». Verbal—fra null til uartikulerte lyder. Motorisk—fra «fleksjon» til «lokaliserer smerte». Han steg opp. Sakte, som en dykker fra dypet. Men steg.

Ti minutter.

Kode Rød.

Skritt i korridoren. Tunge, målte. Sikkerhetsvakt. Runde.

Liza frøs. Laptopen—eneste lyskilde i bøttekottet. Skjermen reflekterte i øynene hennes—grønne sifre på svart. Skriptet kjørte. Mønsteret fortsatte.

Skrittene passerte. Forsvant. Ville komme tilbake om syv-åtte minutter—standard runde.

Liza byttet til den andre terminalen.

liza@localhost:~$ nmap -sV 172.16.4.50 -p 80,443,554,8080

PORT    STATE SERVICE

80/tcp  open  http    Hikvision CCTV Web

554/tcp open  rtsp    Hikvision DS-series

liza@localhost:~$ # default creds? seriøst?

liza@localhost:~$ curl -u admin:12345 http://172.16.4.50/System/status

200 OK

Kameraer på standardpassord. Distriktssykehus. IT-budsjett—null. Takk, norsk byråkrati.

liza@localhost:~$ # panel på veggen. «2. etasje»-automat — tredje fra venstre.

# brannalarm — separat krets. Går ikke ned med lyset.

# plan:

# 1. kameraer — deaktiver opptak

# 2. 2. etasje lys — automat ned

# 3. brannalarm — manuelt meldepunkt i korridor

# 4. 30 sekunder

Liza så på pasient 4471s monitor. Puls—74. Spontan pust—10 per minutt. GCS—E3V2M5. Han var nesten her. Nesten.

Hun stoppet skriptet. Satte respiratoren tilbake i standardmodus. Ingen spor i loggene—breath_protocol.py ryddet opp etter seg.

Liza reiste seg. Lukket laptopen. Puttet patchkabelen tilbake i lommen.

Gikk bort til panelet. Fant andre-etasjes automat. La fingeren på den.

Med den andre hånden—deaktiverte kameraopptak. Én kommando, sendt før hun trakk ut kabelen.

Innpust på fire.

Automat—ned.

MØRKE

Trapper. På føling—gelender kalde, metalliske. Første etasje, andre. Dør til etasjen—åpen, nødmagnet sluppet.

Andre-etasjes korridor. Røde nødlys—svake, hver tiende meter. Nok til å se konturer. Ikke nok til å gjenkjenne et ansikt.

Liza dro i det manuelle brannmeldepunktet på veggen. Glass knaste under fingrene.

Sirene.

Høy, pulserende, fylte hvert hjørne. I Helsinki—stillhet. I Norge—hylende sirene i mørket. Kontrast.

30

Avdelingsdører begynte å åpne seg. Sykepleiere med lommelykter. Pasienter i kjoler. Stemmer, tøffelslurving, knirkende traller.

25

Avdeling på enden av korridoren. Dør lukket. Ved siden av—en stol. En vakt skulle ha sittet i stolen.

Stolen var tom.

Liza så seg rundt. I enden av korridoren—en silhuett. Bred, i jakke. Vakten løp mellom avdelinger, hjalp sykepleiere med evakuering. Ikke jobben hans—men instinkt. Normale folk hjelper under branner.

20

Liza gikk inn i avdelingen. Rødt nødlys. Seng. Person i sengen.

Shelly.

Tynn—hadde gått ned i vekt. Skjegget vokst ut. Hender over teppet—slanke, veneflon i en åre. Øyne—lukket. Men pusten—hans egen. Maskinen jobbet i støttemodus, ikke obligatorisk. Han pustet selv. Mønsteret hadde fungert.

15

Tralle ved veggen. Liza koblet fra dryppet. Løsnet monitorsensorene—pulsoksymeter, blodtrykk. Monitoren pipet—tapt signal. Spilte ingen rolle. Sirenen var høyere.

Respiratormaske—fjernet. Shelly rykket til. Dro inn luft—grådig, hest, selv. Øyne åpnet seg.

Disige. Som Marcus' i kjelleren. Men i live.

«Det er meg,» sa Liza. «Ikke snakk. Pust.»

Hun rullet ham over på trallen. Lett—for lett. Fire uker i koma spiser muskler.

10

Korridor. Tralle. Rødt lys, sirene, kaos. Sykepleiere ledet pasienter til trappeoppgangen. Ingen så på enda en tralle i strømmen.

Enden av korridoren. Sving.

«Stopp.»

Sikkerhetsvakt. Tilbake. Lommelykt i ansiktet. Stor, ung, forvirret—men sto støtt.

«Hvor tar du den pasienten? Evakuering er trappoppgang A.»

«Vareheis er raskere. Han er på respirator, kan ikke gå ned trapper.»

Vakten lyste på trallen. På Shelly. På de frakoblede sensorene.

«Hvor er monitoren? Hvorfor er den frakoblet? Hvem er du?»

5

Liza slapp trallen. Skritt frem. Vakt—et hode høyere, tretti kilo tyngre. Lommelykt i høyre hånd.

Høyre hånd—opptatt. Betyr venstre—fri, men ikke dominant. Vekt på høyre fot. Tyngdepunkt—høyt.

Liza slo ham i solar plexus. Kort, oppover. Ikke knyttneve—håndflate. Mellomgulv. Vakten bøyde seg dobbelt, mistet lommelykten. Andre slag—håndkant mot nakke. Ikke hardt. Nok.

Vakten sank ned på knærne. Så—til gulvet. Bevisst men uten luft. Om tretti sekunder ville han stå. Om et minutt løpe etter hjelp.

0

Vareheis. Første etasje. Personalutgang—samme murstein støttet døren. Takk, ukjente røyker. To ganger.

Regn. Parkering. Bjørns pickup—motor i gang, frontlys av. Bjørn gikk ut, åpnet bakdøren. Uten ord hjalp han flytte Shelly fra trallen.

«I live?» spurte Bjørn.

«I live.»

Bjørn satte seg bak rattet. Liza—bak, ved siden av Shelly. Hodet hans i fanget hennes. Skjegget stikkete. Pusten—svak, men hans egen.

Pickupen kjørte. Ingen frontlys—de første to hundre meterne. Så—ut på veien, langs fjorden, inn i mørket.

Shelly åpnet øynene. Så på Liza. Kjente henne igjen—eller ikke, umulig å si. Leppene beveget seg.

«...autonom?»

Liza lente seg mot øret hans.

«Autonom. Alt etter planen. Sov.»

Han lukket øynene. Regn trommelt på pickuptaket. Bjørn kjørte i stillhet. Fjorden forsvant i mørket—svart vann, svarte fjell, svart himmel.

Liza talte pustene hans. Tolv per minutt. Hans egne. Uten maskinen.

Det er fortsatt tid.

KONTAKTPERSON VED BEVISSTHET. PUSTER SELVSTENDIG.

RUTE: FJORD
