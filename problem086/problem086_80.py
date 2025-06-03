import math
import numpy as np
import numba
from numba import njit, b1, i4, i8, f8
from numba import jit
import collections
import bisect
from collections import deque
from copy import copy, deepcopy
import time
 
def main():
    N,X,T = map(int,input().split())
    print(math.ceil(N/X) * T)

if __name__ == '__main__':
    main()