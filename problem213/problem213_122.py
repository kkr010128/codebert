n=int(input())
l = [int(x) for x in input().split()]
p = int(sum(l)/n + 0.5)
ans = 0
for i in range(n):
    ans += (p-l[i])**2
    
print(ans)