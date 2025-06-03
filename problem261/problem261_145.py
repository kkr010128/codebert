s = input()
n = len(s)
ans = 0
if (n%2 == 0):
  nh = int(n/2)
  for i in range(nh):
    if (s[i] != s[n - i - 1]):
      ans = ans + 1
else:
  nh = int((n - 1)/2)
  for i in range(nh):
    if (s[i] != s[n - i - 1]):
      ans = ans + 1
print(ans)