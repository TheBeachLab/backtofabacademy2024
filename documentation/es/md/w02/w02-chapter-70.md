# Imágenes
[*en desarrollo*]{.mark .yellow}


## Imagemagick

Sirve para infinidad de cosas. Puedes añadir una marca de agua a una imagen.\
O combinar dos o más imágenes horizontalmente de modo que:\
a) Tengan la misma altura\
b) Las imágenes estén separadas por un espacio transparente

[^761]
```{.sh .numberLines .tight-code}
montage savannah.jpg naca65018.png -geometry +5+0 -tile 2x1\ 
  -resize x800 -background none -gravity West -extent x800 avion.webp
```

[^761]: {-} La fotografía compuesta del avión y el perfil alar se han hecho así.

## PGF/TikZ
Solía usar [TikZ](https://tikz.dev) en la universidad para hacer gráficos.\
Como veis, estoy usando cualquier cosa que use código para generarse.

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
  [→ *Código fuente*](../../files/w02/tikz/tikz01.tex)



