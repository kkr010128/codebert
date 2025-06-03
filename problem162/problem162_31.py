n, m = map(int, input().split())
def check_ans(list_pairs):
  dict_people = {i: i for i in range(1, n+1)}
  for i in range(n):
    for k in range(m):
      val1 = dict_people[list_pairs[k][0]]
      val2 = dict_people[list_pairs[k][1]]
      if val1>val2:
        print(val2, val1, end=" / ")
      else:
        print(val1, val2, end=" / ")
    print("")
    for j in range(1, n+1):
      dict_people[j] = (dict_people[j]+1)%n
      if dict_people[j] == 0: dict_people[j] = n
ans = list()
if n%2 == 1:
  for i in range(m):
    node1 = (1-i)%n
    if node1 == 0: node1 = n
    node2 = 2+i
    ans.append((node1, node2))
else:
  distance = -1
  node2 = 1
  for i in range(m):
    node1 = (1-i)%n
    if node1 == 0: node1 = n
    node2 = node2+1
    distance += 2
    if distance == n//2 or distance == n//2 + 1:
      node2 += 1
    ans.append((node1, node2))
[print(str(values[0])+" "+str(values[1])) for values in ans]
# check_ans(ans)