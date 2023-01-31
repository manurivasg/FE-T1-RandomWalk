## Random Walk Simulation
<!-- PROJECT CONTENT -->
**Table of Contents**
<!-- autogenerated by plugin -->
1. [Random Walk Simulation](#Random_Walk_Simulation)
    1. [Creadora](#Creadora)
    1. [Proyecto](#Proyecto)
    1. [Resultados](#Resultados)  

<!-- Creadora del proyecto -->
## Creadora
La estudiante encargada de desarrollar todo el código y pruebas presentes para este proyecto es:

    Nombre: Manuela Rivas Gómez

    Correo institucional: m.rivas2@uniandes.edu.co

    Código estudiantil: 202021971

[Back to top](#RandomWalkSimulation)

<!-- Proyecto -->
## Proyecto

El código y resultados que encontrará en este repositorio hacen parte de la sección de simulación computacional que se le es solicitada a la estudiante como arte de su Tarea 1 para la clase de Física Estadística, semestre 2023-1.

En este podrá encontrar el código con el cual se llevó a cabo la simulación, compuesto por dos funciones, RandomWalk y ejecutar_RandomWalk. La primera es la encargada de desarrollar el proceso de obtener la caminata aleatoria y determinar como se le van a mostrar los resultados al usuario dependiendo de en cuántas dimensiones desea que se de la caminata, mientras que la segunda función es la encargada de interactuar directamente con el usuario para obtener los datos necesarios para desarrollar la caminata (dimensiones y número de pasos).

[Back to top](#RandomWalkSimulation)


<!-- Resultados -->
## Resultados
Para poder replicar los resultados que se muestran en el reporte de la simulación es necesario que el usuario descargue y ejecute el archivo de python "RandomWalk.py". Una vez lo haga, este podrá observar en su consola la siguiente frase: 

"Bienvenido a Random Walk Simulation"

"Por favor ingrese las dimensiones en las que desea llevar a cabo la caminata aleatoria: (1-3) "

Cuando el usuario vaya a ingresar un valor, debe recordar que en este programa solo es posible simular caminatas de 1-3 dimensiones por lo que si ingresa un número menor o igual a 0 o mayor o igual a 4 el programa automáticamente le mostrará en consola:

"No son válidos los parámetros que ingresa por input"

Ahora si, una vez observe esta frase en consola, debe ingresar como número de dimensiones 1, para poder replicar la primera parte. Después de esto, podrá observar la siguiente frase en consola: 

"Por favor ingrese la cantidad de pasos que desea que tenga la caminata aleatoria: (>0) "

Únicamente en este caso debe ingresar la cantidad de pasos como 10, puesto que al ser en una dimesión los resultados no se muestran en una gráfica sino que se muestran en una tabla, por lo que a menor cantidad de pasos, mayor legibilidad de la misma (recuerde que en este caso, al igual que en el anterior, como se desea simular una caminata debe haber por o menos un paso, por lo que si ingresa un valor menor o igual a 0 el programa le mostrará inmediatamente que su parámetro de entrada no es válido). 

Para poder replicar los segundos resultados, el usuario debe volver a correr el programa y cuando observe la frase que le solicita ingresar la cantidad de dimensiones que desea debe ingresar 2. Una vez hecho esto, en la siguiente frase debe ingresar como cantidad de pasos de la caminata 500 (En este caso se opta por un valor mayor que en la primera prueba puesto que es más fácil observar el comportamiento cuando se da en una gráfica) y observar la gráfica que le retorna el programa. 

Por último, para replicar los terceros resultados, el usuario debe volver a correr el programa y cuando observe la frase que le pide la cantidad de dimensiones que desea debe ingresar 3. Una vez hecho esto, en la siguiente frase debe ingresar como cantidad de pasos de la caminata 500 y observar la gráfica que le retorna el programa. 

Cabe resaltar que la ser una caminata aleatoria es posible que los resultados de la caminata no sena identicos a los mostrados en el reporte (ya que la ser aleatoria cada ez que se corra el programa el resultado va a ser diferente a pesar de tener los mismos parámetros de entrada) sin embargo, el usuario podrá observar y analizar por si mismo los resultados reportados y obtener sus propias conlcusiones a partir del programa.


[Back to top](#RandomWalkSimulation)


