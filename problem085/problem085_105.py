n = int(input())
s = list(map(int, input().split()))
s.sort()

A = max(s)
dp = [0] * (A + 1)

for ss in s:
    dp[ss] += 1

pairwise = True
setwise = True

for i in range(2, A + 1):
    cnt = 0
    for j in range(i, A + 1, i):
        cnt += dp[j]
    if cnt > 1:
        pairwise = False
    if cnt == n:
        setwise = False
        break

if pairwise:
    print("pairwise coprime")
elif setwise:
    print("setwise coprime")
else:
    print("not coprime")
