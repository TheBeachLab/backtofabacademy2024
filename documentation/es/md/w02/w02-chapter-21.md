## Simulación de un perfil alar
[*en desarrollo*]{.mark .yellow}

Vuelo en un avión *ICP Savannah S* con perfil de ala NACA-65018[^211] modificado. No es muy rápido, pero puede despegar y aterrizar en distancias muy cortas y volar a muy poca velocidad sin entrar en pérdida[^212]. Cerca del borde de ataque del ala, hay unas piezas de plástico llamadas generadores de vortex. Su función es generar micro-turbulencias para evitar que la capa límite se despegue del ala. El objetivo en OpenFOAM es simular una sección del ala con y sin generadores de vortex y comprobar la diferencia.

![](../../img/w02/avion.webp)

[^212]: Condición que se da cuando el ala pierde sustentación al superar el ángulo de ataque crítico.

[^211]: Los números son parámetros que se pueden introducir en ecuaciones para generar la sección transversal y calcular sus propiedades.

