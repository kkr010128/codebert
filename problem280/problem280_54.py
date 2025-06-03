import itertools as it
import math
def Dist (x1,y1,x2,y2):
    dis = (x2 - x1)**2 + (y2 - y1)**2
    return math.sqrt(dis)
N = int(input())
Pos = []
res = 0
for i in range(N):
    pos = list(map(int,input().split()))
    Pos.append(pos)
array = list(it.permutations(i for i in range(N)))
for i in range(math.factorial(N)):
    for j in range(N-1):
        res += Dist(Pos[array[i][j]][0],Pos[array[i][j]][1],Pos[array[i][j+1]][0],Pos[array[i][j+1]][1])
print(res / math.factorial(N))