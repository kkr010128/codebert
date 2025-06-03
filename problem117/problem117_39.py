import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
from itertools import accumulate
from bisect import bisect
def main():
    n, m, k = map(int, input().split())
    a = tuple(map(int, input().split()))
    b = tuple(map(int, input().split()))

    aa = [0] + list(accumulate(a))
    ba = [0] + list(accumulate(b))
    r = 0
    for i1, aae in enumerate(aa):
        if aae > k:
            break
        else:
            time_remain = k - aae
            b_num = bisect(ba, time_remain)
            r = max(r, i1 + b_num - 1)
    print(r)

if __name__ == '__main__':
    main()