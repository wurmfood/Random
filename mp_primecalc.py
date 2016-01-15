#!/usr/bin/env python3
from primecalc import check_if_prime
from threading import Thread, Lock
from multiprocessing import Queue, Process, JoinableQueue
from datetime import datetime
from time import sleep
import logging

logging.basicConfig(level=logging.INFO,
                    format='(%(threadName)-9s) %(message)s',)

MAX_PRIME_NUMBER = 100000
MAX_QUEUE_SIZE = 30
NUM_WORKERS = 16


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
    def __init__(self, queue_to_fill, start_num, end_num):
        Thread.__init__(self)
        self._queue = queue_to_fill
        self._start_num = start_num
        self._end_num = end_num

    def _give_me_a_number(self):
        for i in range(self._start_num, self._end_num):
            yield i

    def run(self):
        nums = self._give_me_a_number()
        try:
            while True:
                if not self._queue.full():
                    num = next(nums)
                    # logging.debug("Adding {0} to queue.".format(num))
                    if num % 100 == 0:
                        logging.debug("Adding {0} to queue.".format(num))
                    self._queue.put(num)
        except StopIteration:
            logging.warning("StopIteration exception encountered.")
            pass
        finally:
            for _ in range(NUM_WORKERS):
                self._queue.put(None)
            logging.debug("Exiting")
        return


class Task(Process):
    def __init__(self, in_queue: JoinableQueue, results: Queue):
        Process.__init__(self)
        self._queue = in_queue
        self._out_queue = results

    def run(self):
        proc_name = self.name
        while True:
            new_task = self._queue.get()
            if new_task is None:
                # Break out, poison pill found
                logging.debug("Process {0} ending.".format(proc_name))
                self._queue.task_done()
                break
            result = check_if_prime(new_task)
            if result is True:
                logging.debug("{0} : {1} is prime.".format(proc_name, new_task))
                self._out_queue.put(True)
            self._queue.task_done()
        logging.debug("I should be exiting.")


if __name__ == "__main__":
    start_time = datetime.now()
    q = JoinableQueue(MAX_QUEUE_SIZE)
    out_queue = JoinableQueue()
    # c = Counter()
    qf = QueueFiller(q, 1, MAX_PRIME_NUMBER)
    qf.start()

    tasks = [Task(q, out_queue) for i in range(NUM_WORKERS)]
    for w in tasks:
        w.start()

    logging.info("Items left in queue: {0}".format(q.qsize()))
    logging.debug("Joining q")
    # q.join()
    # qf.join()

    if False:
        processes_active = True
        while processes_active:
            for w in tasks:
                processes_active = False or w.is_alive()
                logging.debug(w.is_alive())
            sleep(0.2)

    for y in tasks:
        y.join()

    logging.info("Elapsed time with {0} threads and {1} as maximum number: {2}".format(NUM_WORKERS,
                                                                                       MAX_PRIME_NUMBER,
                                                                                       datetime.now()-start_time))

    count = 0
    while not out_queue.empty():
        out_queue.get()
        out_queue.task_done()
        count += 1
    logging.info("Total primes found: {0}".format(count))
