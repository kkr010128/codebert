N = int(input())
P = list(map(int,input().split()))
P_min = []
a = 200000
ans = 0

for i in range(N):
    if a >= P[i]:
        ans += 1
        a = P[i]

print(ans)