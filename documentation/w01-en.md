# Week 1. Principles and Practices, Project Management

 > *Task A:*
 >
 > Plan and sketch a potential final project.
 >
 > *Task B:*
 >
 > Perform a step-by-step Git tutorial.  
 > Build a personal site in the class repository describing yourself and your final project.

## Reinventing the Way of Documenting

### macOS again? How could you stoop so low?
Let me try to explain this... I'll explain another day.

### Colemak?
I never knew how to touch type, although I always wanted to learn. While working on the organization of Fab15 in Egypt, I noticed that Sherry Lassiter is extremely proficient at typing. At that point, I decided to learn. There's an advantage when you learn something from scratch - you have no bad habits. So, I didn't learn the QWERTY system, which was originally designed to keep old typewriters from jamming. I learned using the [Colemak](https://colemak.com) system instead. Colemak is designed so that the most frequently used letters in English are on the home row. I have an [ortholinear keyboard](https://drop.com/buy/preonic-mechanical-keyboard) which I've set up with the Colemak layout, and I practice about five minutes a day. What I like most about the Colemak layout is that the backspace key is right next to the `A` key.

![](img/w01/preonic.webp)

I also have [software on macOS](https://karabiner-elements.pqrs.org) that changes my keyboard layout to Colemak and also switches the caps lock key function to backspace.

### My Text Editor
I intend to use only a command-line text editor. I know a bit of `vim` and want to deepen my learning. I like the idea of using only the keyboard to edit text. To avoid the temptation of using Visual Studio Code, I've uninstalled it. The vim text editor is quite sparse in its original form. Because of this, I will install some plugins. This is a list that I will expand over time:

- [NERDTree](https://github.com/preservim/nerdtree) to have a sidebar with a list of files, so I can quickly navigate between them.
- [vim-devicons](https://github.com/ryanoasis/vim-devicons) to visualize files and folders with a small graphic icon.

 Other useful links:

- [VimAwesome](https://vimawesome.com) is a webpage with hundreds of vim plugins
- [Fran's My Computing repo](https://github.com/TheBeachLab/myComputing) with some tricks, if you like using the command line.

### Multi-language Documentation with AI
Let's be realistic. I don't have much free time, and soon, I'll have even less. So, I need a system for documenting efficiently. I'm going to try a new technique for documenting that will allow me to have the documentation in two (or more) languages. Right now, most of the text you're reading is being dictated in Spanish to my Mac computer.

![](img/w01/dictation.webp)

This saves me some time when writing. Some parts, like the code, I have to type manually. I also have to do manual corrections, for example, when including links.

This way, I'm generating markdown files with documentation in Spanish. The reason why I'm not dictating directly in English is that my accent is so bad that the computer doesn't understand me. The name of the file for each week contains coded the week I'm in and the language of the documentation. In this case: `w01-es.md`. I'm going to use artificial intelligence to translate the text of that file into English and German and save it as `w01-en.md` and `w01-de.md`, respectively. The AI model has to be capable of recognizing Markdown syntax and preserving it. It also has to handle internal links, because the links that go to `w02-es.md` in the Spanish documentation have to be changed to `w02-en.md` in the English version of the documentation. As the model might improve (or even change) throughout Fab Academy, I will keep the text in Spanish and rerun the translation of all files every week. I will only edit the original file in Spanish. I won't manually manipulate the generated translation. So, if what you read in English or German doesn't make sense, blame OpenAI or whichever model I'm using.

I asked César Garcia, from [La Hora Maker](https://www.youtube.com/lahoramaker), for help in finding a model for translation. César recommended using OpenAI's Whisper API, which is capable of translating directly from audio in Spanish. For now, I'm only interested in the translation, so I created an assistant in the OpenAI API with these instructions:

> Translate the text from Spanish to English, Read the entire document to grasp context before translating it, take into account nuances and idioms of the Spanish language and translate them to the equivalents in English. The translation should not be literal, focus on maintaining the original meaning and provide a translation that makes sense in English. Ignore external URLs and code snippets in the translation; if encountering a markdown link, translate the text inside square brackets. Modify internal markdown link URLs to point to the appropriate English file, e.g., change w01-es.md to w01-en.md. Recognize and retain brands and names without translation. Use correct grammar and syntax in the final text. The style of the translation should be informal.

There's another model for German with similar instructions. I change the instructions now and then to try to improve the translation.

This page you're reading has about 2000 tokens. You can find out how many tokens a text has using the [OpenAI Tokenizer](https://platform.openai.com/tokenizer). The cost of translation is approximately 8 cents of a dollar, considering that every 1000 tokens cost 0.01 USD for the input and 0.03 USD for the output. It might seem little, but the cost will rise as Fab Academy progresses.

On my wishlist, I will continue looking for a local model.

### Automating the Translation Process
At first, I was using the OpenAI API window. Now, I've automated this process using python on the command line. Using a mix of Bing Copilot and the free version of ChatGPT, I asked them to use the OpenAI library for translation. After a lot of back and forth (AI doesn't usually generate correct code on the first try), I ended up frustrated and cursing out Bing.

![](img/w01/bing.webp)

In the end, I had to read the API documentation to make the program work.

Before translating pages that I've modified I must add them using `git add`. Thanks to that, I can limit and control the cost. Once that's done, I simply run `python translate-en.py`, and the script generates the Markdown pages translated into English. I do the same for German.

Normally, I don't perform this step in isolation because I've included it in the next step.

### Automating HTML Generation and File Upload
The Fab Academy documentation has to be presented in web page form. To generate HTML pages from markdown files, I translated a script from Bash language that I made for the [FabZero](https://github.com/Academany/fabzero) program to Python. The code converts all `.md` files to `.html` using [Pandoc](https://pandoc.org/index.html) with a [CSS style template](base.css). During conversion, if it finds a link to a markdown document, it converts it to a link to its corresponding HTML document using [this LUA filter](../links-to-html.lua).

The script also automates the translation from the previous section and the file upload to Github optionally. So, when I want to upload my progress, I write:

`python auto.py --translate updating week 1`

And thus, the script translates the pages if it finds `--translate` among the arguments. It also converts all pages to HTML and then uploads everything to Github as long as there is a message, in this case, it is `updating week 1`. If there is no message, it doesn't perform any of the git-related processes.

You can see the script here: [auto.py](../auto.py)

### Using CD/CI in Github to Serve Web Pages

Let's see what I have so far on Github:

- My original `.md` files in Spanish
- The `.md` files translated by AI into English and German
- The `.html` pages for all the `.md` files generated by Pandoc.

The only thing missing now is a web server. And you can do this from Github by accessing the repository settings.

![](img/w01/cicd.webp)

This will create a file in `.github/workflows/static.yml`, from which I only had to modify the `runner`, because `runs-on: ubuntu-latest` didn't work. I changed it to `runs-on: ubuntu-22.04` and upon making a `commit`, the pages were automatically served.

### Final Result

[https://thebeachlab.github.io/backtofabacademy2024/](https://thebeachlab.github.io/backtofabacademy2024/)

### Conclusion
All of this is making writing documentation somewhat slow at this moment, and a bit tedious. But I believe that with this system, the speed will increase drastically week by week, and in the end, I'll be able to document quickly and in great detail.

Furthermore, I believe this method will help many people who can't express their talent because they don't speak another language. It's unfair for that to happen, and I hope AI helps people demonstrate how valuable they are.

## Git: That Bottomless Pit
Someone might think that because I've been using git for 10 years I know everything there is to know about the version control system. Far from it. Here are the things I want to improve during this Fab Academy cycle:

- Suppressing my tendency to push changes to the main branch. Usually, it doesn't matter, but I need to get used to creating a new branch for each change.

(to be continued...)

## Project Management
(to be continued...)

## Sketch of the Final Project
Everything related to the final project has been moved to its [corresponding section](final-en.md).

[<< Back to the beginning](index-en.md)  
[Next week >>](w02-en.md)