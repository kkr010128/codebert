from itertools import accumulate
n,m,k = map(int,input().split())
deskA = list(map(int,input().split()))
deskB = list(map(int,input().split()))
cumA = [0] + list(accumulate(deskA))
cumB = [0] + list(accumulate(deskB))
ans = 0
j = m
for i in range(n+1):
    if cumA[i] > k:
        continue
    while cumA[i] + cumB[j] > k:
        j -= 1
    ans = max(i+j,ans)
print(ans)