# OpenFOAM

[La ecuación de Navier-Stokes]{.smallcaps} es un conjunto de ecuaciones diferenciales parciales que describen el movimiento de los fluidos. En forma vectorial y en un sistema de coordenadas tridimensional, las ecuaciones de Navier-Stokes para un fluido incompresible son:

\[
\rho \left( \frac{\partial \mathbf{v}}{\partial t} + (\mathbf{v} \cdot \nabla)\mathbf{v} \right) = -\nabla p + \mu \nabla^2 \mathbf{v} + \rho \mathbf{g}
\]

donde:

- \(\rho\) es la densidad del fluido,
- \(\mathbf{v}\) es el vector de velocidad del fluido,
- \(t\) es el tiempo,
- \(p\) es la presión,
- \(\mu\) es la viscosidad dinámica del fluido,
- \(\nabla\) es el operador nabla,
- \(\nabla^2\) es el laplaciano,
- \(\mathbf{g}\) es el vector de la aceleración debida a la gravedad.

Esta ecuación describe la conservación de la cantidad de movimiento y la relación entre la presión, la viscosidad y la aceleración del fluido. Resolver estas ecuaciones puede ser complejo, especialmente en situaciones no lineales o turbulentas. Si el fluido es compresible, la cosa se complica un poco más porque \(\rho\) ya no es constante sino que puede variar en el tiempo y en el espacio.

\[
\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \mathbf{v}) = 0
\]

No se pueden resolver estas ecuaciones de forma analítica, se necesitan usar métodos numéricos. Ahí es donde interviene [OpenFOAM](https://openfoam.org)[^201], un conjunto de programas de código abierto para la simulación numérica de fluidos. OpenFOAM no tiene interfaz gráfica. Todos los archivos, incluyendo la geometría, condiciones iniciales, condiciones de contorno, modelo, etc. se introducen mediante archivos de texto[^203].

[^201]: Open Source Field Operation and Manipulation

[^203]: Si usas una interfaz gráfica pronto estarás en el paro. ¿Por qué crees que se invierte tanto en entrenar modelos de lenguaje?

