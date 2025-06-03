l,r,d = map(int,input().split())
a = r // d
b = l // d
ans = a - b
c = r % d
e = l % d
if c == 0 and e == 0:
  print(ans + 1)
else:
  print(ans)