h,w,n = int(input()),int(input()),int(input())
ans = 0
s = 0
while s < n:
  s += max(h,w)
  ans += 1
print(ans)