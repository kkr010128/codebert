n = int(input())
a = list(map(int,input().split()))
cur = 0
cnt = 0
for v in a:
  if v == cur+1:
    cur = v
    cnt += 1
if cnt==0:
  print(-1)
else:
  print(len(a)-cnt)