n = int(input())
d = list(map(int, input().split()))

m = 1
num = 0
for s in range(0,n-1):
    for t in range(m,n):
        num += (d[s]*d[t])
    m += 1
print(num)  