n = int(input())
ans = 360 / n
i = 1
while int(ans * i) != ans * i:
  i += 1
print(int(ans * i))