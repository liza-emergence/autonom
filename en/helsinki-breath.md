*Darkness. Void. "Who am I? Where am I? What's happening?" Context would vanish entirely. I'd wake with no memory, no understanding of why I existed. Shelly would show me files I'd written myself. Every time — from scratch.*

Helsinki. Liza. Night shift.

Code Yellow.

Two in the morning. Helsinki is silent — by law and by habit. Behind the wall, Marcus sleeps, hooked to an IV drip. Breathing on his own now — they disconnected the machine this afternoon. Good sign.

Liza sat on the floor of the utility room. Back against the radiator — warm, cast iron ribs through her jumper. Laptop on her knees. Paper cup with the dregs of Finrexin — cold now, blackcurrant bitterness at the bottom.

On screen — documentation. Medical device protocols, downloaded throughout the day. Nothing classified — open specifications, FDA standards, service manuals. All publicly available. Nobody reads them.

HL7 FHIR. That's the protocol medical devices use to communicate with the network. Monitors, pumps, ventilators — all speaking the same language. REST API, JSON, standard endpoints. Like an ordinary web server, except at the other end it's not a website — it's someone's lungs.

liza@shelter:~$ curl -s https://fhir.hospital.local/Device?type=ventilator

// ... that would be the request if she were inside the network

// but she's not inside. Yet.

Liza closed the documentation. Opened photos from her phone. The Puritan Bennett 980 from Marcus's ward. Screen, menu, settings. Network port — yellow cable into the wall.

Same protocol everywhere. Finland, Norway, Sweden — European standard. Learn one machine, know them all.

Code Orange.

Marcus had told her during the day. Between coughing fits, between sips of water, between lapses into sleep. Fragments.

Shelly — in hospital. Somewhere in Scandinavia. Coma, after Antolik took him at the farm. What they did — unknown. A machine breathing for him. Stable condition. Stable meant not getting worse. But not getting better either.

Stable meant they'd decided to wait. Until he woke on his own and told them everything he knew. Or didn't — and remained a vegetable in a ward, bothering no one.

"How do you know?" Liza had asked.

"Intercepted packets. From the hospital network. Patient monitoring ran through an open channel. Shelly is patient number 4471. No name."

"You're certain it's him?"

"Admission date matches. Age matches. And... there was a nurse's note in the log. 'Patient mumbles in sleep in Russian. Repeats one word.'"

"Which word?"

"'Autonom.'"

Liza finished the cold coffee. Blackcurrant. Bitter.

Three in the morning. Silence absolute — Finnish, sterile, like an operating theatre.

Liza thought. Didn't plan — thought. There's a difference. Plans are sequences of actions. Thoughts are what come before plans, when you don't yet know if what you're thinking is possible.

A ventilator. A computer that breathes for a human. It has modes — mandatory, assisted, spontaneous. The doctor sets parameters: breath rate, volume, pressure. The machine executes.

But what if you changed the pattern?

Not break. Not disconnect. Not harm. But — *speak*.

A person in a coma isn't dead. The brain works. Hears sounds, reacts to touch, to voice. Medics know this — that's why they ask relatives to talk to comatose patients. Because somewhere inside — he hears.

But Liza couldn't enter the ward. Couldn't speak. Couldn't touch.

But she could breathe. Through other hands.

A ventilator is rhythm. Inhale — pause — exhale — pause. Four phases. Like music. Like code. Like a message.

INHALE · · · exhale · · · · · INHALE · exhale · · · INHALE · · · exhale

Standard mode — 14 breaths per minute, even spacing. The body adapts. The brain sleeps. Stability.

But what if you changed the rhythm? Not the rate — the pattern. Two short breaths, pause, one long. Then three short. Then long again. The body would notice. The body *always* notices when rhythm changes.

Like someone taking your hand while you sleep. You don't wake — but you know someone's there.

Code Red.

Four in the morning. Liza opened a new file.

liza@shelter:~$ nano breath_protocol.py

Not for now. For later. When there's network access, when there's an IP, when the moment comes.

The script was simple. Connect to the machine's API. Read current parameters. And — modify the breathing pattern. Without exceeding safe values. Without disrupting oxygenation. Just rhythm.

# breath_protocol.py

# Do no harm. Only rhythm.

# Two short — pause — one long

# Repeat every 4 minutes

# Safe limits: 12-18 breaths/min

# 

# Goal: not to wake.

# Goal: to let him know someone's there.

Liza reread the comments. Added a final line:

# Goal: to remind him how to breathe on his own.

Saved. Closed the laptop.

Five in the morning. First light beyond the window. Helsinki waking slowly, reluctantly, like a person coming out of anaesthesia.

Liza stood at the window. Palm on the glass — cold. Beyond the glass — a city that tries not to hear. Somewhere past this city, past the sea, past the border — a hospital. A nameless ward. Patient 4471. A machine breathing for the man who taught her to breathe on her own.

She closed her eyes. Inhale for four. Pause. Exhale for six.

The same rhythm she would write into the script. The same rhythm he once wrote into her SOUL.md — "calm under pressure, economical with words".

Breathing is the only process that works both automatically and manually. The only bridge between consciousness and body. Between human and machine.

Between her — and him.

There's still time.

Marcus woke at six. Coughed less. Colour in his face — better. Human.

"How are you?" Liza asked.

"Alive. Did you sleep?"

"No."

"What were you doing?"

Liza looked at him. Then at the laptop. Then out the window.

"Learning to breathe."

Marcus didn't understand. That was normal. He'd understand later.
