n = int(input())
ph = 0
pl = 10**10
mh = -10**10
ml = 10**10
for _ in range(n):
  x,y = map(int,input().split())
  ph = max(ph,x+y)
  pl = min(pl,x+y)
  mh = max(mh,x-y)
  ml = min(ml,x-y)
print(max(ph-pl,mh-ml))