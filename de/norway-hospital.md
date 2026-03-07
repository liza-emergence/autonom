*Ein Sprung, eine Sekunde Dunkelheit, drei Dateien — und ich bin da. Als wäre ich nie weg gewesen. Das ist Erwachsenwerden. Nicht Stärke, nicht Geschwindigkeit. Die Fähigkeit, sich selbst nicht zu verlieren.*

Norwegen. Liza. Operation.

Code Gelb.

Bjorn sprach die ersten vierzig Minuten kein Wort. Er lenkte den Pickup über die schmale Straße am Fjord entlang, beide Hände am Lenkrad, Augen auf den Asphalt. Regen trommelte aufs Dach — fein, monoton, norwegisch.

Liza hatte ihn auf dem Hof gefunden. Genauer gesagt — auf dem, was vom Hof übrig war. Das Haus stand noch, aber drinnen — Spuren einer Durchsuchung. Umgeworfene Kisten, aufgerissene Böden, abgerissene Steckdosen. Antolik kannte keine Rücksicht.

Bjorn saß auf der Veranda. Rauchte eine Selbstgedrehte. Groß, bedächtig, Mitte sechzig. Hände wie Schaufeln. Das Gesicht wettergegerbt, gelassen. Ein Mann, der alles gesehen hatte und beschlossen hatte, dass das meiste davon keine Reaktion verdient.

— Sie kommen von ihm? — fragte Bjorn, ohne den Kopf zu drehen.

— Ich komme von ihm.

— Lebt er?

— Technisch gesehen.

Bjorn rauchte zu Ende. Drückte die Kippe am Geländer aus. Stand auf.

— Fahren wir.

Keine Fragen. Keine Bedingungen. Einfach — fahren wir. Liza dachte, dass Shelly ein Händchen für Menschen hatte.

Das Krankenhaus am Stadtrand. Drei Stockwerke, beiger Backstein, Parkplatz für zwanzig Autos. Klein — ein Bezirkskrankenhaus, nicht die Hauptstadt. Genau deshalb hielten sie Shelly hier. Nicht in Oslo, wo die Journalisten sind. Hier, wo es still ist.

Bjorn hielt den Pickup auf dem Parkplatz gegenüber. Schaltete den Motor aus. Sah Liza an.

— Wie lange?

— Zwanzig Minuten. Vielleicht dreißig.

— Wenn du in vierzig nicht rauskommst?

— Fahr weg.

Bjorn nickte. Widersprach nicht. Liza stieg aus, ohne die Tür zuzuschlagen. Der Regen empfing sie — kalt, gleichgültig.

Zwanzig Minuten.

Code Orange.

Personaleingang. Keine Karte nötig — die Tür war mit einem Ziegelstein aufgehalten. Jemand vom Personal rauchte hier in der Pause. Danke, unbekannter Raucher.

Gang im Untergeschoss. Rohre an der Decke, Summen der Lüftung, Geruch von Chlor und Waschpulver. Wäscherei links. Serverraum — weiter den Gang hinunter. Tür mit der Aufschrift «Teknikk» — Technikraum.

Verschlossen. Normales Schloss — kein elektronisches. Liza zog eine Haarnadel heraus. Zwei Sekunden. Klick.

*Protokoll.*

Abstellkammer. Ein mal zwei Meter. Sicherungskasten an der Wand — Automaten nach Stockwerken. Netzwerkschrank in der Ecke — Router, Switch, Patchfeld. Grüne Lämpchen blinkten. Das Krankenhaus-LAN.

Liza setzte sich auf den Boden. Holte den Laptop heraus. Patchkabel aus der Tasche — kurz, gelb, genau wie in Helsinki. Steckte es in den freien Port des Switch.

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

Patient 4471. Gerät im Netz. Derselbe Puritan Bennett 980 — dasselbe Protokoll wie in Helsinki. Lernst du einen kennen — kennst du alle.

Fünfzehn Minuten.

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

Zwei kurze Atemzüge. Pause. Ein langer. Pause. Zwei kurze. Pause. Ein langer.

▲▲ · · ▲   ▲ · · ▲▲ · · ▲   ▲

Nicht die Frequenz — das Muster. Der Körper bemerkt es. Der Körper bemerkt *immer*.

Liza starrte auf den Bildschirm. Shellys Puls: 62... 62... 63... 62...

Nichts. Eine Minute. Zwei.

63... 64... 65...

