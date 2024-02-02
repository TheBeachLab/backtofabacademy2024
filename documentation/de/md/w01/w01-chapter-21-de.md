### Mit Markdown arbeiten
Hier möchte ich nicht zu innovativ sein. Die Strategie, die mir bereits seit vielen Jahren sehr gut dient, ist das Schreiben von Inhalten in einer einfachen Textdatei im sogenannten [Markdown](https://www.markdownguide.org) Format `.md`. Auf diese Weise konzentriere ich mich ausschließlich auf das Schreiben des Inhalts. Vorteile des Schreibens in Markdown:

- Du benötigst kein spezielles Programm, um einfachen Text zu schreiben. Theoretisch könntest du sogar von Hand schreiben, wenn du eine gute Handschrift hast, und es später scannen.
- Es ist einfach zu schreiben, du musst nicht deine Finger verknoten, indem du `</h1>` und ähnliches tippst.
- Stile anwenden und den Text organisieren, geht leicht von der Hand.
- Es ist lesbar, ohne dass es aussieht, als würdest du Matrix entschlüsseln.

![Wenn du deine Seite direkt aus dem HTML-Code lesen kannst](../../img/w01/code.webp)

Die Dokumentation der Fab Academy muss in Form einer Webseite präsentiert werden. Es gibt ein Programm für die Kommandozeile namens [Pandoc](https://pandoc.org/index.html), das buchstäblich jedes Textformat umwandeln kann. Ich werde es verwenden, um die `.md`-Dateien in *ansehnliche*[^nice] `.html`-Seiten mit einem CSS-Style-Template zu verwandeln.

[^nice]: *Ansehnlich* bezieht sich hier auf leichte Lesbarkeit. Andere Leute setzen hingegen alles auf das visuelle Erscheinungsbild der Seite und investieren Zeit darin, ihr eigenes Kunstwerk zu erschaffen. Ich wünsche ihnen dabei alles Gute.

Ich habe [diese CSS-Vorlage](https://jez.io/pandoc-markdown-css-theme/) verwendet, die es mir ermöglicht, Funktionen wie Gleichungen, Tabellen, Zeilennummern im Code, Randnotizen usw. hinzuzufügen. Die Vorlage nannte den Index „Contents“, und ich habe es geändert, um eine Variable im Header einfügen zu können:

```{.html .numberLines .hl-6 .tight-code}
$if(toc)$
<nav id="$idprefix$TOC" role="doc-toc">
  $if(return-url)$
  <a href="$return-url$">$if(return-text)$$return-text$$else$← Zurück$endif$</a><br>
  $endif$
  <strong>Inhalt</strong><label for="contents">⊕</label>
  <input type="checkbox" id="contents">
  $table-of-contents$
</nav>
$endif$
```


```{.html .numberLines .hl-6 .hl-7 .hl-8 .hl-9 .hl-10 .tight-code}
$if(toc)$
<nav id="$idprefix$TOC" role="doc-toc">
  $if(return-url)$
  <a href="$return-url$">$if(return-text)$$return-text$$else$← Zurück$endif$</a><br>
  $endif$
  <strong>$if(toc-title)$
  $toc-title$
  $else$
  Inhalt
  $endif$</strong><label for="contents">⊕</label>
  <input type="checkbox" id="contents">
  $table-of-contents$
</nav>
$endif$
```

