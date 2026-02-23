En los sistemas operativos modernos, la ejecución concurrente de tareas es fundamental para mejorar el rendimiento y el aprovechamiento de los recursos del sistema.
Python ofrece distintas formas de manejar concurrencia, entre ellas el uso de hilos (threading), procesos (multiprocessing) y programación asíncrona (asyncio).

Marco Teórico____________________________________________________________________________________

Hilos (threading)
Los hilos permiten ejecutar varias tareas de manera concurrente dentro de un mismo proceso. Comparten memoria y recursos, lo que los hace ligeros, aunque no aprovechan múltiples núcleos de CPU debido al GIL de Python.

Procesos (multiprocessing)
Los procesos crean instancias independientes del programa, cada una con su propia memoria. Esto permite el uso de múltiples núcleos del procesador, siendo ideal para tareas que requieren alto consumo de CPU.

Programación Asíncrona (asyncio)
La programación asíncrona permite manejar múltiples tareas sin bloquear la ejecución del programa, utilizando un solo hilo. Es especialmente eficiente para operaciones de entrada y salida (I/O), como solicitudes de red o acceso a archivos.

Desarrollo del Programa__________________________________________________________________________
El siguiente programa implementa las tres técnicas dentro de una sola aplicación, ejecutando una tarea simple que simula carga de trabajo mediante pausas de tiempo.

Resultados_______________________________________________________________________________________
Al ejecutar el programa, se observa que:

        El hilo ejecuta la tarea compartiendo memoria con el proceso principal.
        El proceso se ejecuta de manera independiente, utilizando recursos propios.
        La tarea asíncrona se ejecuta sin bloquear el flujo del programa, usando un solo hilo.
        Esto demuestra cómo cada técnica maneja la concurrencia de forma distinta.

<img width="370" height="186" alt="image" src="https://github.com/user-attachments/assets/7ab729b3-63b1-4bb3-a0c4-c92b98e6d285" />


Conclusión_______________________________________________________________________________________
La programación concurrente es un elemento clave en los sistemas operativos. 
A través de este programa se comprobó que Python ofrece múltiples enfoques para manejar tareas simultáneas, 
cada uno con ventajas y desventajas según el tipo de problema.
