a,b,c,d,e,f=map(int,input().split())
x=input()
for i in range(len(x)):
    if x[i]=="S":
        a,b,c,d,e,f=e,a,c,d,f,b
    if x[i]=="E":
        a,b,c,d,e,f=d,b,a,f,e,c
    if x[i]=="N":
        a,b,c,d,e,f=b,f,c,d,a,e
    if x[i]=="W":
        a,b,c,d,e,f=c,b,f,a,e,d
print(a)
