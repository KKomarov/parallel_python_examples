import logging
import time
import os
from threading import Thread

logging.basicConfig(level=logging.INFO)
logger_thread = logging.getLogger('__thrd__')
logger_main = logging.getLogger(__name__)


class ParallelPython(Thread):
    def run(self):
        logger_thread.info('Thread Starting: %s' % os.getpid())

        for _ in range(6):
            time.sleep(0.5)
            logger_thread.info('here %s' % os.getpid())

        logger_thread.info('Thread Ended')


if __name__ == '__main__':
    logger_main.info('Process Started: %s' % os.getpid())
    hello_python = ParallelPython()
    hello_python.start()
    logger_main.info('Process Ended')
