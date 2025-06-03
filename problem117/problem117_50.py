from itertools import accumulate
n,m,k = map(int,input().split())
deskA = list(map(int,input().split()))
deskB = list(map(int,input().split()))
cumA = list(accumulate(deskA))
cumB = list(accumulate(deskB))
cumA = [0] + cumA
cumB = [0] + cumB
ans = 0
l = m
for i in range(n+1):
    tmp = k - cumA[i]
    if tmp<0:
        continue
    j = l
    tmp -= cumB[j]
    while tmp < 0:
        tmp += cumB[j]
        j -= 1
        tmp -= cumB[j]
    l = j
    ans = max(i+j,ans)
print(ans)