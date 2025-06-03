import itertools

n, m, q = map(int, input().split())
lst = []
for _ in range(q):
  l = [int(i) for i in input().split()]
  lst.append(l)

lists = list(itertools.combinations_with_replacement(range(1, m+1), n))
#print(lists)
max_point = 0
for each in lists:
  point = 0
  for i in range(q):
    l = lst[i]
    a = l[0] - 1
    b = l[1] - 1
    c = l[2]
    if each[b] - each[a] == c:
      point += l[3]
  if point > max_point:
    max_point = point
print(max_point)