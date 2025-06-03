from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    a, b = map(int, input().split())
    print(max(0, a - 2 * b))


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
