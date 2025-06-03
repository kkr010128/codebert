X = int(input())
m = 100
a = 0

while m < X:
  m = m + m // 100
  a += 1
print(a)