#!/usr/bin/env python3
def main():
    _ = int(input())
    P = [int(x) for x in input().split()]

    res = P[0]
    ans = 0
    for p in P:
        if p <= res:
            ans += 1
            res = p
    print(ans)


if __name__ == '__main__':
    main()
