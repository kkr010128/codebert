#!/usr/bin/env python3
def main():
    from math import gcd

    N = int(input())
    A = []
    INF = 10 ** 6 + 5
    frequency = [0] * INF
    for a in [int(x) for x in input().split()]:
        A.append(a)
        frequency[a] += 1
    
    pairwise = True
    for i in range(2, INF):
        cnt = 0
        for j in range(i, INF, i):
            cnt += frequency[j]
        if cnt > 1:
            pairwise = False
    if pairwise:
        print("pairwise coprime")
        return

    g = 0
    for i in range(N):
        g = gcd(g, A[i])
        if g == 1:
            print('setwise coprime')
            return
    
    print('not coprime')


if __name__ == '__main__':
    main()
