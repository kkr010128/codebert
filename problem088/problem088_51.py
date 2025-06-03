N = int(input())
A = map(int, input().split())

curr = 0
ans = 0
for a in A:
  if curr > a:
    ans += curr - a
  else:
    curr = a
print(ans)