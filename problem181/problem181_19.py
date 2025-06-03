# https://atcoder.jp/contests/abc161/tasks/abc161_d

import sys
# sys.setrecursionlimit(100000)
import heapq


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    n = int(input())
    if n < 10:
        print(n)
        return
    cnt = 0
    hq = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while cnt < n:
        i = heapq.heappop(hq)
        cnt += 1
        if cnt == n:
            print(i)
            return
        r = int(str(i)[::-1][0])
        heapq.heappush(hq, int(str(i) + str(r)))
        if r != 9:
            heapq.heappush(hq, int(str(i) + str(r + 1)))
        if r != 0:
            heapq.heappush(hq, int(str(i) + str(r - 1)))
    return


if __name__ == "__main__":
    main()
