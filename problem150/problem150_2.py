n, k = map(int, input().split())
lst = [int(i) for i in input().split()]

tele_lst = []
town_set = set()
town = 1
while True:
  if town not in town_set:
    tele_lst.append(town)
    town_set.add(town)
  else:
    break
  town = lst[town - 1]
ind = tele_lst.index(town)
length = len(town_set)
circle = length - ind
#print(ind, length)
#print(tele_lst)
if k < ind:
  town = tele_lst[k]
  print(town)
else:
  k -= ind
  k %= circle
  #print(k)
  town = tele_lst[ind + k]
  print(town)