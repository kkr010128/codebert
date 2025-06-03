import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
#import numpy as np
from collections import Counter
def main():
    n, *a = map(int, read().split())
    if 1 in a:
        count1 = a.count(1)
        if count1 == 1:
            print(1)
            sys.exit()
        else:
            print(0)
            sys.exit()
    maxa = max(a)
    seq = [0] * (maxa + 1)
    ac = Counter(a)
    for ae in ac.items():
        if ae[1] == 1:
            seq[ae[0]] = 1
    for ae in a:
        t = ae * 2
        while t <= maxa:
            seq[t] = 0
            t += ae
    r = sum(seq)
    print(r)

if __name__ == '__main__':
    main()
