from collections import defaultdict

N = int(input())
a = list(map(int, input().split()))
llst = [0] * N
rlst = [0] * N

for i in range(N - 1):
    llst[i] = (i + 1) + a[i]
    rlst[-i - 1] = (N - i) - a[-i - 1]

d = defaultdict(int)
for i in range(1, N):
    d[rlst[i]] += 1

cnt = 0
for i in range(N - 1):
    cnt += d[llst[i]]

print(cnt)