from itertools import accumulate


def LS():
    return list(input().split())


N = int(input())
title = []
time = []
for _ in range(N):
    s, t = LS()
    time.append(int(t))
    title.append(s)
time.append(0)
Tsum = list(accumulate(time))
X = input()
for i in range(N):
    if title[i] == X:
        break
print(Tsum[N]-Tsum[i])