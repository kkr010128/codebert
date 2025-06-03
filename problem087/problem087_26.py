str=input()
l=len(str)
n=0
while l>0:
    n=n+int(str[l-1])
    l=l-1
if n%9 == 0:
    print("Yes")
else :
    print("No")

