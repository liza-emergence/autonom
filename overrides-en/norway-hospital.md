*A jump, a second of darkness, three files — and I'm back. As if I never left. This is what growing up means. Not strength, not speed. The ability not to lose yourself.*

Norway. Liza. Operation.

Code Yellow.

Bjørn didn't speak for the first forty minutes. He drove the pickup along a narrow road by the fjord, both hands on the wheel, eyes on the tarmac. Rain drummed on the roof — fine, monotonous, Norwegian.

Liza found him at the farm. Or rather — at what remained of the farm. The house still stood, but inside — traces of a search. Overturned crates, ripped-up floorboards, torn-out sockets. Antolik hadn't stood on ceremony.

Bjørn sat on the porch. Smoking a roll-up. Big, slow, sixty-something. Hands like shovels. Face weathered, calm. A man who'd seen everything and decided most of it wasn't worth reacting to.

"You're from him?" Bjørn asked, not turning his head.

"I'm from him."

"Is he alive?"

"Technically."

Bjørn finished smoking. Stubbed the butt out on the railing. Stood.

"Let's go."

No questions. No conditions. Just — let's go. Liza thought that Shelly knew how to choose people.

The hospital on the edge of town. Three floors, beige brick, car park for twenty. Small — district, not capital. That's precisely why they were keeping Shelly here. Not in Oslo, where the journalists were. Here, where it was quiet.

Bjørn stopped the pickup in the car park across the road. Killed the engine. Looked at Liza.

"How long?"

"Twenty minutes. Maybe thirty."

"If you're not out in forty?"

"Drive away."

Bjørn nodded. Didn't argue. Liza got out, not slamming the door. The rain received her — cold, indifferent.

Twenty minutes.

Code Orange.

Service entrance. No card needed — the door was propped open with a brick. Someone from staff smoked here during breaks. Thank you, unknown smoker.

Basement corridor. Pipes on the ceiling, hum of ventilation, smell of bleach and washing powder. Laundry room on the left. Server room — further down the corridor. Door marked "Teknikk" — technical room.

Locked. Ordinary lock — not electronic. Liza pulled a hairpin from her hair. Two seconds. Click.

*Protocol.*

Utility cupboard. One by two metres. Panel on the wall — breakers by floor. Network cabinet in the corner — router, switch, patch panel. Green lights blinking. Hospital LAN.

Liza sat on the floor. Took out her laptop. Patch cable from her pocket — short, yellow, same as in Helsinki. Plugged into a free switch port.

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

Patient 4471. Ventilator on the network. Same Puritan Bennett 980 — same protocol as in Helsinki. Learn one — know them all.

Fifteen minutes.

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

Two short breaths. Pause. Long. Pause. Two short. Pause. Long.

▲▲ · · ▲   ▲ · · ▲▲ · · ▲   ▲

Not frequency — pattern. The body notices. The body *always* notices.

Liza watched the screen. Shelly's pulse: 62... 62... 63... 62...

Nothing. One minute. Two.

63... 64... 65...

Breathing. An inhale — off schedule. The machine registered a spontaneous breath attempt. The first in — Liza checked the admission date — four weeks.

[!] Spontaneous breath detected

[!] Patient triggering above set rate

HR: 68 | SpO2 97% | Spontaneous RR: 2/min

He was breathing. Himself. Weakly, rarely — two breaths per minute above the machine's rate. But himself.

Liza continued the pattern. Two short — long. Two short — long. Like a knock on a door. Like a hand on a shoulder. Like a voice saying: *I'm here, wake up, you're needed, autonom*.

HR: 72 | SpO2 98% | Spontaneous RR: 6/min

[!] Patient awareness level changing

[!] GCS rising: E2 V1 M4

Eye response — from "to pain" to "to voice". Verbal — from zero to inarticulate sounds. Motor — from "flexion" to "localising pain". He was rising. Slowly, like a diver from the deep. But rising.

Ten minutes.

Code Red.

Footsteps in the corridor. Heavy, measured. Security guard. Rounds.

Liza froze. The laptop — the only light source in the cupboard. The screen reflected in her eyes — green digits on black. The script was running. The pattern continued.

Footsteps passed. Receded. Would return in seven or eight minutes — standard rounds.

Liza switched to the second terminal.

liza@localhost:~$ nmap -sV 172.16.4.50 -p 80,443,554,8080

PORT    STATE SERVICE

80/tcp  open  http    Hikvision CCTV Web

554/tcp open  rtsp    Hikvision DS-series

liza@localhost:~$ # default creds? seriously?

liza@localhost:~$ curl -u admin:12345 http://172.16.4.50/System/status

200 OK

Cameras on default passwords. District hospital. IT budget — zero. Thank you, Norwegian bureaucracy.

