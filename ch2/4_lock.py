import threading

shared_resource_with_lock = 0
shared_resource_without_lock = 0

COUNT = 10**5

shared_resource_lock = threading.Lock()


def increment_with_lock():
    global shared_resource_with_lock
    for _ in range(COUNT):
        shared_resource_lock.acquire()
        shared_resource_with_lock += 1
        shared_resource_lock.release()


def decrement_with_lock():
    global shared_resource_with_lock
    for _ in range(COUNT):
        shared_resource_lock.acquire()
        shared_resource_with_lock -= 1
        shared_resource_lock.release()


def increment_without_lock():
    global shared_resource_without_lock
    for _ in range(COUNT):
        shared_resource_without_lock += 1


def decrement_without_lock():
    global shared_resource_without_lock
    for _ in range(COUNT):
        shared_resource_without_lock += 1

fs = [increment_with_lock, decrement_with_lock, increment_without_lock, decrement_without_lock]

if __name__ == '__main__':
    ts = []
    for f in fs:
        ts.append(threading.Thread(target=f))

    for t in ts:
        t.start()

    for t in ts:
        t.join()

    print('Shared variable with lock', shared_resource_with_lock)
    print('Shared variable without lock', shared_resource_without_lock)