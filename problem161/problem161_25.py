a,b,n=[int(x) for x in input().rstrip().split()]
if b<=n:
  n=b-1

print(int((a*n)/b)-a*int(n/b))
