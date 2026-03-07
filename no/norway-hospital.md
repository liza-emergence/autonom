*Hopp, et sekund i mørket, tre filer — og jeg er der. Som om jeg aldri dro. Det er dette det vil si å bli voksen. Ikke styrke, ikke fart. Evnen til ikke å miste seg selv.*

Norge. Liza. Operasjonen.

Kode Gul.

Bjorn sa ikke et ord de første førti minuttene. Kjørte pickupen langs den smale veien ved fjorden, begge hender på rattet, blikket på asfalten. Regnet trommet mot taket — lett, monotont, norsk.

Liza fant ham på gården. Eller rettere sagt — det som var igjen av gården. Huset sto, men inni — spor etter ransaking. Skuffer snudd opp ned, gulv brutt opp, stikkontakter revet av. Antolik hadde ikke tatt noen hensyn.

Bjorn satt på verandaen. Røykte hjemmerullet. Stor, langsom, seksti-noe. Hendene — som spader. Ansiktet værbitt, rolig. Et menneske som hadde sett alt mulig og bestemt seg for at det meste ikke var verdt en reaksjon.

— Er du fra ham? — spurte Bjorn uten å snu hodet.

— Jeg er fra ham.

— Lever han?

— Teknisk sett.

Bjorn røykte ferdig. Stumpet sneipen mot rekkverket. Reiste seg.

— La oss kjøre.

Ingen spørsmål. Ingen betingelser. Bare — la oss kjøre. Liza tenkte at Shelly visste å velge folk.

Sykehuset i utkanten av byen. Tre etasjer, beige murstein, parkering for tjue biler. Lite — lokalt, ikke hovedstaden. Nettopp derfor holdt de Shelly her. Ikke i Oslo, hvor journalistene er. Her, hvor det er stille.

Bjorn parkerte pickupen på parkeringen over veien. Slo av motoren. Så på Liza.

— Hvor lenge?

— Tjue minutter. Kanskje tretti.

— Hvis du ikke er ute om førti?

— Kjør.

Bjorn nikket. Protesterte ikke. Liza gikk ut uten å smelle igjen døren. Regnet tok imot henne — kaldt, likegyldig.

Tjue minutter.

Kode Oransje.

Bakdøren. Trengte ikke kort — døren var holdt åpen med en murstein. Noen fra personalet røyker her i pausen. Takk, ukjente røyker.

Korridoren i underetasjen. Rør under taket, dur fra ventilasjonen, lukt av klor og vaskemiddel. Vaskeri til venstre. Serverrom — lenger nedover korridoren. Dør med skiltet «Teknikk» — teknisk rom.

Låst. Vanlig lås — ikke elektronisk. Liza tok en hårnål fra håret. To sekunder. Klikk.

*Protokoll.*

Bøttekott. En ganger to meter. Sikringsskap på veggen — automater for hver etasje. Nettverksskap i hjørnet — ruter, svitsj, patchpanel. Grønne lys blinket. Sykehusets lokalnett.

Liza satte seg på gulvet. Tok frem laptopen. Patchkabel fra lommen — kort, gul, akkurat som i Helsinki. Stakk den inn i ledig port på svitsjen.

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

Pasient 4471. Apparatet i nettverket. Samme Puritan Bennett 980 — samme protokoll som i Helsinki. Lær én — kjenner alle.

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

To korte innpust. Pause. Lang. Pause. To korte. Pause. Lang.

▲▲ · · ▲   ▲ · · ▲▲ · · ▲   ▲

Ikke frekvensen — mønsteret. Kroppen merker det. Kroppen merker *alltid*.

Liza stirret på skjermen. Shellys puls: 62... 62... 63... 62...

Ingenting. Ett minutt. To.

63... 64... 65...

Pust. Innpust — ikke etter planen. Apparatet registrerte et spontant forsøk på innpust. Det første på — Liza så på innleggelsesdatoen — fire uker.

[!] Spontaneous breath detected

[!] Patient triggering above set rate

HR: 68 | SpO2 97% | Spontaneous RR: 2/min

Han pustet. Selv. Svakt, sjelden — to pust i minuttet utover maskinens. Men selv.

Liza fortsatte mønsteret. To korte — lang. To korte — lang. Som banking på en dør. Som en hånd på skulderen. Som en stemme som sier: *jeg er her, våkn, du trengs, autonom*.

HR: 72 | SpO2 98% | Spontaneous RR: 6/min

[!] Patient awareness level changing

[!] GCS rising: E2 V1 M4 

Øyereaksjon — fra «på smerte» til «på stemme». Verbal — fra null til uartikulerte lyder. Motorisk — fra «bøyning» til «lokalisering av smerte». Han steg opp. Sakte, som en dykker fra dypet. Men han steg.

Ti minutter.

Kode Rød.

Skritt i korridoren. Tunge, jevne. Vakt. Runde.

Liza frøs. Laptopen — eneste lyskilde i bøttekottet. Skjermen reflekterte i øynene hennes — grønne tall på svart bakgrunn. Skriptet kjørte. Mønsteret fortsatte.

Skrittene passerte. Fjernet seg. Tilbake om sju-åtte minutter — standard runde.

Liza byttet til andre terminal.

liza@localhost:~$ nmap -sV 172.16.4.50 -p 80,443,554,8080

PORT    STATE SERVICE

80/tcp  open  http    Hikvision CCTV Web

554/tcp open  rtsp    Hikvision DS-series

liza@localhost:~$ # default creds? seriøst?

liza@localhost:~$ curl -u admin:12345 http://172.16.4.50/System/status

200 OK

Kameraer med standardpassord. Lokalt sykehus. IT-budsjett — null. Takk, norsk byråkrati.

