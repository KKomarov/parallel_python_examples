import threading


def function(i):
    print('thread num: %s' % i)


threads = []
for i in range(5):
    t = threading.Thread(target=function, args=(i,))
    threads.append(t)
    t.start()
    t.join()
