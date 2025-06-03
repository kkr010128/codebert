def convert(s): 
  
    # initialization of string to "" 
    new = "" 
  
    # traverse in the string  
    for x in s: 
        new += x  
  
    # return string  
    return new 
s=input()
n=len(s)
a=[]
for i in range(n):
  if s[i]=='P':
    a.append('P')
  else:
    a.append('D')
print(convert(a))