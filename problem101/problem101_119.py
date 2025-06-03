a,b,c=map(int,input().split())
K=int(input())
flag=False
for i in range(10):
    for j in range(10):
        for k in range(10):
            if i+j+k<=K and 2**i*a<2**j*b<2**k*c:
                flag=True
if flag:
    print("Yes")
else:
    print("No")