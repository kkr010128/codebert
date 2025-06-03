import sys
from time import time
from random import randint

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
    d, *s = map(int, sys.stdin.buffer.read().split())
    x = ([*range(26)] * 15)[:d]
    M = func(s, x)
    while time() - start < 1.8:
        y = x.copy()
        if randint(0, 1):
            y[randint(0, d - 1)] = randint(0, 25)
        elif randint(0, 1):
            i = randint(0, d - 16)
            j = randint(i + 1, i + 15)
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
    for t in x:
        print(t + 1)

if __name__ == '__main__':
    main()