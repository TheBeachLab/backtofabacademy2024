[At Fab Academy]{.smallcaps}, all the documentation must be in English. Traditional language translators are kinda bad. They can't grasp context and end up churning out results that sound about as natural as a robot at a poetry slam. I'm gonna use artificial intelligence to translate the text into English and German because why not?

The AI model needs to have the chops to recognize Markdown syntax and keep it intact. The model might get better (or even switch up) throughout Fab Academy. So, I'm sticking to editing texts in Spanish and I'll rerun the translations on all the files now and then. I won't manually fiddle with the translations. So, if what you're reading in English or German seems like gobbledygook, blame it on OpenAI or whatever model I'm using at the moment.

I got in touch with César Garcia from [La Hora Maker](https://www.youtube.com/lahoramaker), asking him to scout out a translation model for me. César recommended using OpenAI's Whisper API, which can translate straight from Spanish audio. For now, I'm only interested in text translation, so I've set up an assistant in the OpenAI API with these instructions:

"Translate the text from Spanish to English. Read the entire document to grasp the context before translating it. Take into account the nuances and idioms of the Spanish language and translate them to the equivalents in English. The translation shouldn't be literal; focus on maintaining the original meaning and provide a translation that makes sense in English. Translate only the text within quotes in the YAML header of the Markdown file. Do not translate links, URLs, blocks of code, and code snippets. If encountering a markdown link, only translate the text inside square brackets. Recognize and retain brands and names without translation. Use correct grammar and syntax in the final text. The style of the translation should be informal, with a touch of sarcastic humor."

I've got another model for German with similar instructions. I keep tweaking the instructions now and then to try to improve the translations.

This page you're reading clocks in at about 4000 tokens. You can find out how many tokens a piece of text has using the [OpenAI Tokenizer](https://platform.openai.com/tokenizer). Translating this page into both languages costs roughly 0.32 USD, considering every 1000 tokens cost 0.01 USD for input and 0.03 USD for output. It seems pretty steep to me, and the cost is bound to climb as Fab Academy rolls on. That's why I'll only translate content when I deem the work to be advanced enough.

So far, the English translations are coming out pretty darn good. I asked [Sophia Döring](https://fabacademy.org/2024/labs/kamplintfort/students/sophia-doring/) to also check out the German translation. She said it's generally pretty good too, though occasionally it uses some rarely used German words[^242], especially for technical terms.

[^242]: This might be caused by how I write the original text. I'm using the Spanish equivalents of technical terms that, in everyday conversation, I actually express in English.

On my wishlist, I'm keeping an eye out for a local model so I can translate content more often and not worry about the cost. I recently tested the `Miqu-1-70b`[^241] model with slow but satisfying results. I see light at the end of the tunnel.

[^241]: [Allegedly](https://the-decoder.com/unintentional-ai-leak-from-mistral-becomes-an-unexpected-powerhouse/) leaked unintentionally by an employee. Miqu-1-70b could be a strong competitor to GPT-4.

