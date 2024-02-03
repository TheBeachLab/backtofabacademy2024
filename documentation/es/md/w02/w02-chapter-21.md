## Simulación de un perfil alar

Vuelo en un avión ultraligero ICP Savannah S. Tiene un perfil alar NACA-65018[^211] modificado. 

[^211]: Son perfiles con propiedades muy bien conocidas, desarrollados por la National Advisory Committee for Aeronautics. Los números son en realidad parámetros que se pueden introducir en ecuaciones para generar de forma precisa la sección transversal y calcular sus propiedades.

![](../../../img/naca650.webp)

Cerca del borde de ataque tiene unas piezas de plástico llamadas generadores de vortex. Quiero simular una sección del ala con y sin generadores de vortex y comprobar si hay alguna diferencia al entrar en pérdida.[^212] 


[^212]: Condición que se da cuando el ala pierde sustentación al superar el ángulo de ataque crítico. En la práctica, la sensación es que el avión se cae como una piedra.

### Generación de geometría

