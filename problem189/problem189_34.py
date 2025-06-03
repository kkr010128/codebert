import math
N,M=map(int,input().split())
al=math.factorial(N+M)/(math.factorial(2)*math.factorial(N+M-2))
di=N*M
print(int(al)-int(di))