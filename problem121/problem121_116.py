n = int(input())

ans = []

while n > 0:
  n -= 1
  k = n % 26
  n = n // 26
  ans.append(chr(ord('a') + k))

for j in reversed(range(len(ans))):
  print(ans[j], end = '')