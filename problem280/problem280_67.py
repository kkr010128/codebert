#C - Average Length
import math
import itertools
N = int(input())
town = []
for i in range(N):
    x,y = map(int,input().split())
    town.append((x,y))

def dist(A,B):
    return math.sqrt((A[0]-B[0])**2 + (A[1]-B[1])**2)
route = list(itertools.permutations(town))
tot = 0
for i in route:
    for j in range(len(i)-1):
        tot += dist(i[j],i[j+1])
ave = tot/len(route)
print(ave)