d=int(input())
c=list(map(int,input().split()))
sa=[list(map(int,input().split())) for _ in range(d)]
last=[-1]*26
ty=[int(input())-1 for _ in range(d)]
sat=0
for day,i in enumerate(ty):
  last[i]=day
  sat+=sa[day][i]
  for j in range(26):
    sat-=c[j]*(day-last[j])
  print(sat)
  

"""
18398
35037
51140
65837
79325
"""