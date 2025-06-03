from time import time
from random import randint

from numba import njit
from numpy import int64

@njit('i8(i8[:], i8[:])', cache=True)
def func(s, x):
    last = [0] * 26
    score = 0
    for i, v in enumerate(x, 1):
        last[v] = i
        c = 0
        for j in range(26):
            c += s[j] * (i - last[j])
        score += s[i * 26 + v] - c
    return score

def main():
    start = time()
    d, *s = map(int, open(0).read().split())
    s = int64(s)
    x = int64(([*range(26)] * 15)[:d])
    M = func(s, x)
    while time() - start < 1.5:
        y = x.copy()
        if randint(0, 1):
            y[randint(0, d - 1)] = randint(0, 25)
        elif randint(0, 1):
            i=randint(0, d - 16)
            j=randint(i + 1, i + 15)
            y[i], y[j] = y[j], y[i]
        else:
            i = randint(0, d - 15)
            j = randint(i + 1, i + 7)
            k = randint(j + 1, j + 7)
            if randint(0, 1):
                y[i], y[j], y[k] = y[j], y[k], y[i]
            else:
                y[i], y[j], y[k] = y[k], y[i], y[j]
        t = func(s, y)
        if t > M:
            M = t
            x = y
    print(*x + 1, sep='\n')

main()