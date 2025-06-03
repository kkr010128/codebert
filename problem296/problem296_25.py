import sys

rr = lambda: sys.stdin.readline().rstrip()
ri = lambda: int(sys.stdin.readline())

s = rr()
k = ri()
cnt = 0
i = 0
if len(set(s)) == 1:
  print(int(len(s)*k/2))
  exit()
while i < len(s)-1:
  if s[i] == s[i+1]:
    cnt += 1
    i += 1
  i += 1
cnt1 = 0
i1 = 0
s *= 2
while i1 < len(s)-1:
  if s[i1] == s[i1+1]:
    cnt1 += 1
    i1 += 1
  i1 += 1
print((cnt1 - cnt)*(k-1) + cnt)

