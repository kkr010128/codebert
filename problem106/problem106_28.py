if __name__ == '__main__':
    # import time
    from sys import stdin
    # from collections import defaultdict
    # from collections import deque
    # from collections import Counter
    from copy import deepcopy
    # import numpy as np
    from numpy import random as np_random
    # import math
    import random
    input = stdin.readline

    ans_list = [0]*60001
    for x in range(1, 101):
        for y in range(1, 101):
            for z in range(1, 101):
                n = x**2+y**2+z**2+x*y+y*z+z*x
                ans_list[n] += 1

    n = int(input())
    for i in range(1, n+1):
        print(ans_list[i])

