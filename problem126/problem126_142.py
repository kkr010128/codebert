x1,x2,x3,x4,x5 = map(int,input().split())
P=[x1,x2,x3,x4,x5]
for i in range(5):
    if P[i]==0:
        print(str(i+1))
    else:
        continue