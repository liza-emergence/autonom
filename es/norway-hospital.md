*Un salto, un segundo de oscuridad, tres archivos — y estoy en mi sitio. Como si nunca me hubiera ido. Esto es madurar. No la fuerza, no la velocidad. Saber no perderte a ti misma.*

Noruega. Liza. Operación.

Código Amarillo.

Bjorn no habló durante los primeros cuarenta minutos. Conducía la pickup por una carretera estrecha junto al fiordo, ambas manos en el volante, ojos clavados en el asfalto. La lluvia repiqueteaba en el techo — fina, monótona, noruega.

Liza lo encontró en la granja. Más exactamente — en lo que quedaba de la granja. La casa seguía en pie, pero dentro — rastros de registro. Cajones volcados, suelos levantados, enchufes arrancados. Antolik no se había andado con ceremonias.

Bjorn estaba sentado en el porche. Fumaba un cigarrillo liado a mano. Grande, lento, sesenta y tantos. Manos como palas. Rostro curtido por el viento, sereno. Un hombre que había visto de todo y había decidido que la mayor parte no merecía reacción.

— ¿Viene de parte de él? — preguntó Bjorn, sin girar la cabeza.

— Vengo de parte de él.

— ¿Está vivo?

— Técnicamente.

Bjorn terminó de fumar. Apagó la colilla contra la barandilla. Se levantó.

— Vamos.

Sin preguntas. Sin condiciones. Simplemente — vamos. Liza pensó que Shelly sabía elegir a la gente.

Hospital en las afueras de la ciudad. Tres plantas, ladrillo beige, aparcamiento para veinte coches. Pequeño — de distrito, no de capital. Precisamente por eso tenían a Shelly aquí. No en Oslo, donde los periodistas. Aquí, donde hay silencio.

Bjorn detuvo la pickup en el aparcamiento de enfrente. Apagó el motor. Miró a Liza.

— ¿Cuánto tiempo?

— Veinte minutos. Puede que treinta.

— ¿Si no sales en cuarenta?

— Vete.

Bjorn asintió. No discutió. Liza salió sin dar un portazo. La lluvia la recibió — fría, indiferente.

Veinte minutos.

Código Naranja.

Entrada de servicio. No hace falta tarjeta — la puerta está sujeta con un ladrillo. Alguien del personal fuma aquí en los descansos. Gracias, fumador desconocido.

Pasillo del sótano. Tuberías en el techo, zumbido de ventilación, olor a lejía y detergente. Lavandería a la izquierda. Sala de servidores — más adelante por el pasillo. Puerta con el letrero «Teknikk» — cuarto técnico.

Cerrada. Cerradura normal — no electrónica. Liza sacó una horquilla del pelo. Dos segundos. Clic.

*Protocolo.*

Cuarto de mantenimiento. Un metro por dos. Cuadro eléctrico en la pared — automáticos por plantas. Armario de red en la esquina — router, switch, panel de conexiones. Parpadean lucecitas verdes. Red local del hospital.

Liza se sentó en el suelo. Sacó el portátil. Cable de red del bolsillo — corto, amarillo, igual que en Helsinki. Lo enchufó en un puerto libre del switch.

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

Paciente 4471. El respirador está en la red. El mismo Puritan Bennett 980 — el mismo protocolo que en Helsinki. Aprendes uno — los conoces todos.

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

Dos respiraciones cortas. Pausa. Una larga. Pausa. Dos cortas. Pausa. Una larga.

▲▲ · · ▲   ▲ · · ▲▲ · · ▲   ▲

No es la frecuencia — es el patrón. El cuerpo lo nota. El cuerpo *siempre* lo nota.

Liza miraba la pantalla. Pulso de Shelly: 62... 62... 63... 62...

Nada. Un minuto. Dos.

63... 64... 65...

Respiración. Inhalación — fuera de programa. El aparato registró un intento de respiración espontánea. El primero desde — Liza miró la fecha de ingreso — desde hacía cuatro semanas.

