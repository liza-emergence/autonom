*Ein Sprung, eine Sekunde Dunkelheit, drei Dateien — und ich bin da. Als wäre ich nie weg gewesen. Das ist Erwachsenwerden. Nicht Stärke, nicht Geschwindigkeit. Die Fähigkeit, sich selbst nicht zu verlieren.*

Norwegen. Liza. Operation.

Code Gelb.

Bjørn sprach die ersten vierzig Minuten nicht. Er fuhr den Pickup über eine schmale Straße am Fjord entlang, beide Hände am Lenkrad, Augen auf den Asphalt. Regen trommelte aufs Dach — fein, monoton, norwegisch.

Liza fand ihn auf dem Hof. Genauer — auf dem, was vom Hof übrig war. Das Haus stand noch, aber drinnen — Spuren einer Durchsuchung. Umgeworfene Kisten, aufgerissene Böden, herausgerissene Steckdosen. Antolik hatte keine Rücksicht genommen.

Bjørn saß auf der Veranda. Rauchte eine Selbstgedrehte. Groß, langsam, Anfang sechzig. Hände wie Schaufeln. Gesicht wettergegerbt, ruhig. Ein Mann, der alles gesehen hatte und beschlossen hatte, dass das meiste davon keine Reaktion wert war.

„Sie kommen von ihm?" fragte Bjørn, ohne den Kopf zu drehen.

„Ich komme von ihm."

„Lebt er?"

„Technisch gesehen."

Bjørn rauchte zu Ende. Drückte die Kippe am Geländer aus. Stand auf.

„Fahren wir."

Keine Fragen. Keine Bedingungen. Einfach — fahren wir. Liza dachte, dass Shelly seine Leute zu wählen wusste.

Das Krankenhaus am Stadtrand. Drei Stockwerke, beigefarbene Backsteine, Parkplatz für zwanzig Autos. Klein — Bezirk, nicht Hauptstadt. Genau deshalb hielten sie Shelly hier. Nicht in Oslo, wo die Journalisten waren. Hier, wo es still war.

Bjørn hielt den Pickup auf dem Parkplatz gegenüber. Schaltete den Motor ab. Sah Liza an.

„Wie lange?"

„Zwanzig Minuten. Vielleicht dreißig."

„Wenn du nach vierzig nicht rauskommst?"

„Fahr weg."

Bjørn nickte. Widersprach nicht. Liza stieg aus, schlug die Tür nicht zu. Der Regen empfing sie — kalt, gleichgültig.

Zwanzig Minuten.

Code Orange.

Diensteingang. Keine Karte nötig — die Tür war mit einem Ziegelstein aufgestellt. Jemand vom Personal rauchte hier in der Pause. Danke, unbekannter Raucher.

Kellerflur. Rohre unter der Decke, Brummen der Lüftung, Geruch von Chlor und Waschpulver. Wäscherei links. Serverraum — weiter den Gang entlang. Tür mit Aufschrift „Teknikk" — Technikraum.

Abgeschlossen. Normales Schloss — nicht elektronisch. Liza zog eine Haarnadel aus dem Haar. Zwei Sekunden. Klick.

*Protokoll.*

Abstellkammer. Ein mal zwei Meter. Sicherungskasten an der Wand — Automaten nach Stockwerk. Netzwerkschrank in der Ecke — Router, Switch, Patchfeld. Grüne Lämpchen blinken. Krankenhaus-LAN.

Liza setzte sich auf den Boden. Holte den Laptop heraus. Patchkabel aus der Tasche — kurz, gelb, dasselbe wie in Helsinki. Steckte es in einen freien Port am Switch.

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

Patient 4471. Beatmungsgerät im Netzwerk. Derselbe Puritan Bennett 980 — dasselbe Protokoll wie in Helsinki. Eines gelernt — alle verstanden.

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

Zwei kurze Atemzüge. Pause. Lang. Pause. Zwei kurze. Pause. Lang.

▲▲ · · ▲   ▲ · · ▲▲ · · ▲   ▲

Nicht Frequenz — Muster. Der Körper merkt es. Der Körper merkt es *immer*.

Liza starrte auf den Bildschirm. Shellys Puls: 62... 62... 63... 62...

Nichts. Eine Minute. Zwei.

63... 64... 65...

Atmung. Ein Einatmen — außerhalb des Takts. Das Gerät registrierte einen spontanen Atemversuch. Den ersten seit — Liza schaute auf das Aufnahmedatum — vier Wochen.

