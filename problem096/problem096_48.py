N,D = map(int,input().split())
ans = 0
for i in range(N):
    X1,Y1 = map(int,input().split())
    if X1*X1+Y1*Y1 <= D*D:
        ans += 1
print(ans)