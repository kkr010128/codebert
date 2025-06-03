N,X,T = map(int,input().split())
Y = int(N/X)
A = N%X
print( Y*T if A == 0 else Y*T + T )