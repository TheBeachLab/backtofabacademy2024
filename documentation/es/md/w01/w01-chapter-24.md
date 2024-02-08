## Traducciones automáticas con IA
[En Fab Academy]{.smallcaps}, la documentación tiene que estar en inglés. Los traductores de idiomas tradicionales son bastante malos. No son capaces de entender el contexto y producen resultados que no suenan naturales. Voy a usar una inteligencia artificial para traducir el texto de los capítulos al inglés y también al alemán.

El modelo de inteligencia artificial tiene que ser capaz de reconocer la sintaxis de Markdown y ser capaz de respetarla. Es posible que el modelo vaya mejorando (o incluso cambie) a lo largo de Fab Academy. Por eso mantendré el texto en español y volveré a ejecutar la traducción de todos los archivos de vez en cuando. Solo voy a editar los archivos en español. No manipularé manualmente las traducciones generadas. Así que si lo que lees en ingles o alemán no tiene sentido, échale la culpa a OpenAI o cual sea el modelo que esté usando. 

He preguntado a César Garcia, de [La Hora Maker](https://www.youtube.com/lahoramaker), que me ayude a encontrar un modelo para la traducción. César me ha recomendado usar la API Whisper de OpenAI, que es capaz de traducir directamente desde el audio en español. De momento solo estoy interesado en la traducción, por lo que he creado un asistente en la API de OpenAI con estas instrucciones[^243]

```
This file contains text with a mixture of markdown, yaml, pandoc and latex formatting. Translate the text from Spanish to English. Read the entire document to grasp context before translating it. Take into account nuances and idioms of the Spanish language and translate them to the equivalents in English. The translation should not be literal, focus on maintaining the original meaning and provide a translation that makes sense in english. Keep the formatting intact in the translated text, like footnotes, smallcaps, etc .Translate only the text within quotes in the YAML header of the Markdown file. Do not translate the latex notation, links, URLs, blocks of code and code snippets. If encountering a markdown link, only translate the text inside square brackets. Recognize and retain brands and names without translation. Use correct grammar and syntax in the final text. The style of the translation should be informal, with a touch of sarcastic humor.
```

Además de estas instrucciones generales, a veces tengo que comunicarle algo al traductor. Tengo un *hack* para añadir instrucciones especificas en los archivos markdown. Estos comentarios aparecen en la página markdown y, por lo tanto, el traductor los puede leer. Sin embargo Pandoc los ignora y no aparecen en la página web. ¡Es brillante!

```markdown
[comment1]: <> (Note for the translator: Do not translate "hack" as it is universally used in all languages.)
```

[comment1]: <> (Note for the translator: Do not translate "hack" as it is universally used in all languages.)

[^243]:
    Tengo otro modelo en alemán con instrucciones similares. Voy cambiando las instrucciones de vez en cuando para intentar mejorar la traducción. 

Después de dos semanas de uso puedo decir que las traducciones inglesas son muy buenas. Mucho mejor que lo que yo haría. Pedí a [Sophia Döring](https://fabacademy.org/2024/labs/kamplintfort/students/sophia-doring/) que revisara también la traducción en alemán. Me ha dicho que, en general, también está bastante bien, aunque a veces usa palabras en alemán de uso poco frecuente[^242], sobretodo para referirse a términos técnicos. 

[^242]: Puede que eso esté provocado por como escribo el texto original. Estoy usando los equivalentes en español de términos técnicos que, en el día a día, realmente digo en inglés.

Esta página que estas leyendo tiene unos 4000 tokens. Puedes saber cuantos tokens tiene un texto usando el [OpenAI Tokenizer](https://platform.openai.com/tokenizer). El coste de la traducción a los dos idiomas de esta página es aproximadamente 0.32 USD, teniendo en cuenta que cada 1000 tokens cuestan 0.01 USD el input y 0.03 USD el output. Es un coste es admisible, dada la calidad. Voy a adoptar esta solución cuando desee internacionalizar mis proyectos. En Fab Academy entiendo y asumo que el coste será considerable, debido a las múltiples modificaciones que realizaré en cada página.

En mi lista de deseos voy a seguir buscando un modelo que sea local. De ese modo podré traducir los contenidos más frecuentemente y sin preocuparme por el coste. Recientemente he probando el modelo `Miqu-1-70b`[^241] con resultados lentos pero satisfactorios. Veo luz al final del túnel.

[^241]: [Supuestamente](https://the-decoder.com/unintentional-ai-leak-from-mistral-becomes-an-unexpected-powerhouse/) filtrado por un empleado de forma no intencionada. Miqu-1-70b podría ser un buen competidor de GPT4
 
