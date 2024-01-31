# Woche 1. Prinzipien und Praktiken, Projektmanagement

 > *Aufgabe A:*
 >
 > Plane und skizziere ein potentielles Abschlussprojekt.
 >
 > *Aufgabe B:*
 >
 > Mache ein Schritt-für-Schritt-Tutorial zu Git.  
 > Erstelle eine persönliche Website im Klassen-Repository, die dich und dein Abschlussprojekt beschreibt.


## Ich erfinde meinen Dokumentationsprozess neu

### Ich benutze wieder macOS – Wie konnte es nur so weit kommen?
Mal sehen, wie ich das erkläre... Ein andermal.

### Meine Tastatur ist komisch
Ich habe nie gelernt, auf einer Maschine zu schreiben, obwohl ich es immer wollte. Während ich bei der Organisation von Fab15 in Ägypten war, ist mir aufgefallen, dass Sherry Lassiter sehr geschickt im Maschinenschreiben ist. In jenem Moment entschied ich mich, es zu lernen. Wenn man etwas von Grund auf neu lernt, hat man den Vorteil, keine schlechten Angewohnheiten zu haben. Also habe ich nicht das QWERTY-System gelernt, welches ursprünglich entworfen wurde, um das Verklemmen der Tasten bei alten Schreibmaschinen zu verhindern. Ich habe mit dem [Colemak](https://colemak.com)-System gelernt. Colemak ist so entworfen, dass die am häufigsten genutzten Buchstaben im Englischen in der mittleren Reihe liegen. Ich habe eine [ortho-lineare Tastatur](https://drop.com/buy/preonic-mechanical-keyboard), auf der ich das Colemak-Layout habe, und ich übe etwa fünf Minuten pro Tag. Was mir am Colemak-Layout am besten gefällt, ist, dass die Rücktaste neben der Taste `A` liegt.

![](../../img/w01/preonic.webp)

Außerdem habe ich eine [Software auf macOS](https://karabiner-elements.pqrs.org), die meine Tastaturbelegung auf Colemak umstellt und die Funktion der Caps-Lock-Taste zu einem Backspace macht.

### Mein Texteditor ist auch komisch
Ich beabsichtige, nur einen Texteditor in der Kommandozeile zu verwenden. Ich kenne `vim` ein bisschen und möchte mein Wissen vertiefen. Mir gefällt die Idee, Texte nur mit der Tastatur bearbeiten zu können. Um der Versuchung, Visual Studio Code zu benutzen, zu widerstehen, habe ich es deinstalliert. Der Texteditor vim ist von Haus aus ziemlich spartanisch. Deshalb werde ich einige Plugins installieren. Hier ist eine Liste, die ich im Laufe der Zeit erweitern werde:

- [NERDTree](https://github.com/preservim/nerdtree) für eine Seitenleiste mit einer Dateiliste, um schnell zwischen Dateien navigieren zu können.
- [vim-devicons](https://github.com/ryanoasis/vim-devicons) um Dateien und Ordner mit kleinen grafischen Icons darzustellen. 

 Weitere nützliche Links:

- [VimAwesome](https://vimawesome.com) ist eine Webseite mit Hunderten von vim-Plugins
- [Frans My Computing Repo](https://github.com/TheBeachLab/myComputing) mit einigen Tricks, falls du die Kommandozeile magst.

### Mehrsprachige Dokumentation mit KI.
Ich muss realistisch sein. Ich habe nicht viel Freizeit und bald werde ich noch weniger haben. Deshalb benötige ich ein System, mit dem ich die Dokumentation flink verfassen kann. Ich werde eine neue Technik für die Dokumentation ausprobieren, die es mir erlaubt, die Dokumentation in zwei (oder mehr) Sprachen zu haben. Im Moment wird der Großteil des Textes, den du liest, auf Spanisch in meinen Mac diktiert.

![](../../img/w01/dictation.webp)

Das spart mir etwas Zeit beim Schreiben. Einige Teile, wie Code, muss ich manuell eingeben. Auch Korrekturen muss ich manuell machen, zum Beispiel, wenn ich Links einfüge.

So erstelle ich Markdown-Dateien mit der Dokumentation auf Spanisch. Der Dateiname jeder Woche enthält die Woche, in der ich mich befinde, und die Sprache der Dokumentation. In diesem Fall: `w01-es.md`. Das Problem ist, dass die Dokumentation auf Englisch sein muss. Der Grund, warum ich es nicht direkt auf Englisch diktiere, ist, dass mein Akzent so schlecht ist, dass der Computer mich nicht versteht. Um dieses Problem zu lösen, werde ich eine Künstliche Intelligenz verwenden, um den Text dieses Dokuments ins Englische und auch ins Deutsche zu übersetzen. Ich werde die Dateien als `w01-en.md` und `w01-de.md` speichern. Das KI-Modell muss in der Lage sein, die Markdown-Syntax zu erkennen und sie zu respektieren. Es muss auch in der Lage sein, interne Links zu bearbeiten, denn Links, die zu `w02-es.md` in der spanischen Dokumentation führen, müssen in der englischen Variante der Dokumentation zu `w02-en.md` geändert werden. Möglicherweise wird sich das Modell im Laufe des Fab Academy verändern (oder sogar wechseln). Deshalb werde ich den Text auf Spanisch behalten und jede Woche die Übersetzung aller Dateien neu durchführen. Ich werde nur die ursprüngliche spanische Datei bearbeiten. Ich werde die generierte Übersetzung nicht manuell bearbeiten. Wenn das, was du auf Englisch oder Deutsch liest, also keinen Sinn ergibt, gib OpenAI oder welches Modell ich auch immer benutze die Schuld.

Ich habe César Garcia von [La Hora Maker](https://www.youtube.com/lahoramaker) gebeten, mir bei der Suche nach einem Modell für die Übersetzung zu helfen. César hat mir empfohlen, die Whisper-API von OpenAI zu nutzen, die in der Lage ist, direkt von Spanisch zu übersetzen. Derzeit bin ich nur an der Übersetzung interessiert, deshalb habe ich einen Assistenten in der OpenAI-API mit diesen Anweisungen erstellt:

> Übersetze den Text von Spanisch nach Deutsch. Lies das gesamte Dokument, um den Kontext zu verstehen, bevor du übersetzt, und berücksichtige die Nuancen und Redewendungen der spanischen Sprache, um sie in die entsprechenden deutschen Äquivalente zu übersetzen. Die Übersetzung sollte nicht wörtlich sein, konzentriere dich darauf, die ursprüngliche Bedeutung zu erhalten und eine Übersetzung zu liefern, die Sinn macht. Ignoriere externe URLs und Code-Schnipsel in der Übersetzung; wenn du auf einen Markdown-Link stößt, übersetze den Text innerhalb der eckigen Klammern. Ändere interne Markdown-Link-URLs, um auf die entsprechende deutsche Datei zu verweisen, z.B. ändere w01-es.md zu w01-de.md. Behalte Marken und Namen bei, ohne sie zu übersetzen. Verwende korrekte Grammatik und Syntax im finalen Text. Der Stil der Übersetzung sollte informell sein.

Ich habe ein ähnliches Modell auf Deutsch mit ähnlichen Anweisungen. Ich ändere die Anweisungen ab und zu, um zu versuchen, die Übersetzung zu verbessern.

Diese Seite, die du liest, hat etwa 3600 Tokens. Du kannst herausfinden, wie viele Tokens ein Text hat, indem du den [OpenAI Tokenizer](https://platform.openai.com/tokenizer) verwendest. Die Kosten für die Übersetzung dieser Seite in beide Sprachen betragen ungefähr 0,29 USD, wenn man berücksichtigt, dass jede 1000 Tokens 0,01 USD für den Input und 0,03 USD für den Output kosten. Das erscheint mir ziemlich teuer, und außerdem werden die Kosten steigen, je weiter das Fab Academy voranschreitet. Aus diesem Grund werde ich die Inhalte nur dann übersetzen, wenn ich der Meinung bin, dass die Arbeit fortgeschritten ist.

Auf meiner Wunschliste steht, ein lokales Modell zu finden. Auf diese Weise könnte ich die Inhalte öfter übersetzen. Bisher habe ich die Modelle `Phi 2` und `Yarn Mistral` mit katastrophalen Ergebnissen ausprobiert.

### Automatisierung des Übersetzungsprozesses
Anfangs habe ich das API-Fenster von OpenAI benutzt. Jetzt habe ich diesen Prozess automatisiert, indem ich Python in der Kommandozeile nutze. Mit einer Mischung aus Bing Copilot und der kostenlosen Version von ChatGPT bat ich um ein Programm, das die Übersetzung mit der OpenAI-Bibliothek automatisiert. Aber das hat nicht gut geklappt. Nach einigem Hin und Her (die KI generiert selten beim ersten Mal korrekten Code) wurde ich frustriert und beschimpfte Bing.

![](../../img/w01/bing.webp)

Letztendlich musste ich die Dokumentation der API lesen, um das Programm zum Laufen zu bringen.

Um unnötige Kosten zu vermeiden, übersetzt das Skript nur die Markdown-Dateien auf Spanisch, die ich mit `git add` hinzugefügt habe. Dadurch kann ich die Kosten kontrollieren. Danach führe ich einfach `python translate-de.py` aus und das Skript erstellt die übersetzten Markdown-Seiten auf Deutsch. Das Gleiche mache ich für Englisch.

Normalerweise führe ich die Übersetzung nicht isoliert durch, da ich sie in den nächsten Schritt aufgenommen habe.

### Automatisierung der HTML-Erstellung und des Datei-Uploads
Die Dokumentation des Fab Academy muss in Form einer Webseite präsentiert werden. Um die HTML-Seiten aus den Markdown-Dateien zu erstellen, habe ich ein Skript in Bash, das ich für das Bildungsprogramm [FabZero](https://github.com/Academany/fabzero) erstellt hatte, in Python umgewandelt. Der Code konvertiert alle `.md`-Dateien in `.html` unter Nutzung von [Pandoc](https://pandoc.org/index.html) mit einer [CSS-Stilvorlage](../../../base.css). Während der Konvertierung wird, wenn ein Link zu einem Markdown-Dokument gefunden wird, dieser in einen Link zu dem entsprechenden HTML-Dokument umgewandelt, indem [dieser LUA-Filter](../../../links-to-html.lua) verwendet wird.

Optional automatisiert das Skript auch die Übersetzungen ins Englische und Deutsche und das Hochladen der Dateien auf Github. Wenn ich also meinen Fortschritt hochladen möchte, schreibe ich:

`python auto.py --translate updating week 1`

Auf diese Weise übersetzt das Skript die Seiten ins Englische und Deutsche, falls `--translate` unter den Argumenten gefunden wird. Außerdem konvertiert es alle Seiten nach HTML und lädt alles auf Github hoch, solange eine Nachricht vorhanden ist, in diesem Fall `updating week 1`. Gibt es keine Nachricht, führt es keinen der mit git verbundenen Prozesse durch. 

Das Skript kannst du hier einsehen: [auto.py](../../../auto.py)

### Nutzung von CD/CI in Github für das Hosting der Webseiten

Schauen wir, was ich bisher auf Github habe:

- Meine originalen `.md`-Dateien auf Spanisch
- Die durch KI ins Englische und Deutsche übersetzten `.md`-Dateien
- Die `.html`-Seiten aller `.md`-Dateien, die von Pandoc generiert wurden.

Das Einzige, was jetzt noch fehlt, ist ein Webserver. Und das kannst du über Github machen, indem du zu den Einstellungen des Repositories gehst.

![](../../img/w01/cicd.webp)

Dies wird eine Datei unter `.github/workflows/static.yml` erstellen, wo ich nur den `runner` ändern musste, da `runs-on: ubuntu-latest` nicht funktionierte. Ich habe es zu `runs-on: ubuntu-22.04` geändert und beim `commit` wurden die Seiten automatisch gehostet.

### Endergebnis

[https://thebeachlab.github.io/backtofabacademy2024/](https://thebeachlab.github.io/backtofabacademy2024/)

### Fazit
All das macht das Schreiben der Dokumentation im Moment ein bisschen langsam und etwas mühsam. Aber ich glaube, dass dieses System **die Geschwindigkeit Woche für Woche drastisch steigern** wird und ich am Ende in der Lage sein werde, sehr schnell und detailliert zu dokumentieren.

Außerdem denke ich, dass diese Methode **vielen Menschen helfen wird**, die ihr Talent nicht zeigen können, weil sie eine andere Sprache nicht beherrschen. Es ist ungerecht, wenn das passiert, und ich hoffe, dass KI Menschen dabei hilft zu zeigen, wie wertvoll sie sind.

## Git: Dieser unendliche Abgrund
Man könnte denken, dass ich nach 10 Jahren Nutzung von git alles darüber weiß. Weit gefehlt. Das sind die Dinge, die ich während dieses Fab Academy-Zyklus verbessern möchte:

- Meine Neigung unterdrücken, Änderungen direkt in den Hauptzweig hochzuladen. Normalerweise passiert nichts Schlimmes, aber ich muss mich daran gewöhnen, für jede Änderung einen neuen Zweig zu erstellen.
- ~~Steale~~ Lasse mich von Neils [Aliasen](http://academy.cba.mit.edu/classes/project_management/archive.html) inspirieren, um Git-Befehle schneller auszuführen.

(Vielleicht füge ich im Laufe des Fab Academy noch mehr hinzu...)

## Projektmanagement
Ich möchte erklären, wie ich meine Projekte manage. Wenn du keinen Chef hast und niemand dir sagt, was du tun sollst, musst du sehr diszipliniert sein. Andernfalls kannst du in eine negative Spirale geraten.

 Das Wichtigste ist **zu wissen, wohin du gehst**. Denn wenn du das nicht weißt, hast du ein ernstes Problem. Manchmal wirst du dich im Fab Academy (und in deinem Leben) verloren fühlen. Du weißt nicht, was du tun möchtest, du hast keine Lust auf irgendwas und es scheint, als würdest du dich in Zeitlupe bewegen, während die Welt sich in voller Geschwindigkeit dreht. Wenn dir das passiert, denk an [Phil Stutz](https://www.thetoolsbook.com). Investiere in dich selbst: Treibe Sport, knüpfe wieder Kontakte zu anderen Menschen, schreibe deine Memoiren in ein Tagebuch. Mir hilft das und ich bin überzeugt, dass es dir auch helfen wird. Bald wirst du deinen Polarstern sehen. Setze Kurs auf ihn.

 Das Zweite ist **zu lernen, zu reduzieren und zu vereinfachen**. Eines deiner größten Probleme im Fab Academy wird so aussehen: Du findest ein Foto nicht, von dem du sicher bist, dass du es hattest. Du weißt nicht, ob es auf den Fotos deines Handys, in Google Drive oder auf dem USB-Stick ist, ob du es in den Ordner auf deinem Computer verschoben hast, oder ob es dir jemand über WhatsApp geschickt hat... Vereinfache. Reduziere.

Und schließlich, und ich denke, das ist das Wichtigste. Das wahre Geheimnis, um alles zu erreichen, egal wie schwierig es ist, besteht darin, **viele sehr kleine Schritte zu machen**. Du löst ein kleines Problem, dann ein weiteres, und dann noch eins. So funktioniert das.

Was Werkzeuge zur Unterstützung angeht, habe ich einige ausprobiert. Also fange ich mit denen an, die für mich nicht funktionieren:

- Post-it-Notizen an der Wand. Die Idee ist gut. Sehr visuell und agil. Aber es gibt zwei Probleme. Erstens: In Barcelona ist es oft sehr heiß und die Notizen fallen herunter. Zweites Problem: Wenn ich die Wand nicht sehe, gibt es kein Projekt.
- Software à la Kanban und ähnliche. Sie versuchen, Post-it-Notizen zu imitieren. Ich benutze sie nicht, weil: Sie mir zu kompliziert erscheinen und ich nicht darauf zeichnen kann.
- Microsoft Project und ähnliche. Ohne Kommentar.
- Webdienste wie Notion.com, Monday.com und ähnliche. Wenn mir niemand garantiert, dass ich 350 Jahre leben werde, werde ich keinen Sekunde meines kurzen Lebens damit verschwenden, zu verstehen, wie ein Dienst funktioniert, der nur auf TikTok einfach aussieht und wahrscheinlich morgen Nachmittag schließt.

Momentan nutze ich eine Kombination aus Klartext für langfristige Ziele, Erinnerungen für mittelfristige Ziele und Freeform von Apple für die Aufgaben, die ich heute erledigen werde. Freeform ist ein Programm mit einem unendlichen Zeichenbrett, ähnlich wie [Miro](https://miro.com). Es hat die Vorteile der Post-it-Notizen ohne deren Nachteile. Ich kann es anpassen und mein eigenes System schaffen. Zum Beispiel habe ich das Feld `DOING NOW` erstellt, in das nur eine Notiz passt. Für mich ist das wichtig, weil ich nur eine Sache gleichzeitig machen kann. Außerdem kann ich mit der Hand zeichnen, und das gefällt mir. Wahrscheinlich werde ich ein Video machen, in dem ich alles detaillierter erkläre.

![](../../img/w01/freeform.webp)

## Skizze des Abschlussprojekts
Alles bezüglich des Abschlussprojekts habe ich in den [entsprechenden Abschnitt](final-de.md) verschoben.

[<< Zurück zum Anfang](index-de.md)   
[Nächste Woche >>](w02-de.md)