## Todo en uno
[Así funciona mi proceso:]{.smallcaps} Cuando he terminado de editar los capítulos, ejecuto el siguiente script[^261]

[^261]: Es un script originalmente escrito en lenguaje Bash que hice para el programa educativo [FabZero](https://github.com/Academany/fabzero) y que ahora he convertido a Python.

`python auto.py --translate updating week 1`

Si el script encuentra `--translate` entre los argumentos[^262], traduce las los capítulos modificados. Después concatena todos los capítulos y crea un único archivo Markdown para cada semana. El paso siguiente es la conversión a HTML de todos esos archivos. Si durante la conversión encuentra un enlace a un documento de Markdown, lo convierte en un enlace a su correspondiente documento HTML usando [este filtro LUA](../../../links-to-html.lua). Finalmente lo sube todo a Github siempre que exista un mensaje, que en este caso es `updating week 1`. Si no hay mensaje, no realiza ninguno de los procesos relacionados con git. 

[^262]: Eso lo hago para ahorrar costes, ya que no quiero traducir las páginas en cada modificación.

Puedes analizar el script aquí: [auto.py](../../../auto.py)

