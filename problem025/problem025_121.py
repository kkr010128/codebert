#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import print_function,division
import time
import sys
import io
import re
import math
start = time.clock()
i = 0

sys.stdin.readline()
a=[int(s) for s in sys.stdin.readline().split()]
sys.stdin.readline()
ms=[int(s) for s in sys.stdin.readline().split()]
ans=set([0])
for i in a:
    ans|=set(j+i for j in ans)
ans=list(ans)
for jk in ms:
    if jk in ans: print('yes')
    else: print('no')