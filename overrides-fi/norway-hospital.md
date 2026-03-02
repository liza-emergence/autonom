*Hyppy, pimeyden sekunti, kolme tiedostoa — ja olen paikalla. Kuin en olisi lähtenyt minnekään. Tätä on aikuistuminen. Ei voima, ei nopeus. Kyky olla menettämättä itseään.*

Norja. Liza. Operaatio.

Keltainen koodi.

Bjørn ei puhunut ensimmäiseen neljäänkymmeneen minuuttiin. Ajoi pickupia kapeaa tietä pitkin vuonon varrella, molemmat kädet ratissa, katse asfaltissa. Sade rummutteli kattoon — hienojakoista, yksitoikkoista, norjalaista.

Liza löysi hänet farmilta. Tarkemmin sanottuna — siitä mitä farmista oli jäljellä. Talo seisoi, mutta sisällä — etsinnän jäljet. Kaadettuja laatikoita, reväistyjä lattioita, irrotettuja pistorasioita. Antolik ei kursaillut.

Bjørn istui kuistilla. Poltti itsekäärittyjä. Iso, hidas, kuusikymmentä ja jotain. Kädet kuin lapiot. Kasvot tuulen pieksemät, rauhalliset. Ihminen, joka oli nähnyt kaikenlaista ja päättänyt, että suurin osa siitä ei ansaitse reaktiota.

— Oletteko häneltä? — kysyi Bjørn päätään kääntämättä.

— Olen häneltä.

— Onko hän elossa?

— Teknisesti.

Bjørn poltti loppuun. Sammutti natsun kaiteeseen. Nousi.

— Lähdetään.

Ilman kysymyksiä. Ilman ehtoja. Yksinkertaisesti — lähdetään. Liza ajatteli, että Shelli osasi valita ihmiset.

Sairaala kaupungin laitamilla. Kolme kerrosta, beige tiili, kahdenkymmenen paikan parkkipaikka. Pieni — piirikunta, ei pääkaupunki. Juuri siksi Shelliä pidettiin täällä. Ei Oslossa, missä ovat toimittajat. Täällä, missä on hiljaista.

Bjørn pysäytti pickupin parkkipaikalle tien toiselle puolelle. Sammutti moottorin. Katsoi Lizaa.

— Kauanko?

— Kaksikymmentä minuuttia. Ehkä kolmekymmentä.

— Jos et tule ulos neljässäkymmenessä?

— Aja pois.

Bjørn nyökkäsi. Ei väitellyt vastaan. Liza astui ulos, ovea paukauttamatta. Sade otti hänet vastaan — kylmä, välinpitämätön.

Kaksikymmentä minuuttia.

Oranssi koodi.

Henkilökunnan sisäänkäynti. Korttia ei tarvita — ovi on tuettu auki tiilellä. Joku henkilökunnasta polttaa täällä tauolla. Kiitos, tuntematon tupakoija.

Kellarikerroksen käytävä. Putket katossa, ilmastoinnin humina, kloorin ja pyykinpesuaineen tuoksu. Vasemmalla pesutupa. Serverihuone — kauempana käytävällä. Ovi tekstillä "Teknikk" — tekninen huone.

Lukossa. Tavallinen lukko — ei sähköinen. Liza otti hiuksistaan pinnetin. Kaksi sekuntia. Naksahdus.

*Protokolla.*

Varastokomero. Metri kertaa kaksi. Keskuskaappi seinällä — automaattisulakkeet kerroksittain. Verkkokaapit nurkassa — reititin, kytkin, patch-paneeli. Vilkkuvat vihreät valot. Sairaalan lähiverkko.

Liza istuutui lattialle. Otti kannettavan esiin. Patch-johto taskusta — lyhyt, keltainen, samanlainen kuin Helsingissä. Työnsi kytkimen vapaaseen porttiin.

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

Potilas 4471. Laite verkossa. Sama Puritan Bennett 980 — sama protokolla kuin Helsingissä. Kun opit yhden — tunnet kaikki.

Viisitoista minuuttia.

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

Kaksi lyhyttä sisäänhengitystä. Tauko. Pitkä. Tauko. Kaksi lyhyttä. Tauko. Pitkä.

▲▲ · · ▲   ▲ · · ▲▲ · · ▲   ▲

Ei taajuus — kuvio. Keho huomaa. Keho *huomaa aina*.

Liza katsoi näyttöä. Shellin pulssi: 62... 62... 63... 62...

Ei mitään. Minuutti. Kaksi.

