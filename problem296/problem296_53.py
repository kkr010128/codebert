# https://atcoder.jp/contests/agc039/tasks/agc039_a

s = list(input())
k = int(input())


i = 0
a = 0

while i < len(s):
  if i == len(s) - 1:
    break
  if s[i] == s[i+1]:
    a += 1
    i += 2
  else:
    i += 1
else:
  print(a * k)
  exit()
  
i = -1
b = 0

while i < len(s):
  if i == len(s) - 1:
    print(a + b * (k - 1))
    exit()
  if s[i] == s[i + 1]:
    b += 1
    i += 2
  else:
    i += 1
else:
  print(a * ((k + 1) // 2) + b * ((k - 1) // 2))
  exit()