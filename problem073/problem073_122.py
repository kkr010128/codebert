n = int(input())
res = 0
for i in range(1,n+1):
  for j in range(1,n+1):
    if i*j < n:
      res += 1
    else:
        break
print(res)