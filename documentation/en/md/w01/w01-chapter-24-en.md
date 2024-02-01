### AI-Powered Automatic Translations

At Fab Academy, all documentation must be in English. Traditional language translators often fall short. They fail to understand context and produce results that don't sound natural. I plan to use artificial intelligence to translate the text of the chapters into English and also into German.

The AI model needs to be capable of recognizing Markdown syntax and respecting it. It will also need to handle internal links, because the links that go from `w02-es.md` in the Spanish documentation need to be changed to `w02-en.md` in the English version of the documentation. It's possible that the model might improve (or even change) throughout fab academy. Therefore, I'll keep the text in Spanish and rerun the translation of all the files from time to time. I will only edit the files in Spanish. I won't manually manipulate the generated translations. So, if what you read in English or German doesn't make sense, blame OpenAI or whatever model I'm using.

I asked César Garcia, from [La Hora Maker](https://www.youtube.com/lahoramaker), to help me find a model for the translation. César recommended using OpenAI's Whisper API, which is capable of translating directly from Spanish audio. For now, I'm only interested in translation, so I've created an assistant in the OpenAI API with the following instructions:

```
Translate the text from Spanish to English, Read the entire document to grasp context before translating it, take into account nuances and idioms of the Spanish language and translate them to the equivalents in English. The translation should not be literal, focus on maintaining the original meaning and provide a translation that makes sense in english. Ignore external URLs and code snippets in the translation; if encountering a markdown link, translate the text inside square brackets. Modify internal markdown link URLs to point to the appropriate english file, e.g., change w01-es.md to w01-en.md. Recognize and retain brands and names without translation. Use correct grammar and syntax in the final text. The style of the translation should be informal.
```

I have another model in German with similar instructions. I've been changing the instructions from time to time to try to improve the translation.

The page you're reading is about 4000 tokens. You can find out how many tokens a text has using the [OpenAI Tokenizer](https://platform.openai.com/tokenizer). The cost of translating this page into the two languages is roughly 0.32 USD, considering that each 1000 tokens cost 0.01 USD for the input and 0.03 USD for the output. I find it quite expensive, and moreover, the cost is going to rise as Fab Academy progresses. For this reason, I will only translate the contents when I consider the work to be advanced.

So far, the translations are quite good. Sometimes it doesn't change the links correctly, so in the future, I will perform that task through a script which is more reliable. I asked [Sophia Döring](https://fabacademy.org/2024/labs/kamplintfort/students/sophia-doring/) to also review the German translation. She told me that overall it is quite good, although sometimes it uses German words that are rarely used, especially for technical terms. That might be caused by how I write the original text. I'm using Spanish equivalents for technical terms that I actually say in English in everyday life.

On my wish list, I'll keep looking for a local model. That way, I can translate content more frequently. For now, I've been testing the `Phi 2` and `Yarn Mistral` models with disastrous results.

