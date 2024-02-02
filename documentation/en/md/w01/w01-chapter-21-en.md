### Using Markdown
Here, I don't want to get too fancy. The strategy that has worked very well for me for many years is to write content in a plain text file in a format called [Markdown](https://www.markdownguide.org) `.md`. This way, I focus solely on writing the content. Advantages of writing in Markdown:

- You don't need any special program to write plain text. You could even write it by hand if you have good handwriting and scan it later.
- It's easy to write, you don't have to twist your fingers typing `</h1>` and things like that.
- It's easy to apply styles and organize the text.
- It can be read without feeling like you're decoding the Matrix.

![When you can read your page from the HTML code](../../img/w01/code.webp)

The Fab Academy documentation has to be presented in the form of a web page. There's a command-line program called [Pandoc](https://pandoc.org/index.html) that literally converts any text format. I'm going to use it to convert the `.md` files into *nice-looking* `.html` pages with a CSS style template.

[^nice]: *Nice* refers to easy to read. Other kinds of people value the visual appearance of the page above all and prefer to spend time creating their own masterpiece. My best wishes to them.

I used [this CSS template](https://jez.io/pandoc-markdown-css-theme/), which allows me to add features like equations, tables, line numbers in code, side notes, etc. The template had the index name as `Contents`, and I've modified it to be able to include a variable in the header:

```{.html .numberLines .hl-6 .tight-code}
$if(toc)$
<nav id="$idprefix$TOC" role="doc-toc">
  $if(return-url)$
  <a href="$return-url$">$if(return-text)$$return-text$$else$← Return$endif$</a><br>
  $endif$
  <strong>Contents</strong><label for="contents">⊕</label>
  <input type of checkbox" id="contents">
  $table-of-contents$
</nav>
$endif$
```


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

