import itertools

n,m,q = map(int, input().split())
list_ = [list(map(int, input().split())) for _ in range(q)]

num=1
seed = [[i] for i in range(1,m+1)]
while num!=n:
  num+=1
  tmp_list = []
  while seed:
    tmp = seed.pop()
    for i in range(tmp[-1],m+1):
      tmp_list.append(tmp+[i])
  seed = tmp_list.copy()

max_score = 0
visited = set()
for arr in seed:
  score = 0
  for arr_2 in list_:
    if arr[arr_2[1]-1] - arr[arr_2[0]-1] == arr_2[2]:
      score+=arr_2[3]
      max_score = max(max_score, score)
print(max_score)