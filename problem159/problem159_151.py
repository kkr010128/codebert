X = int(input())
M = 100
y = 0
while X > M:
  M += M//100
  y += 1
print(y)