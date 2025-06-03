#!/usr/bin/env python3
import sys
input = sys.stdin.readline

def main():
    N = [0] + list(map(int, tuple(input().rstrip("\n"))))
    Ncopy = N.copy()
    ans = 0

    flag = False
    for i in range(len(N)-1, 0, -1):
        if (Ncopy[i] <= 4) or (Ncopy[i] == 5 and N[i-1] <= 4):
            ans += Ncopy[i]
            flag = False
        else:
            Ncopy[i-1] += 1
            if not flag:
                ans += 10 - N[i]
            else:
                ans += 9 - N[i]
            Ncopy[i] = 0
            flag = True

    if Ncopy[0] == 1:
        ans += 1

    print(ans)

if __name__ == "__main__":
    main()
