tmp = [int(e) for e in input().split()]

a = tmp[0]
b = tmp[1]
c = tmp[2]
d = tmp[3]

res = a * c

tmp = a * d

if tmp > res:
    res = tmp

tmp = b * c

if tmp > res:
    res = tmp

tmp = b * d

if tmp > res:
    res = tmp

print(res)
