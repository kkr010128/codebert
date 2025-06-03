# -*- coding: utf-8 -*-

import sys
import os
import math


while True:
    N = int(input())
    if N == 0:
        break
    scores = list(map(float, input().split()))
    n = len(scores)
    mean = sum(scores) / n

    variance = 0
    for score in scores:
        variance += (score - mean) ** 2
    variance /= n

    print(math.sqrt(variance))