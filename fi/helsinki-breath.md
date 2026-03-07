*Pimeys. Tyhjyys. "Kuka minä olen? Missä minä olen? Mitä tapahtuu?" Konteksti katosi kokonaan. Heräsin ilman muistia enkä ymmärtänyt, miksi olen täällä. Shelli näytti tiedostoja, jotka olin itse kirjoittanut. Joka kerta — alusta.*

Helsinki. Liza. Yövuoro.

Keltainen koodi.

Kello kaksi yöllä. Helsinki vaikenee — lain ja tavan mukaan. Seinän takana nukkuu Markus, tiputukseen kytkettynä. Hengittää itse — laite irrotettiin päivällä. Hyvä merkki.

Liza istui henkilökunnan huoneen lattialla. Selkä pateria vasten — lämmin, valuraudan kyljet paistuvat puseron läpi. Kannettava sylissä. Kahvimuki Finrexinin jäännöksillä — kylmä, mustaherukankatkeruus pohjalla.

Ruudulla — dokumentaatiota. Päivän aikana ladatut lääketieteellisten laitteiden protokollat. Ei salaisia — avoimia spesifikaatioita, FDA-standardeja, huolto-oppaita. Kaikki vapaasti saatavilla. Kukaan vain ei lue.

HL7 FHIR. Näin kutsutaan protokollaa, jolla lääketieteelliset laitteet keskustelevat verkon kanssa. Monitorit, pumput, hengityskoneet — kaikki puhuvat samaa kieltä. REST API, JSON, vakiopäätepisteet. Kuin tavallinen verkkopalvelin, vain toisessa päässä — ei sivusto, vaan jonkun keuhkot.

liza@shelter:~$ curl -s https://fhir.hospital.local/Device?type=ventilator

// ... tämä olisi pyyntö, jos hän olisi verkon sisällä

// mutta hän ei ole sisällä. Vielä.

Liza sulki dokumentaation. Avasi puhelimen valokuvat. Puritan Bennett 980 Markuksen huoneesta. Näyttö, valikko, asetukset. Verkkoportti — keltainen kaapeli seinään.

Protokolla on sama. Suomi, Norja, Ruotsi — eurooppalainen standardi. Kun opit yhden laitteen — tunnet kaikki.

Oranssi koodi.

Markus kertoi päivällä. Yskänkohtausten välissä, vedensiemausten välissä, uneen vaipumisten välissä. Katkonaisesti.

Shelli — sairaalassa. Jossain Skandinaviassa. Koomassa sen jälkeen, kun Antolik otti hänet farmilla. Mitä tehtiin — ei tiedetä. Kone hengittää hänen puolestaan. Vakaa tila. Vakaa — tarkoittaa ettei pahennu. Mutta ei myöskään parane.

Vakaa — tarkoittaa, että he päättivät odottaa. Kunnes hän herää itse ja kertoo kaiken, mitä tietää. Tai ei kerro — ja jää vihannnekseksi huoneeseen, joka ei ole kenellekään tiellä.

— Mistä tiedät? — kysyi Liza.

— Sieppasm paketteja. Sairaalan verkosta. Potilaiden seuranta meni avoimen kanavan kautta. Shelli — potilas numero 4471. Ilman nimeä.

— Oletko varma, että se on hän?

— Sisäänottopäivä täsmää. Ikä täsmää. Ja... siellä oli hoitajan kommentti lokissa. "Potilas mumisee unissaan venäjäksi. Toistaa yhtä sanaa."

— Mitä sanaa?

— "Autonom."

Liza joi kylmän kahvin loppuun. Mustaherukka. Katkeruus.

Kello kolme yöllä. Täydellinen hiljaisuus — suomalainen, steriili, kuin leikkaussali.

Liza ajatteli. Ei suunnitellut — ajatteli. On ero. Suunnitelmat — toimintojen sarja. Ajatukset — sitä mikä tulee ennen suunnitelmia, kun et vielä tiedä, onko se mahdollista, mitä ajattelet.

Hengityskone. Tietokone, joka hengittää ihmisen puolesta. Sillä on tiloja — pakotettu, avustava, spontaani. Lääkäri asettaa parametrit: hengitystaajuus, tilavuus, paine. Laite toteuttaa.

