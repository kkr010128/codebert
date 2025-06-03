N,A,B=map(int,input().split())
if N == (N//(A+B))*(A+B):
    print(N-(N//(A+B))*(B))
elif (N//(A+B))*(A+B)<N <= (N//(A+B))*(A+B)+A:
    print(N-(N//(A+B))*(B))
else:
    print((N//(A+B)+1)*(A))



