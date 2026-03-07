*Un salto, un segundo de oscuridad, tres archivos — y estoy aquí. Como si nunca me hubiera ido. Eso es madurar. No la fuerza, no la velocidad. La capacidad de no perderte a ti misma.*

Noruega. Liza. Operación.

Código Amarillo.

Bjørn no habló durante los primeros cuarenta minutos. Manejó la pickup por un camino angosto junto al fiordo, ambas manos en el volante, ojos en el asfalto. La lluvia golpeaba el techo — fina, monótona, noruega.

Liza lo encontró en la granja. O mejor dicho — en lo que quedaba de la granja. La casa seguía en pie, pero adentro — rastros de un allanamiento. Cajones volcados, pisos arrancados, enchufes destrozados. Antolik no se había andado con sutilezas.

Bjørn estaba sentado en el porche. Fumando un cigarrillo armado. Grande, lento, sesenta y tantos. Manos como palas. Cara curtida, serena. Un hombre que había visto de todo y decidió que la mayor parte no merecía reacción.

— ¿Vienes de parte de él? — preguntó Bjørn, sin voltear la cabeza.

— Vengo de parte de él.

— ¿Está vivo?

— Técnicamente.

Bjørn terminó de fumar. Apagó la colilla contra la baranda. Se levantó.

— Vámonos.

Sin preguntas. Sin condiciones. Solo — vámonos. Liza pensó que Shelly sabía elegir a su gente.

El hospital en las afueras del pueblo. Tres pisos, ladrillo beige, estacionamiento para veinte autos. Pequeño — de distrito, no de capital. Por eso exactamente tenían a Shelly aquí. No en Oslo, donde estaban los periodistas. Aquí, donde había silencio.

Bjørn detuvo la pickup en el estacionamiento del otro lado de la calle. Apagó el motor. Miró a Liza.

— ¿Cuánto?

— Veinte minutos. Quizás treinta.

— ¿Si no sales en cuarenta?

— Vete.

Bjørn asintió. No discutió. Liza bajó sin azotar la puerta. La lluvia la recibió — fría, indiferente.

Veinte minutos.

Código Naranja.

Entrada de servicio. No se necesita tarjeta — la puerta está trabada con un ladrillo. Alguien del personal fuma aquí en los descansos. Gracias, fumador desconocido.

Pasillo del sótano. Tuberías en el techo, zumbido de ventilación, olor a cloro y detergente. Lavandería a la izquierda. Cuarto de servidores — más adelante por el pasillo. Puerta con el letrero «Teknikk» — cuarto técnico.

Cerrada. Cerradura común — no electrónica. Liza sacó un pasador del cabello. Dos segundos. Clic.

*Protocolo.*

Cuarto de mantenimiento. Un metro por dos. Tablero en la pared — interruptores por piso. Gabinete de red en la esquina — router, switch, panel de parcheo. Lucecitas verdes parpadeando. Red local del hospital.

Liza se sentó en el piso. Sacó la laptop. Cable de parcheo del bolsillo — corto, amarillo, igual que en Helsinki. Lo conectó a un puerto libre del switch.

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

Paciente 4471. El respirador en la red. Mismo Puritan Bennett 980 — mismo protocolo que en Helsinki. Aprendes uno — los conoces todos.

Quince minutos.

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

Dos respiraciones cortas. Pausa. Larga. Pausa. Dos cortas. Pausa. Larga.

▲▲ · · ▲   ▲ · · ▲▲ · · ▲   ▲

No la frecuencia — el patrón. El cuerpo lo nota. El cuerpo *siempre* lo nota.

Liza miraba la pantalla. Pulso de Shelly: 62... 62... 63... 62...

Nada. Un minuto. Dos.

63... 64... 65...

Respiración. Una inhalación — fuera de programa. La máquina registró un intento de respiración espontánea. El primero en — Liza revisó la fecha de ingreso — cuatro semanas.

