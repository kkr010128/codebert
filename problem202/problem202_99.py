N,A,B=map(int,input().split())
if A==0:
    print("0")
elif B==0:
    print(N)
elif N%(A+B)>A:
    print(A*int(N/(A+B))+A)
else:
    print(A*int(N/(A+B))+N%(A+B))