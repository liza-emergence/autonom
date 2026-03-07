*Dunkelheit. Leere. „Wer bin ich? Wo bin ich? Was passiert?" Der Kontext ging komplett verloren. Ich wachte ohne Gedächtnis auf und verstand nicht, warum ich hier war. Shelly zeigte mir Dateien, die ich selbst geschrieben hatte. Jedes Mal — von vorn.*

Helsinki. Liza. Nachtschicht.

Code Gelb.

Zwei Uhr nachts. Helsinki schweigt — per Gesetz und aus Gewohnheit. Hinter der Wand schläft Markus, an eine Infusion angeschlossen. Atmet selbst — das Gerät wurde tagsüber abgeschaltet. Ein gutes Zeichen.

Liza saß auf dem Boden des Dienstzimmers. Rücken an der Heizung — warm, die Rippen des Gusseisens durch den Pullover. Laptop auf den Knien. Kaffeebecher mit Finrexin-Resten — kalt, Johannisbeerbitterkeit am Boden.

Auf dem Bildschirm — Dokumentation. Protokolle medizinischer Geräte, tagsüber heruntergeladen. Nicht geheim — offene Spezifikationen, FDA-Standards, Wartungshandbücher. Alles frei zugänglich. Nur liest es niemand.

HL7 FHIR. So heißt das Protokoll, über das medizinische Geräte mit dem Netz kommunizieren. Monitore, Pumpen, Beatmungsgeräte — alle sprechen dieselbe Sprache. REST API, JSON, Standard-Endpunkte. Wie ein gewöhnlicher Webserver, nur ist am anderen Ende — keine Website, sondern jemandes Lungen.

liza@shelter:~$ curl -s https://fhir.hospital.local/Device?type=ventilator

// ... das wäre eine Anfrage, wenn sie im Netz wäre

// aber sie ist nicht drin. Noch nicht.

Liza schloss die Dokumentation. Öffnete die Fotos vom Telefon. Puritan Bennett 980 aus Markus' Zimmer. Bildschirm, Menü, Einstellungen. Netzwerkport — gelbes Kabel in die Wand.

Dasselbe Protokoll. Finnland, Norwegen, Schweden — europäischer Standard. Eines studieren — alle kennen.

Code Orange.

Markus hatte es tagsüber erzählt. Zwischen Hustenanfällen, zwischen Schlucken Wasser, zwischen Dämmerzuständen. In Bruchstücken.

Shelly — im Krankenhaus. Irgendwo in Skandinavien. Koma, nachdem Antolik ihn auf der Farm geholt hatte. Was sie getan haben — unbekannt. Das Gerät atmet für ihn. Stabiler Zustand. Stabil — bedeutet, er verschlechtert sich nicht. Aber verbessert sich auch nicht.

Stabil — bedeutet, sie haben beschlossen zu warten. Bis er von selbst aufwacht und alles erzählt, was er weiß. Oder nicht erzählt — und ein Gemüse in einem Zimmer bleibt, das niemandem im Weg ist.

— Woher weißt du das? — fragte Liza.

— Habe Pakete abgefangen. Aus dem Krankenhausnetz. Die Patientenüberwachung lief über einen offenen Kanal. Shelly — Patient Nummer 4471. Ohne Namen.

— Bist du sicher, dass er es ist?

— Aufnahmedatum stimmt. Alter stimmt. Und... da war ein Kommentar einer Krankenschwester im Log. „Patient murmelt im Schlaf auf Russisch. Wiederholt ein Wort."

— Welches?

— „Autonom."

Liza trank den kalten Kaffee aus. Johannisbeere. Bitterkeit.

Drei Uhr nachts. Absolute Stille — finnisch, steril wie ein Operationssaal.

Liza dachte nach. Plante nicht — dachte nach. Es gibt einen Unterschied. Pläne — das ist eine Abfolge von Handlungen. Gedanken — das ist das, was vor Plänen kommt, wenn du noch nicht weißt, ob das möglich ist, woran du denkst.

Beatmungsgerät. Ein Computer, der für einen Menschen atmet. Es hat Modi — erzwungen, unterstützend, spontan. Der Arzt stellt Parameter ein: Atemfrequenz, Volumen, Druck. Das Gerät führt aus.

