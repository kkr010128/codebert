#!/usr/bin/env python

def main():
    N = int(input())
    D = list(map(int, input().split()))
    ans = 0
    for i in range(N-1):
        d1 = D[i]
        for d2 in D[i+1:]:
            ans += d1 * d2

    print(ans)

if __name__ == '__main__':
    main()
