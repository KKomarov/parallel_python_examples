import urllib.request
from threading import Thread


class ThreadsObject(Thread):
    def run(self):
        function_to_run()


class NoThreadsObject:
    @staticmethod
    def run():
        function_to_run()


def non_threaded(num_iter):
    not_threads = []
    for _ in range(int(num_iter)):
        not_threads.append(NoThreadsObject())
    for not_thread in not_threads:
        not_thread.run()


def threaded(num_iter):
    threads = []
    for _ in range(int(num_iter)):
        threads.append(ThreadsObject())
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


# Will not be faster with threading
# def function_to_run():
#     a, b = 0, 1
#     for _ in range(10000):
#         a, b = b, a + b


# Will be faster with threading because GIL will be released on I/O
def function_to_run():
    for _ in range(10):
        with urllib.request.urlopen('https://www.yandex.ru') as f:
            f.read(1024)


def show_results(obj_name, results):
    print('%-30s %4.6f seconds' % (obj_name, results))


if __name__ == '__main__':
    from timeit import Timer

    repeat = 10
    number = 1
    num_threads = [1, 2, 4, 8]

    print('Starting tests')

    for i in num_threads:
        timer = Timer('non_threaded(%s)' % i,
                      'from __main__ import non_threaded')
        bests_result = min(timer.repeat(repeat=repeat, number=number))
        show_results('non_threaded (%s iterations)' % i, bests_result)

        timer = Timer('threaded(%s)' % i,
                      'from __main__ import threaded')
        bests_result = min(timer.repeat(repeat=repeat, number=number))
        show_results('threaded (%s threads)' % i, bests_result)
