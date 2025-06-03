t1, t2 = map(int,input().split())
a1, a2 = map(int,input().split())
b1, b2 = map(int,input().split())

a1 = t1*a1
a2 = t2*a2
b1 = t1*b1
b2 = t2*b2

if (a1 + a2) == (b1 + b2):
    print('infinity')
    exit(0)

elif (a1 + a2) > (b1 + b2):
    a1, b1 = b1, a1
    a2, b2 = b2, a2
if b1 > a1:
    print(0)
    exit(0)

tmp00 = a1 - b1
tmp01 = b1 + b2 - a1 - a2

ans = tmp00 // tmp01 * 2 + 1
if tmp00 % tmp01 == 0:
    ans -= 1

print(ans)