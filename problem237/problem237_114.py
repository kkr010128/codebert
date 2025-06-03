n=int(input())
rng = [[] for _ in range(n)]
for i in range(n):
  x,l=map(int,input().split())
  rng[i] = [x-l,x+l]
rng.sort(key=lambda y:y[1])
cnt=0
t_mx=-(10**10)
for i in range(n):
  if t_mx > rng[i][0]:
    cnt += 1
  else:
    t_mx = rng[i][1]
print(n-cnt)