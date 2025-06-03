r=input().split()
a=int(r[0])
b=int(r[1])
if a>=b:
    ans=""
    for i in range(a):
        ans+=str(b)
    print(int(ans))
else:
    ans=""
    for i in range(b):
        ans+=str(a)
    print(int(ans))