import sys

input = sys.stdin.readline

N, K = map(int, input().split())
A = sorted(list(map(int, input().split())))
F = tuple(map(int, input().split()))


def can_eat(t):
    F_time = sorted([t // f for f in F])
    training = 0
    for i in range(N):
        training += max(0, A[i] - F_time[i])
    return training <= K


# bisect
l, r = -1, 10 ** 12
while r - l > 1:
    m = (r + l) // 2
    if can_eat(m):
        r = m
    else:
        l = m
print(r)
