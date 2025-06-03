m = 100000
n = int(input())
while n > 0:
  n -= 1
  m = m + (m * 5 // 100)
  m = ((m-1) // 1000 + 1) * 1000
print(m)
