import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
import numpy as np
def main():
    n, *a = map(int, read().split())

    p = np.array(a)
    minp = np.minimum.accumulate(p)
    r = 0
    for i1, ae in enumerate(a):
        r += minp[i1] >= ae

    print(r)

if __name__ == '__main__':
    main()
