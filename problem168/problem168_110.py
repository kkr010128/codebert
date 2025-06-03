N,M=map(int,input().split())
A=[int(x) for x in input().split()]
print(max(-1,(N-sum(A))))