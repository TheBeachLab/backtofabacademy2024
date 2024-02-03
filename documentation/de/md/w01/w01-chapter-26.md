## Alles in einem
[So funktioniert mein Prozess:]{.smallcaps} Wenn ich fertig bin mit dem Bearbeiten der Kapitel, führe ich das folgende Skript aus[^261]

[^261]: Es ist ein Skript, das ursprünglich in Bash geschrieben wurde, welches ich für das Bildungsprogramm [FabZero](https://github.com/Academany/fabzero) erstellt habe und das ich jetzt in Python umgewandelt habe.

`python auto.py --translate updating week 1`

Wenn das Skript `--translate` unter den Argumenten findet[^262], übersetzt es die bearbeiteten Kapitel. Danach fügt es alle Kapitel zusammen und erstellt eine einzelne Markdown-Datei für jede Woche. Der nächste Schritt ist die Umwandlung all dieser Dateien in HTML. Wenn es während der Umwandlung auf einen Link zu einer Markdown-Datei stößt, wandelt es diesen in einen Link zu dem entsprechenden HTML-Dokument um, unter Verwendung [dieses LUA-Filters](../../../links-to-html.lua). Schließlich lädt es alles auf Github hoch, vorausgesetzt es gibt eine Nachricht, die in diesem Fall `updating week 1` lautet. Gibt es keine Nachricht, wird keiner der mit git verbundenen Prozesse ausgeführt.

[^262]: Das mache ich, um Kosten zu sparen, da ich die Seiten nicht bei jeder Änderung übersetzen möchte.

Du kannst das Skript hier analysieren: [auto.py](../../../auto.py)

