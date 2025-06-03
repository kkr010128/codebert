#!/usr/bin/env python3

from math import ceil
import heapq

def main():
    n, d, a = map(int, input().split())
    q = []
    for i in range(n):
        x, h = map(int, input().split())
        heapq.heappush(q, (x, -ceil(h / a)))
    bomb = 0
    res = 0
    while q:
        x, h = heapq.heappop(q)
        if h < 0:
            h *= -1
            if h > bomb:
                heapq.heappush(q, (x + 2 * d, h - bomb))
                res += h - bomb
                bomb = h
        else:
            bomb -= h
    print(res)

if __name__ == "__main__":
    main()
