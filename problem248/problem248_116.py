def stringconcant(S,T):
     a=S 
     b=T
     c=a+b
     return c

S,T = input().split()
a = stringconcant(T,S)
print(a)