## AI-based Translations
[At Fab Academy]{.smallcaps}, documentation must be in English. Traditional language translators are pretty awful. They can't grasp context and produce results that don't sound natural. I'm going to use artificial intelligence to translate the text from these chapters into English and also into German.

The AI model needs to be able to recognize Markdown syntax and be able to respect it. The model might get better (or even change) throughout Fab Academy. That's why I'll keep the text in Spanish and will rerun the translation of all files now and then. I will only edit the files in Spanish. I will not manually manipulate the generated translations. So, if what you're reading in English or German doesn't make sense, blame it on OpenAI or whichever model I'm using.

I asked César Garcia from [La Hora Maker](https://www.youtube.com/lahoramaker) to help me find a model for translation. César recommended using the OpenAI Whisper API, capable of translating directly from Spanish audio. For now, I'm only interested in translations, so I've set up an assistant in the OpenAI API with these instructions[^243]

```
This file contains text with a mixture of markdown, yaml, pandoc, and latex formatting. Translate the text from Spanish to English. Read the entire document to grasp the context before translating it. Take into account nuances and idioms of the Spanish language and translate them to the equivalents in English. The translation should not be literal, focus on maintaining the original meaning and provide a translation that makes sense in English. Keep the formatting intact in the translated text, like footnotes, smallcaps, etc. Translate only the text within quotes in the YAML header of the Markdown file. Do not translate the latex notation, links, URLs, blocks of code, and code snippets. If encountering a markdown link, only translate the text inside square brackets. Recognize and retain brands and names without translation. Use correct grammar and syntax in the final text. The style of the translation should be informal, with a touch of sarcastic humor.
```

Besides these general instructions, sometimes I need to communicate something specific to the translator. I have a *hack* to add specific instructions in the markdown files. These comments appear on the markdown page, so the translator can read them. However, Pandoc ignores them, and they do not appear on the webpage. Brilliant!

```markdown
[comment1]: <> (Note for the translator: Do not translate "hack" as it is universally used in all languages.)
```

[comment1]: <> (Note for the translator: Do not translate "hack" as it is universally used in all languages.)

[^243]:
    I have another model in German with similar instructions. I switch the instructions now and then to try to improve the translation.

After two weeks of use, I can say that the English translations are very good. Much better than what I would do. I asked [Sophia Döring](https://fabacademy.org/2024/labs/kamplintfort/students/sophia-doring/) to also review the German translation. She said that, in general, it's also quite good, although sometimes it uses infrequently used German words[^242], especially for technical terms.

[^242]: That might be provoked by how I write the original text. I'm using the Spanish equivalents of technical terms that, in day-to-day life, I actually say in English.

This page you're reading has about 4000 tokens. You can find out how many tokens a text has using the [OpenAI Tokenizer](https://platform.openai.com/tokenizer). The cost of translating this page to both languages is approximately 0.32 USD, considering that each 1000 tokens cost 0.01 USD for the input and 0.03 USD for the output. This cost is acceptable, given the quality. I will adopt this solution when I wish to internationalize my projects. In Fab Academy, I understand and assume that the cost will be considerable, due to the multiple modifications I will make on each page.

In my wish list, I will continue looking for a local model. That way, I can translate contents more frequently and without worrying about the cost. I have recently tried the `Miqu-1-70b`[^241] model with slow but satisfactory results. I see light at the end of the tunnel.

[^241]: [Supposedly](https://the-decoder.com/unintentional-ai-leak-from-mistral-becomes-an-unexpected-powerhouse/) leaked by an employee unintentionally. Miqu-1-70b could be a strong competitor to GPT4

