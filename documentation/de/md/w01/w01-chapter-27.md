### Webseiten servieren

Schauen wir mal, was ich bisher auf Github habe:

- Meine originalen `.md`-Dateien auf Spanisch
- Die von KI ins Englische und Deutsche übersetzten `.md`-Dateien
- Die `.html`-Seiten aller `.md`-Dateien, erstellt mit Pandoc.

Das Einzige, was jetzt noch fehlt, ist ein Webserver. Und das kannst du direkt über Github machen, indem du zu den CI/CD-Einstellungen des Repos gehst.

![](../../img/w01/cicd.webp)

Das erstellt eine Datei unter `.github/workflows/static.yml`, bei der ich nur den `runner` ändern musste, weil `runs-on: ubuntu-latest` nicht funktionierte. Ich habe es auf `runs-on: ubuntu-22.04` geändert und nach dem `commit` wurden die Seiten automatisch serviert.

### Endergebnis

[https://thebeachlab.github.io/backtofabacademy2024/](https://thebeachlab.github.io/backtofabacademy2024/)

