import multiprocessing
from multiprocessing import Barrier, Lock, Process
from time import time
import datetime as dt


def test_with_barrier(barrier, lock):
    name = multiprocessing.current_process().name
    barrier.wait()
    now = time()
    with lock:
        print('Process %s -----> %s' % (name, dt.datetime.fromtimestamp(now)))


def test_without_barrier():
    name = multiprocessing.current_process().name
    now = time()
    print('Process %s -----> %s' % (name, dt.datetime.fromtimestamp(now)))


if __name__ == '__main__':
    barrier = Barrier(2)
    lock = Lock()
    Process(name='p1 - test_with_barrier',
            target=test_with_barrier,
            args=(barrier, lock)).start()
    Process(name='p2 - test_with_barrier',
            target=test_with_barrier,
            args=(barrier, lock)).start()
    Process(name='p3 - test_without_barrier',
            target=test_without_barrier).start()
    Process(name='p4 - test_without_barrier',
            target=test_without_barrier).start()
