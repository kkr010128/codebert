n = int(input())
a = list(map(int,input().split()))
cnt = 0
for v in a:
  if v == cnt+1:
    cnt += 1
print(-1 if cnt==0 else n-cnt)