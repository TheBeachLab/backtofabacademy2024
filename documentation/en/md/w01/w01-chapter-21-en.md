### Using Markdown
Here, I don't want to be too innovative. The strategy that has worked very well for me for many years is to write content in a plain text file in a format called [Markdown](https://www.markdownguide.org) `.md`. This way, I focus only on writing the content. Advantages of writing in Markdown:

- You don't need any special program to write plain text. You could even write it by hand if your handwriting is good and then scan it.
- It's easy to write; you don't have to contort your fingers typing `</h1>` and stuff like that.
- It's easy to apply styles and organize the text.
- It can be read without feeling like you're decoding The Matrix.

![When you can read your page from HTML code](../../img/w01/code.webp)

The documentation for Fab Academy has to be presented in the form of a web page. There's a command-line program called [Pandoc](https://pandoc.org/index.html) that literally converts any text format. I'm going to use it to convert `.md` files into "nicely looking" `.html` pages with a CSS style template.

> Note: "Nice" refers to easy to read. Other people value above all the visual appearance of the page and prefer to spend time creating their own masterpiece. My best wishes to them.

Temporarily, I'm using the [template I used for HTGAA](http://htgaa.beachlab.org) in 2015. But I plan to switch to [this template soon](https://jez.io/pandoc-markdown-css-theme/), because I need to add more functionalities (equations, tables, line numbers in code, side notes, etc.).

