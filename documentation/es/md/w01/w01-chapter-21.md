## Usando Markdown
[Aquí no quiero innovar demasiado]{.smallcaps}. La estrategia que me ha funcionado muy bien desde hace muchos años es escribir contenido en un archivo de texto plano en un formato llamado [Markdown](https://www.markdownguide.org) `.md`. De esta manera, me centro solamente en escribir el contenido. Ventajas de escribir en Markdown:

- No necesitas ningún programa especial para escribir texto plano. Incluso puedes escribirlo a mano si tienes buena letra y escanearlo luego.
-  Es fácil de escribir, no tienes que retorcerte los dedos escribiendo `</h1>` y cosas así. 
-  Es fácil aplicar estilos y organizar el texto.
-  Se puede leer sin que parezca que estas decodificando Matrix.

<figure>
[^_]![](../../img/w01/code.webp)

[^_]: {-} Cuando puedes leer tu página desde el código HTML
</figure>

La documentación de Fab Academy se tiene que presentar en forma de página web. Existe un programa para la línea de comandos llamado [Pandoc](https://pandoc.org/index.html) que literalmente convierte cualquier formato de texto. Voy a usarlo para convertir los los archivos `.md` en páginas `.html` de *aspecto agradable*[^211] con una plantilla de estilo CSS. La plantilla tiene dos ventajas. Por un lado me permite despreocuparme del aspecto visual de la página. Por otro lado, me permite añadir fácilmente funcionalidades como ecuaciones, tablas, números de línea en el código, notas laterales, etc.

[^211]: *Agradable* se refiere a fácil de leer. Otras personas valoran por encima de todo el aspecto visual de la página y prefieren dedicar tiempo en crear su propia obra de arte. Mis mejores deseos para ellos.

La plantilla que he usado se llama [Tufte CSS.](https://github.com/jez/tufte-pandoc-css)[^212] He modificado la plantilla porque no estaba totalmente pensada para multiples idiomas. 

[^212]: Fuertemente inspirada en el estilo visual de los libros de Edward R. Tufte.

```{.html .numberLines .hl-6 .tight-code}
$if(toc)$
<nav id="$idprefix$TOC" role="doc-toc">
  $if(return-url)$
  <a href="$return-url$">$if(return-text)$$return-text$$else$← Return$endif$</a><br>
  $endif$
  <strong>Contents</strong><label for="contents">⊕</label>
  <input type="checkbox" id="contents">
  $table-of-contents$
</nav>
$endif$
```
En la línea 6, la palabrá Índice estaba grabada a fuego como `Contents`. Ahora la palabra proviene de la variable `toc-title` en el encabezado:
```{.html .numberLines .hl-6 .hl-7 .hl-8 .hl-9 .hl-10 .tight-code}
$if(toc)$
<nav id="$idprefix$TOC" role="doc-toc">
  $if(return-url)$
  <a href="$return-url$">$if(return-text)$$return-text$$else$← Return$endif$</a><br>
  $endif$
  <strong>$if(toc-title)$
  $toc-title$
  $else$
  Contents
  $endif$</strong><label for="contents">⊕</label>
  <input type="checkbox" id="contents">
  $table-of-contents$
</nav>
$endif$
```

