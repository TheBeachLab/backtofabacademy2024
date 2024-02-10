## Automatische Übersetzungen mit KI
Im *Fab Academy* muss die Dokumentation auf Englisch sein. Traditionelle Sprachübersetzer sind ziemlich schlecht. Sie sind nicht in der Lage, den Kontext zu verstehen und produzieren Ergebnisse, die unnatürlich klingen. Ich werde eine künstliche Intelligenz verwenden, um den Text der Kapitel ins Englische und auch ins Deutsche zu übersetzen.

Das KI-Modell muss in der Lage sein, die Syntax von Markdown zu erkennen und diese zu respektieren. Es ist möglich, dass sich das Modell im Laufe des Fab Academy verbessert (oder sogar ändert). Deshalb werde ich den Text auf Spanisch speichern und die Übersetzung aller Dateien von Zeit zu Zeit erneut durchführen. Ich werde nur die Dateien auf Spanisch bearbeiten. Ich werde die generierten Übersetzungen nicht manuell manipulieren. Also, wenn das, was du auf Englisch oder Deutsch liest, keinen Sinn ergibt, gib OpenAI oder welchem Modell ich auch immer verwende, die Schuld.

Ich habe César Garcia von [La Hora Maker](https://www.youtube.com/lahoramaker) gefragt, ob er mir helfen kann, ein Modell für die Übersetzung zu finden. César hat mir empfohlen, die Whisper-API von OpenAI zu verwenden, die in der Lage ist, direkt aus dem Spanischen Audio zu übersetzen. Im Moment bin ich nur an der Übersetzung interessiert, deshalb habe ich in der OpenAI-API einen Assistenten mit diesen Anweisungen erstellt[^243]

```
This file contains text with a mixture of markdown, yaml, pandoc and latex formatting. Translate the text from Spanish to English. Read the entire document to grasp context before translating it. Take into account nuances and idioms of the Spanish language and translate them to the equivalents in English. The translation should not be literal, focus on maintaining the original meaning and provide a translation that makes sense in english. Keep the formatting intact in the translated text, like footnotes, smallcaps, etc .Translate only the text within quotes in the YAML header of the Markdown file. Do not translate the latex notation, links, URLs, blocks of code and code snippets. If encountering a markdown link, only translate the text inside square brackets. Recognize and retain brands and names without translation. Use correct grammar and syntax in the final text. The style of the translation should be informal, with a touch of sarcastic humor.
```

Zusätzlich zu diesen allgemeinen Anweisungen muss ich manchmal dem Übersetzer etwas mitteilen. Ich habe einen *Hack*, um spezifische Anweisungen in den Markdown-Dateien hinzuzufügen. Diese Kommentare erscheinen auf der Markdown-Seite und daher kann der Übersetzer sie lesen. Pandoc ignoriert sie jedoch und sie erscheinen nicht auf der Webseite. Genial!

```markdown
[comment1]: <> (Hinweis für den Übersetzer: "Hack" nicht übersetzen, da es universell in allen Sprachen verwendet wird.)
```

[comment1]: <> (Hinweis für den Übersetzer: "Hack" nicht übersetzen, da es universell in allen Sprachen verwendet wird.)

[^243]:
    Ich habe ein weiteres Modell auf Deutsch mit ähnlichen Anweisungen. Ich ändere die Anweisungen von Zeit zu Zeit, um zu versuchen, die Übersetzung zu verbessern.

Nach zwei Wochen Nutzung kann ich sagen, dass die englischen Übersetzungen sehr gut sind. Viel besser, als ich es tun würde, mit einer Anmerkung: Es scheint, als würde das System manchmal weniger intelligent werden. Ich habe gelesen, dass sich andere Benutzer über das Gleiche beschwert haben. Es ist, als ob OpenAI in der Lage wäre, die dem Modell zugewiesenen Ressourcen zu gradieren oder zu begrenzen. Ich bat [Sophia Döring](https://fabacademy.org/2024/labs/kamplintfort/students/sophia-doring/) auch, die deutsche Übersetzung zu überprüfen. Sie sagte mir, dass sie im Allgemeinen auch ziemlich gut ist, obwohl sie manchmal wenig gebräuchliche deutsche Wörter verwendet[^242], vor allem, um sich auf technische Begriffe zu beziehen.

[^242]: Möglicherweise ist dies durch die Art und Weise, wie ich den Originaltext schreibe, verursacht. Ich verwende die spanischen Äquivalente für technische Begriffe, die ich im Alltag tatsächlich auf Englisch sage.

Diese Seite, die du liest, hat ungefähr 4000 Tokens. Du kannst herausfinden, wie viele Tokens ein Text hat, indem du den [OpenAI Tokenizer](https://platform.openai.com/tokenizer) verwendest. Die Kosten für die Übersetzung dieser Seite in beide Sprachen betragen ungefähr 0,32 USD, wenn man bedenkt, dass je 1000 Tokens 0,01 USD für das Eingabematerial und 0,03 USD für das Ausgabematerial kosten. Dies ist ein akzeptabler Preis, angesichts der Qualität. Ich werde diese Lösung annehmen, wenn ich meine Projekte internationalisieren möchte. Im Fab Academy verstehe und akzeptiere ich, dass die Kosten erheblich sein werden, aufgrund der vielfachen Änderungen, die ich auf jeder Seite vornehmen werde.

Auf meiner Wunschliste werde ich weiterhin nach einem lokalen Modell suchen. So könnte ich die Inhalte häufiger übersetzen und müsste mir keine Sorgen über die Kosten machen. Kürzlich habe ich das Modell `Miqu-1-70b` ausprobiert[^241] mit langsamen, aber zufriedenstellenden Ergebnissen. Ich sehe Licht am Ende des Tunnels.

[^241]: [Angeblich](https://the-decoder.com/unintentional-ai-leak-from-mistral-becomes-an-unexpected-powerhouse/) unbeabsichtigt von einem Mitarbeiter durchgesickert. Miqu-1-70b könnte ein starker Konkurrent von GPT4 sein.