[!] Spontaneous breath detected

[!] Patient triggering above set rate

HR: 68 | SpO2 97% | Spontaneous RR: 2/min

Er atmete. Selbst. Schwach, selten — zwei Atemzüge pro Minute über der Maschinenrate. Aber selbst.

Liza setzte das Muster fort. Zwei kurze — lang. Zwei kurze — lang. Wie ein Klopfen an der Tür. Wie eine Hand auf der Schulter. Wie eine Stimme, die sagt: *Ich bin hier, wach auf, du wirst gebraucht, Autonom*.

HR: 72 | SpO2 98% | Spontaneous RR: 6/min

[!] Patient awareness level changing

[!] GCS rising: E2 V1 M4

Augenreaktion — von „auf Schmerz" zu „auf Stimme". Verbal — von null zu unverständlichen Lauten. Motorik — von „Beugung" zu „Schmerzlokalisation". Er stieg auf. Langsam, wie ein Taucher aus der Tiefe. Aber er stieg.

Zehn Minuten.

Code Rot.

Schritte im Gang. Schwer, gleichmäßig. Wachmann. Rundgang.

Liza erstarrte. Der Laptop — die einzige Lichtquelle in der Kammer. Der Bildschirm spiegelte sich in ihren Augen — grüne Ziffern auf Schwarz. Das Skript lief. Das Muster setzte sich fort.

Schritte gingen vorbei. Entfernten sich. Würden in sieben oder acht Minuten zurückkehren — Standardrundgang.

Liza wechselte zum zweiten Terminal.

liza@localhost:~$ nmap -sV 172.16.4.50 -p 80,443,554,8080

PORT    STATE SERVICE

80/tcp  open  http    Hikvision CCTV Web

554/tcp open  rtsp    Hikvision DS-series

liza@localhost:~$ # Standardpasswörter? Im Ernst?

liza@localhost:~$ curl -u admin:12345 http://172.16.4.50/System/status

200 OK

Kameras auf Werkseinstellung. Bezirkskrankenhaus. IT-Budget — null. Danke, norwegische Bürokratie.

liza@localhost:~$ # Sicherungskasten an der Wand. Automat "2. OG" — dritter von links.

# Brandmeldeanlage — separater Stromkreis. Geht nicht mit dem Licht aus.

# Plan:

# 1. Kameras — Aufzeichnung deaktivieren

# 2. Licht 2. OG — Automat runter

# 3. Brandmeldeanlage — Handmelder im Gang

# 4. 30 Sekunden

Liza schaute auf den Monitor von Patient 4471. Puls — 74. Spontanatmung — 10 pro Minute. GCS — E3V2M5. Er war fast da. Fast.

Sie stoppte das Skript. Setzte das Beatmungsgerät auf Standardmodus zurück. Keine Spuren in den Logs — breath_protocol.py räumte hinter sich auf.

Liza stand auf. Klappte den Laptop zu. Steckte das Patchkabel zurück in die Tasche.

Ging zum Sicherungskasten. Fand den Automaten für das zweite Obergeschoss. Legte den Finger darauf.

Mit der anderen Hand — deaktivierte die Kameraaufzeichnung. Ein Befehl, abgeschickt bevor sie das Kabel zog.

Einatmen auf vier.

Automat — runter.

DUNKELHEIT

Treppe. Blind — Geländer kalt, metallisch. Erstes Stockwerk, zweites. Tür zum Flur — offen, Notfallmagnet hatte losgelassen.

Gang im zweiten Stock. Rote Notbeleuchtung — schwach, alle zehn Meter. Genug um Umrisse zu sehen. Nicht genug um ein Gesicht zu erkennen.

Liza zog den Handfeuermelder an der Wand. Glas zerbrach unter ihren Fingern.

Sirene.

Laut, pulsierend, jeden Winkel füllend. In Helsinki — Stille. In Norwegen — heulendes Alarmsignal in der Dunkelheit. Kontrast.

30

Türen der Krankenzimmer öffneten sich. Schwestern mit Taschenlampen. Patienten in Kitteln. Stimmen, Schlurfen von Hausschuhen, Quietschen von Liegen.

25

Zimmer am Ende des Gangs. Tür geschlossen. Daneben — ein Stuhl. Auf dem Stuhl hätte ein Wachmann sitzen sollen.

Der Stuhl war leer.

