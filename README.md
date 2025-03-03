El juego de adivinanzas de palabras es un proyecto diseñado en Python que combina aspectos educativos con entretenimiento. Este programa emplea técnicas básicas de programación como condicionales, bucles y funciones, junto con herramientas adicionales como la biblioteca random. Ahora, vamos a explicar su funcionamiento en detalle.

Descripción General
El objetivo del juego es que el jugador adivine palabras basándose en pistas proporcionadas por el programa. El juego selecciona palabras de una lista predefinida, muestra una pista correspondiente y pide al jugador que adivine. Cada respuesta correcta otorga puntos, y el jugador puede salir del juego en cualquier momento escribiendo la palabra clave "salir".

Componentes del Programa
Biblioteca Importada:

Se importa la biblioteca random para elegir palabras de forma aleatoria. Esto asegura que el juego sea dinámico y no siempre siga el mismo patrón, añadiendo un elemento de sorpresa.

Lista de Palabras y Pistas:

Una lista de tuplas almacena cada palabra junto con su respectiva pista. Esto organiza el contenido de manera sencilla y eficiente. La palabra es el elemento que se espera que el jugador adivine, mientras que la pista sirve como una ayuda para facilitar el juego.

La Función jugar():

Es el núcleo del programa y contiene toda la lógica del juego. Esta función se encarga de interactuar con el jugador, mostrar las pistas, validar las respuestas y controlar el flujo general del juego.

Estructura del Código
Inicio del Juego:

Al comenzar, se muestra un mensaje de bienvenida que explica las reglas básicas. También se inicializa la variable puntuacion en 0 para llevar un registro de los puntos ganados por el jugador.

Selección de Palabras y Pistas:

Dentro de un bucle infinito, el programa utiliza la función random.choice() para seleccionar una palabra y pista al azar de la lista. Esto asegura que cada ronda del juego sea única.

Interacción con el Usuario:

Se muestra la pista al jugador y se solicita una respuesta. La entrada del jugador se procesa mediante el método .lower() para evitar problemas con mayúsculas o minúsculas.

Validación de la Respuesta:

Se utilizan condicionales (if, else) para validar la respuesta del jugador:

Si el jugador escribe "salir", el programa termina y muestra la puntuación final.

Si la respuesta es correcta, se incrementa la puntuación y se informa al jugador.

Si la respuesta es incorrecta, se revela la palabra correcta.

Continuación del Juego:

El bucle garantiza que el juego continuará hasta que el jugador decida salir. Cada ronda comienza con la selección de una nueva palabra y pista.

Finalización:

Cuando el jugador decide salir, el programa muestra un mensaje de despedida con la puntuación total acumulada.

Características Clave
Modularidad: La función jugar() contiene toda la lógica principal, lo que facilita futuras modificaciones o expansiones.

Interacción Dinámica: El uso de pistas y palabras aleatorias hace que el juego sea atractivo y varíe en cada ejecución.

Simplicidad y Funcionalidad: El programa utiliza estructuras básicas como listas, condicionales y bucles, lo que lo hace accesible para principiantes en programación.
