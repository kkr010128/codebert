import sys
input = sys.stdin.readline


def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    for a1, a2 in zip(A[:-k], A[k:]):
        if a1 < a2:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
