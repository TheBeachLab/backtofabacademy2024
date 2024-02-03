### AI-assisted translations
At [Fab Academy]{.smallcaps}, documentation must be in English. Traditional language translators are pretty lousy. They can't understand context and produce results that don't sound natural. I'll use artificial intelligence to translate the text from the chapters into English and also into German.

The AI model has to be capable of recognizing Markdown syntax and able to respect it. The model might improve (or even change) throughout Fab Academy. That's why I'll keep the text in Spanish and rerun the translation on all files from time to time. I'm only going to edit the files in Spanish. I won’t manually manipulate the generated translations. So if what you read in English or German doesn't make sense, blame OpenAI or whatever model I'm using.

I've asked César Garcia, from [La Hora Maker](https://www.youtube.com/lahoramaker), to help me find a model for the translation. César recommended using the OpenAI Whisper API, which is capable of translating directly from Spanish audio. For now, I'm only interested in the translation, so I've created an assistant in the OpenAI API with these instructions:

```
This file contains text with a mixture of markdown, yaml, pandoc and latex formatting. Translate the text from Spanish to English. Read the entire document to grasp context before translating it. Take into account nuances and idioms of the Spanish language and translate them to the equivalents in English. The translation should not be literal, focus on maintaining the original meaning and provide a translation that makes sense in english. Keep the formatting intact in the translated text, like footnotes, smallcaps, etc .Translate only the text within quotes in the YAML header of the Markdown file. Do not translate the latex notation, links, URLs, blocks of code and code snippets. If encountering a markdown link, only translate the text inside square brackets. Recognize and retain brands and names without translation. Use correct grammar and syntax in the final text. The style of the translation should be informal, with a touch of sarcastic humor.
```

I have another model in German with similar instructions. I keep changing the instructions from time to time to try to improve the translation.

This page you're reading has about 4000 tokens. You can find out how many tokens a text has using the [OpenAI Tokenizer](https://platform.openai.com/tokenizer). The cost of translating this page into both languages is approximately 0.32 USD, considering that each 1000 tokens cost 0.01 USD for input and 0.03 USD for output. I find it quite expensive, and the cost will go up as Fab Academy progresses. For that reason, I'll only translate the contents when I consider the work to be advanced.

For the moment, the English translations are quite good. I asked [Sophia Döring](https://fabacademy.org/2024/labs/kamplintfort/students/sophia-doring/) to also review the German translation. She told me that, in general, it's also quite good, although sometimes it uses rarely used German words[^242], especially for referring to technical terms.

[^242]: That might be caused by how I write the original text. I'm using the Spanish equivalents of technical terms that, in everyday life, I actually say in English.

In my wishlist, I will continue searching for a local model. That way, I can translate the content more frequently and without worrying about the cost. Recently, I've tried the `Miqu-1-70b`[^241] model with slow but satisfying results. I see light at the end of the tunnel.

[^241]: [Supposedly](https://the-decoder.com/unintentional-ai-leak-from-mistral-becomes-an-unexpected-powerhouse/) leaked unintentionally by an employee. Miqu-1-70b might be a good competitor to GPT4.

