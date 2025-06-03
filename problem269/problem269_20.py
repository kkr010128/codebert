t1, t2 = list(map(int, input().split()))
a1, a2 = list(map(int, input().split()))
b1, b2 = list(map(int, input().split()))

a1 *= t1
a2 *= t2
b1 *= t1
b2 *= t2

if a1 > b1:
    l1 = a1
    l2 = a2
    s1 = b1
    s2 = b2
else:
    l1 = b1
    l2 = b2
    s1 = a1
    s2 = a2


if l1 + l2 == s1 + s2:
    print('infinity')
elif l1 + l2 < s1 + s2:
    lim = l1 - s1
    if lim % (s1+s2-l1-l2):
        print(1 + 2 * (lim // (s1+s2-l1-l2)))
    else:
        print(2 * (lim // (s1+s2-l1-l2)))
else:
    print(0)
