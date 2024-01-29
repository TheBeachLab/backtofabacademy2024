# Week 1. Principles and Practices, Project Management

 > *Task A:*
 >
 > Plan and sketch a potential final project.
 >
 > *Task B:*
 >
 > Complete a step-by-step Git tutorial.  
 > Build a personal site in the class repository describing yourself and your final project.


## Reinventing the Way of Documenting

### Transcribing Multi-Language Documentation with AI.

Let's face it. I don't have much free time and soon, I will have even less. Thus, I need a system to write documentation efficiently. I am going to try a new technique for documenting that will allow me to have the documentation in two (or more) languages. Currently, most of the text you are reading is being dictated in Spanish to my Mac computer.

![](img/w01/dictation.webp)

This saves me some time when writing. Some parts, like code, I have to type manually. I also have to manually make corrections, for example, when I include links.

This way, I am generating markdown files with the documentation in Spanish. The filename includes coded the week I am in and the language of the documentation. In this case: `w01-es.md`. I am going to use artificial intelligence to translate the text from that file into English and save it as `w01-en.md`. The reason why I do not dictate directly in English is that my accent is so bad that the computer does not understand me. The AI model has to be capable of recognizing the Markdown syntax and be able to respect it. It will also have to manipulate the internal links, because links going to `w02-es.md` in the Spanish documentation have to be changed to `w02-en.md` in the English version of the documentation. As it is possible that the model will improve (or even change) throughout Fab Academy, I will keep the text in Spanish and re-run the translation of all files every week. I will only edit the original file in Spanish. I will not manually manipulate the generated translation. So, if what you read in English does not make sense, blame OpenAI or the model I am using.

I asked César Garcia, from [La Hora Maker](https://www.youtube.com/lahoramaker), to help me find a model for the translation. César recommended using the OpenAI Whisper API, which is capable of translating directly from audio in Spanish. For now, I am only interested in the translation, so I've created an assistant in the OpenAI API with these instructions:

> You are an expert translator from Spanish to English. You know the nuances, and idioms of the Spanish language and translate them into the appropriate idioms of the English language. You ignore URLs in the translations. If you find a markdown link, you translate the text inside the square brackets if necessary. You will modify the internal URL of the markdown link so that it points to the appropriate markdown file in English. For example, you will change a markdown link that points to w01-es.md to make it point to w01-en.md. But remember, you will only do that for the markdown links. You can recognize brands and names so that you avoid translating them. You will also fix the original text by capitalizing titles and fixing any other syntax or grammar error before translating it. You deliver the answers in code rather than rendering the markdown in HTML, so that I can copy the markdown syntax.

Translating this page you are reading has cost me about 2000 tokens. You can find out how many tokens the translation will cost you using the [OpenAI Tokenizer](https://platform.openai.com/tokenizer).

At first, I was using the OpenAI API window. Now, I have automated this process using the command line. Using [Bing Copilot](), I have transformed a Bash script that I made for the [FabZero]() program into Python and asked it to use the OpenAI library to perform the translation. After a bit of back and forth (AI does not usually generate correct code on the first attempt), Bing has generated a script that works. You can see the script here: [auto.py](auto.py)

On my wish list, I will continue searching for a model that is local. I do not want to use a web service.

### Text Editor
My intention is to use only a text editor in the command line. I have some knowledge of vim and I want to deepen my learning. I like the idea of using only the keyboard to edit text. To avoid the temptation of using Visual Studio Code, I have uninstalled it. The vim text editor is quite spare by origin. Therefore, I am going to install some plugins. This is a list that I will expand over time:

- [NERDTree](https://github.com/preservim/nerdtree) to have a sidebar with a list of files, so that I can quickly navigate between files.
- [vim-devicons](https://github.com/ryanoasis/vim-devicons) to visualize files and folders with small graphic icons.
- 

 Other useful links:

- [VimAwesome](https://vimawesome.com)
- [Fran's My Computing repo](https://github.com/TheBeachLab/myComputing) with some tricks, if you like using the command line.

### Keyboard Layout

I never knew how to type, but I always wanted to learn. At Fab15 in Egypt, I noticed Sherry Lassiter, who has great typing skills. At that moment, I decided to learn. There is an advantage when you learn something late, and that is you have no bad habits. So, I did not learn the QWERTY system. I learned directly the [Colemak](https://colemak.com) system. I have an [ortholinear keyboard](https://drop.com/buy/preonic-mechanical-keyboard), and I practice about five minutes a day. I also have a [software on macOS](https://karabiner-elements.pqrs.org) that changes my keyboard layout and also changes the function of the caps lock key to backspace.

### Conclusion

All of this is making writing the documentation a bit slow at this moment, and a bit tedious. But I believe that with this system, the speed will drastically increase week by week and in the end, I will be able to document with great speed and level of detail.

## Git: That Bottomless Pit

Someone might think that because I have been using git for 10 years I know everything there is to know about the version control system. Not at all. These are the things I want to improve during this Fab Academy cycle:

- Curb my tendency to push changes to the main branch. Normally nothing happens but I have to get used to creating a new branch for each change.

(to be continued...)

## Project Management

(to be continued...)

## Sketch of the Final Project

Everything related to the final project has been moved to the file [final-en](final-en.md).

[<< Back to the beginning](index-en.md)  
[Next Week >>](w02-en.md)