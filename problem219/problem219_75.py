s=input()[::-1]+'0'
d=[0,1]
for c in s:
    x=int(c)
    d=[x+min(d[0],1+d[1]),min(1+d[0],d[1])+9-x]
print(min(d))
