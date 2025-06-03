import itertools
import functools
import math
from collections import Counter
from itertools import combinations
import re


N,R=map(int,input().split())

if N >= 10:
    print(R)
else:
    print( R + ( 100 * ( 10 - N )))
