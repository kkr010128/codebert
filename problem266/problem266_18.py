X=int(input())
maisu_max=X//100
if X<100:
    print(0)
    exit()
else:
    X=str(X)
    X=int(X[-2:])
    if X==0:
        print(1)
        exit()
ans=100
for i in range(2):
    for j in range(2):
        for k in range(2):
            for l in range(2):
                for m in range(20):
                    tmp=i+j*2+k*3+l*4+m*5
                    if tmp==X:
                        if i+j+k+l+m<ans:
                            ans=i+j+k+l+m
if maisu_max>=ans:
    print(1)
else:
    print(0)