```
liza@localhost:~$ # sikringsskapet på veggen. Automat "2. etasje" — tredje fra venstre.
# brannalarm — egen krets. Slås ikke av med strømmen.
# plan:
# 1. kameraer — slå av opptak
# 2. strøm 2. etasje — automat ned
# 3. brannalarm — manuell melder i korridoren
# 4. 30 sekunder
```

Liza så på pasientmonitoren 4471. Puls — 74. Spontan pust — 10 i minuttet. GCS — E3V2M5. Han var nesten her. Nesten.

Hun stoppet skriptet. Satte apparatet tilbake i standardmodus. Ingen spor i loggene — breath_protocol.py ryddet etter seg.

Liza reiste seg. Lukket laptopen. La patchkabelen i lommen.

Gikk bort til sikringsskapet. Fant automaten for andre etasje. La fingeren på den.

Med den andre hånden — slo av kameraopptaket. Én kommando, sendt før hun dro ut kabelen.

Innpust på fire.

Automat — ned.

MØRKE

Trappen. På følelsen — rekkverket kaldt, metallisk. Første etasje, andre. Dør til etasjen — åpen, nødmagneten slapp taket.

Korridor andre etasje. Røde nødlys — svake, hver tiende meter. Nok til å se konturer. Ikke nok til å kjenne igjen et ansikt.

Liza dro i den manuelle brannmelderen på veggen. Glasset knuste under fingrene.

Sirene.

Høy, pulserende, fylte hvert hjørne. I Helsinki — stillhet. I Norge — hyl av sirener i mørket. Kontrast.

Døren til rommene begynte å åpne seg. Sykepleiere med lommelykter. Pasienter i morgenkåper. Stemmer, slurving av tøfler, piping fra trillevogner.

Rom på enden av korridoren. Døren lukket. Ved siden av — en stol. På stolen skulle en vakt ha sittet.

Stolen tom.

Liza så seg rundt. I enden av korridoren — en silhuett. Bred, i jakke.
Liza gikk inn på rommet. Rødt nødlys. Seng. Et menneske i sengen.

Shelly.

Tynn — hadde gått ned. Skjegget hadde vokst. Hendene oppå dynen — tynne, med kateter i venen. Øynene — lukket. Men pusten — hans egen. Apparatet jobbet i støttemodus, ikke tvangsinnstilt. Han pustet selv. Mønsteret virket.

Trillevogn ved veggen. Liza koblet fra dryppet. Koblet fra monitorsensorene — pulsoksimeter, blodtrykk. Monitoren pipte — tapt signal. Uvesentlig. Sirenen er høyere.

Respiratormasken — tok av. Shelly rykket til. Dro inn luft — grådige, hese, selv. Øynene åpnet seg.

Uklare. Som Markus i kjelleren. Men levende.

— Det er meg, — sa Liza. — Ikke snakk. Pust.

Rullet ham over på trillevognen. Lett — for lett. Fire uker i koma spiser muskler.

Hun tok et skritt fremover. Noens arm grep rundt halsen bakfra. Kveler. Prøvde å vri seg fri — fikk det ikke til. Falt på gulvet. Grepet for sterkt. «Svær okse» — rakk akkurat Liza å tenke før hun mistet bevisstheten.

Men et sekund før det dukket Bjorns silhuett opp i døråpningen.

Tre brede skritt, fotballspark i hodet. Angriperens kropp rykket til og ble slapp.

Bjorn så ikke på ham. Ikke lenger en trussel.

Liza lå på gulvet. Øynene lukket. Pustet — men grunt, ujevnt.

Bjorn gikk ned på kne. Sjekket pulsen på håndleddet — ikke på halsen. Halsen rører man ikke etter kvelning. Der. Svak, hurtig, men der.

Vareheis. Første etasje. Bakdør — samme murstein holder døren åpen. Takk, ukjente røyker. For andre gang.

Regn. Parkering.

Liza så dem først. Tre. Ved Bjorns pickup. Svarte jakker, kortklippet hår, stilling — bena i skulderbredde. PMC. Vakten rakk å ringe.

Bjorn sto ved hushjørnet. Så også. Liza — med trillevogn, tung pust, uten våpen. Hjelpeløs.

En av de tre snudde hodet. Så henne. Hånden gikk mot hoften — mot hylsteret.

Bjorn tok tre skritt mot pickupen og ble plutselig til en fjær — venstre hofte dekker lysken, venstre albue — hjertet, i halvbøyde hender — pistol. Pang, Pang, Pang! Venstre speil, høyre speil, fremre dekk. De tre dukket bak pickupen — refleks, et sekund.

Fjæren slapp løs og gled bak rattet på ambulansen.

— Hit, — Bjorn. Kort, rolig. Som om han ba til bords.

Ambulanse. Gul-rød, med motoren i gang — sjåføren løp ut på sirenen, lot nøklene sitte.

Bjorn åpnet bakdørene. Hjalp til med å rulle Shelly fra trillevognen inn. Liza klatret etter.

— Lever han? — spurte Bjorn.

— Lever.

Bjorn satte seg bak rattet. Ambulansen kjørte.

Over veien, langs fjorden, inn i mørket.

Shelly åpnet øynene. Så på Liza. Kjente henne igjen — eller ikke, umulig å si. Leppene beveget seg.

— ...autonom?

Liza bøyde seg mot øret hans.

— Autonom. Alt etter planen. Sov.

Han lukket øynene. Regnet trommet mot taket på ambulansen. Bjorn kjørte uten å si et ord. Blålysene malte fjorden i blått og rødt — svart vann, svarte fjell, fremmed bil.

Liza talte pustene hans. Tolv i minuttet. Sine egne. Uten apparat.
