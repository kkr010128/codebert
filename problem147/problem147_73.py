name=input()
len_n=len(name)
name2=input()
len_n2=len(name2)
 
if name==name2[:-1] and len_n+1==len_n2:
  print("Yes")
else:
  print("No")