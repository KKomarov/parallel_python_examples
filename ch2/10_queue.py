import queue
import random
import threading

num_worker_threads = 3


def worker():
    while True:
        item = q.get()
        if item is None:
            break
        print('work %s' % item)
        q.task_done()


q = queue.Queue()
threads = []
for i in range(num_worker_threads):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

for _ in range(3):
    item = random.randint(0, 256)
    q.put(item)

# block until all tasks are done
q.join()

# stop workers
for _ in range(num_worker_threads):
    q.put(None)
for t in threads:
    t.join()
