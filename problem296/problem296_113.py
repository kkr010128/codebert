from itertools import accumulate, permutations, combinations, combinations_with_replacement, groupby, product
# import math
# import numpy as np  # Pythonのみ！
# from operator import xor
# import re
# from scipy.sparse.csgraph import connected_components  # Pythonのみ！
# ↑cf.  https://note.nkmk.me/python-scipy-connected-components/
# from scipy.sparse import csr_matrix
# import string
import sys

sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():
    S = list(input())
    K = int(input())
    l = []
    cnt = 0
    if len(S)==1:
        print(K//2)
    else:
        gr = groupby(S)
        for key, group in gr:
            l.append(list(group))
        if len(l)==1:
            print(len(S)*K//2)
        else:
            for i in range(len(l)):
                cnt += len(l[i]) // 2
                
            if l[0][0] == l[-1][0]:
                dev = len(l[0]) // 2 + len(l[-1]) // 2 - (len(l[-1]) + len(l[0])) // 2
            else:
                dev = 0
            print(cnt * K - dev * (K - 1))


resolve()