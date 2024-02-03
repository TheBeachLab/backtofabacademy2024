## All in one
[Here’s how my process works:]{.smallcaps} When I’m done editing the chapters, I run the following script[^261]

[^261]: It's a script originally written in Bash language that I created for the educational program [FabZero](https://github.com/Academany/fabzero) and now I have converted to Python.

`python auto.py --translate updating week 1`

If the script finds `--translate` among the arguments[^262], it translates the modified chapters. Then it concatenates all the chapters and creates a single Markdown file for each week. The next step is to convert all those files into HTML. If, during the conversion, it finds a link to a Markdown document, it converts it into a link to its corresponding HTML document using [this LUA filter](../../../links-to-html.lua). Finally, it uploads everything to Github provided there is a message, which in this case is `updating week 1`. If there is no message, it doesn't perform any of the processes related to git.

[^262]: I do this to save costs, as I don't want to translate the pages every time they are modified.

You can analyze the script here: [auto.py](../../../auto.py)

