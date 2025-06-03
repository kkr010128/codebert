n = int(input())
a = list(map(int,input().split()))
s = sum(a)
x = 0
m = s
for i in range(n):
    x += a[i]
    m = min(m, abs(s-x*2))
print(m)
