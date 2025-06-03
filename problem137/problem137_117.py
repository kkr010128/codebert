import sys


def main():
    input = sys.stdin.buffer.readline
    n = int(input())
    ab = [map(int, input().split()) for _ in range(n)]
    a, b = [list(i) for i in zip(*ab)]
    new_a = sorted(a)
    new_b = sorted(b)
    if n % 2 == 1:
        min_m = new_a[(n + 1) // 2 - 1]
        max_m = new_b[(n + 1) // 2 - 1]
        print((max_m - min_m) + 1)
    else:
        min_m = (new_a[n // 2 - 1] + new_a[n // 2])
        max_m = (new_b[n // 2 - 1] + new_b[n // 2])
        print((max_m - min_m) + 1)


if __name__ == '__main__':
    main()
