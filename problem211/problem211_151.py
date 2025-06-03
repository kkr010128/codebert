n,r=map(int,input().split())
res = r
if n < 10:
  res += 100 * (10 - n)
print(res)