import sys
s=0
N=int(input())
if N%2==1:
  print(0)
  sys.exit()
N=N//2
while True:
  N=N//5
  s+=N
  if N==0:
    break
print(s)