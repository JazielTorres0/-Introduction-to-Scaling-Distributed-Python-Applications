import threading
import multiprocessing
import asyncio
import time

def tarea_sincrona(nombre):
    for i in range(2):
        print(f"{nombre} - iteración {i}")
        time.sleep(1)

def ejecutar_hilo():
    hilo = threading.Thread(
        target=tarea_sincrona,
        args=("HILO",)
    )
    hilo.start()
    hilo.join()

def ejecutar_proceso():
    proceso = multiprocessing.Process(
        target=tarea_sincrona,
        args=("PROCESO",)
    )
    proceso.start()
    proceso.join()

async def tarea_async():
    for i in range(2):
        print(f"ASYNC - iteración {i}")
        await asyncio.sleep(1)

async def ejecutar_async():
    await asyncio.gather(tarea_async())

if __name__ == "__main__":
    print("\n--- INICIO DEL PROGRAMA ---\n")

    ejecutar_hilo()
    ejecutar_proceso()

    asyncio.run(ejecutar_async())

    print("\n--- FIN DEL PROGRAMA ---")