import math , sys

N , M = list(map( int, input().split() ))

cor = 0
pen = 0

F = [False]*N
C = [0]*N

for i in range(M):
    A , B = list( input().split() )
    A = int(A)-1

    if B == "WA" and not F[A]:
        C[A]+=1

    #print(C)

    if B == "AC" and not F[A]:
        F[A] = True
        cor += 1
        pen +=C[A]
print(cor,pen)