n = int(input())
a = list(map(int,input().split()))
m = max(a) + 1
li = [0]*m 
for x in a:
    li[x] += 1
ans = 0
for i in range(1,m):
    if li[i]: 
        if li[i]==1: 
            ans += 1 
        for j in range(i,m,i): 
            li[j] = 0
print(ans)