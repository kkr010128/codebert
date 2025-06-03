import itertools
import math

n = int(input())

location = [list(map(int, input().split())) for _ in range(n)]

pmt = list(itertools.permutations(range(0, n)))

dis_sum = 0

for i in pmt:
    dis = 0
    for j in range(n-1):
        x1, y1 = location[i[j]]
        x2, y2 = location[i[j+1]]
        dis += math.sqrt((x1-x2)**2 + (y1-y2)**2)
    dis_sum += dis

print(dis_sum/len(pmt))



