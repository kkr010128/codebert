N=int(input())
a,b,c,d=0,0,0,0
for i in range(N):
  A=input()
  if A=="AC":
    a+=1
  elif A=="WA":
    b+=1
  elif A=="TLE":
    c+=1
  else:
    d+=1
print("AC x",a)
print("WA x",b)
print("TLE x",c)
print("RE x",d)