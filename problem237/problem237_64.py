n = int(input())
a = []
for i in range(n):
    x,l = map(int,input().split())
    s = x-l
    g = x+l
    a.append((s,g))

a = sorted(a, reverse=False, key=lambda x: x[1]) 
tmp = a[0][1]
ans = 1
for i in range(1,len(a)):
    if tmp <= a[i][0]:
        tmp = a[i][1]
        ans += 1 

print(ans)