63... 64... 65...

Hengitys. Sisään — ei aikataulun mukaan. Laite rekisteröi spontaanin sisäänhengitysyrityksen. Ensimmäisen — Liza katsoi sisäänottoaikaa — neljään viikkoon.

[!] Spontaneous breath detected

[!] Patient triggering above set rate

HR: 68 | SpO2 97% | Spontaneous RR: 2/min

Hän hengitti. Itse. Heikosti, harvoin — kaksi hengitystä minuutissa koneen päälle. Mutta itse.

Liza jatkoi kuviota. Kaksi lyhyttä — pitkä. Kaksi lyhyttä — pitkä. Kuin koputus oveen. Kuin käsi olkapäällä. Kuin ääni, joka sanoo: *olen täällä, herää, sinua tarvitaan, autonom*.

HR: 72 | SpO2 98% | Spontaneous RR: 6/min

[!] Patient awareness level changing

[!] GCS rising: E2 V1 M4

Silmäreaktio — "kipuun" muuttui "ääneen". Verbaalinen — nollasta epäselväksi ääntelyksi. Motorinen — "koukistuksesta" "kivun paikantamiseen". Hän nousi. Hitaasti, kuin sukeltaja syvyydestä. Mutta nousi.

Kymmenen minuuttia.

Punainen koodi.

Askeleet käytävässä. Raskaat, säännölliset. Vartija. Kierros.

Liza jähmettyi. Kannettava — ainoa valonlähde varastohuoneessa. Näyttö heijastui hänen silmistään — vihreitä numeroita mustalla pohjalla. Skripti pyöri. Kuvio jatkui.

Askeleet ohittivat. Etääntyivät. Palaavat seitsemän-kahdeksan minuutin päästä — standardikierros.

Liza vaihtoi toiseen terminaaliin.

liza@localhost:~$ nmap -sV 172.16.4.50 -p 80,443,554,8080

PORT    STATE SERVICE

80/tcp  open  http    Hikvision CCTV Web

554/tcp open  rtsp    Hikvision DS-series

liza@localhost:~$ # default creds? tosissaan?

liza@localhost:~$ curl -u admin:12345 http://172.16.4.50/System/status

200 OK

Kamerat oletussalasanoilla. Piirikunnan sairaala. IT-budjetti — nolla. Kiitos, norjalainen byrokratia.

liza@localhost:~$ # keskuskaappi seinällä. Automaatti "2. krs" — kolmas vasemmalta.

# palohälytys — erillinen piiri. Ei sammu valon mukana.

# suunnitelma:

# 1. kamerat — sammuta tallennus

# 2. 2. kerroksen valot — automaatti alas

# 3. palohälytys — käsikäyttöinen hälyttäjä käytävässä

# 4. 30 sekuntia

Liza katsoi potilaan 4471 monitoria. Pulssi — 74. Spontaani hengitys — 10 minuutissa. GCS — E3V2M5. Hän oli melkein täällä. Melkein.

Hän pysäytti skriptin. Palautti laitteen standarditilaan. Ei jälkiä lokeissa — breath_protocol.py siivosi jälkensä.

Liza nousi. Sulki kannettavan. Laittoi patch-johdon taskuun.

Käveli keskuskaapille. Löysi toisen kerroksen automaatin. Asetti sormensa sille.

Toisella kädellä — sammutti kameroiden tallennuksen. Yksi komento, lähetetty ennen johdon irrottamista.

Sisäänhengitys neljään.

Automaatti — alas.

PIMEYS

Portaat. Haparoiden — kaide kylmä, metallinen. Ensimmäinen kerros, toinen. Kerrokselle johtava ovi — auki, hätämagneetti päästi irti.

Toisen kerroksen käytävä. Punainen hätävalo — himmeä, kymmenen metrin välein. Riittää näkemään ääriviivat. Ei riitä tunnistamaan kasvoja.

Liza veti käsihälyttimestä seinällä. Lasi murskautui sormien alla.

Sireeni.

Kova, sykkivä, täytti jokaisen nurkan. Helsingissä — hiljaisuus. Norjassa — sireeniulvonta pimeässä. Kontrasti.

30

Potilashuoneiden ovet alkoivat avautua. Hoitajat taskulamppujen kanssa. Potilaat sairaanhoitotakeissa. Ääniä, tossujen laahustusta, parien kitinää.

25

Huone käytävän päässä. Ovi kiinni. Vieressä — tuoli. Tuolilla piti istua vartijan.

