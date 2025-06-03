n, k = map(int, input().split())
p = sorted(list(map(int, input().split())))

a = 0

for i in range(k):
    a += p[i]
    
print(a)
