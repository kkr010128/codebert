H = int(input())
count = 0
ans = 0
while H>1:
  H = H//2
  ans += 2**count
  count += 1
ans += 2**count
print(ans)