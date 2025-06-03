import sys

s = sys.stdin.readline().rstrip()
k = int(sys.stdin.readline())
cnt = 0
i = 0
l = len(s)
if len(set(s)) == 1:
  print(int(l*k/2))
  exit()
while i < l-1:
  if s[i] == s[i+1]:
    cnt += 1
    i += 2
    continue
  i += 1
cnt1 = 0
i1 = 0
s *= 2
while i1 < l*2-1:
  if s[i1] == s[i1+1]:
    cnt1 += 1
    i1 += 2
    continue
  i1 += 1
print((cnt1 - cnt)*(k-1) + cnt)

