n,d = map(int,input().split())
ans = 0
for i in range(n):
    x1,y1 = map(int,input().split())
    if(d*d >= x1*x1+y1*y1):
        ans += 1
print(ans)
