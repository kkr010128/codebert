A, B, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = min(a)+min(b)
for i in range(M):
    c, d, e = map(int, input().split())
    ans = min(ans, a[c-1]+b[d-1]-e)
print(ans)
    
