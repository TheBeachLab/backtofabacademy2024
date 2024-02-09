# Characterizing... the laser cutter?
[I would like to have Neil's laser cutter]{.smallcaps}. **My laser cutter doesn't have a fixed kerf**. The *power* and the *cutting speed* affect the kerf, the *material* affects the kerf, the *thickness* of the material affects the kerf, even the *color*[^101] of the material affects the kerf. I have to follow a process to characterize each material with the laser. Although I don't usually show it in the documentation, I repeat this process every time I change any parameter of the material. It's a real drag, I know. But skipping these minutes can lead to hours of delays and frustration later on, or even ruin all the work. My free advice of the week: 

<center>*spend those minutes*</center>

The first thing I do is search for the optimal cutting or marking parameters. I take a sample[^100] of the material I want to characterize. I place it on the platform and make sure the focus is correct. The idea is to find *the lowest possible energy*[^102] that cuts the material, without deforming or burning it. I make a pattern in Inkscape with copies in different colors and assign a setting to each line. As a starting point, you can use settings from a material and a machine similar to yours. Some machines include a library of materials with predefined cutting settings. I normally start at +5% of the known setting and go down by 5% on each line. The important thing is to note those settings on the same material and save them for future reference. These settings then serve me whenever I want to cut or mark the material. 

![Characterization example for engraving an aluminum plate](../../img/w03/character.webp)

[^100]:
    5x5 cm is enough
[^101]:
    Dark colors absorb more radiation and are easier to cut 
[^102]:
    It's a combination of power, speed, number of passes, and frequency, if available. My laser (Full Spectrum 5th gen) doesn't have frequency control. Whenever possible, I try to keep the speed at maximum. If it's a material sensitive to heat (like cellular polypropylene) I do more than one pass at low power.

Only then do I proceed to measure the kerf. But remember, if you change any parameter, that kerf is no longer valid.

