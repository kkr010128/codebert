#!/usr/bin/env python3
import sys

input = sys.stdin.readline


def S():
    return input().rstrip()


def I():
    return int(input())


def MI():
    return map(int, input().split())


n, k = MI()
p = list(MI())
c = list(MI())

p.insert(0, 0)
c.insert(0, 0)

ans = -float("INF")
for i in range(1, n + 1):
    next = p[i]
    score = 0
    MAX = -float("INF")

    for j in range(1, k + 1):
        score += c[next]
        MAX = max(MAX, score)
        if next == i:
            loop_score = score
            loop_size = j
            if loop_score > 0:
                q, r = divmod(k, loop_size)
                # 周れるだけ周る-1+余りの回数で最大となるマス動く
                score1 = loop_score * (q - 1) + MAX
                # 周れるだけ周る+余りの回数で最大となるマス動くとき
                score2 = loop_score * q
                MAX = score2
                next = p[i]
                for _ in range(1, r + 1):
                    score2 += c[next]
                    MAX = max(MAX, score2)
                    next = p[next]
                score = max(score1, MAX)
                break
            else:
                # 一周未満
                score = MAX
                break
        else:
            next = p[next]
    else:
        score = MAX

    ans = max(ans, score)


print(int(ans))
