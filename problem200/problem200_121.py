A, B, M=map(int, input().split())
a=list(map(int, input().split()))
b=list(map(int, input().split()))
c = [list(map(int, input().split())) for i in range(M)]

# とりあえず最小
minc=min(a)+min(b)

for v in c:
  minc = min(minc, (a[v[0]-1]+b[v[1]-1]-v[2]))

print(minc)