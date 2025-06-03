N = int(input())
a = list(map(int, input().split()))
num = 1
cnt = 0

for i in range(N):
  if a[i] == num:
    num += 1
  else:
    cnt += 1
    
if cnt == N:
  print(-1)
else:
  print(cnt)