### Automatizando el proceso de traducción
Al principio estuve usando la ventana de API de OpenAI. Ahora he automatizado este proceso usando python en la linea de comandos. Usando una mezcla de Bing Copilot y la versión gratuita de ChatGPT, pedí un programa que automatizase la traducción usando la libreria de OpenAI. Pero no salió bien. Después de bastante tira y afloja (la IA no suele generar código correcto a la primera), acabé desquiciado e insultando a Bing.

![](../../img/w01/bing.webp)

Al final tuve que leer la documentación de la API para hacer que el programa funcionase.

Para evitar sobrecostes innecesarios, el script solo traduce los capítulos en español que he añadido usando `git add`. Gracias a eso puedo controlar mejor el coste. Una vez hecho esto, simplemente ejecuto `python translate-en.py` y el script genera las páginas Markdown traducidas al ingles. Hago lo mismo para el alemán.

En realidad, normalmente no hago la traducción de forma aislada porque lo he incluido en el siguiente paso.

