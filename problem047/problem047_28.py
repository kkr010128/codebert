s=input().split()
a=int(s[0])
b=int(s[2])
c=s[1]
while (c!='?'):
    if(c=='+'):print(a+b)
    elif(c=='-'):print(a-b)
    elif(c=='*'):print(a*b)    
    elif(c=='/'):print(int(a/b))
    s=input().split()
    a=int(s[0])
    b=int(s[2])
    c=s[1]