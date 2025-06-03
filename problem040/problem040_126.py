abc = input().split()
a = int(abc[0])
b = int(abc[1])
c = int(abc[2])
# 12
if a > b:
  a, b = b, a
# 13
if a > c:
  a, c = c, a
# 23
if b > c:
  b, c = c, b
print("{0} {1} {2}".format(a, b, c))