n = int(input())
p = list(map(int,input().split()))
c = 0
m = 10**9
for i in range(n):
    if p[i] < m:
        m = p[i]
        c += 1
        
print(c)