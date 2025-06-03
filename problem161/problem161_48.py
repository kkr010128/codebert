import sys
input = sys.stdin.readline
# sys.setrecursionlimit(100000)


def main():
    A, B, N = [int(i) for i in input().strip().split()]
    ans = 0
    if N >= B:
        if A >= B:
            n = range(B - 1, N + 1, B)[-1]
        else:
            n = range(B - 1, N + 1, B)[0]
        ans = ((A * n) // B) - (A * (n // B))
    else:
        ans = ((A * N) // B) - (A * (N // B))
    return ans


if __name__ == "__main__":
    print(main())
