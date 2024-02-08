## Automatische Übersetzungen mit KI
[Im Fab Academy]{.smallcaps} muss die Dokumentation auf Englisch sein. Traditionelle Sprachübersetzer sind ziemlich schlecht. Sie können den Kontext nicht verstehen und erzeugen Ergebnisse, die unnatürlich klingen. Ich werde eine künstliche Intelligenz nutzen, um den Text der Kapitel ins Englische und auch ins Deutsche zu übersetzen.

Das KI-Modell muss in der Lage sein, die Markdown-Syntax zu erkennen und sie zu respektieren. Es ist möglich, dass sich das Modell verbessert (oder sogar ändert) im Laufe des Fab Academy. Deshalb werde ich den Text auf Spanisch beibehalten und die Übersetzung aller Dateien von Zeit zu Zeit erneut ausführen. Ich werde nur die Dateien auf Spanisch bearbeiten. Ich werde die generierten Übersetzungen nicht manuell manipulieren. Also, wenn das, was du auf Englisch oder Deutsch liest, keinen Sinn macht, gib OpenAI oder welches Modell auch immer ich benutze, die Schuld.

Ich habe César Garcia von [La Hora Maker](https://www.youtube.com/lahoramaker) gefragt, ob er mir helfen kann, ein Modell für die Übersetzung zu finden. César hat mir empfohlen, die Whisper API von OpenAI zu verwenden, die in der Lage ist, direkt aus dem Spanischen Audio zu übersetzen. Momentan interessiere ich mich nur für die Übersetzung, daher habe ich mit diesen Anweisungen[^243] einen Assistenten in der OpenAI API erstellt.

```
This file contains text with a mixture of markdown, yaml, pandoc and latex formatting. Translate the text from Spanish to English. Read the entire document to grasp context before translating it. Take into account nuances and idioms of the Spanish language and translate them to the equivalents in English. The translation should not be literal, focus on maintaining the original meaning and provide a translation that makes sense in english. Keep the formatting intact in the translated text, like footnotes, smallcaps, etc .Translate only the text within quotes in the YAML header of the Markdown file. Do not translate the latex notation, links, URLs, blocks of code and code snippets. If encountering a markdown link, only translate the text inside square brackets. Recognize and retain brands and names without translation. Use correct grammar and syntax in the final text. The style of the translation should be informal, with a touch of sarcastic humor.
```

Zusätzlich zu diesen allgemeinen Anweisungen muss ich manchmal etwas Spezielles dem Übersetzer mitteilen. Ich habe einen *Hack*, um spezifische Anweisungen in die Markdown-Dateien zu integrieren. Diese Kommentare erscheinen auf der Markdown-Seite und somit kann der Übersetzer sie lesen. Allerdings ignoriert Pandoc sie und sie erscheinen nicht auf der Webseite. Das ist genial!

```markdown
[comment1]: <> (Note for the translator: Do not translate "hack" as it is universally used in all languages.)
```

[comment1]: <> (Note for the translator: Do not translate "hack" as it is universally used in all languages.)

[^243]:
    Ich habe ein anderes Modell auf Deutsch mit ähnlichen Anweisungen. Ich ändere die Anweisungen von Zeit zu Zeit, um die Übersetzung zu verbessern.

Nach zwei Wochen Nutzung kann ich sagen, dass die englischen Übersetzungen sehr gut sind. Viel besser als das, was ich machen würde. Ich habe [Sophia Döring](https://fabacademy.org/2024/labs/kamplintfort/students/sophia-doring/) gebeten, auch die deutsche Übersetzung zu überprüfen. Sie hat mir gesagt, dass sie im Allgemeinen auch ziemlich gut ist, obwohl sie manchmal ungewöhnliche deutsche Wörter verwendet[^242], besonders wenn es um technische Begriffe geht.

[^242]: Das könnte durch meine Art der Texterstellung verursacht sein. Ich verwende die spanischen Äquivalente von technischen Begriffen, die ich im Alltag tatsächlich auf Englisch sage.

Diese Seite, die du liest, hat ungefähr 4000 Tokens. Du kannst herausfinden, wie viele Tokens ein Text hat, indem du den [OpenAI Tokenizer](https://platform.openai.com/tokenizer) verwendest. Die Kosten für die Übersetzung dieser Seite in zwei Sprachen betragen ungefähr 0.32 USD, wenn man berücksichtigt, dass jeder 1000 Tokens 0.01 USD für die Eingabe und 0.03 USD für die Ausgabe kosten. Das ist ein akzeptabler Preis angesichts der Qualität. Ich werde diese Lösung annehmen, wenn ich meine Projekte internationalisieren möchte. Im Fab Academy verstehe und akzeptiere ich, dass die Kosten aufgrund der zahlreichen Änderungen, die ich auf jeder Seite vornehme, erheblich sein werden.

Auf meiner Wunschliste werde ich weiterhin nach einem lokalen Modell suchen, damit ich die Inhalte häufiger und ohne Kostenbedenken übersetzen kann. Kürzlich habe ich das Modell `Miqu-1-70b`[^241] getestet, mit langsamen, aber zufriedenstellenden Ergebnissen. Ich sehe Licht am Ende des Tunnels.

[^241]: [Angeblich](https://the-decoder.com/unintentional-ai-leak-from-mistral-becomes-an-unexpected-powerhouse/) durch einen Mitarbeiter unbeabsichtigt durchgesickert. Miqu-1-70b könnte ein guter Konkurrent von GPT4 sein.

