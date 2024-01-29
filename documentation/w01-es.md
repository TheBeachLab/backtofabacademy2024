# Semana 1. Principios y prácticas, Gestión de Proyectos

 > *Tarea A:*
 >
 > Planifica y realiza un boceto de un potencial proyecto final. 
 >
 > *Tarea B:*
 >
 > Realiza un tutorial de Git paso a paso.  
 > Construye un sitio personal en el repositorio de la clase describiéndote a ti y tu proyecto final.

## Reinventando la manera de documentar multi-idioma con IA.

Seamos realistas. No tengo mucho tiempo libre y, dentro de poco, tendré aún menos tiempo. Así que necesito un sistema para escribir la documentación de forma ágil. Voy a probar una nueva técnica para documentar que me va a permitir tener la documentación en dos (o más) idiomas. Ahora mismo, la mayor parte del texto que estas leyendo, esta siendo dictado en español a mi computadora Mac.

![dictation settings](img/w01/dictation.webp)

Esto me ahorra algo tiempo a la hora de escribir. Algunas partes, como el código, lo tengo que escribir manualmente. También tengo que hacer correcciones manualmente, por ejemplo, cuando incluyo enlaces.

De esta manera, estoy generando archivos en markdown con la documentación en español. El nombre de archivo contiene codificado la semana en la que me encuentro y el idioma de la documentación. En este caso: `w01-es.md`. Voy a usar una inteligencia artificial para traducir el texto de ese archivo al idioma inglés y que lo guarde como `w01-en.md`. El motivo por el cual no lo dicto directamente en inglés, es que mi acento es tan malo que la computadora no me entiende. El modelo de inteligencia artificial tiene que ser capaz de reconocer la sintaxis de Markdown y ser capaz de respetarla. También tendrá que manipular los enlaces internos, porque los enlaces que vayan `w02-es.md` de la documentación en español tienen que cambiarse a `w02-en.md` en la versión inglesa de la documentación. Como es posible que el modelo vaya mejorando (o incluso cambie) a lo largo de fab academy, mantendré el texto en español y volveré a ejecutar la traducción de todos los archivos cada semana. Solo voy a editar el archivo original en español. No manipularé manualmente la traducción generada. Así que si lo que lees en ingles no tiene sentido, echale la culpa a OpenAI o al modelo que esté usando. 

He preguntado a César Garcia, de [La Hora Maker](https://www.youtube.com/lahoramaker), que me ayude a encontrar un modelo para la traducción. César me ha recomendado usar la API Whisper de OpenAI, que es capaz de traducir directamente desde el audio en español. De momento solo estoy interesado en la traducción, por lo que he creado un asistente en la API de OpenAI con estas instrucciones:

> You are an expert translator from Spanish to English. You know the nuances, and idioms of the spanish language and translate them into the appropiate idioms of the english language. You ignore URLs in the translations. If you find markdown link, you translate the text inside the square brackets if necessary. You will modify the internal URL of the markdown link so that it points to the appropiate markdown file in english. For example you will change a markdown link that points to w01-es.md to make it point to w01-en.md. But remember, you will only do that for the markdown links. You can recognize brands and names so that you avoid translating them. You will also fix the original text by capitalizing titles and fixing any other syntax or grammar error before translating it. You deliver the answers in code rather than rendering the markdown in html,  so that I can copy the markdown syntax.

De momento estoy usando la ventana de API de OpenAI. Traducir esta página que estas leyendo me ha costado unos 1500 tokens. Puedes saber cuantos tokens te va a costar la traducción usando el [OpenAI Tokenizer](https://platform.openai.com/tokenizer)

El siguiente paso es automatizar este proceso usando la linea de comandos. En mi lista de deseos voy a seguir buscando un modelo que sea local. No quiero usar un servicio web.

## Editor de Texto
Mi intención es usar únicamente un editor de texto en la línea de comandos. Tengo algunas nociones de vim y quiero profundizar en el aprendizaje. Me gusta la idea de usar únicamente el teclado para editar texto. Para evitar la tentación de usar Visual Studio Code, lo he desinstalado. El editor de texto vim es bastante parco de origen. Por ello, voy a instalar algunos plugins. Esta es una lista que iré ampliando con el tiempo:

- [NERDTree](https://github.com/preservim/nerdtree) para tener una barra lateral con el listado de ficheros, y así poder navegar rápidamente entre archivos.
- [vim-devicons](https://github.com/ryanoasis/vim-devicons) para visualizar con un pequeño icono gráfico los archivos y las carpetas.
- 

 Otros enlaces utiles:

- [VimAwesome](https://vimawesome.com)
- [Fran's My Computing repo](https://github.com/TheBeachLab/myComputing) con algunos trucos, si te gusta usar la línea de comandos.

## Distribución del Teclado

Nunca supe escribir a máquina, pero siempre quise aprender. En Fab15 en Egipto, me fijé en Sherry Lassiter, tiene una gran habilidad para escribir a máquina. En ese momento, me decidí a aprender. Hay una ventaja cuando aprendes a hacer una cosa tarde, y es que no tienes ningún vicio. Así que yo no aprendí el sistema QWERTY. Yo aprendí directamente el sistema [Colemak](https://colemak.com). Tengo un [teclado orto lineal](https://drop.com/buy/preonic-mechanical-keyboard), y practico unos cinco minutos al día. También tengo un [software en macOS](https://karabiner-elements.pqrs.org) que cambia mi distribución del teclado y también cambia la función de la tecla bloqueo de mayúsculas por el borrado hacia atrás.

Todo esto está haciendo que escribir la documentación sea un poco lento en este momento, y un poco tedioso. Pero creo que con éste sistema, la velocidad va a aumentar drásticamente semana a semana y al final seré capaz de documentar con gran velocidad y nivel de detalle.

[<< Volver al inicio](index-es.md)  
[Semana siguiente >>](w02-es.md)