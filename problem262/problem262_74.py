import itertools

n = int(input())
lst = []
for _ in range(n):
  m = int(input())
  lst_s = []
  for _ in range(m):
    evi = list(map(int, input().split()))
    lst_s.append(evi)
  lst.append(lst_s)
#print(lst)

truth = [0, 1]
all_lists = list(itertools.product(truth, repeat=n))
#print(all_lists)
max_count = 0
for each in all_lists:
  flag = True
  count = 0
  #print(each)
  for i in range(n):
    trust = each[i]
    #print(trust)
    evis = lst[i]
    for evid in evis:
      #print(evid)
      person_ind = evid[0] - 1
      person_trust = evid[1]
      if trust == 1:
        if person_trust != each[person_ind]:
          flag = False
          break
    if not flag:
      break
    if trust == 1:
      count += 1
  if (count > max_count) and flag:
    max_count = count
print(max_count)