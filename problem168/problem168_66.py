import sys


def main():
    input = sys.stdin.buffer.readline
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))
    for a in a_list:
        n -= a
        if n < 0:
            break
    print(n if n >= 0 else -1)


if __name__ == '__main__':
    main()
