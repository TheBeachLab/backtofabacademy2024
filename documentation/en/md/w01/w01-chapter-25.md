### Automating the Translation
Initially, I was using the OpenAI API window. Now, I've automated this process with a Python script. Using a mix of Bing Copilot and the free version of ChatGPT, I asked for a program that would automate the translation using the OpenAI library. But it didn't go well. After a lot of back-and-forth (AI doesn't usually generate correct code on the first try), I ended up frustrated and cursing at Bing.

In the end, I had to read the API documentation to make the program work.

To avoid unnecessary extra costs, the script only translates Spanish chapters that I've added using `git add`. Thanks to this, I can better control the cost. Once done, I simply run `python translate-en.py` and the script generates the Markdown pages translated to English. I do the same for German.

Actually, I usually don't do the translation in isolation, because I've included it in the next step.

