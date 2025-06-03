k = int(input())
s = input()

if k >= len(s):
  print(s)
else :
  l_s = list(s)
  n_s = "".join(l_s[:k])+"..."
  print(n_s)