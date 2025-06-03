import sys
import math  # noqa
import bisect  # noqa
import queue  # noqa


def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())

    que = queue.Queue()
    que.put(('a', ord('a')))

    while not que.empty():
        res, m = que.get()
        if len(res) < N:
            for i in range(ord('a'), min(ord('z'), m + 1) + 1):
                que.put((res + chr(i), max(m, i)))
        elif len(res) == N:
            print(res)
        else:
            break


if __name__ == '__main__':
    main()
