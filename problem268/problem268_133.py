# E - Colorful Hats 2
MOD = 10**9+7
N = int(input())
A = list(map(int,input().split()))
count = [0]*N+[3]
used = [0]*(N+1)
ans = 1
for x in A:
    ans = (ans*(count[x-1]-used[x-1]))%MOD
    count[x] += 1
    used[x-1] += 1
print(ans)