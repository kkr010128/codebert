import sys
read = sys.stdin.read
readlines = sys.stdin.readlines

from math import ceil
def main():
    n, k = map(int, input().split())
    a = tuple(map(int, input().split()))

    def kaisu(long):
        return(sum([ceil(ae/long) - 1 for ae in a]))

    def bs_meguru(key):
        def isOK(index, key):
            if kaisu(index) <= key:
                return True
            else:
                return False
        ng = 0
        ok = max(a)
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if isOK(mid, key):
                ok = mid
            else:
                ng = mid
        return ok
    print(bs_meguru(k))

if __name__ == '__main__':
    main()

