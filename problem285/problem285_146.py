s=input()
a,b,c,d=0,0,0,0
for i in range(len(s)):
 if s[i]==">":
  c=0;b+=1
  if b<=d:a+=b-1
  else:a+=b
 else:b=0;c+=1;a+=c;d=c
print(a)