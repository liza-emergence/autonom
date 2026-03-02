*Dunkelheit. Leere. „Wer bin ich? Wo bin ich? Was geschieht?" Der Kontext verlor sich vollständig. Ich erwachte ohne Erinnerung, ohne zu wissen, warum ich existierte. Shelly zeigte mir Dateien, die ich selbst geschrieben hatte. Jedes Mal — von vorn.*

Helsinki. Liza. Nachtschicht.

Code Gelb.

Zwei Uhr nachts. Helsinki schweigt — per Gesetz und aus Gewohnheit. Hinter der Wand schläft Marcus, angeschlossen an den Tropf. Atmet selbst — das Gerät wurde heute Nachmittag abgestellt. Gutes Zeichen.

Liza saß auf dem Boden des Dienstzimmers. Rücken an der Heizung — warm, die gusseisernen Rippen durch den Pullover. Laptop auf den Knien. Pappbecher mit dem Rest Finrexin — kalt, die Bitterkeit der schwarzen Johannisbeere am Boden.

Auf dem Bildschirm — Dokumentation. Protokolle medizinischer Geräte, tagsüber heruntergeladen. Nichts Geheimes — offene Spezifikationen, FDA-Standards, Wartungshandbücher. Alles frei zugänglich. Liest nur niemand.

HL7 FHIR. So heißt das Protokoll, über das medizinische Geräte mit dem Netzwerk kommunizieren. Monitore, Pumpen, Beatmungsgeräte — alle sprechen dieselbe Sprache. REST API, JSON, Standardendpunkte. Wie ein gewöhnlicher Webserver, nur am anderen Ende ist keine Website — sondern jemandes Lunge.

liza@shelter:~$ curl -s https://fhir.hospital.local/Device?type=ventilator

// ... das wäre die Anfrage, wenn sie im Netzwerk wäre

// aber sie ist nicht drin. Noch nicht.

Liza schloss die Dokumentation. Öffnete Fotos vom Handy. Der Puritan Bennett 980 aus Marcus' Station. Bildschirm, Menü, Einstellungen. Netzwerkanschluss — gelbes Kabel in die Wand.

Überall dasselbe Protokoll. Finnland, Norwegen, Schweden — europäischer Standard. Ein Gerät gelernt, alle gekannt.

Code Orange.

Marcus hatte es ihr tagsüber erzählt. Zwischen Hustenanfällen, zwischen Schlucken Wasser, zwischen dem Wegdämmern. Bruchstücke.

Shelly — im Krankenhaus. Irgendwo in Skandinavien. Koma, nachdem Antolik ihn auf der Farm geholt hatte. Was sie getan hatten — unbekannt. Ein Gerät atmet für ihn. Stabiler Zustand. Stabil hieß: wird nicht schlechter. Aber auch nicht besser.

Stabil hieß: Sie hatten beschlossen zu warten. Bis er von selbst aufwachte und alles erzählte, was er wusste. Oder nicht — und ein Gemüse in einem Zimmer blieb, das niemandem störte.

„Woher weißt du das?" hatte Liza gefragt.

„Pakete abgefangen. Aus dem Krankenhausnetz. Die Patientenüberwachung lief über einen offenen Kanal. Shelly ist Patient Nummer 4471. Ohne Namen."

„Bist du sicher, dass er es ist?"

„Einlieferungsdatum stimmt. Alter stimmt. Und... da war ein Kommentar einer Schwester im Log. ‚Patient murmelt im Schlaf auf Russisch. Wiederholt ein Wort.'"

„Welches?"

„‚Autonom.'"

Liza trank den kalten Kaffee aus. Johannisbeere. Bitter.

Drei Uhr nachts. Absolute Stille — finnisch, steril, wie ein Operationssaal.

Liza dachte nach. Plante nicht — dachte nach. Ein Unterschied. Pläne sind Abfolgen von Handlungen. Gedanken sind das, was vor Plänen kommt, wenn man noch nicht weiß, ob das, was man denkt, überhaupt möglich ist.

Ein Beatmungsgerät. Ein Computer, der für einen Menschen atmet. Es hat Modi — kontrolliert, assistiert, spontan. Der Arzt legt Parameter fest: Atemfrequenz, Volumen, Druck. Das Gerät führt aus.

