import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
import numpy as np
def main():
    n, *a = map(int, read().split())

    p = np.array(a)
    minp = np.minimum.accumulate(p)
    r = np.count_nonzero(minp >= p)
    print(r)

if __name__ == '__main__':
    main()