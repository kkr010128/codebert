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
        pos_ = []
        neg_ = []
        for x in a:
            if x >= 0:
                pos_.append(x)
            else:
                neg_.append(x)
        pos = deque(sorted(pos_, reverse=True))
        neg = deque((sorted(neg_)))
        while len(que) < k:
            if len(pos) >= 2:
                pp = pos[0] * pos[1]
            else:
                pp = -1
            if len(neg) >= 2:
                np = neg[0] * neg[1]
            else:
                np = -1
            if (pp > np) or len(que) == (k-1):
                que.append(pos.popleft())
            else:
                que.append(neg.popleft())
                que.append(neg.popleft())

    while len(que) > 1:
        que.append(que.popleft() * que.popleft())

    print(que.popleft() % MOD)


if __name__ == '__main__':
    main()
