n = int(input())
a_list = [int(i) for i in input().split()]
a_dict = {}
for a in a_list:
  if a in a_dict:
    a_dict[a] += 1
  else:
    a_dict[a] = 1
q = int(input())
si = 0
for a in a_dict:
  si += a * a_dict[a]
for _ in range(q):
  bi, ci = [int(i) for i in input().split()]
  if not bi in a_dict:
    print(si)
    continue
  if not ci in a_dict:
    a_dict[ci] = 0
  a_dict[ci] += a_dict[bi]
  si += (ci - bi) * a_dict[bi]
  a_dict[bi] = 0
  print(si)