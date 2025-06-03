n = int(input())
a = list(map(int, input().split()))
b = 0
c = 0

for i in range(n):
    b = max(b,a[i])
    c += (b-a[i])

print(c)