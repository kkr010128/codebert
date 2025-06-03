import sys
import queue


def solve(k):
    q = queue.Queue()
    for i in range(1, 10):
        q.put(i)
    for i in range(k):
        n = q.get()
        if i == k - 1:
            return n
        if n % 10 == 0:
            q.put(n * 10)
            q.put(n * 10 + 1)
        elif n % 10 == 9:
            q.put(n * 10 + 8)
            q.put(n * 10 + 9)
        else:
            l = n % 10
            q.put(n * 10 + l - 1)
            q.put(n * 10 + l)
            q.put(n * 10 + l + 1)


def main():
    input = sys.stdin.buffer.readline
    k = int(input())
    print(solve(k))


if __name__ == "__main__":
    main()
