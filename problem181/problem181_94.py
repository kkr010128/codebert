import sys
from collections import deque

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    K = int(readline())

    queue = deque(range(1, 10))
    for _ in range(K):
        n = queue.popleft()

        tail = n % 10
        n10 = n * 10
        if tail == 0:
            queue.append(n10 + tail)
            queue.append(n10 + tail + 1)
        elif tail == 9:
            queue.append(n10 + tail - 1)
            queue.append(n10 + tail)
        else:
            queue.append(n10 + tail - 1)
            queue.append(n10 + tail)
            queue.append(n10 + tail + 1)

    print(n)
    return


if __name__ == '__main__':
    main()
