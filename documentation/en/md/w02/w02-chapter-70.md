# Images
[*in development*]{.mark .yellow}


## Imagemagick

It's good for a ton of stuff. You can add a watermark to an image.\
Or combine two or more images horizontally so that:\
a) They have the same height\
b) The images are separated by a transparent space

[^761]
```{.sh .numberLines .tight-code}
montage savannah.jpg naca65018.png -geometry +5+0 -tile 2x1\ 
  -resize x800 -background none -gravity West -extent x800 airplane.webp
```

[^761]: {-} The composite photograph of the airplane and the airfoil profile was made like this.

## PGF/TikZ
I used to use [TikZ](https://tikz.dev) in college to make graphics.\
As you can see, I’m using anything that generates through code.

[^760]
```{.tex .numberLines .tight-code}
% Filename: tikz01.tex
% Usage: latex tikz01.tex --> tikz01.dvi
%        dvisvgm --font-format=woff tikz01.dvi --> tikz01.svg
\documentclass[tikz]{standalone}
\begin{document}
\begin{tikzpicture}[domain=0:4]
  \draw[very thin,color=gray] (-0.1,-1.1) grid (3.9,3.9);
  \draw[->] (-0.2,0) -- (4.2,0) node[right] {$x$};
  \draw[->] (0,-1.2) -- (0,4.2) node[above] {$f(x)$};
  \draw[color=red]    plot (\x,\x)             node[right] {$f(x) =x$};
  % \x r means to convert '\x' from degrees to _r_adians:
  \draw[color=blue]   plot (\x,{sin(\x r)})    node[right] {$f(x) = \sin x$};
  \draw[color=orange] plot (\x,{0.05*exp(\x)}) node[right] {$f(x) = \frac{1}{20} \mathrm e^x$};
\end{tikzpicture}
\end{document}
```

[^760]:
  {-} ![](../../files/w02/tikz/tikz01.svg)
  [→ *Source code*](../../files/w02/tikz/tikz01.tex)



