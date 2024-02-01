### Automating the Entire Process
To automate the entire process, I converted a Bash script I made for the educational program [FabZero](https://github.com/Academany/fabzero) into Python. I write something like this:

`python auto.py --translate updating week 1`

The script translates the updated chapters if it finds `--translate` among the arguments. I do this to save costs. Then, it concatenates all chapters and creates a single Markdown file for each week. The next step is converting all these files into HTML. During the conversion, if it finds a link to a markdown document, it converts it into a link to its corresponding HTML document using [this LUA filter](../../../links-to-html.lua). Finally, it uploads everything to Github as long as there is a message, which in this case is `updating week 1`. If there's no message, it doesn't carry out any of the processes related to git.

You can check out the script here: [auto.py](../../../auto.py)

