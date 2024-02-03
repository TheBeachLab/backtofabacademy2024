## Using Markdown
[I'm not exactly looking to break new ground here]{.smallcaps}. The strategy that has served me well for many years is to write content in a plain text file in a format called Markdown `.md`. This way, I focus solely on writing the content. Advantages of writing in Markdown:

- You don't need any special program to write plain text. You could even write it by hand if you have nice handwriting and scan it later.
- It's easy to write, you don't have to twist your fingers typing `</h1>` and stuff like that.
- It's easy to apply styles and organize text.
- It can be read without feeling like you're decoding The Matrix.

![When you can read your page from the HTML code](../../img/w01/code.webp)

Fab Academy documentation must be presented in the form of a web page. There is a command-line program called [Pandoc](https://pandoc.org/index.html) that literally converts any text format. I'm going to use it to convert `.md` files into *nice-looking*[^211] `.html` pages with a CSS style template. The template has two advantages. On one hand, it allows me to forget about the visual aspect of the page. On the other hand, it makes it easy to add functionalities such as equations, tables, line numbers in the code, side notes, etc.

[^211]: *Nice-looking* refers to being easy to read. Other people value the visual aspect of the page above all and prefer to spend time creating their own masterpiece. My best wishes to them.

The template I've used is called [Tufte CSS.](https://github.com/jez/tufte-pandoc-css)[^212] I modified the template because it wasn't fully designed for multiple languages. 

[^212]: Strongly inspired by the visual style of Edward R. Tufte's books.

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
On line 6, the word 'Contents' was hardcoded. Now, the word comes from the `toc-title` variable in the header:
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

