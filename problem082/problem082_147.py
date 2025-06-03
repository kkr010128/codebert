#!/usr/bin/env python3


def main():
    s = input()
    t = input()

    ans = float("inf")

    add = 0
    for j in range(len(s) - len(t) + 1):
        tans = 0
        for i in range(len(t)):
            if s[i + add] == t[i]:
                pass
            else:
                tans += 1
        add += 1
        ans = min(ans, tans)

    print(ans)


main()
