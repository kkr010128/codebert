#152_B
a, b = map(int, input().split())

s1 = ''
for i in range(a):
    s1 = s1 + str(b)

s2 = ''
for i in range(b):
    s2 = s2 + str(a)

if s1 < s2:
    print(s1)
else:
    print(s2)