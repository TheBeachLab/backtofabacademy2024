# Caracterizar... ¿la cortadora laser?
[Me gustaría tener la cortadora laser de Neil]{.smallcaps}. **Mi cortadora laser no tiene un kerf fijo**. La *potencia* y la *velocidad* de corte influyen en el kerf, el *material* influye en el kerf, el *espesor* del material influye en el kerf, incluso el *color*[^101] del material influye en kerf. Yo tengo que seguir un proceso para caracterizar cada material con la laser. Aunque no lo suelo mostrar en la documentación, yo repito este proceso para cada vez que cambio cualquier parámetro del material. Da una pereza impresionante, lo sé. Pero ahorrarse estos minutos, os puede suponer horas de retrasos y frustración mas tarde o incluso arruinar todo el trabajo. Mi consejo gratis de la semana: 

<center>*gasta esos minutos*</center>

Lo primero que hago es buscar los parámetros óptimos de corte o marcado. Tomo una muestra[^100] del material que quiero caracterizar. La coloco en la plataforma y me aseguro que el enfoque es correcto. La idea es encontrar *la mínima energía posible*[^102] que corta el material, sin deformarlo ni quemarlo. Hago un patrón en Inkscape con copias de diferentes colores y asigno un ajuste a cada línea. Como punto de partida puedes usar ajustes de un material y una máquina parecidos a la tuya. Algunas máquinas incluyen una biblioteca de materiales con ajustes de corte predeterminados. Normalmente empiezo en +5% del ajuste conocido y voy bajando un 5% en cada línea. Lo importante es anotar esos ajustes en el mismo material y guardarlos para futura referencia. Estos ajustes me sirven ya para cada vez que quiero cortar o marcar el material. 

![Ejemplo de caracterización para grabado de una chapa de aluminio](../../img/w03/character.webp)

[^100]:
    5x5 cm es suficiente
[^101]:
    Los colores oscuros absorben más radiación y son más fáciles de cortar 
[^102]:
    Es una combinación de potencia, velocidad, número de pasadas y frecuencia, si es que tiene. Mi laser (Full Spectrum 5th gen) no tiene control de frecuencia. Siempre que es posible procuro que la velocidad sea máxima. Si es un material sensible al calor (como el polipropileno alveolar) hago más de una pasada a baja potencia.

Solo entonces procedo a medir el kerf. Pero recuerda, si cambias cualquier parámetro, ese kerf ya no es válido. 

