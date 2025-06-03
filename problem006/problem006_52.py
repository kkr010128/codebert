# -*- coding: utf-8 -*-

import sys
from math import ceil

for line in sys.stdin.readlines():
    List = map(int, line.strip().split())
    
    n = List[0]
    yen = 100000
    for i in xrange(n):
        yen *= 1.05
        yen = int(ceil(yen/1000)) * 1000
    print yen