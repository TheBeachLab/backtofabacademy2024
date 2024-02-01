### Automatizando todo el proceso
Para automatizar el proceso completo he convertido a Python un script en lenguaje Bash que hice para el programa educativo [FabZero](https://github.com/Academany/fabzero). Yo escribo algo así:

`python auto.py --translate updating week 1`

El script traduce las los capitulos modificados si encuentra `--translate` entre los argumentos[^1]. Después concatena todos los capítulos y crea un único archivo Markdown de cada semana. El paso siguiente es la conversión a HTML de todos esos archivos. Durante la conversión, si encuentra un enlace a un documento de markdown, lo convierte en un enlace a su correspondiente documento HTML usando [este filtro LUA](../../../links-to-html.lua). Finalmente lo sube todo a Github siempre que exista un mensaje, que en este caso es `updating week 1`. Si no hay mensaje, no realiza ninguno de los procesos relacionados con git. 

[^1]: Eso lo hago para ahorrar costes, ya que no quiero traducir las páginas en cada modificación.

Puedes analizar el script aquí: [auto.py](../../../auto.py)

