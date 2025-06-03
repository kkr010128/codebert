n=str(input())
a=list(n)
b=0
for i in a:
    b=b+int(i)

if b%9==0:
    print("Yes")
else:
    print("No")