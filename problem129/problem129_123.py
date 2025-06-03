from collections import Counter

N = int(input())
A = [int(i) for i in input().split()]
num = set(A)
count = Counter(A)
dp = [True] * (10**6 + 1)

for a in num:
    for n in range(a+a, 10**6+1, a):
        dp[n] = False

ans = 0
for a in num:
    if count[a] == 1 and dp[a] == True:
        ans += 1

print(ans)