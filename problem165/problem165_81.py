import sys


def input():
    return sys.stdin.readline().rstrip()


def main():
    n = int(input())
    items = {input() for _ in range(n)}
    print(len(items))


if __name__ == "__main__":
    main()