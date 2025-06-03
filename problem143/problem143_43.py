k = int(input())
s = list(input())

if len(s) <= k:
  print("".join(s[0:]))
else:
  print(str("".join(s[0:k])) + "...")