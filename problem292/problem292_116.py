N=int(input())
d=list(map(int, input().split()))

ans=0

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        elif i < j:
            ans += d[i]*d[j]
print(ans)