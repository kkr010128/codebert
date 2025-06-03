n = int(input())

r = -10000000000
y = int(input())

m = y
x = y

for i in range(1, n):
    x = int(input())
    if r < (x - m):
        r = (x - m)

    if x < m:
        m = x

print(r)