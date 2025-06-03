n,k = map(int,input().split())
a = list(map(int,input().split()))
b = [0] * n
c = ['Y'] * n
c[0] = 'N'
x = 0
y = 1
while x != k:
    c[y-1] = 'N'
    x += 1
    y = a[y-1]
    b[x-1] = y
    if c[y-1] == 'N':
        break
if x != k:
    y = b.index(a[y-1])
    k -= x
    k %= (x-y)
    c = b[y:x]
    print(c[k-1])
else:
    print(y)