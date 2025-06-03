import sys
import copy
import math
import bisect
import pprint
import bisect
from functools import reduce
from copy import deepcopy
from collections import deque

def lcm(x, y):
    return (x * y) // math.gcd(x, y)

if __name__ == '__main__':
    s = input()
    s = s.replace("hi","")

    if s =="":
        print("Yes")
    else:
        print("No")
