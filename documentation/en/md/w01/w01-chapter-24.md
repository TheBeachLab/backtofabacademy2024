### AI-driven automatic translations
At Fab Academy, documentation has to be in English. Traditional language translators are pretty bad. They can't understand context and produce results that don't sound natural. I'll be using artificial intelligence to translate the text of the chapters into English and also into German.

The AI model must be able to recognize Markdown syntax and respect it. The model may improve (or even change) throughout Fab Academy. That's why I'll keep the text in Spanish and rerun the translations on all files from time to time. I will only edit the files in Spanish. I won't manually manipulate the generated translations. So, if what you read in English or German makes no sense, blame OpenAI or whichever model I'm using.

I asked César Garcia, from La Hora Maker, to help me find a model for translation. César recommended using OpenAI's Whisper API, which can translate directly from Spanish audio. For now, I'm only interested in the translation, so I created an assistant in the OpenAI API with these instructions:

```
Translate the text from Spanish to English. Read the entire document to grasp the context before translating it. Take into account nuances and idioms of the Spanish language and translate them into their English equivalents. The translation should not be literal, focusing on maintaining the original meaning and providing a translation that makes sense in English. Only translate the text within quotes in the YAML header of the Markdown file. Do not translate links, URLs, blocks of code, and code snippets. If encountering a markdown link, only translate the text inside square brackets. Recognize and retain brands and names without translation. Use correct grammar and syntax in the final text. The style of the translation should be informal, with a touch of sarcastic humor.
```

I have another model in German with similar instructions. I keep changing the instructions from time to time to try and improve the translation.

This page you're reading has about 4000 tokens. You can find out how many tokens a text has using the OpenAI Tokenizer. The cost of translating this page into the two languages is approximately 0.32 USD, considering that every 1000 tokens cost 0.01 USD for the input and 0.03 USD for the output. It seems pretty expensive to me, and the cost will go up as Fab Academy progresses. For that reason, I will only translate contents when I consider the work advanced.

For the moment, the English translations are quite good. I asked [Sophia Döring]() to also review the German translation. She said that, in general, it's also quite good, although sometimes it uses German words that are infrequently used, especially for referring to technical terms.

In my wish list, I will continue looking for a local model. That way, I can translate the content more frequently and without worrying about the cost. I recently tried the `Miqu-1-70b`[^241] model with slow but satisfactory results. I see light at the end of the tunnel.

[^241]: Note 

