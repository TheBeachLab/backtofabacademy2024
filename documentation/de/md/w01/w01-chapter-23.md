## Dateistruktur
[Am Anfang]{.smallcaps} schrieb ich den Text jeder Woche in einer einzigen Datei. Aber wie du später noch lesen wirst, verwende ich einen kostenpflichtigen Service für die Übersetzung. Jedes Mal, wenn ich eine Zeile bearbeitete, musste ich die ganze Datei erneut übersetzen lassen. Um die Kosten zu begrenzen, habe ich die Woche in Kapitel[^231] aufgeteilt und erstelle eine Datei für jedes Kapitel. So müssen nur die Kapitel, die ich geändert habe, übersetzt werden.

[^231]: Meine Dateistruktur ist inspiriert von der Programmiersprache [BASIC](https://en.wikipedia.org/wiki/BASIC)

```
/documentation
    /es
        /md
            /w01
                w01-chapter-00.md
                w01-chapter-10.md
                w01-chapter-20.md
                w01-chapter-21.md
                ...
                w01-chapter-90.md
```

Der Dateiname codiert sowohl die Woche, in der ich mich befinde, als auch das Kapitel. Kapitel 00 ist die Einleitung. Ich verwende die Kapitel 10, 20, 30... um die Abschnitte der Woche zu entwickeln. Wenn ein Kapitel sehr lang ist, teile ich es mit den Zwischennummern auf: 20, 21, 22, etc. Kapitel 90 ist immer das Fazit.

Anschließend füge ich[^232] alle Kapitel der Woche in einer einzigen Datei zusammen, in diesem Fall `w01.md`.

[^232]: **Wichtiger Hinweis:** Ich bearbeite niemals manuell die zusammengefügte Datei. Ich bearbeite nur die einzelnen Kapitel.

