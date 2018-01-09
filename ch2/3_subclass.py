import threading
import time

EXIT_FLAG = 0


class MyThread(threading.Thread):
    def __init__(self, thread_id, counter, **kwargs):
        super(MyThread, self).__init__(**kwargs)
        self.thread_id = thread_id
        self.counter = counter

    def run(self):
        print('Starting %s' % self.name)
        print_time(self.name, self.counter, 5)
        print('Exiting %s\n' % self.name)


def print_time(thread_name, delay, counter):
    while counter:
        if EXIT_FLAG:
            return
        time.sleep(delay)
        print('%s: %s' % (thread_name, time.ctime(time.time())))
        counter -= 1


thread1 = MyThread(1, 1, name='Thread-1')
thread2 = MyThread(2, 2, name='Thread-2')

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print('Exiting main thread!\n')
