abef=0
bbef=1
s=input()
for i in range(len(s)):
  curr=int(s[len(s)-1-i])
  a=abef+curr
  b=bbef+9-curr
  a=min(a,1+bbef+curr)
  b=min(b,abef+10-curr)
  abef=a
  bbef=b
curr=0
a=abef+curr
b=bbef+9-curr
a=min(a,1+bbef+curr)
b=min(b,abef+10-curr)
print(min(a,b))