### Usando Markdown
Aquí no quiero innovar demasiado. La estrategía que me ha funcionado muy bien desde hace muchos años es escribir contenido en un archivo de texto plano en un formato llamado [Markdown](https://www.markdownguide.org) `.md`. De esta manera, me centro sólamente en escribir el contenido. Ventajas de escribir en Markdown:

- No necesitas ningún programa especial para escribir texto plano. Incluso puedes escribirlo a mano si tienes buena letra y escanearlo luego.
-  Es fácil de escribir, no tienes que retorcerte los dedos escribiendo `</h1>` y cosas así. 
-  Es fácil aplicar estilos y organizar el texto.
-  Se puede leer sin que parezca que estas decodificando Matrix.

![Cuando puedes leer tu página desde el código HTML](../../img/w01/code.webp)

La documentación de Fab Academy se tiene que presentar en forma de página web. Existe un programa para la línea de comandos llamado [Pandoc](https://pandoc.org/index.html) que literalmente convierte cualquier formato de texto. Voy a usarlo para convertir los los archivos `.md` en páginas `.html` de *aspecto agradable*[^nice] con una plantilla de estilo CSS.

[^nice]: *Agradable* se refiere a fácil de leer. Otro tipo de personas valoran por encima de todo el aspecto visual de la página y prefieren dedicar tiempo en crear su propia obra de arte. Mis mejores deseos para ellos.

He modificado [esta plantilla CSS](https://jez.io/pandoc-markdown-css-theme/), que me permite añadir funcionalidades como ecuaciones, tablas, números de línea en el código, notas laterales, etc. La plantilla tenía el nombre del índice como `Contents` y lo he modificado para poder incluir una variable en el 

```html{.html .numberLines .hl-6 .tight-code}
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

