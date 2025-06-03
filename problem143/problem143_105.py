k = int(input())
s = str(input())

if len(s) <= k:
  print(s)
elif len(s) > k:
  print(s[:k] + '...')