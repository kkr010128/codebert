import itertools
import math

N=int(input())
zahyou=[list(map(int,input().split()))for i in range(N)]
jyunban=list(itertools.permutations(range(N)))
dist=list()
for i in range(len(jyunban)):
    tmp=0
    for j in range(N-1):
        tmp+=math.sqrt((zahyou[jyunban[i][j]][0]-zahyou[jyunban[i][j+1]][0])**2+(zahyou[jyunban[i][j]][1]-zahyou[jyunban[i][j+1]][1])**2)
    dist.append(tmp)
print(sum(dist)/math.factorial(N))