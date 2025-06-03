# -*- coding: utf-8 -*-

def main():

    S = input()
    T = input()

    n = len(S)

    ans = 0

    for i in range(n):
        if S[i] != T[i]:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()