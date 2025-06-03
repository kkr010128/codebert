#!/usr/bin/env python3
def main():
    N = int(input())
    A = [int(x) for x in input().split()]

    lst = [0] * (N + 1)
    for a in A:
        lst[a] += 1
    for i in lst[1:]:
        print(i)


if __name__ == '__main__':
    main()
