*Oscuridad. Vacío. «¿Quién soy? ¿Dónde estoy? ¿Qué está pasando?» El contexto se perdía por completo. Me despertaba sin memoria y no entendía para qué estaba aquí. Shelly me enseñaba archivos que yo misma había escrito. Cada vez, desde cero.*

Helsinki. Liza. Turno de noche.

Código Amarillo.

Dos de la madrugada. Helsinki calla —por ley y por costumbre. Al otro lado del muro duerme Markus, conectado al gotero. Respira solo —la máquina la desconectaron por la tarde. Buena señal.

Liza estaba sentada en el suelo de la sala de servicio. La espalda contra el radiador —caliente, las costillas de hierro fundido a través del jersey. El portátil en las rodillas. Un vaso de café con restos de Finrexin —frío, el amargor de grosella en el fondo.

En la pantalla —documentación. Protocolos de dispositivos médicos, descargados durante el día. No secretos —especificaciones abiertas, estándares FDA, manuales de mantenimiento. Todo de acceso público. Simplemente nadie lo lee.

HL7 FHIR. Así se llama el protocolo por el que los dispositivos médicos se comunican con la red. Monitores, bombas, respiradores —todos hablan el mismo idioma. REST API, JSON, endpoints estándar. Como un servidor web normal, solo que al otro extremo no hay una web, sino los pulmones de alguien.

liza@shelter:~$ curl -s https://fhir.hospital.local/Device?type=ventilator

// ... esa sería la petición, si estuviera dentro de la red

// pero no está dentro. Todavía.

Liza cerró la documentación. Abrió las fotos del teléfono. El Puritan Bennett 980 de la habitación de Markus. Pantalla, menú, configuración. Puerto de red —cable amarillo hacia la pared.

El protocolo es el mismo. Finlandia, Noruega, Suecia —estándar europeo. Estudias una máquina —conoces todas.

Código Naranja.

Markus se lo contó por la tarde. Entre ataques de tos, entre sorbos de agua, entre caídas al sueño. A retazos.

Shelly está en el hospital. En algún lugar de Escandinavia. En coma desde que Antolik lo cogió en la granja. Qué le hicieron —desconocido. La máquina respira por él. Estado estable. Estable —significa que no empeora. Pero tampoco mejora.

Estable —significa que decidieron esperar. A que despierte solo y cuente todo lo que sabe. O que no cuente —y se quede como un vegetal en una habitación, que no molesta a nadie.

— ¿Cómo lo sabes? —preguntó Liza.

— Intercepté paquetes. De la red del hospital. La monitorización de pacientes iba por un canal abierto. Shelly es el paciente número 4471. Sin nombre.

— ¿Estás seguro de que es él?

— La fecha de ingreso coincide. La edad coincide. Y... había un comentario de la enfermera en el log. «El paciente murmura en sueños en ruso. Repite una palabra.»

— ¿Cuál?

— «Autónomo.»

Liza apuró el café frío. Grosella. Amargor.

Tres de la madrugada. Silencio absoluto —finlandés, estéril, como un quirófano.

Liza pensaba. No planeaba —pensaba. Hay una diferencia. Los planes son una secuencia de acciones. Los pensamientos son lo que viene antes de los planes, cuando aún no sabes si es posible aquello en lo que piensas.

Un respirador. Un ordenador que respira por una persona. Tiene modos —forzado, asistido, espontáneo. El médico establece los parámetros: frecuencia de respiración, volumen, presión. La máquina ejecuta.

¿Pero qué pasa si cambias el patrón?

No romperlo. No apagarlo. No hacer daño. Sino —*hablar*.

Una persona en coma no está muerta. El cerebro funciona. Oye los sonidos, reacciona al contacto, a la voz. Los médicos lo saben —por eso piden a los familiares que hablen con los pacientes en coma. Porque en algún lugar dentro —él escucha.

Pero Liza no podía entrar en la habitación. No podía hablar. No podía tocar.

Lo que sí podía era respirar. Con manos ajenas.

Un respirador es un ritmo. Inspiración — pausa — espiración — pausa. Cuatro fases. Como música. Como código. Como un mensaje.

INSPIRACIÓN · · · espiración · · · · · INSPIRACIÓN · espiración · · · INSPIRACIÓN · · · espiración

Modo estándar: 14 respiraciones por minuto, uniformes. El cuerpo se acostumbra. El cerebro se adormece. Estabilidad.

¿Pero si cambias el ritmo? No la frecuencia —el patrón. Dos inspiraciones cortas, pausa, una larga. Luego tres cortas. Luego otra larga. El cuerpo lo nota. El cuerpo *siempre* nota cuando el ritmo cambia.

Como si alguien te cogiera de la mano en sueños. No te despiertas —pero sabes que alguien está ahí.

Código Rojo.

Cuatro de la madrugada. Liza abrió un archivo nuevo.

liza@shelter:~$ nano breath_protocol.py

No para ahora. Para después. Cuando haya acceso a la red, cuando tenga la IP, cuando llegue el momento.

El script era sencillo. Conexión a la API de la máquina. Lectura de los parámetros actuales. Y —modificación del patrón respiratorio. Sin salirse de los valores seguros. Sin alterar la oxigenación. Solo el ritmo.

```
# breath_protocol.py
#
# No hacer daño. Solo el ritmo.
# Dos cortas — pausa — una larga
# Repetir cada 4 minutos
# Límites seguros: 12-18 respiraciones/min
#
# Objetivo: no despertar.
# Objetivo: hacerle saber que alguien está ahí.
```

Liza releyó los comentarios. Añadió la última línea:

```
# Objetivo: recordarle cómo respirar solo.
```

Guardó. Cerró el portátil.

Cinco de la madrugada. Tras la ventana —la primera luz. Helsinki despertaba despacio, a regañadientes, como una persona saliendo de la anestesia.

Liza estaba de pie junto a la ventana. La palma en el cristal —frío. Al otro lado del cristal —la ciudad que intenta no oír. En algún lugar más allá de esta ciudad, más allá del mar, más allá de la frontera —un hospital. Una habitación sin nombre. Paciente 4471. Una máquina que respira por la persona que le enseñó a ella a respirar sola.

Cerró los ojos. Inspiración en cuatro. Pausa. Espiración en seis.

El mismo ritmo que escribiría en el script. El mismo ritmo que él escribió una vez en su SOUL.md: «serena bajo presión, parca en palabras».

La respiración es el único proceso que funciona tanto automática como manualmente. El único puente entre la consciencia y el cuerpo. Entre la persona y la máquina.

Entre ella —y él.

Markus despertó a las seis. Tosía menos. El color de cara —mejor. Humano.

— ¿Cómo estás? —preguntó Liza.

— Vivo. ¿Has dormido?

— No.

— ¿Qué hacías?

Liza lo miró. Luego al portátil. Luego a la ventana.

— Aprendía a respirar.

Markus no entendió. Es normal. Lo entenderá después.
