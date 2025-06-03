n=int(input())
p =list(map(int,input().split()))
ans = 0
x = p[0]
for i in range(n):
    if x >= p[i]:
        ans +=1
        x = p[i]

print(ans)