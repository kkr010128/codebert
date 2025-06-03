X = int(input())
k = 0
res = 100
for i in range (1, 4200):
  res += res // 100
  if res >= X:
    k = i
    break
print(k)