n,m = map(int, input().split())
shukudai = sum(list(map(int,input().split())))
  
if n >= shukudai:
  print(n-shukudai)
else:
  print(-1)