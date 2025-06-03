n = int(input())
MOD = 1000000007
 

ans = pow(10,n,MOD) - pow(9,n,MOD) - pow(9,n,MOD) + pow(8,n,MOD) 
print((ans+MOD)%MOD)