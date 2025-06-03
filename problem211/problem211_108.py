join,rate=map(int,input().split())
if join>=10:
  print(rate)
else:
  print(rate+100*(10-join))