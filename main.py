#!/usr/bin/env python
#-*- coding: utf-8 -*-

import time
import jobController

def handler(index, job, args):
    time.sleep(1)
    print("handled job({args}): {job}".format(args = args, job = job))

jc = jobController.jobController(handler, 4, args = ('123'))
for i in range(10):
    jc.queue.put(i)
jc.join()
