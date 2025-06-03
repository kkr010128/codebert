n = int(input())
A = [0]+list(map(int,input().split()))

d = {}

ans = 0
for i in range(1,n+1):
    if i+A[i] not in d:
        d[i+A[i]] = 1
    else:
        d[i+A[i]] += 1
    if i-A[i] in d:
        ans += d[i-A[i]]
        
print(ans)