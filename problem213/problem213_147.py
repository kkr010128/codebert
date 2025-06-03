n = int(input())
x = list(map(int, input().split()))
m = 10**9
for i in range(min(x),max(x)+1):
    t = 0
    for h in x:
        t += (h-i)**2
    if t < m:
        m = t
print(m)