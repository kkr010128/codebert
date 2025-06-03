import numpy as np
from collections import Counter
from math import sqrt
from time import time


def main():
    N = int(input())
    np_a_o = list([int(x) for x in input().split()])
    np_a = Counter(np_a_o)

    np_a_keys = set(np_a.keys())

    div_list = set()
    key_max = max(np_a_keys)

    c = 0

    for key in np_a_keys:
        for div in range(key*2, key_max+1, key):
            div_list.add(div)

    r = np_a_keys - div_list

    u, count = np.unique(np.array(np_a_o), return_counts=True)
    r -= set(u[count > 1])

    print(len(r))


if __name__ == '__main__':
    main()
