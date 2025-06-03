n = int(input())
xl = [list(map(int, input().split())) for i in range(n)]
lr = list(map(lambda x:[x[0]-x[1], x[0]+x[1]], xl))
lr.sort(key=lambda x:x[1])
#print(lr)
limit = lr[0][1]
ans=n
for i in range(1, n):
  if lr[i][0]<limit:
    ans-=1
  else:
    limit=lr[i][1]
print(ans)