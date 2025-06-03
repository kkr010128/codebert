n,m=map(int,input().split())

if m == 0:
  print(0,0)
  exit(0)

results=[]
for i in range(n+1):
  results.append([0,0])
  
ac = 0
wa = 0
memo = [0]*(n+1)
for i in range(m):
  p,s=input().split()
  p = int(p)
  s = s.strip()

  if memo[p] != -1:
    if s == 'WA':
      memo[p] += 1
    else:
      ac += 1
      wa += memo[p]
      memo[p] = -1

print(ac,wa)