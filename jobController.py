#!/usr/local/bin/python
#-*- coding: utf-8 -*-

import threading
import Queue

class Thr(threading.Thread):
    def __init__(self, num, queue, handler, args):
        threading.Thread.__init__(self)
        self._num = num
        self._queue = queue
        self._handler = handler
        self._args = args
    def run(self):
        while True:
            job = self._queue.get()
            if job is False: break
            self._handler(self._num, job, self._args)
            self._queue.task_done()
class jobController():
    def __init__(self, handler, thread_num = 4, args = None):
        self.queue = Queue.Queue()
        self._thread_num = thread_num
        self._threads = []
        self._handler = handler
        self._args = args
    #def start(self):
        for i in range(self._thread_num):
            handle = Thr(i, self.queue, self._handler, self._args)
            handle.daemon = True
            handle.start()
            self._threads.append(handle)
    def join(self):
        for i in range(self._thread_num):
            self.queue.put(False)
        for thread in self._threads:
            while thread.isAlive():
                thread.join(1)