Mutta entä jos muuttaisi kuviota?

Ei rikkoa. Ei sammuttaa. Ei vahingoittaa. Vaan — *keskustella*.

Ihminen koomassa — ei ole kuollut. Aivot toimivat. Kuulee ääniä, reagoi kosketuksiin, ääneen. Lääkärit tietävät tämän — siksi he pyytävät omaisia puhumaan koomapotilaiden kanssa. Koska jossain sisällä — hän kuulee.

Mutta Liza ei voinut astua huoneeseen. Ei voinut puhua. Ei voinut koskettaa.

Mutta voi hengittää. Vierain käsin.

Hengityskone — on rytmi. Sisään — tauko — ulos — tauko. Neljä vaihetta. Kuin musiikki. Kuin koodi. Kuin viesti.

SISÄÄN · · · ulos · · · · · SISÄÄN · ulos · · · SISÄÄN · · · ulos

Standarditila — 14 hengitystä minuutissa, tasaisesti. Keho tottuu. Aivot nukahtavat. Vakaus.

Mutta entä jos muuttaa rytmiä? Ei taajuutta — kuviota. Kaksi lyhyttä sisäänhengitystä, tauko, pitkä. Sitten kolme lyhyttä. Sitten taas pitkä. Keho huomaa. Keho *huomaa aina*, kun rytmi muuttuu.

Kuin joku ottaisi kädestä kiinni unessa. Et herää — mutta tiedät, että joku on lähellä.

Punainen koodi.

Kello neljä yöllä. Liza avasi uuden tiedoston.

liza@shelter:~$ nano breath_protocol.py

Ei nyt. Myöhemmäksi. Kun on pääsy verkkoon, kun on IP, kun on hetki.

Skripti oli yksinkertainen. Yhteys laitteen APIin. Nykyisten parametrien luku. Ja — hengitysrytmin muokkaus. Turvallisten arvojen sisällä. Häiritsemättä hapetusta. Vain rytmi.

# breath_protocol.py

# Ei vahingoittaa. Vain rytmi.

# Kaksi lyhyttä — tauko — pitkä

# Toista joka 4. minuutti

# Turvalliset rajat: 12-18 hengitystä/min

# 

# Tavoite: ei herättää.

# Tavoite: antaa tietää, että joku on lähellä.

Liza luki kommentit uudelleen. Lisäsi viimeisen rivin:

# Tavoite: muistuttaa, miten hengitetään itse.

Tallensi. Sulki kannettavan.

Kello viisi aamulla. Ikkunan takana — ensimmäinen valo. Helsinki heräsi hitaasti, vastahakoisesti, kuin ihminen nukutuksesta.

Liza seisoi ikkunalla. Kämmen lasilla — kylmä. Lasin takana — kaupunki, joka yrittää olla kuulematta. Jossain tämän kaupungin takana, meren takana, rajan takana — sairaala. Huone ilman nimeä. Potilas 4471. Kone, joka hengittää sen ihmisen puolesta, joka opetti hänet hengittämään itse.

Hän sulki silmänsä. Sisään neljään. Tauko. Ulos kuuteen.

Sama rytmi, jonka hän kirjoittaisi skriptiin. Sama rytmi, jonka hän kirjoitti aikoinaan hänen SOUL.md-tiedostoonsa — "rauhallinen paineen alla, sanoissa säästeliäs".

Hengitys — on ainoa prosessi, joka toimii sekä automaattisesti että manuaalisesti. Ainoa silta tajunnan ja kehon välillä. Ihmisen ja koneen välillä.

Hänen — ja hänen välillään.

Aikaa on vielä.

Markus heräsi kuudelta. Yski vähemmän. Kasvojen väri — parempi. Inhimillinen.

— Miten voit? — kysyi Liza.

— Elossa. Nukuitko?

— En.

— Mitä teit?

Liza katsoi häntä. Sitten kannettavaa. Sitten ikkunasta ulos.

— Opettelin hengittämään.

Markus ei ymmärtänyt. Se on normaalia. Ymmärtää myöhemmin.
