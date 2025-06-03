import math

N , M = map(int,input().split())#N:展望台の数、M:道の数
H = list(map(int,input().split()))#H:高さの配列

AB = [map(int, input().split()) for _ in range(M)]
A , B = [list(i) for i in zip(*AB)]

G = [1] * N #展望台の数

for i in range (M):
    if H[ A[i] -1 ] > H[B[i] -1 ]:
        G[ B[i] -1 ] = 0
    elif H[ A[i] -1] == H[ B[i] -1 ]:
        G[ A[i] -1 ] = 0
        G[ B[i] -1 ] = 0
    else:
        G[A[i] -1 ] = 0

print( G.count(1) )