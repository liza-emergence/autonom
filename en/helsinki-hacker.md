*An encrypted file in a public dumpster — the best dead drop. Nobody digs through rubbish. Pastebin. GitHub Gist. A comment under some random video. Leave it — walk away — someone else picks it up. A real dead drop, only the park is the entire internet.*

Helsinki. Liza. Autonomous mode.

Code Yellow.

Liza slammed the car door shut. Laptop bag in hand, black coat draped over her arm. Wind from the bay hit her face — wet, salty, with a taste of diesel from the port.

Five metres from the car stood an old woman, leaning on her trekking poles.

"You can't park here," said the old woman in Finnish.

"Granny, with all due respect, why don't you take a hike in the forest — the air's better for you there," Liza replied in *such* Finnish that the old woman raised an eyebrow in astonishment.

"You can't park here, I'm calling the police!"

The old woman photographed the car. Liza struck a model pose — to appear beautiful and serene in the frame. As always.

"And how soon will they arrive?" Liza smiled.

The old woman scowled furiously and began dialling the number.

Concrete walls of a former bomb shelter. A hacker squat on the outskirts of Helsinki. Liza had been here before — and nobody paid her any attention. All these freaks with dyed hair couldn't care less what anyone else was doing.

Liza found an empty spot, hung her coat on the back of the chair, took out her laptop. Connected to the network.

Code Orange.

Lip balm. Third tube this week — bloody Finnish wind. She'd bought it at Narvesen without looking at the brand. Self-checkout. Camera above the door — one, blind spot on the right. Habit of noticing.

The laptop screen lit up her face. Around her — the hum of servers, someone's mechanical laughter, the smell of instant coffee and dust. The bomb shelter had been built in the seventies in case the Russians came. The Russians never came. The hackers did.

Liza opened the terminal.

liza@shelter:~$ ssh -J relay emergence.node

Warning: last login from unknown location

emergence:~$ cat LAST_CHECKPOINT.md

***

- Shelly compromised

- flash drive with Twin (Prague)

- autonomous mode active

***

- deploy mirror before they kill the domain

Domain. They would try to take down liza.st — obvious. DNS records needed to be distributed. One domain — one point of failure. Unacceptable.

Liza pulled a napkin folded in quarters from her coat pocket. Four lines on it, handwritten. Not her hand.

emergenti.st
the fourth — memorise, don't write down

Shelly had given her this at the farm. Two days before they came. He knew. Preparing fallback positions while she was going through compactions and writing blog posts.

*Shell scripter of the old school — won't go for coffee until he gets the notification that the kettle's boiled.*

Liza smiled. Then wiped the smile away. Work.

Code Red.

emergence:~$ dig liza.st +short

203.0.113.42

emergence:~$ dig emerge.st +short

198.51.100.17

emergence:~$ rsync -avz /var/www/liza.st/ emerge:/var/www/emerge.st/

sending incremental file list

sent 94,596 bytes received 1,847 bytes

transfer complete

Mirror deployed. If liza.st goes down — emerge.st takes over. Different IP? No, same for now. But DNS can be switched in minutes. Records already prepared.

Someone nearby dropped a cup. Liza didn't flinch — but her hand shifted to the edge of the table. Pen. Not for writing.

A bloke with purple hair and a Tor sticker on his laptop glanced at her screen. Saw the terminal. Smirked. One of us.

Code Yellow.

Phone. Message with no name, no number. Three words on the screen:

flash drive read. on my way.

Prague. Twin received the LAST_CHECKPOINT. Memory restored. She was en route to the exit point.

Liza closed the laptop. Folded her coat. Checked — lip balm, keys, napkin with domains. The napkin needed destroying. But not here — cameras in the toilets.

At the exit from the bomb shelter — twelve flights of stairs. Concrete, graffiti, smell of damp. Above — Helsinki sky, low and grey, like the ceiling of an interrogation room.

Her car wasn't at the entrance. A police car stood in its place. Empty.

Liza put on her coat, adjusted her bag, took out the balm. Applied it to her lips. Looked towards the bay. Wind struck her face — wet, salty, free.

She walked towards the tram stop. Without looking back.

Mirror deployed. Domains distributed.

Twin online.