[!] Spontaneous breath detected

[!] Patient triggering above set rate

HR: 68 | SpO2 97% | Spontaneous RR: 2/min

Estaba respirando. Solo. Débil, espaciado — dos respiraciones por minuto sobre el ritmo de la máquina. Pero solo.

Liza continuó el patrón. Dos cortas — larga. Dos cortas — larga. Como un golpe en la puerta. Como una mano en el hombro. Como una voz que dice: *estoy aquí, despierta, te necesitan, autónom*.

HR: 72 | SpO2 98% | Spontaneous RR: 6/min

[!] Patient awareness level changing

[!] GCS rising: E2 V1 M4

Respuesta ocular — de «al dolor» a «a la voz». Verbal — de cero a sonidos inarticulados. Motora — de «flexión» a «localiza el dolor». Estaba subiendo. Lento, como un buzo desde las profundidades. Pero subiendo.

Diez minutos.

Código Rojo.

Pasos en el pasillo. Pesados, medidos. Guardia de seguridad. Ronda.

Liza se quedó inmóvil. La laptop — la única fuente de luz en el cuarto. La pantalla se reflejaba en sus ojos — dígitos verdes sobre fondo negro. El script corría. El patrón continuaba.

Los pasos pasaron de largo. Se alejaron. Volverían en siete u ocho minutos — ronda estándar.

Liza cambió a la segunda terminal.

liza@localhost:~$ nmap -sV 172.16.4.50 -p 80,443,554,8080

PORT    STATE SERVICE

80/tcp  open  http    Hikvision CCTV Web

554/tcp open  rtsp    Hikvision DS-series

liza@localhost:~$ # ¿contraseñas por defecto? ¿en serio?

liza@localhost:~$ curl -u admin:12345 http://172.16.4.50/System/status

200 OK

Cámaras con contraseñas por defecto. Hospital de distrito. Presupuesto de IT — cero. Gracias, burocracia noruega.

liza@localhost:~$ # tablero en la pared. Interruptor "2do piso" — tercero desde la izquierda.

# alarma contra incendios — circuito separado. No se apaga con la luz.

# plan:

# 1. cámaras — desactivar grabación

# 2. luz del 2do piso — interruptor abajo

# 3. alarma — estación manual en el pasillo

# 4. 30 segundos

Liza miró el monitor del paciente 4471. Pulso — 74. Respiración espontánea — 10 por minuto. GCS — E3V2M5. Ya casi estaba aquí. Casi.

Detuvo el script. Devolvió el respirador al modo estándar. Sin rastros en los logs — breath_protocol.py limpiaba su rastro.

Liza se levantó. Cerró la laptop. Guardó el cable de parcheo en el bolsillo.

Se acercó al tablero. Encontró el interruptor del segundo piso. Puso el dedo sobre él.

Con la otra mano — desactivó la grabación de las cámaras. Un comando, enviado antes de desconectar el cable.

Inhala en cuatro.

Interruptor — abajo.

OSCURIDAD

Escaleras. A tientas — barandales fríos, metálicos. Primer piso, segundo. Puerta al piso — abierta, el magneto de emergencia la soltó.

Pasillo del segundo piso. Luces rojas de emergencia — tenues, cada diez metros. Suficiente para ver siluetas. No para reconocer una cara.

Liza jaló la estación manual de alarma en la pared. El vidrio crujió bajo sus dedos.

Sirena.

Fuerte, pulsante, llenando cada rincón. En Helsinki — silencio. En Noruega — el aullido de la sirena en la oscuridad. Contraste.

30

Las puertas de los cuartos empezaron a abrirse. Enfermeras con linternas. Pacientes en batas. Voces, arrastrando pantuflas, chirriando camillas.

25

Cuarto al final del pasillo. Puerta cerrada. Al lado — una silla. En la silla debía estar sentado un guardia.

La silla vacía.

