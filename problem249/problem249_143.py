import sys
input = sys.stdin.readline


def main():
    a, b, k = map(int, input().split())
    if a >= k:
        print(a-k, b)
        return
    if a+b >= k:
        k -= a
        print(0, b-k)
        return
    if a+b < k:
        print(0, 0)
        return


if __name__ == "__main__":
    main()
