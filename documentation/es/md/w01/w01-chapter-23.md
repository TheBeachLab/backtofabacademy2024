### Estructura de archivos
[Al principio]{.smallcaps}, escribía el texto de cada semana en un único archivo. Pero como leerás más adelante, uso un servicio de pago para la traducción. Cada vez que editaba una línea, tenía que traducir todo el archivo entero de nuevo. Para limitar los costes he dividido la semana en capítulos[^231] y creo un archivo para cada capítulo. De ese modo solo se traducen los capítulos que he modificado.

[^231]: Mi estructura de archivos está inspirada en el lenguaje de programación [BASIC](https://en.wikipedia.org/wiki/BASIC)

```
/documentation
    /es
        /md
            /w01
                w01-chapter-00.md
                w01-chapter-10.md
                w01-chapter-20.md
                w01-chapter-21.md
                ...
                w01-chapter-90.md
```

El nombre del archivo contiene codificado la semana en la que me encuentro y el capítulo. El capítulo 00 es el encabezado. Uso los capítulos 10, 20, 30... para desarrollar los apartados de la semana. Si un capítulo es muy largo lo subdivido usando los números intermedios: 20, 21, 22, etc. El capítulo 90 siempre es la conclusión.

Posteriormente concateno[^232] todos los capítulos de la semana en un sólo archivo, en este caso `w01.md`.

[^232]: **Nota Importante:** Nunca edito manualmente el archivo concatenado. Sólo edito los capítulos por separado.

