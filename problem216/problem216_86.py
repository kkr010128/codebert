a,b,c = map(int,input().split())
h = set([a,b,c])
if(len(list(h))==2):
  print("Yes")
else:
  print("No")