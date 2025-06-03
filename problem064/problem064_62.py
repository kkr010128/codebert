import sys

s = list(input())
p = list(input())
for i in range(len(s)):
  counter = 0
  for j in range(len(p)):
    m = (i+j)%len(s)
    if s[m] == p[j]:
      counter += 1
  if counter == len(p):
    print('Yes')
    sys.exit()
print('No')