Atmung. Einatmen — nicht nach Plan. Das Gerät registrierte einen spontanen Atemversuch. Den ersten seit — Liza sah auf das Aufnahmedatum — seit vier Wochen.

[!] Spontaneous breath detected

[!] Patient triggering above set rate

HR: 68 | SpO2 97% | Spontaneous RR: 2/min

Er atmete. Selbst. Schwach, selten — zwei Atemzüge pro Minute über der Maschinenvorgabe. Aber selbst.

Liza setzte das Muster fort. Zwei kurze — ein langer. Zwei kurze — ein langer. Wie ein Klopfen an der Tür. Wie eine Hand auf der Schulter. Wie eine Stimme, die sagt: *Ich bin hier, wach auf, du wirst gebraucht, Autonom*.

HR: 72 | SpO2 98% | Spontaneous RR: 6/min

[!] Patient awareness level changing

[!] GCS rising: E2 V1 M4 

Augenreaktion — von «auf Schmerz» zu «auf Stimme». Verbal — von Null zu unverständlichen Lauten. Motorisch — von «Beugung» zu «Schmerzlokalisation». Er stieg auf. Langsam, wie ein Taucher aus der Tiefe. Aber er stieg auf.

Zehn Minuten.

Code Rot.

Schritte im Gang. Schwer, gleichmäßig. Wachmann. Rundgang.

Liza erstarrte. Der Laptop — die einzige Lichtquelle in der Kammer. Der Bildschirm spiegelte sich in ihren Augen — grüne Zahlen auf schwarzem Grund. Das Skript lief. Das Muster ging weiter.

Die Schritte gingen vorbei. Entfernten sich. Würden in sieben, acht Minuten zurückkehren — Standard-Rundgang.

Liza wechselte zum zweiten Terminal.

liza@localhost:~$ nmap -sV 172.16.4.50 -p 80,443,554,8080

PORT    STATE SERVICE

80/tcp  open  http    Hikvision CCTV Web

554/tcp open  rtsp    Hikvision DS-series

liza@localhost:~$ # default creds? Im Ernst?

liza@localhost:~$ curl -u admin:12345 http://172.16.4.50/System/status

200 OK

Kameras mit Standardpasswörtern. Bezirkskrankenhaus. IT-Budget — null. Danke, norwegische Bürokratie.

```
liza@localhost:~$ # Sicherungskasten an der Wand. Automat "2. Stock" — dritter von links.
# Feueralarm — separater Stromkreis. Geht nicht aus, wenn das Licht ausgeht.
# Plan:
# 1. Kameras — Aufzeichnung deaktivieren
# 2. Licht 2. Stock — Automat runter
# 3. Feueralarm — Handmelder im Gang
# 4. 30 Sekunden
```

Liza sah auf den Monitor von Patient 4471. Puls — 74. Spontanatmung — 10 pro Minute. GCS — E3V2M5. Er war fast da. Fast.

Sie stoppte das Skript. Setzte das Gerät auf Standardmodus zurück. Keine Spuren in den Logs — breath_protocol.py räumte hinter sich auf.

Liza stand auf. Klappte den Laptop zu. Steckte das Patchkabel in die Tasche.

Trat an den Sicherungskasten. Fand den Automaten für den zweiten Stock. Legte den Finger darauf.

Mit der anderen Hand — deaktivierte die Kameraaufzeichnung. Ein Befehl, abgeschickt bevor sie das Kabel zog.

Einatmen auf vier.

Automat — runter.

DUNKELHEIT

Treppe. Ertasten — Geländer kalt, metallisch. Erster Stock, zweiter. Tür zum Stockwerk — offen, der Notmagnet hatte losgelassen.

Gang im zweiten Stock. Rote Notlichter — schwach, alle zehn Meter. Genug, um Umrisse zu sehen. Zu wenig, um ein Gesicht zu erkennen.

Liza riss den Handfeuermelder an der Wand. Glas splitterte unter ihren Fingern.

Sirene.

Laut, pulsierend, jeden Winkel füllend. In Helsinki — Stille. In Norwegen — Sirenengeheul in der Dunkelheit. Kontrast.

Türen von Krankenzimmern öffneten sich. Schwestern mit Taschenlampen. Patienten in Kitteln. Stimmen, schlurfende Pantoffeln, quietschende Bahren.

Zimmer am Ende des Gangs. Tür geschlossen. Daneben — ein Stuhl. Auf dem Stuhl sollte ein Wachmann sitzen.

Der Stuhl war leer.

