---
title: "Woche 1. Prinzipien und Praktiken, Projektmanagement"
subtitle: "Zurück zum Fab Academy 2024. Fran Sanchez"
toc-title: "Inhaltsverzeichnis"
lang: de-DE
---
:::{.note .yellow}
|     |
| --- |
| *Aufgabe A:* |
| Plane und skizziere ein potenzielles Abschlussprojekt.  |
|     |
| *Aufgabe B:* |
| Erstelle ein Schritt-für-Schritt-Tutorial für Git. |
| Erstelle eine persönliche Website im Klassenrepository, auf der du dich und dein Abschlussprojekt beschreibst. |
:::

## Meine Umgebung

### Ich nutze wieder macOS – Wie konnte ich nur so tief sinken?
Mal sehen, wie ich das erkläre... Eines anderen Tages werde ich es erklären.

### Meine Tastatur ist seltsam
Ich konnte nie wirklich Maschinenschreiben, obwohl ich es immer lernen wollte. Während ich bei der Organisation von Fab15 in Ägypten arbeitete, fiel mir auf, dass Sherry Lassiter sehr geschickt im Maschinenschreiben ist. In dem Moment entschied ich mich zu lernen. Wenn man etwas von Grund auf neu lernt, hat man den Vorteil, keine schlechten Angewohnheiten zu übernehmen. Deshalb lernte ich nicht das QWERTY-System, das ursprünglich entworfen wurde, um das Verklemmen alter Schreibmaschinen zu verhindern. Ich lernte mit dem [Colemak](https://colemak.com)-System. Colemak ist so gestaltet, dass die am häufigsten genutzten Buchstaben im Englischen in der mittleren Reihe liegen. Ich besitze eine [ortho-lineare Tastatur](https://drop.com/buy/preonic-mechanical-keyboard), auf die ich das Colemak-Layout aufgespielt habe, und ich übe etwa fünf Minuten am Tag. Was mir am Colemak-Layout am besten gefällt, ist, dass die Rücktaste links neben der Taste `A` liegt.

![](../../img/w01/preonic.webp)

Außerdem habe ich eine [Software unter macOS](https://karabiner-elements.pqrs.org), die meine Tastaturbelegung auf Colemak ändert und die Funktion der Feststelltaste als Rücktaste umsetzt.

### Mein Texteditor ist auch seltsam
Ich beabsichtige, ausschließlich `vim`, einen Texteditor für die Kommandozeile, zu verwenden. Ich habe einige Grundkenntnisse in `vim` und möchte mein Wissen vertiefen. Ich mag die Idee, ausschließlich die Tastatur für das Texteditieren zu verwenden. Um der Versuchung zu widerstehen, Visual Studio Code zu nutzen, habe ich es deinstalliert. Von Haus aus ist der Texteditor vim recht spartanisch. Deshalb werde ich einige Plugins installieren. Hier ist eine Liste, die ich mit der Zeit erweitern werde:

- [NERDTree](https://github.com/preservim/nerdtree) für eine Seitenleiste mit einer Dateiliste, was das schnelle Navigieren zwischen Dateien ermöglicht.
- [vim-devicons](https://github.com/ryanoasis/vim-devicons) um Dateien und Ordner mit kleinen grafischen Symbolen darzustellen.

Weitere nützliche Links:

- [VimAwesome](https://vimawesome.com) ist eine Webseite mit hunderten von vim-Plugins
- [Frans My Computing Repo](https://github.com/TheBeachLab/myComputing) mit einigen Tricks, falls du gerne die Kommandozeile nutzt.

## Meine Dokumentationsprozesse neu erfinden
Ich muss realistisch sein. Ich habe nicht viel Freizeit und bald werde ich noch weniger davon haben. Daher benötige ich ein System, das mir ermöglicht, Dokumentationen flink zu verfassen. Ich werde ein neues System zum Dokumentieren ausprobieren. Als unerwarteten Vorteil wird mir dieses System ermöglichen, die Dokumentation in zwei (oder mehr) Sprachen zu haben.

### Markdown nutzen

Hier will ich nicht zu sehr innovieren. Die Strategie, die mir schon seit vielen Jahren sehr gut funktioniert, ist das Schreiben von Inhalten in einer einfachen Textdatei in einem Format namens [Markdown](https://www.markdownguide.org) `.md`. Auf diese Weise konzentriere ich mich ausschließlich auf das Schreiben des Inhalts. Vorteile des Schreibens in Markdown:

- Du brauchst kein spezielles Programm, um Plain Text zu schreiben. Du kannst es sogar von Hand schreiben, wenn du eine gute Handschrift hast, und es danach einscannen.
- Es ist leicht zu schreiben; du musst nicht deine Finger verrenken, um `</h1>` und solche Dinge zu tippen.
- Es ist einfach, Stile anzuwenden und den Text zu organisieren.
- Es kann gelesen werden, ohne dass es aussieht, als würdest du die Matrix entschlüsseln.

![Wenn du deine Seite vom HTML-Code aus lesen kannst](../../img/w01/code.webp)

Die Dokumentation für das Fab Academy muss in Form einer Webseite präsentiert werden. Es gibt ein Kommandozeilenprogramm namens [Pandoc](https://pandoc.org/index.html), das buchstäblich jedes Textformat umwandeln kann. Ich werde es nutzen, um die `.md` Dateien in "ansehnliche" `.html` Seiten mithilfe einer CSS-Stilvorlage umzuwandeln.

> Anmerkung: "Ansehnlich" bezieht sich auf leicht lesbar. Andere Leute schätzen das visuelle Erscheinungsbild der Seite über alles und ziehen es vor, Zeit damit zu verbringen, ihr eigenes Kunstwerk zu erschaffen. Ich wünsche ihnen alles Gute.

Ich benutze [diese CSS-Vorlage](https://jez.io/pandoc-markdown-css-theme/), die es mir erlaubt, Funktionen wie Gleichungen, Tabellen, Zeilennummern im Code, Randnotizen usw. hinzuzufügen.

### Zeit sparen durch Diktieren
Der größte Teil des Textes, den du gerade liest, wurde **auf Spanisch** in eine Markdown-Datei diktiert. Der Grund, warum ich es nicht direkt auf Englisch diktiere, ist, dass mein Akzent so schlecht ist, dass mich der Computer nicht versteht. Zum Diktieren verwende ich das Diktierwerkzeug von macOS.

![](../../img/w01/dictation.webp)

Ich mag dieses Tool wirklich sehr, weil:

- Es überall im Betriebssystem funktioniert, einschließlich des Terminals.
- Du kannst sprechen und Pausen von bis zu 30 Sekunden machen, ohne dass es sich trennt.
- Du kannst den Text während des Diktierens bearbeiten.
- Du kannst Emojis hinzufügen 😊
- Es fügt automatisch Satzzeichen hinzu, und du kannst sie auch manuell einfügen.
- Du kannst auch durch Sagen die Zeile und den Absatz wechseln.
- Wenn du einen Apple Silicon Prozessor hast, versteht es den Kontext und korrigiert sich selbst. All das offline.
- Ich kann es benutzen, während ich Musik über meine Kopfhörer höre.

Hier ist die vollständige Liste der Befehle auf [Spanisch](https://support.apple.com/es-es/guide/mac-help/mh40695/14.0/mac/14.0), [Englisch](https://support.apple.com/en-gb/guide/mac-help/mh40695/14.0/mac/14.0) und [Deutsch](https://support.apple.com/de-de/guide/mac-help/mh40695/14.0/mac/14.0). Das spart mir etwas Zeit beim Schreiben. Einige Teile muss ich manuell schreiben, zum Beispiel, wenn ich Code schreibe oder Links einfüge. Auch einige Korrekturen muss ich manuell machen.

### Dateistruktur

So erzeuge ich Markdown-Dateien mit der Dokumentation auf Spanisch. Zuerst schrieb ich den Text jeder Woche in einer einzigen Datei. Aber wie du später lesen wirst, benutze ich einen bezahlten Service für die Übersetzung. Jedes Mal, wenn ich eine Zeile bearbeitete, musste ich das gesamte Dokument neu übersetzen lassen. Um die Kosten zu reduzieren, teile ich die Woche jetzt in Kapitel auf und erstelle eine Datei für jedes Kapitel. Auf diese Weise werden nur die Kapitel übersetzt, die ich geändert habe. Meine Dateistruktur ist inspiriert von der Programmiersprache [BASIC](https://en.wikipedia.org/wiki/BASIC):

```
/documentation
    /es
        /md
            /w01
                w01-kapitel-00-es.md
                w01-kapitel-10-es.md
                w01-kapitel-20-es.md
                w01-kapitel-21-es.md
                ...
                w01-kapitel-90-es.md
                w01-kapitel-99-es.md
```

Der Name der Datei jeder Woche enthält kodiert die Woche, in der ich mich befinde, das Kapitel und die Sprache der Dokumentation. Das Kapitel 00 ist die Einleitung. Ich verwende die Kapitel 10, 20, 30... um die Abschnitte der Woche zu entwickeln. Wenn ein Kapitel sehr lang ist, unterteile ich es mit den Zwischennummern: 20, 21, 22, usw. Das Kapitel 90 ist immer der Abschluss und 99 der Fußtext.

Später füge ich alle Kapitel der Woche in einer einzigen Datei zusammen, in diesem Fall: `w01-es.md`.

> **Wichtige Anmerkung:** Ich bearbeite niemals manuell die zusammengefügte Datei. Ich bearbeite immer nur die einzelnen Kapitel separat.

### Automatische Übersetzungen mit KI
Im Fab Academy muss die Dokumentation auf Englisch sein. Traditionelle Sprachübersetzer sind ziemlich schlecht. Sie können den Kontext nicht verstehen und produzieren Ergebnisse, die unnatürlich klingen. Ich werde eine künstliche Intelligenz verwenden, um den Text der Kapitel ins Englische und auch ins Deutsche zu übersetzen.

Das KI-Modell muss in der Lage sein, die Markdown-Syntax zu erkennen und sie zu respektieren. Es muss auch interne Links bearbeiten, da Links, die in der spanischen Dokumentation zu `w02-es.md` führen, in der englischen Version der Dokumentation zu `w02-en.md` geändert werden müssen. Es ist möglich, dass sich das Modell im Laufe des Fab Academy verbessert (oder sogar ändert). Deshalb werde ich den Text auf Spanisch behalten und die Übersetzung aller Dateien von Zeit zu Zeit erneut durchführen. Ich werde nur die Dateien auf Spanisch bearbeiten. Ich werde keine manuellen Änderungen an den generierten Übersetzungen vornehmen. Also, wenn das, was du auf Englisch oder Deutsch liest, keinen Sinn ergibt, gib OpenAI oder welches Modell auch immer ich verwende, die Schuld.

Ich habe César Garcia von [La Hora Maker](https://www.youtube.com/lahoramaker) gebeten, mir bei der Suche nach einem Modell für die Übersetzung zu helfen. César empfahl mir, die Whisper API von OpenAI zu verwenden, die in der Lage ist, direkt vom spanischen Audio zu übersetzen. Vorläufig bin ich nur an der Übersetzung interessiert, also habe ich einen Assistenten in der OpenAI API mit diesen Anweisungen erstellt:

```
Translate the text from Spanish to English. Lies das gesamte Dokument, um den Kontext zu verstehen, bevor du es übersetzt, berücksichtige Nuancen und Idiome der spanischen Sprache und übersetze sie in die entsprechenden englischen Ausdrücke. Die Übersetzung sollte nicht wörtlich sein, konzentriere dich darauf, die ursprüngliche Bedeutung zu bewahren und eine Übersetzung zu liefern, die auf Englisch Sinn ergibt. Ignoriere externe URLs und Code-Snippets in der Übersetzung; wenn du auf einen Markdown-Link stößt, übersetze den Text innerhalb der eckigen Klammern. Ändere interne Markdown-Link-URLs, um auf die entsprechende englische Datei zu zeigen, z. B. ändere w01-es.md in w01-en.md. Erkenne und behalte Marken und Namen ohne Übersetzung. Verwende korrekte Grammatik und Syntax im endgültigen Text. Der Stil der Übersetzung sollte informell sein.
```

Ich habe ein anderes Modell auf Deutsch mit ähnlichen Anweisungen. Ich wechsle die Anweisungen von Zeit zu Zeit, um die Übersetzung zu verbessern.

Diese Seite, die du gerade liest, hat etwa 4000 Token. Du kannst herausfinden, wie viele Token ein Text hat, indem du den [OpenAI Tokenizer](https://platform.openai.com/tokenizer) verwendest. Die Kosten für die Übersetzung dieser Seite in beide Sprachen betragen etwa 0,32 USD, wenn man bedenkt, dass jedes 1000 Token 0,01 USD für das Input und 0,03 USD für das Output kostet. Das erscheint mir ziemlich teuer, und außerdem werden die Kosten steigen, je weiter das Fab Academy fortschreitet. Aus diesem Grund werde ich die Inhalte nur übersetzen, wenn ich die Arbeit für weit fortgeschritten halte.

Bis jetzt sind die Übersetzungen ziemlich gut. Manchmal ändert sie die Links nicht korrekt, daher werde ich diese Aufgabe in Zukunft mit einem Skript durchführen, das zuverlässiger ist. Ich habe [Sophia Döring](https://fabacademy.org/2024/labs/kamplintfort/students/sophia-doring/) gebeten, auch die deutsche Übersetzung zu überprüfen. Sie sagte, dass sie im Allgemeinen auch ziemlich gut sei, obwohl sie manchmal wenig gebrauchte deutsche Wörter verwendet, insbesondere wenn es um technische Begriffe geht. Das könnte durch die Art und Weise verursacht sein, wie ich den ursprünglichen Text schreibe. Ich verwende spanische Äquivalente für technische Begriffe, die ich im Alltag tatsächlich auf Englisch sage.

Auf meiner Wunschliste werde ich weiterhin nach einem lokalen Modell suchen. Auf diese Weise könnte ich die Inhalte häufiger übersetzen. Bisher habe ich die Modelle `Phi 2` und `Yarn Mistral` mit katastrophalen Ergebnissen ausprobiert.

### Automatisierung des Übersetzungsprozesses
Zuerst habe ich die OpenAI API direkt benutzt. Jetzt habe ich diesen Prozess mit Python in der Befehlszeile automatisiert. Mit einer Kombination aus Bing Copilot und der kostenlosen Version von ChatGPT bat ich um ein Programm, das mithilfe der OpenAI-Bibliothek die Übersetzung automatisierte. Das hat allerdings nicht gut geklappt. Nach einigem Hin und Her (KI generiert nicht immer beim ersten Mal korrekten Code) war ich am Ende frustriert und habe Bing beschimpft.

![](../../img/w01/bing.webp)

Schließlich musste ich die Dokumentation der API lesen, um das Programm zum Laufen zu bringen.

Um unnötige Kosten zu vermeiden, übersetzt das Skript nur die Kapitel auf Spanisch, die ich mit `git add` hinzugefügt habe. Dadurch kann ich die Kosten besser kontrollieren. Danach führe ich einfach `python translate-en.py` aus, und das Skript erzeugt die ins Englische übersetzten Markdown-Seiten. Dasselbe mache ich für Deutsch.

Eigentlich führe ich die Übersetzung nicht isoliert durch, da ich sie in den nächsten Schritt integriert habe.

### Den gesamten Prozess automatisieren
Um den kompletten Prozess zu automatisieren, habe ich ein Bash-Skript, das ich für das Bildungsprogramm [FabZero](https://github.com/Academany/fabzero) erstellt habe, in Python umgewandelt. Ich gebe folgendes ein:

`python auto.py --translate updating week 1`

Das Skript übersetzt die bearbeiteten Kapitel, wenn es `--translate` unter den Argumenten findet. Das mache ich, um Kosten zu sparen. Danach fügt es alle Kapitel zusammen und erstellt eine einzige Markdown-Datei für jede Woche. Der nächste Schritt ist die Konvertierung all dieser Dateien in HTML. Während der Konversion, wenn es auf einen Link zu einem Markdown-Dokument stößt, konvertiert es diesen in einen Link zu dem entsprechenden HTML-Dokument mit [diesem LUA-Filter](../../../links-to-html.lua). Schließlich lädt es alles auf Github hoch, vorausgesetzt es gibt eine Nachricht, die in diesem Fall `updating week 1` ist. Wenn es keine Nachricht gibt, führt es keinen der Prozesse im Zusammenhang mit git durch.

Du kannst das Skript hier analysieren: [auto.py](../../../auto.py)

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

## Git: Dieses bodenlose Loch
Man könnte denken, dass ich nach 10 Jahren Gebrauch von Git alles über dieses Versionierungssystem weiß. Weit gefehlt. Hier sind die Dinge, an denen ich während des Fab Academy-Zyklus arbeiten möchte:

- Meine Neigung unterdrücken, Änderungen direkt in den Hauptzweig hochzuladen. Normalerweise passiert nichts Schlimmes, aber ich muss mich daran gewöhnen, für jede Änderung einen neuen Zweig zu erstellen.
- ~~Die~~ Mich von Neils [Aliasen](http://academy.cba.mit.edu/classes/project_management/archive.html) inspirieren lassen, um Git-Befehle schneller auszuführen.

(Ich könnte im Laufe des Fab Academy noch mehr hinzufügen...)

## Projektmanagement

Ich möchte erklären, wie ich meine Projekte manage. Wenn man keinen Chef hat und niemand einem sagt, was zu tun ist, muss man sehr diszipliniert sein. Andernfalls kann man leicht in eine negative Spirale geraten.

Das Wichtigste ist, **zu wissen, wohin man geht**. Denn wenn man das nicht weiß, hat man ein ernsthaftes Problem. Manchmal wirst du dich im Fab Academy (und in deinem Leben) verloren fühlen. Du weißt nicht, was du machen willst, hast auf nichts Lust und es scheint, als wärst du in Zeitlupe unterwegs, während die Welt an dir vorbeirast. Wenn dir das passiert, denk an [Phil Stutz](https://www.thetoolsbook.com). Investiere in dich selbst: Mach Sport, knüpfe Kontakte zu anderen Menschen, schreibe deine Erinnerungen in ein Tagebuch. Mir hilft es und ich bin überzeugt, dass es auch dir helfen wird. Bald wirst du deinen Polarstern sehen. Setz Kurs auf ihn.

Das Zweite ist, **zu lernen, wie man Dinge reduziert und vereinfacht**. Eines deiner größten Probleme im Fab Academy wird ähnlich sein: Du findest ein Foto nicht, von dem du sicher bist, dass du es mal hattest. Du weißt nicht, ob es in den Fotos auf dem Handy, auf Google Drive oder auf dem USB-Stick ist, ob du es auf den Computer übertragen oder jemand es dir über WhatsApp geschickt hat... Vereinfache. Reduziere.

Und zuletzt, und das halte ich für das Wichtigste. Das echte Geheimnis, um irgendetwas zu erreichen, egal wie schwierig es ist, besteht darin, **viele sehr kleine Schritte zu machen**. Du löst ein kleines Problem, dann ein weiteres und danach noch eins. So funktioniert es.

Was Werkzeuge zur Unterstützung des Managements angeht, habe ich einige ausprobiert. Also fange ich mit denen an, die für mich nicht funktionieren:

- Post-it-Notizen an der Wand. Die Idee ist gut. Sehr visuell und agil. Aber es gibt zwei Probleme. Erstes Problem: In Barcelona ist es oft sehr heiß und die Notizen fallen ab. Zweites Problem: Wenn ich die Wand nicht sehe, gibt es kein Projekt.
- Kanban-ähnliche Software. Sie versuchen, wie Post-it-Notizen zu sein. Ich benutze sie nicht, weil: Sie scheinen mir kompliziert und lassen mich nicht zeichnen.
- Microsoft Project und Ähnliches. Ohne Kommentar.
- Webservice-Plattformen wie Notion.com, Monday.com und Ähnliches. Ich werde keine Sekunde meines kostbaren Lebens damit verschwenden, herauszufinden, wie ein Dienst funktioniert, der nur auf TikTok leicht aussieht und der wahrscheinlich morgen Nachmittag schon wieder geschlossen wird.

Jetzt benutze ich eine Kombination aus reinem Text für langfristige Ziele, Erinnerungen für mittelfristige Ziele und Apples Freeform für Aufgaben, die ich heute erledigen werde. Freeform ist ein Programm mit unendlicher Leinwand, ähnlich wie [Miro](https://miro.com). Es hat die Vorteile von Post-it-Notizen ohne deren Nachteile. Ich kann es anpassen und mein eigenes System schaffen. Zum Beispiel habe ich das Feld `DOING NOW` erstellt, in das nur eine Notiz passt. Das ist für mich wichtig, weil ich jeweils nur eine Sache zur Zeit machen kann. Außerdem kann ich von Hand zeichnen, was mir gefällt. Wahrscheinlich werde ich ein Video machen, um alles detaillierter zu erklären.

![](../../img/w01/freeform.webp)

## Skizze des Abschlussprojekts
Alles, was das Abschlussprojekt betrifft, habe ich in den [entsprechenden Abschnitt](final-de.md) verschoben.

## Fazit
All das macht das Schreiben der Dokumentation derzeit langsam und ein wenig mühsam. Aber ich glaube, dass mit diesem System **die Geschwindigkeit von Woche zu Woche drastisch zunehmen wird** und ich am Ende in der Lage sein werde, mit großer Geschwindigkeit und Detailliertheit zu dokumentieren.

Ich glaube auch, dass diese Methode **vielen Menschen helfen wird**, die ihr Talent nicht **ausdrücken können**, weil sie eine andere Sprache nicht beherrschen. Es ist unfair, dass das passiert. Ich hoffe, dass AI den Menschen helfen wird, zu zeigen, wie wertvoll sie sind.

[← Zurück zum Anfang](index-de.md)  

