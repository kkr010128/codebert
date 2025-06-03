n = int(input())
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ans = 'No'
for i in range(len(num)):
  for s in range(len(num)):
    if num[i] * num[s] == n:
      ans = 'Yes'
      break
print(ans)