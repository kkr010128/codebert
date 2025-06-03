S=int(input())
a,s=divmod(S,60)
h,m=divmod(a,60)
print(str(h)+':'+str(m)+':'+str(s))
