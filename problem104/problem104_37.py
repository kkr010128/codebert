L, R, D = map(int, input().split())
counter = 0
for i in range(L, R + 1):
  if i % D == 0:
    counter+= 1
print(counter)