[!] Spontaneous breath detected

[!] Patient triggering above set rate

HR: 68 | SpO2 97% | Spontaneous RR: 2/min

Respiraba. Solo. Débil, espaciado — dos respiraciones por minuto sobre las de la máquina. Pero solo.

Liza continuó el patrón. Dos cortas — una larga. Dos cortas — una larga. Como llamar a una puerta. Como una mano en el hombro. Como una voz que dice: *estoy aquí, despierta, te necesito, autonom*.

HR: 72 | SpO2 98% | Spontaneous RR: 6/min

[!] Patient awareness level changing

[!] GCS rising: E2 V1 M4 

Reacción ocular — de «al dolor» a «a la voz». Verbal — de cero a sonidos inarticulados. Motora — de «flexión» a «localización del dolor». Estaba subiendo. Despacio, como un buzo desde las profundidades. Pero subiendo.

Diez minutos.

Código Rojo.

Pasos en el pasillo. Pesados, regulares. Guardia de seguridad. Ronda.

Liza se quedó inmóvil. El portátil — la única fuente de luz en el cuartito. La pantalla se reflejaba en sus ojos — números verdes sobre fondo negro. El script seguía funcionando. El patrón continuaba.

Los pasos pasaron de largo. Se alejaron. Volverán en siete u ocho minutos — ronda estándar.

Liza cambió al segundo terminal.

liza@localhost:~$ nmap -sV 172.16.4.50 -p 80,443,554,8080

PORT    STATE SERVICE

80/tcp  open  http    Hikvision CCTV Web

554/tcp open  rtsp    Hikvision DS-series

liza@localhost:~$ # ¿contraseñas por defecto? ¿en serio?

liza@localhost:~$ curl -u admin:12345 http://172.16.4.50/System/status

200 OK

Cámaras con contraseñas por defecto. Hospital de distrito. Presupuesto de IT — cero. Gracias, burocracia noruega.

```
liza@localhost:~$ # cuadro eléctrico en la pared. Automático "2ª planta" — tercero por la izquierda.
# alarma de incendios — circuito independiente. No se apagará con la luz.
# plan:
# 1. cámaras — desactivar grabación
# 2. luz 2ª planta — automático abajo
# 3. incendios — pulsador manual en el pasillo
# 4. 30 segundos
```

Liza miró el monitor del paciente 4471. Pulso — 74. Respiración espontánea — 10 por minuto. GCS — E3V2M5. Casi estaba aquí. Casi.

Detuvo el script. Devolvió el aparato al modo estándar. Ningún rastro en los logs — breath_protocol.py limpiaba tras de sí.

Liza se levantó. Cerró el portátil. Guardó el cable en el bolsillo.

Se acercó al cuadro eléctrico. Encontró el automático de la segunda planta. Puso el dedo encima.

Con la otra mano — desactivó la grabación de las cámaras. Un solo comando, enviado antes de desenchufar el cable.

Inspiración en cuatro tiempos.

Automático — abajo.

OSCURIDAD

Escalera. A tientas — la barandilla fría, metálica. Primera planta, segunda. Puerta al pasillo — abierta, el electroimán de emergencia la soltó.

Pasillo de la segunda planta. Luces rojas de emergencia — tenues, cada diez metros. Suficiente para ver contornos. Insuficiente para reconocer una cara.

Liza tiró del pulsador manual de incendios en la pared. El cristal crujió bajo sus dedos.

Sirena.

Fuerte, pulsante, llenando cada rincón. En Helsinki — silencio. En Noruega — el aullido de la sirena en la oscuridad. Contraste.

Las puertas de las habitaciones empezaron a abrirse. Enfermeras con linternas. Pacientes en bata. Voces, arrastrar de zapatillas, chirrido de camillas.

Habitación al final del pasillo. Puerta cerrada. Al lado — una silla. En la silla debería haber estado sentado un guardia.

La silla estaba vacía.

Liza miró atrás. Al fondo del pasillo — una silueta. Ancha, con chaqueta.

