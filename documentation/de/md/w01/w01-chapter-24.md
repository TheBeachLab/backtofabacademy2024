## KI-gestützte automatische Übersetzungen
[Im Fab Academy]{.smallcaps} muss die Dokumentation auf Englisch sein. Traditionelle Sprachübersetzer sind ziemlich schlecht. Sie können den Kontext nicht verstehen und erzeugen Ergebnisse, die unnatürlich klingen. Ich werde eine künstliche Intelligenz nutzen, um den Text der Kapitel ins Englische und auch ins Deutsche zu übersetzen.

Das KI-Modell muss in der Lage sein, die Syntax von Markdown zu erkennen und sie zu respektieren. Es ist möglich, dass sich das Modell im Verlauf des Fab Academy verbessert (oder sogar ändert). Deshalb werde ich den Text auf Spanisch behalten und die Übersetzung aller Dateien von Zeit zu Zeit erneut durchführen. Ich werde nur die Dateien auf Spanisch bearbeiten. Ich werde die generierten Übersetzungen nicht manuell anpassen. Also, wenn das, was du auf Englisch oder Deutsch liest, keinen Sinn ergibt, gib die Schuld OpenAI oder welchem Modell auch immer ich gerade nutze.

Ich habe César Garcia von [La Hora Maker](https://www.youtube.com/lahoramaker) gefragt, ob er mir helfen kann, ein Modell für die Übersetzung zu finden. César hat mir empfohlen, die Whisper API von OpenAI zu nutzen, die in der Lage ist, direkt aus dem spanischen Audio zu übersetzen. Im Moment interessiere ich mich nur für die Übersetzung, daher habe ich einen Assistenten in der OpenAI API mit diesen Anweisungen erstellt:

```
This file contains text with a mixture of markdown, yaml, pandoc and latex formatting. Translate the text from Spanish to English. Read the entire document to grasp context before translating it. Take into account nuances and idioms of the Spanish language and translate them to the equivalents in English. The translation should not be literal, focus on maintaining the original meaning and provide a translation that makes sense in english. Keep the formatting intact in the translated text, like footnotes, smallcaps, etc .Translate only the text within quotes in the YAML header of the Markdown file. Do not translate the latex notation, links, URLs, blocks of code and code snippets. If encountering a markdown link, only translate the text inside square brackets. Recognize and retain brands and names without translation. Use correct grammar and syntax in the final text. The style of the translation should be informal, with a touch of sarcastic humor.
```

Ich habe ein weiteres Modell auf Deutsch mit ähnlichen Anweisungen. Ich ändere die Anweisungen von Zeit zu Zeit, um zu versuchen, die Übersetzung zu verbessern.

Diese Seite, die du gerade liest, besteht aus etwa 4000 Tokens. Du kannst herausfinden, wie viele Tokens ein Text hat, indem du den [OpenAI Tokenizer](https://platform.openai.com/tokenizer) verwendest. Die Kosten für die Übersetzung dieser Seite in beide Sprachen betragen ungefähr 0.32 USD, wenn man bedenkt, dass je 1000 Tokens 0.01 USD für den Input und 0.03 USD für den Output kosten. Das erscheint mir ziemlich teuer, und die Kosten werden im Laufe des Fab Academy wahrscheinlich steigen. Deshalb werde ich die Inhalte nur übersetzen, wenn ich die Arbeit als fortgeschritten betrachte.

Bis jetzt sind die englischen Übersetzungen ziemlich gut. Ich habe [Sophia Döring](https://fabacademy.org/2024/labs/kamplintfort/students/sophia-doring/) gebeten, auch die deutsche Übersetzung zu überprüfen. Sie sagte mir, dass sie im Allgemeinen auch ziemlich gut ist, obwohl sie manchmal deutsche Wörter verwendet, die selten gebraucht werden[^242], vor allem bei technischen Begriffen.

[^242]: Das könnte durch meine Art und Weise verursacht sein, wie ich den Originaltext schreibe. Ich verwende spanische Äquivalente für technische Begriffe, die ich im Alltag eigentlich auf Englisch sage.

Auf meiner Wunschliste suche ich weiterhin nach einem lokalen Modell. Auf diese Weise könnte ich die Inhalte häufiger und ohne Sorge um die Kosten übersetzen. Kürzlich habe ich das Modell `Miqu-1-70b`[^241] ausprobiert, mit langsamen, aber zufriedenstellenden Ergebnissen. Ich sehe Licht am Ende des Tunnels.

[^241]: [Angeblich](https://the-decoder.com/unintentional-ai-leak-from-mistral-becomes-an-unexpected-powerhouse/) durch einen Mitarbeiter unbeabsichtigt geleakt. Miqu-1-70b könnte ein starker Konkurrent von GPT4 sein.

