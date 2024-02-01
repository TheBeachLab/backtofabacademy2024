### Using Markdown
Here, I don't want to innovate too much. The strategy that has worked very well for me for many years is to write content in a plain text file in a format called [Markdown](https://www.markdownguide.org) `.md`. This way, I focus solely on writing the content. Advantages of writing in Markdown:

- You don't need any special program to write plain text. You can even write it by hand if you have good handwriting and then scan it.
- It's easy to write, you don't have to twist your fingers typing `</h1>` and stuff like that.
- It's easy to apply styles and organize the text.
- It can be read without feeling like you're decoding The Matrix.

![When you can read your page from the HTML code](../../img/w01/code.webp)

Fab Academy documentation has to be presented in the form of a web page. There is a command-line program called [Pandoc](https://pandoc.org/index.html) that literally converts any text format. I'm going to use it to convert `.md` files into "nice-looking" `.html` pages with a CSS style template.

> Note: "Nice" refers to easy to read. Other people value above all the visual aspect of the page and prefer to spend time creating their own work of art. My best wishes to them.

 I'm using [this CSS template](https://jez.io/pandoc-markdown-css-theme/), which allows me to add functionalities like equations, tables, line numbers in code, side notes, etc.

