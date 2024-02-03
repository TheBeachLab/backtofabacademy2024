## Automatisierung der Übersetzung
[Zu Beginn]{.smallcaps} habe ich das OpenAI API-Fenster verwendet. Jetzt habe ich diesen Prozess mit einem Python-Skript automatisiert. Unter Verwendung einer Mischung aus Bing Copilot und der kostenlosen Version von ChatGPT bat ich um ein Programm, das die Übersetzung mit der OpenAI-Bibliothek automatisieren sollte. Aber es ging schief. Nach einigem Hin und Her (KI generiert selten beim ersten Versuch korrekten Code), endete ich frustriert und fluchte über Bing.

![](../../img/w01/bing.webp)

Letztlich musste ich die API-Dokumentation lesen, um das Programm zum Laufen zu bringen.

Um unnötige Mehrkosten zu vermeiden, übersetzt das Skript nur die Kapitel auf Spanisch, die ich mit `git add` hinzugefügt habe. Dank dessen kann ich die Kosten besser kontrollieren. Danach führe ich einfach `python translate-en.py` aus und das Skript erzeugt die ins Englische übersetzten Markdown-Seiten. Dasselbe mache ich für Deutsch.

In Wirklichkeit mache ich die Übersetzung normalerweise nicht isoliert, weil ich sie in den nächsten Schritt eingebaut habe.

