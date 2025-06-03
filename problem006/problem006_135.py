n = int(input())
a = 100000
while n>0:
  a *= 1.05
  if a % 1000 != 0:
    a = int(a + 1000 - (a%1000))
  n -= 1
print(a)