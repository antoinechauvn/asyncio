__author__ = "Chauvin Antoine"
__copyright__ = ""
__credits__ = ["Chauvin Antoine"]
__license__ = ""
__version__ = "1.0"
__maintainer__ = "Chauvin Antoine"
__email__ = "antoine.chauvin@live.fr"
__status__ = "Production"
# On importe la librairie asyncio
import asyncio


# On créer une coroutine à l'aide du keyword async
async def count():
    print("One")
    # On utilise un Future (objet dis awaitable). On va ici redonner la main à la boucle principale
    # afin d'exécuter d'autres tâches pendant que cette coroutine dort
    await asyncio.sleep(1)   
    print("Two")

async def main():
    # On va ici executer plusieurs awaitable de façon conccurente
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    import time # On va importer time afin de créer un timer
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
