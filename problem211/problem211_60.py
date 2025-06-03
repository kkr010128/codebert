inp=list(map(int,input().strip().split()))[:2]
n,r=inp[0],inp[1]
if(n <= 9):
  print(100*(10-n)+r)
else:
  print(r)
