import sys


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    a = str(readline().rstrip().decode('utf-8'))
    print("A" if a.isupper() else "a")


if __name__ == '__main__':
    solve()
