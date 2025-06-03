s = int(input())
a = b = 0; c = int(s > 2)
for _ in range(s - 3):
  a, b, c = b, c, a + c
print(c % (10**9 + 7))
