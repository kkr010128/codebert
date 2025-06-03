x, k, d = map(int, input().split())

# k回　dだけ変化

n=abs(x)//d
if k>=n:
  k=k-n
else:
  n=k
  k=0
  
if k%2 == 0:
  x=abs(x)-d*n
else:
  x=abs(x)-d*(n+1)

print(abs(x))