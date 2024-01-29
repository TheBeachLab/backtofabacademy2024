# Week 1: Principles and Practices, Project Management

 > *Task A:*
 >
 > Plan and sketch a potential final project.
 >
 > *Task B:*
 >
 > Perform a step-by-step Git tutorial.  
 > Build a personal site in the class repository describing yourself and your final project.

## Reinventing the Multi-Language Documentation Approach with AI.

Let's face it. I don't have much free time, and soon, I will have even less. So, I need a system for writing documentation efficiently. I'm going to try a new documentation technique that will allow me to have documentation in two (or more) languages. Right now, most of the text you are reading is being dictated in Spanish to my Mac computer.

![dictation settings](img/w01/dictation.webp)

This saves me some time when writing. Some parts, like code, I have to type manually. I also have to make manual corrections, for example, when including links.

In this way, I am generating markdown files with documentation in Spanish. The filename encodes the week I am in and the language of the documentation. In this case: `w01-es.md`. I'm going to use artificial intelligence to translate the text of that file into English and save it as `w01-en.md`. The reason why I don't dictate directly in English is that my accent is so bad that the computer doesn't understand me. The artificial intelligence model has to be capable of recognizing the Markdown syntax and being able to respect it. It will also have to handle internal links, because links going to `w02-es.md` in the Spanish documentation have to be changed to `w02-en.md` in the English version of the documentation. As it's possible that the model may improve (or even change) throughout fab academy, I will keep the text in Spanish and run the translation of all files every week again. I will only edit the original file in Spanish. I will not manually manipulate the generated translation. So if what you read in English doesn't make sense, blame OpenAI or the model I am using.

I asked César García, from [La Hora Maker](https://www.youtube.com/lahoramaker), to help me find a model for the translation. César recommended me to use OpenAI's Whisper API, which is capable of translating directly from Spanish audio. For now, I'm only interested in translation, so I have created an assistant in the OpenAI API with these instructions:

> You are an expert translator from Spanish to English. You know the nuances and idioms of the Spanish language and translate them into the appropriate idioms of the English language. You ignore URLs in the translations. If you find a markdown link, you translate the text inside the square brackets if necessary. You will modify the internal URL of the markdown link so that it points to the appropriate markdown file in English. For example, you will change a markdown link that points to w01-es.md to make it point to w01-en.md. But remember, you will only do that for the markdown links. You can recognize brands and names so that you avoid translating them. You will also fix the original text by capitalizing titles and fixing any other syntax or grammar error before translating it. You deliver the answers in code rather than rendering the markdown in HTML, so that I can copy the markdown syntax.

For now, I'm using OpenAI's API window. Translating this page you're reading has cost me about 1500 tokens. You can find out how many tokens the translation will cost you using the [OpenAI Tokenizer](https://platform.openai.com/tokenizer)

The next step is to automate this process using the command line. On my wish list, I will continue to look for a model that is local. I don't want to use a web service.

## Text Editor
My intention is to use only a text editor on the command line. I have some notions of vim and I want to delve deeper into learning. I like the idea of using only the keyboard to edit text. To avoid the temptation of using Visual Studio Code, I have uninstalled it. The vim text editor is quite spartan by origin. Therefore, I am going to install some plugins. Here is a list that I will be expanding over time:

- [NERDTree](https://github.com/preservim/nerdtree) to have a sidebar with the file listing, and thus be able to navigate quickly between files.
- [vim-devicons](https://github.com/ryanoasis/vim-devicons) to visualize files and folders with a small graphic icon.
- 

Other useful links:

- [VimAwesome](https://vimawesome.com)
- [Fran's My Computing repo](https://github.com/TheBeachLab/myComputing) with some tricks, if you like using the command line.

## Keyboard Layout

I never knew how to type, but I always wanted to learn. At Fab15 in Egypt, I noticed Sherry Lassiter, she has a great ability to type. At that moment, I decided to learn. There's an advantage when you learn something late, and that is that you have no bad habits. So, I didn't learn the QWERTY system. I learned directly the [Colemak](https://colemak.com) system. I have an [ortholinear keyboard](https://drop.com/buy/preonic-mechanical-keyboard), and I practice about five minutes a day. I also have [software on macOS](https://karabiner-elements.pqrs.org) that changes my keyboard layout and also changes the function of the caps lock key to backspace.

All this is making writing the documentation a bit slow at the moment, and a bit tedious. But I believe that with this system, speed will drastically increase week by week and in the end, I will be able to document with great speed and level of detail.

[<< back to home](index-en.md)  
[Next week >>](w02-en.md)