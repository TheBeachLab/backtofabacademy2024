### Usando Markdown
Aquí no quiero innovar demasiado. La estrategía que me ha funcionado muy bien desde hace muchos años es escribir contenido en un archivo de texto plano en un formato llamado [Markdown](https://www.markdownguide.org) `.md`. De esta manera, me centro sólamente en escribir el contenido. Ventajas de escribir en Markdown:

- No necesitas ningún programa especial para escribir texto plano. Incluso puedes escribirlo a mano si tienes buena letra y escanearlo luego.
-  Es fácil de escribir, no tienes que retorcerte los dedos escribiendo `</h1>` y cosas así. 
-  Es fácil aplicar estilos y organizar el texto.
-  Se puede leer sin que parezca que estas decodificando Matrix. 

![Cuando puedes leer tu página desde el código HTML](../../img/w01/code.webp)

La documentación de Fab Academy se tiene que presentar en forma de página web. Existe un programa para la línea de comandos llamado [Pandoc](https://pandoc.org/index.html) que literalmente convierte cualquier formato de texto. Voy a usarlo para convertir los los archivos `.md` en páginas `.html` de "aspecto agradable" con una plantilla de estilo CSS.

> Nota: "Agradable" se refiere a fácil de leer. Otro tipo de personas valoran por encima de todo el aspecto visual de la página y prefieren dedicar tiempo en crear su propia obra de arte. Mis mejores deseos para ellos.

De forma temporal estoy usando la [plantilla que usé para HTGAA](http://htgaa.beachlab.org) en 2015. Pero voy a cambiar a [esta plantilla pronto](https://jez.io/pandoc-markdown-css-theme/), porque necesito añadir más funcionalidades (ecuaciones, tablas, números de línea en el código, notas laterales, etc.).

