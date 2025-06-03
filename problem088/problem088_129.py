n = int(input())
a = list(map(int, input().split()))

x = 0
m = a[0]

for i in range(n):
    if a[i] < m:
        x += m - a[i]
    else:
        m = a[i]
    
print(x)
