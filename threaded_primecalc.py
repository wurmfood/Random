#!/usr/bin/env python3
from primecalc import check_if_prime
from threading import Thread, Lock
from queue import Queue
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO,
                    format='(%(threadName)-9s) %(message)s',)

MAX_PRIME_NUMBER = 10000
MAX_QUEUE_SIZE = 10
NUM_WORKERS = 1

q = Queue(MAX_QUEUE_SIZE)


class Counter(object):
    def __init__(self, start=0):
        self.lock = Lock()
        self.value = start

    def __str__(self):
        return str(self.value)

    def increment(self):
        self.lock.acquire()
        try:
            self.value += 1
            logging.debug("Counter value: {0}".format(self.value))
        finally:
            self.lock.release()


class QueueFiller(Thread):
    def __init__(self, start_num, end_num):
        Thread.__init__(self)
        self._start_num = start_num
        self._end_num = end_num

    def _give_me_a_number(self):
        for i in range(self._start_num, self._end_num):
            yield i

    def run(self):
        nums = self._give_me_a_number()
        try:
            while True:
                if not q.full():
                    num = next(nums)
                    logging.debug("Adding {0} to queue.".format(num))
                    q.put(num)
        except StopIteration:
            pass
        finally:
            for i in range(NUM_WORKERS):
                q.put(None)
        return


class PrimeThread(Thread):
    def __init__(self, counter):
        Thread.__init__(self)
        self.counter = counter
        self.internal_counter = 0

    def run(self):
        try:
            while True:
                if not q.empty():
                    num = q.get()
                    if num is None:
                        break
                    if check_if_prime(num):
                        logging.debug("Found a prime: {0}, Counter: {1}".format(num, self.counter))
                        self.internal_counter += 1
                        self.counter.increment()
                    q.task_done()
        except StopIteration:
            pass
        finally:
            logging.info("Thread exiting with {0} hits.".format(self.internal_counter))
        return


def main():
    start_time = datetime.now()
    hits = Counter()

    my_queue_filler = QueueFiller(0, MAX_PRIME_NUMBER)
    my_queue_filler.start()

    threads = []
    for x in range(NUM_WORKERS):
        worker = PrimeThread(hits)
        worker.daemon = False
        worker.start()
        threads.append(worker)

    # my_queue_filler.join()
    # logging.debug("Items in queue: {0}".format(q.unfinished_tasks))
    # q.join()

    for t in threads:
        logging.debug("Joining thread.")
        t.join()

    logging.debug("Items in queue: {0}".format(q.unfinished_tasks))

    # q.join()

    logging.info("Elapsed time with {0} threads and {1} as maximum number: {2}".format(NUM_WORKERS,
                                                                                       MAX_PRIME_NUMBER,
                                                                                       datetime.now()-start_time))

    logging.info("Total primes found: {0}".format(hits))


if __name__ == "__main__":
    main()
