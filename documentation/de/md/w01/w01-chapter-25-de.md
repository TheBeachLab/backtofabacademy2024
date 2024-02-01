### Automatisierung des Übersetzungsprozesses
Zuerst habe ich die OpenAI API direkt benutzt. Jetzt habe ich diesen Prozess mit Python in der Befehlszeile automatisiert. Mit einer Kombination aus Bing Copilot und der kostenlosen Version von ChatGPT bat ich um ein Programm, das mithilfe der OpenAI-Bibliothek die Übersetzung automatisierte. Das hat allerdings nicht gut geklappt. Nach einigem Hin und Her (KI generiert nicht immer beim ersten Mal korrekten Code) war ich am Ende frustriert und habe Bing beschimpft.

![](../../img/w01/bing.webp)

Schließlich musste ich die Dokumentation der API lesen, um das Programm zum Laufen zu bringen.

Um unnötige Kosten zu vermeiden, übersetzt das Skript nur die Kapitel auf Spanisch, die ich mit `git add` hinzugefügt habe. Dadurch kann ich die Kosten besser kontrollieren. Danach führe ich einfach `python translate-en.py` aus, und das Skript erzeugt die ins Englische übersetzten Markdown-Seiten. Dasselbe mache ich für Deutsch.

Eigentlich führe ich die Übersetzung nicht isoliert durch, da ich sie in den nächsten Schritt integriert habe.

