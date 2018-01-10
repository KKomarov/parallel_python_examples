import multiprocessing
from time import sleep
import logging
import os

logging.basicConfig(level=logging.INFO)


def foo(i):
    sleep(2)
    logging.info("Name: %s", multiprocessing.current_process().name)
    logging.info('Called function in process: %s %s', i, os.getpid())


if __name__ == '__main__':
    process_jobs = []
    for i in range(5):
        process = multiprocessing.Process(target=foo, args=(i,), name="sdmfg_%s" % i)
        process.daemon = True
        process_jobs.append(process)
        process.start()
        if i == 3:
            process.terminate()
        process.join()
