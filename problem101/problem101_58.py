a,b,c=map(int, input().split())
k=int(input())
mink=0
while a>=b:
    b*=2
    mink+=1
while b>=c:
    c*=2
    mink+=1
if mink<=k:
    print("Yes")
else:
    print("No")
#print(mink,a,b,c)