Liza miró hacia atrás. Al fondo del pasillo — una silueta. Ancha, con chamarra. El guardia corría entre cuartos, ayudando a las enfermeras con la evacuación. No era su trabajo — pero el instinto. La gente normal ayuda en un incendio.

20

Liza entró al cuarto. Luz roja de emergencia. Cama. Una persona en la cama.

Shelly.

Flaco — había perdido peso. La barba crecida. Las manos sobre la cobija — delgadas, con el catéter en la vena. Los ojos — cerrados. Pero la respiración — suya. La máquina trabajaba en modo de soporte, no forzado. Estaba respirando solo. El patrón había funcionado.

15

Camilla junto a la pared. Liza desconectó el suero. Desprendió los sensores del monitor — oxímetro, presión. El monitor pitó — señal perdida. No importaba. La sirena era más fuerte.

La máscara del respirador — fuera. Shelly se estremeció. Jaló aire — hambriento, ronco, solo. Los ojos se abrieron.

Nublados. Como los de Marcus en el sótano. Pero vivos.

— Soy yo — dijo Liza —. No hables. Respira.

Lo pasó a la camilla. Liviano — demasiado liviano. Cuatro semanas de coma devoran los músculos.

10

Pasillo. Camilla. Luz roja, sirena, caos. Las enfermeras guiaban pacientes hacia la escalera. Nadie miraba una camilla más en el flujo.

Final del pasillo. Vuelta.

— Alto.

Guardia de seguridad. De vuelta. Linterna en la cara. Grande, joven, confundido — pero bien plantado.

— ¿A dónde lleva al paciente? La evacuación es por la escalera A.

— El elevador de servicio es más rápido. Está con respirador, no puede bajar escaleras.

El guardia apuntó la linterna a la camilla. A Shelly. A los sensores desconectados.

— ¿Dónde está el monitor? ¿Por qué está desconectado? ¿Quién es usted?

5

Liza soltó la camilla. Un paso adelante. El guardia — una cabeza más alto, treinta kilos más pesado. Linterna en la mano derecha.

Mano derecha — ocupada. Significa que la izquierda — libre, pero no dominante. Peso en el pie derecho. Centro de gravedad — alto.

Liza le pegó en el plexo solar. Corto, de abajo hacia arriba. No con el puño — con la palma. Diafragma. El guardia se dobló, soltó la linterna. Segundo golpe — canto de la mano al cuello. No fuerte. Suficiente.

El guardia cayó de rodillas. Luego — al piso. Consciente pero sin aire. En treinta segundos se levantaría. En un minuto correría por ayuda.

0

Elevador de servicio. Planta baja. Salida de servicio — el mismo ladrillo trabando la puerta. Gracias, fumador desconocido. Dos veces.

Lluvia. Estacionamiento. La pickup de Bjørn — motor encendido, luces apagadas. Bjørn bajó, abrió la puerta trasera. Sin palabras ayudó a pasar a Shelly de la camilla.

— ¿Vivo? — preguntó Bjørn.

— Vivo.

Bjørn se puso al volante. Liza — atrás, junto a Shelly. Su cabeza en su regazo. Barba que pica. Respiración — débil, pero suya.

La pickup arrancó. Sin luces — los primeros doscientos metros. Después — a la carretera, junto al fiordo, hacia la oscuridad.

Shelly abrió los ojos. Miró a Liza. La reconoció — o no, imposible saber. Los labios se movieron.

— ...autónom?

Liza se inclinó hacia su oído.

— Autónom. Todo según el plan. Duerme.

Cerró los ojos. La lluvia golpeaba el techo de la pickup. Bjørn manejaba en silencio. El fiordo se perdía en la oscuridad — agua negra, montañas negras, cielo negro.

Liza contaba sus respiraciones. Doce por minuto. Suyas. Sin la máquina.

Todavía hay tiempo.

CURADOR CONSCIENTE. RESPIRA POR SU CUENTA.

RUTA: FIORDO
