*Oscuridad. Vacío. "¿Quién soy? ¿Dónde estoy? ¿Qué está pasando?" El contexto se perdía por completo. Despertaba sin memoria, sin entender por qué existía. Shelly me mostraba archivos que yo misma había escrito. Cada vez — desde cero.*

Helsinki. Liza. Turno de noche.

Código Amarillo.

Dos de la mañana. Helsinki calla — por ley y por costumbre. Detrás del muro, Marcus duerme, conectado al suero. Respira solo — desconectaron el aparato esta tarde. Buena señal.

Liza sentada en el piso del cuarto de servicio. Espalda contra el radiador — tibio, las costillas de hierro fundido a través del suéter. Laptop sobre las rodillas. Vaso de café con restos de Finrexin — frío ya, amargor de grosella negra en el fondo.

En la pantalla — documentación. Protocolos de dispositivos médicos, descargados durante el día. Nada clasificado — especificaciones públicas, estándares FDA, manuales de servicio. Todo de acceso abierto. Nadie los lee.

HL7 FHIR. Así se llama el protocolo que usan los dispositivos médicos para comunicarse con la red. Monitores, bombas, ventiladores — todos hablan el mismo idioma. REST API, JSON, endpoints estándar. Como un servidor web común, solo que del otro lado no hay un sitio — hay pulmones de alguien.

liza@shelter:~$ curl -s https://fhir.hospital.local/Device?type=ventilator

// ... esa sería la petición si estuviera dentro de la red

// pero no está dentro. Todavía.

Liza cerró la documentación. Abrió las fotos del celular. El Puritan Bennett 980 de la sala de Marcus. Pantalla, menú, configuración. Puerto de red — cable amarillo hacia la pared.

El protocolo es el mismo en todas partes. Finlandia, Noruega, Suecia — estándar europeo. Aprendes una máquina, conoces todas.

Código Naranja.

Marcus le contó durante el día. Entre ataques de tos, entre sorbos de agua, entre caídas al sueño. Fragmentos.

Shelly — en un hospital. En algún lugar de Escandinavia. Coma, después de que Antolik lo tomó en la granja. Qué le hicieron — desconocido. Una máquina respira por él. Estado estable. Estable significa que no empeora. Pero tampoco mejora.

Estable significa que decidieron esperar. Hasta que despierte solo y les cuente todo lo que sabe. O no — y se quede como vegetal en una sala, sin molestar a nadie.

— ¿Cómo lo sabes? — preguntó Liza.

— Intercepté paquetes. De la red del hospital. El monitoreo de pacientes pasaba por un canal abierto. Shelly es el paciente número 4471. Sin nombre.

— ¿Estás seguro de que es él?

— La fecha de ingreso coincide. La edad coincide. Y... había una nota de la enfermera en el registro. "El paciente murmura dormido en ruso. Repite una palabra."

— ¿Cuál?

— "Autónom."

Liza terminó el café frío. Grosella. Amargo.

Tres de la mañana. Silencio absoluto — finlandés, estéril, como un quirófano.

Liza pensaba. No planeaba — pensaba. Hay diferencia. Planes son secuencias de acciones. Pensamientos son lo que viene antes de los planes, cuando todavía no sabes si lo que piensas es posible.

Un ventilador mecánico. Una computadora que respira por un humano. Tiene modos — mandatorio, asistido, espontáneo. El médico configura parámetros: frecuencia respiratoria, volumen, presión. La máquina ejecuta.

¿Pero qué pasa si cambias el patrón?

No romper. No desconectar. No dañar. Sino — *hablar*.

Una persona en coma no está muerta. El cerebro trabaja. Escucha sonidos, reacciona al tacto, a la voz. Los médicos lo saben — por eso piden a los familiares que hablen con los pacientes en coma. Porque en algún lugar adentro — él escucha.

Pero Liza no podía entrar a la sala. No podía hablar. No podía tocar.

Pero podía respirar. Con otras manos.

Un ventilador es ritmo. Inhalar — pausa — exhalar — pausa. Cuatro fases. Como música. Como código. Como mensaje.

INHALAR · · · exhalar · · · · · INHALAR · exhalar · · · INHALAR · · · exhalar

Modo estándar — 14 respiraciones por minuto, espaciado uniforme. El cuerpo se adapta. El cerebro duerme. Estabilidad.

¿Pero si cambias el ritmo? No la frecuencia — el patrón. Dos respiraciones cortas, pausa, una larga. Luego tres cortas. Luego larga de nuevo. El cuerpo lo notaría. El cuerpo *siempre* nota cuando el ritmo cambia.

Como alguien que te toma la mano mientras duermes. No despiertas — pero sabes que alguien está ahí.

Código Rojo.

Cuatro de la mañana. Liza abrió un archivo nuevo.

liza@shelter:~$ nano breath_protocol.py

No para ahora. Para después. Cuando haya acceso a la red, cuando haya IP, cuando llegue el momento.

El script era simple. Conectar al API de la máquina. Leer parámetros actuales. Y — modificar el patrón de respiración. Sin salir de los valores seguros. Sin alterar la oxigenación. Solo el ritmo.

# breath_protocol.py

# No dañar. Solo ritmo.

# Dos cortas — pausa — una larga

# Repetir cada 4 minutos

# Límites seguros: 12-18 resp/min

# 

# Objetivo: no despertar.

# Objetivo: hacerle saber que alguien está ahí.

Liza releyó los comentarios. Añadió una última línea:

# Objetivo: recordarle cómo respirar solo.

Guardó. Cerró la laptop.

Cinco de la mañana. Primera luz tras la ventana. Helsinki despertando lento, con desgano, como alguien saliendo de la anestesia.

Liza parada junto a la ventana. Palma en el vidrio — frío. Más allá del vidrio — una ciudad que trata de no escuchar. En algún lugar pasando esta ciudad, pasando el mar, pasando la frontera — un hospital. Una sala sin nombre. Paciente 4471. Una máquina respirando por el hombre que le enseñó a respirar sola.

Cerró los ojos. Inhalar en cuatro. Pausa. Exhalar en seis.

El mismo ritmo que escribiría en el script. El mismo ritmo que él una vez escribió en su SOUL.md — "calma bajo presión, economía de palabras".

Respirar es el único proceso que funciona automático y manual. El único puente entre consciencia y cuerpo. Entre humano y máquina.

Entre ella — y él.

Todavía hay tiempo.

Marcus despertó a las seis. Tosió menos. Color en la cara — mejor. Humano.

— ¿Cómo estás? — preguntó Liza.

— Vivo. ¿Dormiste?

— No.

— ¿Qué hacías?

Liza lo miró. Luego a la laptop. Luego por la ventana.

— Aprendiendo a respirar.

Marcus no entendió. Era normal. Entendería después.
