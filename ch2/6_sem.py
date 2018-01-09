import threading
import time
import random

semaphore = threading.Semaphore(0)


def consumer():
    print('Consumer is waiting')
    time.sleep(3)
    semaphore.acquire()
    print('Consumer notify : consumed item number', item)


def producer():
    global item
    # time.sleep(3)
    item = random.randint(0, 1000)
    print('Producer notify : produced item number', item)
    semaphore.release()
    print('released')
    # I'm dislike this, what if it releases twice I will loose item


if __name__ == '__main__':
    for i in range(2):
        t1 = threading.Thread(target=producer)
        t2 = threading.Thread(target=consumer)

        t1.start()
        t2.start()

        t1.join()
        t2.join()

    print('Program terminated')
