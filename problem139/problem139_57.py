# import sys
# readline = sys.stdin.readline
# generator = (readline().strip() for _ in range(N))

# N, M = map(int, input().split())
# As = list(map(int, input().split()))
# queries = (input() for _ in range(N))


def solve():
    h1, m1, h2, m2, k = map(int, input().split())

    period = (h2-h1)*60 + (m2-m1)
    return period - k


def main():
    print(solve())


if __name__ == "__main__":
    main()
