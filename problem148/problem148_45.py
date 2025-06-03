a,b,c,k = map(int, input().split())
goukei = 0
if k>=a:
  k -= a
  goukei += a
else:
  goukei += k
  k = 0
if k>=b:
  k -= b
else:
  k = 0
if k>0:
  goukei -= k
  
print(goukei)