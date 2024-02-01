### Einsatz von CI/CD auf Github zum Bereitstellen von Webseiten

Schauen wir, was ich bisher auf Github habe:

- Meine originalen `.md`-Dateien auf Spanisch
- Die von KI ins Englische und Deutsche übersetzten `.md`-Dateien
- Die `.html`-Seiten aller `.md`-Dateien, erzeugt durch Pandoc.

Das Einzige, was jetzt noch fehlt, ist ein Webserver. Und das kannst du direkt von Github aus machen, indem du zu den Einstellungen des Repositories gehst.

![](../../img/w01/cicd.webp)

Das wird eine Datei unter `.github/workflows/static.yml` erstellen, bei der ich nur den `runner` anpassen musste, da `runs-on: ubuntu-latest` nicht funktionierte. Ich änderte es zu `runs-on: ubuntu-22.04` und nach dem `commit` wurden die Seiten automatisch bereitgestellt.

### Endergebnis

[https://thebeachlab.github.io/backtofabacademy2024/](https://thebeachlab.github.io/backtofabacademy2024/)

