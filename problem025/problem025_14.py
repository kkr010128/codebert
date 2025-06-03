import sys


input = sys.stdin.readline


def make_sum_set(i, v):
    if i == N:
        S.add(v)
        return
    else:
        make_sum_set(i+1, v)
        make_sum_set(i+1, v+A[i])


def main():
    make_sum_set(0, 0)
    for m in M:
        if m in S:
            print("yes")
        else:
            print("no")


if __name__ == "__main__":
    N = int(input())
    A = [int(a) for a in input().split()]
    Q = int(input())
    M = [int(m) for m in input().split()]
    S = set()
    main()
