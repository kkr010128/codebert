n,m = map(int,input().split())
a = 0
n = n - 1
m = m - 1

while n > 0:
    a = a + n
    n = n - 1

while m > 0:
    a = a + m
    m = m - 1

print(a)
