N,D = map(int, input().split())
ans = 0

for i in range(N):
    p,q = map(int, input().split())
    if (p**2+q**2)**0.5 <= D:
        ans += 1
print(ans)