N,M = map(int,input().split())
ac = (N+1)*[0]
wa = (N+1)*[0]
pt = 0
for i in range(M):
  p,s = input().split()
  p = int(p)
  if ac[p] == 0 and s == "AC":
    ac[p] = 1
    pt += wa[p]
  wa[p] += 1
print(sum(ac),pt)  
