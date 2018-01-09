from threading import Thread, Condition
import time

items = []
condition = Condition()


class Consumer(Thread):

    def consume(self):
        global condition
        global items

        condition.acquire()
        if len(items) == 0:
            condition.wait()
            print('Consumer notify : no item to consume')
        items.pop()

        print('Consumer notify : consumed 1 item')
        print('Consumer notify : items to consume are', len(items))

        condition.notify()
        condition.release()

    def run(self):
        for i in range(20):
            time.sleep(1)
            self.consume()


class Producer(Thread):

    def produce(self):
        global condition
        global items

        condition.acquire()
        if len(items) == 10:
            condition.wait()
            print('Producer notify : items produced are', len(items))
            print('Producer notify : stop the production')
        items.append(1)

        print('Producer notify : total items produced', len(items))

        condition.notify()
        condition.release()

    def run(self):
        for i in range(20):
            time.sleep(1.2)
            self.produce()


if __name__ == '__main__':
    producer = Producer()
    consumer = Consumer()

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()
