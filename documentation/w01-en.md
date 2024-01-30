# Week 1: Principles and Practices, Project Management

 > *Task A:*
 >
 > Plan and sketch a potential final project.
 >
 > *Task B:*
 >
 > Work through a Git tutorial step by step.
 > Build a personal site in the class repository describing you and your final project.

## Reinventing the Way of Documenting

### macOS Again? How Could You Sink So Low?
Let me see how I can explain this... I'll explain another day.

### Colemak?
I never knew how to touch type, even though I always wanted to learn. While working on the organization of Fab15 in Egypt, I noticed that Sherry Lassiter has a great skill for typing. At that moment, I decided to learn. When you learn something from scratch, there's an advantage - you have no bad habits. So, I didn't learn the QWERTY system, which was originally designed to prevent old typewriters from jamming. I learned using the [Colemak](https://colemak.com) system. Colemak is designed so that the most frequently used letters in the English language are on the home row. I have an [ortho-linear keyboard](https://drop.com/buy/preonic-mechanical-keyboard) to which I've applied the Colemak layout, and I practice about five minutes a day. What I like most about the Colemak layout is that the backspace key is right next to the `A` key.

![](img/w01/preonic.webp)

I also have [software on macOS](https://karabiner-elements.pqrs.org) that changes my keyboard layout to Colemak and also changes the function of the caps lock key to backspace.

### My Text Editor
My intention is to use only a command-line text editor. I have some knowledge of `vim` and I want to delve deeper. I like the idea of using only the keyboard to edit text. To avoid the temptation of using Visual Studio Code, I've uninstalled it. The vim text editor is quite basic by default. Therefore, I'm going to install some plugins. Here is a list that I will expand over time:

- [NERDTree](https://github.com/preservim/nerdtree) to have a sidebar with a file listing, so you can quickly navigate between files.
- [vim-devicons](https://github.com/ryanoasis/vim-devicons) to visualize files and folders with small graphic icons.

Other useful links:

- [VimAwesome](https://vimawesome.com) is a page with hundreds of vim plugins.
- [Fran's My Computing repo](https://github.com/TheBeachLab/myComputing) with some tricks, if you like using the command line.

### Multi-language Documentation Transcription with AI
Let's face it. I don't have much free time and soon I'll have even less. So, I need a system to write documentation quickly. I'm going to try a new technique for documenting that will allow me to have documentation in two (or more) languages. Right now, most of the text you're reading is being dictated in Spanish to my Mac computer.

![](img/w01/dictation.webp)

This saves me some time when writing. Some parts, like the code, I have to write manually. I also have to make corrections manually, for example, when including links.

This way, I'm generating markdown files with the documentation in Spanish. The file name contains the week I'm in and the documentation language. In this case: `w01-es.md`. I'm going to use an artificial intelligence to translate the text from that file into English and save it as `w01-en.md`. The reason why I'm not dictating directly in English is that my accent is so bad that the computer doesn't understand me. The artificial intelligence model must be able to recognize Markdown syntax and respect it. It must also manipulate internal links because links that go `w02-es.md` in the Spanish documentation have to be changed to `w02-en.md` in the English version of the documentation. As the model may improve (or even change) throughout the Fab Academy, I'll keep the text in Spanish and re-run the translation of all files every week. I will only edit the original file in Spanish. I will not manually manipulate the generated translation. So, if what you read in English doesn't make sense, blame it on OpenAI or the model I'm using.

I asked César Garcia, from [La Hora Maker](https://www.youtube.com/lahoramaker), to help me find a model for the translation. César recommended using the OpenAI Whisper API, which is capable of translating directly from Spanish audio. For now, I'm only interested in translation, so I created an assistant in the OpenAI API with these instructions:

> Translate the text from Spanish to English, considering nuances and idioms. Read the entire document to grasp context before translating, maintaining the original meaning even if not literal. Ignore URLs and code snippets in the translation; if encountering a markdown link, translate the text inside square brackets. Modify internal markdown link URLs to point to the appropriate English file, e.g., change w01-es.md to w01-en.md. Recognize and retain brands and names without translation. Capitalize titles in the final text. The style of the translation should be informal.

I'm changing the instructions from time to time to try to improve the translation. This page you're reading has about 1900 tokens. You can find out how many tokens a text has using the [OpenAI Tokenizer](https://platform.openai.com/tokenizer). The cost of the translation is approximately 8 cents, taking into account that each 1000 tokens cost 0.01 USD for the input and 0.03 USD for the output. It may seem little, but the cost will increase as Fab Academy progresses.

On my wish list, I'm still looking for a local model.

### Automating the Translation Process
At first, I was using the OpenAI API window. Now I've automated this process using python on the command line. Using a mix of Bing Copilot and the free version of ChatGPT I asked it to use the OpenAI library to do the translation. After quite a tug of war (AI doesn't usually generate correct code on the first try), I ended up frustrated and insulting Bing.

![](img/w01/bing.webp)

In the end, I had to read the API documentation to make the program work.

Before translating the pages I have modified I must add them using `git add`. Thanks to this, I can limit and control the cost. Once done, I simply run `python translate.py` and the script generates the translated Markdown pages.

### Automating the Generation of HTML and Upload of Files
I translated a Bash script that I made for the [FabZero](https://github.com/Academany/fabzero) program into Python. The code converts all `.md` files into `.html` using [Pandoc](https://pandoc.org/index.html). During conversion, if it finds a link to a markdown document, it converts it into a link to its corresponding HTML document using [this LUA filter](../links-to-html.lua). You can see the script here: [auto.py](../auto.py)

The script also automates the git process. So, when I want to upload my progress I write:

`python auto.py updating week 1`

And it converts all the pages to HTML and then uploads everything to GitHub with the message `updating week 1`.

### Conclusion

All this is making writing documentation a bit slow at the moment, and a bit tedious. But I believe that with this system, the speed is going to increase drastically week by week, and in the end, I'll be able to document with great speed and level of detail.

## Git: That Bottomless Pit

Someone might think that because I've used git for 10 years, I know everything there is to know about the version control system. Not at all. Here are the things I want to improve during this cycle of Fab Academy:

- Suppress my tendency to upload changes to the main branch. Normally it's not a problem, but I have to get used to creating a new branch for each change.

(to be continued...)

## Project Management

(to be continued...)

## Sketch of the Final Project

Everything related to the final project has been moved to the file [final-es](final-es.md).

[<< Back to beginning](index-en.md)  
[Next week >>](w02-en.md)