n,r=map(int,input().split())
inn=0
if n<10:
  inn=100*(10-n)
  print(r+inn)
else:
  print(r)