k = int(input())
a,b = [int(a) for a in input().split()]
c=0
for i in range (a,b+1):
  if i%k!=0:
    c+=1
if c==b-a+1:
  print("NG")
else:
  print("OK")      