# Woche 1: Prinzipien und Praktiken, Projektmanagement

> *Aufgabe A:*
>
> Plane und skizziere ein mögliches Abschlussprojekt.
>
> *Aufgabe B:*
>
> Führe ein Schritt-für-Schritt-Tutorial zu Git durch.
> Erstelle eine persönliche Website im Klassenrepository, um dich und dein Abschlussprojekt zu beschreiben.

## Die Art der Dokumentation neu erfinden

### macOS wieder? Wie konntest du nur so tief sinken?
Mal sehen, wie ich das erkläre... Ich erkläre es ein anderes Mal.

### Colemak?
Ich konnte nie Maschinenschreiben, obwohl ich es immer lernen wollte. Während ich bei der Organisation von Fab15 in Ägypten mitarbeitete, bemerkte ich, dass Sherry Lassiter eine großartige Fähigkeit zum Maschinenschreiben hat. In jenem Moment entschied ich mich zu lernen. Wenn du etwas von Grund auf neu lernst, hast du den Vorteil, dass du keine schlechten Gewohnheiten hast. Also habe ich nicht das QWERTY-System gelernt, welches ursprünglich entworfen wurde, um zu verhindern, dass die Tasten alter Schreibmaschinen klemmen. Ich habe mit dem [Colemak](https://colemak.com)-System gelernt. Colemak ist so gestaltet, dass die am häufigsten genutzten Buchstaben in der englischen Sprache in der mittleren Reihe sind. Ich habe eine [ortholineare Tastatur](https://drop.com/buy/preonic-mechanical-keyboard), auf der ich das Colemak-Layout habe, und ich übe etwa fünf Minuten am Tag. Was mir an der Colemak-Anordnung am besten gefällt, ist, dass die Rücktaste neben der Taste `A` ist.

![](img/w01/preonic.webp)

Außerdem habe ich eine [Software auf macOS](https://karabiner-elements.pqrs.org), die meine Tastaturbelegung auf Colemak umstellt und auch die Funktion der Caps Lock-Taste durch das Rückwärtslöschen ersetzt.

### Mein Texteditor
Ich beabsichtige, ausschließlich einen Texteditor in der Kommandozeile zu verwenden. Ich habe einige Grundkenntnisse in `vim` und möchte mein Wissen vertiefen. Ich mag die Idee, ausschließlich die Tastatur zum Texteditieren zu verwenden. Um der Versuchung zu widerstehen, Visual Studio Code zu benutzen, habe ich es deinstalliert. Der Texteditor vim ist ursprünglich recht spartanisch. Deshalb werde ich einige Plugins installieren. Hier ist eine Liste, die ich im Laufe der Zeit erweitern werde:

- [NERDTree](https://github.com/preservim/nerdtree) um eine Seitenleiste mit einer Dateiliste zu haben, sodass ich schnell zwischen Dateien navigieren kann.
- [vim-devicons](https://github.com/ryanoasis/vim-devicons) um Dateien und Ordner mit kleinen grafischen Icons zu visualisieren.

Weitere hilfreiche Links:

- [VimAwesome](https://vimawesome.com) ist eine Webseite mit hunderten von vim-Plugins
- [Frans Computing Repo](https://github.com/TheBeachLab/myComputing) mit einigen Tricks, wenn du gerne die Kommandozeile benutzt.

### Mehrsprachige Dokumentation mit KI
Mal realistisch betrachtet. Ich habe nicht viel Freizeit und bald werde ich noch weniger Zeit haben. Also brauche ich ein System, um die Dokumentation effizient zu schreiben. Ich werde eine neue Technik ausprobieren, mit der ich die Dokumentation in zwei (oder mehr) Sprachen verfassen kann. Der größte Teil des Textes, den du gerade liest, wird auf Spanisch in meinen Mac diktiert.

![](img/w01/dictation.webp)

Das spart mir etwas Zeit beim Schreiben. Einige Teile, wie Code, muss ich manuell eintippen. Ich muss auch manuelle Korrekturen vornehmen, zum Beispiel, wenn ich Links einfüge.

So erzeuge ich Markdown-Dateien mit der Dokumentation auf Spanisch. Der Grund, warum ich es nicht direkt auf Englisch diktiere, ist, dass mein Akzent so schlecht ist, dass der Computer mich nicht versteht. Der Name der Datei für jede Woche enthält codiert, in welcher Woche ich mich befinde und in welcher Sprache die Dokumentation vorliegt. In diesem Fall: `w01-es.md`. Ich werde eine künstliche Intelligenz nutzen, um den Text der Datei in Englisch und Deutsch zu übersetzen und es als `w01-en.md` und `w01-de.md` zu speichern. Das KI-Modell muss in der Lage sein, die Markdown-Syntax zu erkennen und zu respektieren. Es muss auch interne Links handhaben können, denn Links, die zu `w02-es.md` in der spanischen Dokumentation führen, müssen in der englischen Version der Dokumentation in `w02-en.md` geändert werden. Da das Modell sich im Laufe des Fab Academy verbessern könnte (oder sogar wechseln), werde ich den spanischen Text behalten und die Übersetzung aller Dateien jede Woche erneut durchführen. Ich werde nur die ursprüngliche Datei auf Spanisch bearbeiten. Ich werde die erzeugte Übersetzung nicht manuell bearbeiten. Sollte also das, was du auf Englisch oder Deutsch liest, keinen Sinn ergeben, gib OpenAI oder dem Modell, das ich benutze, die Schuld.

Ich habe César Garcia von [La Hora Maker](https://www.youtube.com/lahoramaker) gefragt, ob er mir dabei helfen kann, ein Modell für die Übersetzung zu finden. César hat mir empfohlen, die Whisper API von OpenAI zu nutzen, die in der Lage ist, direkt vom Spanischen ins Englische zu übersetzen. Im Moment bin ich nur an der Übersetzung interessiert, daher habe ich einen Assistenten in der OpenAI-API mit folgenden Anweisungen erstellt:

> Übersetze den Text vom Spanischen ins Deutsche, berücksichtigt Nuancen und Idiome. Lies das gesamte Dokument, um den Kontext zu verstehen, bevor du übersetzt, und halte die ursprüngliche Bedeutung auch dann bei, wenn sie nicht wörtlich ist. Ignoriere URLs und Code-Schnipsel in der Übersetzung; triffst du auf einen Markdown-Link, übersetze den Text innerhalb der eckigen Klammern. Modifiziere interne Markdown-Link-URLs, um auf die entsprechende englische Datei zu zeigen, z.B. ändere w01-es.md zu w01-en.md. Erkenne und behalte Marken und Namen ohne Übersetzung bei. Großschreibung von Titeln im endgültigen Text. Der Stil der Übersetzung sollte informell sein.

Für Deutsch gibt es ein ähnliches Modell mit analogen Anweisungen. Ich ändere die Anweisungen von Zeit zu Zeit, um zu versuchen, die Übersetzung zu verbessern.

Diese Seite, die du gerade liest, hat etwa 2000 Tokens. Du kannst herausfinden, wie viele Tokens ein Text hat, indem du den [OpenAI Tokenizer](https://platform.openai.com/tokenizer) verwendest. Die Kosten für die Übersetzung betragen ungefähr 8 Cent pro Seite, wenn man bedenkt, dass jeder 1000 Tokens 0,01 USD für die Eingabe und 0,03 USD für die Ausgabe kosten. Es mag wenig erscheinen, aber die Kosten werden steigen, je weiter Fab Academy fortschreitet.

Auf meiner Wunschliste steht weiterhin ein lokales Modell zu finden.

### Automatisierung des Übersetzungsprozesses
Anfangs habe ich das API-Fenster von OpenAI verwendet. Jetzt habe ich diesen Prozess automatisiert, indem ich Python in der Kommandozeile verwende. Mit einer Mischung aus Bing Copilot und der kostenlosen Version von ChatGPT bat ich darum, die OpenAI-Bibliothek für die Übersetzung zu verwenden. Nach einigem Hin und Her (die KI generiert selten beim ersten Mal korrekten Code) endete ich frustriert und beschimpfte Bing.

![](img/w01/bing.webp)

Letztendlich musste ich die Dokumentation der API lesen, um das Programm zum Laufen zu bringen.

Bevor ich die Seiten, die ich geändert habe, übersetze, muss ich sie mit `git add` hinzufügen. Dadurch kann ich die Kosten begrenzen und kontrollieren. Danach führe ich einfach `python translate-en.py` aus und das Script generiert die ins Englische übersetzten Markdown-Seiten. Das Gleiche mache ich für Deutsch.

### Automatisierung der Erstellung von HTML und des Hochladens von Dateien
Ich habe ein Skript in Bash, das ich für das [FabZero](https://github.com/Academany/fabzero)-Programm erstellt hatte, in Python übersetzt. Der Code konvertiert alle `.md`-Dateien in `.html` mit [Pandoc](https://pandoc.org/index.html). Während der Konvertierung, wenn es auf einen Link zu einem Markdown-Dokument stößt, konvertiert es diesen in einen Link zu seinem entsprechenden HTML-Dokument mithilfe [dieses LUA-Filters](../links-to-html.lua). Du kannst das Skript hier sehen: [auto.py](../auto.py)

Das Skript automatisiert auch den Git-Prozess. So, wenn ich meinen Fortschritt hochladen will, schreibe ich:

`python auto.py updating week 1`

Und das konvertiert alle Seiten in HTML und lädt alles auf Github hoch mit der Nachricht `updating week 1`.

### Fazit
All dies macht das Schreiben der Dokumentation momentan ein wenig langsam und etwas mühsam. Aber ich glaube, dass mit diesem System die Geschwindigkeit drastisch von Woche zu Woche zunehmen wird und ich am Ende in der Lage sein werde, mit großer Geschwindigkeit und Detailgenauigkeit zu dokumentieren.

## Git: dieses unendliche Rätsel
Man könnte denken, dass ich, da ich Git seit 10 Jahren benutze, alles darüber wüsste, was es über dieses Versionskontrollsystem zu wissen gibt. Weit gefehlt. Dies sind die Dinge, die ich während dieses Fab Academy-Zyklus verbessern möchte:

- Meine Tendenz unterdrücken, Änderungen auf den Hauptzweig hochzuladen. Normalerweise passiert nichts Schlechtes, aber ich muss mich daran gewöhnen, für jede Änderung einen neuen Zweig zu erstellen.

(Fortsetzung folgt...)

## Projektmanagement
(Fortsetzung folgt...)

## Skizze des Abschlussprojekts
Alles, was mit dem Abschlussprojekt zu tun hat, habe ich in den [entsprechenden Abschnitt](final-de.md) verschoben.

[<< Zurück zum Anfang](index-de.md)  
[Nächste Woche >>](w02-de.md)