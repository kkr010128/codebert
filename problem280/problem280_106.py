import itertools
Row = int(input())
List = []
l=[]
for i in range (Row):
  l.append(i+1)
  List.append(list(map(int, input().split())))
x = 0
y = 0
mid = 0
p_list = list(itertools.permutations(l, Row))
for v in p_list:
  for i in range(1,Row):
    x = List[v[i]-1][0]-List[v[i-1]-1][0]
    y = List[v[i]-1][1]-List[v[i-1]-1][1]
    k = x*x+y*y
    mid += k**0.5
res = mid / len(p_list)
print(res)