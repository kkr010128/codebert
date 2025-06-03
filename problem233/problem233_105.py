N = int(input())
P = [p for p in map(int,input().split())]

ans = 0
min_p = P[0]

for p in P:
    if min_p >= p:
        min_p = p
        ans += 1

print(ans)