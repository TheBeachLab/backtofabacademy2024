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
[TikZ](https://tikz.dev) es un paquete para $\LaTeX$ que permite crear figuras y gráficos. Solía usarlo en la universidad. He creado la figura de Ikigai que usaré para decidir qué proyecto final hacer.\
Como veis, estoy usando cualquier cosa que use código para generarse.

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
\node[font=\tiny] at (-1.35,-1.2) {Mission};
\node[font=\tiny] at (-1.35,1.2) {Vocation};
% Title
\node[font=\large] at (0,0) {Ikigai};
\end{tikzpicture}
\end{document}
```

[^760]:
  {-} ![](../../img/final/ikigai/ikigai.svg)
  [→ *Código fuente*](../../img/final/ikigai/ikigai.tex)

Para generar la figura `svg` hay que ejecutar el comando:\
`pdflatex ikigai.tex && pdf2svg ikigai.pdf ikigai.svg`

