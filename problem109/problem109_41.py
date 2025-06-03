a=int(input())
b=[input() for i in range(a)]
c=0
d=0
e=0
f=0
for i in range(a):
  if b[i]=="AC":
    c=c+1
  if b[i]=="WA":
    d=d+1
  if b[i]=="TLE":
    e=e+1
  if b[i]=="RE":
    f=f+1
print("AC","x",c)
print("WA","x",d)
print("TLE","x",e)
print("RE","x",f)