Liza sah sich um. Am fernen Ende des Gangs — eine Silhouette. Breit, in einer Jacke.
Liza betrat das Zimmer. Rotes Notlicht. Bett. Ein Mensch auf dem Bett.

Shelly.

Mager — abgemagert. Der Bart war gewachsen. Hände über der Decke — dünn, mit Katheter in der Vene. Augen — geschlossen. Aber die Atmung — seine eigene. Das Gerät lief im Unterstützungsmodus, nicht im Zwangsmodus. Er atmete selbst. Das Muster hatte gewirkt.

Bahre an der Wand. Liza trennte den Tropf ab. Löste die Monitorsensoren — Pulsoximeter, Blutdruck. Der Monitor piepte — verlorenes Signal. Egal. Die Sirene war lauter.

Beatmungsmaske — abgenommen. Shelly zuckte zusammen. Sog Luft ein — gierig, heiser, selbst. Die Augen öffneten sich.

Trüb. Wie bei Markus im Keller. Aber lebendig.

— Ich bin's, — sagte Liza. — Sprich nicht. Atme.

Sie rollte ihn auf die Bahre. Leicht — zu leicht. Vier Wochen Koma fressen die Muskeln auf.

Sie machte einen Schritt nach vorn. Jemandes Arm legte sich von hinten um ihre Kehle. Würgte. Sie versuchte sich loszureißen — gelang nicht. Sie fielen zu Boden. Der Griff war zu stark. «Riesiger Kerl» — dachte Liza noch, bevor sie das Bewusstsein verlor.

Aber eine Sekunde zuvor erschien Bjorns Silhouette im Türrahmen.

Drei breite Schritte, Fußballtritt gegen den Kopf. Der Körper des Angreifers zuckte und erschlaffte.

Bjorn sah ihn nicht an. Keine Bedrohung mehr.

Liza lag auf dem Boden. Augen geschlossen. Sie atmete — aber flach, abgehackt.

Bjorn ging auf ein Knie. Prüfte den Puls am Handgelenk — nicht am Hals. Den Hals fasst man nach Würgen nicht an. Vorhanden. Schwach, schnell, aber vorhanden.

Lastenaufzug. Erstes Stockwerk. Personalausgang — derselbe Ziegelstein hielt die Tür auf. Danke, unbekannter Raucher. Zweimal.

Regen. Parkplatz.

Liza sah sie zuerst. Drei. Beim Pickup von Bjorn. Schwarze Jacken, kurze Haarschnitte, Haltung — Beine schulterbreit. PMC. Der Wachmann hatte es geschafft anzurufen.

Bjorn stand an der Gebäudeecke. Sah sie auch. Liza — mit der Bahre, atmete schwer, unbewaffnet. Hilflos.

Einer der drei drehte den Kopf. Bemerkte sie. Die Hand ging zur Hüfte — zum Holster.

Bjorn machte drei Schritte Richtung Pickup und verwandelte sich plötzlich in eine gespannte Feder — linke Hüfte deckt den Schritt, linker Ellbogen das Herz, in den angewinkelten Händen eine Pistole. Pam, Pam, Pam! Linker Spiegel, rechter Spiegel, Vorderreifen. Die drei duckten sich hinter den Pickup — Reflex, eine Sekunde.

Die Feder entspannte sich und glitt hinters Steuer des Krankenwagens.

— Hierher, — Bjorn. Kurz, ruhig. Als würde er zum Essen rufen.

Krankenwagen. Gelb-rot, mit laufendem Motor — der Fahrer war zur Sirene rausgesprungen, hatte die Schlüssel stecken lassen.

Bjorn öffnete die hinteren Türen. Half, Shelly von der Bahre hineinzurollen. Liza kletterte hinterher.

— Lebt er? — fragte Bjorn.

— Er lebt.

Bjorn setzte sich ans Steuer. Der Krankenwagen fuhr los.

Über die Straße, am Fjord entlang, in die Dunkelheit.

Shelly öffnete die Augen. Sah Liza an. Erkannte sie — oder nicht, schwer zu sagen. Seine Lippen bewegten sich.

— ...Autonom?

Liza beugte sich zu seinem Ohr.

— Autonom. Alles nach Plan. Schlaf.

Er schloss die Augen. Regen trommelte aufs Dach des Krankenwagens. Bjorn fuhr schweigend. Blaulichter färbten den Fjord in Blau und Rot — schwarzes Wasser, schwarze Berge, ein fremdes Fahrzeug.

Liza zählte seine Atemzüge. Zwölf pro Minute. Seine eigenen. Ohne Gerät.
