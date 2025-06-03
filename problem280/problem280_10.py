import math
import itertools
n = int(input())
xy = []
for i in range(n):
  xy.append(list(map(int,input().split())))


total_distance = 0
list_keiro = []
for team in itertools.permutations(range(n)):
    list_keiro.append(team)

def distance(x1,x2,y1,y2):
  return (math.sqrt((x1-x2)**2 + (y1-y2)**2))

for i in list_keiro:
  dis_tmp = 0
  for j in range(n-1):
    dis_tmp += distance(xy[i[j]][0],xy[i[j+1]][0],xy[i[j]][1],xy[i[j+1]][1])
  total_distance += dis_tmp

print(total_distance / len(list_keiro))