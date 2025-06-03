N,M = map(int,input().split())
print((str(N)*M,str(M)*N)[N > M])