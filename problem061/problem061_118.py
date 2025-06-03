s=input()
res=''
for i in s:
  if i.islower():
    i=i.upper()
  elif i.isupper():
    i=i.lower() 
  res+=i
print(res)
