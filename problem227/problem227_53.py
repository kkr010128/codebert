n,k = map(int,input().split())
h = list(map(int,input().split()))
m = sorted(h,reverse=True)
if n <= k:
  print(0)
  exit()

q = sum(m[k:n])
print(q)