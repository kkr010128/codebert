n = int(input())
lis=[]
for _ in range(n):
    x,l = map(int,input().split())
    lis.append([x+l,x-l])

lis.sort()

m = -(10**9+7)
ans = 0

for i in range(n):
    a ,b = lis[i]
    if m <= b:
        ans += 1
        m = a
    
print(ans)
