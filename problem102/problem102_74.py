tmp = (input().split(' '))
n = int(tmp[0])
k = int(tmp[1])
tmp = input().split(' ')
map_tmp = map(int,tmp)
grades = list(map_tmp)
j = k
while j < n:
  curr_res = grades[j]
  prev_res = grades[j-k]
  if curr_res > prev_res:
    print('Yes')
  else:
    print('No')
  
  j+=1