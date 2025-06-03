#d=日数, c=満足低下度, s=満足上昇度, t=コンテストの日程 
d = int(input())
c = list(map(int, input().split()))
s = [list(map(int, input().split())) for i in range(d)]
t = [int(input()) for j in range(d)]
last = [0 for i in range(26)]
#print(c)
res = 0
count = 0
#while count != len(t):
for day in range(d):
  res += s[day][t[day]-1]
  last[t[day]-1] = day+1
  #print(last)
  #print(c[last[t[day]-1]])
  for i in range(26):
    #print(c[i] * (day + 1 - last[i]))
    res -= c[i] * (day + 1 - last[i])
  print(res)
