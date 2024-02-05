## Simulation eines Flügelprofils
[*in Entwicklung*]{.mark .yellow}

Fliegen in einem Flugzeug *ICP Savannah S* mit modifiziertem Flügelprofil NACA-65018[^211]. Es ist nicht besonders schnell, aber es kann auf sehr kurzen Strecken abheben und landen und bei sehr niedriger Geschwindigkeit ohne Absturz fliegen[^212]. Nahe der Vorderkante des Flügels gibt es Kunststoffteile, die als Vortex-Generatoren bezeichnet werden. Ihre Funktion besteht darin, Mikroturbulenzen zu erzeugen, um zu verhindern, dass die Grenzschicht sich vom Flügel löst. Das Ziel in OpenFOAM besteht darin, einen Abschnitt des Flügels mit und ohne Vortex-Generatoren zu simulieren und den Unterschied zu überprüfen.

![](../../img/w02/avion.webp)

[^212]: Ein Zustand, der auftritt, wenn der Flügel den Auftrieb verliert, indem er den kritischen Angriffswinkel überschreitet.

[^211]: Die Zahlen sind Parameter, die in Gleichungen eingeführt werden können, um den Querschnitt zu generieren und seine Eigenschaften zu berechnen.

