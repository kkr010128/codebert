tbl = [[0,4,2,5,3,0],[3,0,6,1,0,4],[5,1,0,0,6,2],\
       [2,6,0,0,1,5],[4,0,1,6,0,3],[0,3,5,2,4,0]]
num = (input().split())
ite = int(input())
for i in range(ite):
    T,F = map(int,input().split())
    Tin = num.index(str(T))
    Fin = num.index(str(F))
    print(num[tbl[Fin][Tin]-1])
