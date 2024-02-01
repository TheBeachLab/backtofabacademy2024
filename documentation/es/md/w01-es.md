---
title: "Semana 1. Principios y prácticas, Gestión de Proyectos"
subtitle: "Regreso a Fab Academy 2024. Fran Sanchez"
lang: es-ES
---
:::{.note .yellow}
|     |
| --- |
| *Tarea A:* |
| Planifica y realiza un boceto de un potencial proyecto final.  |
|     |
| *Tarea B:* |
| Realiza un tutorial de Git paso a paso. |
| Construye un sitio personal en el repositorio de la clase describiéndote a ti y tu proyecto final. |
:::

## Mi entorno

### Estoy usando macOS otra vez ¿Cómo pude caer tan bajo?
A ver como explico ésto... Otro dia lo explico.

### Mi teclado es raro
Nunca supe escribir a máquina, aunque siempre quise aprender. Mientras trabajaba en la organización de Fab15 en Egipto, me fijé en que Sherry Lassiter tiene una gran habilidad para escribir a máquina. En ese momento, me decidí a aprender. Hay una ventaja cuando aprendes a hacer una cosa desde cero, y es que no tienes ningún vicio. Así que yo no aprendí el sistema QWERTY, que está originalmente diseñado para que las antiguas máquinas de escribir no se atascaran. Yo aprendí con el sistema [Colemak](https://colemak.com). Colemak está diseñado para que las letras de mayor uso en idioma ingles esten en la fila central. Tengo un [teclado orto lineal](https://drop.com/buy/preonic-mechanical-keyboard) al que he puesto el layout colemak, y practico unos cinco minutos al día. Lo que más me gusta de la distribución Colemak es que la tecla de borrar está al lado izquierdo de la tecla `A`.

![](../../img/w01/preonic.webp)

También tengo un [software en macOS](https://karabiner-elements.pqrs.org) que cambia mi distribución del teclado a Colemak y también cambia la función de la tecla bloqueo de mayúsculas por el borrado hacia atrás.

### Mi editor de texto también es raro
Mi intención es usar únicamente `vim`, un editor de texto en la línea de comandos. Tengo algunas nociones de `vim` y quiero profundizar en el aprendizaje. Me gusta la idea de usar únicamente el teclado para editar texto. Para evitar la tentación de usar Visual Studio Code, lo he desinstalado. El editor de texto vim es bastante parco de origen. Por ello, voy a instalar algunos plugins. Esta es una lista que iré ampliando con el tiempo:

- [NERDTree](https://github.com/preservim/nerdtree) para tener una barra lateral con el listado de ficheros, y así poder navegar rápidamente entre archivos.
- [vim-devicons](https://github.com/ryanoasis/vim-devicons) para visualizar con un pequeño icono gráfico los archivos y las carpetas. 

 Otros enlaces utiles:

- [VimAwesome](https://vimawesome.com) es una página con cientos de plugins de vim
- [Fran's My Computing repo](https://github.com/TheBeachLab/myComputing) con algunos trucos, si te gusta usar la línea de comandos.

## Reinventando mi proceso de documentar
Debo ser realista. No tengo mucho tiempo libre y, dentro de poco, aún tendré menos. Así que necesito un sistema para escribir la documentación de forma ágil. Voy a probar un nuevo sistema para documentar. Como beneficio inesperado, este sistema me va a permitir tener la documentación en dos (o más) idiomas.

### Usando Markdown
Aquí no quiero innovar demasiado. La estrategía que me ha funcionado muy bien desde hace muchos años es escribir contenido en un archivo de texto plano en un formato llamado [Markdown](https://www.markdownguide.org) `.md`. De esta manera, me centro sólamente en escribir el contenido. Ventajas de escribir en Markdown:

- No necesitas ningún programa especial para escribir texto plano. Incluso puedes escribirlo a mano si tienes buena letra y escanearlo luego.
-  Es fácil de escribir, no tienes que retorcerte los dedos escribiendo `</h1>` y cosas así. 
-  Es fácil aplicar estilos y organizar el texto.
-  Se puede leer sin que parezca que estas decodificando Matrix.

![Cuando puedes leer tu página desde el código HTML](../../img/w01/code.webp)

La documentación de Fab Academy se tiene que presentar en forma de página web. Existe un programa para la línea de comandos llamado [Pandoc](https://pandoc.org/index.html) que literalmente convierte cualquier formato de texto. Voy a usarlo para convertir los los archivos `.md` en páginas `.html` de "aspecto agradable" con una plantilla de estilo CSS.

> Nota: "Agradable" se refiere a fácil de leer. Otro tipo de personas valoran por encima de todo el aspecto visual de la página y prefieren dedicar tiempo en crear su propia obra de arte. Mis mejores deseos para ellos.

 Estoy usando [esta plantilla CSS](https://jez.io/pandoc-markdown-css-theme/), que me permite añadir funcionalidades como ecuaciones, tablas, números de línea en el código, notas laterales, etc.

### Ahorrar tiempo dictando
La mayor parte del texto que estas leyendo, esta siendo dictado **en español** dentro de un archivo de texto Markdown. El motivo por el cual no lo dicto directamente en inglés es que mi acento es tan malo que el ordenador no me entiende. Para dictar estoy usando la herramienta de dictado de macOS.

![](../../img/w01/dictation.webp)

Me gusta mucho esta herramienta porque:

- Funciona en todas partes del sistema operativo, incluyendo el terminal.
- Te permite hablar y hacer pausas de hasta 30 segundos sin que se desconecte.
- Puedes editar el texto mientras dictaestas dictando.
- Puedes añadir emojis 😊 
- Añade signos de puntuación automáticamente, y tambien los puedes añadir manualmente.
- También puedes cambiar de línea y de parrafo usando la voz.
- Si tu procesador es Apple Silicon entiende el contexto y se autocorrige. Todo ello sin conexión.
- Lo puedo usar mientras escucho música con mis auriculares.

Aquí esta la lista completa de comandos en [español](https://support.apple.com/es-es/guide/mac-help/mh40695/14.0/mac/14.0), [ingles](https://support.apple.com/en-gb/guide/mac-help/mh40695/14.0/mac/14.0) y [alemán](https://support.apple.com/de-de/guide/mac-help/mh40695/14.0/mac/14.0). Esto me ahorra algo tiempo a la hora de escribir. Algunas partes las tengo que escribir manualmente, por ejemplo, cuando escribo código o incluyo enlaces. También tengo que hacer algunas correcciones manualmente.

### Estructura de archivos
De esta manera, estoy generando archivos en Markdown con la documentación en español. Al principio escribia el texto de cada semana en un único archivo. Pero como leerás más adelante, uso un servicio de pago para la traducción. Cada vez que editaba una línea, tenía que traducir todo el archivo entero de nuevo. Para reducir los costes ahora divido la semama en capítulos y creo un archivo para cada capítulo. De ese modo solo se traducen los capítulos que he modificado. Mi estructura de archivos está inspirado en el lenguaje de programación [BASIC](https://en.wikipedia.org/wiki/BASIC):

```
/documentation
    /es
        /md
            /w01
                w01-chapter-00-es.md
                w01-chapter-10-es.md
                w01-chapter-20-es.md
                w01-chapter-21-es.md
                ...
                w01-chapter-90-es.md
                w01-chapter-99-es.md
```

El nombre del archivo de cada semana contiene codificado la semana en la que me encuentro, el capítulo y el idioma de la documentación. El capítulo 00 es el encabezado. Uso los capítulos 10, 20, 30... para desarrollar los apartados de la semana. Si un capítulo es muy largo lo subdivido usando los números intermedios: 20, 21, 22, etc. El capítulo 90 siempre es la conclusión y el 99 es el pie de página.

Posteriormente concateno todos los capítulos de la semana en un sólo archivo, en este caso: `w01-es.md`.

> **Nota Importante:** Nunca edito manualmente el archivo concatenado. Sólo edito los capitulos por separado.

### Traducciones automáticas con IA
En Fab Academy, la documentación tiene que estar en inglés. Los traductores de idiomas tradicionales son bastante malos. No son capaces de entender el contexto y producen resultados que no suenan naturales. Voy a usar una inteligencia artificial para traducir el texto de los capítulos al inglés y también al alemán.

El modelo de inteligencia artificial tiene que ser capaz de reconocer la sintaxis de Markdown y ser capaz de respetarla. También tendrá que manipular los enlaces internos, porque los enlaces que vayan `w02-es.md` de la documentación en español tienen que cambiarse a `w02-en.md` en la versión inglesa de la documentación. Es posible que el modelo vaya mejorando (o incluso cambie) a lo largo de fab academy. Por eso mantendré el texto en español y volveré a ejecutar la traducción de todos los archivos de vez en cuando. Solo voy a editar los archivos en español. No manipularé manualmente las traducciones generadas. Así que si lo que lees en ingles o alemán no tiene sentido, echale la culpa a OpenAI o cual sea el modelo que esté usando. 

He preguntado a César Garcia, de [La Hora Maker](https://www.youtube.com/lahoramaker), que me ayude a encontrar un modelo para la traducción. César me ha recomendado usar la API Whisper de OpenAI, que es capaz de traducir directamente desde el audio en español. De momento solo estoy interesado en la traducción, por lo que he creado un asistente en la API de OpenAI con estas instrucciones:

```
Translate the text from Spanish to English, Read the entire document to grasp context before translating it, take into account nuances and idioms of the Spanish language and translate them to the equivalents in English. The translation should not be literal, focus on maintaining the original meaning and provide a translation that makes sense in english. Ignore external URLs and code snippets in the translation; if encountering a markdown link, translate the text inside square brackets. Modify internal markdown link URLs to point to the appropriate english file, e.g., change w01-es.md to w01-en.md. Recognize and retain brands and names without translation. Use correct grammar and syntax in the final text. The style of the translation should be informal.
```

Tengo otro modelo en alemán con instrucciones similares. Voy cambiando las instrucciones de vez en cuando para intentar mejorar la traducción. 

Esta página que estas leyendo tiene unos 4000 tokens. Puedes saber cuantos tokens tiene un texto usando el [OpenAI Tokenizer](https://platform.openai.com/tokenizer). El coste de la traducción a los dos idiomas de esta página es aproximadamente 0.32 USD, teniendo en cuenta que cada 1000 tokens cuestan 0.01 USD el input y 0.03 USD el output. Me parece bastante caro, y además el coste va a subir a medida que avanza Fab Academy. Por ese motivo solo traduciré los contenidos cuando considere avanzado el trabajo.

Por el momento las traducciones son bastante buenas. Algunas veces no cambia correctamente los enlaces, así que en el futuro esa tarea la voy a realizar mediante un script que es más fiable. Pedí a [Sophia Döring](https://fabacademy.org/2024/labs/kamplintfort/students/sophia-doring/) que revisara también la traducción en alemán. Me ha dicho que en general también está bastante bien, aunque a veces usa palabras en alemán en poco uso, sobretodo para referirse a términos técnicos. Puede que eso esté provocado por como escribo el texto original. Estoy usando los equivalentes en español de términos técnicos que en el día a día realmente digo en inglés.

En mi lista de deseos voy a seguir buscando un modelo que sea local. De ese modo podré traducir los contenidos más frecuentemente. Por ahora he estado probando los modelos `Phi 2` y `Yarn Mistral` con resultados nefastos.

### Automatizando el proceso de traducción
Al principio estuve usando la ventana de API de OpenAI. Ahora he automatizado este proceso usando python en la linea de comandos. Usando una mezcla de Bing Copilot y la versión gratuita de ChatGPT, pedí un programa que automatizase la traducción usando la libreria de OpenAI. Pero no salió bien. Después de bastante tira y afloja (la IA no suele generar código correcto a la primera), acabé desquiciado e insultando a Bing.

![](../../img/w01/bing.webp)

Al final tuve que leer la documentación de la API para hacer que el programa funcionase.

Para evitar sobrecostes innecesarios, el script solo traduce los capítulos en español que he añadido usando `git add`. Gracias a eso puedo controlar mejor el coste. Una vez hecho esto, simplemente ejecuto `python translate-en.py` y el script genera las páginas Markdown traducidas al ingles. Hago lo mismo para el alemán.

En realidad, normalmente no hago la traducción de forma aislada porque lo he incluido en el siguiente paso.

### Automatizando todo el proceso
Para automatizar el proceso completo he convertido a Python un script en lenguaje Bash que hice para el programa educativo [FabZero](https://github.com/Academany/fabzero). Yo escribo algo así:

`python auto.py --translate updating week 1`

El script traduce las los capitulos modificados si encuentra `--translate` entre los argumentos[^1]. Después concatena todos los capítulos y crea un único archivo Markdown de cada semana. El paso siguiente es la conversión a HTML de todos esos archivos. Durante la conversión, si encuentra un enlace a un documento de markdown, lo convierte en un enlace a su correspondiente documento HTML usando [este filtro LUA](../../../links-to-html.lua). Finalmente lo sube todo a Github siempre que exista un mensaje, que en este caso es `updating week 1`. Si no hay mensaje, no realiza ninguno de los procesos relacionados con git. 

[^1]: Eso lo hago para ahorrar costes, ya que no quiero traducir las páginas en cada modificación.

Puedes analizar el script aquí: [auto.py](../../../auto.py)

### Usando CD/CI en Github para servir las páginas web

Veámos lo que tengo hasta ahora en Github:

- Mis archivos `.md` originales en español
- Los archivos `.md` traducidos por IA al inglés y alemán
- Las páginas `.html` de todos los archivos `.md` generadas por Pandoc.

Lo único que falta ahora es un servidor web. Y eso lo puedes hacer desde Github accediendo a los ajustes del repositorio.

![](../../img/w01/cicd.webp)

Esto creará un archivo en `.github/workflows/static.yml`, del cual solo tuve que modificar el `runner`, porque `runs-on: ubuntu-latest` no funcionaba. Lo cambié por `runs-on: ubuntu-22.04` y al hacer `commit`, las páginas se sirvieron de forma automática.

### Resultado final

[https://thebeachlab.github.io/backtofabacademy2024/](https://thebeachlab.github.io/backtofabacademy2024/)

## Git: Ese pozo sin fondo
Alguien podría pensar que como uso git desde hace 10 años ya se todo lo que hay que saber acerca del sistema de control de versiones. Para nada. Estas son las cosas que quiero mejorar durante este ciclo de Fab Academy:

- Reprimir mi tendencia a subir los cambios a la rama principal. Normalmente no pasa nada, pero tengo que acostumbrarme a crear una nueva rama para cada cambio.
- ~~Robar los~~ Inspirarme en los [alias de Neil](http://academy.cba.mit.edu/classes/project_management/archive.html) para ejecutar comandos de git más rápidamente.

(Puede que añada más cosas a lo largo de Fab Academy...)

## Gestión de proyectos
Me gustaría explicar como gestiono mis proyectos. Cuando no tienes jefe, y nadie te dice lo que tienes que hacer, hay que ser muy disciplinado. De lo contrario puedes caer en una espiral negativa.

 Lo mas importante es **saber adonde vas**. Porque si no lo sabes, tienes un problema muy grave. A veces te encontrarás perdido en Fab Academy (y en tu vida). No sabrás lo que quieres hacer, no tienes ganas de nada y parece que te mueves a camara lenta mientras el mundo se mueve a toda velocidad. Cuando eso te ocurra, recuerda a [Phil Stutz](https://www.thetoolsbook.com). Invierte en tí mismo: Haz ejercicio, reconecta con otras personas, escribe tus memorias en un diario. A mi me ayuda y estoy convencido de que a ti también te ayudará. Pronto verás tu estrella polar. Pon rumbo a ella.

 Lo segundo es **aprender a reducir y simplificar**. Unos de tus mayores problemas en Fab Academy va a ser parecido a este: No encuentras una foto que estas seguro que tenias. No sabes si está en las fotos del movil, en el Google Drive, o en el disco USB, si la pasaste a la carpeta del ordenador, o alguien te la dio por WhatsApp... Simplifica. Reduce.

Y por último, y creo que lo más importante. El verdadero secreto de conseguir cualquier cosa, da igual lo dificil que sea, es avanzar dando **muchos pasos muy pequeños**. Solucionas un problema pequeño, después otro, y después otro más. Así es como funciona.

En cuanto a herramientas para ayudarte a gestionar, he probado unas cuantas. Así que empezaré por las que no me funcionan:

- Notas Post-it en la pared. La idea es buena. Muy visual y ágil. Pero tiene dos problemas. Primer problema: En Barcelona suele hace mucha calor y las notas se caen. Segundo problema: Si no veo la pared no hay proyecto.
- Software tipo Kanban y similares. Intentan parecerse a las notas Post-it. No las uso porque: Me parecen complicadas y no me dejan dibujar.
- Microsoft Project y similares. Sin comentarios.
- Servicios web como Notion.com, Monday.com y similares. No pienso dedicar ni un segundo de mi corta vida a entender como funciona un servicio que solo se ve facil en tik tok y que posiblemente cerrará mañana por la tarde.

Ahora estoy usando una combinacion de texto plano para objetivos a largo plazo, recordatorios para objetivos a medio plazo y Freeform de Apple para las tareas que voy a hacer en el dia de hoy. Freeform es un programa con lienzo infinito, parecido a [Miro](https://miro.com). Tiene las ventajas de las notas Post-it sin sus inconvenientes. Puedo personalizarlo y crear mi propio sistema. Por ejemplo he creado la casilla `DOING NOW` donde solo cabe una nota. Para mi eso es importante, porque yo solo puedo hacer una cosa a la vez. Tambien puedo dibujar a mano y eso me gusta. Probablemente haré un video explicandolo todo con más detalle.

![](../../img/w01/freeform.webp)

## Boceto del proyecto final
Todo lo relacionado con el proyecto final lo he movido a su [correspondiente sección](final-es.md).

## Conclusión
Todo esto está haciendo que escribir la documentación sea lento y un poco tedioso en este momento. Pero creo que con éste sistema, **la velocidad va a aumentar drásticamente semana a semana** y al final seré capaz de documentar con gran velocidad y nivel de detalle.

Además creo que este método va a **ayudar** a muchas personas que no pueden **expresar su talento** porque no dominan otro idioma. Es injusto que eso ocurra. Espero que la AI ayude a la gente a demostrar lo valiosas que son.

[← Volver al inicio](index-es.md)

