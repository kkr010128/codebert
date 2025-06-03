import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from collections import deque
    import bisect
    n, k = map(int, readline().split())
    a = list(map(int, readline().split()))
    a.sort()
    que = deque()

    if n == k:
        que.extend(a)
    elif a[-1] < 0 and k % 2 == 1:
        que.extend(a)
        for _ in range(n - k):
            que.popleft()
    else:
        b = [[] for _ in range(n)]
        for i in range(n):
            b[i] = [abs(a[i]), a[i]]
        b.sort(reverse=True)
        b = deque(b)
        que1 = deque()
        que2 = deque()
        sign = 1

        for i in range(k):
            val_abs, val = b.popleft()
            if val > 0:
                que1.append(val_abs)
            elif val < 0:
                que2.append(val_abs)
                sign *= -1
            else:
                print(0)
                return

        if sign == -1:
            add1, add2 = 0, 0
            rmv1, rmv2 = 10 ** 19, 10 ** 19
            if que1:
                rmv1 = que1[-1]
                for x_abs, x in b:
                    if x < 0:
                        add1 = x_abs
                        break
            if que2:
                rmv2 = que2[-1]
                for x_abs, x in b:
                    if x > 0:
                        add2 = x_abs
                        break

            if add1 == add2:
                print(0)
                return

            if add1 * rmv2 > add2 * rmv1:
                que2.append(add1)
                que1.pop()
            else:
                que1.append(add2)
                que2.pop()

        que.extend(que1)
        que.extend(que2)

    while len(que) > 1:
        que.append(que.popleft() * que.popleft())

    print(que.popleft() % MOD)


if __name__ == '__main__':
    main()
