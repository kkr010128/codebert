import sys
import math

def check(k, w, P):
    i = 0
    for t in range(k):
        p = 0
        while p + w[i] <= P:
            p += w[i]
            i += 1
            if i == len(w):
                return True
    return False

def allocate(k, w):
    t = [0] * k
    le = 0
    ri = 100000 * 10000

    while ri - le > 1:
        P = (ri + le) / 2
        if check(k, w, P):
            ri = P
        else:
            le = P
    return ri

if __name__ == "__main__":
    w = sys.stdin.readlines()
    k = int(w[0].split()[1])
    del w[0]
    w = [int(wi) for wi in w]
    print allocate(k, w)