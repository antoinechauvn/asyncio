__author__ = "Chauvin Antoine"
__copyright__ = "pymotw.com"
__credits__ = ["Chauvin Antoine"]
__license__ = ""
__version__ = "1.0"
__maintainer__ = "Chauvin Antoine"
__email__ = "antoine.chauvin@live.fr"
__status__ = "Production"
# On importe la librairie asyncio
import asyncio
# On importe la librairie concurrent.futures pour executer de manière asynchrone une tâche dite bloquante
import concurrent.futures
import logging
#On utilise la journalisation pour indiquer de manière
# pratique quel thread et quelle fonction produisent chaque message de journal.
# Comme un enregistreur distinct est utilisé dans chaque appel à blocks(),
# la sortie montre clairement que les mêmes threads sont réutilisés pour appeler plusieurs copies
# de la fonction avec différents arguments.
import sys
import time


def blocks(n):
    log = logging.getLogger('blocks({})'.format(n))
    log.info('running')
    time.sleep(0.1)
    log.info('done')
    return n ** 2

# Explicit
async def run_blocking_tasks(executor):
    log = logging.getLogger('run_blocking_tasks')
    log.info('starting')
    log.info('creating executor tasks')
    
    # On récupère la boucle dévénement
    loop = asyncio.get_event_loop()
    # On spécifie ici lesfonctions à executer sous forme de liste avec les paramètres
    blocking_tasks = [
        loop.run_in_executor(executor, blocks, i)
        for i in range(6)
    ]
    log.info('waiting for executor tasks')
    
    # On redonne la main pour attendre que chaque tâche se finisse
    completed, pending = await asyncio.wait(blocking_tasks)
    
    results = [t.result() for t in completed]
    log.info('results: {!r}'.format(results))
    log.info('exiting')


if __name__ == '__main__':
  # On configure une journalisation basique afin d'afficher
  # le nom du Thread et son message.
    logging.basicConfig(
        level=logging.INFO,
        format='%(threadName)10s %(name)18s: %(message)s',
        stream=sys.stderr,
    )

    # On va créer un PoolExecutor qui contiendra des Threads
    # qu'on va limiter volontairement à 3 workers
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=3)
    try:
        # On créer notre boucle d'événement dans laquel on renseigne la fonction à executer
        event_loop.run_until_complete(
            run_blocking_tasks(executor)
        )
    finally:
        event_loop.close()
