import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
from collections import defaultdict
def main():
    n, k, *a = map(int, read().split())

    cur_town = 0
    transits = set()
    tran_time = defaultdict(int)
    cnt = 0
    while True:
        if k == 0:
            print(cur_town + 1)
            sys.exit()
        if cur_town in transits:
            break
        else:
            transits.add(cur_town)
            tran_time[cur_town] = cnt
            cur_town = a[cur_town] - 1
            cnt += 1
            k -= 1
    k2 = k % (cnt - tran_time[cur_town])
    while k2 > 0:
        k2 -= 1
        cur_town = a[cur_town] - 1
    print(cur_town + 1)

if __name__ == '__main__':
    main()