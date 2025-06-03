n = int(input())
P = list(map(int, input().split()))
cnt = 0
m = P[0]
for p in P:
    if m >= p:
        cnt += 1
        m = p
print(cnt)
