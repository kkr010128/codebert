import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
from math import ceil
def main():
    n, k, *a = map(int, read().split())
    def isOK(x):
        kaisu = 0
        for ae in a:
            kaisu += ceil(ae / x) - 1
        if kaisu <= k:
            return True
        else:
            return False
    ng = 0
    ok = max(a)
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if isOK(mid):
            ok = mid
        else:
            ng = mid
    print(ok)

if __name__ == '__main__':
    main()
