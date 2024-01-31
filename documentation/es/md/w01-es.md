# Semana 1. Principios y prácticas, Gestión de Proyectos

 > *Tarea A:*
 >
 > Planifica y realiza un boceto de un potencial proyecto final. 
 >
 > *Tarea B:*
 >
 > Realiza un tutorial de Git paso a paso.  
 > Construye un sitio personal en el repositorio de la clase describiéndote a ti y tu proyecto final.


## Reinventando mi proceso de documentar

### Estoy usando macOS otra vez ¿Cómo pude caer tan bajo?
A ver como explico ésto... Otro dia lo explico.

### Mi teclado es raro
Nunca supe escribir a máquina, aunque siempre quise aprender. Mientras trabajaba en la organización de Fab15 en Egipto, me fijé en que Sherry Lassiter tiene una gran habilidad para escribir a máquina. En ese momento, me decidí a aprender. Hay una ventaja cuando aprendes a hacer una cosa desde cero, y es que no tienes ningún vicio. Así que yo no aprendí el sistema QWERTY, que está originalmente diseñado para que las antiguas máquinas de escribir no se atascaran. Yo aprendí con el sistema [Colemak](https://colemak.com). Colemak está diseñado para que las letras de mayor uso en idioma ingles esten en la fila central. Tengo un [teclado orto lineal](https://drop.com/buy/preonic-mechanical-keyboard) al que he puesto el layout colemak, y practico unos cinco minutos al día. Lo que más me gusta de la distribución Colemak es que la tecla de borrar está al lado izquierdo de la tecla `A`.

![](../../img/w01/preonic.webp)

También tengo un [software en macOS](https://karabiner-elements.pqrs.org) que cambia mi distribución del teclado a Colemak y también cambia la función de la tecla bloqueo de mayúsculas por el borrado hacia atrás.

### Mi editor de texto también es raro
Mi intención es usar únicamente un editor de texto en la línea de comandos. Tengo algunas nociones de `vim` y quiero profundizar en el aprendizaje. Me gusta la idea de usar únicamente el teclado para editar texto. Para evitar la tentación de usar Visual Studio Code, lo he desinstalado. El editor de texto vim es bastante parco de origen. Por ello, voy a instalar algunos plugins. Esta es una lista que iré ampliando con el tiempo:

- [NERDTree](https://github.com/preservim/nerdtree) para tener una barra lateral con el listado de ficheros, y así poder navegar rápidamente entre archivos.
- [vim-devicons](https://github.com/ryanoasis/vim-devicons) para visualizar con un pequeño icono gráfico los archivos y las carpetas. 

 Otros enlaces utiles:

- [VimAwesome](https://vimawesome.com) es una página con cientos de plugins de vim
- [Fran's My Computing repo](https://github.com/TheBeachLab/myComputing) con algunos trucos, si te gusta usar la línea de comandos.

### Documentación multi-idioma con IA.
Debo ser realista. No tengo mucho tiempo libre y, dentro de poco, aún tendré menos. Así que necesito un sistema para escribir la documentación de forma ágil. Voy a probar una nueva técnica para documentar que me va a permitir tener la documentación en dos (o más) idiomas. Ahora mismo, la mayor parte del texto que estas leyendo, esta siendo dictado en español a mi ordenador Mac.

![](../../img/w01/dictation.webp)

Esto me ahorra algo tiempo a la hora de escribir. Algunas partes, como el código, lo tengo que escribir manualmente. También tengo que hacer correcciones manualmente, por ejemplo, cuando incluyo enlaces.

De esta manera, estoy generando archivos en Markdown con la documentación en español. El nombre del archivo de cada semana contiene codificado la semana en la que me encuentro y el idioma de la documentación. En este caso: `w01-es.md`. El problema es que la documentación tiene que estar en inglés. El motivo por el cual no lo dicto directamente en inglés, es que mi acento es tan malo que el ordenador no me entiende. Para solucionar ese problema, voy a usar una inteligencia artificial para traducir el texto de ese archivo al idioma inglés y también al alemán. Guardaré los archivos como `w01-en.md` y `w01-de.md` respectivamente. El modelo de inteligencia artificial tiene que ser capaz de reconocer la sintaxis de Markdown y ser capaz de respetarla. También tendrá que manipular los enlaces internos, porque los enlaces que vayan `w02-es.md` de la documentación en español tienen que cambiarse a `w02-en.md` en la versión inglesa de la documentación. Es posible que el modelo vaya mejorando (o incluso cambie) a lo largo de fab academy. Por eso mantendré el texto en español y volveré a ejecutar la traducción de todos los archivos cada semana. Solo voy a editar el archivo original en español. No manipularé manualmente la traducción generada. Así que si lo que lees en ingles o aleman no tiene sentido, echale la culpa a OpenAI o cual sea el modelo que esté usando. 

He preguntado a César Garcia, de [La Hora Maker](https://www.youtube.com/lahoramaker), que me ayude a encontrar un modelo para la traducción. César me ha recomendado usar la API Whisper de OpenAI, que es capaz de traducir directamente desde el audio en español. De momento solo estoy interesado en la traducción, por lo que he creado un asistente en la API de OpenAI con estas instrucciones:

> Translate the text from Spanish to English, Read the entire document to grasp context before translating it, take into account nuances and idioms of the Spanish language and translate them to the equivalents in English. The translation should not be literal, focus on maintaining the original meaning and provide a translation that makes sense in english. Ignore external URLs and code snippets in the translation; if encountering a markdown link, translate the text inside square brackets. Modify internal markdown link URLs to point to the appropriate english file, e.g., change w01-es.md to w01-en.md. Recognize and retain brands and names without translation. Use correct grammar and syntax in the final text. The style of the translation should be informal.

Tengo otro modelo en alemán con instrucciones similares. Voy cambiando las instrucciones de vez en cuando para intentar mejorar la traducción. 

Esta página que estas leyendo tiene unos 3600 tokens. Puedes saber cuantos tokens tiene un texto usando el [OpenAI Tokenizer](https://platform.openai.com/tokenizer). El coste de la traducción a los dos idiomas de esta página es aproximadamente 0.29 USD, teniendo en cuenta que cada 1000 tokens cuestan 0.01 USD el input y 0.03 USD el output. Me parece bastante caro, y además el coste va a subir a medida que avanza Fab Academy. Por ese motivo solo traduciré los contenidos cuando considere avanzado el trabajo.

En mi lista de deseos voy a seguir buscando un modelo que sea local. De ese modo podré traducir los contenidos más frecuentemente. Por ahora he estado probando los modelos `Phi 2` y `Yarn Mistral` con resultados nefastos.

### Automatizando el proceso de traducción
Al principio estuve usando la ventana de API de OpenAI. Ahora he automatizado este proceso usando python en la linea de comandos. Usando una mezcla de Bing Copilot y la versión gratuita de ChatGPT, pedí un programa que automatizase la traducción usando la libreria de OpenAI. Pero no salió bien. Después de bastante tira y afloja (la IA no suele generar código correcto a la primera), acabé desquiciado e insultando a Bing.

![](../../img/w01/bing.webp)

Al final tuve que leer la documentación de la API para hacer que el programa funcionase.

Para evitar sobrecostes innecesarios, el script solo traduce los archivos Markdown en español que he añadido usando `git add`. Gracias a eso puedo controlar el coste. Una vez hecho esto, simplemente ejecuto `python translate-en.py` y el script genera las páginas Markdown traducidas al ingles. Hago lo mismo para el alemán.

En realidad, normalmente no hago la traducción de forma aislada porque lo he incluido en el siguiente paso.

### Automatizando la generación de HTML y subida de archivos
La documentación de Fab Academy se tiene que presentar en forma de página web. Para generar las páginas HTML a partir de los archivos markdown he convertido a Python un script en lenguaje Bash que hice para el programa educativo [FabZero](https://github.com/Academany/fabzero). El código convierte todos los archivos `.md` en `.html` usando [Pandoc](https://pandoc.org/index.html) con una [plantilla de estilo CSS](../../../base.css). Durante la conversión, si encuentra un enlace a un documento de markdown, lo convierte en un enlace a su correspondiente documento HTML usando [este filtro LUA](../../../links-to-html.lua).

Opcionalmente, el script también automatiza la traducciones a ingles y alemán y la subida de archivos a Github. Así que cuando quiero subir mi progreso escribo:

`python auto.py --translate updating week 1`

Y de ese modo el script traduce las páginas si encuentra `--translate` entre los argumentos. También convierte todas las páginas a HTML y después lo sube todo a Github siempre que exista un mensaje, que en este caso es `updating week 1`. Si no hay mensaje, no realiza ninguno de los procesos relacionados con git. 

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

### Conclusión
Todo esto está haciendo que escribir la documentación sea un poco lento en este momento, y un poco tedioso. Pero creo que con éste sistema, **la velocidad va a aumentar drásticamente semana a semana** y al final seré capaz de documentar con gran velocidad y nivel de detalle.

Además creo que este método va a **ayudar** a muchas personas que no pueden **expresar su talento** porque no dominan otro idioma. Es injusto que eso ocurra y espero que la AI ayude a la gente a demostrar lo valiosas que son.

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
- Servicios web como Notion.com, Monday.com y similares. Si nadie me asegura que voy a vivir 350 años, no pienso dedicar ni un segundo de mi corta vida a entender como funciona un servicio que solo se ve facil en tik tok y que posiblemente cerrará mañana por la tarde.

Ahora estoy usando una combinacion de texto plano para objetivos a largo plazo, recordatorios para objetivos a medio plazo y Freeform de Apple para las tareas que voy a hacer en el dia de hoy. Freeform es un programa con lienzo infinito, parecido a [Miro](https://miro.com). Tiene las ventajas de las notas Post-it sin sus inconvenientes. Puedo personalizarlo y crear mi propio sistema. Por ejemplo he creado la casilla `DOING NOW` donde solo cabe una nota. Para mi eso es importante, porque yo solo puedo hacer una cosa a la vez. Tambien puedo dibujar a mano y eso me gusta. Probablemente haré un video explicandolo todo con más detalle.

![](../../img/w01/freeform.webp)

## Boceto del proyecto final
Todo lo relacionado con el proyecto final lo he movido a su [correspondiente sección](final-es.md).

[<< Volver al inicio](index-es.md)  
[Semana siguiente >>](w02-es.md)