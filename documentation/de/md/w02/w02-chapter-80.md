# Audio und Video
[*in Entwicklung*]{.mark .yellow}

## ffmpeg

Sehr nützlich für unzählige Operationen. Früher war es schwierig, sich die Befehle zu merken, aber jetzt kannst du sie einfach ein Sprachmodell fragen.

## yt-dlp

Ich benutze dieses Terminal-Tool, um Videos von Fab Academy herunterzuladen, die auf [Youtube]() oder [Vimeo](https://vimeo.com/academany/videos) gehostet sind. Zum Beispiel:

```{.bash .numberLines .tight-code}
yt-dlp --write-sub --all-subs [Video-URL]
```

## Manim

Du hast sicherlich schon mal ein Video von [3blue1brown](https://www.youtube.com/@3blue1brown) gesehen.\
[Manim] ist die Python-Bibliothek, die er selbst geschaffen hat, um seine Animationen zu generieren.\
Hier ist mein *Hallo Welt!*: `manim -pqh hello_manim.py AnimatedSquareToCircle`

[^802]
```{.python .numberLines .tight-code}
from manim import *
class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # erstelle einen Kreis
        square = Square()  # erstelle ein Quadrat

        self.play(Create(square))  # zeige das Quadrat auf dem Bildschirm
        self.play(square.animate.rotate(PI / 4))  # rotiere das Quadrat
        self.play(
            ReplacementTransform(square, circle)
        )  # verwandle das Quadrat in einen Kreis
        self.play(
            circle.animate.set_fill(BLUE, opacity=0.2)
        )  # färbe den Kreis auf dem Bildschirm
```

[^802]:
    {-} <video nocontrols autoplay loop muted style="max-width: 100%; height: auto;">
    <source src="../../files/w02/manim/media/videos/hello_manim/1080p60/AnimatedSquareToCircle.mp4" type="video/mp4">
    Ihr Browser unterstützt das Video-Element nicht.
    </video>\
    [→ *Quellcode*](../../files/w02/manim/hello_manim.py)

## Sonic Pi
Ich erstelle eine Session mit einigen Audioproben von Fab Academy.\
Mehr kann ich nicht verraten.

[^801]
```{.ruby .numberLines .tight-code}
use_bpm 130

live_loop :met1 do # das ist ein Metronom zur Synchronisierung der Beats
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
    Ihr Browser unterstützt das Audio-Element nicht.
    </audio>\
    [→ *Quellcode*](../../files/w02/sonicpi/neil_rave.rb)

