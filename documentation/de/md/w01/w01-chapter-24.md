### KI-gestützte automatische Übersetzungen
[Im Fab Academy]{.smallcaps} muss die Dokumentation auf Englisch sein. Traditionelle Sprachübersetzer sind ziemlich schlecht. Sie sind nicht in der Lage, den Kontext zu verstehen und produzieren Ergebnisse, die unnatürlich klingen. Ich werde eine künstliche Intelligenz verwenden, um den Text der Kapitel ins Englische und auch ins Deutsche zu übersetzen.

Das KI-Modell muss in der Lage sein, die Markdown-Syntax zu erkennen und diese zu respektieren. Es ist möglich, dass das Modell sich im Laufe des Fab Academy verbessert (oder sogar ändert). Daher werde ich den Text auf Spanisch behalten und die Übersetzung aller Dateien von Zeit zu Zeit erneut durchführen. Ich werde nur die Dateien auf Spanisch bearbeiten. Die generierten Übersetzungen werde ich nicht manuell manipulieren. Also, wenn das, was du auf Englisch oder Deutsch liest, keinen Sinn ergibt, gib OpenAI oder welches Modell auch immer ich verwende, die Schuld.

Ich habe César Garcia von [La Hora Maker](https://www.youtube.com/lahoramaker) gefragt, ob er mir helfen kann, ein Modell für die Übersetzung zu finden. César hat mir empfohlen, die Whisper-API von OpenAI zu verwenden, die in der Lage ist, direkt aus dem Spanischen Audio zu übersetzen. Im Moment interessiere ich mich nur für die Übersetzung, deshalb habe ich einen Assistenten in der OpenAI-API mit diesen Anweisungen erstellt:

```
Übersetze den Text vom Spanischen ins Englische. Lies das gesamte Dokument, um den Kontext zu erfassen, bevor du es übersetzt. Berücksichtige Nuancen und Redewendungen der spanischen Sprache und übersetze sie in die entsprechenden englischen Äquivalente. Die Übersetzung sollte nicht wörtlich sein, konzentriere dich darauf, die ursprüngliche Bedeutung zu bewahren und eine Übersetzung zu liefern, die auf Englisch Sinn ergibt. Übersetze nur den Text in Anführungszeichen im YAML-Header der Markdown-Datei. Übersetze keine Links, URLs, Codeblöcke und Code-Schnipsel. Wenn du auf einen Markdown-Link stößt, übersetze nur den Text innerhalb der eckigen Klammern. Erkenne und behalte Marken und Namen ohne Übersetzung bei. Verwende korrekte Grammatik und Syntax im endgültigen Text. Der Stil der Übersetzung sollte informell sein, mit einer Prise sarkastischem Humor.
```

Ich habe ein anderes Modell auf Deutsch mit ähnlichen Anweisungen. Ich ändere die Anweisungen von Zeit zu Zeit, um zu versuchen, die Übersetzung zu verbessern.

Diese Seite, die du gerade liest, hat etwa 4000 Token. Du kannst herausfinden, wie viele Token ein Text hat, indem du den [OpenAI Tokenizer](https://platform.openai.com/tokenizer) verwendest. Die Kosten für die Übersetzung dieser Seite in beide Sprachen betragen ungefähr 0,32 USD, wenn man bedenkt, dass jeder 1000 Token 0,01 USD für den Input und 0,03 USD für den Output kosten. Das erscheint mir ziemlich teuer, und die Kosten werden mit dem Fortschreiten des Fab Academy steigen. Aus diesem Grund werde ich die Inhalte nur übersetzen, wenn ich die Arbeit für fortgeschritten halte.

Bis jetzt sind die englischen Übersetzungen ziemlich gut. Ich bat [Sophia Döring](https://fabacademy.org/2024/labs/kamplintfort/students/sophia-doring/), auch die deutsche Übersetzung zu überprüfen. Sie sagte mir, dass sie im Allgemeinen auch ziemlich gut sei, obwohl sie manchmal selten verwendete deutsche Wörter verwendet[^242], insbesondere bei der Bezugnahme auf technische Begriffe.

[^242]: Das könnte durch die Art und Weise verursacht sein, wie ich den ursprünglichen Text schreibe. Ich verwende spanische Äquivalente für technische Begriffe, die ich im Alltag eigentlich auf Englisch sage.

Auf meiner Wunschliste werde ich weiterhin nach einem lokalen Modell suchen. So kann ich die Inhalte häufiger und ohne Sorge um die Kosten übersetzen. Kürzlich habe ich das Modell `Miqu-1-70b`[^241] ausprobiert, mit langsamen, aber zufriedenstellenden Ergebnissen. Ich sehe Licht am Ende des Tunnels.

[^241]: [Angeblich](https://the-decoder.com/unintentional-ai-leak-from-mistral-becomes-an-unexpected-powerhouse/) durch einen Mitarbeiter unabsichtlich geleakt. Miqu-1-70b könnte ein starker Konkurrent von GPT4 sein.

