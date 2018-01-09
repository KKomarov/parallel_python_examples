import threading
import time
import logging

logging.basicConfig(level=logging.INFO)


def first_function():
    logging.info(threading.currentThread().getName() + str(' is starting...'))
    time.sleep(2)
    logging.info(threading.currentThread().getName() + str(' is exiting...'))


if __name__ == '__main__':
    t1 = threading.Thread(name='first_function', target=first_function)
    t2 = threading.Thread(name='second_function', target=first_function)
    t3 = threading.Thread(name='third_function', target=first_function)

    t1.start()
    t2.start()
    t3.start()

    logging.debug('Not mandatory to join thread, main thread wait until all is finished.')