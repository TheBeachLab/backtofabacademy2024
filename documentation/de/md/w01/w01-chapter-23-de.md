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

