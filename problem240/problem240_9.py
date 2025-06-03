N,M = map(int, input().split())
flag = [False]*N
ac = wa = 0
wal = [0]*N

for i in range(M):
  p, s = input().split()
  if s == "AC":
    if flag[int(p)-1] == False:
      ac+=1
      wa+=wal[int(p)-1]
      flag[int(p)-1] = True
  if s == "WA":
    if flag[int(p)-1] == False:
      wal[int(p)-1]+=1

print(ac,wa)