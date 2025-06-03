N,K = map(int,input().split())
count = N//K
N = abs( N - count*K )
N_2 = abs( N - K )
print( N if N <= N_2 else N_2 )