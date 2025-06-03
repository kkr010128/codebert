from math import sqrt
import itertools
N = int(input())
dis = [input().split() for i in range(N)]
lst = [x for x in range(N)]

p_lst = list(itertools.permutations(lst))

ans = 0
for i in p_lst:
    for j in range(N-1):
        ans += sqrt((int(dis[i[j]][0]) - int(dis[i[j+1]][0]))**2
                  + (int(dis[i[j]][1]) - int(dis[i[j+1]][1]))**2)

print(ans/len(p_lst))