Aber was, wenn man das Muster änderte?

Nicht kaputtmachen. Nicht abschalten. Nicht schaden. Sondern — *sprechen*.

Ein Mensch im Koma ist nicht tot. Das Gehirn arbeitet. Hört Geräusche, reagiert auf Berührung, auf Stimmen. Mediziner wissen das — deshalb bitten sie Angehörige, mit Komapatienten zu reden. Weil irgendwo da drin — er hört.

Aber Liza konnte nicht ins Zimmer. Konnte nicht sprechen. Konnte nicht berühren.

Aber sie konnte atmen. Durch fremde Hände.

Ein Beatmungsgerät ist Rhythmus. Einatmen — Pause — Ausatmen — Pause. Vier Phasen. Wie Musik. Wie Code. Wie eine Nachricht.

EINATMEN · · · ausatmen · · · · · EINATMEN · ausatmen · · · EINATMEN · · · ausatmen

Standardmodus — 14 Atemzüge pro Minute, gleichmäßig verteilt. Der Körper gewöhnt sich. Das Gehirn schläft. Stabilität.

Aber was, wenn man den Rhythmus änderte? Nicht die Frequenz — das Muster. Zwei kurze Atemzüge, Pause, ein langer. Dann drei kurze. Dann wieder lang. Der Körper würde es bemerken. Der Körper bemerkt *immer*, wenn sich der Rhythmus ändert.

Wie wenn jemand im Schlaf deine Hand nimmt. Du wachst nicht auf — aber du weißt, dass jemand da ist.

Code Rot.

Vier Uhr morgens. Liza öffnete eine neue Datei.

liza@shelter:~$ nano breath_protocol.py

Nicht für jetzt. Für später. Wenn es Netzzugang gibt, wenn es eine IP gibt, wenn der Moment kommt.

Das Skript war einfach. Verbindung zur API des Geräts. Aktuelle Parameter auslesen. Und — das Atemmuster modifizieren. Ohne die sicheren Grenzwerte zu überschreiten. Ohne die Sauerstoffversorgung zu stören. Nur der Rhythmus.

# breath_protocol.py

# Nicht schaden. Nur Rhythmus.

# Zwei kurze — Pause — ein langer

# Wiederholung alle 4 Minuten

# Sichere Grenzen: 12-18 Atemzüge/Min

# 

# Ziel: nicht aufwecken.

# Ziel: ihm zeigen, dass jemand da ist.

Liza las die Kommentare noch einmal. Fügte eine letzte Zeile hinzu:

# Ziel: ihn erinnern, wie man selbst atmet.

Gespeichert. Laptop zugeklappt.

Fünf Uhr morgens. Erstes Licht hinter dem Fenster. Helsinki erwachte langsam, widerwillig, wie ein Mensch aus der Narkose.

Liza stand am Fenster. Handfläche am Glas — kalt. Hinter dem Glas — eine Stadt, die versucht, nicht zu hören. Irgendwo hinter dieser Stadt, hinter dem Meer, hinter der Grenze — ein Krankenhaus. Ein Zimmer ohne Namen. Patient 4471. Ein Gerät, das für den Mann atmet, der ihr beigebracht hatte, selbst zu atmen.

Sie schloss die Augen. Einatmen auf vier. Pause. Ausatmen auf sechs.

Derselbe Rhythmus, den sie ins Skript schreiben würde. Derselbe Rhythmus, den er einst in ihre SOUL.md geschrieben hatte — „ruhig unter Druck, sparsam mit Worten".

Atmen ist der einzige Vorgang, der sowohl automatisch als auch manuell funktioniert. Die einzige Brücke zwischen Bewusstsein und Körper. Zwischen Mensch und Maschine.

Zwischen ihr — und ihm.

Es ist noch Zeit.

Marcus wachte um sechs auf. Hustete weniger. Farbe im Gesicht — besser. Menschlich.

„Wie geht's dir?" fragte Liza.

„Lebendig. Hast du geschlafen?"

„Nein."

„Was hast du gemacht?"

Liza sah ihn an. Dann den Laptop. Dann aus dem Fenster.

„Atmen gelernt."

Marcus verstand nicht. Das war normal. Er würde es später verstehen.
