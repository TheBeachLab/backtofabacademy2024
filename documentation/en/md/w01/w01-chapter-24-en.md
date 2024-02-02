### AI-Powered Automatic Translations
At Fab Academy, documentation must be in English. Traditional language translators are pretty terrible. They're unable to grasp context and produce results that sound anything but natural. I'll be using artificial intelligence to translate the chapter text into English and also into German.

The AI model needs to recognize Markdown syntax and keep it intact. It must also handle internal links, because links going to `w02-es.md` in the Spanish documentation need to be changed to `w02-en.md` in the English version of the documentation. It's possible that the model might improve (or even change) over the course of Fab Academy. That's why I'll keep the Spanish text and rerun the translation for all files now and again. I'm only going to tweak the files in Spanish. I won't manually fiddle with the generated translations. So, if what you're reading in English or German doesn't make sense, blame OpenAI or whichever model I'm using.

I reached out to César Garcia from [La Hora Maker](https://www.youtube.com/lahoramaker) to help me find a model for translations. César suggested using OpenAI's Whisper API, capable of translating directly from Spanish audio. For now, I'm only interested in the translation part, so I've set up an assistant in the OpenAI API with these instructions:

```
Translate the text from Spanish to English, Read the entire document to grasp context before translating it, take into account nuances and idioms of the Spanish language and translate them to the equivalents in English. The translation should not be literal, focus on maintaining the original meaning and provide a translation that makes sense in English. Translate only the text within quotes in the YAML header of the Markdown file. Ignore external URLs, blocks of code and code snippets in the translation; if encountering a markdown link, only translate the text inside square brackets. Modify internal markdown link URLs to point to the appropriate English file, e.g., change w01-es.md to w01-en.md. Recognize and retain brands and names without translation. Use correct grammar and syntax in the final text. The style of the translation should be informal, with a touch of sarcastic humor.
```

I have another model for German with similar instructions. I keep tweaking the instructions from time to time to try and improve the translations.

The page you're reading is about 4000 tokens. You can find out how many tokens a text has using the [OpenAI Tokenizer](https://platform.openai.com/tokenizer). Translating this page into both languages costs approximately 0.32 USD, considering that each 1000 tokens cost 0.01 USD for input and 0.03 USD for output. I find it quite pricey, and the cost will rise as Fab Academy progresses. For that reason, I will only translate the content when I consider the work to be sufficiently advanced.

So far, the translations are quite good. Sometimes it doesn't correctly change the links, so in the future, I'll carry out that task using a script, which is more reliable. I asked [Sophia Döring](https://fabacademy.org/2024/labs/kamplintfort/students/sophia-doring/) to also check the German translation. She said it's generally quite good, although sometimes it uses somewhat outdated German words, especially for technical terms. That might be caused by the way I write the original text. I use Spanish equivalents of technical terms that, in everyday life, I actually say in English.

On my wish list, I'll keep looking for a model that can be local. That way, I can translate the content more frequently. So far, I've been testing the `Phi 2` and `Yarn Mistral` models with disastrous results.

