# Images
[*under development*]{.mark .yellow}


## Imagemagick

It's good for a bazillion things. You can slap a watermark on an image.\
Or combine two or more images horizontally so that:\
a) They have the same height\
b) The images are separated by a transparent space

[^761]
```{.sh .numberLines .tight-code}
montage savannah.jpg naca65018.png -geometry +5+0 -tile 2x1\ 
  -resize x800 -background none -gravity West -extent x800 airplane.webp
```

[^761]: {-} The composite photograph of the airplane and the airfoil profile was done this way.

## PGF/TikZ
[TikZ](https://tikz.dev) is a package for $\LaTeX$ that allows creating figures and graphics. I used to use it in college. I've created the Ikigai figure I'll be using on the final project page.\
As you see, I'm using anything that uses code to be generated.

[^760]
```{.tex .numberLines .tight-code}
\documentclass[tikz]{standalone}
\begin{document}
\begin{tikzpicture}
% Circles
\fill[cyan!45, opacity=0.5, draw=cyan] (0,1) circle (2cm);
\fill[magenta!45, opacity=0.5, draw=magenta] (0,-1) circle (2cm);
\fill[yellow!45, opacity=0.5, draw=orange] (1,0) circle (2cm);
\fill[black!15, opacity=0.4, draw=gray] (-1,0) circle (2cm);
% Labels
\node[font=\small, align=center] at (-2.8,0) {What the\\ World needs};
\node[font=\small, align=center] at (2.8,0) {What you\\ are good at};
\node[font=\small, align=center] at (0,-2.4) {What you\\ can be paid for};
\node[font=\small] at (0,2.4) {What you love};
% Small Labels
\node[font=\tiny] at (1.35,-1.2) {Profession};
\node[font=\tiny] at (1.35,1.2) {Passion};
\node[font=\tiny] at (-1.35,-1.2) {Vocation};
\node[font=\tiny] at (-1.35,1.2) {Mission};
% Title
\node[font=\large] at (0,0) {Ikigai};
\end{tikzpicture}
\end{document}
```

[^760]:
  {-} ![](../../img/final/ikigai/ikigai.svg)
  [→ *Source code*](../../img/final/ikigai/ikigai.tex)

To generate the `svg` figure you have to execute the command:\
`pdflatex ikigai.tex && pdf2svg ikigai.pdf ikigai.svg`

