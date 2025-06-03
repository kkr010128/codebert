a,b = map(int,input().split())
q = list()
for i in range(1009):
  if int(i*0.08) == a and int(i*0.1) == b:
    q.append(i)

if len(q) == 0:
  print(-1)
  exit()
print(min(q))
