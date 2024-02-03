### Markdown nutzen
["Hier will ich nicht allzu innovativ sein."]{.smallcaps} Die Strategie, die mir schon seit vielen Jahren sehr gut dient, ist das Schreiben von Inhalten in einer einfachen Textdatei im Format namens [Markdown](https://www.markdownguide.org) `.md`. So konzentriere ich mich ausschließlich auf das Schreiben des Inhalts. Vorteile des Schreibens in Markdown:

- Du benötigst kein spezielles Programm, um einfachen Text zu schreiben. Du könntest ihn sogar per Hand schreiben, wenn du eine gute Handschrift hast, und ihn später scannen.
- Es ist einfach zu schreiben, du musst dir nicht die Finger verrenken, indem du `</h1>` und so weiter tippst.
- Es ist einfach, Stile anzuwenden und den Text zu organisieren.
- Es lässt sich lesen, ohne dass es so aussieht, als würdest du die Matrix entschlüsseln.

![Wenn du deine Seite direkt aus dem HTML-Code lesen kannst](../../img/w01/code.webp)

Die Dokumentation der Fab Academy muss in Form einer Webseite präsentiert werden. Es gibt ein Programm für die Befehlszeile namens [Pandoc](https://pandoc.org/index.html), das buchstäblich jeden Textformat umwandeln kann. Ich werde es benutzen, um die `.md`-Dateien in *ansehnliche*[^211] `.html`-Seiten mit einem CSS-Style-Template umzuwandeln. Das Template hat zwei Vorteile. Zum einen erlaubt es mir, mich nicht um das visuelle Erscheinungsbild der Seite kümmern zu müssen. Zum anderen erlaubt es mir, leicht Funktionen wie Gleichungen, Tabellen, Zeilennummern im Code, Randnotizen usw. hinzuzufügen.

[^211]: *Ansehnlich* bezieht sich hier auf die Lesbarkeit. Andere Menschen legen vor allem Wert auf das visuelle Erscheinungsbild der Seite und verbringen gerne Zeit damit, ihr eigenes Kunstwerk zu erstellen. Meine besten Wünsche für sie.

Das Template, das ich verwendet habe, nennt sich [Tufte CSS.](https://github.com/jez/tufte-pandoc-css)[^212] Ich habe das Template angepasst, weil es nicht vollständig für mehrere Sprachen gedacht war.

[^212]: Stark inspiriert vom visuellen Stil der Bücher von Edward R. Tufte.

```{.html .numberLines .hl-6 .tight-code}
$if(toc)$
<nav id="$idprefix$TOC" role="doc-toc">
  $if(return-url)$
  <a href="$return-url$">$if(return-text)$$return-text$$else$← Return$endif$</a><br>
  $endif$
  <strong>Contents</strong><label for="contents">⊕</label>
  <input type="checkbox" id="contents">
  $table-of-contents$
</nav>
$endif$
```
In Zeile 6 war das Wort Index als `Contents` fest eingebettet. Jetzt stammt das Wort aus der Variable `toc-title` im Header:
```{.html .numberLines .hl-6 .hl-7 .hl-8 .hl-9 .hl-10 .tight-code}
$if(toc)$
<nav id="$idprefix$TOC" role="doc-toc">
  $if(return-url)$
  <a href="$return-url$">$if(return-text)$$return-text$$else$← Return$endif$</a><br>
  $endif$
  <strong>$if(toc-title)$
  $toc-title$
  $else$
  Contents
  $endif$</strong><label for="contents">⊕</label>
  <input type="checkbox" id="contents">
  $table-of-contents$
</nav>
$endif$
```

