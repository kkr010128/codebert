a = 100
x = int(input())
count = 0

while a < x:
  a = a + a // 100
  count += 1

print(count)