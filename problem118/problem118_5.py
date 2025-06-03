n=int(input())
li = [0]*(n+5)
for i in range(1,n+1):
    for j in range(i,n+1,i):
        li[j] += 1
ans = 0
for i in range(1,n+1):
    ans += i*li[i]
print(ans)
