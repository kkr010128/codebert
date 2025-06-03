N=int(input())
mod=10**9+7
print((pow(10,N,mod)-pow(9,N,mod)-pow(9,N,mod)+pow(8,N,mod))%mod)
