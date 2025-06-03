import sys

A, B = (int(x) for x in input().split())
num=0
while int(num*0.08)<=A:
  if int(num*0.08)==A and int(num*0.1)==B:
    print(num)
    sys.exit(0)
  num+=1
print(-1)