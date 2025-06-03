import sys

data=int(input())

h,mod=divmod(data,3600)
m,s=divmod(mod,60)

print(str(h)+":"+str(m)+":"+str(s))
