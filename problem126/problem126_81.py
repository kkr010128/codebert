x = list(map(int, input().split()))
if 0 in x:
  ans = x.index(0) + 1
print(ans)