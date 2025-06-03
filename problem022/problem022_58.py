#!/usr/bin/env python
# -*- coding:utf-8 -*-
#from __future__ import print_function
import time
import sys
import io
import re
import math
start = time.clock()
i = 0
m=int(raw_input())
n=map(int, raw_input().split())
o=int(raw_input())
p=map(int, raw_input().split())
for j in xrange(o):
    if int(p[j]) in n: i+=1
print i