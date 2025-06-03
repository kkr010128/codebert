r=input().split()
A=int(r[0])
B=int(r[1])
K=int(r[2])
if K>=A+B:
    print("0 0")
elif K>=A:
    print("0 "+str(B-K+A))
else:
    print(str(A-K)+" "+str(B))