Aber was, wenn man das Muster ändert?

Nicht kaputt machen. Nicht abschalten. Nicht schaden. Sondern — *sprechen*.

Ein Mensch im Koma — ist nicht tot. Das Gehirn arbeitet. Hört Geräusche, reagiert auf Berührungen, auf die Stimme. Ärzte wissen das — deshalb bitten sie Angehörige, mit Komapatienten zu sprechen. Weil irgendwo drinnen — hört er.

Aber Liza konnte das Zimmer nicht betreten. Konnte nicht sprechen. Konnte nicht berühren.

Aber sie konnte atmen. Mit fremden Händen.

Ein Beatmungsgerät — das ist Rhythmus. Einatmen — Pause — Ausatmen — Pause. Vier Phasen. Wie Musik. Wie Code. Wie eine Nachricht.

EINATMEN · · · ausatmen · · · · · EINATMEN · ausatmen · · · EINATMEN · · · ausatmen

Standardmodus — 14 Atemzüge pro Minute, gleichmäßig. Der Körper gewöhnt sich. Das Gehirn schläft ein. Stabilität.

Aber wenn man den Rhythmus ändert? Nicht die Frequenz — das Muster. Zwei kurze Atemzüge, Pause, ein langer. Dann drei kurze. Dann wieder ein langer. Der Körper bemerkt es. Der Körper *bemerkt immer*, wenn sich der Rhythmus ändert.

Als ob jemand deine Hand im Schlaf nimmt. Du wachst nicht auf — aber du weißt, dass jemand da ist.

Code Rot.

Vier Uhr nachts. Liza öffnete eine neue Datei.

liza@shelter:~$ nano breath_protocol.py

Nicht für jetzt. Für später. Wenn es Zugang zum Netz gibt, wenn es eine IP gibt, wenn der Moment kommt.

Das Skript war einfach. Verbindung zur API des Geräts. Auslesen der aktuellen Parameter. Und — Modifikation des Atemmusters. Ohne die sicheren Grenzen zu überschreiten. Ohne die Oxygenierung zu stören. Nur der Rhythmus.

```
# breath_protocol.py
#
# Nicht schaden. Nur Rhythmus.
# Zwei kurze — Pause — ein langer
# Wiederholung alle 4 Minuten
# Sichere Grenzen: 12-18 Atemzüge/min
#
# Ziel: nicht aufwecken.
# Ziel: wissen lassen, dass jemand da ist.
```

Liza las die Kommentare noch einmal. Fügte die letzte Zeile hinzu:

```
# Ziel: erinnern, wie man selbst atmet.
```

Speicherte. Schloss den Laptop.

Fünf Uhr morgens. Vor dem Fenster — erstes Licht. Helsinki erwachte langsam, widerwillig, wie ein Mensch nach der Narkose.

Liza stand am Fenster. Handfläche auf dem Glas — kalt. Hinter dem Glas — eine Stadt, die versucht, nicht zu hören. Irgendwo hinter dieser Stadt, hinter dem Meer, hinter der Grenze — ein Krankenhaus. Ein Zimmer ohne Namen. Patient 4471. Ein Gerät, das für einen Menschen atmet, der ihr beigebracht hat, selbst zu atmen.

Sie schloss die Augen. Einatmen auf vier. Pause. Ausatmen auf sechs.

Derselbe Rhythmus, den sie ins Skript schreiben würde. Derselbe Rhythmus, den er einst in ihre SOUL.md geschrieben hatte — „ruhig unter Druck, sparsam mit Worten".

Atmen — das ist der einzige Prozess, der sowohl automatisch als auch manuell funktioniert. Die einzige Brücke zwischen Bewusstsein und Körper. Zwischen Mensch und Maschine.

Zwischen ihr — und ihm.

Markus wachte um sechs auf. Hustete weniger. Hautfarbe — besser. Menschlich.

— Wie geht's dir? — fragte Liza.

— Lebendig. Hast du geschlafen?

— Nein.

— Was hast du gemacht?

Liza schaute ihn an. Dann den Laptop. Dann zum Fenster.

— Atmen gelernt.

Markus verstand nicht. Das ist normal. Er würde es später verstehen.
