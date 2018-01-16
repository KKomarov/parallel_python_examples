import multiprocessing
import os


def worker(dictionary, key, item):
    dictionary[key] = item
    print('Key:', key, 'Value:', item, os.getpid())


if __name__ == '__main__':
    manager = multiprocessing.Manager()
    dictionary = manager.dict()
    jobs = [multiprocessing.Process(target=worker, args=(dictionary, i, i * 2))
            for i in range(10)]
    for job in jobs:
        job.start()
    for job in jobs:
        job.join()
    print('Results:', dictionary)
