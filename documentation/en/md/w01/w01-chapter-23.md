## File Structure
In the beginning, I used to write the text for each week in a single file. But as you'll read later, I use a paid service for translation. Every time I edited a line, I had to translate the entire file again. To cut costs, I've divided the week into chapters[^231] and created a file for each chapter. That way, only the chapters I've modified get translated.

[^231]: My file structure is inspired by the programming language [BASIC](https://en.wikipedia.org/wiki/BASIC)

```
/documentation
    /es
        /md
            /w01
                w01-chapter-00.md
                w01-chapter-10.md
                w01-chapter-20.md
                w01-chapter-21.md
                ...
                w01-chapter-90.md
```

The file name encodes the week I'm in and the chapter. Chapter 00 is the header. I use chapters 10, 20, 30... to develop the sections of the week. If a chapter gets too long, I subdivide it using intermediate numbers: 20, 21, 22, etc. Chapter 90 is always the conclusion.

Later, I concatenate[^232] all the chapters of the week into a single file, in this case, `w01.md`.

[^232]: **Important Note:** I never manually edit the concatenated file. I only edit the separate chapters.

