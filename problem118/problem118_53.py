n = int(input())

ans = 0
for i in range(1, n + 1):
  for j in range(1, n//i + 1):
    if i * j <= n:
      ans += i * j
    else:
      break
      
print(ans)