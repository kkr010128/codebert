A,B,M=map(int,input().split())
*a,=map(int,input().split())
*b,=map(int,input().split())
xyc = [tuple(map(int,input().split())) for _ in range(M)]

ans = min(a)+min(b)
for i in range(M):
  x,y,c=xyc[i]
  ans = min(ans,a[x-1]+b[y-1]-c)
  
print(ans)