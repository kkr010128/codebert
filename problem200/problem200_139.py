a,b,m = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
ret = 2**60
for _ in range(m):
  x,y,c = map(int,input().split())
  x -= 1
  y -= 1
  ret = min(ret, A[x]+B[y]-c)
print( min(ret, min(A)+min(B)) )
