n = int(input())
P = list(map(int,input().split()))


S={}
ans="YES"
for p in P:
    if p in S:
        ans = "NO"
        break
    else:
        S[p]=1

print(ans)

