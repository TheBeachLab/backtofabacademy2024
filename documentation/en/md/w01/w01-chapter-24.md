## AI-Assisted Translations
At Fab Academy, documentation must be in English. Traditional language translators aren't up to snuff. They fail to grasp the context and churn out results that sound funky. I'm bringing an artificial intelligence to the mix to translate the text of the chapters into English and also into German.

The AI model needs to get a grip on Markdown syntax and keep it intact. The model might get better (or even change) throughout Fab Academy. Hence, I'll keep the Spanish text as is and rerun the translations on all files now and then. I'm only tweaking the files in Spanish. I won't fiddle manually with the generated translations. So, if what you're reading in English or German seems like gobbledygook, blame it on OpenAI or whatever model I'm rolling with.

I hit up César Garcia, from [La Hora Maker](https://www.youtube.com/lahoramaker), to scout for a model for this translation gig. César recommended the Whisper API from OpenAI, which can translate straight from Spanish audio. For now, I'm only after the translation, so I've set up an assistant in the OpenAI API with these instructions[^243]

```
This file contains text with a mixture of markdown, yaml, pandoc and latex formatting. Translate the text from Spanish to English. Read the entire document to grasp context before translating it. Take into account nuances and idioms of the Spanish language and translate them to the equivalents in English. The translation should not be literal, focus on maintaining the original meaning and provide a translation that makes sense in english. Keep the formatting intact in the translated text, like footnotes, smallcaps, etc .Translate only the text within quotes in the YAML header of the Markdown file. Do not translate the latex notation, links, URLs, blocks of code and code snippets. If encountering a markdown link, only translate the text inside square brackets. Recognize and retain brands and names without translation. Use correct grammar and syntax in the final text. The style of the translation should be informal, with a touch of sarcastic humor.
```

Besides these general instructions, sometimes I need to pass a specific note to the translator. I've got a *hack* for adding special instructions in the markdown files. These comments show up in the markdown page, so the translator can read them. However, Pandoc ignores them, and they don't appear on the web page. Brilliant, right?

```markdown
[comment1]: <> (Note for the translator: Do not translate "hack" as it is universally used in all languages.)
```

[comment1]: <> (Note for the translator: Do not translate "hack" as it is universally used in all languages.)

[^243]:
    I've got another model for German with similar instructions. I tweak the instructions now and then to try and improve the translations. 

After a fortnight of use, I can say the English translations are pretty darn good. Way better than what I'd muster, with a caveat: It seems that at times the system dumbs down. I've read other users griping about the same. It's as if OpenAI can throttle or limit the resources allocated to the model. I got [Sophia Döring](https://fabacademy.org/2024/labs/kamplintfort/students/sophia-doring/) to check out the German translation too. She reckons it's generally on point, albeit occasionally it throws out some German words that are rarely used[^242], especially for technical terms. 

[^242]: That might be triggered by how I pen the original text. I use Spanish equivalents of technical terms that, in everyday speech, I actually say in English.

This page you're reading is about 4000 tokens long. You can figure out how many tokens a piece of text has using the [OpenAI Tokenizer](https://platform.openai.com/tokenizer). Translating this page into both languages costs roughly 0.32 USD, considering each 1000 tokens cost 0.01 USD for input and 0.03 USD for output. The cost is manageable, given the quality. I'm signing up for this solution when I want to go global with my projects. At Fab Academy, I understand and brace for a considerable expense, given the multiple tweaks I'll make on each page.

On my wishlist, I'm still scouting for a local model. That way, I can translate content more often without sweating the cost. I recently tested the `Miqu-1-70b` model[^241], with slow but satisfying outcomes. I see light at the end of the tunnel.

[^241]: [Supposedly](https://the-decoder.com/unintentional-ai-leak-from-mistral-becomes-an-unexpected-powerhouse/) leaked by an employee by accident. Miqu-1-70b might be a strong contender against GPT4

