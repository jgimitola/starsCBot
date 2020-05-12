# Estrellas y Constelaciones

Para este ejercicio, deben usar los archivos stars.txt y los de constelaciones que estarán adjuntos al enunciado. 

El archivo stars contiene un listado de estrellas, con información sobre cada una. Cada fila corresponde a una estrella y el formato de cada fila es el siguiente: 

- Los primeros tres campos corresponden a las coordenadas x, y y z de la estrella. Para este ejercicio, solo deben tener en cuenta las coordenadas x e y. Los valores de las coordenadas están en el rango [−1, 1].
- El cuarto campo corresponde a un identificador (único) para la estrella. Estos identificadores se conocen como números Henry Draper.
- El quinto ítem corresponde a la magnitud del brillo de la estrella.
- El sexto campo corresponde el Harvard Revised number, que es otro identificador.
- El séptimo campo no está en todas las estrellas, sino que está solo para unas pocas. Este campo corresponde a el nombre de la estrella. Alguna estrellas pueden tener m´as de un nombre, por lo que en este caso estarán separados por punto y coma (;). 

Adicional a el archivo de estrellas, contaran con una carpeta de archivos con información sobre algunas constelaciones. Cada línea de estos archivos corresponde a el nombre de dos estrellas, lo que indica que, para la correspondiente constelación, esas dos estrellas deben estar unidas por una línea.

A partir de esto deben crear un bot de Telegram que permita hacer peticiones relacionadas con las estrellas y constelaciones. Es decir, debe permitir: 

- Mostrar un gráfico  de todas las estrellas.
- Mostrar un gráfico con todas las estrellas y, adicionalmente, una constelación en particular, escogida por el usuario.
- Mostrar todas las estrellas y todas las constelaciones. 

Importante: El bot debe tener instrucciones claras sobre como usarlo y como acceder a cada uno de los comandos. Tienen total libertad sobre la forma en que permitirán al usuario interactuar con el bot; pero se recalca la importancia de que el bot permita conocer con claridad como acceder a que realice cada una de las acciones.