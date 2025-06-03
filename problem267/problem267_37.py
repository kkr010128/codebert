N = int(input())
S = str(input())
R = S[::-1]

ans = 0
for i in range(1000):
  z = str(i).zfill(3)
  right = -1
  left = -1
  if z[2] in R:
    r = R.index(z[2]) + 1
    right = N-r
  else:
    continue
  if z[0] in S:
    left = S.index(z[0]) + 1
  else:
    continue
  if z[1] in S[left:right]:
    ans += 1
print(ans)
