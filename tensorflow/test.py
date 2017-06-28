#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 13:39:18 2017

@author: llan
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tf_utils
import time

start_time = time.time()
time.sleep(5)
for step in range(100):
    tf_utils.process_record(start_time, step, 100)
