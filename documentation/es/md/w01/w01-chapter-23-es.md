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

