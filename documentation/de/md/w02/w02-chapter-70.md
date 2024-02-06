# Bilder
[*in Entwicklung*]{.mark .yellow}


## Imagemagick

Es ist für unendlich viele Dinge nützlich. Du kannst ein Wasserzeichen zu einem Bild hinzufügen.\
Oder kombiniere zwei oder mehr Bilder horizontal so, dass:\
a) Sie die gleiche Höhe haben\
b) Die Bilder durch einen transparenten Raum getrennt sind

[^761]
```{.sh .numberLines .tight-code}
montage savannah.jpg naca65018.png -geometry +5+0 -tile 2x1\ 
  -resize x800 -background none -gravity West -extent x800 flugzeug.webp
```

[^761]: {-} Das zusammengesetzte Foto des Flugzeugs und des Flügelprofils wurde so gemacht.

## PGF/TikZ
[TikZ](https://tikz.dev) ist ein Paket für $\LaTeX$, das es ermöglicht, Figuren und Grafiken zu erstellen. Ich habe es an der Universität verwendet. Ich habe die Ikigai-Figur erstellt, die ich auf der Seite des Abschlussprojekts verwenden werde.\
Wie ihr seht, verwende ich alles Mögliche, das durch Code erzeugt wird.

[^760]
```{.tex .numberLines .tight-code}
\documentclass[tikz]{standalone}
\begin{document}
\begin{tikzpicture}
% Kreise
\fill[cyan!45, opacity=0.5, draw=cyan] (0,1) circle (2cm);
\fill[magenta!45, opacity=0.5, draw=magenta] (0,-1) circle (2cm);
\fill[yellow!45, opacity=0.5, draw=orange] (1,0) circle (2cm);
\fill[black!15, opacity=0.4, draw=gray] (-1,0) circle (2cm);
% Beschriftungen
\node[font=\small, align=center] at (-2.8,0) {Was die\\ Welt braucht};
\node[font=\small, align=center] at (2.8,0) {Worin du\\ gut bist};
\node[font=\small, align=center] at (0,-2.4) {Wofür du\\ bezahlt werden kannst};
\node[font=\small] at (0,2.4) {Was du liebst};
% Kleine Beschriftungen
\node[font=\tiny] at (1.35,-1.2) {Beruf};
\node[font=\tiny] at (1.35,1.2) {Leidenschaft};
\node[font=\tiny] at (-1.35,-1.2) {Berufung};
\node[font=\tiny] at (-1.35,1.2) {Mission};
% Titel
\node[font=\large] at (0,0) {Ikigai};
\end{tikzpicture}
\end{document}
```

[^760]:
  {-} ![](../../img/final/ikigai/ikigai.svg)
  [→ *Quellcode*](../../img/final/ikigai/ikigai.tex)

Um die `svg`-Figur zu generieren, führen Sie den Befehl aus:\
`pdflatex ikigai.tex && pdf2svg ikigai.pdf ikigai.svg`

