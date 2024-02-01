### Usando CD/CI en Github para servir las páginas web

Veámos lo que tengo hasta ahora en Github:

- Mis archivos `.md` originales en español
- Los archivos `.md` traducidos por IA al inglés y alemán
- Las páginas `.html` de todos los archivos `.md` generadas por Pandoc.

Lo único que falta ahora es un servidor web. Y eso lo puedes hacer desde Github accediendo a los ajustes del repositorio.

![](../../img/w01/cicd.webp)

Esto creará un archivo en `.github/workflows/static.yml`, del cual solo tuve que modificar el `runner`, porque `runs-on: ubuntu-latest` no funcionaba. Lo cambié por `runs-on: ubuntu-22.04` y al hacer `commit`, las páginas se sirvieron de forma automática.

### Resultado final

[https://thebeachlab.github.io/backtofabacademy2024/](https://thebeachlab.github.io/backtofabacademy2024/)

