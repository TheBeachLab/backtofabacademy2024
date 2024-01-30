# Woche 1: Prinzipien und Praktiken, Projektmanagement

> *Aufgabe A:*
>
> Plane und skizziere ein potentielles Endprojekt.
>
> *Aufgabe B:*
>
> Führe ein Schritt-für-Schritt-Git-Tutorial durch.
> Erstelle eine persönliche Website im Klassenrepository, die dich und dein Endprojekt beschreibt.

## Die Art der Dokumentation neu erfinden

### macOS, schon wieder? Wie konntest du so tief sinken?
Mal schauen, wie ich das erkläre... Ein anderer Tag vielleicht.

### Colemak?
Ich konnte nie maschinenschreiben, obwohl ich es immer lernen wollte. Während ich bei der Organisation von Fab15 in Ägypten war, bemerkte ich, dass Sherry Lassiter sehr geschickt im Maschinenschreiben ist. In diesem Moment entschied ich mich zu lernen. Es gibt einen Vorteil, wenn man etwas von Grund auf lernt: man hat keine schlechten Angewohnheiten. Also lernte ich nicht das QWERTY-System, das ursprünglich entworfen wurde, um zu verhindern, dass die alten Schreibmaschinen klemmen. Stattdessen lernte ich mit dem [Colemak](https://colemak.com) System. Colemak ist so entworfen, dass die am häufigsten genutzten Buchstaben in Englisch auf der mittleren Reihe sind. Ich habe eine [ortho-lineare Tastatur](https://drop.com/buy/preonic-mechanical-keyboard), auf der ich das Colemak-Layout verwende, und ich übe etwa fünf Minuten am Tag. Das, was mir am besten an der Colemak-Verteilung gefällt, ist, dass die Löschtaste links neben der `A`-Taste liegt.

![](img/w01/preonic.webp)

Außerdem habe ich eine [Software auf macOS](https://karabiner-elements.pqrs.org), die meine Tastaturverteilung zu Colemak ändert und die Funktion der Caps-Lock-Taste in „Rückwärts löschen“ ändert.

### Mein Texteditor
Ich möchte ausschließlich einen Texteditor in der Kommandozeilen nutzen. Ich kenne mich ein wenig mit `vim` aus und möchte mein Wissen vertiefen. Mir gefällt die Idee, nur die Tastatur zum Texteditieren zu verwenden. Um der Versuchung zu widerstehen, Visual Studio Code zu benutzen, habe ich es deinstalliert. Der Texteditor vim ist von Haus aus ziemlich spärlich. Deshalb werde ich einige Plugins installieren. Hier ist eine Liste, die ich im Laufe der Zeit erweitern werde:

- [NERDTree](https://github.com/preservim/nerdtree) für eine Seitenleiste mit einer Dateiliste, um schnell zwischen Dateien zu navigieren.
- [vim-devicons](https://github.com/ryanoasis/vim-devicons) um Dateien und Ordner mit einem kleinen Grafiksymbol zu sehen.

Andere nützliche Links:

- [VimAwesome](https://vimawesome.com) eine Seite mit Hunderten von vim-Plugins
- [Frans "My Computing"-Repo](https://github.com/TheBeachLab/myComputing) mit einigen Tricks, wenn du gerne die Kommandozeile benutzt.


### Dokumentation in mehreren Sprachen mit KI
Seien wir ehrlich. Ich habe nicht viel Freizeit und in Kürze werde ich noch weniger Zeit haben. Deshalb brauche ich ein System, um die Dokumentation effizient zu schreiben. Ich werde eine neue Technik ausprobieren, die es mir ermöglicht, die Dokumentation in zwei (oder mehr) Sprachen zu führen. Derzeit wird der größte Teil des Textes, den du liest, auf Spanisch in meinen Mac diktiert.

![](img/w01/dictation.webp)

Das spart mir etwas Schreibzeit. Einige Teile, wie Code, muss ich manuell eingeben. Auch Korrekturen, z.B. wenn ich Links einfüge, muss ich manuell vornehmen.

So erzeuge ich Markdown-Dateien mit der Dokumentation auf Spanisch. Der Grund, warum ich sie nicht direkt auf Englisch diktiere, ist, dass mein Akzent so schlecht ist, dass der Computer mich nicht versteht. Der Name der Datei für jede Woche enthält codiert, in welcher Woche ich mich befinde und in welcher Sprache die Dokumentation ist. In diesem Fall: `w01-es.md`. Ich werde eine künstliche Intelligenz nutzen, um den Text aus dieser Datei ins Englische und Deutsche zu übersetzen und ihn als `w01-en.md` bzw. `w01-de.md` zu speichern. Das KI-Modell muss in der Lage sein, die Markdown-Syntax zu erkennen und zu respektieren. Es muss auch interne Links manipulieren können, denn Links, die zu `w02-es.md` in der spanischen Dokumentation führen, müssen in der englischen Version der Dokumentation in `w02-en.md` geändert werden. Da es möglich ist, dass sich das Modell im Laufe des Fab Academy verbessert (oder sogar wechselt), werde ich den Text auf Spanisch behalten und jede Woche die Übersetzung aller Dateien erneut durchführen. Ich werde nur die Originaldatei auf Spanisch bearbeiten. Ich werde die generierte Übersetzung nicht manuell manipulieren. Wenn also das, was du auf Englisch oder Deutsch liest, keinen Sinn macht, gib die Schuld OpenAI oder dem Modell, das ich verwende.

Ich habe César Garcia von [La Hora Maker](https://www.youtube.com/lahoramaker) gebeten, mir zu helfen, ein Modell für die Übersetzung zu finden. César hat mir empfohlen, die Whisper API von OpenAI zu nutzen, die in der Lage ist, direkt vom Spanischen ins Englische zu übersetzen. Derzeit bin ich nur an der Übersetzung interessiert, deshalb habe ich einen Assistenten in der OpenAI API mit folgenden Anweisungen erstellt:

> Übersetze den Text vom Spanischen ins Englische, lies das gesamte Dokument, um den Kontext zu verstehen, bevor du es übersetzt, berücksichtige die Nuancen und Idiome der spanischen Sprache und übersetze sie in gleichwertige Ausdrücke im Englischen. Die Übersetzung sollte nicht wörtlich sein, konzentriere dich darauf, die ursprüngliche Bedeutung zu bewahren und eine Übersetzung zu liefern, die auf Englisch Sinn macht. Ignoriere externe URLs und Code-Snippets in der Übersetzung; wenn du auf einen Markdown-Link stößt, übersetze den Text in den Klammern. Ändere interne Markdown-Link-URLs, um auf die entsprechende englische Datei zu zeigen, z.B. ändere w01-es.md in w01-en.md. Behalte Marken und Namen in der Übersetzung bei. Verwende die korrekte Grammatik und Syntax im Endtext. Der Stil der Übersetzung sollte informell sein.

Es gibt ein anderes Modell für Deutsch mit analogen Anweisungen. Ich ändere die Anweisungen gelegentlich, um die Übersetzung zu verbessern.

Diese Seite, die du liest, hat etwa 2000 Tokens. Du kannst herausfinden, wie viele Tokens ein Text hat, indem du den [OpenAI Tokenizer](https://platform.openai.com/tokenizer) benutzt. Die Kosten für die Übersetzung betragen ungefähr 8 Cent, wenn man bedenkt, dass 1000 Tokens 0,01 USD für den Input und 0,03 USD für den Output kosten. Das mag wenig erscheinen, aber die Kosten werden steigen, je weiter das Fab Academy fortschreitet.

In meiner Wunschliste werde ich weiterhin nach einem lokalen Modell suchen.

### Automatisierung des Übersetzungsprozesses
Am Anfang benutzte ich das API-Fenster von OpenAI. Nun habe ich diesen Prozess automatisiert und nutze Python in der Kommandozeile. Mit einer Mischung aus Bing Copilot und der kostenlosen Version von ChatGPT bat ich darum, die OpenAI-Bibliothek für die Übersetzung zu nutzen. Nach viel Hin und Her (die KI generiert selten im ersten Anlauf korrekten Code) endete ich frustriert und beschimpfte Bing.

![](img/w01/bing.webp)

Letztendlich musste ich die API-Dokumentation lesen, um das Programm zum Laufen zu bekommen.

Bevor ich die modifizierten Seiten übersetze, muss ich sie mit `git add` hinzufügen. Dadurch kann ich die Kosten begrenzen und kontrollieren. Danach führe ich einfach `python translate-en.py` aus und das Skript erzeugt die ins Englische übersetzten Markdown-Seiten. Dasselbe mache ich für Deutsch.

Normalerweise führe ich diesen Schritt nicht isoliert durch, da ich ihn im nächsten Schritt integriert habe.

### Automatisierung der HTML-Erstellung und des Datei-Uploads
Die Dokumentation der Fab Academy muss in Form einer Webseite präsentiert werden. Um die HTML-Seiten aus den Markdown-Dateien zu erstellen, habe ich ein Skript von Bash nach Python übersetzt, das ich für das Programm [FabZero](https://github.com/Academany/fabzero) erstellt habe. Der Code konvertiert alle `.md` Dateien in `.html`, indem er [Pandoc](https://pandoc.org/index.html) mit einem [CSS-Style-Template](base.css) nutzt. Während der Konvertierung, wenn es auf einen Link zu einer Markdown-Datei stößt, wird dieser in einen Link zu der entsprechenden HTML-Datei umgewandelt, indem [dieser LUA-Filter](../links-to-html.lua) verwendet wird.

Das Skript automatisiert optional auch die Übersetzung aus dem vorherigen Abschnitt und den Upload der Dateien auf Github. Also, wenn ich meinen Fortschritt hochladen möchte, schreibe ich:

`python auto.py --translate updating week 1`

Auf diese Weise übersetzt das Skript die Seiten, wenn es `--translate` unter den Argumenten findet. Es konvertiert auch alle Seiten in HTML und lädt anschließend alles auf Github hoch, solange es eine Nachricht gibt, in diesem Fall ist es `updating week 1`. Wenn es keine Nachricht gibt, führt es keines der Prozesse in Bezug auf git durch.

Du kannst das Skript hier sehen: [auto.py](../auto.py)

### Nutzung von CD/CI in Github zum Bereitstellen der Webseiten

Schauen wir mal, was ich jetzt auf Github habe:

- Meine originalen `.md` Dateien auf Spanisch
- Die von KI ins Englische und Deutsche übersetzten `.md` Dateien
- Die `.html` Seiten aller `.md` Dateien, die von Pandoc erstellt wurden.

Das Einzige, was jetzt noch fehlt, ist ein Webserver. Und das kannst du von Github aus machen, indem du zu den Einstellungen des Repositories gehst.

![](img/w01/cicd.webp)

Dies wird eine Datei in `.github/workflows/static.yml` erstellen, von der ich nur den `runner` ändern musste, denn `runs-on: ubuntu-latest` funktionierte nicht. Ich habe es auf `runs-on: ubuntu-22.04` geändert und nach dem `commit` wurden die Seiten automatisch bereitgestellt.

### Endergebnis

[https://thebeachlab.github.io/backtofabacademy2024/](https://thebeachlab.github.io/backtofabacademy2024/)

### Fazit
All dies macht das Schreiben der Dokumentation im Moment etwas langsam und ein wenig mühsam. Aber ich glaube, dass mit diesem System die Geschwindigkeit von Woche zu Woche drastisch zunehmen wird und ich am Ende in der Lage sein werde, mit großer Geschwindigkeit und Detailgenauigkeit zu dokumentieren.

Außerdem glaube ich, dass diese Methode vielen Menschen helfen wird, die ihr Talent nicht zeigen können, weil sie eine andere Sprache nicht beherrschen. Es ist ungerecht, dass dies passiert, und ich hoffe, dass die KI Menschen dabei hilft zu zeigen, wie wertvoll sie sind.

## Git: Dieser endlose Abgrund
Man könnte denken, dass ich nach 10 Jahren Nutzung von git alles über dieses Versionskontrollsystem wüsste. Weit gefehlt. Das sind die Dinge, die ich während dieses Fab Academy-Zyklus verbessern möchte:

- Meine Tendenz zur Unterdrückung, Änderungen in den Hauptzweig hochzuladen. Normalerweise passiert nichts, aber ich muss mich daran gewöhnen, für jede Änderung einen neuen Zweig zu erstellen.

(fortzusetzen...)

## Projektmanagement
(fortzusetzen...)

## Skizze des Endprojektes
Alles rund um das Endprojekt habe ich in den [entsprechenden Abschnitt](final-es.md) verschoben.

[<< Zurück zum Anfang](index-es.md)  
[Nächste Woche >>](w02-es.md)