### Automating Translation
[Initially]{.smallcaps}, I was using the OpenAI API window. Now, I've automated this process with a Python script. Using a mix of Bing Copilot and the free version of ChatGPT, I requested a program that could automate translation using OpenAI's library. But it didn't go well. After a lot of back-and-forth (AI doesn't usually spit out correct code on the first try), I ended up losing my mind and hurling insults at Bing.

![](../../img/w01/bing.webp)

In the end, I had to read the API documentation to make the program work.

To avoid unnecessary extra costs, the script only translates the chapters in Spanish that I've added using `git add`. Thanks to this, I can control the costs better. Once this is done, I just run `python translate-en.py`, and the script generates the Markdown pages translated to English. I do the same for German.

Actually, I usually don't do the translation in isolation, because I've included it in the next step.

