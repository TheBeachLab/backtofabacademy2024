# OpenFOAM

[Die Navier-Stokes-Gleichungen]{.smallcaps} sind eine Reihe von partiellen Differentialgleichungen, die die Bewegung von Flüssigkeiten beschreiben. In vektorieller Form und in einem dreidimensionalen Koordinatensystem sind die Navier-Stokes-Gleichungen für eine inkompressible Flüssigkeit:

\[
\rho \left( \frac{\partial \mathbf{v}}{\partial t} + (\mathbf{v} \cdot \nabla)\mathbf{v} \right) = -\nabla p + \mu \nabla^2 \mathbf{v} + \rho \mathbf{g}
\]

wobei:

- \(\rho\) ist die Dichte der Flüssigkeit,
- \(\mathbf{v}\) ist der Geschwindigkeitsvektor der Flüssigkeit,
- \(t\) ist die Zeit,
- \(p\) ist der Druck,
- \(\mu\) ist die dynamische Viskosität der Flüssigkeit,
- \(\nabla\) ist der Nabla-Operator,
- \(\nabla^2\) ist der Laplace-Operator,
- \(\mathbf{g}\) ist der Vektor der durch die Schwerkraft verursachten Beschleunigung.

Diese Gleichung beschreibt die Erhaltung des Impulses und die Beziehung zwischen Druck, Viskosität und Beschleunigung der Flüssigkeit. Diese Gleichungen zu lösen, kann besonders in nichtlinearen oder turbulenten Situationen komplex sein. Wenn die Flüssigkeit kompressibel ist, wird die Sache etwas komplizierter, da \(\rho\) nicht mehr konstant ist, sondern sich zeitlich und räumlich verändern kann.

\[
\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \mathbf{v}) = 0
\]

Diese Gleichungen können analytisch nicht gelöst werden, es müssen numerische Methoden verwendet werden. Hier kommt [OpenFOAM](https://openfoam.org)[^201] ins Spiel, eine Sammlung von Open-Source-Programmen für die numerische Simulation von Flüssigkeiten. OpenFOAM hat keine grafische Benutzeroberfläche. Alle Dateien, einschließlich Geometrie, Anfangsbedingungen, Randbedingungen, Modell usw., werden über Textdateien eingegeben[^203].

[^201]: Open Source Field Operation and Manipulation

[^203]: Wenn du eine grafische Benutzeroberfläche benutzt, wirst du bald arbeitslos sein. Warum glaubst du, wird so viel in das Training von Sprachmodellen investiert?

