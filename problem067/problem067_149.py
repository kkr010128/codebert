n = int(input())
a, b = 0, 0
for i in range(n):
    s1, s2 = input().split()
    if s1 > s2:
        a += 3
    elif s1 == s2:
        a += 1
        b += 1
    else:
        b += 3
print('{0} {1}'.format(a, b))