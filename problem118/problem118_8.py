N=int(input())
out=0
for X in range(1,N+1):
    Y=N//X
    out+=Y*(Y+1)*X/2
print(int(out))