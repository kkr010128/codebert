def root(x, root_ls):
  if root_ls[x] < 0:
    return x
  else:
    root_ls[x] = root(root_ls[x], root_ls)
    return root_ls[x]

def unite(a, b, root_ls):
  a = root(a, root_ls)
  b = root(b, root_ls)
  if a != b:
    root_ls[a] += root_ls[b]
    root_ls[b] = a
  
n, m = list(map(int, input().rstrip().split(" ")))
members = [-1 for i in range(n)]
max_idx = 0
for mm in range(m):
  a, b = list(map(int, input().rstrip().split(" ")))
  unite(a-1, b-1, members)
print(max([-m for m in members]))
