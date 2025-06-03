n = int(input())
al = list(map(int, input().split()))

ans = 0
for i in range(n-1):
    if al[i] >= al[i+1]:
        ans += al[i]-al[i+1]
        al[i+1] += (al[i]-al[i+1])

print(ans)