# -*- coding: utf-8 -*-

def main():

    A, B, C, K = map(int, input().split())

    ans = 0

    if K <= A:
        ans = K

    else:
        if K <= A + B:
            ans = A

        else:
            ans = A + (-1 * (K - A - B))

    print(ans)


if __name__ == "__main__":
    main()