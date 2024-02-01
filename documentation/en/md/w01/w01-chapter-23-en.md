### File Structure
In this way, I am generating Markdown files with documentation in Spanish. At first, I wrote the text for each week in a single file. But as you'll read later on, I use a paid service for translation. Every time I edited a line, I had to translate the whole file again. To cut down on costs, I now divide the week into chapters and create a file for each chapter. This way, only the chapters I've modified get translated. My file structure is inspired by the programming language [BASIC](https://en.wikipedia.org/wiki/BASIC):

```
/documentation
    /es
        /md
            /w01
                w01-chapter-00-es.md
                w01-chapter-10-es.md
                w01-chapter-20-es.md
                w01-chapter-21-es.md
                ...
                w01-chapter-90-es.md
                w01-chapter-99-es.md
```

The name of each week's file encodes the week number, chapter, and language of the documentation. Chapter 00 is the header. I use chapters 10, 20, 30... to develop the sections of the week. If a chapter is too long, I subdivide it using the intermediate numbers: 20, 21, 22, etc. Chapter 90 is always the conclusion, and 99 is the footer.

Later, I concatenate all the chapters of the week into a single file, in this case: `w01-es.md`.

> **Important Note:** I never manually edit the concatenated file. I only edit the separate chapters.

