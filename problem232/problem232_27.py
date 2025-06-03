a,b=map(int,input().split())
x=''
if a<b:
    for i in range(b):
        x+=str(a)
elif a>b:
    for i in range(a):
        x+=str(b)
elif a==b:
    for i in range(a):
        x+=str(a)
print(x)