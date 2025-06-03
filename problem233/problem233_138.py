N = int(input())
P = list(map(int,input().split()))
mini = N+1
cnt = 0
for i in P:
  if mini > i:
    cnt += 1
    mini = i
print(cnt)