import sys
from collections import defaultdict


def input():
    return sys.stdin.readline().rstrip()


def main():
    T1, T2 = map(int, input().split())
    A1, A2 = map(int, input().split())
    B1, B2 = map(int, input().split())

    len1 = T1 * A1 + T2 * A2
    len2 = T1 * B1 + T2 * B2
    first1 = T1 * A1
    first2 = T1 * B1
    second1 = T2 * A2
    second2 = T2 * B2

    if len1 == len2:
        print("infinity")
        exit()

    if len1 > len2:
        if first1 < first2:
            a, b = divmod(first2 - first1, len1 - len2)
            if b == 0:
                print(a * 2)
                exit()
            else:
                print(a * 2+1)
                exit()
        else:
            print(0)
            exit()

    if len2 > len1:
        if first2 < first1:
            a, b = divmod(first1 - first2, len2 - len1)
            if b == 0:
                print(a * 2 )
                exit()
            else:
                print(a * 2+1)
                exit()
        else:
            print(0)
            exit()



if __name__ == "__main__":
    main()
