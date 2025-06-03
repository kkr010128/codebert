N=int(input())
if N%1000==0:
  print("0")
else:
  n=((N-(N%1000))/1000)+1
  print(int((1000*n)-N))