N=int(input())
if N%1000==0:
    Q=N//1000
else:
    Q=N//1000+1
W=Q*1000-N
print(W)