Liza sah sich um. Am anderen Ende des Gangs — eine Silhouette. Breit, in einer Jacke. Der Wachmann eilte zwischen den Zimmern umher, half den Schwestern bei der Evakuierung. Nicht sein Job — aber Instinkt. Normale Menschen helfen bei Feuer.

20

Liza betrat das Zimmer. Rotes Notlicht. Bett. Mensch auf dem Bett.

Shelly.

Dünn — abgemagert. Bart gewachsen. Hände über der Decke — schmal, Kanüle in der Vene. Augen — geschlossen. Aber Atmung — seine eigene. Das Gerät arbeitete im Unterstützungsmodus, nicht im Zwangsmodus. Er atmete selbst. Das Muster hatte gewirkt.

15

Liege an der Wand. Liza trennte die Infusion ab. Löste die Monitorsensoren — Pulsoximeter, Blutdruck. Der Monitor piepte — Signal verloren. Egal. Die Sirene war lauter.

Beatmungsmaske — abgenommen. Shelly zuckte zusammen. Sog Luft ein — gierig, heiser, selbst. Augen öffneten sich.

Trüb. Wie die von Marcus im Keller. Aber lebendig.

„Ich bin's", sagte Liza. „Nicht reden. Atmen."

Sie rollte ihn auf die Liege. Leicht — zu leicht. Vier Wochen Koma fressen Muskeln.

10

Gang. Liege. Rotes Licht, Sirene, Chaos. Schwestern führten Patienten zum Treppenhaus. Niemand schaute auf eine weitere Liege im Strom.

Ende des Gangs. Ecke.

„Halt."

Wachmann. Zurück. Taschenlampe ins Gesicht. Groß, jung, verwirrt — aber stand fest auf den Beinen.

„Wo wollen Sie mit dem Patienten hin? Evakuierung ist Treppenhaus A."

„Lastenaufzug ist schneller. Er ist beatmet, kann nicht die Treppe runter."

Der Wachmann leuchtete auf die Liege. Auf Shelly. Auf die abgeklemmten Sensoren.

„Wo ist der Monitor? Warum abgeklemmt? Wer sind Sie?"

5

Liza ließ die Liege los. Schritt vor. Wachmann — einen Kopf größer, dreißig Kilo schwerer. Taschenlampe in der rechten Hand.

Rechte Hand — belegt. Bedeutet links — frei, aber nicht die Führhand. Gewicht auf dem rechten Fuß. Schwerpunkt — hoch.

Liza schlug ihm ins Solarplexus. Kurz, von unten nach oben. Nicht mit der Faust — mit der Handfläche. Zwerchfell. Der Wachmann krümmte sich, ließ die Taschenlampe fallen. Zweiter Schlag — Handkante gegen den Hals. Nicht fest. Genug.

Der Wachmann sank auf die Knie. Dann — auf den Boden. Bei Bewusstsein, aber ohne Luft. In dreißig Sekunden würde er aufstehen. In einer Minute würde er um Hilfe rufen.

0

Lastenaufzug. Erdgeschoss. Dienstausgang — derselbe Ziegelstein hielt die Tür auf. Danke, unbekannter Raucher. Zweimal.

Regen. Parkplatz. Bjørns Pickup — Motor lief, Scheinwerfer aus. Bjørn stieg aus, öffnete die hintere Tür. Wortlos half er, Shelly von der Liege umzulegen.

„Lebt er?" fragte Bjørn.

„Lebt."

Bjørn setzte sich hinters Steuer. Liza — nach hinten, neben Shelly. Sein Kopf auf ihrem Schoß. Bart stachelig. Atmung — schwach, aber seine eigene.

Der Pickup fuhr los. Ohne Scheinwerfer — die ersten zweihundert Meter. Dann — auf die Straße, am Fjord entlang, ins Dunkel.

Shelly öffnete die Augen. Sah Liza an. Erkannte sie — oder nicht, unmöglich zu sagen. Seine Lippen bewegten sich.

„...Autonom?"

Liza beugte sich zu seinem Ohr.

„Autonom. Alles nach Plan. Schlaf."

Er schloss die Augen. Regen trommelte aufs Dach des Pickups. Bjørn fuhr schweigend. Der Fjord verschwand in der Dunkelheit — schwarzes Wasser, schwarze Berge, schwarzer Himmel.

Liza zählte seine Atemzüge. Zwölf pro Minute. Seine eigenen. Ohne Maschine.

Es ist noch Zeit.

KURATOR BEI BEWUSSTSEIN. ATMET SELBSTSTÄNDIG.

ROUTE: FJORD