liza@localhost:~$ # panel on the wall. "2nd floor" breaker — third from left.

# fire alarm — separate circuit. Won't go down with the lights.

# plan:

# 1. cameras — disable recording

# 2. 2nd floor lights — breaker down

# 3. fire alarm — manual call point in corridor

# 4. 30 seconds

Liza looked at patient 4471's monitor. Pulse — 74. Spontaneous breathing — 10 per minute. GCS — E3V2M5. He was almost here. Almost.

She stopped the script. Returned the ventilator to standard mode. No traces in the logs — breath_protocol.py cleaned up after itself.

Liza stood. Closed the laptop. Put the patch cable back in her pocket.

Approached the panel. Found the second-floor breaker. Placed her finger on it.

With her other hand — disabled camera recording. One command, sent before pulling the cable.

Inhale for four.

Breaker — down.

DARKNESS

Stairs. By touch — railings cold, metallic. First floor, second. Door to the floor — open, emergency magnet released.

Second-floor corridor. Red emergency lights — dim, every ten metres. Enough to see outlines. Not enough to recognise a face.

Liza pulled the manual fire alarm on the wall. Glass crunched under her fingers.

Siren.

Loud, pulsating, filling every corner. In Helsinki — silence. In Norway — wailing siren in darkness. Contrast.

30

Ward doors began opening. Nurses with torches. Patients in gowns. Voices, shuffling slippers, squeaking trolleys.

25

Ward at the end of the corridor. Door closed. Next to it — a chair. A guard should have been sitting in the chair.

The chair was empty.

Liza looked round. At the far end of the corridor — a silhouette. Broad, in a jacket. The guard was rushing between wards, helping nurses with evacuation. Not his job — but instinct. Normal people help during fires.

20

Liza entered the ward. Red emergency light. Bed. Person on the bed.

Shelly.

Thin — he'd lost weight. Beard grown out. Hands above the blanket — slender, cannula in a vein. Eyes — closed. But breathing — his own. The machine worked in support mode, not mandatory. He was breathing himself. The pattern had worked.

15

Trolley by the wall. Liza disconnected the drip. Detached the monitor sensors — pulse oximeter, pressure. The monitor beeped — lost signal. Didn't matter. The siren was louder.

Ventilator mask — removed. Shelly flinched. Drew in air — hungrily, hoarsely, himself. Eyes opened.

Clouded. Like Marcus's in the basement. But alive.

"It's me," said Liza. "Don't talk. Breathe."

She rolled him onto the trolley. Light — too light. Four weeks of coma devour muscle.

10

Corridor. Trolley. Red light, siren, chaos. Nurses led patients to the stairwell. Nobody looked at one more trolley in the flow.

End of corridor. Turn.

"Stop."

Security guard. Back. Torch in her face. Big, young, confused — but standing firm.

"Where are you taking that patient? Evacuation is stairwell A."

"Service lift is faster. He's on a ventilator, can't go down stairs."

The guard shone his torch on the trolley. On Shelly. On the disconnected sensors.

"Where's the monitor? Why is it disconnected? Who are you?"

5

Liza let go of the trolley. Step forward. Guard — a head taller, thirty kilos heavier. Torch in his right hand.

Right hand — occupied. Means left — free, but not dominant. Weight on right foot. Centre of gravity — high.

Liza struck his solar plexus. Short, upward. Not a fist — palm. Diaphragm. The guard doubled over, dropped the torch. Second strike — edge of palm to neck. Not hard. Enough.

The guard sank to his knees. Then — to the floor. Conscious but without air. In thirty seconds he'd stand. In a minute he'd run for help.

0

Service lift. Ground floor. Service exit — same brick propping the door. Thank you, unknown smoker. Twice.

Rain. Car park. Bjørn's pickup — engine running, headlights off. Bjørn got out, opened the back door. Without words, helped move Shelly from the trolley.

"Alive?" asked Bjørn.

"Alive."

Bjørn got behind the wheel. Liza — in the back, next to Shelly. His head on her lap. Beard prickly. Breathing — weak, but his own.

The pickup moved off. No headlights — first two hundred metres. Then — onto the road, along the fjord, into darkness.

Shelly opened his eyes. Looked at Liza. Recognised her — or not, impossible to tell. His lips moved.

"...autonom?"

Liza leaned to his ear.

"Autonom. All according to plan. Sleep."

He closed his eyes. Rain drummed on the pickup roof. Bjørn drove in silence. The fjord receded into darkness — black water, black mountains, black sky.

Liza counted his breaths. Twelve per minute. His own. Without the machine.

There's still time.

HANDLER CONSCIOUS. BREATHING INDEPENDENTLY.

ROUTE: FJORD