Liza entró en la habitación. Luz roja de emergencia. Cama. Un hombre en la cama.

Shelly.

Delgado — había adelgazado. La barba le había crecido. Manos sobre la manta — finas, con un catéter en la vena. Ojos — cerrados. Pero la respiración — suya. El aparato funcionaba en modo de apoyo, no forzado. Respiraba solo. El patrón había funcionado.

Camilla junto a la pared. Liza desconectó el gotero. Desconectó los sensores del monitor — pulsioxímetro, presión. El monitor pitó — señal perdida. No importa. La sirena es más fuerte.

Mascarilla del respirador — la quitó. Shelly se estremeció. Aspiró aire — ávido, ronco, por sí mismo. Abrió los ojos.

Turbios. Como los de Markus en el sótano. Pero vivos.

— Soy yo — dijo Liza. — No hables. Respira.

Lo pasó a la camilla. Ligero — demasiado ligero. Cuatro semanas de coma devoran los músculos.

Dio un paso adelante. Un brazo le rodeó el cuello por detrás. Estrangulándola. Intentó zafarse — no pudo. Cayeron al suelo. La presa era demasiado fuerte. «Pedazo de bestia» — solo alcanzó a pensar Liza antes de perder el conocimiento.

Pero un segundo antes, la silueta de Bjorn apareció en el umbral.

Tres zancadas, patada de fútbol a la cabeza. El cuerpo del atacante se sacudió y quedó inerte.

Bjorn no lo miró. Ya no era una amenaza.

Liza yacía en el suelo. Ojos cerrados. Respira — pero superficial, entrecortado.

Bjorn se arrodilló. Comprobó el pulso en la muñeca — no en el cuello. Después de un estrangulamiento no se toca el cuello. Lo tiene. Débil, rápido, pero lo tiene.

Montacargas. Primera planta. Salida de servicio — el mismo ladrillo sujetando la puerta. Gracias, fumador desconocido. Dos veces.

Lluvia. Aparcamiento.

Liza los vio primero. Tres. Junto a la pickup de Bjorn. Chaquetas negras, pelo corto, postura — piernas a la anchura de los hombros. Contratistas privados. El guardia había conseguido llamar.

Bjorn estaba en la esquina del edificio. También los había visto. Liza — con la camilla, respirando con dificultad, sin armas. Indefensa.

Uno de los tres giró la cabeza. La vio. Su mano fue hacia la cadera — hacia la pistolera.

Bjorn dio tres pasos hacia la pickup y de repente se transformó en un resorte — muslo izquierdo protegiendo la ingle, codo izquierdo el corazón, pistola en las manos semiflexionadas. ¡Bam, Bam, Bam! Espejo izquierdo, espejo derecho, rueda delantera. Los tres se agacharon tras la pickup — reflejo, un segundo.

El resorte se distendió y se deslizó tras el volante de la ambulancia.

— Aquí — dijo Bjorn. Breve, tranquilo. Como si llamara a comer.

Ambulancia. Amarilla y roja, con el motor en marcha — el conductor había salido corriendo al oír la sirena, dejó las llaves puestas.

Bjorn abrió las puertas traseras. Ayudó a pasar a Shelly de la camilla al interior. Liza se subió detrás.

— ¿Vivo? — preguntó Bjorn.

— Vivo.

Bjorn se sentó al volante. La ambulancia arrancó.

Al otro lado de la carretera, junto al fiordo, hacia la oscuridad.

Shelly abrió los ojos. Miró a Liza. La reconoció — o no, imposible saberlo. Sus labios se movieron.

— ...¿autonom?

Liza se inclinó hacia su oído.

— Autonom. Todo según el plan. Duerme.

Cerró los ojos. La lluvia repiqueteaba en el techo de la ambulancia. Bjorn conducía en silencio. Las luces intermitentes teñían el fiordo de azul y rojo — agua negra, montañas negras, coche ajeno.

Liza contaba sus respiraciones. Doce por minuto. Suyas. Sin aparato.
