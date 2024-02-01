### Den gesamten Prozess automatisieren
Um den kompletten Prozess zu automatisieren, habe ich ein Bash-Skript, das ich für das Bildungsprogramm [FabZero](https://github.com/Academany/fabzero) erstellt habe, in Python umgewandelt. Ich gebe folgendes ein:

`python auto.py --translate updating week 1`

Das Skript übersetzt die bearbeiteten Kapitel, wenn es `--translate` unter den Argumenten findet. Das mache ich, um Kosten zu sparen. Danach fügt es alle Kapitel zusammen und erstellt eine einzige Markdown-Datei für jede Woche. Der nächste Schritt ist die Konvertierung all dieser Dateien in HTML. Während der Konversion, wenn es auf einen Link zu einem Markdown-Dokument stößt, konvertiert es diesen in einen Link zu dem entsprechenden HTML-Dokument mit [diesem LUA-Filter](../../../links-to-html.lua). Schließlich lädt es alles auf Github hoch, vorausgesetzt es gibt eine Nachricht, die in diesem Fall `updating week 1` ist. Wenn es keine Nachricht gibt, führt es keinen der Prozesse im Zusammenhang mit git durch.

Du kannst das Skript hier analysieren: [auto.py](../../../auto.py)

