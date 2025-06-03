X,Y=map(int,input().split())
b=0

for i in range(X+1):
    if 4*(i)+2*(X-i)==Y:
            b+=1
        
if not b==0:
    print("Yes")
else:
    print("No")