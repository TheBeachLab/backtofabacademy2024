# Bilder
[*in Entwicklung*]{.mark .yellow}


## Imagemagick

Es ist gut für unzählige Dinge. Du kannst einem Bild ein Wasserzeichen hinzufügen.\
Oder zwei oder mehr Bilder horizontal kombinieren, sodass:\
a) Sie die gleiche Höhe haben\
b) Die Bilder durch einen transparenten Raum getrennt sind

[^761]
```{.sh .numberLines .tight-code}
montage savannah.jpg naca65018.png -geometry +5+0 -tile 2x1\ 
  -resize x800 -background none -gravity West -extent x800 flugzeug.webp
```

[^761]: {-} Das zusammengesetzte Foto des Flugzeugs und des Flügelprofils wurde so gemacht.

## PGF/TikZ
Ich habe [TikZ](https://tikz.dev) an der Universität für Grafiken benutzt.\
Wie ihr seht, benutze ich alles Mögliche, was sich durch Code generieren lässt.

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
  % \x r bedeutet, dass '\x' von Grad in _R_adian umgewandelt wird:
  \draw[color=blue]   plot (\x,{sin(\x r)})    node[right] {$f(x) = \sin x$};
  \draw[color=orange] plot (\x,{0.05*exp(\x)}) node[right] {$f(x) = \frac{1}{20} \mathrm e^x$};
\end{tikzpicture}
\end{document}
```

[^760]:
  {-} ![](../../files/w02/tikz/tikz01.svg)
  [→ *Quellcode*](../../files/w02/tikz/tikz01.tex)





