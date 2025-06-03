d = int(input())
c = list(map(int,input().strip().split()))
s = [list(map(int,input().strip().split())) for i in range(d)]
t = [int(input()) for i in range(d)]

last = [0]*26
sat = 0
for day,kind in enumerate(t):
  sat += s[day][kind-1]
  last[kind-1] = day+1
  for l_kind,l_day in enumerate(last):
    sat -= c[l_kind] * (day+1-l_day)
  print(sat)