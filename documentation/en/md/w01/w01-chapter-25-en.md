### Automating the Translation Process
At first, I was using the OpenAI API console. Now, I have automated this process using Python on the command line. By mixing Bing Copilot and the free version of ChatGPT, I requested a program that would automate translation using the OpenAI library. However, it didn’t go well. After quite a bit of back-and-forth (AI usually doesn’t generate correct code on the first try), I ended up frustrated and cursing at Bing.

![](../../img/w01/bing.webp)

Eventually, I had to read the API documentation to get the program working.

To avoid unnecessary extra costs, the script only translates the Spanish chapters that I have added using `git add`. Thanks to this, I can better control the cost. Once that's done, I simply execute `python translate-en.py`, and the script generates the Markdown pages translated into English. I do the same for German.

In reality, I usually don’t do the translation in isolation because I’ve incorporated it into the next step.