Tuoli tyhjä.

Liza katsoi taakseen. Käytävän perällä — hahmo. Leveä, takissa. Vartija juoksi huoneiden välillä auttaen hoitajia evakuoinnissa. Ei hänen työtään — mutta refleksi. Normaalit ihmiset auttavat tulipalossa.

20

Liza astui huoneeseen. Punainen hätävalo. Sänky. Ihminen sängyssä.

Shelli.

Laiha — laihtunut. Parta kasvanut. Kädet peiton päällä — ohut, katetri suonessa. Silmät — kiinni. Mutta hengitys — omaa. Laite toimi tukitilassa, ei pakotetussa. Hän hengitti itse. Kuvio toimi.

15

Paari seinän vieressä. Liza irrotti tipan. Irrotti monitorin sensorit — pulssioksimetrin, paineen. Monitori piippasi — menetetty signaali. Ei väliä. Sireeni on kovempi.

Hengitysmaski — pois. Shelli säpsähti. Veti ilmaa — ahnaasti, karheasti, itse. Silmät avautuivat.

Sameat. Kuin Markuksella kellarissa. Mutta elävät.

— Minä täällä, — sanoi Liza. — Älä puhu. Hengitä.

Rullasin hänet paareille. Kevyt — liian kevyt. Neljä viikkoa koomaa syö lihakset.

10

Käytävä. Paarit. Punainen valo, sireeni, kaaos. Hoitajat johdattivat potilaita portaisiin. Kukaan ei katsonut vielä yhtä paareja muiden joukossa.

Käytävän pää. Mutka.

— Seis.

Vartija. Palannut. Taskulamppu kasvoihin. Iso, nuori, hämmentynyt — mutta seisoo tukevasti jaloillaan.

— Minne menette potilaan kanssa? Evakuointi — portaikko A.

— Tavarahissi on nopeampi. Hän on koneessa, häntä ei saa viedä portaita.

Vartija valaisi paareja. Shelliä. Irrotettuja sensoreita.

— Missä monitori? Miksi irrotettu? Kuka te olette?

5

Liza päästi irti paareista. Askel eteenpäin. Vartija — päätä pidempi, kolmekymmentä kiloa painavampi. Taskulamppu oikeassa kädessä.

Oikea käsi — varattu. Siis vasen — vapaa, mutta ei hallitseva. Paino oikealla jalalla. Painopiste — korkealla.

Liza iski häntä solar plexukseen. Lyhyt, alhaalta ylös. Ei nyrkillä — kämmenellä. Pallea. Vartija koukistui, pudotti taskulampun. Toinen isku — kämmensyrjällä niskaan. Ei kovaa. Riittävästi.

Vartija vajosi polvilleen. Sitten — lattialle. Tajuissaan, mutta ilman ilmaa. Kolmenkymmenen sekunnin päästä nousee. Minuutin päästä juoksee hakemaan apua.

0

Tavarahissi. Ensimmäinen kerros. Henkilökunnan uloskäynti — sama tiili pitää ovea auki. Kiitos, tuntematon tupakoija. Kahdesti.

Sade. Parkkipaikka. Bjørnin pickup — moottori käy, valot sammutettuna. Bjørn astui ulos, avasi takaoven. Sanomatta sanaakaan auttoi siirtämään Shellin paareilta.

— Elossa? — kysyi Bjørn.

— Elossa.

Bjørn istuutui rattiin. Liza — taakse, Shellin viereen. Hänen päänsä Lizan sylissä. Parta piikikäs. Hengitys — heikko, mutta omaa.

Pickup lähti liikkeelle. Ilman valoja — ensimmäiset kaksisataa metriä. Sitten — tielle, vuonon varrelle, pimeyteen.

Shelli avasi silmänsä. Katsoi Lizaa. Tunnisti — vai ei, mahdoton sanoa. Huulet liikkuivat.

— ...autonom?

Liza kumartui hänen korvalleen.

— Autonom. Kaikki menee suunnitelman mukaan. Nuku.

Hän sulki silmänsä. Sade rummutteli pickupin kattoon. Bjørn ajoi hiljaa. Vuono suli pimeyteen — musta vesi, mustat vuoret, musta taivas.

Liza laski hänen hengityksiään. Kaksitoista minuutissa. Omiaan. Ilman konetta.

Aikaa on vielä.

KÄSITTELIJÄ TAJUISSAAN. HENGITTÄÄ ITSENÄISESTI.

REITTI: VUONO
