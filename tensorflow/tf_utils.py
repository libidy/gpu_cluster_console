#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 13:39:18 2017

@author: llan
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import time

def get_cluster_spec():
    return eval(os.environ.get("CLUSTER_SPEC"))

def get_job_name():
    return os.environ.get("JOB_NAME")

def get_task_index():
    return int(os.environ.get("TASK_INDEX"))

def process_record(starttime,step,max_step):
    step = step + 1
    if (step != 0  and step % 10 == 0) or (step == max_step):
        duration = time.time() - starttime
        process = step*1.0/max_step*100
        lasting = duration/step * (max_step-step)
        with open('task_record.txt', 'w') as wf:
            print('step:%d\trunning time:%.2f s\tprocess:%.2f%%\tremaining time:%.2f s\n' %(step,duration,process,lasting))
            wf.write('%.2f\t%.2f\t%.2f' %(duration,process,lasting))
    
