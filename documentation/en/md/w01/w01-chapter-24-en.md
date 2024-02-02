### AI-Powered Automatic Translations
At Fab Academy, documentation must be in English. Traditional language translators are pretty terrible. They fail to understand context and produce results that don't sound natural. I'm planning to use artificial intelligence to translate chapter texts into English as well as German.

The AI model has to be capable of recognizing Markdown syntax and keeping it intact. It also needs to handle internal links, because links that go from `w02-es.md` in the Spanish documentation have to be changed to `w02-en.md` in the English version of the documentation. It's possible that the model might improve (or even change) throughout Fab Academy. That’s why I'll keep the text in Spanish and rerun the translation of all files now and then. I'm only going to edit files in Spanish. I will not manually manipulate the generated translations. So, if what you're reading in English or German doesn't make sense, blame OpenAI or whatever model I'm using.

I asked César Garcia from [La Hora Maker](https://www.youtube.com/lahoramaker) to help me find a model for translation. César recommended using OpenAI's Whisper API, which can translate directly from Spanish audio. For now, I'm only interested in translation, so I created an assistant in OpenAI's API with these instructions:

```
Translate the text from Spanish to English, Read the entire document to grasp context before translating it, take into account nuances and idioms of the Spanish language and translate them to the equivalents in English. The translation should not be literal, focus on maintaining the original meaning and provide a translation that makes sense in English. Translate only the text within quotes in the YAML header of the Markdown file. Do not translate external URLs, blocks of code and code snippets; if encountering a markdown link, only translate the text inside square brackets. Modify internal markdown link URLs to point to the appropriate English file, e.g., change w01-es.md to w01-en.md. Recognize and retain brands and names without translation. Use correct grammar and syntax in the final text. The style of the translation should be informal, with a touch of sarcastic humor.
```

I have another model in German with similar instructions. I keep tweaking the instructions now and then to try and improve the translation.

This page you're reading has about 4000 tokens. You can find out how many tokens a piece of text has using the [OpenAI Tokenizer](https://platform.openai.com/tokenizer). The cost of translating this page into both languages is approximately 0.32 USD, considering that each 1000 tokens cost 0.01 USD for the input and 0.03 USD for the output. That seems pretty pricey, and the cost is going to rise as Fab Academy progresses. For that reason, I'll only translate the content when I consider it to be advanced.

For now, the translations are quite good. Sometimes it doesn't correctly change the links, so in the future, I'll handle that task using a script which is more reliable. I asked [Sophia Döring](https://fabacademy.org/2024/labs/kamplintfort/students/sophia-doring/) to also check the German translation. She told me it's generally quite good, although sometimes it uses rarely-used German words, especially when referring to technical terms. That might be caused by the way I write the original text. I'm using the Spanish equivalents of technical terms that, in day-to-day speech, I actually say in English.

On my wish list, I'll keep looking for a local model. That way, I can translate content more frequently. For now, I've been trying out the `Phi 2` and `Yarn Mistral` models with disastrous results.

