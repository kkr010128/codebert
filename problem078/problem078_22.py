n=int(input())
m=10**9+7
print((pow(10,n,m)-pow(9,n,m)*2+pow(8,n,m))%m if n!=1 else 0)
