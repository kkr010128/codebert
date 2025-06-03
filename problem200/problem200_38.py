a,b,m = map(int, input().split())
aprice = list(map(int, input().split()))
bprice = list(map(int, input().split()))
c = sorted(aprice)
d = sorted(bprice)
e = c[0]+d[0]
f  =0
for i in range(m):
  x,y,k = map(int, input().split())
  f =aprice[x-1]+bprice[y-1]-k
  if(e>f):
    e = f
print(e)