__author__ = "Chauvin Antoine"
__copyright__ = "pymotw.com"
__credits__ = ["Chauvin Antoine"]
__license__ = ""
__version__ = "1.0"
__maintainer__ = "Chauvin Antoine"
__email__ = "antoine.chauvin@live.fr"
__status__ = "Production"
import asyncio
import concurrent.futures
import logging
import sys
import time


def blocks(n):
    log = logging.getLogger('blocks({})'.format(n))
    log.info('running')
    time.sleep(0.1)
    log.info('done')
    return n ** 2

async def main():
    log = logging.getLogger('main')
    log.info('starting')

    loop = asyncio.get_running_loop()

    # Create a limited thread pool.
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)
    loop.set_default_executor(executor)

    log.info('creating executor tasks')
    awt = [asyncio.to_thread(blocks, 3),
    asyncio.to_thread(blocks, 3),
    asyncio.to_thread(blocks, 3),
    asyncio.to_thread(blocks, 3),
    asyncio.to_thread(blocks, 3),
    asyncio.to_thread(blocks, 3)]

    log.info('waiting for executor tasks')
    await asyncio.gather(*awt)
    
    log.info('exiting')


if __name__ == '__main__':
    # Configure logging to show the name of the thread
    # where the log message originates.
    logging.basicConfig(level=logging.INFO, format='%(threadName)10s %(name)18s: %(message)s', stream=sys.stderr)
    asyncio.run(main())
