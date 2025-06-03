m=[0]*50
f=[0]*50
r=[0]*50
result=[""]*50

num=0
while True:
  a,b,c=map(int,input().split())
  if a == b == c ==-1:
    break
  else:
    m[num],f[num],r[num]=a,b,c
  num+=1

for i in range(num):
  if m[i] == -1 or f[i]==-1:
    result[i]="F"
  elif m[i]+f[i]>=80:
    result[i]="A"
  elif m[i]+f[i]>=65:
    result[i]="B"
  elif m[i]+f[i]>=50:
    result[i]="C"
  elif m[i]+f[i]>=30:
    if r[i] >=50:
      result[i]="C"
    else:
      result[i]="D"
  else:
    result[i]="F"

for i in range(num):
  print(result[i])
