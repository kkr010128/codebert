x = int(input())
y = x
if x == 1:
    print('0 -1')
    exit()
v = []
for i in range(0,1001):
    v.append(i*i*i*i*i)
    v.append(i*i*i*i*i*-1)
c = 0
d = 0
for i in range(len(v)):
    y -= v[i]
    for j in range(len(v)):
        if v[j] == y * -1:
            c = i
            d = j
            break
    y = x
if c % 2 == 0: c //= 2
else:
    c = (c-1) // 2
    c *= -1
if d % 2 == 0: d //= 2
else:
    d = (d-1) // 2
    d *= -1
print(c,d)