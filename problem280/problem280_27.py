import math
import itertools

n = int(input())
l = list(range(n))

pos_list =[list(map(int, input().split())) for _ in range(n)]

ans = 0 
def clc_distandce(a,b):
    [x1, y1] = a
    [x2, y2] = b
    dist = math.sqrt((a[0] - b[0])**2 + (a[1]-b[1])**2)
    return dist


for i in itertools.permutations(l,n):
    #print(i)
    #print(list(i)[0])
    for k in range(1,n):
        dist = clc_distandce(pos_list[list(i)[k]],pos_list[list(i)[k-1]])
        ans += dist
    #print(ans)
    #print()
    
print(ans/math.factorial(n))