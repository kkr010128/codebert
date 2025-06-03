# 152 B

a, b = input().split()

s1 = a * int(b)
s2 = b * int(a)

if s1 <= s2:
    print(s1)
elif s1 > s2:
    print(s2)