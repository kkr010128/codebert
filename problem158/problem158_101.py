k=int(input())
a,b = map(int,input().split())

ans="NG"
for i in range(1001):
    if a<=(i*k)<=b :
        ans = "OK"
print(ans)