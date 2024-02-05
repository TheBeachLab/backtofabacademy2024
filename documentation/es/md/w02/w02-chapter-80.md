# Audio y video
[*en desarrollo*]{.mark .yellow}

## ffmpeg

Muy útil para infinidad de operaciones. Antes era difícil aprenderse los comandos, pero ahora se los puedes preguntar a un modelo de lenguaje.

## yt-dlp

Uso esta utilidad de terminal para bajarme los videos de Fab Academy alojados en [Youtube](https://www.youtube.com/@FabAcademyGlobal/playlists) o [Vimeo](https://vimeo.com/academany/videos). Por ejemplo:

```{.bash .numberLines .tight-code}
yt-dlp --write-sub --all-subs [Video URL]
```

## Manim

Seguramente habrás visto algún video de [3blue1brown](https://www.youtube.com/@3blue1brown).\
[Manim] es la biblioteca de Python que él mismo creó para generar sus animaciones.\
Aquí mi *hello world!*: `manim -pqh hello_manim.py AnimatedSquareToCircle`

[^802]
```{.python .numberLines .tight-code}
from manim import *
class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        square = Square()  # create a square

        self.play(Create(square))  # show the square on screen
        self.play(square.animate.rotate(PI / 4))  # rotate the square
        self.play(
            ReplacementTransform(square, circle)
        )  # transform the square into a circle
        self.play(
            circle.animate.set_fill(BLUE, opacity=0.2)
        )  # color the circle on screen
```

[^802]:
    {-} <video nocontrols autoplay loop muted style="max-width: 100%; height: auto;">
    <source src="../../files/w02/manim/media/videos/hello_manim/1080p60/AnimatedSquareToCircle.mp4" type="video/mp4">
    Your browser does not support the video element.
    </video>\
    [→ *Código fuente*](../../files/w02/manim/hello_manim.py)

## Sonic Pi
Estoy creando una sesión usando algunas muestras de audio de Fab Academy.\
No puedo desvelar más.

[^801]
```{.ruby .numberLines .tight-code}
use_bpm 130

live_loop :met1 do # this is a metronome to sync the beats
  sleep 1
end

define :pattern do |pattern|
  pattern.ring.tick == "x"
end

live_loop :kick, sync: :met1 do
  a = 2
  sample :bd_haus, amp: a, release: 8, cutoff: 110 if pattern("x-----x---x--x--")
  sleep 0.25
end

live_loop :clap, sync: :met1 do
  sleep 1
  sample :perc_snap, amp: 1
  sleep 1
end

live_loop :hhc1, sync: :met1 do
  sample :drum_cymbal_closed, amp: 0.5 if pattern("x-x-x-x-xxx-x-x-")
  sleep 0.125
end
```

[^801]:
    {-} <audio controls>
    <source src="../../files/w02/sonicpi/neil_rave.m4a" type="audio/mp4">
    Your browser does not support the audio element.
    </audio>\
    [→ *Código fuente*](../../files/w02/sonicpi/neil_rave.rb)

