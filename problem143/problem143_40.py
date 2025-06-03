k = int(input())
s = input()
a = list(s.split())
if len(s) <= k:
  print(s)
elif len(s) > k:
  print((s[0:k] + '...'))