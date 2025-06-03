import sys
input = sys.stdin.readline
# sys.setrecursionlimit(100000)


def main():
    N = int(input().strip())
    return (N//2) + N % 2


if __name__ == "__main__":
    print(main())